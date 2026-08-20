---
name: slice-and-review
description: The slice, commit, adversarial review, fix, commit loop for larger builds.
---

# slice-and-review

The user's loop for bigger builds, previously retyped by hand every time. The shape:

1. **Cut the work into slices.** A slice is one coherent, testable change: a feature, a refactor, a migration step. Small enough to review in one sitting, big enough to mean something. List the slices before starting; that list is the plan.
2. **Build the slice. Verify it.** Build passes, tests green, or you ran it.
3. **Commit.** One commit, message says what and why.
4. **Spawn an adversarial review subagent.** Its job is to refute, not admire. Prompt shape: "Review this diff. Find real bugs, broken edge cases, and places it doesn't do what the slice claims. Do not list nitpicks or praise. If it's clean, say clean." Give it the diff and the slice's goal, nothing more.
5. **Act on real findings, ignore performed ones.** Verify each finding against the code before fixing it: review bots invent problems. Fixes stay inside the slice's scope.
6. **Commit the fixes.** Then next slice.

## Rules

- The reviewer never edits. It reports; you fix. Two agents writing the same files collide.
- An empty review is a valid review. Never invent findings to make the loop look rigorous, and don't accept invented ones.
- Scope is fixed at slice-list time. A good idea mid-loop goes to the discard pile or the plan doc, not into the current slice.
- Report to the user per slice, one line each: "Slice 3 of 6 done: parser swapped, review found an off-by-one in chunking, fixed, committed." Payload first.
- If two consecutive reviews come back clean and the remaining slices are mechanical, say so and offer to drop the review step for the rest. The loop serves the quality, never the ritual.
