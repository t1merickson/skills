---
name: claude
description: Consult or delegate to Claude from Codex for independent judgment, repository investigation, implementation, synthesis, or a cross-vendor handoff.
---

# Claude

Use Claude when an independent context, Claude-native capability, or genuine ownership of a bounded lane improves the outcome. Do not delegate for ceremony or to avoid making a local decision. The calling task remains responsible for verifying any result it presents as complete.

## Choose the relationship

- **Consult:** read-only judgment, critique, or product/technical opinion.
- **Investigate:** read-only evidence gathering with a supported conclusion.
- **Delegate:** a bounded outcome with explicit edit/test authority.
- **Handoff:** a continuing lane transferred through repository state and a durable handoff.

One sharp answer usually needs consultation, not a new workstream. Keep one writer per checkout. Hand off only when work will genuinely continue in Claude's context.

## Select model and effort deliberately

Probe the installed CLI and account rather than assuming an alias exists. Model names, effort levels, pricing, and availability change. Apply the local preferences in [references/routing.md](references/routing.md) only after confirming they are supported.

Model choice reflects baseline judgment and desired independence. Effort reflects the obscurity and complexity of this task. Large input is not the same as hard reasoning, and increased effort does not repair an underspecified brief.

## Brief the outcome

Read [references/prompting.md](references/prompting.md). Include:

1. one outcome or decision;
2. relevant evidence and settled decisions;
3. scope and authority boundaries;
4. observable completion criteria;
5. required return evidence and format.

Point to repository files rather than pasting an entire conversation. Invite disagreement when the premise is uncertain.

## Dispatch within Claude's conventions

Read [references/cli.md](references/cli.md) and verify current flags with `claude --help`.

- Use Claude's read-only/plan and tool allowlist controls for consultation.
- Use its normal edit permission mode only when implementation was delegated.
- Respect project `CLAUDE.md`, settings, hooks, agents, and worktree conventions.
- Never use permission-bypass flags as a shortcut.
- Start fresh for independence; resume when shared context is the point.

## Verify the return

Inspect actual files and diffs, reproduce material checks, and distinguish evidence from persuasive prose. Repair a small miss locally or send one focused follow-up. If steering repeats without progress, take the lane back or reframe it.

For continuing work, use [references/handoff.md](references/handoff.md). Repository state and explicit decisions are the shared truth.
