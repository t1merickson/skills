# skills

My live [Agent Skills](https://agentskills.io), mostly authored while using Claude Code and written neutrally where the workflow is genuinely portable. They're plain markdown; Codex, ChatGPT, Claude, another compatible agent, or a human can read the format. Skills refer to "the user" — that's whoever runs them. A few encode opinionated defaults (design taste, workflow shape); treat those as starting points and tune to your own.

## What's here

### Working style

| Skill | What it does |
|---|---|
| **[checkpoint](checkpoint/)** | Save task state to a per-task file in `.checkpoints/`, or reload it when resuming a project. |
| **[cut-memory](cut-memory/)** | Audit memory files and cut everything CLAUDE.md or the codebase already records. |
| **[standup](standup/)** | Cross-project recap of where everything stands and what's next. |
| **[heads-down](heads-down/)** | Maximum autonomy with the guardrails hot. Throughput over dialogue. |
| **[slow-mode](slow-mode/)** | Teaching-pace collaboration: one decision per beat; understanding is the deliverable. |
| **[obsess](obsess/)** | Deep immersion on a named topic so the session runs on verified in-context knowledge. Then teach. |
| **[explaining-problems](explaining-problems/)** | The structure for problem reports and any technical explanation longer than a few lines. |
| **[session-audit](session-audit/)** | Audit a bounded local transcript corpus for repeated corrections, workflows, and per-model failures. |
| **[claude-md-coach](claude-md-coach/)** | Interview-driven creation and improvement of CLAUDE.md and AGENTS.md files. |
| **[second-loop](second-loop/)** | A human-gated improvement loop for repeated outbound work like applications and pitches. |

### Build loops

| Skill | What it does |
|---|---|
| **[codex](codex/)** | Let Claude consult or delegate to Codex with host-probed model and effort routing. |
| **[claude](claude/)** | Let Codex consult or delegate to Claude while respecting Claude-native permissions and worktrees. |
| **[slice-and-review](slice-and-review/)** | The slice, commit, adversarial review, fix, commit loop for larger builds. |
| **[mock-and-pick](mock-and-pick/)** | The a/b/c static-mock workflow for UI or copy changes with no stated direction. |
| **[crash-debugging](crash-debugging/)** | Diagnose macOS and iOS crash reports with build identity, symbolication grade, evidence, and confidence. |
| **[os-workarounds](os-workarounds/)** | Track upstream workarounds with a repro, issue, owner, and concrete removal test. |
| **[ship-macos](ship-macos/)** | Release a macOS app with credential gates, artifact verification, provenance, and rollback. |

### Design

| Skill | What it does |
|---|---|
| **[interface-integrity](interface-integrity/)** | Design and audit whether interactive product behavior is predictable, truthful, recoverable, and respectful of user control. |
| **[macos-design](macos-design/)** | Best practices for native macOS apps: real-app behavior, menu bar, targets, AppKit vs SwiftUI, HIG design. |
| **[ios-design](ios-design/)** | Best practices for native iOS apps: real-app setup, targets, UIKit vs SwiftUI, platform conventions. |
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

### Reverse engineering

| Skill | What it does |
|---|---|
| **[hopper-mcp](hopper-mcp/)** | Explicit-only binary inspection through the Hopper Disassembler MCP server. |

## Install

This checkout is the canonical authored source. Claude Code keeps using its native `~/.claude/skills/` convention, while Codex and other Open Agent Skills consumers use `~/.agents/skills/`. The entries in those directories are deployment links back here, not separate working copies.

This repository contains authored skills only. Third-party or downloaded skills belong in a separate vendor store and may be linked into the host skill directories as unmanaged entries. Do not copy them here or add them to `skillset.toml` unless the user explicitly adopts the material as authored source after reviewing its provenance and maintenance responsibility.

The manifest in [`skillset.toml`](skillset.toml) records which skills belong on which host, which modes require explicit invocation, which skills depend on one another, and which entries carry volatile host or platform facts. Most are portable; genuinely host-shaped workflows stay host-specific. In particular, `codex` is for Claude calling Codex, while `claude` is for Codex calling Claude. `claude-md-coach`, `cut-memory`, and `session-audit` remain Claude-shaped.

Check the source and compare it with both installed locations:

```bash
python3 scripts/manage-skills.py check
python3 scripts/manage-skills.py status
```

Preview a reconciliation, then apply the exact same operation after reviewing it:

```bash
python3 scripts/manage-skills.py link --migrate-existing
python3 scripts/manage-skills.py link --migrate-existing --apply
```

Canonical links and clean Git-tracked sources use Git as their recovery system and are not duplicated into quarantine. A diverged installed copy is moved intact to a dated directory under `~/.agent-skill-quarantine/` only when it contains state Git does not protect. Unmanaged or vendor-provided skills are never touched. For skills marked explicit, reconciliation also writes Codex's `agents/openai.yaml` policy from the repo and atomically merges missing Claude `skillOverrides.<name> = "user-invocable-only"` entries; conflicting user settings block rather than being overwritten. Restart a host session if a newly linked skill or policy does not appear immediately.

Edit skills in this repository. When advice truly differs between hosts, prefer a separate host-specific skill or a neutral shared core with host-specific supporting references. Host invocation controls live in native metadata/settings rather than bracketed prose conditionals, so the installed `SKILL.md` remains ordinary, inspectable Agent Skills markdown on both sides.

## Notes

- **`hopper-mcp` needs a paid tool**: the MCP server ships with [Hopper Disassembler](https://www.hopperapp.com), a commercial app.
- **`codex` assumes the `codex` CLI** is installed and authenticated against a ChatGPT subscription.
- **`claude` assumes the `claude` CLI** is installed and authenticated.
- Descriptions are deliberately one line each — they load into the agent's context every turn, so they pay rent per word.

## License

MIT — see [LICENSE](LICENSE).
