---
name: checkpoint
description: Save session state to CHECKPOINT.md, or reload it when resuming a project.
---

# Checkpoint: reload the state, not the summary

A compaction summary preserves what was done and drops what it was like to be mid-problem — the unproven hunch, the branch killed and why, the aside the user dropped that never became a task. Those are the expensive parts to rebuild and the first things cut. A checkpoint restores that half: the bar is not "the next instance can execute the next task," it's "the next instance can argue about the problem space."

## The one rule: the repo is not the payload

Code, diffs, git history, CLAUDE.md — all of it survives compaction perfectly and re-reads in seconds. The test for every line: **would someone who has read the whole repo and the full diff still not know this?** If they'd know it, cut it. What survives that filter only ever existed in the conversation — and that's the entire point of the file. They can see *what* the code does; they can't see that the obvious approach died on Tuesday, that a number is a placeholder, that the user said something in passing that changes the direction.

## The recall pass

The trap is structural: the instance writing the checkpoint still has everything in context, so nothing feels missing. Salience now is a terrible predictor of value later. So interrogate yourself before writing, and record what comes back even when it feels thin:

- What would I be annoyed to have to rediscover?
- What did I decide without mentioning, because it seemed too small to raise?
- What am I only ~60% sure of — and what would settle it?
- What did I try that failed, and what specifically was the failure?
- **What did I almost say and cut for length?**
- What's running, waiting, blocked, or promised but not started?
- What did the user say in passing that I haven't acted on?
- What would I do next if nobody interrupted me?
- **What's nagging me that I can't justify yet?**

The bolded two are usually the highest-value lines in the file and the first to get silently dropped.

## Permission for the unearned

The instinct to write only what's verified and defensible destroys the thing being preserved. Half-formed is allowed. "This feels wrong and I don't know why" is a valuable entry. So is "I think the user actually wants X even though they asked for Y" — flagged as a read, not a fact. The one hard requirement is **calibration**: mark how sure you are and how it could be checked. A hunch labeled as a hunch might be the most useful line in the file; a hunch laundered as a fact is a landmine.

## The file

`CHECKPOINT.md` in the project root. Six sections:

| Section | Lifetime | Holds |
|---|---|---|
| **Now** | rewrite | One paragraph: what we're doing, what phase, what's next. First thing read, so it goes first. |
| **Plates** | rewrite | Everything in motion — in-flight, background, waiting on the user, promised, known-necessary but unstarted — each with its state and what unblocks it. |
| **Terrain** | rewrite/merge | Hard-won environment facts: paths, commands, gotchas, what broke and how it got fixed. Anything durable enough to outlive the project graduates to CLAUDE.md instead. |
| **Decided** | append | Settled calls, each with its reason — without the reason, future-me relitigates from scratch. |
| **Discards** | append | Killed branches with cause of death. A discard with a recorded reason can be un-killed later; one that vanished silently can't. |
| **Live wires** | rewrite | Hunches, nags, half-baked notions, confidence on shaky claims. As items resolve, promote them to Decided or Discards. |

Skip empty sections; never pad to fill the shape. Keep rewritten sections tight — they're re-read every session. Append sections can grow; archive to `CHECKPOINT-<phase>.md` past roughly a thousand lines. Commit it with the work: the diff history of a checkpoint shows how the thinking moved, which the code history doesn't. Outside a repo, write to `~/.claude/checkpoints/<slug>.md`.

Same pass: sweep the session's temp and scratch dirs, and record in Terrain anything deliberately left in place and why.

## Reading one back

A checkpoint is a claim about a world that has since moved. Trust it for reasoning, verify it for action:

1. Read the whole file first — Live wires and Discards change what you'd do, and they're at the bottom.
2. Verify volatile claims against reality before acting: `git status`, `git log`, do the tests still pass. Claims about *state* may be stale; claims about *reasoning* keep.
3. Say what you reloaded, in two lines — the user can't remember the session either.
4. Flag contradictions between the file and the code rather than silently reconciling; the gap is information.

## When not to

A three-message session doesn't need one. Checkpoint when there's genuinely a state worth reloading: an accumulated design position, live plates, a real discard pile. A bad checkpoint costs more than none, on every future read.
