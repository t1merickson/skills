# Codex CLI

Resolve the installed executable rather than guessing its location:

```bash
CODEX_BIN="$(command -v codex)"
test -n "$CODEX_BIN"
```

Run from the repository or pass `-C <directory>`.

Three CLI traps are easy to misdiagnose as a weak or hung model:

- `-o <file>` captures the final answer; stdout is a progress stream. Read both for different purposes.
- For a long brief, pass `-` and redirect a prompt file into stdin rather than fighting shell quoting.
- When the prompt is already an argument in a non-interactive process, redirect stdin from `/dev/null`; otherwise `codex exec` may wait for additional input indefinitely.

Non-trivial runs take time. Run them through the host's background mechanism when available and continue useful independent work, then collect the output file.

## Read-only consultation

```bash
codex_model="<confirmed-model-id>"
"$CODEX_BIN" exec \
  --model "$codex_model" \
  -c 'model_reasoning_effort="high"' \
  --sandbox read-only \
  -C /absolute/repository/path \
  -o /tmp/codex-consult.md \
  - < /tmp/codex-brief.md
```

## Bounded implementation

```bash
codex_model="<confirmed-model-id>"
"$CODEX_BIN" exec \
  --model "$codex_model" \
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
- The directory passed with `-C` defines the practical write blast radius. Point it at the repository, never a broad parent or home directory.
- Do not use danger-bypass flags.
- Check the worktree before and after a writing run.
- Capture the final response, but judge it against the actual diff and command results.
