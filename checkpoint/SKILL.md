---
name: checkpoint
description: Save session state to a per-session file in .checkpoints/, or reload every live checkpoint when resuming a project.
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

## The files

Checkpoints go in `.checkpoints/` at the project root — a directory, not a single file. Outside a repo: `~/.claude/checkpoints/<project-slug>/`.

One file per session, named `<YYYY-MM-DD>-<session-slug>-<task-slug>.md`. Get the session slug from the first line of `ListAgents`, which names the session you're in (`timmy-7a`, `roots-brain-56`). Pick the filename once, on your first write, and keep writing to that same file for the rest of the session — that's what keeps Decided and Discards genuinely append-only instead of a pile of snapshots.

Why a directory: several agents work the same project from different tasks and different altitudes, and they close out at different times. One shared file means whoever finishes last erases everyone else's thinking, silently. Per-session files make the writes stop competing. Note that a subagent reports its *parent's* session slug, so the slug identifies a session rather than a single writer; the task slug is what separates two subagents of one session.

Every file opens with a header, above the sections:

```
Session: <session-slug> · Written: <YYYY-MM-DD HH:MM> · Scope: <what this agent was working on, and at what altitude>
```

The scope line is what lets a later reader tell overlap from independence. Two checkpoints that both touch the sync layer are a contradiction to resolve if they're the same task and two halves of a picture if one was refactoring and the other was writing tests. Without the line, that's unknowable.

Then six sections:

| Section | Lifetime | Holds |
|---|---|---|
| **Now** | rewrite | One paragraph: what we're doing, what phase, what's next. First thing read, so it goes first. |
| **Plates** | rewrite | Everything in motion — in-flight, background, waiting on the user, promised, known-necessary but unstarted — each with its state and what unblocks it. |
| **Terrain** | rewrite/merge | Hard-won environment facts: paths, commands, gotchas, what broke and how it got fixed. Anything durable enough to outlive the project graduates to CLAUDE.md instead. |
| **Decided** | append | Settled calls, each with its reason — without the reason, future-me relitigates from scratch. |
| **Discards** | append | Killed branches with cause of death. A discard with a recorded reason can be un-killed later; one that vanished silently can't. |
| **Live wires** | rewrite | Hunches, nags, half-baked notions, confidence on shaky claims. As items resolve, promote them to Decided or Discards. |

Skip empty sections; never pad to fill the shape. Keep rewritten sections tight — they're re-read every session. Append sections can grow. Commit checkpoints with the work: the diff history of a checkpoint shows how the thinking moved, which the code history doesn't.

When a thread is genuinely finished — merged, shipped, abandoned on purpose — move its file to `.checkpoints/archive/`. Move, never delete: a closed thread's discard pile is still the reason nobody should retry that branch. Archiving is what keeps "read all of them" on resume from growing without limit, and it's a deliberate act by someone who knows the work is done, not a guess made by a reader who wasn't there.

Same pass: sweep the session's temp and scratch dirs, and record in Terrain anything deliberately left in place and why.

## Reading one back

A checkpoint is a claim about a world that has since moved. Trust it for reasoning, verify it for action:

0. **Look for state that isn't in `.checkpoints/` yet** — a bare `CHECKPOINT.md`, a `RESUME.md`, whatever this project's previous agents hand-rolled. See *Adopting stray state files*. Do this before reading, so the pass below covers everything rather than a subset that happens to be correctly filed.
1. **Read every unarchived file in `.checkpoints/`, newest first — not just the newest one.** Recency does not rank these. The most recent checkpoint isn't a better version of the others; it's a different scope, written by an agent that may have been working a different problem entirely. Picking one and ignoring the rest loses exactly the thinking the directory exists to protect.
2. **Check who's still alive.** Call `ListAgents` and match the session slugs against the filenames. A writer still in the list is actively working — treat its checkpoint as someone else's live desk, don't act on its plates, and message it directly if you need to, since the slug is the address. A writer that's gone means the file is finished thinking and safe to fold into yours. The slug is not durable, though: next week that name may belong to a different session. It answers "is this being worked right now," never "who owns this."
3. Read each file whole — Live wires and Discards change what you'd do, and they're at the bottom.
4. Verify volatile claims against reality before acting: `git status`, `git log`, do the tests still pass. Claims about *state* may be stale; claims about *reasoning* keep.
5. Say what you reloaded, in two lines — the user can't remember the session either. If you read more than one checkpoint, say whose, and say whether they agreed.
6. Flag contradictions rather than silently reconciling — between a file and the code, and between two files. The gap is information either way. Two checkpoints disagreeing about the same task usually means one of them didn't know about the other, and which one was wrong is a question for the user, not something to resolve by timestamp.

## Adopting stray state files

Projects accumulate hand-rolled versions of this file: `CHECKPOINT.md` with no slug (the old format), `COMPACTED.md`, `RESUME.md`, `STATE.md`, `PARKED.md`, `HANDOFF.md`, `CONTEXT.md`, `WIP.md`, `SESSION-NOTES.md`. Names vary and the list never ends, so judge by content, not filename. Do this pass once, the first time this skill runs in a project: `ls` the root and any docs directory, and read anything that might be session state.

**The test is the one the whole skill runs on:** would someone who has read the repo and the full diff still not know this? Session state fails that test — it only ever existed in a conversation. Standing knowledge passes it, and standing knowledge is not yours to move. Three signals settle most cases:

- **Who it's addressed to.** An agent writing to its future self ("next concrete step," "I tried X and it failed," "waiting on the user") versus a document written for a reader who wasn't there. Architecture notes, ADRs, and READMEs are the second thing even when they're informal.
- **Provenance.** `git log --format='%an · %s' -- <file>`. A file the user has been editing by hand across months is theirs.
- **Inbound references.** `grep -rn '<filename>' .` — if the README, CLAUDE.md, or docs link to it, it's part of the project and it stays exactly where it is.

Then one of three verdicts:

- **Session state** → normalize it into its own file in `.checkpoints/`, named `<its-last-modified-date>-adopted-<original-name>.md`, with a scope header recording where it came from. Give it its own file rather than merging it into yours: it's a different session's thinking at a different altitude, and folding it into your checkpoint is the same overwrite this directory exists to prevent. Once the content is preserved, move the original to `.checkpoints/archive/`.
- **Standing knowledge** → leave it untouched. Mention that you found it and moved on.
- **Both, which is the common case** → copy the session-shaped parts into an adopted checkpoint, leave the file in place holding the standing parts, and note in Terrain what moved and where. Never strip a file down to what you think is left.

**Never delete, and prefer asking.** Move originals to `.checkpoints/archive/`; a redundant file costs one re-read, a deleted one costs the thing this skill exists to protect. Anything untracked by git has no other undo, so move it and say so in the same breath. Ask before touching a file you judged mixed or couldn't classify, and ask before adopting more than a couple at once — read `file-batch-safety` first if it's a real pile. When ambiguity survives all three signals, keep the file where it is and put the question in Live wires. Report what you adopted, what you left, and the one command that undoes it.

## When not to

A three-message session doesn't need one. Checkpoint when there's genuinely a state worth reloading: an accumulated design position, live plates, a real discard pile. A bad checkpoint costs more than none, on every future read.
