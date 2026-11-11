# Implicit models

Some rules every app has, but few write down in one place. Each one ends up spread across UI, server code, database records, and background jobs. The app behaves as if the model exists, and the bugs live where the copies disagree. This file covers three:

| Frame | The unwritten model | Prefix | Variant |
|---|---|---|---|
| [Lifecycle](#lifecycle) | Which states a workflow can be in, and what moves it between them | `LIFE` | `states` |
| [Permissions](#permissions) | Who may do what to which object | `PERM` | `permissions` |
| [Derived data](#derived-data) | What is computed or copied from what, and when it goes stale | `DATA` | `derived` |

At `standard` depth, run a light pass on each frame: list candidates, map the top one, report what's clearly broken. At `deep`, under a frame's variant, or under `models` (all three), run all of it.

Findings use the format in `audit-playbook.md` under `## Finding format`. This file adds the maps and the checks. Read [The method](#the-method), then the frames you're auditing.

## The method

### Restraint

- **Map only what earns a map.** Each frame says when. A boolean that drives one spinner is not a state machine; a single-user local app has no permission model worth mapping.
- **Don't prescribe a library by default.** Plain code (an enum, one function, one module) fixes most of these. Recommend a library only when the repo already uses one, or when hand-rolling clearly costs more. Say why.
- **Preserve intended behavior.** The goal is one clear model and fewer impossible cases, not a redesign. If the right fix changes what users see, flag it as a product decision.

### Map, then check

Rank candidates by how often users hit them and how bad a failure is (money, data loss, exposure of someone else's data, stuck accounts, lost work). Map the top ones with the frame's template. Every row needs `file:line` evidence. List the rest as "not mapped."

Every map names its **source of truth**: where the real answer lives. Most bugs in all three frames come from a second copy that disagrees with it.

### Confirm before reporting

A suspected bug is a hypothesis until the code says otherwise.

- Look for the guard you expect is missing: a constraint, a unique index, a lock, a server-side check, middleware, a scoped query.
- Look for a test that covers the case. A passing test on the exact case means it isn't a bug, or the test is wrong. Say which.
- Mark each finding **confirmed** (traced the path, found no guard) or **hypothesis** (plausible, couldn't trace every path). These map to HIGH and MED or LOW confidence. Hypotheses get an "investigate" plan, not a fix plan.

### Smallest fix first

Each frame lists its fixes in order of preference. The order is the same idea every time: guard the one place that's wrong, then make one owner, then make the model explicit. Every fix comes with regression tests; the plan template lists the cases per frame.

### Who it helps

UX and DX costs are usually plain. AX is easier to miss: a coding agent reading a scattered model finds one copy, changes it, and misses the others. A single named owner (a state type, a `can()` function, an invalidation hook) is something an agent finds with one search. Prefer fixes that help all three. When they pull apart, say so.

### Report

For a frame variant or `models`:

1. **Candidates found**, ranked, one line each. Mark which were mapped.
2. **Maps** for the mapped ones. Offer `show-me` for a diagram when there are several or a map is large.
3. **Findings**, in the standard table, each tagged confirmed or hypothesis.
4. **Coverage limits**: what wasn't mapped, paths not traced (dynamic dispatch, external services, jobs or policies defined outside the repo), and anything only running the app would show.

---

## Lifecycle

Implicit state machines: workflow rules spread across flags, callbacks, UI, database records, and background jobs.

**Map a workflow when** it has three or more states, crosses a boundary (process, network, thread, screen, database), or has failed before (check git log and issues).

**Signals:** several booleans about one thing, a status column checked in several places, callbacks and jobs that move a record forward, UI that branches on flag combinations. Two are easy to miss: timestamps used as state (`cancelled_at`, where "null or not" is the real status), and comments like "should never happen" or "guard against double submit."

```markdown
### Workflow: <name in the product's own words>

**Contract**: When the person <does action> on <object>, the app <result>.
It shows <feedback>. If it fails, it keeps <state> and offers <recovery>.

**Source of truth**: <a DB column, a store, a server>. Other copies:
<caches, UI flags, local state> and how they sync.

| State | How it is represented | Evidence |
|---|---|---|
| draft | `orders.status = 'draft'` | `models/order.ts:14` |
| submitting | `isSubmitting` in component state, no DB value | `Checkout.tsx:88` |

| From | Event | To | Owner | Guard | Evidence |
|---|---|---|---|---|---|
| draft | submit | submitting | `Checkout.tsx` handler | button disabled while submitting | `Checkout.tsx:102` |
| submitting | payment webhook | paid | `webhooks/stripe.ts` | none | `stripe.ts:40` |
```

The contract sentence comes from `interface-integrity`. If it needs hidden conditions, or a state means two things, that is itself a finding.

**Checks:**

- **Invalid combinations.** Which flag or field combinations can the types represent that should never happen (`isLoading && hasError`, `status = 'paid'` with `paid_at = null`)? Can any path produce one?
- **Missing transitions.** States with no way out. Events with no handler in some states (`default:` that silently does nothing).
- **Split ownership.** Two places performing the same transition with different rules. A transition done in the UI that the server never checks.
- **More than one source of truth.** Optimistic UI, caches, a second tab, a second device. Which wins, and does the user see the conflict?
- **Races.** Including a webhook that arrives before the request that caused it returns, and check-then-act without a lock or transaction.
- **Cancellation.** Does work that finishes after the user cancelled or left still write state?
- **Retries.** Is the retried step idempotent? Is there a limit and a backoff? Can a retry run after a cancel?
- **Partial failure.** Multi-step writes with no transaction or compensation: charged but not recorded, uploaded but not linked.
- **Recovery.** After a crash mid-workflow, does the app resume, roll back, or leave a stuck record? Can anyone fix one?

**Fixes, in order:**

1. Add the missing guard where the transition already happens (a constraint, a check, an idempotency key).
2. Replace a cluster of booleans with one enum or tagged union, so impossible combinations can't be represented.
3. Move every transition into one function or module that owns it.
4. Make the source of truth explicit and derive the other copies from it.
5. Only then: a declared state machine, with or without a library.

---

## Permissions

The access model: who may do what to which object. It's usually spread across hidden buttons, route middleware, query filters, database policies, and plan or tier checks.

**Map it when** the app has more than one kind of actor (roles, owners and members, guests, anonymous visitors, API keys, background jobs acting for someone) or objects that belong to someone. Skip single-user local apps.

The framing rules from the playbook's Security section apply: describe the pattern, the impact, and the fix, with no runnable misuse steps.

**`PERM` or `SEC`?** A permissions map that finds a hole reports it as `PERM`. A lone missing check found without a map stays `SEC`. When both turn up the same hole, report it once, as `PERM`.

**Signals:** role checks (`isAdmin`, `role ===`), UI hidden or disabled by role, route guards, queries filtered by `user_id` or `org_id`, row-level security policies, plan or entitlement checks, share links and invite tokens, API key scopes.

```markdown
### Access: <object or area, in the product's own words>

**Source of truth**: <where roles, membership, and ownership live>.
Cached copies: <session claims, tokens, client state> and when they refresh.

| Action | Object | Allowed for | Enforced in UI | Enforced on server | Enforced in data layer | Evidence |
|---|---|---|---|---|---|---|
| delete | project | owner | button hidden | `projects/delete.ts:22` checks owner | none | ... |
| export | project | member | menu item | none | none | `export.ts:9` |
```

Fill one row per action and object that matters. An empty server cell next to a filled UI cell is the most common finding.

**Checks:**

- **UI-only enforcement.** The UI hides the action; the server allows it.
- **Entry points that disagree.** The same action reachable through the main API, a bulk endpoint, an export, a webhook, a background job, a GraphQL resolver, or an admin tool, with different rules on each.
- **Trusting the client about identity.** A user ID, org ID, or role taken from the request body, a query parameter, or an unverified token claim instead of the server's session.
- **Missing ownership or tenant scope.** Objects fetched by ID with no check that they belong to the caller's account or tenant.
- **Indirect paths.** Gaining access through invite, duplicate, transfer, restore from trash, or a share link that outlives its purpose.
- **Stale grants.** A removed member, a downgraded plan, or a revoked key that keeps working because a session, token, or cache still says yes.
- **Default allow.** A branch that falls through to "allowed" when a role or object is unknown.
- **Over-broad automation.** Service accounts, API keys, or agent tokens with more scope than their job needs.

**Fixes, in order:**

1. Add the missing server-side check where the action is handled.
2. One `can(actor, action, object)` function (or the repo's equivalent) that every entry point calls.
3. Enforce scope in the data layer: scoped queries or database policies, so a forgotten check fails closed.
4. Only then: a declared policy table or an authorization library.

For ranking, a confirmed `PERM` hole that exposes or changes someone else's data counts as a security finding.

---

## Derived data

Data computed or copied from other data and stored somewhere: caches, denormalized columns, counters, search indexes, aggregates, thumbnails, client-side stores, generated files. Each copy carries a rule about when it must be refreshed. That rule is usually nowhere in the code.

**Map it when** a stored value can be recomputed from something else, and a wrong or stale value would mislead a user or a later computation. Skip short-lived memoization inside one function.

**Signals:** `cache`, `memo`, `_count`, `last_*`, and `total_*` fields; functions named `invalidate`, `refresh`, `rebuild`, `reindex`, `sync`, `recompute`; TTLs; scripts that "fix counts"; generated files checked into the repo.

```markdown
### Derived: <value, in the product's own words>

**Source of truth**: <the data it is computed from>.

| Derived value | Computed from | Computed when, by whom | Refreshed by | Staleness allowed | Rebuild path | Evidence |
|---|---|---|---|---|---|---|
| `projects.task_count` | `tasks` rows | on task create, `tasks/create.ts:30` | create only | none | none | ... |
| search index | `documents` | job on save | save, not bulk import | minutes | `scripts/reindex.ts` | ... |
```

**Checks:**

- **Write paths that skip the refresh.** The main path updates the copy; the bulk import, admin edit, migration, raw SQL, or delete path doesn't.
- **Deletes that don't propagate.** The source row is gone; the cache entry, index document, or counter still counts it.
- **Counter drift.** Increments and decrements outside a transaction, or in two places with different rules.
- **Read-modify-write races.** Two writers recompute from stale reads and the last one wins.
- **No rebuild path.** If the copy is wrong, nothing can recompute it from the source.
- **Cache keys missing a dimension.** A key without the user, tenant, locale, or permission level serves one person's data to another. That's also a `PERM` finding.
- **Hand-edited generated files.** Output edited by hand that the next generation run will overwrite.

**Fixes, in order:**

1. Delete the copy and compute on read, when that's cheap enough. The best derived data is none.
2. Refresh in the one place every write passes through, and route the stray write paths through it.
3. Add a rebuild command and a check that compares the copy with the source.
4. Only then: a declared dependency graph or a reactive data library.
