#!/usr/bin/env python3
"""
Heuristic privacy + secret scan. Reports file:line:rule only — never matched values.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWLIST_PATH = ROOT / "scripts" / "privacy_allowlist.json"

SKIP_DIRS = {".git", ".venv", "__pycache__", "node_modules", "tests"}

TEXT_EXTENSIONS = {
    ".md",
    ".json",
    ".yml",
    ".yaml",
    ".py",
    ".sh",
    ".txt",
    ".env",
    "",
}

SYNTHETIC_MARKERS = (
    "SYNTHETIC",
    "SINTÉTICO",
    "SINTETICO",
    "PLACEHOLDER",
    "example.invalid",
    "example.com",
    "example.org",
    "00000000-0000-0000-0000-000000000099",
    "Bearer SYNTHETIC",
    "fictício",
    "ficticio",
)

SAFE_EMAIL_LOCAL = re.compile(
    r"^[a-zA-Z0-9._%+-]+@(example\.(invalid|com|org)|users\.noreply\.github\.com)$"
)

RULES: list[tuple[str, re.Pattern[str]]] = [
    ("aws_key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("github_pat", re.compile(r"ghp_[A-Za-z0-9]{20,}")),
    ("github_fine", re.compile(r"github_pat_[A-Za-z0-9_]{20,}")),
    ("jwt", re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.")),
    ("private_pem", re.compile(r"-----BEGIN (?:RSA )?PRIVATE KEY-----")),
    (
        "bearer_token",
        re.compile(r"Bearer\s+(?!SYNTHETIC)[A-Za-z0-9._-]{20,}"),
    ),
    ("whatsapp_jid", re.compile(r"\d{6,}@(s\.whatsapp\.net|c\.us|g\.us)\b")),
    (
        "phone_e164",
        re.compile(r"(?<!\d)\+[1-9]\d{9,14}(?!\d)"),
    ),
    (
        "phone_br",
        re.compile(
            r"(?<!\d)(?:\+55\s?)?(?:\(?\d{2}\)?\s?)?(?:9\s?)?\d{4}[-\s]?\d{4}(?!\d)"
        ),
    ),
    (
        "email",
        re.compile(
            r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
        ),
    ),
    (
        "uuid",
        re.compile(
            r"\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}\b"
        ),
    ),
    (
        "internal_url",
        re.compile(
            r"https?://(?:localhost|127\.0\.0\.1|10\.\d+\.\d+\.\d+|192\.168\.\d+\.\d+|"
            r"172\.(?:1[6-9]|2\d|3[01])\.\d+\.\d+|[a-z0-9.-]+\.(?:local|internal|lan)\b)",
            re.I,
        ),
    ),
    (
        "suspicious_host",
        re.compile(
            r"https?://(?:[a-z0-9-]+\.)?(?:ngrok\.io|trycloudflare\.com|loca\.lt)\b",
            re.I,
        ),
    ),
]


@dataclass(frozen=True)
class AllowEntry:
    path: str
    line: int
    rule: str
    reason: str


def load_allowlist() -> list[AllowEntry]:
    if not ALLOWLIST_PATH.is_file():
        return []
    data = json.loads(ALLOWLIST_PATH.read_text(encoding="utf-8"))
    out: list[AllowEntry] = []
    for raw in data.get("exceptions", []):
        out.append(
            AllowEntry(
                path=raw["path"],
                line=int(raw["line"]),
                rule=raw["rule"],
                reason=raw.get("reason", ""),
            )
        )
    return out


def line_is_synthetic(line: str) -> bool:
    lower = line.lower()
    return any(m.lower() in lower for m in SYNTHETIC_MARKERS)


def email_is_placeholder(match: str) -> bool:
    return bool(SAFE_EMAIL_LOCAL.match(match))


def iter_scan_files() -> list[Path]:
    paths: list[Path] = []
    for p in ROOT.rglob("*"):
        if p.is_dir():
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        rel = p.relative_to(ROOT)
        if rel.parts and rel.parts[0] == "tests":
            continue
        if p.suffix.lower() in TEXT_EXTENSIONS or p.name in {
            "LICENSE",
            "CODEOWNERS",
            "catalog.json",
        }:
            paths.append(p)
    return paths


def allowed(
    allowlist: list[AllowEntry], rel: str, line_no: int, rule: str
) -> bool:
    for entry in allowlist:
        if entry.path == rel and entry.line == line_no and entry.rule == rule:
            return True
    return False


def check_line(
    line: str, line_no: int, rel: str, allowlist: list[AllowEntry]
) -> list[str]:
    if line_is_synthetic(line):
        return []
    hits: list[str] = []
    for rule_id, pattern in RULES:
        if not pattern.search(line):
            continue
        if rule_id == "email":
            for m in pattern.finditer(line):
                addr = m.group(0)
                if addr.startswith("git@"):
                    continue
                if email_is_placeholder(addr):
                    continue
                if not allowed(allowlist, rel, line_no, rule_id):
                    hits.append(rule_id)
                    break
            continue
        if rule_id == "uuid" and "00000000-0000-0000-0000-000000000099" in line:
            continue
        if rule_id == "phone_br":
            if "0000-0000" in line or "99999-9999" in line:
                continue
        if not allowed(allowlist, rel, line_no, rule_id):
            hits.append(rule_id)
    return hits


def scan_tree(root: Path | None = None) -> list[str]:
    """Return redacted finding lines: rel:line:rule"""
    allowlist = load_allowlist()
    findings: list[str] = []
    files = iter_scan_files() if root is None else list(root.rglob("*"))
    if root is not None:
        files = [p for p in files if p.is_file()]
    base = ROOT if root is None else root
    for path in files:
        if not path.is_file():
            continue
        try:
            rel = str(path.relative_to(base if root else ROOT))
        except ValueError:
            rel = str(path)
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for i, line in enumerate(text.splitlines(), start=1):
            for rule in check_line(line, i, rel, allowlist):
                findings.append(f"{rel}:{i}:{rule}")
    return findings


def main() -> int:
    findings = scan_tree()
    if findings:
        print(
            "Policy scan FAILED (heuristic; values redacted). Fix or allowlist:",
            file=sys.stderr,
        )
        for f in sorted(set(findings)):
            print(f"  - {f}", file=sys.stderr)
        return 1
    print("Policy scan OK (heuristic; human review still required)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
