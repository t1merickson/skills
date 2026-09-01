# Codex CLI

Resolve the installed executable rather than guessing its location:

```bash
CODEX_BIN="$(command -v codex)"
test -n "$CODEX_BIN"
```

Run from the repository or pass `-C <directory>`.

## Read-only consultation

```bash
"$CODEX_BIN" exec \
  --model gpt-5.6-sol \
  -c 'model_reasoning_effort="high"' \
  --sandbox read-only \
  -C /absolute/repository/path \
  -o /tmp/codex-consult.md \
  - < /tmp/codex-brief.md
```

## Bounded implementation

```bash
"$CODEX_BIN" exec \
  --model gpt-5.6-terra \
  -c 'model_reasoning_effort="medium"' \
  --sandbox workspace-write \
  -C /absolute/repository/path \
  -o /tmp/codex-result.md \
  - < /tmp/codex-brief.md
```

Use the exact model identifiers advertised by the installed host. `codex exec --help` is the source of truth for current flags.

## Continuation and review

Use `codex exec resume` when a focused correction benefits from the same context. Use a fresh read-only run for independent review. `codex review` is useful when the requested judgment matches its diff-oriented interface.

## Safety

- `read-only` is the default for advice and evidence gathering.
- `workspace-write` authorizes repository edits, not arbitrary machine access.
- Do not use danger-bypass flags.
- Check the worktree before and after a writing run.
- Capture the final response, but judge it against the actual diff and command results.
