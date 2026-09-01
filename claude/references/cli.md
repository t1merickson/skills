# Claude CLI

Resolve the installed executable:

```bash
CLAUDE_BIN="$(command -v claude)"
test -n "$CLAUDE_BIN"
```

Run it from the target repository. Use the exact model alias or identifier accepted by the installed CLI; check `claude --help` when aliases change.

## Read-only Fable consultation

```bash
"$CLAUDE_BIN" -p \
  --model fable \
  --effort high \
  --permission-mode plan \
  --tools 'Read,Glob,Grep' \
  --output-format json \
  < /tmp/claude-brief.md > /tmp/claude-result.json
```

Restricting the tool set is the important read-only boundary. `plan` mode is useful, but it is not an operating-system sandbox.

## Bounded implementation

```bash
"$CLAUDE_BIN" -p \
  --model fable \
  --effort medium \
  --permission-mode acceptEdits \
  --output-format json \
  < /tmp/claude-brief.md > /tmp/claude-result.json
```

Run a writing session only in a prepared checkout or worktree whose scope is clear. Use `--worktree` when isolation is appropriate. Do not use `--dangerously-skip-permissions` or equivalent bypasses.

## Opus consultation

```bash
"$CLAUDE_BIN" -p \
  --model opus \
  --effort medium \
  --permission-mode plan \
  --tools 'Read,Glob,Grep' \
  --output-format json \
  < /tmp/claude-brief.md > /tmp/claude-result.json
```

Put the concision requirement in the brief.

## Continuation

JSON output includes session information that can be used with `--resume`. Resume for a focused follow-up; start a new session for an independent view. `claude --help` is the source of truth for current flags and permission modes.
