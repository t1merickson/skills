# Briefing Claude

Claude does not need a ceremonial role prompt. Give it a compact contract and ask for plain language.

```text
Outcome or decision: <what must be accomplished or decided>

Context:
- <relevant evidence, file pointers, and settled decisions>

Constraints:
- <what must remain true>
- <what Claude may and may not change>

Acceptance:
- <observable checks>

Return:
- Be concise and use plain language.
- Report evidence, remaining uncertainty, and any changed files or verification.
```

For consultation, ask for the recommendation, the evidence behind it, and the strongest contrary case. For orchestration, name the lanes, dependencies, and decision points without dictating a plan prematurely.

For implementation, specify whether commits are allowed, what tests matter, and which files or behaviors are out of scope. Ask Claude to challenge a premise that would make the assignment wasteful.

Resume a session for corrections that depend on accumulated context. Start fresh for an independent review or after a bad framing.
