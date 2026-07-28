# skills

A few [Agent Skills](https://agentskills.io) I've written for my own Claude Code / agent setup, cleaned up and shared. They're plain markdown — any agent (or human) that reads the [Agent Skills](https://agentskills.io) format can pick them up.

## What's here

| Skill | What it does |
|---|---|
| **[claude-md-coach](claude-md-coach/)** | Interview-driven authoring and improvement of CLAUDE.md / AGENTS.md files. Two modes — bootstrap (batched multiple-choice interview → generated file) and tune-up (per-line audit → targeted diffs) — on a mechanism-first principles layer: adherence economy, shape-output-never-reasoning, affect honesty, route-by-kind (hooks vs skills vs prose). The only tool I know of that serves the *global persona* file, not just project memory. Benchmarked +32 points over no-skill baseline on first eval round. |
| **[checkpoint](checkpoint/)** | Flush live session state to a durable `CHECKPOINT.md` so a later session reloads the whole working context — hunches, discards, spinning plates and all — instead of the thin task summary a compaction leaves behind. Built around one rule: the repo is not the payload. |
| **[codex](codex/)** | Delegate coding work to Codex (GPT-5.5) agents via the `codex` CLI, with Claude as the planner and judge. Plan in Claude, implement in Codex, judge in Claude. Covers handoff prompts, the judge loop, mixed Claude+Codex worktree geography, and a gated image-gen subroutine. |
| **[slow-mode](slow-mode/)** | Teaching-pace collaboration where understanding is the deliverable and code is the byproduct. One decision per beat, ask-before-propose, debugging that starts from *your* hypothesis, and pace as a spotlight — slow where the learning is dense, fast through the plumbing. |
| **[heads-down](heads-down/)** | Maximum autonomy with the guardrails hot (formerly `yolo-mode`). Interaction moves to the edges — scope up front, silent middle, auditable decision ledger at the end. Speed comes from cutting questions and narration, never from skipping verification, reversibility, or scope. |
| **[hopper-mcp](hopper-mcp/)** | Reverse-engineer macOS binaries through the [Hopper Disassembler](https://www.hopperapp.com) MCP server — disassembly, decompilation, and behavior analysis, explained in plain language. |
| **[hopper-discovery](hopper-discovery/)** | Tool-level reference for the Hopper MCP surface — symbols, procedures, strings, call graph, address navigation, annotations — for driving a program already open in Hopper. |
| **[window-capture](window-capture/)** | Screenshot a single macOS app window by CoreGraphics window id, without disturbing the desktop or capturing unrelated content. Documents the AppleScript window-id trap that silently turns a window capture into a full-screen one. |
| **[second-loop](second-loop/)** | Interview-driven setup of a human-gated improvement loop for any "send things into the world" task — job hunts, client outreach, pitches. Externalizes your judgment into versioned config, logs outcomes with reasons, and has an agent propose one evidenced change a week that you approve. |

## Install

Copy any skill's folder into your agent's skills directory. For Claude Code that's `~/.claude/skills/`:

```bash
git clone https://github.com/t1merickson/skills.git
cp -R skills/codex ~/.claude/skills/
```

Restart the session so the skill is picked up.

## Notes

- **`hopper-mcp` needs a paid tool.** It drives the MCP server that ships with [Hopper Disassembler](https://www.hopperapp.com) (a commercial app). Without Hopper installed and its MCP server wired into your agent, the skill has nothing to talk to.
- **`codex` assumes the `codex` CLI** is installed and authenticated against a ChatGPT subscription.
- These were written for my own workflow and lightly de-personalized. Tune the trigger phrases and defaults to taste.

## License

MIT — see [LICENSE](LICENSE).
