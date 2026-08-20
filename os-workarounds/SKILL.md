---
name: os-workarounds
description: Tag and track code that works around OS or framework bugs, so fault and removal conditions stay knowable. Use when a bug turns out to be Apple's, or when writing code that routes around an OS defect.
---

# os-workarounds

When code exists only because someone else's bug exists, say so at the site. Modeled on Apple's own modulemap pattern: every workaround carries the bug id and its removal condition, so the codebase keeps a greppable inventory of "not our fault."

## Before tagging: prove whose fault it is

A workaround tag is a claim. Earn it: reproduce the bug in a minimal case outside the project's own code (a bare Xcode project, a 20-line playground). If the minimal repro shows the framework misbehaving, it's theirs. If it doesn't reproduce, the bug is ours and gets fixed, not tagged. Keep the repro — it's the FB attachment and the retest harness.

## The tag

```swift
// WORKAROUND(FB1234567, macOS 15.2): NSTableView drops first responder
// on section reload. remove when fixed — retest each OS update.
```

Four parts, all required:

1. **`WORKAROUND(` marker** — one spelling, always greppable: `grep -rn "WORKAROUND(" .`
2. **The Feedback Assistant id.** No FB filed yet? That's the prompt: draft the feedback with the minimal repro attached and give it to the user to file (filing goes through their account — it leaves the machine, so it's theirs to send). Tag with `FB-pending` until the number exists, then backfill.
3. **The OS version where the bug was observed.**
4. **The removal condition** — usually "when fixed, retest each OS update," sometimes a specific announced fix version.

Same format in any language: `// WORKAROUND(...)` reads identically in Swift, TypeScript, or CSS comments.

## The lifecycle

- **On every OS or SDK update:** grep the inventory, retest each tag against its minimal repro. Fixed → delete the workaround and the tag in one commit ("remove WORKAROUND(FB1234567): fixed in macOS 15.4"). Still broken → bump the observed-version in the tag.
- **During bug triage:** grep first. A bug inside a tagged region is probably the workaround aging, not new fault. See `crash-debugging` for the diagnosis side.
- **Never tag preferences.** A workaround is for defects — wrong behavior against documented contract — not for "the API is awkward." Awkward gets a normal comment or nothing.
