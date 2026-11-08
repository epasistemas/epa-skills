"""Tests for privacy/secret policy scanner (no real PII in assertions)."""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import scan_policy  # noqa: E402


class TestPolicyPatterns(unittest.TestCase):
    def test_synthetic_line_skipped(self):
        line = "contato: +5511999999999 SINTÉTICO exemplo"
        self.assertEqual(scan_policy.check_line(line, 1, "x.md", []), [])

    def test_whatsapp_jid_detected(self):
        line = "jid: 5511999999999@s.whatsapp.net"
        hits = scan_policy.check_line(line, 2, "skills/x/SKILL.md", [])
        self.assertIn("whatsapp_jid", hits)

    def test_placeholder_email_allowed(self):
        line = "Mail: user@example.invalid para testes"
        self.assertEqual(scan_policy.check_line(line, 1, "x.md", []), [])

    def test_realistic_email_flagged(self):
        line = "enviar para cliente.real@empresa.com.br"
        hits = scan_policy.check_line(line, 1, "x.md", [])
        self.assertIn("email", hits)

    def test_phone_br_flagged(self):
        line = "tel (11) 98765-4321"
        hits = scan_policy.check_line(line, 1, "x.md", [])
        self.assertIn("phone_br", hits)

    def test_output_never_contains_match_value(self):
        """Scanner reports only rule id, not the sensitive substring."""
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bad = root / "leak.md"
            bad.write_text("jid: 5511888777666@s.whatsapp.net\n", encoding="utf-8")
            findings = scan_policy.scan_tree(root)
            self.assertTrue(findings)
            joined = " ".join(findings)
            self.assertNotIn("5511888777666", joined)
            self.assertNotIn("@s.whatsapp", joined)
            self.assertIn("whatsapp_jid", joined)

    def test_allowlist_exception(self):
        from scan_policy import AllowEntry

        line = "contato: demo@cliente.com"
        rel = "docs/public-ref.md"
        allow = [
            AllowEntry(
                path=rel,
                line=5,
                rule="email",
                reason="E-mail institucional público citado na fonte oficial X",
            )
        ]
        self.assertEqual(scan_policy.check_line(line, 5, rel, allow), [])
        self.assertIn("email", scan_policy.check_line(line, 6, rel, allow))

    def test_repo_scan_passes(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "scan_policy.py")],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, msg=result.stderr)


if __name__ == "__main__":
    unittest.main()
