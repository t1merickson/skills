---
name: window-capture
description: Screenshot one macOS app window by window id. Read before any screen capture; never the full screen.
---

# window-capture

This is a live, shared daily-driver machine. A full-screen grab can expose
unrelated private content, and rearranging windows to line up a shot interrupts
whatever the user was doing. Capture exactly one window, leave the desktop alone.

## The procedure

**1. Get the CGWindowID.** Resolve the installed skill directory from the
current skill location or host registry; do not assume a Claude-only
environment variable. The helper next to this file lists on-screen app windows:

```bash
swift <skill-directory>/windowid.swift Xcode
```

Filter by any substring of the owning app's name (case-insensitive). Output is
`id / size / owner`, one per line. If several windows match and you can't tell
them apart by size, re-run with `--titles` — that's opt-in because a window
title is often a document or folder name, and the user's standing rule is no
inspection beyond what the current task needs.

**2. Capture through the guard.** The wrapper refuses existing output paths,
revalidates the ID immediately before capture, and removes the result if its
pixel dimensions do not match the requested window at 1x or 2x scale.

```bash
<skill-directory>/capture-window.sh <CGWindowID> /tmp/shot.png
```

Do not bypass the wrapper with a raw `screencapture` call. CoreGraphics and
Accessibility window IDs are different, and `screencapture` may silently fall
back instead of rejecting the wrong namespace.

**3. Read the PNG back** to confirm you captured what you meant to, before
showing it to the user. A silent fallback (see below) looks like a successful
command.

## The trap that matters

`screencapture -l` wants a **CoreGraphics window id**. AppleScript and the
Accessibility API report a *different* number for `id of window 1`. Passing that
number does not error — `screencapture` falls back to capturing the whole
screen and exits 0. That is the exact failure this skill exists to prevent:
silent, successful-looking, and it dumps the user's entire desktop into the
transcript.

Only ever source the id from `CGWindowListCopyWindowInfo` (what `windowid.swift`
uses). Never from `osascript`. Dimension verification is the second safety
boundary in case an ID goes stale between listing and capture.

## Constraints

- **Never** capture the full screen — no `screencapture -x`, no region grabs.
- **Never** hide, move, activate, minimize, or resize a window to set up a shot.
  Occluded is fine; the backing store has the pixels.
- If Screen Recording permission is denied, `windowid.swift` still lists ids but
  titles come back empty, and the capture may be blank. Skip the shot and say
  so plainly — never fall back to full-screen as a consolation.
- Only capture the app under development. Other apps' windows are not yours to
  look at, and Chrome is the only browser you may drive at all.
- Clean up `/tmp` shots when the thread is done.

## When not to bother

To merely confirm a change compiles or behaves, a clean build plus tests is
better evidence than a screenshot, and cheaper. Reach for a capture when the
question is genuinely visual — spacing, weight, color, motion end-state — or
when the user asked to see it. They like being offered visual reviews, so offer;
just don't substitute a picture for a passing test.
