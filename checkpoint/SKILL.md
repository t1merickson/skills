---
name: checkpoint
description: Save in-flight task state to a visible checkpoints/ folder, or reload it before resuming. Fire when the user says they need to compact, asks to log or save anything still in flight, before a long run or risky step, or when resuming work that has checkpoint or older state files (RESUME, STATE, CHECKPOINT, COMPACTED, HANDOFF). Not for "where were we" or "catch me up" recaps; that is catch-me-up. Not for short obvious tasks with nothing live.
---

# Checkpoint

A checkpoint keeps what compaction drops: the unproven hunch, the branch killed and why, the aside the user dropped that never became a task, the work still running in the background.

The repo is not the payload. Code, diffs, history, and docs can be reread. Test every line with: **would someone who read the whole repo and diff still not know this?** If they would, cut it.

Saving and loading state is this skill's whole job. For a recap of where things stand, use `catch-me-up`. It may read checkpoints, but the recap lives there.

## What earns a line

- What would be expensive to rediscover?
- What was tried and rejected, and what killed it?
- Which decisions were made, and why?
- What is running, blocked, waiting, promised, or not started?
- Which claims are uncertain, and what would settle them?
- What did the user say that has not reached the repo yet?
- What is the next action if work resumed now?
- What did I almost say and cut for length? What is nagging me?

The last prompt often recovers the most useful material. Label a hunch as a hunch and say how to check it. Do not turn uncertainty into fact.

## Rules and instructions: sourced only

Record a rule only if the user actually stated it in this work, with where: `"no new deps" (the user, chat, 2026-10-30)`. Never write generic rules from habit or from another tool's defaults, such as "do not commit unless asked". Those contradict `~/.claude/CLAUDE.md`, which already governs and does not need copying. If unsure whether they said it, leave it out.

## Storage

In a repo, use `checkpoints/` at the project root. Visible, never dot-prefixed. Outside a repo, follow the host's personal state convention with a visible folder. One file per task or independent work lane:

```text
checkpoints/<YYYY-MM-DD>-<task-slug>.md
```

Use a stable slug from the goal. Separate writers get separate files; never merge live lanes. Checkpoints are gitignored by default; commit them only if the project already tracks them or the user asks.

Create the file with the script, then fill it. The script owns the filename, header, section order, and `.gitignore` entry:

```bash
<skill-directory>/scripts/new.sh <task-slug> "<goal and scope>" [project-root]
```

Header, exactly:

```text
Task: <task-slug> · Written: <YYYY-MM-DD HH:MM> · Scope: <goal and scope>
```

Delete empty sections; keep the rest:

| Section | Lifetime | Holds |
|---|---|---|
| **Now** | rewrite | Current phase and next concrete action. |
| **Plates** | rewrite | Running, waiting, blocked, promised, or necessary work. |
| **Terrain** | rewrite/merge | Hard-won environment facts not yet written down elsewhere. |
| **Decided** | append | Decisions and their reasons. |
| **Discards** | append | Rejected branches and what killed them. |
| **Live wires** | rewrite | Hunches, contradictions, open uncertainty. |

Keep a file readable in one pass; past roughly 200 lines, archive it and start fresh. `checkpoints/` holds task state only; guides go in `docs/`. Move finished tasks to `checkpoints/archive/`. Keep their decisions and discards: a dead branch with its cause recorded can be reconsidered, one that vanished gets retried.

Shape example: [references/example.md](references/example.md).

## Pre-compact save

When the user says they need to compact, or asks to log what is in flight: update or create the checkpoint now, focused on Now, Plates, and Live wires. Reply with the path and one line on what was saved. No recap.

## Reload

1. Find every unarchived file in `checkpoints/`. Also check for a legacy `.checkpoints/`; move it to `checkpoints/` (merge archives, update `.gitignore`), then read it. Say in one line that you moved it.
2. Check live task or agent ownership when the host shows it. Don't take over another active lane.
3. Read each relevant file whole. Don't assume the newest replaces the others.
4. Check anything volatile you are about to act on (branch, running process, test status) against the real state. Trust checkpoints for reasons; check them before acting.
5. Say what was loaded, any contradictions, and the next action. Then continue the work.

## Older state files

Root files like `RESUME.md`, `STATE.md`, `CHECKPOINT.md`, `COMPACTED.md`, and `HANDOFF.md` are candidates to adopt. Read [references/adopting-state.md](references/adopting-state.md) first. Adopt byte-intact: never carve a file into parts or rewrite its contents.

## When not to checkpoint

A short, obvious task with no decisions and nothing live. A low-value checkpoint is permanent rereading cost.
