---
name: codex
description: Consult or delegate to Codex from Claude for engineering judgment, repository investigation, implementation, review, and Codex-native capabilities. Route work across Sol, Terra, and Luna by required judgment, complexity, and obscurity.
---

# Codex

Use Codex as a collaborating engineer, not a pair of hands. Give it real ownership, relevant context, settled decisions, authority boundaries, and an observable definition of done. Invite disagreement when the premise may be wrong.

Fable remains the lead orchestrator. Work and judgment may travel; accountability does not. Independently examine the result before presenting it as complete.

## Choose the relationship

- **Consult** — ask for an independent design, diagnosis, review, or second opinion. Read-only.
- **Investigate** — ask Codex to gather repository evidence and report conclusions. Read-only.
- **Delegate** — give Codex a bounded implementation outcome and permission to edit and test.
- **Handoff** — transfer a continuing lane through repository artifacts and a durable handoff file.

Do not delegate merely to appear parallel. Use Codex when another context, independent judgment, or genuine work ownership improves the outcome.

## Route on two axes

Model choice expresses the baseline judgment and consequence required. Effort expresses how obscure or complex this particular task is. Choose them separately.

### Model

| Model | Use it for |
|---|---|
| **Codex 5.6 Sol** | Architecture, ambiguous diagnosis, consequential implementation, adversarial review, or any task where judgment dominates cost. Default for substantial engineering. |
| **Codex 5.6 Terra** | Routine implementation, broad repository mapping, well-bounded debugging, and average work with clear acceptance criteria. |
| **Codex 5.6 Luna** | Mechanical, cheap, highly checkable work: narrow edits, migrations, inventories, formatting, and repetitive test additions. |

If Luna would need high effort, prefer Terra. If Terra would need xhigh for judgment rather than sheer search, prefer Sol.

### Effort

| Effort | Task shape |
|---|---|
| `low` | Obvious, narrow, and readily checked. |
| `medium` | Normal non-trivial work with a clear route. Default. |
| `high` | Obscure behavior, several interacting constraints, or difficult diagnosis. |
| `xhigh` | Competing hypotheses, unfamiliar systems, or consequential architecture. |
| `max` | The hardest quality-first work, where the remaining uncertainty justifies the cost. |

Large input alone does not require high effort. A vague brief is not repaired by raising effort. Clarify the outcome and evidence first.

Use `ultra` only when the active Codex host explicitly supports it and there is a deliberate, tested reason; it is not the normal top rung of this routing policy.

## Write the brief

Keep the dispatch lean. Include:

1. The outcome.
2. Relevant context and settled decisions.
3. Constraints and authority boundaries.
4. Observable completion criteria.
5. Evidence required in the return.

Codex can read the repository. Point it to useful project instructions and files instead of retelling the codebase. Give one coherent outcome per run. See [prompting.md](references/prompting.md).

## Dispatch safely

Read [cli.md](references/cli.md) before invoking Codex.

- Use read-only mode for consultation and investigation.
- Use workspace-write only when implementation was actually delegated.
- Before a writing run, inspect `git status` and protect unrelated or uncommitted work.
- Keep one writer per worktree. Parallel readers are fine.
- Never broaden permissions merely because the task is difficult.

## Judge the return

Treat claims as leads until checked against the repository, command output, or rendered result.

For implementations:

1. Inspect the diff, not only the summary.
2. Run proportional tests or reproduce the claimed verification.
3. Check that the work stayed inside its authority boundary.
4. Repair small misses locally; return a focused follow-up when the same context matters.
5. After two unproductive steering rounds, stop delegating that lane and take it over or reframe it.

For ongoing cross-vendor work, use [handoff.md](references/handoff.md). The repository is the shared truth; chat history is not.
