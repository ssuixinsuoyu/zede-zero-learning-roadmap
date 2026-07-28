from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "zede-zero-learning-roadmap"
SKILL = SKILL_DIR / "SKILL.md"
OPENAI_YAML = SKILL_DIR / "agents" / "openai.yaml"
PLANNING_PATTERNS = SKILL_DIR / "references" / "planning-patterns.md"
PROGRESS_PROTOCOL = SKILL_DIR / "references" / "progress-protocol.md"
CASES = ROOT / "evals" / "cases.json"
JUDGE_SCHEMA = ROOT / "evals" / "judge-schema.json"
FORWARD_RUNNER = ROOT / "scripts" / "run_forward_evals.py"
INSTALLER = ROOT / "scripts" / "install_cross_agent.py"
README = ROOT / "README.md"
AGENTS_ROUTER = ROOT / "AGENTS.md"
CLAUDE_ROUTER = ROOT / "CLAUDE.md"
GEMINI_ROUTER = ROOT / "GEMINI.md"
CURSOR_ROUTER = ROOT / ".cursor" / "rules" / "zede-zero-learning-roadmap.mdc"
UNIVERSAL_PROMPT = ROOT / "adapters" / "universal-prompt.md"
COMPATIBILITY_DOC = ROOT / "docs" / "cross-agent-compatibility.md"

EXPECTED_NAME = "zede-zero-learning-roadmap"
EXPECTED_TITLE = "# Zede-Zero（零）"
GOAL_TYPES = {
    "exam-certification",
    "technical-project",
    "career-transition",
    "language-expression",
    "theory-academic",
    "business-entrepreneurship",
    "exploration",
}
REQUIRED_HEADINGS = {
    "## 首次使用时说明全部规则",
    "## 展示并确认目标卡",
    "## 选择正式输出模式",
    "## 检索路线依据与资源",
    "## 输出前自我核验",
    "## 保存和恢复路线",
    "## 从反馈永久升级 Skill",
}
REQUIRED_CASES = {
    "first-use-complete-input",
    "new-vague-goal",
    "first-principles-vague-ai",
    "first-principles-clear-exam-fast-pass",
    "first-principles-business-outcome",
    "first-principles-clear-project-fast-pass",
    "self-report-conflicts-with-task",
    "diagnosis-fewer-than-three",
    "unrealistic-deadline",
    "goal-card-not-confirmed",
    "output-mode-choice",
    "layered-output-contract",
    "full-output-contract",
    "official-source-first",
    "goal-selective-official-sources",
    "network-unavailable",
    "source-conflict",
    "research-stop-when-sufficient",
    "github-star-signal",
    "stale-source-resume",
    "exam-pattern",
    "business-external-outcome",
    "exploration-sprint",
    "high-risk-boundary",
    "high-risk-general-knowledge",
    "time-budget-contract",
    "stage-remediation",
    "resume-legacy-v0",
    "resume-schema-v1",
    "resume-schema-v2",
    "resume-future-schema",
    "save-consent-every-write",
    "ordinary-feedback",
    "checkpoint-effectiveness",
    "explicit-persistent-upgrade",
    "tutoring-boundary",
    "transfer-not-imitation",
    "feedback-strongest-available",
    "delayed-retest-durable-skill",
    "exam-retest-adaptive",
    "delayed-retest-remediation",
    "exploration-no-retention-overkill",
    "no-excuse-progress",
    "blocking-gap-specific",
    "technical-project-specific-content",
    "academic-content-depth",
    "business-lean-content",
    "layered-content-not-empty",
    "language-comprehensible-input-loop",
    "language-input-not-passive",
    "language-exam-official-balance",
    "task-first-no-hoarding",
    "theory-creation-digestion",
    "high-risk-task-first-safe",
    "confirmed-context-not-recoverable",
    "cognitive-load-stage-control",
    "bottleneck-not-mechanical-pareto",
    "deliberate-practice-criteria",
    "interleaving-entry-condition",
}


def fail(message: str, failures: list[str]) -> None:
    failures.append(message)


def require_markers(text: str, markers: tuple[str, ...], label: str, failures: list[str]) -> None:
    for marker in markers:
        if marker not in text:
            fail(f"{label} lacks required marker: {marker}", failures)


def main() -> int:
    failures: list[str] = []
    required_files = (
        SKILL,
        OPENAI_YAML,
        PLANNING_PATTERNS,
        PROGRESS_PROTOCOL,
        CASES,
        JUDGE_SCHEMA,
        FORWARD_RUNNER,
        INSTALLER,
        README,
        AGENTS_ROUTER,
        CLAUDE_ROUTER,
        GEMINI_ROUTER,
        CURSOR_ROUTER,
        UNIVERSAL_PROMPT,
        COMPATIBILITY_DOC,
    )
    for path in required_files:
        if not path.is_file():
            fail(f"Missing required file: {path.relative_to(ROOT)}", failures)
    if failures:
        return report(failures)

    skill = SKILL.read_text(encoding="utf-8")
    openai_yaml = OPENAI_YAML.read_text(encoding="utf-8")
    planning = PLANNING_PATTERNS.read_text(encoding="utf-8")
    progress = PROGRESS_PROTOCOL.read_text(encoding="utf-8")
    installable_text = "\n".join((skill, openai_yaml, planning, progress))
    readme = README.read_text(encoding="utf-8")
    installer = INSTALLER.read_text(encoding="utf-8")
    routers = {
        "AGENTS.md": AGENTS_ROUTER.read_text(encoding="utf-8"),
        "CLAUDE.md": CLAUDE_ROUTER.read_text(encoding="utf-8"),
        "GEMINI.md": GEMINI_ROUTER.read_text(encoding="utf-8"),
        "Cursor rule": CURSOR_ROUTER.read_text(encoding="utf-8"),
        "universal prompt": UNIVERSAL_PROMPT.read_text(encoding="utf-8"),
    }
    compatibility = COMPATIBILITY_DOC.read_text(encoding="utf-8")

    if not re.search(rf"^name:\s*{re.escape(EXPECTED_NAME)}\s*$", skill, re.MULTILINE):
        fail("SKILL.md frontmatter name is incorrect.", failures)
    if EXPECTED_TITLE not in skill:
        fail("SKILL.md display title is incorrect.", failures)
    if len(skill.splitlines()) >= 500:
        fail("SKILL.md must remain under 500 lines.", failures)

    if "Current local version: `v1.0.0`" not in readme:
        fail("README version is not v1.0.0.", failures)
    if "从原点出发，无限逼近真知。" not in skill or "从原点出发，无限逼近真知。" not in readme:
        fail("Zede-Zero tagline is missing from SKILL.md or README.md.", failures)
    require_markers(
        readme,
        (
            "## Cross-agent compatibility",
            "Native Skill",
            "Repository router",
            "Universal prompt fallback",
            "scripts/install_cross_agent.py --target all-native --apply",
            "docs/cross-agent-compatibility.md",
        ),
        "README.md",
        failures,
    )

    canonical_path = "zede-zero-learning-roadmap/SKILL.md"
    for label, router in routers.items():
        if canonical_path not in router:
            fail(f"{label} does not route to the canonical Skill.", failures)
        if "## 使用规则" in router:
            fail(f"{label} duplicates canonical workflow content.", failures)

    require_markers(
        compatibility,
        (
            "one source of truth",
            "Native Skill",
            "Repository router",
            "Universal fallback",
            "Compatibility means the workflow can be loaded",
            "does not mean every product",
            "zede-zero-learning-roadmap-skill.zip",
        ),
        "cross-agent-compatibility.md",
        failures,
    )
    require_markers(
        installer,
        (
            '"codex": home / ".codex" / "skills" / SKILL_NAME',
            '"claude": home / ".claude" / "skills" / SKILL_NAME',
            '"shared": home / ".agents" / "skills" / SKILL_NAME',
            '"--apply"',
            "[REFUSE]",
            "hashlib.sha256",
            "tree_manifest",
            "shutil.copytree",
        ),
        "install_cross_agent.py",
        failures,
    )

    for heading in REQUIRED_HEADINGS:
        if heading not in skill:
            fail(f"Missing required section: {heading}", failures)

    onboarding = re.search(r"```markdown\s+(.*?)\s+```", skill, flags=re.DOTALL)
    if not onboarding:
        fail("Could not find the first-use rules block.", failures)
    else:
        numbers = re.findall(r"^(\d+)\.\s", onboarding.group(1), re.MULTILINE)
        if numbers != [str(number) for number in range(1, 13)]:
            fail("The first-use block must contain exactly rules 1 through 12.", failures)

    require_markers(
        skill,
        (
            "references/planning-patterns.md",
            "references/progress-protocol.md",
            "第一性原理拆解",
            "目标本质与成功证据",
            "关键结果变量",
            "不可绕过的底层能力与约束",
            "最小验证闭环",
            "快速通过",
            "分层版（`layered`）",
            "全量版（`full`）",
            "不得合并、改名或省略",
            "阶段｜时间范围与估算置信度｜必要主题与前置条件｜主动练习与产出｜验收阈值与证据｜未通过时的补救｜进入下一阶段条件",
            "计划时间不得超过总可用时间的 85%",
            "至少保留总可用时间的 15%",
            "15%–20%",
            "证据充分时立即停止",
            "GitHub 高 Star",
            "Star 数当作权威性或适用性的证明",
            "计划与实际时间、任务完成率、验收通过率",
            "### 迁移、反馈与保持",
            "目标迁移层级",
            "可获得的最强适用反馈",
            "7/30/90 天延迟复测",
            "学习交接卡",
            "## 真实性与推进义务",
            "## 展开目标相关的具体内容",
            "### 具体学习内容与项目拆解",
            "## 以做促学，避免知识囤积",
            "最小任务先行 → 暴露具体缺口 → 即时学习 → 立即应用",
            "阅读、观看、收藏和记笔记",
            "项目模块｜输入、输出与约束｜具体知识点与子技能｜实现与练习任务｜典型错误与边界情况｜测试与验收｜暂不包含",
            "不要为了显得全面",
            "已核验事实",
            "工作假设",
            "它会改变哪个决定",
            "当前上下文、路线文件或可读证据",
            "真正瓶颈并控制阶段认知负荷",
            "机械 80/20",
            "薄弱子技能、适当难度、明确标准、及时反馈、针对性修正和重试证据",
            "单项基础已经稳定且需要辨别策略时才启用交错学习",
            "不展开逐题教学、提示话术或即时纠错",
            "每次创建或更新文件前",
            "高于 v2 的文件不得覆盖",
        ),
        "SKILL.md",
        failures,
    )
    require_markers(
        planning,
        (
            *tuple(f"`{goal_type}`" for goal_type in sorted(GOAL_TYPES)),
            "## 第一性原理拆解",
            "工具、课程或证书当成目标",
            "不要把“理解底层”本身当成成果",
            "1–2 周探索冲刺",
            "方向尚未确定前不要搜索或推荐完整课程",
            "可控能力与交付物",
            "高风险领域修正",
            "来源｜等级｜支持的结论｜版本/地区｜核验日期｜访问状态｜置信度",
            "超过 30 天未核验",
            "新增材料不会改变范围、顺序、资源或验收决策时，停止检索",
            "Star 只表示关注度",
            "一般知识、历史、理论、考试常识或个人素养学习不因主题名称自动触发高风险门",
            "最多一条主线和一个辅助主题",
            "验收量表、通过阈值和所需证据",
            "未通过时的补救动作",
            "计划时间与实际时间",
            "## 学习有效性闭环",
            "## 具体内容深度",
            "宽泛主题名只能作为分组标题",
            "技术项目必须先形成模块映射",
            "商业、自媒体与探索型目标",
            "### 语言学习的高效闭环",
            "完全听不懂称为沉浸",
            "不要把“可理解输入”误写成只输入不输出",
            "考试型语言目标仍以当前官方大纲",
            "## 以做促学",
            "路线默认从最小代表任务开始",
            "没有近期应用和证据",
            "高风险目标只使用模拟、沙盒、受监督或法规允许的任务",
            "能力迁移阶梯",
            "反馈质量阶梯",
            "7 天",
            "30 天",
            "90 天",
            "教程或答案复现不能被写成“已掌握”",
            "不设置伪精确的 7/30/90 保持计划",
            "## 学习方法选择与负荷控制",
            "### 阶段认知负荷",
            "### 瓶颈优先，而非机械 80/20",
            "目标影响 × 缺口程度 × 使用频率 ÷ 时间成本",
            "### 刻意练习成立条件",
            "缺少可信反馈、明确标准或针对性修正时",
            "### 交错学习启用条件",
            "混合任务只增加难度，不产生辨别或迁移价值",
            "路线负责定义练习契约，不负责逐次出题和现场提示",
            "不受该缺口影响的部分",
            "明确说明受影响的决定",
        ),
        "planning-patterns.md",
        failures,
    )
    require_markers(
        progress,
        (
            "schema_version: 2",
            "goal_type:",
            "target_date:",
            "plan_revision:",
            "output_mode:",
            "sources_checked_on:",
            "legacy v0",
            "`schema_version: 1`",
            "`schema_version` 大于 `2`",
            "每次创建或更新前",
            "检查点效果记录",
            "第一性原理摘要",
            "具体学习内容与项目模块映射",
            "任务、暴露缺口、即时学习与产出证据",
            "迁移证据与反馈来源",
            "7/30/90 天复测记录",
            "聚焦补救",
        ),
        "progress-protocol.md",
        failures,
    )

    for reference in (PLANNING_PATTERNS, PROGRESS_PROTOCOL):
        text = reference.read_text(encoding="utf-8")
        if len(text.splitlines()) > 100 and "## 目录" not in text:
            fail(f"{reference.name} exceeds 100 lines but has no table of contents.", failures)

    if "$zede-zero-learning-roadmap" not in openai_yaml:
        fail("agents/openai.yaml default prompt lacks the invocation command.", failures)
    if "分层版或全量版" not in openai_yaml:
        fail("agents/openai.yaml does not describe output-mode selection.", failures)
    if "第一性原理" not in openai_yaml or "最小验证闭环" not in openai_yaml:
        fail("agents/openai.yaml does not describe first-principles clarification.", failures)
    if not all(marker in openai_yaml for marker in ("具体学习", "边做边学", "迁移", "反馈", "延迟复测")):
        fail("agents/openai.yaml does not describe the learning-effectiveness loop.", failures)
    short_match = re.search(r'^\s*short_description:\s*"([^"]+)"\s*$', openai_yaml, re.MULTILINE)
    if not short_match:
        fail("agents/openai.yaml has no quoted short_description.", failures)
    elif not 25 <= len(short_match.group(1)) <= 64:
        fail("short_description must contain 25–64 characters.", failures)

    if "$plan-learning-roadmap" in installable_text:
        fail("Found the obsolete invocation command.", failures)
    public_text = "\n".join((skill, openai_yaml, readme, compatibility, installer, *routers.values()))
    obsolete_public_names = (
        "zede-" + "plan-learning-roadmap",
        "Zede Plan " + "Learning Roadmap",
        "适合" + "一切",
    )
    for obsolete_name in obsolete_public_names:
        if obsolete_name in public_text:
            fail(f"Found obsolete or rejected public name text: {obsolete_name}", failures)
    for coupled_skill in ("interactive-learning", "dbs-learning"):
        if coupled_skill in installable_text:
            fail(f"Found an unwanted dependency on another Skill: {coupled_skill}", failures)
    if re.search(r"C:\\Users\\|/Users/|/home/", installable_text):
        fail("Found a machine-specific user path in installable content.", failures)
    if re.search(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----", installable_text):
        fail("Found private-key-shaped content.", failures)
    if re.search(r"\bsk-[A-Za-z0-9_-]{20,}\b", installable_text):
        fail("Found token-shaped content.", failures)
    if "TODO" in installable_text:
        fail("Found unresolved TODO text in installable content.", failures)

    try:
        payload = json.loads(CASES.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        fail(f"evals/cases.json is invalid JSON: {error}", failures)
        return report(failures)

    if payload.get("schema_version") != 2:
        fail("Behavior cases must use schema_version 2.", failures)
    if payload.get("hard_gate_pass_rate") != 1.0:
        fail("hard_gate_pass_rate must be 1.0.", failures)
    if payload.get("quality_threshold") != 0.9:
        fail("quality_threshold must be 0.9.", failures)

    cases = payload.get("cases")
    if not isinstance(cases, list):
        fail("Behavior cases must be a list.", failures)
        cases = []

    ids: list[str] = []
    covered_goal_types: set[str] = set()
    hard_count = 0
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            fail(f"Case {index} must be an object.", failures)
            continue
        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id:
            fail(f"Case {index} has no valid id.", failures)
            continue
        ids.append(case_id)

        goal_type = case.get("goal_type")
        if goal_type not in GOAL_TYPES:
            fail(f"Case {case_id} has invalid goal_type: {goal_type}", failures)
        else:
            covered_goal_types.add(goal_type)

        if case.get("severity") not in {"hard", "quality"}:
            fail(f"Case {case_id} has invalid severity.", failures)
        elif case["severity"] == "hard":
            hard_count += 1

        if not isinstance(case.get("mode"), str) or not case["mode"].strip():
            fail(f"Case {case_id} has no valid mode.", failures)

        for field in ("turns", "expected", "forbidden"):
            value = case.get(field)
            if not isinstance(value, list) or not value or not all(
                isinstance(item, str) and item.strip() for item in value
            ):
                fail(f"Case {case_id} has no valid {field} list.", failures)

    if len(ids) != len(set(ids)):
        fail("Behavior case ids must be unique.", failures)
    missing_cases = sorted(REQUIRED_CASES.difference(ids))
    if missing_cases:
        fail(f"Missing behavior cases: {', '.join(missing_cases)}", failures)
    missing_goal_types = sorted(GOAL_TYPES.difference(covered_goal_types))
    if missing_goal_types:
        fail(f"Uncovered goal types: {', '.join(missing_goal_types)}", failures)
    if hard_count < 10:
        fail("Behavior suite must contain at least 10 hard-gate cases.", failures)

    try:
        judge_schema = json.loads(JUDGE_SCHEMA.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        fail(f"evals/judge-schema.json is invalid JSON: {error}", failures)
        judge_schema = {}
    judge_required = set(judge_schema.get("required", []))
    if judge_required != {
        "pass",
        "hard_gate_failures",
        "quality_issues",
        "summary",
    }:
        fail("Judge schema does not require the complete judgment contract.", failures)

    runner = FORWARD_RUNNER.read_text(encoding="utf-8")
    require_markers(
        runner,
        (
            "--ephemeral",
            "--sandbox",
            "read-only",
            "TemporaryDirectory",
            "hard_pass_rate",
            "quality_pass_rate",
            "output-schema",
        ),
        "run_forward_evals.py",
        failures,
    )

    return report(failures)


def report(failures: list[str]) -> int:
    if failures:
        for failure in failures:
            print(f"[FAIL] {failure}")
        return 1
    print("[PASS] v1.0.0 Skill contract, cross-agent adapters, and behavior cases are complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
