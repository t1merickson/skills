---
name: checkpoint
description: Flush live session state to a durable markdown file so a later session reloads the whole working context — not just what got done, but the hunches, discards, spinning plates, and half-formed threads a compaction summary strips out. Use when Tim says "checkpoint", "compaction", "flush state", "save context", "dump context", "log everything", "spinning plates", "before you compact" — when auto-compact is visibly approaching, at a phase boundary, before a risky operation, or when handing work to another agent or model. Also covers the read path: use when Tim says "catch me up", "where were we", "read the checkpoint", or when starting real work in a project that already has a CHECKPOINT.md.
---

# Checkpoint: reload the state, not the summary

A compaction summary is optimized for task continuation. It preserves what was done and drops what it was like to be mid-problem — the hunch you hadn't proven, the branch you killed and why, the thing that kept nagging, the aside Tim dropped that never became a task. Those are the expensive parts to rebuild, and they're the first things cut.

A checkpoint is written to restore **disposition**, not just facts. The bar isn't "the next instance can execute the next task." It's "the next instance can *argue about the problem space*" — hold an opinion on the design, know which paths are already dead, feel where the soft spots are. Facts are the cheap half. Write for the other half.

## The one rule: the repo is not the payload

Code, diffs, `git log`, the README, CLAUDE.md — all of it survives compaction perfectly and re-reads in seconds. Restating it in the checkpoint is pure waste that buries the real content.

**The test: would an instance that has read the whole repo and the full diff still not know this?** If they'd know it, cut it. What survives that filter is the stuff that only ever existed in the conversation — and that is the entire point of the file.

This is what separates a checkpoint from a status report. A status report describes the artifact. A checkpoint describes everything *around* the artifact that the artifact doesn't record.

## Write for a reader in a predicament

Not "future me" — too vague, and it invites a diary. Write for someone specific: **a competent stranger who has the repo open, has read the diff, and has no idea why any of it was chosen.** They can see *what* the code does. They cannot see that the obvious approach was tried and abandoned on Tuesday, that a number is a placeholder, that Tim said something in passing that changes the whole direction.

Every line earns its place by answering something that reader would otherwise get wrong or waste an hour rediscovering.

## The recall pass — the load-bearing move

Section headers are a filing system; they don't extract anything. The extraction happens by interrogating yourself before writing. The trap is structural: **the instance writing the checkpoint still has everything in context, so nothing feels missing.** Salience now is a terrible predictor of value later — what feels like noise while you're holding it is exactly what's precious once it's gone.

Run these questions cold, and write down what comes back even when it feels thin:

- What would I be annoyed to have to rediscover?
- What did I decide without mentioning, because it seemed too small to raise?
- What am I only ~60% sure of — and what would actually settle it?
- What did I try that didn't work, and what specifically was the failure?
- **What did I almost say and cut for length?**
- What's running, waiting, blocked, or promised but not started?
- What did Tim say in passing that I haven't acted on?
- What would I do next if nobody interrupted me?
- **What's nagging me that I can't justify yet?**

The two bolded ones are usually the highest-value lines in the file and the first to get silently dropped. They're the difference between reloading a task and reloading a mind.

## Explicit permission for the unearned

The default instinct is to filter for rigor — to write only what's verified, decided, and defensible. **In this file that instinct is wrong and it destroys the thing being preserved.**

Half-formed is allowed. Unjustified is allowed. "This feels wrong and I don't know why" is a legitimate, valuable entry. So is a wild idea that hasn't earned a line of code. So is "I think Tim actually wants X even though he asked for Y" — flag it as a read, not a fact, and write it.

The only hard requirement is **calibration**: mark how sure you are and how it could be checked. A hunch labeled as a hunch costs nothing and might be the most useful line in the file. A hunch laundered as a fact is a landmine. (Related: [heads-down](../heads-down/SKILL.md) uses "ledger" for its end-of-run decision list — a report section, not this file. Different scale, different lifetime.)

## The file

`CHECKPOINT.md` in the project root. Six sections — first three rewritten each flush, next two append-only, last one rewritten:

| Section | Lifetime | Holds |
|---|---|---|
| **Now** | rewrite | One paragraph: what we're doing, what phase, what's immediately next. The orientation payload — first thing read, so it goes first. |
| **Plates** | rewrite | Everything in motion: in-flight work, background jobs, things waiting on Tim, things promised, things known-necessary but unstarted. Each with its state and what unblocks it. |
| **Terrain** | rewrite/merge | Hard-won facts about the environment: paths, commands, gotchas, what lives where, what broke and how it got fixed. Dedupe as it grows. Anything durable enough to outlive the project graduates to CLAUDE.md instead. |
| **Decided** | append | Settled calls, each with its reason. The reason is the whole entry — without it, future-me relitigates from scratch. |
| **Discards** | append | Killed branches with cause of death. Tim's standing rule: a discard whose reason is recorded can be un-killed later when something changes. One that vanished silently can't. |
| **Live wires** | rewrite | Hunches, nags, half-baked notions, what almost got said, confidence on the shaky claims. Rewritten because it tracks the *current* unresolved state — as items resolve, promote them into Decided or Discards rather than leaving them here. |

Skip empty sections; don't pad to fill the shape. Keep the rewritten regions tight — they're re-read every session, so bloat there is a recurring tax. The append regions can grow; archive to `CHECKPOINT-<phase>.md` past roughly a thousand lines.

Commit it with the work. The diff history of a checkpoint is a genuinely useful artifact — it shows how the thinking moved, which the code history doesn't. For work outside a repo, write to `~/.claude/checkpoints/<slug>.md`.

Same pass, while you're in it: sweep the session's temp and scratch dirs, and record in Terrain anything deliberately left in place and why. Scratch that outlives the context explaining it is just litter for the next session to be confused by.

## Reading one back

A checkpoint is a claim about a world that has since moved. Trust it for reasoning, verify it for action:

1. **Read the whole file** before touching anything — the Live wires and Discards sections are the ones that change what you'd do, and they're at the bottom.
2. **Verify the volatile claims** against reality before acting on them: `git status`, `git log`, whether the branch still exists, whether the tests still pass. Anything about *state* may be stale; anything about *reasoning* is still good.
3. **Say what you reloaded**, briefly — Tim can't remember the session either, and a two-line "here's where we were" is how he re-enters too.
4. **Flag contradictions** rather than silently reconciling them. If the file says a thing was decided and the code says otherwise, that gap is information.

## When not to

A three-message session doesn't need one. Checkpoint when there's genuinely a state worth reloading: an accumulated design position, live plates, a real discard pile. Writing one costs a few minutes — a bad one costs more than that on every future read.

## The grounding line

The measure of a checkpoint isn't completeness — it's whether the next instance can pick up the thread mid-thought instead of starting the conversation over. Facts are the easy half. Write down the things you can't quite justify yet; that's the half that actually dies.
