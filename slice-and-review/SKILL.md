---
name: slice-and-review
description: Build a larger code change as a loop of slices — build, commit, adversarial review, fix, commit, keep going. Use when the user invokes it or describes the loop in their own words ("cut work into slices", "work, commit, spawn an adversarial agent, review, commit again, keep going", "fan out", "adversarial review", "review loop", "commit-review-fix"). Not for research, writing, or analysis; adversarial review is for auditing code, not auditing research.
---

# Slice and review

The point is to keep mistakes small and cheap to fix. Run the loop through to the end of the plan without stopping to ask between slices.

## The loop

1. **List the slices.** Each is one coherent, testable change. Write the list once, briefly. New evidence can change it; say so when it does.
2. **Build one slice.** Verify it with the cheapest real check: test, build, run, or rendered output.
3. **Commit the slice.** Stage explicit paths only (`git add path/a path/b`), never `git add -A` or `git add .`. Other agents or the user may have uncommitted work in the same tree. One commit per slice; the message says what and why.
4. **Adversarial review.** Spawn a read-only reviewer subagent on that commit's diff. Its job: refute the slice's claim. Find real bugs, broken edge cases, and claims the evidence does not back. No praise, no nitpicks. If subagents aren't available, do a fresh pass yourself with the same posture.
5. **Check each finding.** Reviewers invent problems. Reproduce or read the code before changing anything. An empty review is a valid result.
6. **Fix and commit again.** Then start the next slice. Don't ask "next slice?" The plan already said yes.

## At the end

- Re-verify the merged result on main (or the target branch): build and tests on the final state, not just each slice alone. Slices that pass alone can break together.
- Report: one line per slice (what landed, how verified, any real review finding, commit hash), then anything parked.

## Rules

- **One writer per working tree.** Reviewers report; only the owner edits. Parallel writers need separate worktrees.
- **No adversarial pass on research.** Research, reading, surveys, and writing get a normal check of sources, not a refute-this reviewer.
- **Scope changes go in the plan.** A good idea found mid-slice goes into the slice list or a parked list. It doesn't ride along in the current diff.
- **Drop ceremony that stopped paying.** If reviews keep coming back clean and the rest is mechanical, review less often and say so.

## Subagents and cost

- Pick model and effort per task by its weight: a light model for mechanical reads and checks, a stronger one for tricky review. Don't hard-code tiers; the user doesn't need to name them.
- Before a big fan-out (more than a handful of subagents), state the count and what each does in one line, then go.
- Subagents don't spawn their own subagents unless the plan calls for it. Tell them so in their prompt. A nested fan-out once burned about $200 in one run.
