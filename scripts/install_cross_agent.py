from __future__ import annotations

import argparse
import hashlib
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "zede-zero-learning-roadmap"
SOURCE = ROOT / SKILL_NAME


def destinations(home: Path) -> dict[str, Path]:
    return {
        "codex": home / ".codex" / "skills" / SKILL_NAME,
        "claude": home / ".claude" / "skills" / SKILL_NAME,
        "shared": home / ".agents" / "skills" / SKILL_NAME,
    }


def file_digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def tree_manifest(root: Path) -> dict[str, str]:
    return {
        path.relative_to(root).as_posix(): file_digest(path)
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def same_tree(left: Path, right: Path) -> bool:
    return tree_manifest(left) == tree_manifest(right)


def selected_targets(target: str) -> tuple[str, ...]:
    if target == "all-native":
        return ("codex", "claude", "shared")
    return (target,)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Preview or install Zede-Zero for native Skill hosts."
    )
    parser.add_argument(
        "--target",
        choices=("codex", "claude", "shared", "all-native"),
        default="all-native",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Copy files. Without this flag the command is a read-only preview.",
    )
    args = parser.parse_args()

    if not (SOURCE / "SKILL.md").is_file():
        raise SystemExit(f"Canonical Skill not found: {SOURCE}")

    home = Path.home()
    target_map = destinations(home)
    failed = False

    for target in selected_targets(args.target):
        destination = target_map[target]
        if destination.exists():
            if same_tree(SOURCE, destination):
                print(f"[OK] {target}: already up to date at {destination}")
            else:
                print(
                    f"[REFUSE] {target}: a different copy already exists at "
                    f"{destination}"
                )
                failed = True
            continue

        if not args.apply:
            print(f"[PREVIEW] {target}: {SOURCE} -> {destination}")
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(SOURCE, destination)
        print(f"[INSTALLED] {target}: {destination}")

    if failed:
        print("Review, rename, or remove the conflicting copy before retrying.")
        return 2
    if not args.apply:
        print("Preview only. Add --apply to install.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
