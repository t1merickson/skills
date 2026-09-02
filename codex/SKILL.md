---
name: codex
description: Consult or delegate to Codex from Claude for engineering judgment, repository investigation, implementation, review, or Codex-native capabilities.
---

# Codex

Use Codex when an independent engineering context, Codex-native capability, or bounded implementation lane improves the outcome. Give it real ownership, relevant evidence, settled decisions, authority boundaries, and an observable definition of done. The calling task verifies the result before presenting it as complete.

## Choose the relationship

- **Consult:** read-only design, diagnosis, review, or second opinion.
- **Investigate:** read-only repository evidence and conclusions.
- **Delegate:** a bounded implementation with explicit write/test authority.
- **Handoff:** continuing work transferred through repository artifacts and decisions.

Do not delegate merely to appear parallel. Keep one writer per checkout; parallel readers are fine when the active host and user authorize them.

## Select model and effort deliberately

Probe the destination host rather than assuming a model identifier exists. Names, effort support, and availability change. Apply [references/routing.md](references/routing.md) after confirming the host's advertised options.

Choose model tier for baseline judgment/consequence and effort for this task's obscurity. Large input alone does not justify high effort. Clarify a vague outcome before spending more reasoning.

## Write the brief

Read [references/prompting.md](references/prompting.md). Include one outcome, relevant context and settled decisions, scope/authority, observable completion criteria, and evidence required in the return. Point to project instructions and files instead of narrating the repository.

## Dispatch within Codex's conventions

Read [references/cli.md](references/cli.md) and verify flags with `codex exec --help`.

- Use read-only sandboxing for consultation and investigation.
- Use workspace-write only for delegated implementation.
- Inspect the worktree before and after a writing run; preserve unrelated changes.
- Respect `AGENTS.md`, skills, rules, approvals, and the repository's branch/history policy.
- Never use danger-bypass flags merely because work is difficult.
- Use a fresh run for independent review and resume for a focused continuation.

## Verify the return

Inspect the diff, reproduce proportional tests, and check the authority boundary. Repair a small miss locally or return one focused follow-up. If repeated steering is unproductive, stop delegating that lane and take it over or reframe it.

For continuing cross-vendor work, use [references/handoff.md](references/handoff.md). Repository state is the shared truth.
