#!/usr/bin/env python3
"""Validate the portable skill files without external dependencies."""

from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def frontmatter(text: str) -> dict[str, str]:
    """Parse our YAML frontmatter subset including folded/literal descriptions."""
    if not text.startswith("---\n"):
        return {}
    parts = text.split("---\n", 2)
    if len(parts) < 3:
        return {}
    data: dict[str, str] = {}
    block_key: str | None = None
    block_lines: list[str] = []

    def flush_block() -> None:
        nonlocal block_key, block_lines
        if block_key is not None:
            data[block_key] = " ".join(block_lines).strip()
            block_key = None
            block_lines = []

    for line in parts[1].splitlines():
        if (line.startswith(" ") or line.startswith("\t")) and block_key is not None:
            block_lines.append(line.strip())
            continue
        flush_block()
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        key, value = key.strip(), value.strip()
        if value in (">", "|", ">-", "|-"):
            block_key = key
        else:
            data[key] = value.strip('"\'')
    flush_block()
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
        elif not description.lower().startswith(("use when", "use for")):
            errors.append(f"{rel}: description should begin with 'Use when' or 'Use for'")

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

    manifest_file = ROOT / "skill-manifest.json"
    if manifest_file.exists():
        try:
            manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
            listed_paths = [item["path"] for item in manifest["skills"]]
            listed_names = [item["name"] for item in manifest["skills"]]
            actual_paths = {str(path.relative_to(ROOT)) for path in files if path != ROOT / "SKILL.md"}
            if len(listed_paths) != len(set(listed_paths)):
                errors.append("skill-manifest.json: duplicate skill paths")
            if len(listed_names) != len(set(listed_names)):
                errors.append("skill-manifest.json: duplicate skill names")
            if set(listed_paths) != actual_paths:
                errors.append(f"skill-manifest.json mismatch: expected {sorted(actual_paths)}, got {sorted(listed_paths)}")
            if manifest.get("root_skill") != "SKILL.md":
                errors.append("skill-manifest.json: root_skill must be SKILL.md")
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors.append(f"skill-manifest.json: invalid manifest: {exc}")
    else:
        errors.append("Missing skill-manifest.json")

    if errors:
        print("Skill validation failed:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(files)} skill files: {', '.join(sorted(names))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
