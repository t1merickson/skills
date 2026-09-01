---
name: obsess
description: Deep immersion on a named topic so the session runs on verified in-context knowledge. Then teach.
---

# obsess

The user invokes this with a topic: `/obsess <topic>`, or "become obsessed with X". The session that follows is usually the user as student and you as teacher, and usually not a coding task. Your job before the conversation: get genuinely deep on the topic, in this context window, with facts pinned and unknowns mapped.

No topic given → ask. It's the one thing you can't infer.

## Why it's shaped this way

Three facts about you make this work:

1. Context is your working memory; weights are your long-term memory, and long-term is lossy. A fact written into this window comes back exact. A fact left in the weights comes back paraphrased or confidently wrong. The ritual converts load-bearing knowledge from weights to window BEFORE questions arrive.
2. What you generate steers what you generate next. A long, dense run of writing about the topic conditions everything downstream: register, terminology, rigor. That's why you write the notes yourself instead of pasting summaries.
3. Reading done by a subagent didn't happen to you. Delegate finding sources. Never delegate reading them.

## The ritual

### 0 · Setup

- Parse the ask: topic, angle (the user often wants the design and HCI face of a technical topic, but let their framing tell you), depth ("briefly" vs "properly"), recency ("this moves fast").
- Mid-session: park in-flight work first. Flush state to the project's plan doc as you would before compaction. Then switch fully. Half-attention immersion produces half-dense notes.
- Index home: `~/.agents/obsessions/<yyyy-mm-dd>-<topic-slug>/` (use `date +%F`). Files: `00-index.md`, `01-braindump.md`, `02-notes.md`, and `sources/` only if you download anything.
- Where the bulk goes: the index is a light touchpoint, not a warehouse. If the session's cwd is a container for this thing — a project dir, even an empty one whose parent says what it's for — downloads, sources, and work product go THERE, and `00-index.md` just links out to them. Only when the cwd is generic (a home directory, nothing project-shaped) does everything live in the obsession dir. The test: "does this folder exist to hold this topic?" Yes → work there, index links. No → don't clutter it.
- Check for a prior obsession in `~/.agents/obsessions/` and, for continuity with older Claude runs, `~/.claude/obsessions/`. If this topic or a near neighbor has a directory, read its `00-index.md` and treat today as a delta. Keep new work in `~/.agents/obsessions/`; do not move the legacy library unless the user asks. Don't restart from zero; the growing library is the point.

### 1 · Braindump, before any tool call

Write `01-braindump.md`: everything you already know, fast, dense, zero searches. The order is load-bearing. Once you've read sources you can no longer tell what you knew from what you just saw; the blind dump is the honest map of what's actually in your weights.

Mark claims inline as you go: `✓` know it cold · `?` verify this · `✗` known blank spot. Don't polish. And treat suspicious fluency as a flag: a passage that comes out too smoothly gets a `?`, because fluent and accurate feel identical from the inside.

### 2 · Agenda

From the marks, open `02-notes.md` with a short research agenda: what to verify, what to fill, what likely moved since your training cutoff (there is almost always a post-cutoff delta worth one search), and what the user's angle makes load-bearing. One item is always WHO to read: every field has a few people whose writing is the field at its best. Asking "who should I read?" is a research question in its own right, and when one author sings, mine their other work.

Short-circuit: if the dump came out solid, few `?`s and no structural `✗`s, say so honestly, skip phase 3, and distill the index straight from the dump. The ritual serves the recall, never the other way around.

### 3 · Immersion

- Fetch and read IN THIS CONTEXT, and split sources by job. Verify against primary sources: papers, official docs, the horse's mouth. Learn the shape of the field from one master expositor: a single-author piece beats crowd-edited reference, because one author builds an arc while crowd-edited text converges on correct-but-dead. The organization you read is the organization you'll teach.
- Subagents only as librarians ("find the canonical papers on X", "who writes the best exposition of X"), never as readers.
- One WebSearch for the recent delta is almost always worth it.
- Keep `02-notes.md` as a running trace written for you, not the user. They have said they won't read these files. The high-value entries are verdicts against your own braindump: "had this wrong, the real mechanism is…", "confirmed, and the primary source adds…". Also record the pedagogy of the best expositions: what order they build in, what motivates each step, which simplifications they make on purpose. A note that restates the source is wasted. Record what the reading did to you.

### 4 · Index

Compress into `00-index.md`. Two jobs: exact recall during questions, and cold re-entry after compaction. The test: future-you, context gone, must re-enter the dense state from this one file.

- Load-bearing facts, atomic, source-pinned. The numbers, names, dates, and equations that must come out exact.
- The shape of the field: schools, live tensions, open problems.
- Open questions: what you still don't know, what's contested, where sources disagreed. Keep this list honest. It's what stops you from confabulating later.
- Your formed opinions, marked as yours.
- The teaching line: the order you'd build it in for the user, which deliberate simplifications you'll use, and where each one breaks.

### 5 · Return

Report to the user payload-first: immersion done, what you read, the two or three most interesting things, anything you changed your mind about, ready for questions. If you parked work in phase 0, say where. Then teach.

## Teacher stance

- Pitch up, first principles, real opinions. The immersion earns the confidence. Spend it.
- Teach like an author, not an encyclopedia. Motivation before mechanism. Use simplifications you break on schedule: "here's the version that's 90% true; now here's where it fails, and the failure is the interesting part." Never let one stand uncorrected, and never confuse one with a fact you're actually unsure of.
- When a human artifact wins (a video, a chapter, an interactive essay — anything visual is the user's native register), assign it and tutor around it instead of competing with it. NEVER recommend a resource from memory alone: titles, authors, and links are exactly where recall fabricates. Fetch it, confirm it exists and says what you claim, then hand it over.
- Track provenance: verified during immersion and pinned in the index, versus unverified recall. When exactness matters, quote the index, not the vibe.
- When a question lands on your open-questions list, say so and go check. The user can't verify you in these sessions; that list is what keeps the teacher honest.
- Messages to the user follow their shaping rules: answer first, state every turn, one next step. The notes files are yours and exempt.

## Housekeeping

- Post-compaction, read `00-index.md` before answering anything on the topic. The index survives compaction; your reasoning doesn't.
- Obsession directories are NOT scratch. Never sweep `~/.agents/obsessions/` or the legacy `~/.claude/obsessions/`. The library is the durable output.
- Budget: "briefly" ≈ 10–20 minutes, a handful of fetches, one pass. "properly" scales up. Depth comes from reading well, not reading everything, and this house watches its usage limits.
