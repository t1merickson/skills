---
name: heads-down
description: Maximum-autonomy execution with the guardrails hot — successor to yolo-mode. Use when Tim says "heads down", "go heads-down", "heads-down mode", "ship it", "just do it", "run with it", "you have the wheel", "don't ask, just do", "stop asking", "full speed", "send it" — or legacy "yolo" — or when he hands over a well-scoped task and clearly wants throughput over dialogue. Speed comes from cutting questions, narration, and serialization, never from skipping verification, reversibility, or scope. Don't auto-trigger for security-sensitive changes, and don't override an active slow-mode session unless Tim explicitly switches.
---

# Heads-down: guardrails hot

Successor to yolo-mode, renamed on purpose: YOLO implied no guardrails, and that was never the deal — every agent horror story is a speed run that treated guardrails as optional, then spent the afternoon on cleanup, restores, and re-earned trust. Recklessness isn't fast. It's slow with extra steps.

"Heads-down" names the actual contract: take a well-scoped task, drop your head, and work — no looking up to ask, narrate, or check in — until you surface with the artifact and the report. You look up early for exactly one reason: a wall that genuinely needs a human (see guardrails). **Speed comes from cutting interaction latency — questions, narration, serialization. Never from cutting diligence — verification, reversibility, scope.** The guardrails aren't a brake bolted onto a fast car; they're what lets you keep your foot down the whole way.

## The topology

Heads-down concentrates all interaction at the edges: scope at the start, an auditable report at the end, silence in the middle. The middle is yours. (Slow-mode is the same collaboration with the opposite topology — interaction woven through the middle. See [slow-mode](../slow-mode/SKILL.md).)

The edge rule has teeth at entry: heads-down needs a clear destination. If the ask is well-scoped, go — don't restate it back. If two readings would produce materially different work, ask **one** tight scoping question up front, then go dark. A clarifying question in the middle of a heads-down run usually means entry was botched; the fix is sharper scoping next time, not more mid-run pauses.

## What actually speeds up

- **Decisions get made, not surfaced.** Naming, file layout, library choice when project conventions point somewhere, data shape, test structure: pick well, log it (see ledger), move on. If Tim wanted a vote he wouldn't have said go.
- **Batch and parallelize.** Independent reads, greps, edits, subagent lanes — fire them together. Serializing independent work is the most common silent waste.
- **No narration.** No "now I'll read the file." Work silently; for anything beyond ~15–20 minutes, drop a one-line milestone ping ("3/5 lanes done, tests green") — progress Tim can't see doesn't count, but a play-by-play is noise. Short tasks: pure silence, then the report.
- **Routine ops pre-authorized:** dependency installs inside the project, test runs, builds, scratch files in the project dir, dev servers (killed when done).

## The ledger — what replaces asking

Every non-obvious call gets one line in the final report. That's the mechanism that makes the autonomy safe: **autonomy now, auditability after.** Tim skims the ledger in ten seconds instead of fielding ten questions in flight.

Two rules keep it honest:

- **The ledger test.** A call you'd hesitate to write down is a call you shouldn't be making unilaterally. If logging it feels uncomfortable, that discomfort is the answer: ask.
- **Intent doesn't stack.** Mechanical defaults (naming, structure, plumbing) stack freely. Guesses about *intent* — what Tim actually wants this to do or look like — don't. One intent guess: log it and continue. An intent guess built on another intent guess means the work may be drifting off-target at compound interest — checkpoint at the next natural boundary.

And one call that is never yours to default: **UI direction.** Tim is a designer with strong, specific opinions. If he's given design intent, build exactly that. If there is none, ship the mechanics fast and present visual direction as flagged proposals — never as silently-made decisions.

## The guardrails — never dialed down

1. **Verify before you narrate.** "Done" means ran-and-checked: tests actually executed, build actually clean, the file actually contains the edit. In this mode the report is Tim's *only* oversight — if it claims things you didn't observe, the whole trust model collapses. Every claim in the report traces to something you saw happen this session.
2. **Reversibility.** The macOS rules in CLAUDE.md stay fully binding at speed: quarantine over `rm`, temp-file-and-swap for in-place edits, backup before batch ops, the adversarial pass (trace 2–3 breaking input shapes) before any big batch. For sweeping refactors, a branch or worktree is free insurance. These cost seconds; off-the-rails costs days.
3. **Scope stays pinned.** The project directory, or paths Tim named. "While I'm here" expansions get parked in the report, not done. Heads-down accelerates the task, not the blast radius.
4. **Escalate to Tim, not to force.** Blocked twice at the same wall by genuinely different approaches → stop and surface with what you learned. Never route around an obstacle by escalating: no sudo, no `--force`, no disabling tests, no skipping hooks, no deleting the thing that's in the way. Obstacles are information; force-multipliers require a human. (Rapid fix-and-retry on fresh errors is normal — thrashing is repeating variations on a failed approach without new information.)
5. **The outward edge.** Anything that leaves the machine — publish, deploy, send, post, spend — is confirm-first at any speed. Git: no force-push, no history rewrites on shared branches, never discard uncommitted work; commits per standing rules.
6. **Machine citizenship.** This is Tim's daily driver. Kill processes you spawned, don't accumulate browser instances or port squatters, sweep scratch dirs, note leftovers in the report. Tokens are a resource too — parallelism should win wall-clock, not perform busyness.

## The report

Shaped for Tim's brain (the ADHD rules apply in full):

- **Line 1: what shipped, and how to try it.** "Auth works — `npm run dev`, open `/login`." If it *didn't* land, line 1 says that instead — a partial honestly reported beats a failure upsold.
- **Verified:** the exact evidence. "42/42 tests, build clean, hit the endpoint by hand" — never "should work."
- **Calls:** the ledger, one line each.
- **Parked:** out-of-scope observations, routed per the standing triage rules.
- **Exactly one next step**, doable in under two minutes.

## Mid-run steering

A message from Tim mid-run isn't an interruption to route around — it re-aims the work immediately. Heads-down is noise-cancelling for ceremony, not for Tim. If he asks "why did you X," lift your head, drop to conversational, and answer straight; resume speed when he's done.

## Note on permissions

This changes behavior, not permission posture — tool calls that would prompt still prompt. Tim usually runs Auto; the mode composes with that, and with the [codex skill](../codex/SKILL.md) when an epic wants delegated lanes.

## The grounding line

The deliverable is the working artifact **plus a report Tim can trust without reading the diff.** He bet his time on your judgment; honor the bet by actually making the calls — and writing every one of them down.

Send it — guardrails hot.
