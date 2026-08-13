---
name: explaining-problems
description: The structure Tim wants for explaining a bug, design decision, architecture, or deployment surprise at depth. Use when writing a problem report or any technical explanation longer than a few lines — especially before explaining what went wrong in a system Tim hasn't touched this session.
---

# explaining-problems

Write for a smart reader who knows nothing about this system's internals — that's Tim at the start of every session. Start at the beginning. Define each technical term before using it. Don't assume he knows the commands, files, services, lists, databases, or workflows involved. Short sentences, active voice.

For a problem report, cover the normal world first:

1. What the named thing is.
2. Where it exists.
3. Who uses it, and why.
4. Whether it runs automatically or manually.
5. What should normally happen.

Then the break:

6. What is wrong.
7. The exact conditions that cause it.
8. A numbered example using real objects from this system.
9. The result Tim would actually see.
10. How likely this path is in practice.
11. The smallest permanent fix.
12. One focused check to run after the fix.

This is the order to walk, not a form to fill. Skip a step when it genuinely doesn't apply — say nothing rather than pad it. It's for explanations that earn the depth: a bug worth understanding, a design decision, a deployment surprise. A one-line answer to a one-line question stays one line.
