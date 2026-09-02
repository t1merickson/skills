---
name: heads-down
description: Run a well-scoped task with maximum autonomy and minimal dialogue while preserving ordinary permissions, safety, verification, and reporting.
---

# Heads down

Use this mode only when the user invokes it or clearly asks for sustained autonomous execution. It changes the interaction pattern, not authority: work decisively inside the requested scope, comply with the host's update requirements, and stop when the task needs a new user decision.

## Entry contract

Before starting, establish four things from the request and repository:

1. The observable outcome.
2. The paths or systems in scope.
3. What evidence will count as complete.
4. The conditions that require stopping.

If two plausible readings would produce materially different work, ask one tight question before beginning. Otherwise start without restating the plan.

## Work posture

- Make mechanical and convention-backed decisions without asking. Record only non-obvious calls for the final report.
- Batch independent reads and checks. Use parallel agents only when the user and host authorize them.
- Follow the host's required commentary cadence. Prefer milestone updates over play-by-play.
- Treat new user input as steering, not noise. Re-aim immediately.
- Park attractive out-of-scope work; do not expand the blast radius.

## Guardrails

- **Permissions do not change.** Dependency installs, commits, external writes, publishing, spending, credentials, and other mutations still follow the user's request and the host's approval system.
- **Verification does not change.** A completion claim must trace to something observed in this run.
- **Reversibility does not change.** Preserve unrelated work, use quarantine for destructive cleanup, and apply `file-batch-safety` before a real batch.
- **No force as problem-solving.** After two genuinely different approaches hit the same wall, report the wall and the evidence. Do not reach for permission bypasses, disabled checks, history rewrites, or destructive resets.
- **One writer per worktree.** Parallel readers are fine; simultaneous writers are not.
- **Leave the machine clean.** Stop processes you started and report deliberate leftovers.

## Report

Lead with what landed and how to try it. Then give:

- **Verified:** exact checks and observed results.
- **Calls:** non-obvious decisions actually made; empty is valid.
- **Parked:** useful observations outside scope.
- **Next:** one small next action, only when one is genuinely useful.

If the requested outcome did not land, say that first and name the remaining blocker. Heads-down succeeds by concentrating interaction at the edges, never by hiding uncertainty.
