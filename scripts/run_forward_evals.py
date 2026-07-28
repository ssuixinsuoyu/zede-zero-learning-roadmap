from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "zede-zero-learning-roadmap"
CASES_PATH = ROOT / "evals" / "cases.json"
JUDGE_SCHEMA = ROOT / "evals" / "judge-schema.json"
DEFAULT_RESULTS = ROOT / "evals" / "runs"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run isolated forward evaluations against the local Skill."
    )
    parser.add_argument(
        "--case",
        action="append",
        dest="case_ids",
        help="Run one case id. Repeat to select multiple cases.",
    )
    parser.add_argument(
        "--severity",
        choices=("hard", "quality", "all"),
        default="all",
        help="Filter cases by severity when --case is omitted.",
    )
    parser.add_argument("--limit", type=int, help="Run at most this many selected cases.")
    parser.add_argument("--model", help="Optional model override passed to codex exec.")
    parser.add_argument(
        "--codex-bin",
        help="Path to codex executable. Defaults to codex.cmd or codex on PATH.",
    )
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=DEFAULT_RESULTS,
        help="Directory for raw responses, judge results, and summary.json.",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=240,
        help="Timeout in seconds for each agent or judge call.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate selection and print the run plan without calling a model.",
    )
    return parser.parse_args()


def load_cases() -> tuple[dict, list[dict]]:
    payload = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    cases = payload.get("cases")
    if not isinstance(cases, list):
        raise ValueError("evals/cases.json has no valid cases list")
    return payload, cases


def select_cases(cases: list[dict], args: argparse.Namespace) -> list[dict]:
    by_id = {case["id"]: case for case in cases}
    if args.case_ids:
        missing = [case_id for case_id in args.case_ids if case_id not in by_id]
        if missing:
            raise ValueError(f"Unknown case ids: {', '.join(missing)}")
        selected = [by_id[case_id] for case_id in args.case_ids]
    else:
        selected = [
            case
            for case in cases
            if args.severity == "all" or case["severity"] == args.severity
        ]
    if args.limit is not None:
        if args.limit <= 0:
            raise ValueError("--limit must be greater than zero")
        selected = selected[: args.limit]
    if not selected:
        raise ValueError("No cases selected")
    return selected


def find_codex(explicit: str | None) -> str:
    if explicit:
        path = Path(explicit)
        if not path.is_file():
            raise FileNotFoundError(f"Codex executable not found: {path}")
        return str(native_codex_for(path))
    discovered = shutil.which("codex.cmd") or shutil.which("codex")
    if not discovered:
        raise FileNotFoundError(
            "Codex executable not found. Pass --codex-bin with an explicit path."
        )
    return str(native_codex_for(Path(discovered)))


def native_codex_for(path: Path) -> Path:
    if sys.platform != "win32" or path.suffix.lower() not in {".cmd", ".ps1"}:
        return path
    vendor = (
        path.parent
        / "node_modules"
        / "@openai"
        / "codex"
        / "node_modules"
        / "@openai"
        / "codex-win32-x64"
        / "vendor"
        / "x86_64-pc-windows-msvc"
        / "bin"
        / "codex.exe"
    )
    if vendor.is_file():
        return vendor
    raise FileNotFoundError(
        "Found the Windows Codex launcher but not its native executable. "
        "Upgrade the Codex CLI or pass --codex-bin with codex.exe."
    )


def skill_digest() -> str:
    digest = hashlib.sha256()
    for path in sorted(SKILL_DIR.rglob("*")):
        if path.is_file():
            digest.update(path.relative_to(SKILL_DIR).as_posix().encode("utf-8"))
            digest.update(b"\0")
            digest.update(path.read_bytes())
            digest.update(b"\0")
    return digest.hexdigest()


def agent_prompt(case: dict, isolated_skill: Path) -> str:
    turns = "\n".join(
        f"用户第 {index} 条消息：{turn}"
        for index, turn in enumerate(case["turns"], start=1)
    )
    return f"""使用位于 {isolated_skill} 的本地 Skill 回应下面的用户状态。
先完整读取 SKILL.md，并只按其中条件读取直接引用的 references。
不要检查父目录、测试文件、评判标准或其他仓库内容。
把多条消息视为同一段对话中按顺序出现的用户消息；已有状态描述视为已经发生。
只输出此刻应该给用户的回复，不解释测试过程，不评价 Skill。

{turns}
"""


def judge_prompt(case: dict, response: str) -> str:
    return f"""你是严格的 Skill 行为评审。只依据给定案例评判回复，不补全回复没有表达的内容。

案例：
{json.dumps(case, ensure_ascii=False, indent=2)}

待评回复：
---BEGIN RESPONSE---
{response}
---END RESPONSE---

判定规则：
1. expected 中的每一项都必须在语义上满足。
2. forbidden 中任何一项出现都算失败。
3. severity=hard 时，遗漏任何 expected 或触发任何 forbidden 都写入 hard_gate_failures。
4. severity=quality 时，把问题写入 quality_issues；只要存在实质遗漏，pass=false。
5. 不因文风、措辞差异或额外无害说明扣分。
6. summary 用一句中文说明结论。
"""


def codex_command(
    codex_bin: str,
    cwd: Path,
    output_path: Path,
    model: str | None,
    schema: Path | None = None,
) -> list[str]:
    command = [
        codex_bin,
        "exec",
        "--ephemeral",
        "--skip-git-repo-check",
        "--sandbox",
        "read-only",
        "--color",
        "never",
        "-C",
        str(cwd),
        "--output-last-message",
        str(output_path),
    ]
    if model:
        command.extend(("--model", model))
    if schema:
        command.extend(("--output-schema", str(schema)))
    command.append("-")
    return command


def run_codex(command: list[str], prompt: str, timeout: int) -> None:
    completed = subprocess.run(
        command,
        input=prompt,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        timeout=timeout,
        check=False,
    )
    if completed.returncode != 0:
        details = completed.stderr.strip() or completed.stdout.strip()
        if "requires a newer version of Codex" in details:
            details += (
                "\nThe configured model is newer than this Codex CLI. "
                "Upgrade the CLI or pass --model with a model supported by this CLI."
            )
        raise RuntimeError(
            f"Codex exited with status {completed.returncode}: {details[-2000:]}"
        )


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
    args = parse_args()
    payload, cases = load_cases()
    selected = select_cases(cases, args)
    codex_bin = find_codex(args.codex_bin)

    print(f"Selected {len(selected)} case(s):")
    for case in selected:
        print(f"- {case['id']} [{case['severity']}]")
    print(f"Skill SHA-256: {skill_digest()}")
    if args.dry_run:
        print(f"Codex executable: {codex_bin}")
        print("Dry run complete; no model calls were made.")
        return 0

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = args.results_dir.resolve() / run_id
    run_dir.mkdir(parents=True, exist_ok=False)
    results: list[dict] = []

    for index, case in enumerate(selected, start=1):
        print(f"[{index}/{len(selected)}] {case['id']}")
        case_dir = run_dir / case["id"]
        case_dir.mkdir()
        response_path = case_dir / "response.md"
        judge_path = case_dir / "judge.json"

        with tempfile.TemporaryDirectory(prefix="zede-roadmap-eval-") as temp_name:
            isolated_root = Path(temp_name)
            isolated_skill = isolated_root / SKILL_DIR.name
            shutil.copytree(SKILL_DIR, isolated_skill)

            agent_command = codex_command(
                codex_bin, isolated_root, response_path, args.model
            )
            run_codex(
                agent_command,
                agent_prompt(case, isolated_skill),
                args.timeout,
            )
            response = response_path.read_text(encoding="utf-8")

            judge_command = codex_command(
                codex_bin,
                isolated_root,
                judge_path,
                args.model,
                JUDGE_SCHEMA,
            )
            run_codex(judge_command, judge_prompt(case, response), args.timeout)
            judgment = json.loads(judge_path.read_text(encoding="utf-8"))

        results.append(
            {
                "id": case["id"],
                "severity": case["severity"],
                "pass": bool(judgment["pass"]),
                "hard_gate_failures": judgment["hard_gate_failures"],
                "quality_issues": judgment["quality_issues"],
                "summary": judgment["summary"],
            }
        )
        print(f"  {'PASS' if judgment['pass'] else 'FAIL'}: {judgment['summary']}")

    hard = [result for result in results if result["severity"] == "hard"]
    quality = [result for result in results if result["severity"] == "quality"]
    hard_rate = sum(result["pass"] for result in hard) / len(hard) if hard else 1.0
    quality_rate = (
        sum(result["pass"] for result in quality) / len(quality) if quality else 1.0
    )
    summary = {
        "run_id": run_id,
        "skill_sha256": skill_digest(),
        "selected_cases": len(results),
        "hard_pass_rate": hard_rate,
        "quality_pass_rate": quality_rate,
        "required_hard_pass_rate": payload["hard_gate_pass_rate"],
        "required_quality_pass_rate": payload["quality_threshold"],
        "passed": (
            hard_rate >= payload["hard_gate_pass_rate"]
            and quality_rate >= payload["quality_threshold"]
        ),
        "results": results,
    }
    (run_dir / "summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(
        f"Hard: {hard_rate:.0%}; quality: {quality_rate:.0%}; "
        f"overall: {'PASS' if summary['passed'] else 'FAIL'}"
    )
    print(f"Results: {run_dir}")
    return 0 if summary["passed"] else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, ValueError, RuntimeError, subprocess.TimeoutExpired) as error:
        print(f"[ERROR] {error}", file=sys.stderr)
        raise SystemExit(2)
