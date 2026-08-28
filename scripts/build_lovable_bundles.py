#!/usr/bin/env python3
"""Build Lovable-compatible ZIP skill bundles using only the Python standard library."""

from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import shutil

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist" / "lovable"


def add_tree(zf: ZipFile, source: Path, target_prefix: str = "") -> None:
    if not source.exists():
        return
    for path in sorted(source.rglob("*")):
        if not path.is_file():
            continue
        if "__pycache__" in path.parts or path.name.startswith("."):
            continue
        rel = path.relative_to(source)
        target = Path(target_prefix) / rel
        zf.write(path, target.as_posix())


def build_orchestrator() -> Path:
    out = DIST / "ui-design-orchestrator.zip"
    with ZipFile(out, "w", ZIP_DEFLATED) as zf:
        zf.write(ROOT / "SKILL.md", "SKILL.md")
        zf.write(ROOT / "NOTICE.md", "NOTICE.md")
        add_tree(zf, ROOT / "skills", "skills")
        add_tree(zf, ROOT / "references", "references")
        add_tree(zf, ROOT / "starter", "starter")
    return out


def build_focused(skill_dir: Path) -> Path:
    out = DIST / f"{skill_dir.name}.zip"
    with ZipFile(out, "w", ZIP_DEFLATED) as zf:
        # Lovable expects the selected skill's SKILL.md at package root.
        zf.write(skill_dir / "SKILL.md", "SKILL.md")
        zf.write(ROOT / "NOTICE.md", "NOTICE.md")
        # Keep shared references available to skills that mention them.
        add_tree(zf, ROOT / "references", "references")
        add_tree(zf, ROOT / "starter", "starter")
    return out


def main() -> None:
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True, exist_ok=True)

    outputs = [build_orchestrator()]
    for skill_dir in sorted((ROOT / "skills").iterdir()):
        if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
            outputs.append(build_focused(skill_dir))

    print("Built Lovable bundles:")
    for path in outputs:
        print(f"- {path.relative_to(ROOT)} ({path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
