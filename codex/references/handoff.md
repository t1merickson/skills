# Cross-vendor handoff

Use a durable repository file when Claude and Codex will alternate on a lane. Keep it factual and short.

```markdown
# Handoff

## Goal
<end state>

## Current state
<what works, what does not, branch/worktree>

## Settled decisions
- <decision and reason>

## Next action
<one concrete next move>

## Verification
- `<command>` — <result>

## Risks and unknowns
- <unresolved item>
```

The outgoing collaborator updates it after material work. The incoming collaborator reads it, checks repository state, and corrects stale claims before continuing. Do not use it as a diary or paste chat transcripts into it.
