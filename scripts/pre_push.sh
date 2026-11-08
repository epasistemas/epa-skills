#!/usr/bin/env bash
# Suggested gate before git push (manual or hook). Does not auto-push.

set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

./scripts/git_concurrency_check.sh
python3 scripts/validate_skills.py
python3 scripts/scan_policy.py
python3 -m unittest discover -s tests -p 'test_*.py' -q
echo "pre_push: all checks passed (heuristic; review diff manually)."
