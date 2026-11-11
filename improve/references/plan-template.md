# Plan template

Every plan is written for an executor with **zero context**. It hasn't seen the advisor session, the audit, the other plans, or any conversation. It may be a smaller, cheaper model. Assume it follows explicit instructions well and is weak at filling gaps, recovering from ambiguity, or knowing when to stop.

Three properties make a plan executable by a weaker model:

1. **Self-contained context.** Everything is in the file: paths, code excerpts, conventions, commands.
2. **Verification gates.** Every step ends with a command and its expected result. The executor never has to judge whether it worked.
3. **Hard boundaries and escape hatches.** An explicit out-of-scope list, and STOP conditions instead of improvising when reality doesn't match the plan.

File naming: `plans/NNN-short-slug.md`, numbered in recommended execution order.

---

## Template

```markdown
# Plan NNN: <Imperative title: what will be true after this plan>

> **Executor instructions**: Follow this plan step by step. Run every
> verification command and confirm the expected result before the next step.
> If a STOP condition occurs, stop and report; do not improvise. When done,
> update this plan's status row in `plans/README.md`, unless a reviewer
> dispatched you and said they maintain the index.
>
> **Drift check (run first)**: `git diff --stat <planned-at SHA>..HEAD -- <in-scope paths>`
> If any in-scope file changed since this plan was written, compare the
> "Current state" excerpts with the live code. A mismatch is a STOP condition.

## Status

- **Priority**: P1 | P2 | P3
- **Effort**: S | M | L
- **Risk**: LOW | MED | HIGH
- **Depends on**: plans/NNN-*.md (or "none")
- **Category**: COR | SEC | PERF | TEST | DEBT | DEP | DX | DOC | LIFE | PERM | DATA | DIR (the finding's prefix)
- **Planned at**: commit `<short SHA>`, <YYYY-MM-DD>
- **Issue**: <GitHub issue URL, only when published with `--issues`; omit otherwise>

## Why this matters

2 to 5 sentences: the problem, what it costs, and what improves when this
lands. Say who gains: users, developers, agents. Intent is what lets the
executor make the right call when a detail is off.

## Current state

The facts the executor needs, inlined. Never "as discussed" or "see audit."

- The relevant files, one line each on their role:
  - `src/orders/api.ts`: order-list endpoint; contains the N+1 (lines 130-160)
- Short excerpts of the code as it is today, with `file:line` markers, so the
  executor can confirm it's in the right place.
- The conventions that apply, with one example file:
  "Errors use the Result pattern; see `src/lib/result.ts` and its use in
  `src/users/api.ts:40-60`. Match it."
- Vocabulary and constraints from intent docs, quoted: `CONTEXT.md` terms to
  use in names, `DESIGN.md` tokens or components to reuse, the ADR this work
  must stay consistent with. The executor hasn't read those docs.

## Model map

(LIFE, PERM, and DATA plans only. Omit otherwise.)

The relevant map as it is today and as it will be after this plan, in the
same table shape as the audit (states and transitions, access rows, or
derived values), with the source of truth and `file:line` evidence. Mark
which rows this plan adds, removes, guards, or moves.

## Commands you will need

| Purpose   | Command                  | Expected on success |
|-----------|--------------------------|---------------------|
| Install   | `pnpm install`           | exit 0              |
| Typecheck | `pnpm typecheck`         | exit 0, no errors   |
| Tests     | `pnpm test -- <filter>`  | all pass            |
| Lint      | `pnpm lint`              | exit 0              |

(Exact commands from this repo, verified during recon, not guessed.)

## Suggested executor toolkit

(Optional. Include only skills or docs that plausibly exist where the
executor runs.)

- Skills to use if available, and for what: "use `swift-concurrency` when
  adding the actor in step 3."
- Docs worth reading first, by path or URL.

## Scope

**In scope** (the only files you may modify):
- `src/orders/api.ts`
- `src/orders/api.test.ts` (create)

**Out of scope** (do NOT touch, even though they look related):
- `src/orders/legacy-api.ts`: deprecated, scheduled for deletion; v1
  clients still depend on it.
- The public response shape. Clients depend on it.

## Git workflow

(Filled in from recon. Match the repo's conventions.)

- Branch: the repo's naming convention, or `advisor/NNN-<slug>` if none.
- Commit per step or logical unit, in the repo's message style. Include one
  example from `git log`.
- Do NOT push or open a PR unless the operator said to.

## Steps

### Step 1: <imperative title>

What to do, precisely, naming files and symbols. Show the target code shape
when it matters (the pattern to produce, not every line).

**Verify**: `<command>` → <expected output>

### Step 2: ...

(Each step small enough to verify alone. Order them so the code never breaks
between steps when possible: add the new path, switch callers, remove the old.)

## Test plan

- New tests: which file, which cases (happy path, the specific bug this plan
  fixes, named edge cases).
- LIFE plans: each allowed transition happens; each forbidden one is
  rejected; plus the race, cancellation, retry, partial-failure, or recovery
  case behind the finding.
- PERM plans: for each entry point in scope, an allowed actor succeeds and a
  disallowed one (another tenant, a removed member, a lower role) is refused.
- DATA plans: every write path in scope refreshes the copy; a delete removes
  it; the rebuild, if added, matches the source.
- The existing test to copy the structure from: "model after
  `src/users/api.test.ts`."
- Verification: `<test command>` → all pass, including N new tests.

## Done criteria

Machine-checkable. ALL must hold:

- [ ] `pnpm typecheck` exits 0
- [ ] `pnpm test` exits 0; new tests for <X> exist and pass
- [ ] `grep -rn "<old pattern>" src/` returns nothing
- [ ] No files outside the in-scope list changed (`git status`)
- [ ] `plans/README.md` status row updated

## STOP conditions

Stop and report back (do not improvise) if:

- The code at the "Current state" locations doesn't match the excerpts.
- A step's verification fails twice after a reasonable fix attempt.
- The fix seems to need an out-of-scope file.
- The assumption "<key assumption>" turns out false.

## Maintenance notes

For whoever owns this code next:

- What future changes will interact with this ("if pagination is added
  here, revisit the batching in step 2").
- What a reviewer should look hard at.
- Follow-ups deliberately left out of this plan, and why.
```

---

## Index file: `plans/README.md`

Written by the advisor after all plans; updated by executors.

```markdown
# Implementation plans

Written by the improve skill on <date>. Execute in this order unless the
dependencies say otherwise. Executors: read the whole plan first, honor its
STOP conditions, and update your row when done.

## Order and status

| Plan | Title | Priority | Effort | Depends on | Status |
|------|-------|----------|--------|------------|--------|
| 001  | ...   | P1       | S      | none       | TODO   |
| 002  | ...   | P1       | M      | 001        | TODO   |

Status values: TODO | IN PROGRESS | DONE | BLOCKED (one-line reason) |
REJECTED (one-line reason: fixed independently, or approach dropped)

## Dependency notes

- 002 needs 001 because <reason>.

## Considered and rejected

- <finding>: not worth doing because <one line>. (So nobody re-audits it.)
```

## Check each plan before finishing it

- Could a model that has never seen this repo execute it with only this file and the repo? If a step needs something from the advisor session, inline it.
- Is every verification a command with an expected result, not a judgment ("make sure it works")?
- Does every step name exact files and symbols, not "the relevant module"?
- Are the STOP conditions about this plan's real risks, not boilerplate?
- Would a reviewer who reads only "Why this matters" and "Done criteria" know what they're approving?
- No secret values anywhere; locations and credential types only.
- The "Planned at" SHA is filled in, and the drift check's paths match Scope.
