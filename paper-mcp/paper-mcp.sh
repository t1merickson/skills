#!/usr/bin/env bash
set -euo pipefail

paper_mcp_endpoint="${PAPER_MCP_ENDPOINT:-http://127.0.0.1:29979/mcp}"
paper_mcp_protocol="${PAPER_MCP_PROTOCOL_VERSION:-2025-03-26}"
headers=(-H 'Content-Type: application/json' -H 'Accept: application/json, text/event-stream')

usage() {
  echo "usage: $0 init | call <session> <tool> [json-args] | raw <session> <jsonrpc-body>" >&2
  exit 64
}

post() {
  local timeout="$1"
  shift
  curl --silent --show-error --fail-with-body --max-time "$timeout" \
    -X POST "$paper_mcp_endpoint" "${headers[@]}" "$@"
}

command_name="${1:-}"
case "$command_name" in
  init)
    [[ $# -eq 1 ]] || usage
    header_file="$(mktemp -t paper-mcp-headers.XXXXXX)"
    trap 'rm -f -- "$header_file"' EXIT
    init_body="$(jq -nc --arg version "$paper_mcp_protocol" '{jsonrpc:"2.0",id:1,method:"initialize",params:{protocolVersion:$version,capabilities:{},clientInfo:{name:"authored-agent-skill",version:"1.0"}}}')"
    post 10 -D "$header_file" -d "$init_body" >/dev/null
    session_id="$(awk 'tolower($1)=="mcp-session-id:" {gsub("\r", "", $2); print $2}' "$header_file" | tail -n 1)"
    if [[ -z "$session_id" ]]; then
      echo "Paper MCP did not return a session id" >&2
      exit 69
    fi
    post 10 -H "mcp-session-id: $session_id" \
      -d '{"jsonrpc":"2.0","method":"notifications/initialized"}' >/dev/null
    printf '%s\n' "$session_id"
    ;;
  call)
    [[ $# -ge 3 && $# -le 4 ]] || usage
    session_id="$2"
    tool_name="$3"
    arguments="{}"
    if [[ $# -eq 4 ]]; then
      arguments="$4"
    fi
    body="$(jq -nc --arg tool "$tool_name" --argjson arguments "$arguments" '{jsonrpc:"2.0",id:2,method:"tools/call",params:{name:$tool,arguments:$arguments}}')"
    post 120 -H "mcp-session-id: $session_id" -d "$body" | sed -n 's/^data: //p'
    ;;
  raw)
    [[ $# -eq 3 ]] || usage
    post 60 -H "mcp-session-id: $2" -d "$3" | sed -n 's/^data: //p'
    ;;
  *) usage ;;
esac
