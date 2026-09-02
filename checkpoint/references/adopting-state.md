# Adopting older state files

Projects accumulate hand-written state files: `CHECKPOINT.md`, `COMPACTED.md`, `RESUME.md`, `STATE.md`, `PARKED.md`, `HANDOFF.md`, `CONTEXT.md`, `WIP.md`, and `SESSION-NOTES.md`. Judge them by content, not filename.

## Classify before touching

Use three signals:

1. **Audience.** Is an agent writing to its future self, or is this durable documentation for any reader?
2. **Provenance.** Inspect `git log --format='%an · %s' -- <file>`. Long-lived user-authored documents are not session debris.
3. **Inbound references.** Search with `rg -n '<filename>' .`. Files linked from README, AGENTS.md, CLAUDE.md, or documentation are part of the project until proven otherwise.

Then choose one result:

- **Task state:** copy it into its own checkpoint with an `adopted-<original-name>` slug and a scope header. Preserve the original in `.checkpoints/archive/` only after the copy is verified.
- **Durable knowledge:** leave it exactly where it is.
- **Mixed:** copy only the task-state portion into a checkpoint and leave the source intact. Record what was copied.
- **Ambiguous:** leave it in place and ask.

Never silently merge another task's reasoning into the current checkpoint. Never delete an original. Ask before changing a mixed file or adopting more than a couple at once; for a pile, apply `file-batch-safety` and produce a manifest.

Report every source, classification, destination, and the command or move that restores it.
