#!/usr/bin/env python3
"""Lightweight secret pattern scan (heuristic, not exhaustive)."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SKIP_DIRS = {".git", ".venv", "__pycache__", "node_modules"}
ALLOWLIST_SUBSTRINGS = (
    "SYNTHETIC_TOKEN_EXAMPLE",
    "example.invalid",
    "00000000-0000-0000-0000-000000000099",
    "Bearer SYNTHETIC",
)

PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("aws_key", re.compile(r"AKIA[0-9A-Z]{16}")),
    ("github_pat", re.compile(r"ghp_[A-Za-z0-9]{20,}")),
    ("github_fine", re.compile(r"github_pat_[A-Za-z0-9_]{20,}")),
    ("jwt", re.compile(r"eyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.")),
    ("bearer_real", re.compile(r"Bearer\s+(?!SYNTHETIC)[A-Za-z0-9._-]{20,}")),
    ("private_pem", re.compile(r"-----BEGIN (?:RSA )?PRIVATE KEY-----")),
]

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


def iter_files() -> list[Path]:
    paths: list[Path] = []
    for p in ROOT.rglob("*"):
        if p.is_dir():
            continue
        if any(part in SKIP_DIRS for part in p.parts):
            continue
        if p.suffix.lower() in TEXT_EXTENSIONS or p.name in {
            "LICENSE",
            "CODEOWNERS",
            "catalog.json",
        }:
            paths.append(p)
    return paths


def line_allowed(line: str) -> bool:
    return any(s in line for s in ALLOWLIST_SUBSTRINGS)


def main() -> int:
    findings: list[str] = []
    for path in iter_files():
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for i, line in enumerate(text.splitlines(), start=1):
            if line_allowed(line):
                continue
            for label, pattern in PATTERNS:
                if pattern.search(line):
                    rel = path.relative_to(ROOT)
                    findings.append(f"{rel}:{i}: possible {label}")

    if findings:
        print("Secret scan FAILED (review findings; may be false positives):", file=sys.stderr)
        for f in findings:
            print(f"  - {f}", file=sys.stderr)
        return 1

    print("Secret scan OK (heuristic)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
