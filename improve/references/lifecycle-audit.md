# Lifecycle audit

Find the implicit state machines: lifecycle rules spread across flags, callbacks, UI, database records, and background jobs. Nobody wrote them down as a state machine, but the app behaves as one, and the bugs live where the pieces disagree.

At `standard` depth this is a light pass: list the workflows, map the top one or two, report what's clearly broken. At `deep` depth or under the `states` variant, run all of it.

Findings still use the format in `audit-playbook.md` under `## Finding format`. This file adds the workflow map and the checks.

## Restraint first

- **Don't turn every variable into a state machine.** A boolean that only drives one spinner is fine. Map a workflow only when it has three or more states, crosses a boundary (process, network, thread, screen, database), or has failed before (check git log and issues).
- **Don't prescribe a library by default.** An enum plus one function that owns transitions fixes most of these. Recommend a state machine library only when the repo already uses one, or when the workflow is complex enough (nested or parallel states, many timers) that hand-rolling costs more. Say why.
- **Preserve intended behavior.** The goal is clearer states and fewer impossible ones, not a redesign. If the right fix changes what users see, flag it as a product decision.

## 1. Find the workflows

Start from the workflows recon named, then search for the signals that one exists:

- Several booleans about the same thing: `isLoading`, `isSaving`, `hasError`, `didFinish`, `isRetrying`.
- Status strings or enums stored in a database column, plus code that checks them in more than one place.
- Timestamps used as state: `cancelled_at`, `completed_at`, `processed_at`, where "null or not" is the real status.
- Callbacks and listeners that set flags: `onSuccess`, `onError`, webhook handlers, delegate methods, `useEffect` cleanups.
- Background jobs, queues, cron tasks, and retries that move a record forward.
- UI that branches on combinations: `if (loading && !error && data)`.
- Comments like "should never happen," "guard against double submit," "hack: reset state."

Rank candidates by how often users hit the workflow and how bad it is when it breaks (money, data loss, stuck accounts, lost work). Map the top ones. List the rest as "not mapped" in the coverage limits.

## 2. Map each workflow

For each mapped workflow, write this map. Every row needs `file:line` evidence.

```markdown
### Workflow: <name in the product's own words>

**Contract**: When the person <does action> on <object>, the app <result>.
It shows <feedback>. If it fails, it keeps <state> and offers <recovery>.

**Source of truth**: <where the real state lives: a DB column, a store, a
server, a file>. Other copies: <caches, UI flags, local state> and how they sync.

| State | How it is represented | Evidence |
|---|---|---|
| draft | `orders.status = 'draft'` | `models/order.ts:14` |
| submitting | `isSubmitting` in component state, no DB value | `Checkout.tsx:88` |

| From | Event | To | Owner (who performs it) | Guard | Evidence |
|---|---|---|---|---|---|
| draft | submit | submitting | `Checkout.tsx` handler | button disabled while submitting | `Checkout.tsx:102` |
| submitting | payment webhook | paid | `webhooks/stripe.ts` | none | `stripe.ts:40` |
```

The contract sentence comes from `interface-integrity`. If it needs hidden conditions or a state means two things, that is itself a finding.

## 3. Check each map

Go down this list for every mapped workflow:

- **Invalid combinations.** Which combinations of flags or fields can the types represent that should never happen (`isLoading && hasError`, `status = 'paid'` with `paid_at = null`)? Can any code path actually produce one?
- **Missing transitions.** States with no way out (stuck records). Events with no handler in some states (`default:` that silently does nothing).
- **Split ownership.** Two places that perform the same transition with different rules. A transition performed in the UI that the server never checks.
- **More than one source of truth.** Copies that can disagree: optimistic UI, caches, a second tab, a second device. Which wins, and does the user see the conflict?
- **Races.** Double submit, two workers taking the same job, a webhook arriving before the request that caused it returns, check-then-act without a lock or transaction.
- **Cancellation.** What happens when the user leaves, closes the window, or presses Cancel mid-flight? Does late completion still write state? Is cleanup done?
- **Retries.** Is the retried step idempotent? Is there a limit and a backoff? Can a retry run after the user cancelled?
- **Partial failure.** Multi-step writes with no transaction or compensation: charged but not recorded, uploaded but not linked.
- **Recovery.** After a crash or restart mid-workflow, does the app resume, roll back, or leave a zombie? Is there any way for a user or an admin to fix a stuck record?

## 4. Confirm before reporting

A suspected lifecycle bug is a hypothesis until the code says otherwise.

- Look for the guard you expect is missing: a DB constraint, a unique index, a lock, a server-side check, a disabled button, a debounce, middleware.
- Look for a test that covers the transition. A passing test on the exact case means it isn't a bug, or the test is wrong. Say which.
- Mark each finding **confirmed** (you traced the path and found no guard) or **hypothesis** (plausible, but you couldn't trace every path). These map to HIGH and MED or LOW confidence. Hypotheses get an "investigate" plan, not a fix plan.

## 5. Recommend the smallest fix

Most fixes are one of these, in order of preference:

1. Add the missing guard where the transition already happens (a constraint, a check, an idempotency key).
2. Replace a cluster of booleans with one enum or tagged union, so impossible combinations can't be represented.
3. Move every transition for the workflow into one function or module that owns it, and make the rest call it.
4. Make the source of truth explicit and derive the other copies from it.
5. Only then: a declared state machine, with or without a library.

Every fix comes with regression tests:

- each allowed transition happens;
- each forbidden transition is rejected (or can't be expressed);
- the race, cancellation, retry, or partial-failure case that prompted the finding;
- recovery from the stuck or half-done state, if the finding was about one.

## 6. Rate who it helps

Each finding names who pays today and who gains from the fix:

- **UX**: users see wrong status, lose work, get stuck, double-charge.
- **DX**: developers can't tell where a transition happens or which state is real; changes need edits in several places.
- **AX**: coding agents misread the workflow, add another flag, or "fix" one copy of a transition and miss the others. An explicit state type and one owning module are things an agent can find with a single search.

Prefer fixes that help all three. When they pull apart, say so. Example: a declared state machine library helps DX and AX, but adds a dependency and a learning curve, and users gain nothing until a bug is fixed with it.

## 7. Report

For the `states` variant, the report runs in this order:

1. **Workflows found**, ranked, one line each. Mark which were mapped.
2. **Workflow maps** for the mapped ones. Offer `show-me` for a diagram when there are several or a map is large.
3. **Findings**, in the standard table, each tagged confirmed or hypothesis.
4. **Coverage limits**: workflows not mapped, code paths not traced (dynamic dispatch, external services, jobs defined outside the repo), and anything only running the app would show.

This is an audit. The fixes go into plans, written only for the findings the user picks.
