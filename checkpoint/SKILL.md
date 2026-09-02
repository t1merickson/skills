---
name: checkpoint
description: Save non-reconstructable task state to .checkpoints/, or reload live checkpoints before resuming work.
---

# Checkpoint

A checkpoint preserves what the repository cannot: unsettled reasoning, failed approaches and why, partial confidence, user remarks not yet reflected in artifacts, and work that is running or promised. It is not a summary of files, diffs, or documentation that a later agent can reread.

## What earns a line

Before writing, ask:

- What would be expensive or annoying to rediscover?
- What was tried and rejected, and what killed it?
- Which decisions were made, with what reason?
- What is running, blocked, waiting, promised, or not started?
- Which claims are uncertain, and what would settle them?
- What did the user say that has not reached the repository yet?
- What would the next action be if work resumed now?

Half-formed material is welcome when calibrated. Label a hunch as a hunch and record how to check it. Do not launder uncertainty into fact.

## Storage and ownership

In a repository, use `.checkpoints/` at the project root. Outside one, follow the active host's personal state convention. One file belongs to one task or independent work lane:

```text
<YYYY-MM-DD>-<task-slug>.md
```

Use a stable goal-derived slug. Independent writers get independent files; never merge live desks. Checkpoints are local by default. Commit them only when the project's standing convention or the user explicitly treats task state as shared repository history.

Start every file with:

```text
Task: <task-slug> · Written: <YYYY-MM-DD HH:MM> · Scope: <goal and altitude>
```

Then use only the sections that have content:

| Section | Lifetime | Holds |
|---|---|---|
| **Now** | rewrite | Current phase and next concrete action. |
| **Plates** | rewrite | Running, waiting, blocked, promised, or necessary work. |
| **Terrain** | rewrite/merge | Hard-won environment facts not yet durable elsewhere. |
| **Decided** | append | Decisions and their reasons. |
| **Discards** | append | Rejected branches and cause of death. |
| **Live wires** | rewrite | Hunches, contradictions, and calibrated uncertainty. |

Keep each file small enough to read whole on resume. Move finished tasks to `.checkpoints/archive/`; do not delete their reasoning.

For a concrete shape, read [references/example.md](references/example.md).

## Reload

1. Find every unarchived checkpoint relevant to the current project; do not assume the newest supersedes the others.
2. Check live task or agent ownership when the host exposes it. Do not take over another active lane.
3. Read each relevant file whole.
4. Verify volatile state against the repository, running processes, and current tests. Trust checkpoints for reasons; verify them for action.
5. Report what was reloaded, contradictions found, and the next supported action.

If the project contains older state files such as `RESUME.md`, `STATE.md`, or a bare `CHECKPOINT.md`, read [references/adopting-state.md](references/adopting-state.md) before moving or normalizing anything.

## When not to checkpoint

Do not create one for a short, obvious task with no meaningful reasoning or live state. A low-value checkpoint becomes permanent rereading cost.
