# skills

A few [Agent Skills](https://agentskills.io) I've written for my own Claude Code / agent setup, cleaned up and shared. They're plain markdown — any agent (or human) that reads the [Agent Skills](https://agentskills.io) format can pick them up.

## What's here

| Skill | What it does |
|---|---|
| **[codex](codex/)** | Delegate coding work to Codex (GPT-5.5) agents via the `codex` CLI, with Claude as the planner and judge. Plan in Claude, implement in Codex, judge in Claude. Covers handoff prompts, the judge loop, mixed Claude+Codex worktree geography, and a gated image-gen subroutine. |
| **[slow-mode](slow-mode/)** | Collaborative, teaching-oriented coding. Stops the agentic loop, plans before coding, generates one small step at a time, and pulls you into every meaningful decision. For when you want to *understand* the code, not just receive it. |
| **[yolo-mode](yolo-mode/)** | The opposite of slow-mode. Maximum autonomy — skip the rubber-stamp questions, make sensible defaults, batch tool calls, ship the artifact. Still stops for genuinely destructive operations. |
| **[hopper-mcp](hopper-mcp/)** | Reverse-engineer macOS binaries through the [Hopper Disassembler](https://www.hopperapp.com) MCP server — disassembly, decompilation, and behavior analysis, explained in plain language. |

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
