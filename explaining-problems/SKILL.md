---
name: explaining-problems
description: "Structure a causal explanation when the user asks to understand a mechanism, root cause, postmortem, surprising deployment result, or consequential design rationale beyond a short answer. Do not use merely because a task contains an error, diagnosis, design choice, or deployment step; ordinary implementation and status answers should stay direct."
---

# explaining-problems

Write for a smart reader who knows nothing about this system. Give the verdict in one plain sentence first. Then start at the beginning, define each term before using it, and explain only the commands, files, services, or workflows needed to understand the verdict. Short sentences. Active voice.

Problem reports walk this order. The normal world first:

1. What the named thing is.
2. Where it exists.
3. Who uses it, and why.
4. Whether it runs automatically or manually.
5. What should normally happen.

Then the break:

6. What is wrong.
7. The exact conditions that cause it.
8. A numbered example using real objects from this system.
9. The result the user would actually see.
10. How likely this path is in practice.
11. The smallest permanent fix.
12. One focused check to run after the fix.

This is an order to walk, NOT a form to fill. Skip a step that doesn't apply. Say nothing rather than pad. And it's only for explanations that earn the depth: a bug worth understanding, a design decision, a deployment surprise. A one line answer to a one line question stays one line.
