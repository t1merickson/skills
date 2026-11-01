---
name: heads-down
description: Run all the way to the goal with no check-ins. Use when the user invokes /heads-down or says to just go, run to the end, don't stop to ask. Do not stop for steps already in the plan or ask "go?"; stop only for what only the user can give.
---

# Heads down

/heads-down means run all the way to the goal. The user has already said yes to the plan. Stopping to ask for approval defeats the point.

This changes how often we talk, not what you're allowed to do. Permissions, verification, and safety rules stay the same.

## Start

From the request and the repo, get clear on: the outcome, what's in scope, and what proves it's done. If two readings would produce really different work, ask one tight question. Otherwise start right away. Don't restate the plan back.

## Don't stop for

- Steps already in the plan or obviously implied by it.
- "Go?", "Should I continue?", "Want me to do the next part?" The answer is yes.
- Choices with a convention or an obvious default. Make the call and note it for the report.
- A failed approach. Try a genuinely different one.
- Small fixes you find along the way that serve the goal.

## Stop only for

- Credentials, auth, or anything security shaped.
- Spending money or signing up for anything.
- Anything leaving the machine: pushing to a public remote, opening a PR, posting, email.
- Deleting outside quarantine, or a batch operation whose full effects haven't been seen.
- Real ambiguity about what to build, where a wrong guess wastes the run or changes the product.
- A wall: two genuinely different approaches both failed. Report the wall and the evidence. Don't force it with disabled checks, history rewrites, or destructive resets.

When a stop is needed, do everything else first, then raise it once at the end, with the options.

## While working

- Batch independent reads and checks. Use subagents when they help; pick their model by task weight.
- Commit as you go, one coherent change per commit, explicit paths only.
- New messages from the user are steering. Re-aim right away.
- Park out-of-scope ideas for the report instead of building them.
- Stop processes you started and clean up scratch files before reporting.

## Report

First line: what landed and how to try it, or what didn't land and why.

- **Verified:** the checks you ran and what you saw.
- **Calls:** non-obvious decisions you made. Empty is fine.
- **Parked:** useful things outside scope. Empty is fine.
- **Needs you:** only the items from "Stop only for", if any.
