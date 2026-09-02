---
name: obsess
description: Build a bounded, source-pinned immersion on an explicitly named topic, then teach from verified in-context notes. Use only when invoked.
---

# Obsess

The user invokes this with a topic: `/obsess <topic>`, “become obsessed with X,” or an equally explicit request to immerse. The session that follows is usually the user as student and you as teacher. Your job before teaching is to get genuinely deep on the topic in this task, with facts pinned and unknowns mapped.

If the subject is one person and the desired output is a durable person-shaped vault, use `obsess-hero` instead. If no topic is supplied, ask; it is the one thing you cannot infer.

## Why it is shaped this way

Three facts make the ritual work:

1. Model recall is useful but lossy. Exact facts placed in the task's working notes can be checked and recovered; facts left as fluent recall can be paraphrased or wrong. The ritual moves load-bearing knowledge from recall into a source-pinned working set before questions arrive.
2. The material and organization you write while learning shape the synthesis you produce afterward. Write the notes yourself rather than pasting search snippets or delegated summaries.
3. Reading done only by a subagent did not happen to the primary task. Subagents may act as librarians when a selected route funds them; they do not replace direct inspection of the sources used for teaching.

## The ritual

### 0 · Set up

- Parse the topic, angle, desired depth, recency risk, output location, time/request/token budget, and stopping condition.
- If work is already in flight, park its non-reconstructable state before switching. Half-attention immersion produces half-dense notes.
- Prefer a project-local research directory when the current project exists to hold this topic; otherwise use the host's configured durable research root. Keep `00-index.md`, `01-braindump.md`, `02-notes.md`, and `sources/` when downloads are permitted and useful. The index is a re-entry point, not a warehouse; bulk material belongs in the topic's project and is linked from the index.
- Locate any prior index, but do not read it before the blind braindump. After the braindump, read it and treat this run as a dated delta. Never move or consolidate an older library without a separate request.

### 1 · Braindump, before research

Write `01-braindump.md` before searching, opening sources, reading a prior index, or asking an agent to investigate. Put down everything you already believe about the topic, fast and dense. This ordering is load-bearing: once research begins, you can no longer honestly separate recall from what you just read.

Mark claims inline:

- `✓` — high-confidence recall, still source-check it when load-bearing;
- `?` — plausible, but exactness or recency is uncertain;
- `✗` — a known blank spot or missing structure.

Dates, quotations, titles, statistics, current status, and recommendations begin as `?`. Treat suspicious fluency as a reason to add `?`, because fluent and accurate feel identical from the inside. Do not polish the dump and never revise it to make the later research look inevitable.

### 2 · Build the agenda and mile map

Now read any prior index. Open `02-notes.md` with a research agenda built from the marks: what to verify, what to fill, the core mechanism, canonical primary sources, the best exposition, live disputes, the recent delta, and what the user's angle makes load-bearing. One item is always “who should I read?” Every field has a few people whose writing gives it shape; when one author sings, consider their other work as a route.

If the dump is already structurally solid, with few `?` marks and no important `✗` marks, say so. Offer a short verification route or proceed directly to the index if no external research is needed. The ritual serves the learning; it is not a collection quota.

Before the first external research pull, chart a small set of plausible paths that could materially change the result. For each path show:

- the question it answers and the likely artifact or insight at its end;
- the source types and bounded research pull it requires;
- the incremental main-task working-token estimate as a range;
- the number and role of proposed subagents plus a separate delegated-token range, normally zero unless parallel discovery has a clear payoff;
- important dependencies, uncertainty, and the point where the path stops.

A compact table usually works: `Path | Leads to | Research pull | Main tokens | Subagents + delegated tokens | Stop`.

Token ranges are planning estimates, not billing promises. Do not imply exact metering. Ask the user which path or paths to fund; they may reorder, combine, narrow, or reject them. Do not start an unchosen branch, spawn its agents, or spend its research budget. “Deep” or “comprehensive” expands the proposed routes; it does not waive checkpoints.

### 3 · Immerse, one selected pull at a time

- Read the evidence in this task. Use search to discover sources, not as the evidence itself. Verify facts against primary sources—papers, official documentation, original artifacts, or the horse's mouth—and learn the field's shape from one or two strong expositors. A coherent author often teaches structure better than a crowd-edited reference; the organization you read becomes the organization you can teach.
- A selected subagent may find canonical papers, identify strong expositors, or map candidate sources. The primary task reads every source that supports the final teaching synthesis.
- Keep `02-notes.md` as a running verdict log against the braindump: “had this wrong; the mechanism is…,” “confirmed, and the primary source adds…,” “sources disagree because….” Record the pedagogy of the best exposition: what it motivates first, what it deliberately simplifies, and where that simplification breaks. A note that merely restates a source is wasted.
- Keep source metadata and links beside the notes. Download only when useful and within the user's chosen storage scope.

At the end of each selected pull, reach a mile marker:

1. report what changed, whether the predicted payoff appeared, and the actual observable spend;
2. if exact token use is unavailable, say `not metered` and report requests made, sources inspected or captured, delegated agents used, and storage added;
3. redraw only the frontier changed by the evidence, with revised cost and agent estimates;
4. pause for the user's next choice.

Skip the pause only when the user explicitly authorizes an uninterrupted run with clearly bounded paths, total budget, and stopping condition. Newly discovered branches remain parked unless they fit that authorization. Stop when a mile marker, budget, coverage condition, access boundary, or diminishing-return point is reached.

### 4 · Compile the index

Compress the working set into `00-index.md`. It has two jobs: exact recall during questions and cold re-entry after context loss. Future-you must be able to recover the dense state from this one file.

Include:

- atomic load-bearing facts with source pointers—the names, dates, numbers, mechanisms, and equations that must come out exactly;
- the field's shape: schools, lineages, live tensions, and open problems;
- corrections to the blind braindump;
- open questions, contradictions, and what evidence would settle them;
- formed synthesis or opinion, visibly marked as yours;
- the teaching line: the order you would build the subject in, the simplifications you will use, and where each breaks;
- coverage date, selected paths, observable spend, remaining frontier, and stopping reason.

### 5 · Return, then teach

Report payload-first: what you learned, what changed your mind, the best sources, the most interesting two or three insights, the remaining uncertainty, and why the run stopped. Then teach.

## Teacher stance

- Pitch up: first principles, precise language, and real synthesis. The immersion earns confidence; spend it without pretending uncertainty disappeared.
- Teach like an author, not an encyclopedia. Motivation before mechanism. Use deliberate simplifications, then break them on schedule before they become misleading.
- When a human artifact—a chapter, talk, video, diagram, or interactive essay—teaches better than prose alone, assign it and tutor around it. Never recommend a title or link from recall alone; verify that it exists and says what you claim.
- Distinguish verified evidence, unresolved recall, and your synthesis. When a question lands on the open frontier, say so and offer the next bounded pull.

## Housekeeping

- After context loss, read `00-index.md` before answering on the topic and reverify volatile claims.
- Obsession directories are durable outputs, not scratch. Never sweep, merge, or relocate them casually.
- “Brief” means one prioritized pull and an explicit frontier. “Deep” means more user-selected pulls with contradiction checking. Depth comes from reading well, not reading everything.
