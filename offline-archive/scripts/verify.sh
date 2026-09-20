#!/usr/bin/env bash
# Serve a mirrored docroot locally and report what is there. Mechanical check only:
# file and byte counts, failed URLs from the manifest, and a curl of the entry page.
# Judgment (does the tool still work offline, are lazy assets present) stays with you.
# Usage: verify.sh <docroot> [host] [port]
set -euo pipefail
root="${1:?usage: verify.sh <docroot> [host] [port]}"
host="${2:-}"; port="${3:-8877}"
root="$(cd -- "$root" && pwd)"
if [[ -z "$host" ]]; then
  host="$(ls "$root" | grep -v '^\.' | head -n1)"
fi
serve_dir="$root/$host"
[[ -d "$serve_dir" ]] || { echo "no docroot for host '$host' under $root" >&2; exit 66; }

echo "files:  $(find "$serve_dir" -type f | wc -l | tr -d ' ')"
echo "bytes:  $(du -sk "$serve_dir" | cut -f1) KB"
if [[ -f "$root/.mirror/failed.json" ]]; then
  echo "failed: $(python3 -c "import json;print(len(json.load(open('$root/.mirror/failed.json'))))")"
fi

python3 -m http.server "$port" --bind 127.0.0.1 --directory "$serve_dir" >/dev/null 2>&1 &
pid=$!
trap 'kill $pid 2>/dev/null || true' EXIT
sleep 0.7
code="$(curl -s -o /dev/null -w '%{http_code}' "http://127.0.0.1:$port/")"
echo "entry:  http://127.0.0.1:$port/  -> HTTP $code"
echo "server pid $pid is running; press Ctrl-C to stop, or open the URL now."
wait $pid
