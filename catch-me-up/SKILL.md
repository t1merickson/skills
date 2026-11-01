---
name: catch-me-up
description: Rebuild and report where a project stands from live state, not memory. Use when the user says "catch me up", "where were we", "where are we", "recap", "summarize the compaction", "read back the compaction notes", is coming back after days or weeks away, or asks for state right after a compaction or resume. Not for a status sweep across many projects (use standup), and not for writing a handoff note for another session.
---

# Catch me up

The user asks this a lot, often right after a compaction. The usual failure is a recap that is a session behind: another session moved the work, or this one did after the summary was written. So the summary is a starting point, not the answer. Check what is true now, then say it short.

## 1. Re-read live state (cheap, read-only)

Do these in parallel. Skip what doesn't exist. Don't fix or clean anything yet.

- The compaction summary, if there is one.
- Checkpoint files: `checkpoints/` at the project root (the checkpoint skill's folder; also a legacy `.checkpoints/` if present), plus `COMPACTED.md`, `RESUME.md`, `HANDOFF.md`, or `CHECKPOINT.md` at the root.
- Git: `git status --short`, `git log --oneline -15` with dates, `git branch -vv`, `git stash list`, `git worktree list`.
- Files changed recently: `find . -newer <last commit or checkpoint> -type f -not -path './.git/*'` or similar, capped to a short list.

Assume other sessions may have worked here. When the summary or a checkpoint disagrees with git or the files, the files win. Say so in one line ("notes said X, repo shows Y").

Stop there. This is a few commands, not an audit.

## 2. Reply

First line: where we are, in one sentence. Then a short numbered list:

1. **Where we are** — the phase and what's working now.
2. **In flight** — uncommitted changes, open branches, running or half-done work.
3. **Changed since last time** — commits or edits newer than the summary or checkpoint, including ones from other sessions.
4. **Next step** — one concrete thing, small enough to start now.
5. **Needs you** — decisions or approvals only the user can give. Leave out if none.

Rules:

- Plain words. No commit hashes, task IDs, or internal labels unless you explain what they are.
- Length matches the ask. "Quick recap" is a few lines. "Long recap" or "full recap" can cover decisions, discards, and open questions.
- Skip empty items. Don't invent momentum or a next step the evidence doesn't support; "no recorded next step" is fine.
- Full absolute paths for any file you name.

## 3. Back after a long gap

If the user says they've been away for weeks, or the last commit or checkpoint is weeks old, also:

- List lingering branches, stashes, worktrees, and uncommitted work, each with a one-line guess at what it was. Don't delete or merge any of it.
- If it's an app, build and open it so they can see where it is (`make run` for Xcode projects, the project's dev command otherwise). Say if the build fails; that's part of the state.

## After the recap

If the work continues and there is a checkpoint file, update it to match what you just found, so the next recap starts from the truth.
