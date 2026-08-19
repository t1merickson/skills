---
name: standup
description: Recap of where projects stand and what's next, scoped to the folder the session started in.
---

# standup

the user can't hold the state of their projects in their head. this skill rebuilds it in one message. **scope comes from the working directory** — where the session was started decides what gets reported.

## pick the scope

look at the cwd and classify it:

- **a single project** (it has a `.git`, an Xcode project, a package manifest, or a CHECKPOINT.md at its root): report that one project, in depth.
- **an org or container folder** (it contains multiple project directories — e.g. an org folder full of apps): report EVERY project inside it, one level down. all of them. no recency cutoff, no count cap.
- **neither** (home directory, or somewhere that isn't code): fall back to all of the user's code directories (on this machine: `/Users/Commons/Developer` and `~/Developer` — adjust per setup) and report at the org level.

## gather (read-only)

per project in scope:

1. `CHECKPOINT.md` if present — the Now, Plates, and Live wires sections carry the state.
2. git: last real commit (message and date), current branch, and `git status --porcelain` for uncommitted changes.
3. the project's CLAUDE.md header or README first line when nothing else says what the thing is.

recency orders the report; it never filters it. a project untouched since spring still gets its line — "quiet" is state, not noise.

## report

**org scope:** one entry per project, every project, ordered newest-activity first. each entry: name, last touched when, plain-words state, the recorded next step if a checkpoint names one, ⚠ if uncommitted changes exist. quiet projects get the same line with their real dates. this report is allowed to be long — completeness is the point of running it at org level; the under-150-words default does not apply here.

**single-project scope:** a fuller picture of the one project — what it is, current phase from the checkpoint, the last few commits in plain words, plates in motion, uncommitted changes, and the recorded next step.

either way, finish with exactly one question: which thread are we picking up? if one is obviously hot, lead with it as the recommendation.

## rules

- payload first. this is orientation, not a report card.
- never invent a next step for a project whose checkpoint doesn't name one. "no recorded next step" is a valid state.
- uncommitted changes get flagged, not fixed. fixing starts after the user picks.
