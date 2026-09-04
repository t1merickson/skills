# Adopting older state files

Projects accumulate hand-written state files: `CHECKPOINT.md`, `COMPACTED.md`, `RESUME.md`, `STATE.md`, `PARKED.md`, `HANDOFF.md`, `CONTEXT.md`, `WIP.md`, and `SESSION-NOTES.md`. Judge them by content, not filename.

## Classify before touching

Use three signals:

1. **Audience.** Is an agent writing to its future self, or is this durable documentation for any reader?
2. **Provenance.** Inspect `git log --format='%an · %s' -- <file>`. Long-lived user-authored documents are not session debris.
3. **Inbound references.** Search with `rg -n '<filename>' .`. Files linked from README, AGENTS.md, CLAUDE.md, or documentation are part of the project until proven otherwise.

Then choose one result:

- **Task state:** write it into its own checkpoint with an `adopted-<original-name>` slug and a scope header. Verify the checkpoint, then remove the old path. Git history or an explicit rollback copy must make the transformation recoverable.
- **Durable knowledge:** leave it exactly where it is.
- **Mixed:** carve the file into two. Move the task-state portions into their own adopted checkpoint, then rewrite the source file to contain only the durable knowledge. Repair headings and connective text in both outputs so each stands alone. Record exactly what moved and where.
- **Ambiguous:** leave it in place and ask.

For a mixed split:

1. classify every substantive section or paragraph as task state, durable knowledge, or specifically ambiguous;
2. write and verify the adopted checkpoint;
3. remove the moved task-state material from the source and repair the durable document's structure;
4. compare the two outputs with the original and confirm that their union preserves every substantive claim, decision, uncertainty, and next action;
5. check inbound links and update them only when the split changed their intended target.

Do not keep the complete mixed source as a third live copy: that defeats the split and leaves two authorities for task state. Recovery belongs in Git history or a clearly temporary rollback artifact, not in the project's active documentation. If the file is untracked and has no recoverable history, create a rollback copy before rewriting it and report that copy.

Never silently merge another task's reasoning into the current checkpoint. A mixed classification itself authorizes the split; ask only when a particular passage remains genuinely ambiguous after checking audience, provenance, and inbound references. Ask before adopting more than a couple of files at once; for a pile, apply `file-batch-safety` and produce a manifest.

Report every source, classification, destination, what moved out of each mixed file, and the command or Git operation that restores the pre-split state.
