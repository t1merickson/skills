---
name: cut-memory
description: Audit Claude's project-scoped memory, preserve the few non-reconstructable facts, and quarantine redundant or stale entries with an auditable undo.
---

# Cut memory

Use this skill only when invoked. Treat memory skeptically, not as disposable: its job is to preserve behavior-changing facts that are neither durable elsewhere nor cheaply reconstructable.

Claude project memory normally lives under `~/.claude/projects/<encoded-cwd>/memory/`. Confirm the active location and schema before operating; host layouts drift.

## Inventory

Read `MEMORY.md` and every file it references. Record file count, total bytes, inbound links, and any unindexed files. Do not inspect another project's memory merely because it is adjacent on disk.

## Classify

A memory earns retention only when all three hold:

1. It changes future behavior or prevents a likely mistake.
2. The fact is absent from project instructions, code, durable docs, skills, and agent configuration.
3. Reconstructing it is meaningfully harder than reading one file or running one command.

Typical cuts are task reports, duplicated project facts, stale tool state, motives already preserved beside a rule, and command-derived inventories. Typical keeps are silent runtime traps, user context with no appropriate durable home, and facts whose default inference would be confidently wrong.

Verify the supposed duplicate or stale source before classifying it. Do not move global preferences into another agent's configuration as a side effect; report the routing question instead.

## Apply reversibly

Move cut files to a dated sibling quarantine. Write a manifest containing original path, quarantine path, size, reason, and the durable source that supersedes it. Rebuild `MEMORY.md` with one concise pointer per survivor; do not summarize removed material back into the index.

Report before/after file and byte counts, every classification, the quarantine path, and the exact undo. Cutting nothing—or cutting everything—is valid when the evidence supports it.
