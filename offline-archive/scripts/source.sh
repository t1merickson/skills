#!/usr/bin/env bash
# Write the provenance file skeleton beside an archive. Fixed fields filled from the
# mirror manifest; prose fields left as TODO for the judgment pass.
# Usage: source.sh <archive-dir> <original-url> [scope-one-liner]
set -euo pipefail
dir="${1:?usage: source.sh <archive-dir> <original-url> [scope]}"
url="${2:?original url required}"
scope="${3:-TODO}"
dir="$(cd -- "$dir" && pwd)"
out="$dir/SOURCE.md"
[[ -e "$out" ]] && { echo "exists, not overwriting: $out" >&2; exit 73; }

files=0; bytes=0; failed=0; entry_sha="TODO"
if [[ -f "$dir/.mirror/manifest.json" ]]; then
  read -r files bytes < <(python3 - "$dir/.mirror/manifest.json" <<'PY'
import json,sys
m=json.load(open(sys.argv[1])); print(len(m), sum(v["bytes"] for v in m.values()))
PY
)
  [[ -f "$dir/.mirror/failed.json" ]] && failed="$(python3 -c "import json,sys;print(len(json.load(open(sys.argv[1]))))" "$dir/.mirror/failed.json")"
fi
entry="$(find "$dir" -maxdepth 2 -name index.html -not -path '*/.mirror/*' | head -n1 || true)"
[[ -n "$entry" ]] && entry_sha="$(shasum -a 256 "$entry" | cut -d' ' -f1)"

cat > "$out" <<MD
# $(printf '%s' "$url" | sed -E 's#^https?://##; s#/$##')

TODO: one paragraph on what this is and why it was kept.

| | |
| --- | --- |
| Original URL | $url |
| Retrieved | $(date +%F) |
| Scope | $scope |
| Request policy | mirror.py defaults: serial, base delay 0.5 s with jitter, 3 retries with backoff, Retry-After honoured |
| Capture tool | offline-archive/scripts/mirror.py, $(python3 --version 2>&1), urllib |
| Size | $files files, $(( bytes / 1024 )) KB; $failed failed URLs (see .mirror/failed.json) |
| Entry page sha256 | $entry_sha |

Per-file URLs, bytes, and sha256 of the bytes as served are in \`.mirror/manifest.json\`.

## How to open it

\`\`\`
offline-archive/scripts/verify.sh .
\`\`\`

## Transformations

TODO: rewrites, shims, disabled features. "None" is a valid answer.

## Omitted and known failures

TODO: what was out of scope, what did not reproduce offline.

## Licenses

TODO.
MD
printf '%s\n' "$out"
