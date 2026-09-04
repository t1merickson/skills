---
name: codex
description: "Explicit-only: consult or delegate to Codex from Claude for a bounded second opinion, investigation, implementation lane, review, or Codex-native capability. Use only when the user asks to invoke Codex or names this skill. Do not use for routine engineering work, ordinary repository investigation, or an incidental mention of Codex."
---

# Codex

Codex is a collaborator, not an answer vending machine. Use it when an independent engineering context, Codex-native capability, or bounded implementation lane improves the outcome. Give it real ownership, relevant evidence, settled decisions, authority boundaries, and an observable definition of done. The calling task remains architect and judge: delegation moves labor, not responsibility for the verdict.

## Choose the relationship

- **Consult:** read-only design, diagnosis, review, or second opinion.
- **Investigate:** read-only repository evidence and conclusions.
- **Delegate:** a bounded implementation with explicit write/test authority.
- **Handoff:** continuing work transferred through repository artifacts and decisions.

Do not delegate merely to appear parallel. Keep one writer per checkout; parallel readers are fine when the active host and user authorize them.

Consultation is different from subcontracting. When your own design or diagnosis will not settle, hand a peer model your actual position and name where it creaks. A neutral summary hides the uncertainty you wanted challenged.

## Select model and effort deliberately

Probe the destination host rather than assuming a model identifier exists. Names, effort support, and availability change. Apply [references/routing.md](references/routing.md) after confirming the host's advertised options.

Choose model tier for baseline judgment/consequence and effort for this task's obscurity. Large input alone does not justify high effort. If “done” cannot yet be written in a paragraph, clarify the outcome before spending more reasoning; otherwise the delegation merely outsources confusion.

## Write the brief

Read [references/prompting.md](references/prompting.md). Include one outcome, relevant context and settled decisions, scope/authority, observable completion criteria, and evidence required in the return. Point to project instructions and files instead of narrating the repository.

## Dispatch within Codex's conventions

Read [references/cli.md](references/cli.md) and verify flags with `codex exec --help`.

- Use read-only sandboxing for consultation and investigation.
- Use workspace-write only for delegated implementation.
- Inspect the worktree before and after a writing run; preserve unrelated changes. For destructive-risk review, look for vanished files and dangerous commands as well as visible diff hunks.
- Respect `AGENTS.md`, skills, rules, approvals, and the repository's branch/history policy.
- Never use danger-bypass flags merely because work is difficult.
- Use a fresh run for independent review and resume for a focused continuation.

## Verify the return

Delegation without judgment is hoping. Collect the final response, but inspect the actual diff and new/deleted files. Reproduce proportional tests yourself; a delegated report that tests passed is a claim, not yet your evidence. Check the authority boundary and surrounding code, not only the changed hunks.

Then choose a verdict: accept, steer with one focused delta, or take the lane back. One or two steering rounds are normal. If repeated steering is unproductive, the brief or ownership split is probably wrong; stop spending context on the same framing.

For continuing cross-vendor work, use [references/handoff.md](references/handoff.md). There is no magical cross-vendor conversational resume: repository state, settled decisions with reasons, and verification commands are the shared truth. Durable work belongs on a real branch in the canonical checkout; a worktree is temporary geography, not the product.
