#!/usr/bin/env bash
# One-line Codex dispatch. Fixes sandbox, model, effort, cwd, and output path per relationship.
# Usage: run.sh <consult|investigate|delegate> <repo-dir> <brief-file> [model] [effort]
#   consult / investigate -> --sandbox read-only
#   delegate              -> --sandbox workspace-write
# Prints the output file path. The brief file is the judgment; this script is only plumbing.
set -euo pipefail

if [[ $# -lt 3 || $# -gt 5 ]]; then
  echo "usage: run.sh <consult|investigate|delegate> <repo-dir> <brief-file> [model] [effort]" >&2
  exit 64
fi

mode="$1"; repo="$2"; brief="$3"
model="${4:-${CODEX_MODEL:-gpt-6.1-sol}}"
effort="${5:-}"

case "$mode" in
  consult|investigate) sandbox="read-only";      effort="${effort:-high}" ;;
  delegate)            sandbox="workspace-write"; effort="${effort:-medium}" ;;
  *) echo "mode must be consult, investigate, or delegate" >&2; exit 64 ;;
esac

[[ -d "$repo" ]]  || { echo "repo dir not found: $repo" >&2; exit 66; }
[[ -f "$brief" ]] || { echo "brief file not found: $brief" >&2; exit 66; }
repo="$(cd -- "$repo" && pwd)"
case "$repo" in
  "$HOME"|/|/Users|/Users/Commons|/Users/Commons/Developer)
    echo "refusing: -C would point at a broad parent ($repo)" >&2; exit 65 ;;
esac

CODEX_BIN="$(command -v codex || true)"
[[ -n "$CODEX_BIN" ]] || { echo "codex not on PATH" >&2; exit 69; }

out="$(mktemp "/tmp/codex-$mode-XXXXXX").md"

"$CODEX_BIN" exec \
  --model "$model" \
  -c "model_reasoning_effort=\"$effort\"" \
  --sandbox "$sandbox" \
  -C "$repo" \
  -o "$out" \
  - < "$brief" >/dev/null

printf '%s\n' "$out"
