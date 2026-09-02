---
name: obsess
description: Build a bounded, source-pinned immersion on an explicitly named topic, then teach from verified notes. Use only when invoked.
---

# Obsess

Use only when the user explicitly asks to become immersed or invokes this skill. If the subject is one person and the desired output is a durable person-shaped vault, use `obsess-hero` instead.

## Set the contract

Name the topic, angle, desired depth, recency risk, output location, time/request budget, and stopping condition. If no topic is supplied, ask. Prefer a project-local research directory or the host's configured durable research root; writing elsewhere requires the normal filesystem authority.

If a prior index exists, read it first and treat this run as a dated delta. Do not move or consolidate older libraries without a separate request.

## Map the mile markers

Before the first external research pull, chart the plausible paths that could materially change the result. Keep the chart small and decision-useful. For each path show:

- the question it answers and the likely artifact or insight at its end;
- the source types or research pull it requires;
- the incremental main-task working-token estimate as a range;
- the number and role of proposed subagents plus a separate delegated-token range, normally zero unless parallel discovery has a clear payoff;
- important dependencies, uncertainty, and the point where that path will stop.

A compact table usually works: `Path | Leads to | Research pull | Main tokens | Subagents + delegated tokens | Stop`.

Token ranges are planning estimates, not billing promises. Do not imply exact metering. If actual token use is unavailable, say `not metered` at later checkpoints and report observable spend instead: requests made, sources inspected or captured, delegated agents used, and storage added.

Ask the user which path or paths to fund. The user may reorder, combine, narrow, or reject them. Do not begin an unchosen branch, spawn its agents, or spend its research budget. A request for “deep” or “comprehensive” work expands the proposed paths; it does not waive checkpoints.

Treat each selected path as one bounded research pull. At its mile marker:

1. report what changed, actual observable spend, and whether the predicted payoff appeared;
2. redraw only the frontier that the evidence changed, with revised cost and agent estimates;
3. pause for the next choice.

Skip these pauses only when the user explicitly authorizes an uninterrupted run. That authorization must still name or clearly bound the selected paths, total budget, and stopping condition. New branches discovered during an uninterrupted run remain parked unless they fit that authorization.

## Separate recall from research

Before searching, write a compact braindump of relevant recall. Mark each claim:

- `known` — high-confidence but still subject to source checking when load-bearing;
- `verify` — plausible, exactness or recency uncertain;
- `gap` — known missing structure.

Dates, quotations, titles, statistics, current status, and recommendations are `verify` until checked. This step records provenance; it does not make recall authoritative.

Turn the marks into a research agenda: the core mechanism, canonical primary sources, best exposition, live disputes, recent delta, and the user's angle. Define what will remain out of scope.

## Immerse

Read primary sources for facts and one or two strong expositors for shape and pedagogy. Use search to discover sources, not as the evidence itself. Record what each source confirmed, corrected, complicated, or left open; do not merely restate it.

Keep source metadata and links beside the notes. Download only when permitted and useful, and respect copyright, access controls, host terms, and the user's storage scope. Additional agents may discover candidate sources only on a user-selected path that includes them, but the teaching synthesis must be based on material this task actually inspected.

Stop at each selected mile marker and whenever the agreed budget or coverage condition is met, the remaining frontier is named, or another source would mostly repeat established evidence. “Deep” expands coverage and contradiction checking; it does not mean unbounded collection.

## Compile the index

The durable index contains:

1. exact load-bearing facts with source pointers;
2. the field's structure, schools, and disagreements;
3. corrections to the initial braindump;
4. open questions and what would settle them;
5. clearly labeled synthesis or opinion;
6. a teaching sequence and the limits of each simplification;
7. coverage, date, selected paths, observable spend, and stopping reason.

After context loss, reload this index and reverify volatile claims before relying on them.

## Return and teach

Lead with what was learned, what changed, the most useful sources, remaining uncertainty, and readiness for questions. Teach motivation before mechanism, distinguish verified fact from synthesis, and correct simplifying models before they become misleading. Never recommend a title or link from recall alone.
