"""Tests for skill validation."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class TestSkillsLibrary(unittest.TestCase):
    def test_validate_skills_exit_zero(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_skills.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(
            result.returncode,
            0,
            msg=result.stderr or result.stdout,
        )

    def test_catalog_skill_names_match_directories(self):
        catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
        slugs = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
        catalog_slugs = {e["slug"] for e in catalog["skills"]}
        self.assertEqual(catalog_slugs, slugs)

    def test_each_skill_name_in_frontmatter(self):
        front_re = re.compile(r"^---\s*\nname:\s*([^\n]+)\n", re.MULTILINE)
        for skill_dir in (ROOT / "skills").iterdir():
            if not skill_dir.is_dir():
                continue
            text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
            m = front_re.search(text)
            self.assertIsNotNone(m, f"{skill_dir}: name in frontmatter")
            name = m.group(1).strip().strip('"').strip("'")
            self.assertEqual(name, skill_dir.name)


if __name__ == "__main__":
    unittest.main()
