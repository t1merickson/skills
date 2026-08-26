# skills

My live [Agent Skills](https://agentskills.io) for Claude Code, written neutrally so anyone can use them. They're plain markdown; any agent (or human) that reads the format can pick them up. Skills refer to "the user" — that's whoever runs them. A few encode opinionated defaults (design taste, workflow shape); treat those as starting points and tune to your own.

## What's here

### Working style

| Skill | What it does |
|---|---|
| **[checkpoint](checkpoint/)** | Save session state to CHECKPOINT.md, or reload it when resuming a project. |
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
| **[codex](codex/)** | Delegate coding to Codex (GPT-5.6) via the codex CLI, with Claude planning and judging. |
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
| **[brain-wiki](brain-wiki/)** | Distill an exported corpus (Notion, Slack, GitHub) into a source-grounded wiki. |
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

Copy any skill's folder into your agent's skills directory. For Claude Code that's `~/.claude/skills/`:

```bash
git clone https://github.com/t1merickson/skills.git
cp -R skills/checkpoint ~/.claude/skills/
```

Restart the session so the skill is picked up. Then edit it — the personalization is the point, and yours will differ.

## Notes

- **`hopper-mcp` needs a paid tool**: the MCP server ships with [Hopper Disassembler](https://www.hopperapp.com), a commercial app.
- **`codex` assumes the `codex` CLI** is installed and authenticated against a ChatGPT subscription.
- Descriptions are deliberately one line each — they load into the agent's context every turn, so they pay rent per word.

## License

MIT — see [LICENSE](LICENSE).
