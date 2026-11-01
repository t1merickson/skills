# Adopting older state files

Projects collect hand-written state files: `CHECKPOINT.md`, `COMPACTED.md`, `RESUME.md`, `STATE.md`, `HANDOFF.md`, `PARKED.md`, `CONTEXT.md`, `WIP.md`, `SESSION-NOTES.md`. Judge them by content, not filename.

## Classify before touching

Three signals:

1. **Audience.** An agent writing to its future self, or documentation for any reader?
2. **Provenance.** `git log --format='%an · %s' -- <file>`. Long-lived files Timmy wrote are not session debris.
3. **Inbound references.** `rg -n '<filename>' .`. Files linked from README, AGENTS.md, CLAUDE.md, or docs are part of the project.

Then one result:

- **Task state:** move the file byte-intact to `checkpoints/<YYYY-MM-DD>-adopted-<original-name>.md`. Use `git mv` when tracked, plain `mv` otherwise. Do not edit, trim, reformat, or add a header inside it; confirm with `cmp` or `git diff -M` that the content is unchanged. New notes go in a separate checkpoint that links to it.
- **Durable knowledge:** leave it exactly where it is.
- **Mixed:** leave it in place, whole. Reference it from the current checkpoint's Terrain (`see RESUME.md, mixed task state and docs`). Splitting it is Timmy's call; ask, don't do it.
- **Ambiguous:** leave it in place and ask.

Never carve a file apart, adopt "a partial", or merge another task's decisions into the current checkpoint.

Ask before adopting more than a couple of files at once; for a pile, read `file-batch-safety` and produce a manifest.

Report each source, its classification, its destination, and the command that undoes the move.
