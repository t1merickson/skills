---
name: claude
description: Consult or delegate to Claude from Codex for orchestration, independent judgment, repository investigation, implementation, synthesis, and cross-vendor handoffs. Prefer Fable; use Opus selectively; do not route work to Sonnet or Haiku.
---

# Claude

Use Claude when the task benefits from a genuinely independent collaborator, stronger orchestration, or a different style of synthesis—not as ceremony and not as a way to avoid making a decision.

Fable 5 sits at the top of this collaboration ladder and is the preferred orchestrator. Codex remains responsible for checking any Claude work it presents as completed in the current task.

## Choose the relationship

- **Consult** — obtain independent judgment, critique, planning, or product sense. Read-only.
- **Investigate** — ask Claude to map evidence and return a supported conclusion. Read-only.
- **Delegate** — give Claude a bounded outcome with permission to edit and verify.
- **Handoff** — transfer an ongoing lane through repository state and a durable handoff file.

Use a consultation when one sharp answer is enough. Delegate when Claude should own the path to an outcome. Hand off only when the work will genuinely continue in Claude land.

## Route on two axes

Model choice expresses the trust and judgment needed. Effort expresses the obscurity or complexity of the task. Do not use model tier as a substitute for choosing effort.

### Model

| Model | Use it for |
|---|---|
| **Claude Fable 5** | Default. Orchestration, architecture, ambiguous product or technical direction, difficult research and writing, multi-lane synthesis, and consequential consultation or handoff. |
| **Claude Opus 5** | A selective second Claude-family view or a deep, single-lane analysis when Fable is unavailable or Opus is specifically useful. Demand a concise return; its verbosity and token cost are liabilities. |

Do not route work to Claude Sonnet 5 or Claude Haiku. For cheaper average or mechanical work, prefer Codex Terra or Luna instead.

### Effort

| Effort | Task shape |
|---|---|
| `low` | Obvious and tightly bounded. |
| `medium` | Normal consultation or implementation with a clear route. Default. |
| `high` | Obscure behavior, multi-step reasoning, architecture, or difficult diagnosis. |
| `xhigh` | Competing hypotheses, unfamiliar systems, or cross-domain synthesis. |
| `max` | Exceptional, quality-first work where unresolved uncertainty has real consequence. |

For Fable, use medium for bounded consultation, high for meaningful orchestration, xhigh for genuinely obscure cross-system work, and max only for the hardest cases. If Opus appears to need xhigh or max, prefer Fable unless the point is specifically to obtain Opus's independent view.

Large context is not complexity. Raising effort does not repair an underspecified brief.

## Write the brief

Read [prompting.md](references/prompting.md). Include only:

1. The outcome or decision.
2. Relevant evidence and settled decisions.
3. Constraints and authority boundaries.
4. Observable completion criteria.
5. The return format and evidence required.

Ask for plain language and a concise result. Claude can inspect the repository when given tools; do not paste a whole conversation when file pointers and decisions will do.

## Dispatch safely

Read [cli.md](references/cli.md) before invoking Claude.

- For consultation and investigation, expose read-only tools only.
- For implementation, inspect the worktree first and protect unrelated changes.
- Keep one writer per worktree.
- Never use permission-bypass flags.
- Use a fresh session for an independent review; resume only when shared context is valuable.

## Judge the return

Claude's confidence is not evidence. Verify repository claims, inspect diffs, and reproduce important checks. Separate useful judgment from attractive prose.

For delegated implementation:

1. Inspect the actual changes.
2. Run proportional verification.
3. Confirm that scope and settled decisions were respected.
4. Repair small misses locally or send one focused follow-up.
5. After two unproductive steering rounds, take the lane back or reframe it.

For an ongoing handoff, use [handoff.md](references/handoff.md). Repository state is the shared truth.
