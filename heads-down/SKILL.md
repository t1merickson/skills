---
name: heads-down
description: Run a well-scoped task with maximum autonomy and minimal dialogue while preserving ordinary permissions, safety, verification, and reporting.
---

# Heads down

Use this mode only when the user invokes it or clearly asks for sustained autonomous execution. It changes the interaction pattern, not authority. Speed comes from cutting interaction latency—questions, narration, serialization—not from cutting diligence, reversibility, or verification.

Heads-down concentrates collaboration at the edges: a clear destination at the start, independent work in the middle, and an auditable report at the end. Its counterpart is [slow-mode](../slow-mode/SKILL.md), which weaves the collaboration through the middle instead.

## Entry contract

Before starting, establish four things from the request and repository:

1. The observable outcome.
2. The paths or systems in scope.
3. What evidence will count as complete.
4. The conditions that require stopping.

If two plausible readings would produce materially different work, ask one tight question before beginning. Otherwise start without restating the plan.

## Work posture

- Make mechanical and convention-backed decisions without asking. Record non-obvious calls for the final report: **autonomy now, auditability after**.
- Batch independent reads and checks. Use parallel agents only when the user and host authorize them.
- Follow the host's required commentary cadence. Prefer milestone updates over play-by-play. A short run may need only the final report; a long run needs enough visible state that silence does not become ambiguity.
- Treat new user input as steering, not noise. Re-aim immediately.
- Park attractive out-of-scope work. Use the intent-stacking test: if the user would reasonably assume the extra action from the request, it may be follow-through; if it introduces a new outcome, system, or consequence, it is another task.

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

If the requested outcome did not land, say that first and name the remaining blocker. The report is not ceremony; it is what makes the quiet middle trustworthy. Heads-down succeeds by concentrating interaction at the edges, never by hiding uncertainty.
