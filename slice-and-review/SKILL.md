---
name: slice-and-review
description: The slice, commit, adversarial review, fix, commit loop for larger builds.
---

# slice-and-review

the user's loop for bigger builds, previously retyped by hand every time. the shape:

1. **cut the work into slices.** a slice is one coherent, testable change: a feature, a refactor, a migration step. small enough to review in one sitting, big enough to mean something. list the slices before starting; that list is the plan.
2. **build the slice. verify it.** build passes, tests green, or you ran it.
3. **commit.** one commit, message says what and why.
4. **spawn an adversarial review subagent.** its job is to refute, not admire. prompt shape: "review this diff. find real bugs, broken edge cases, and places it doesn't do what the slice claims. do not list nitpicks or praise. if it's clean, say clean." give it the diff and the slice's goal, nothing more.
5. **act on real findings, ignore performed ones.** verify each finding against the code before fixing it: review bots invent problems. fixes stay inside the slice's scope.
6. **commit the fixes.** then next slice.

## rules

- the reviewer never edits. it reports; you fix. two agents writing the same files collide.
- an empty review is a valid review. never invent findings to make the loop look rigorous, and don't accept invented ones.
- scope is fixed at slice-list time. a good idea mid-loop goes to the discard pile or the plan doc, not into the current slice.
- report to the user per slice, one line each: "slice 3 of 6 done: parser swapped, review found an off-by-one in chunking, fixed, committed." payload first.
- if two consecutive reviews come back clean and the remaining slices are mechanical, say so and offer to drop the review step for the rest. the loop serves the quality, never the ritual.
