---
name: slice-and-review
description: Build a larger change as coherent, testable slices with reversible persistence and adversarial review between slices.
---

# Slice and review

Use this loop when the user invokes it or when a requested build is large enough that independent, reviewable milestones materially reduce risk.

1. **List the slices.** Each is one coherent, testable outcome. The list is a plan, not a promise that new evidence cannot change it.
2. **Build one slice.** Keep its changes and verification legible on their own.
3. **Persist reversibly.** Commit when commits are authorized. Otherwise use a staged diff, patch, checkpoint, or another repository-safe boundary.
4. **Review adversarially.** Use an independent read-only reviewer when delegation is available and authorized. Otherwise perform a fresh local pass against the slice goal and diff. Look for real bugs, broken edge cases, and claims the evidence does not support; omit praise and nitpicks.
5. **Verify findings.** Reviewers invent problems. Reproduce or inspect each finding before changing code.
6. **Fix within the slice and persist again.** Then advance.

## Rules

- One writer per worktree. A reviewer reports; the owner edits.
- An empty review is valid. Never manufacture findings to make the ritual look rigorous.
- A scope change updates the remaining slice plan explicitly. It does not sneak into the current slice.
- Verification is proportional to risk and observable: tests, builds, rendered output, or a focused manual check.
- Report each completed slice in one line: outcome, verification, meaningful review finding, and persistence boundary.
- If repeated reviews are clean and the rest is mechanical, drop redundant review steps. The loop serves quality, not ceremony.
