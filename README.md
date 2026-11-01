# skills-personal

My live [Agent Skills](https://agentskills.io), mostly authored while using Claude Code and written neutrally where the workflow is genuinely portable. They're plain markdown; Codex, ChatGPT, Claude, another compatible agent, or a human can read the format. Skills refer to "the user" — that's whoever runs them. A few encode opinionated defaults (design taste, workflow shape); treat those as starting points and tune to your own.

## What's here

### Working style

| Skill | What it does |
|---|---|
| **[checkpoint](checkpoint/)** | Save task state to a per-task file in `checkpoints/`, or reload it when resuming a project. |
| **[catch-me-up](catch-me-up/)** | Recap where one project stands, rebuilt from live state rather than stale notes. |
| **[handoff](handoff/)** | One self-contained doc so another agent or reviewer can pick up the work cold. Closeout mode files the learnings. |
| **[cut-memory](cut-memory/)** | Audit memory files and cut everything CLAUDE.md or the codebase already records. |
| **[standup](standup/)** | Cross-project recap of where everything stands and what's next. |
| **[heads-down](heads-down/)** | Maximum autonomy with the guardrails hot. Throughput over dialogue. |
| **[slow-mode](slow-mode/)** | Teaching-pace collaboration: one decision per beat; understanding is the deliverable. |
| **[obsess](obsess/)** | Deep immersion on a named topic so the session runs on verified in-context knowledge. Then teach. |
| **[obsess-hero](obsess-hero/)** | A bounded, sourced vault about one person's published work. Explicit-only. |
| **[prediction](prediction/)** | Resolve a forecast into testable claims, stress-test its mechanisms, and record a probability-banded verdict with falsifiers. |
| **[explaining-problems](explaining-problems/)** | The structure for problem reports and any technical explanation longer than a few lines. |
| **[session-audit](session-audit/)** | Audit a bounded local transcript corpus for repeated corrections, workflows, and per-model failures. |
| **[second-loop](second-loop/)** | A human-gated improvement loop for repeated outbound work like applications and pitches. |

### Build loops

| Skill | What it does |
|---|---|
| **[codex](codex/)** | Let Claude consult or delegate to Codex with host-probed model and effort routing. |
| **[claude](claude/)** | Let Codex consult or delegate to Claude while respecting Claude-native permissions and worktrees. |
| **[slice-and-review](slice-and-review/)** | The slice, commit, adversarial review, fix, commit loop for larger builds. |
| **[mock-and-pick](mock-and-pick/)** | The a/b/c static-mock workflow for UI or copy changes with no stated direction. |
| **[show-me](show-me/)** | Show work, a decision, or a comparison visually, in the project's own app or one HTML page. |
| **[crash-debugging](crash-debugging/)** | Diagnose macOS and iOS crash reports with build identity, symbolication grade, evidence, and confidence. |
| **[os-workarounds](os-workarounds/)** | Track upstream workarounds with a repro, issue, owner, and concrete removal test. |
| **[ship-macos](ship-macos/)** | Release a macOS app with credential gates, artifact verification, provenance, and rollback. |
| **[audit-macos-app](audit-macos-app/)** | Read-only audit of an existing Mac app across code health, HIG, menus, accessibility, performance, and release readiness. |

### Design

| Skill | What it does |
|---|---|
| **[interface-integrity](interface-integrity/)** | Design and audit whether interactive product behavior is predictable, truthful, recoverable, and respectful of user control. |
| **[spatial-interfaces](spatial-interfaces/)** | Map contexts, routes, and hierarchy when navigation is confusing or the structure changes. |
| **[transitional-interfaces](transitional-interfaces/)** | Keep identity and position continuous between two interface states. |
| **[macos-defaults](macos-defaults/)** | Best practices for native macOS apps: real-app behavior, menu bar, targets, AppKit vs SwiftUI, HIG design. |
| **[ios-defaults](ios-defaults/)** | Best practices for native iOS apps: real-app setup, targets, UIKit vs SwiftUI, platform conventions. |
| **[apple-native-motion](apple-native-motion/)** | Native Apple motion: springs, gestures, interruption, Reduce Motion. |
| **[apple-ui-copy](apple-ui-copy/)** | Interface text for Apple-platform apps: labels, alerts, errors, empty states, capitalization. |
| **[icon-design](icon-design/)** | Design and package macOS and iOS icons from editable SVG with optical size variants. |
| **[web-design-defaults](web-design-defaults/)** | A base direction for new web systems without rewriting an existing project's stack. |

### Media, files, archives

| Skill | What it does |
|---|---|
| **[offline-archive](offline-archive/)** | Preserve legitimately accessible web material with polite acquisition, provenance, and offline replay. |
| **[brain-wiki](brain-wiki/)** | Sort loose documents into a typed, linked Tolaria or Obsidian vault. Survey, compile a shape, then write. |
| **[synthetic-fixtures](synthetic-fixtures/)** | Recipes for synthetic test media — images, audio, video, data — instead of personal files. |
| **[file-batch-safety](file-batch-safety/)** | Guardrails for batch file operations. Real file loss lives here. |
| **[window-capture](window-capture/)** | Screenshot one macOS app window by window id; never the full screen. |
| **[paper-mcp](paper-mcp/)** | Drive the Paper (paper.design) app over its local MCP server: layers, masks, blends, exports. |
| **[kit](kit/)** | Operate Kit, the font-project toolkit: audits, measuring, curve repair, kerning, specimens. |

### Binary inspection

| Skill | What it does |
|---|---|
| **[hopper-mcp](hopper-mcp/)** | Explicit-only binary inspection through the Hopper Disassembler MCP server. |

## Install

This checkout is the canonical authored source. It contains personal skills only.
Downloaded skills live in `../skills-vendor`, and orchestration lives in
`../skills-brain`. Disabled and archived skills remain in their ownership
collection but are not deployed.

Claude Code uses `~/.claude/skills/`; Codex and other Agent Skills consumers use
`~/.agents/skills/`. Those entries are deployment symlinks, not working copies.

The cross-collection manifest and deployment tool live in
[`../skills-brain`](../skills-brain/README.md). They record personal, vendor,
disabled, and archived skills together without mixing their source trees.

Check the source and compare it with both installed locations:

```bash
make -C ../skills-brain check
make -C ../skills-brain status
```

Preview a reconciliation, then apply the exact same operation after reviewing it:

```bash
make -C ../skills-brain sync
make -C ../skills-brain sync-apply
```

The skills-brain reconciler changes only manifest-owned links. Unknown host entries
are left alone. Restart a host session if a newly linked skill or policy does not
appear immediately.

Edit skills in this repository. When advice truly differs between hosts, prefer a separate host-specific skill or a neutral shared core with host-specific supporting references. Host invocation controls live in native metadata/settings rather than bracketed prose conditionals, so the installed `SKILL.md` remains ordinary, inspectable Agent Skills markdown on both sides.

## Notes

- **`hopper-mcp` needs a paid tool**: the MCP server ships with [Hopper Disassembler](https://www.hopperapp.com), a commercial app.
- **`codex` assumes the `codex` CLI** is installed and authenticated against a ChatGPT subscription.
- **`claude` assumes the `claude` CLI** is installed and authenticated.
- Descriptions are deliberately one line each — they load into the agent's context every turn, so they pay rent per word.

## License

MIT — see [LICENSE](LICENSE).
