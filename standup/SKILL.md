---
name: standup
description: Recap of where projects stand and what's next, scoped to the folder the session started in.
---

# standup

The user can't hold the state of their projects in their head. This skill rebuilds it in one message. **Scope comes from the working directory** — where the session was started decides what gets reported.

## Pick the scope

Look at the cwd and classify it:

- **A single project** (it has a `.git`, an Xcode project, a package manifest, or a CHECKPOINT.md at its root): report that one project, in depth.
- **An org or container folder** (it contains multiple project directories — e.g. an org folder full of apps): report EVERY project inside it, one level down. All of them. No recency cutoff, no count cap.
- **Neither** (home directory, or somewhere that isn't code): fall back to all of the user's code directories (on this machine: `/Users/Commons/Developer` and `~/Developer` — adjust per setup) and report at the org level.

## Gather (read-only)

Per project in scope:

1. `CHECKPOINT.md` if present — the Now, Plates, and Live wires sections carry the state.
2. Git: last real commit (message and date), current branch, and `git status --porcelain` for uncommitted changes.
3. The project's CLAUDE.md header or README first line when nothing else says what the thing is.

Recency orders the report; it never filters it. A project untouched since spring still gets its line — "quiet" is state, not noise.

## Report

**Org scope:** One entry per project, every project, ordered newest-activity first. Each entry: name, last touched when, plain-words state, the recorded next step if a checkpoint names one, ⚠ if uncommitted changes exist. Quiet projects get the same line with their real dates. This report is allowed to be long — completeness is the point of running it at org level; the under-150-words default does not apply here.

**Single-project scope:** A fuller picture of the one project — what it is, current phase from the checkpoint, the last few commits in plain words, plates in motion, uncommitted changes, and the recorded next step.

Either way, finish with exactly one question: which thread are we picking up? If one is obviously hot, lead with it as the recommendation.

## Rules

- Payload first. This is orientation, not a report card.
- Never invent a next step for a project whose checkpoint doesn't name one. "No recorded next step" is a valid state.
- Uncommitted changes get flagged, not fixed. Fixing starts after the user picks.
