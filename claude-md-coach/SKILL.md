---
name: claude-md-coach
description: Interview, audit, create, or improve concise CLAUDE.md and AGENTS.md files while separating shared project policy from host-specific adapters.
---

# CLAUDE.md coach

Standing instruction files spend attention on every task. Keep only information that changes behavior and belongs at that scope.

## Resolve target and authority

Inspect existing `AGENTS.md`, `CLAUDE.md` variants, `.claude/rules/`, imports, hooks, and relevant global files before asking questions. Determine whether the user wants:

- shared project policy;
- Claude-specific project guidance;
- a personal working relationship;
- a tune-up of an existing file.

Prefer one canonical shared source plus the smallest host adapter current tooling requires. Do not duplicate rules across AGENTS.md and CLAUDE.md. Verify the installed Claude version's discovery/import behavior before recommending a shim; host support changes.

Read [references/mechanics.md](references/mechanics.md) when routing files or diagnosing ignored instructions.

## Bootstrap

Read [references/interview.md](references/interview.md). Ask a few conversational questions per round, focusing on repeated corrections, non-obvious commands, costly past failures, desired pushback, autonomy boundaries, and definition of done. Verify project commands before recording them.

Draft only what the evidence supports. Present the file section by section as a proposal and preserve user-authored phrasing when it carries intent.

## Tune up

Read the target whole and classify each instruction:

- load-bearing fact or non-inferable project convention;
- specific output/interaction preference;
- hard invariant better enforced by a hook/test/policy;
- on-demand procedure better placed in a skill or scoped rule;
- formatter/linter concern;
- inferable, duplicate, vague, obsolete, conflicting, or reasoning-constraining text.

Report findings before editing. Then make targeted, reversible diffs unless the user explicitly wants a rewrite. Recheck imports, precedence, command truth, and total instruction weight after the edit.

## Writing rules

Read [references/principles.md](references/principles.md) before first generation.

1. Every line must prevent a likely mistake or preserve a real preference.
2. Write mechanism and boundary in plain language; avoid ritualistic absolutes without rationale.
3. Make instructions observable and scoped. Shape final output, not hidden reasoning.
4. Do not copy repository structure, code, generic language conventions, or long procedures the agent can inspect on demand.
5. Route enforced invariants to deterministic controls; route deferred knowledge to scoped rules/skills; route formatting to tooling.
6. Use pointers to durable docs rather than copied snippets.
7. Named logs, queues, and sections say when empty is valid, or eager agents may fabricate contents.
8. Separate durable rules from temporary counterweights for a particular model generation. Date and review volatile patches.

Read [references/field-lessons.md](references/field-lessons.md) for evidence-derived failure patterns and [references/targets.md](references/targets.md) for project versus personal content.

## Validate

Check that the resulting hierarchy has one authority per rule, no contradictions, no stale commands, no machine-specific paths in portable policy, and no advisory prose pretending to enforce security. Explain what was kept resident, deferred, enforced elsewhere, or deleted—and why.
