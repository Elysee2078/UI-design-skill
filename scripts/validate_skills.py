#!/usr/bin/env python3
"""Validate the portable skill files without external dependencies."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}
    data: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def main() -> int:
    files = [ROOT / "SKILL.md", *sorted((ROOT / "skills").glob("*/SKILL.md"))]
    errors: list[str] = []
    names: set[str] = set()

    if not files or not (ROOT / "SKILL.md").exists():
        errors.append("Root SKILL.md is missing")

    for path in files:
        if not path.exists():
            errors.append(f"Missing: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        meta = frontmatter(text)
        rel = path.relative_to(ROOT)

        name = meta.get("name", "")
        description = meta.get("description", "")

        if not name:
            errors.append(f"{rel}: frontmatter 'name' missing")
        elif not re.fullmatch(r"[a-z0-9][a-z0-9-]*", name):
            errors.append(f"{rel}: invalid skill name '{name}'")
        elif name in names:
            errors.append(f"{rel}: duplicate skill name '{name}'")
        else:
            names.add(name)

        if not description:
            errors.append(f"{rel}: frontmatter 'description' missing")
        elif not description.lower().startswith("use when"):
            errors.append(f"{rel}: description should begin with 'Use when'")

        if len(text) > 100_000:
            errors.append(f"{rel}: exceeds 100k character portability target")

    required = [
        ROOT / "AGENTS.md",
        ROOT / "references" / "source-catalog.md",
        ROOT / "NOTICE.md",
    ]
    for path in required:
        if not path.exists():
            errors.append(f"Missing required repository file: {path.relative_to(ROOT)}")

    if errors:
        print("Skill validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(files)} skill files: {', '.join(sorted(names))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
