#!/usr/bin/env python3
"""Validate Agent Skills layout for epa-skills (agentskills.io subset)."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
CATALOG_PATH = ROOT / "catalog.json"

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

# Simple YAML parser for flat frontmatter (no nested deps required for CI)
def parse_simple_yaml(block: str) -> dict[str, str]:
    data: dict[str, str] = {}
    current_key: str | None = None
    for line in block.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if re.match(r"^[\w-]+:\s*", line) and not line.startswith(" "):
            key, _, val = line.partition(":")
            val = val.strip().strip('"').strip("'")
            current_key = key.strip()
            if val:
                data[current_key] = val
            else:
                data[current_key] = ""
        elif line.startswith(" ") and current_key:
            data[current_key] += "\n" + line.strip()
    return data


def load_frontmatter(path: Path) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        raise ValueError(f"{path}: missing YAML frontmatter")
    body = text[m.end() :]
    return parse_simple_yaml(m.group(1)), body


def validate_name(name: str, slug: str) -> list[str]:
    errs: list[str] = []
    if not name:
        errs.append("missing name")
        return errs
    if len(name) > 64:
        errs.append(f"name longer than 64 chars: {name!r}")
    if name != slug:
        errs.append(f"name {name!r} must match directory {slug!r}")
    if not NAME_RE.match(name):
        errs.append(f"name {name!r} invalid format")
    if "--" in name or name.startswith("-") or name.endswith("-"):
        errs.append(f"name {name!r} has invalid hyphen placement")
    return errs


def find_markdown_links(body: str) -> list[str]:
    return re.findall(r"\]\(([^)]+)\)", body)


def validate_skill_dir(skill_dir: Path) -> list[str]:
    errs: list[str] = []
    slug = skill_dir.name
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        return [f"{skill_dir}: SKILL.md required"]
    try:
        fm, body = load_frontmatter(skill_md)
    except ValueError as e:
        return [str(e)]

    errs.extend(validate_name(fm.get("name", ""), slug))
    desc = fm.get("description", "")
    if not desc or not desc.strip():
        errs.append(f"{skill_md}: empty description")
    elif len(desc) > 1024:
        errs.append(f"{skill_md}: description longer than 1024 characters")

    for link in find_markdown_links(body):
        if link.startswith(("http://", "https://", "mailto:")):
            continue
        if link.startswith("#"):
            continue
        target = (skill_dir / link).resolve()
        if not target.exists():
            errs.append(f"{skill_md}: broken relative link {link!r}")

    return errs


def validate_catalog(skill_slugs: set[str]) -> list[str]:
    errs: list[str] = []
    if not CATALOG_PATH.is_file():
        return ["catalog.json missing"]
    try:
        catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"catalog.json invalid JSON: {e}"]

    if catalog.get("defaultBranch") != "main":
        errs.append('catalog.json defaultBranch must be "main"')

    entries = catalog.get("skills", [])
    cat_slugs = set()
    for entry in entries:
        slug = entry.get("slug")
        if not slug:
            errs.append("catalog entry missing slug")
            continue
        cat_slugs.add(slug)
        path = entry.get("path", "")
        expected = f"skills/{slug}"
        if path != expected:
            errs.append(f"catalog path for {slug!r} expected {expected!r}, got {path!r}")
        if slug not in skill_slugs:
            errs.append(f"catalog lists unknown skill {slug!r}")

    if cat_slugs != skill_slugs:
        missing = skill_slugs - cat_slugs
        extra = cat_slugs - skill_slugs
        if missing:
            errs.append(f"skills missing from catalog: {sorted(missing)}")
        if extra:
            errs.append(f"catalog has extra slugs: {sorted(extra)}")

    return errs


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print("No skills/ directory", file=sys.stderr)
        return 1

    all_errs: list[str] = []
    slugs: set[str] = set()
    for child in sorted(SKILLS_DIR.iterdir()):
        if not child.is_dir() or child.name.startswith("."):
            continue
        slugs.add(child.name)
        all_errs.extend(validate_skill_dir(child))

    all_errs.extend(validate_catalog(slugs))

    if all_errs:
        print("Validation FAILED:", file=sys.stderr)
        for e in all_errs:
            print(f"  - {e}", file=sys.stderr)
        return 1

    print(f"Validation OK ({len(slugs)} skills)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
