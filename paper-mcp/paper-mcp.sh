#!/bin/bash
# Helper for driving the Paper Desktop MCP server (http://127.0.0.1:29979/mcp).
# Usage:
#   paper-mcp.sh init                      -> prints new session id
#   paper-mcp.sh call <session> <tool> '<json-args>'
#   paper-mcp.sh raw  <session> '<full-jsonrpc-body>'
# Responses are SSE; this extracts the JSON payload from the data: line.

EP=http://127.0.0.1:29979/mcp
HDR=(-H 'Content-Type: application/json' -H 'Accept: application/json, text/event-stream')

case "$1" in
  init)
    resp=$(curl -s -m 10 -X POST "$EP" "${HDR[@]}" -D /tmp/paper-mcp-headers.txt \
      -d '{"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-03-26","capabilities":{},"clientInfo":{"name":"claude-code","version":"1.0"}}}')
    sid=$(grep -i '^mcp-session-id:' /tmp/paper-mcp-headers.txt | tr -d '\r' | awk '{print $2}')
    curl -s -m 10 -X POST "$EP" "${HDR[@]}" -H "mcp-session-id: $sid" \
      -d '{"jsonrpc":"2.0","method":"notifications/initialized"}' > /dev/null
    echo "$sid"
    ;;
  call)
    sid=$2; tool=$3; args=${4:-'{}'}
    body=$(jq -nc --arg t "$tool" --argjson a "$args" '{"jsonrpc":"2.0","id":2,"method":"tools/call","params":{"name":$t,"arguments":$a}}')
    curl -s -m 120 -X POST "$EP" "${HDR[@]}" -H "mcp-session-id: $sid" -d "$body" \
      | sed -n 's/^data: //p'
    ;;
  raw)
    sid=$2; body=$3
    curl -s -m 60 -X POST "$EP" "${HDR[@]}" -H "mcp-session-id: $sid" -d "$body" \
      | sed -n 's/^data: //p'
    ;;
  *) echo "usage: $0 init | call <sid> <tool> <json-args> | raw <sid> <body>"; exit 1;;
esac
