---
name: claude-md-coach
description: Interview, audit, create, or improve concise CLAUDE.md and AGENTS.md files while separating shared project policy from host-specific adapters.
---

# CLAUDE.md coach

A standing instruction file is conditioning, not merely configuration: it is read into context and quietly shifts everything the model does afterward. That makes it unusually high-leverage and unusually easy to ruin. Every resident instruction spends adherence against every other one; keep only information that changes behavior and belongs at that scope.

Two different documents are often confused:

1. **Project memory** tells a new teammate what the repository cannot teach quickly: verified commands, non-default conventions, scars, and definition of done.
2. **The personal working relationship** says who the human is, how honest disagreement should work, where autonomy begins and ends, and how communication should fit their mind.

Decide which one you are writing before asking the first question.

## Resolve target and authority

Inspect existing `AGENTS.md`, `CLAUDE.md` variants, `.claude/rules/`, imports, hooks, and relevant global files before asking questions. Determine whether the user wants:

- shared project policy;
- Claude-specific project guidance;
- a personal working relationship;
- a tune-up of an existing file.

Prefer one canonical shared source plus the smallest host adapter current tooling requires. Do not duplicate rules across AGENTS.md and CLAUDE.md. Verify the installed Claude version's discovery/import behavior before recommending a shim; host support changes.

Read [references/mechanics.md](references/mechanics.md) when routing files or diagnosing ignored instructions.

## Bootstrap

Read [references/interview.md](references/interview.md). Ask a few conversational questions per round, focusing on repeated corrections, non-obvious commands, costly past failures, desired pushback, autonomy boundaries, and definition of done. Multiple choice is a starting gun, not a cage: when an answer is surprising, follow it before returning to the questionnaire. The interview is where the material no generator can infer comes from.

Verify project commands before recording them. A stale command is worse than an omitted one because its location grants it standing authority.

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

As a diagnostic, score instructions by **pull from baseline**: how far does this line move the model from what the host already causes it to do? Short contradictions of defaults and structures with no baseline have high pull. Generic encouragement and duplicated host rules have low pull. Facts are a separate class: they exert little behavioral pull but can still be load-bearing.

## Writing rules

Read [references/principles.md](references/principles.md) before first generation.

1. Every line must prevent a likely mistake or preserve a real preference. Ask: “Would removing this cause a recurring failure?”
2. Write mechanism and boundary in plain language; avoid ritualistic absolutes without rationale.
3. Make instructions observable and scoped. Shape final output, not hidden reasoning. “Keep the final message compact” is different from globally suppressing exploration.
4. Do not copy repository structure, code, generic language conventions, or long procedures the agent can inspect on demand.
5. Route enforced invariants to deterministic controls; route deferred knowledge to scoped rules/skills; route formatting to tooling.
6. Use pointers to durable docs rather than copied snippets.
7. Named logs, queues, and sections say when empty is valid, or eager agents may fabricate contents.
8. Separate durable rules from temporary counterweights for a particular model generation. Date and review volatile patches so the file does not fossilize around a model that no longer exists.

Read [references/field-lessons.md](references/field-lessons.md) for evidence-derived failure patterns and [references/targets.md](references/targets.md) for project versus personal content.

## Validate

Check that the resulting hierarchy has one authority per rule, no contradictions, no stale commands, no machine-specific paths in portable policy, and no advisory prose pretending to enforce security. Explain what was kept resident, deferred, enforced elsewhere, or deleted—and why.
