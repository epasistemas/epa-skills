#!/usr/bin/env bash
# Concurrency helper: fetch and report if local branch is behind its upstream.
# Does not pull, reset, or force-push. Exit 1 if behind (suggest merge first).

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

echo "== branch =="
git branch -vv

echo "== status =="
git status --short

BRANCH="$(git branch --show-current)"
if [[ -z "$BRANCH" ]]; then
  echo "ERROR: detached HEAD; checkout a branch first." >&2
  exit 1
fi

echo "== fetch =="
git fetch origin "$BRANCH" main 2>&1 || true

UPSTREAM="$(git rev-parse --abbrev-ref '@{u}' 2>/dev/null || true)"
if [[ -z "$UPSTREAM" ]]; then
  echo "WARNING: no upstream set for $BRANCH" >&2
  exit 0
fi

LOCAL="$(git rev-parse HEAD)"
REMOTE="$(git rev-parse "$UPSTREAM")"
echo "== SHAs =="
echo "HEAD:   $LOCAL"
echo "upstream ($UPSTREAM): $REMOTE"

BEHIND="$(git rev-list --count HEAD.."$UPSTREAM" 2>/dev/null || echo 0)"
AHEAD="$(git rev-list --count "$UPSTREAM"..HEAD 2>/dev/null || echo 0)"
echo "ahead=$AHEAD behind=$BEHIND"

if [[ "$BEHIND" -gt 0 ]]; then
  echo "ERROR: branch is $BEHIND commit(s) behind $UPSTREAM. Fetch done; merge before push." >&2
  echo "Remote commits you lack:" >&2
  git log --oneline HEAD.."$UPSTREAM" >&2 || true
  exit 1
fi

if [[ "$LOCAL" != "$REMOTE" && "$AHEAD" -gt 0 ]]; then
  echo "OK: $AHEAD local commit(s) ahead of upstream (ready to push after revalidation)."
fi

echo "Concurrency check OK (does not eliminate race with parallel editors)."
