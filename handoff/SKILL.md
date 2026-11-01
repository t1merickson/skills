---
name: handoff
description: Write one self-contained markdown doc so another agent, a PR reviewer, or a future session can pick up the work with zero context. Use on /handoff, "write a handoff", "note for another agent", "handoff doc for the merge agent", "write down everything so it survives", or /handoff closeout / "closeout" at the end of a project or phase. Not for mid-task save points the current session will reload (use checkpoint) or for explaining a root cause to the user (use explaining-problems).
---

# handoff

The reader has none of this conversation. They have the repo, this one file, and nothing else. Write for them.

## Default output

- One file. Default `HANDOFF.md` at the repo or project root. If the user names a path or filename, use that.
- If a `HANDOFF.md` already exists from earlier work, read it first. Update it in place when it covers the same work; otherwise use `HANDOFF-<slug>.md`. Never silently drop someone else's content.
- Never a hidden path, never memory, never a scratch folder.

## What goes in

Use these sections in order. Skip a section only when it's truly empty, and say "none" rather than padding.

1. **Goal.** What we're building or fixing and why, in two or three sentences.
2. **State now.** What works, what doesn't, what's half done. Branch name and last commit hash.
3. **Verified, and how.** Each claim with its check: build passed, tests green (which ones), ran it and saw X. Anything not checked is marked unchecked.
4. **Corners cut and known risks.** Be honest. Shortcuts, hacks, flaky bits, things that will bite later. This is the section reviewers need most.
5. **Data model and schema changes.** Migrations, format changes, anything that touches stored data. "None" if none.
6. **Decisions and rejected paths.** What was chosen, what was tried and dropped, and what killed it, so the reader doesn't retry it.
7. **Open questions.** What's unresolved and who decides it (the user or the next agent).
8. **Next steps.** Numbered, concrete, first one doable right away.
9. **Files.** Absolute paths to every file, doc, log, or artifact referenced above.

Before writing, check the live state you're about to describe: `git status`, `git log -1`, and the latest build or test result if one exists. Don't describe state from memory of earlier in the session.

Keep it tight. A reader should get the picture from the first screen. Detail goes lower.

## Closeout mode

Triggered by "closeout", "/handoff closeout", or asks like "write down everything hard won" or "postmortem, discoveries, my preferences" at the end of a project or phase.

Do everything above, plus move durable knowledge out of the chat into the project's real docs:

- **Postmortems and hard-won findings** go in the project's docs folder (e.g. `docs/`), or a new `docs/NOTES.md` if none exists.
- **API quirks and undocumented behavior** go next to the code or in the project's API docs.
- **The user's stated preferences for this project** go in the project's `CLAUDE.md`. Add to it; don't rewrite what's there. If the repo has no `CLAUDE.md`, ask before creating one.
- Not into memory files, not into hidden folders.

The test for each item: would someone who read the whole repo still not know this? If they'd know it, skip it.

List every doc you added to or changed at the end of the handoff file and in your reply.

## PR handoffs

When the reader is a PR reviewer or merge agent, write the same file, framed as a review note: what changed, what to look at hardest, how it was verified, risks.

Posting it as a PR comment or description sends it off this machine. Only do that if the user asked for it in this request. Otherwise write the file and offer.

## Finishing

1. Write the file.
2. Open it yourself (`open <path>` on macOS) so the user sees it.
3. Reply with the one file to hand over, by absolute path, first line. Then any closeout docs changed. Then anything you couldn't verify.

Committing the handoff follows the repo's normal git rules. In a solo repo, commit it with the work. In a shared repo, ask.
