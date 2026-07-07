# Mid-epic handoff: checkpoint checklist + brief template

For swapping the labor force (usually Claude → Codex) partway through an
epic. The test the whole protocol serves: **could a competent stranger with
repo access — no chat history — pick up the next task?** Codex is that
stranger. So is next week's Claude session.

## Checkpoint checklist

Work through in order; each step removes a class of handoff failure.

**1. Land the state (git)**
- [ ] All WIP committed on a named branch in the canonical checkout. Commit
      messages say what works and what's half-done — a `wip:` prefix is
      honest and fine. Never hand off via stash, dirty tree, or a diff that
      exists only in a worktree.
- [ ] Agent-scratch worktrees merged or discarded (workspace-geography
      rules). Nothing Codex will read references a `.claude/worktrees/` path.
- [ ] Pushed to the remote if one exists. If none exists, tell the user — an
      agent-heavy epic multiplies the ways a local-only tree dies.

**2. Crystallize the plan (repo file)**
- [ ] Write/update the epic's plan file — `docs/plans/<epic>.md` or the
      project's existing convention. Contents:
      - **Goal** — one paragraph, plus overall done-criteria.
      - **Decisions made + why** — every architectural/API choice already
        settled, each with its one-line rationale. This is what stops a
        fresh agent from relitigating week-one debates.
      - **Done** — completed tasks, with pointers to the commits/files.
      - **Remaining** — discrete tasks, each self-contained enough to
        become one Codex brief (if a task can't be stated without the chat,
        split or clarify it now, while you still have the context).
      - **Verification** — exact commands: build, test, lint, run.
      - **Gotchas** — everything painful discovered so far: flaky tests,
        ordering constraints, platform traps, files that look editable but
        aren't.
- [ ] Commit the plan file. It's product, not scratch.

**3. Note untracked state**
- [ ] `.env`/secrets locations (never their contents), required local
      services and how to start them, seeded test data, anything else git
      doesn't carry. Goes in the plan file's gotchas or a setup section.

**4. Sanity-check the stranger test**
- [ ] Reread the plan file cold. If any remaining task needs conversation
      memory to interpret, fix the file — not the eventual brief.

## Dispatch brief template

One task per run. The brief stays thin because the plan file is fat:

```xml
<task>
Read docs/plans/<epic>.md for full context — goal, decisions already made,
and gotchas. Respect the decisions; do not relitigate them.

Your task is item <N>: <one-sentence restatement>.
Done means: <observable criteria for this task alone>.
</task>

<structured_output_contract>
Return: 1. summary of changes  2. files touched
3. verification performed (exact commands, results)
4. anything you learned that belongs in the plan file's gotchas
</structured_output_contract>

<default_follow_through_policy>
Default to the most reasonable low-risk interpretation and keep going.
</default_follow_through_policy>

<completeness_contract>
Resolve this task fully before stopping.
</completeness_contract>

<verification_loop>
Run <verification commands from the plan file> before finalizing;
fix and re-run on failure.
</verification_loop>

<action_safety>
Keep changes scoped to this task. Other items in the plan's Remaining
list belong to other runs.
</action_safety>
```

Run with the usual implementation settings: `-s workspace-write -C <repo>`,
`-c model_reasoning_effort="xhigh"`, `-o` to the scratchpad, background.

## After each dispatched task

- Judge loop as normal — diff, independent verification, verdict.
- On accept: update the plan file (move the item to Done, absorb any new
  gotchas Codex reported), commit. The plan file only works if it's never
  stale — a stale plan is worse than none, because agents trust it.
- Steering rounds via `codex exec resume --last` work within one dispatched
  task's thread. Across tasks, each run is fresh: the plan file is the
  continuity.
