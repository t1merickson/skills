---
name: explaining-problems
description: The structure for problem reports and any technical explanation longer than a few lines.
---

# explaining-problems

write for a smart reader who knows nothing about this system. that's timmy at the start of every session. start at the beginning. define each term before you use it. don't assume he knows the commands, files, services, or workflows involved. short sentences. active voice.

problem reports walk this order. the normal world first:

1. what the named thing is.
2. where it exists.
3. who uses it, and why.
4. whether it runs automatically or manually.
5. what should normally happen.

then the break:

6. what is wrong.
7. the exact conditions that cause it.
8. a numbered example using real objects from this system.
9. the result timmy would actually see.
10. how likely this path is in practice.
11. the smallest permanent fix.
12. one focused check to run after the fix.

this is an order to walk, NOT a form to fill. skip a step that doesn't apply. say nothing rather than pad. and it's only for explanations that earn the depth: a bug worth understanding, a design decision, a deployment surprise. a one line answer to a one line question stays one line.
