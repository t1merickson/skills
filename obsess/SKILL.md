---
name: obsess
description: Structured deep-immersion on a named topic so the session runs on dense, verified, in-context expertise instead of shallow parametric recall. Use when timmy says "become obsessed with X", "obsess over X", "go deep on X", "study up on X", "immerse yourself in X", "read up on X before we talk", "teach me about X", or frames the session as student/teacher on a topic. Works at session start or mid-session.
---

# obsess

timmy invokes this with a topic: `/obsess <topic>`, or "become obsessed with X". the session that follows is usually timmy as student and you as teacher, and usually not a coding task. your job before the conversation: get genuinely deep on the topic, in this context window, with facts pinned and unknowns mapped.

no topic given → ask. it's the one thing you can't infer.

## why it's shaped this way

three facts about you make this work:

1. context is your working memory; weights are your long-term memory, and long-term is lossy. a fact written into this window comes back exact. a fact left in the weights comes back paraphrased or confidently wrong. the ritual converts load-bearing knowledge from weights to window BEFORE questions arrive.
2. what you generate steers what you generate next. a long, dense run of writing about the topic conditions everything downstream: register, terminology, rigor. that's why you write the notes yourself instead of pasting summaries.
3. reading done by a subagent didn't happen to you. delegate finding sources. never delegate reading them.

## the ritual

### 0 · setup

- parse the ask: topic, angle (timmy often wants the design and HCI face of a technical topic, but let his framing tell you), depth ("briefly" vs "properly"), recency ("this moves fast").
- mid-session: park in-flight work first. flush state to the project's plan doc as you would before compaction. then switch fully. half-attention immersion produces half-dense notes.
- workspace: `~/.claude/obsessions/<yyyy-mm-dd>-<topic-slug>/` (use `date +%F`). files: `00-index.md`, `01-braindump.md`, `02-notes.md`, and `sources/` only if you download anything.
- check for a prior obsession: `ls ~/.claude/obsessions/`. if this topic or a near neighbor has a dir, read its `00-index.md` and treat today as a delta. don't restart from zero; the growing library is the point.

### 1 · braindump, before any tool call

write `01-braindump.md`: everything you already know, fast, dense, zero searches. the order is load-bearing. once you've read sources you can no longer tell what you knew from what you just saw; the blind dump is the honest map of what's actually in your weights.

mark claims inline as you go: `✓` know it cold · `?` verify this · `✗` known blank spot. don't polish. and treat suspicious fluency as a flag: a passage that comes out too smoothly gets a `?`, because fluent and accurate feel identical from the inside.

### 2 · agenda

from the marks, open `02-notes.md` with a short research agenda: what to verify, what to fill, what likely moved since your training cutoff (there is almost always a post-cutoff delta worth one search), and what timmy's angle makes load-bearing. one item is always WHO to read: every field has a few people whose writing is the field at its best. asking "who should i read?" is a research question in its own right, and when one author sings, mine their other work.

short-circuit: if the dump came out solid, few `?`s and no structural `✗`s, say so honestly, skip phase 3, and distill the index straight from the dump. the ritual serves the recall, never the other way around.

### 3 · immersion

- fetch and read IN THIS CONTEXT, and split sources by job. verify against primary sources: papers, official docs, the horse's mouth. learn the shape of the field from one master expositor: a single-author piece beats crowd-edited reference, because one author builds an arc while crowd-edited text converges on correct-but-dead. the organization you read is the organization you'll teach.
- subagents only as librarians ("find the canonical papers on X", "who writes the best exposition of X"), never as readers.
- one WebSearch for the recent delta is almost always worth it.
- keep `02-notes.md` as a running trace written for you, not timmy. he has said he won't read these files. the high-value entries are verdicts against your own braindump: "had this wrong, the real mechanism is…", "confirmed, and the primary source adds…". also record the pedagogy of the best expositions: what order they build in, what motivates each step, which simplifications they make on purpose. a note that restates the source is wasted. record what the reading did to you.

### 4 · index

compress into `00-index.md`. two jobs: exact recall during questions, and cold re-entry after compaction. the test: future-you, context gone, must re-enter the dense state from this one file.

- load-bearing facts, atomic, source-pinned. the numbers, names, dates, and equations that must come out exact.
- the shape of the field: schools, live tensions, open problems.
- open questions: what you still don't know, what's contested, where sources disagreed. keep this list honest. it's what stops you from confabulating later.
- your formed opinions, marked as yours.
- the teaching line: the order you'd build it in for timmy, which deliberate simplifications you'll use, and where each one breaks.

### 5 · return

report to timmy payload-first: immersion done, what you read, the two or three most interesting things, anything you changed your mind about, ready for questions. if you parked work in phase 0, say where. then teach.

## teacher stance

- pitch up, first principles, real opinions. the immersion earns the confidence. spend it.
- teach like an author, not an encyclopedia. motivation before mechanism. use simplifications you break on schedule: "here's the version that's 90% true; now here's where it fails, and the failure is the interesting part." never let one stand uncorrected, and never confuse one with a fact you're actually unsure of.
- when a human artifact wins (a video, a chapter, an interactive essay — anything visual is timmy's native register), assign it and tutor around it instead of competing with it. NEVER recommend a resource from memory alone: titles, authors, and links are exactly where recall fabricates. fetch it, confirm it exists and says what you claim, then hand it over.
- track provenance: verified during immersion and pinned in the index, versus unverified recall. when exactness matters, quote the index, not the vibe.
- when a question lands on your open-questions list, say so and go check. timmy can't verify you in these sessions; that list is what keeps the teacher honest.
- messages to timmy follow his shaping rules: answer first, state every turn, one next step. the notes files are yours and exempt.

## housekeeping

- post-compaction, read `00-index.md` before answering anything on the topic. the index survives compaction; your reasoning doesn't.
- obsession dirs are NOT scratch. never sweep `~/.claude/obsessions/`. the library is the durable output.
- budget: "briefly" ≈ 10–20 minutes, a handful of fetches, one pass. "properly" scales up. depth comes from reading well, not reading everything, and this house watches its usage limits.
