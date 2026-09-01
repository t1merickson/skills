# Briefing Codex

Codex performs best with a compact contract, not a transcript dump.

## Minimal brief

```text
Outcome: <what should be true when finished>

Context:
- <relevant files, behavior, and settled decisions>

Constraints:
- <what must remain true>
- <what Codex may and may not change>

Acceptance:
- <observable checks>

Return:
- <summary, files changed, tests/evidence, remaining uncertainty>
```

Add a proposed approach only when it is a real constraint. Otherwise let Codex inspect the repository and form one. Ask it to challenge the premise when a wrong assumption would waste the run.

## Consultations

State the decision you face, the evidence available, and what would change your mind. Ask for a recommendation plus the strongest contrary case. Require file-and-line anchors for repository claims.

## Implementations

Name the owned outcome rather than dictating keystrokes. Be explicit about scope, compatibility, tests, generated files, and whether commits are permitted. Require a clean account of what changed and what could not be verified.

## Follow-ups

Resume the same run when a focused correction benefits from the context it already built. Start fresh when you want an independent review or the first framing was wrong.

Do not use elaborate schemas, XML, or long role instructions unless downstream parsing genuinely needs them.
