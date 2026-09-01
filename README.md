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
| **[session-audit](session-audit/)** | Audit transcripts with subagents for repeated corrections, workflows, and per-model failures. |
| **[claude-md-coach](claude-md-coach/)** | Interview-driven creation and improvement of CLAUDE.md and AGENTS.md files. |
| **[second-loop](second-loop/)** | A human-gated improvement loop for repeated outbound work like applications and pitches. |

### Build loops

| Skill | What it does |
|---|---|
| **[codex](codex/)** | Let Claude consult or delegate to Codex, with explicit model and effort routing. |
| **[claude](claude/)** | Let Codex consult or delegate to Claude, favoring Fable for orchestration and deep judgment. |
| **[slice-and-review](slice-and-review/)** | The slice, commit, adversarial review, fix, commit loop for larger builds. |
| **[mock-and-pick](mock-and-pick/)** | The a/b/c static-mock workflow for UI or copy changes with no stated direction. |
| **[crash-debugging](crash-debugging/)** | Diagnose macOS and iOS crash reports: read the log, symbolicate, name the root cause. |
| **[os-workarounds](os-workarounds/)** | Tag and track workarounds for OS/framework bugs: FB id, observed version, removal condition. |
| **[ship-macos](ship-macos/)** | Release a macOS app: archive, Developer ID export, notarize, staple, DMG or TestFlight. |

### Design

| Skill | What it does |
|---|---|
| **[macos-design](macos-design/)** | Best practices for native macOS apps: real-app behavior, menu bar, targets, AppKit vs SwiftUI, HIG design. |
| **[ios-design](ios-design/)** | Best practices for native iOS apps: real-app setup, targets, UIKit vs SwiftUI, platform conventions. |
| **[web-design-defaults](web-design-defaults/)** | A base web design direction: Base UI, system fonts, no Tailwind, black-and-white minimalism. |

### Media, files, archives

| Skill | What it does |
|---|---|
| **[offline-archive](offline-archive/)** | Scrape a page or web tool into a self-contained offline copy that still works. |
| **[brain-wiki](brain-wiki/)** | Sort loose documents into a typed, linked Tolaria or Obsidian vault. Survey, compile a shape, then write. |
| **[synthetic-fixtures](synthetic-fixtures/)** | Recipes for synthetic test media — images, audio, video, data — instead of personal files. |
| **[file-batch-safety](file-batch-safety/)** | Guardrails for batch file operations. Real file loss lives here. |
| **[window-capture](window-capture/)** | Screenshot one macOS app window by window id; never the full screen. |
| **[paper-mcp](paper-mcp/)** | Drive the Paper (paper.design) app over its local MCP server: layers, masks, blends, exports. |

### Reverse engineering

| Skill | What it does |
|---|---|
| **[hopper-mcp](hopper-mcp/)** | Reverse-engineering macOS binaries with the Hopper Disassembler MCP server. |
| **[hopper-discovery](hopper-discovery/)** | Reference for the Hopper MCP tools: symbols, procedures, strings, annotations. |

## Install

This checkout is the canonical authored source. Claude Code keeps using its native `~/.claude/skills/` convention, while Codex and other Open Agent Skills consumers use `~/.agents/skills/`. The entries in those directories are deployment links back here, not separate working copies.

The manifest in [`skillset.toml`](skillset.toml) records which skills belong on which host. Most are portable; genuinely host-shaped workflows stay host-specific. In particular, `codex` is for Claude calling Codex, while `claude` is for Codex calling Claude. `claude-md-coach`, `cut-memory`, and `session-audit` remain Claude-shaped.

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

Existing managed copies are moved intact to a dated directory under `~/.agent-skill-quarantine/` before their leaf symlinks are created. Unmanaged or vendor-provided skills are never touched. Restart a host session if a newly linked skill does not appear immediately.

Edit skills in this repository. When advice truly differs between hosts, prefer a separate host-specific skill or a neutral shared core with host-specific supporting references. Avoid inline build-time conditionals in `SKILL.md`: the installed source should remain ordinary, inspectable Agent Skills markdown on both sides.

## Notes

- **`hopper-mcp` needs a paid tool**: the MCP server ships with [Hopper Disassembler](https://www.hopperapp.com), a commercial app.
- **`codex` assumes the `codex` CLI** is installed and authenticated against a ChatGPT subscription.
- **`claude` assumes the `claude` CLI** is installed and authenticated.
- Descriptions are deliberately one line each — they load into the agent's context every turn, so they pay rent per word.

## License

MIT — see [LICENSE](LICENSE).
