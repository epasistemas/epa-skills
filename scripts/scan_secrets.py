#!/usr/bin/env python3
"""Deprecated: use scan_policy.py. Wrapper kept for backwards compatibility."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import scan_policy  # noqa: E402

if __name__ == "__main__":
    sys.exit(scan_policy.main())
