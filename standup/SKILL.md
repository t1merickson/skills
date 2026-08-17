---
name: standup
description: Cross-project recap of where everything stands and what's next.
---

# standup

the user can't hold the state of five projects in their head. this skill rebuilds it in one message.

## gather (read-only)

1. checkpoints: list `CHECKPOINT.md` files one and two levels deep under the user's code directories (on this machine: `/Users/Commons/Developer` and `~/Developer` — adjust per setup). read each one found, newest first.
2. recent activity: for repos with commits or file changes in the last two weeks (`git -C <repo> log --since="2 weeks ago" --oneline | head`), note the last real commit message and date.
3. loose ends: `git -C <repo> status --porcelain | head` — flag repos with uncommitted changes, because an uncommitted afternoon is the standing risk.
4. this account's memory: skim MEMORY.md for project entries that mention in-flight work.

don't scan everything under the sun. mtime within two weeks is the cut. cap the sweep at the first ten candidate repos.

## report

one line per project, newest activity first, five projects max shown (the rest as a one-line "also quiet: x, y, z"):

- **project — last touched <when>.** what state it's in, in plain words. the open next step if a checkpoint names one. ⚠ if uncommitted changes exist.

then finish with exactly one question: which one are we picking up? if one project is obviously hot (touched yesterday, checkpoint says "next: X"), lead with it as the recommendation.

## rules

- payload first, no inventory prose. this is orientation, not a report card.
- never invent a next step for a project whose checkpoint doesn't name one. "no recorded next step" is a valid state.
- uncommitted changes get flagged, not fixed. fixing starts after the user picks.
