# Closing the loop: execute, reconcile, issues

Three follow-through flows: dispatching an executor and reviewing its work (`execute`), keeping the plan backlog current (`reconcile`), and publishing plans as GitHub issues (`--issues`).

The founding rule holds: **the advisor never edits source code.** In `execute`, a separate executor subagent edits code in an isolated git worktree. The advisor dispatches, reviews, and gives a verdict, like a tech lead who doesn't push to your branch.

---

## `execute <plan>`: dispatch and review

### Check before dispatching

- The repo is a git repository. Worktree isolation needs one. If not, stop and say so.
- The plan exists, and every plan it depends on shows DONE in `plans/README.md`. If not, stop and name the missing one.
- Run the plan's drift check yourself. If in-scope files changed since "Planned at," refresh the plan first (see `reconcile`). Never hand an executor a stale plan.

### Dispatch

Spawn **one** subagent in an isolated worktree (in Claude Code: a `general-purpose` agent with `isolation: "worktree"`). Use a cheaper model than yours, or the one the user named (`execute 003 haiku`).

The prompt contains:

1. **The full plan text, inlined.** The worktree holds only committed files. If `plans/` is uncommitted, the executor can't read it.
2. This preamble:

> You are the executor for the plan below. Follow it step by step. Run every
> verification command and confirm the expected result before moving on.
> Touch only the in-scope files. If a STOP condition occurs, stop and report.
> Don't improvise around obstacles. Commit in the worktree following the
> plan's git workflow section. One override: do NOT update
> `plans/README.md`; your reviewer maintains it. Before reporting, check
> every claim against an actual tool result from this session. If a
> verification failed or was skipped, say so plainly. Reply in exactly the
> report format below.

3. The report format:

```
STATUS: COMPLETE | STOPPED
STEPS: per step, done or skipped, plus the verification result
STOPPED BECAUSE: (only if STOPPED) which STOP condition, what you saw
FILES CHANGED: list
NOTES: deviations, surprises, judgment calls
```

### Review

A fresh worktree shares git history but not installed dependencies or build output. The executor installs first, and tooling that reads from `dist/` may need one build the plan didn't mention. That's expected, not a deviation.

Review like a tech lead reading a PR against its spec. Never fix anything yourself.

1. **Re-run every done criterion** in the worktree. Don't trust the report.
2. **Check scope.** `git -C <worktree> diff --stat` against the in-scope list. Any file outside it fails review.
3. **Read the whole diff.** Does it solve the problem in "Why this matters"? Does it follow the conventions the plan named?
4. **Read the new tests.** Executors game criteria. A test that asserts nothing passes and proves nothing.

Running verification inside the executor's worktree is fine. It's disposable. The no-mutation rule protects the user's tree.

### Verdict

**Judge documented deviations on merit.** "Don't improvise" exists to stop silent drift. An executor that hits a real obstacle, adapts minimally, and explains it in NOTES did the right thing. Approve it if the change serves the plan's intent and stays in scope. An undocumented deviation fails review.

| Verdict | When | Action |
|---|---|---|
| **APPROVE** | Criteria pass, scope clean, quality holds | Mark DONE in the index. Tell the user: diff summary, worktree path and branch, anything from NOTES. **Merging is the user's call. Never merge, push, or commit to their branch.** |
| **REVISE** | Fixable gaps | Message the same executor with specific feedback ("criterion 3 fails: X; `api.ts:90` swallows the error; use the Result pattern per the plan"). **At most 2 rounds**, then BLOCK. |
| **BLOCK** | STOP condition hit, scope broken beyond repair, or revisions used up | Mark BLOCKED with the reason. Rewrite the plan with what was learned. Tell the user what happened and what changed. |

---

## `reconcile`: keep `plans/` current

Read `plans/README.md` and every plan, then by status:

- **DONE**: spot-check the cheap done criteria on current HEAD. Mark verified. Keep the plan files; they're the record.
- **BLOCKED**: read the reason and investigate the obstacle. Rewrite the plan around it (a new number if the approach changed, in place otherwise), or mark REJECTED with one line why.
- **IN PROGRESS** but stale: tell the user an executor probably died mid-run. Check its worktree if one exists.
- **TODO**: run the drift check. If drifted, confirm the finding still exists (it may have been fixed in passing), then refresh the excerpts and "Planned at" SHA. If it's gone, mark REJECTED ("fixed independently").

Finish with a short report: verified done, refreshed, rejected, and what can run right now.

---

## `--issues`: publish plans as GitHub issues

A modifier on any planning invocation (`/improve --issues`, `/improve security --issues`). The flag is the user's permission to create issues. Never create them without it.

1. **Preflight.** `gh auth status` succeeds and the repo has a GitHub remote. If either fails, write the plans as usual and say why issues were skipped.
2. **Visibility.** `gh repo view --json visibility`. If the repo is public, warn that issues are public and get explicit confirmation before publishing any plan about a vulnerability, a credential location, or anything else sensitive.
3. **Confirm the list.** Show the titles about to become issues; confirm once if interactive.
4. **Create.** Per plan: `gh issue create --title "<plan title>" --body-file <plan file>`. Add the labels `improve` and the category only if they exist or can be created without error; skip labels rather than fail.
5. **Record.** Put each issue URL in the plan's Status block and the index.

The plan file stays the source of truth; the issue is a copy for distribution. Because plans stand alone, the body needs no edits to make sense to whoever picks it up.
