---
name: os-workarounds
description: "Document and manage code that works around a confirmed upstream OS or framework defect, including reproduction evidence, ownership, and a removal condition. Use when evidence supports upstream fault or the user asks to audit tagged workarounds. Do not use for ordinary app bugs, awkward API usage, compatibility code, or speculative framework blame."
---

# OS workarounds

When code exists only because an upstream bug exists, say so at the site. A workaround tag is a claim about fault, not a synonym for awkward API usage.

## Prove the boundary

Reproduce the defect outside project-specific code with the smallest practical fixture. Record the affected OS/SDK, hardware or simulator context when relevant, expected contract, observed result, and a command or test that reproduces it. If the minimal case does not fail, fix the project instead of tagging upstream.

Keep the fixture as the retest harness. File or link an upstream report when practical, but do not make a vendor-specific ticket system mandatory.

## Tag the site

```swift
// WORKAROUND(FB1234567, macOS 15.2): NSTableView drops first responder
// during section reload. Repro: Tests/Repros/TableReload. Remove when the
// repro passes on every supported runtime; owner: Editor team.
```

Every tag includes:

1. the exact `WORKAROUND(` marker;
2. an upstream issue ID or URL, or `pending` while a report awaits user submission;
3. the runtime or SDK where it was observed;
4. a reproducible test or fixture path;
5. an owner and a concrete removal condition.

Use the same marker in every language so `rg -n 'WORKAROUND\('` inventories the codebase.

## Lifecycle

- Retest when a relevant OS, SDK, deployment target, or implementation dependency changes—not on unrelated system updates.
- When fixed, remove the workaround, tag, and obsolete fixture in one reviewable change; record the version that cleared it.
- When still broken, update evidence only if the supported matrix changed.
- During triage, inspect tagged regions early: the compatibility branch may have aged.
- Never use a workaround tag for preference, undocumented convenience, or code whose upstream attribution is still only a hunch.
