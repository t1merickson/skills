---
name: prediction
description: Run a rigorous, fully-logged decision-tree analysis of any prediction about the future — technology, ideology, institutions, markets, culture, careers — at any horizon. Use whenever the user states or asks about a forecast ("in 50 years X will be obsolete", "will AI replace Y", "is remote work dead", "who wins A vs B long-term"), asks to steelman/evaluate a prediction, brings a hot take about the future, or poses any messy claim about how things will turn out. Trigger even without the word "prediction" — any "will X happen / survive / replace / die / win" question qualifies. Interviews the user to scope the prediction first, converts vague gestures into canonical resolvable claims, walks them through a fixed node chain (reference class, durability sort, mechanism stress-test, evidence audit, analogy court, transition shape, adversarial pass), logs every node to markdown, and terminates in binary-adjacent verdicts with probability bands, falsifiers, and a watchboard.
---

# /prediction — The Durability Tree

A framework for taking a messy, poorly-scoped prediction about the future and doing the actual work of answering it — instead of gesturing broadly toward one possible outcome.

## The doctrine

**Do not simulate the future forward. Sort the present's premises by durability, and let the prediction pass only through the mutable ones.**

Forward simulation over long horizons compounds error at every step; by year 30 the simulation is fiction. Constraint-sorting does not compound: a premise that is invariant within the horizon (physics, geometry, game theory, positional scarcity) blocks the prediction wherever it stands on that premise, no matter what else changes. A premise that is mutable (prices, ownership models, regulation, fashion, org charts) cannot protect the incumbent, no matter how solid it looks today.

Everything in this skill is machinery for doing that sort honestly: decomposing the claim so legs can't borrow strength from each other, finding what the attacked thing actually rests on, stress-testing the proposed mechanism, auditing the evidence for category errors, trying analogies in court instead of by vibe, and red-teaming the verdict before shipping it.

The second commitment is **the ledger**. Every node of reasoning is written to a markdown file *before* the next node begins, with its possible outcomes enumerated and weighted, so the chain of "why" is inspectable and the final verdict cannot be quietly retrofitted. The ledger is a commitment device against the single most common failure of long-horizon reasoning: deciding first and constructing the tree afterward.

## What counts as done

A tree is complete when **every leaf terminates in one of exactly three things**:

1. **An invariant** — a constraint that survives the horizon (with the reason it survives stated).
2. **An explicit probability with named sensitivities** — a number band plus the list of nodes that would flip it.
3. **A declared unknown with a watch indicator** — an honest "can't be resolved from here," plus the observable that would resolve it and roughly when it becomes observable.

If any chain of "why" ends anywhere else — a vibe, an untested analogy, an authority citation, a trend line extended with a ruler — the tree is not done. This criterion, not a fixed node count, is the answer to "how many nodes does this question require." The 12 core nodes below are the minimum spanning set; claim shape determines which ones expand (see the adaptation table).

## Inputs and modes

The user gives you a prediction in whatever shape it arrives: a sentence, a tweet thread, a rant, a question, a bet. It may bundle several claims at several horizons. That's fine — unbundling is Node 0's job.

**Two analysis modes.** Default is **reasoning-first**: work from internal knowledge, log every factual claim you rely on in the fact register with status `model-recall-unverified`, `assumed-from-user`, or `verified`, and let the verdict's confidence reflect that. Switch to **research mode** (verify load-bearing facts with web search before N5) if the user asks, or if the verdict turns out to hinge on a fact you're unsure of — in that case say so and offer the upgrade. Reasoning-first is the default because the framework's value is mostly in the sort and the structure, not the trivia, and because half the point is discovering *which* facts are load-bearing before spending effort verifying any.

**Two depth modes.** Default is a **full run**: one file per node in a run directory. If the user asks for a quick pass, or the claim is narrow and near-horizon, run **compact mode**: same node chain, same discipline, but all nodes logged as sections of a single `LEDGER.md`. Never skip nodes in compact mode — shorten them.

## Setup

1. **Run the pre-tree interview.** Before shaping any part of the tree — before the node plan, before final canonicalization — put your scoping questions to the user. Do it informed: silently draft the claim extraction first, so the questions are about *their* prediction rather than generic. Ask only what changes the tree:
   - **Horizons**, if unstated or ambiguous.
   - **Intended meaning** of each vague predicate — offer 2–3 candidate resolvable definitions as options and let the user pick or supply their own; the choice often predetermines a verdict, so it belongs to them when they're present to make it.
   - **Scope priority** among bundled claims: which matter most, which may be dropped or demoted.
   - **Facts to stipulate vs verify** — settles reasoning-first vs research mode — and **depth** (full vs compact).
   - **Purpose and stakes** (a bet, a decision, an essay, curiosity): shapes watchboard design and delivery format.
   - Optionally, **their own stance** — do they hold this prediction or are they testing someone else's, and what would they *prefer* to be true? Log it for the adversarial pass's residue disclosure. It informs framing only; preferences never move a verdict.

   Mechanics: batch into a single AskUserQuestion call (up to 4 questions, with options plus free-text) when the tool is available; plain-text questions otherwise. One round is the default; a second round only if the answers overturned the draft claim extraction. Record questions and answers verbatim in the intake file, along with how each answer shaped the canonicalization and node plan. **Binding rules:** the user owns meanings, horizons, and scope — those answers bind. Facts they assert enter the register as `assumed-from-user`. Stated preferences bind nothing. If the session is unattended or the user says "just run it," skip the interview, choose defaults, state each one in the intake file, and proceed.
2. **Create the run directory**: `~/.claude/obsessions/<yyyy-mm-dd>-prediction-<slug>/` (use `date +%F`). This is the same library the `obsess` skill writes to; prediction ledgers live alongside obsession indexes so one `ls` surfaces everything the model has gone deep on. One prediction-bundle per directory, even if it contains many claims. Before creating it, `ls ~/.claude/obsessions/` — if this prediction or a near neighbor already has a directory, read its `11-VERDICT.md` (or `LEDGER.md`) and treat today as a revision pass: append `## REVISED` blocks and update the watchboard instead of regrowing the tree from zero. These directories are not scratch; never sweep them.
3. **Braindump before any research.** Before any web search or fetch — in either analysis mode — write everything you already know that bears on the claim into the intake file as a fast, dense, unpolished dump, marking each claim inline: `✓` know it cold, `?` verify this, `✗` known blank spot. The order matters: once you've read sources you can no longer tell what you knew from what you just saw, and the blind dump is the honest map of what's actually in your weights. Treat suspicious fluency as a flag — a passage that comes out too smoothly gets a `?`. The marks seed the fact register (`✓` → `model-recall-unverified` with high confidence, `?` → `model-recall-unverified` flagged for verification, `✗` → an open question), and in research mode the `?`s and `✗`s are the search agenda.
4. **Copy templates.** The `templates/` directory of this skill contains the file skeletons. Instantiate them as you reach each node — don't pre-create empty files, which invites checkbox-filling.
5. **Create a task list** (one task per node plus delivery) so the user can watch the tree grow.

## The node chain

Twelve nodes, three phases. Files are numbered to sort in execution order. Full procedures for every node live in `references/node-library.md` — **read it before your first run of this skill in a session**, and re-read a node's entry whenever it activates in expanded form. The table is the map, not the territory.

| # | Node | File | Question it answers |
|---|------|------|---------------------|
| **Phase I — Scoping** |
| N0 | Intake, Interview & Canonicalization | `00-INTAKE.md` | What is actually being claimed, about what, by when, and what would count as true — and what does the user say about all of that? |
| N1 | Reference Class & Base Rates | `01-reference-class.md` | What kind of claim is this, and how often do claims of this kind come true? |
| **Phase II — The tree** |
| N2 | Decomposition & Shared Premises | `02-decomposition.md` | What separable legs does the claim bundle, and what premises do the rivals secretly share? |
| N3 | Load-Bearing Analysis & Durability Sort | `03-durability-sort.md` | What does the incumbent's advantage actually rest on, and which premises survive the horizon? |
| N4 | Mechanism Stress-Test | `04-mechanism-tests.md` | Do the causal mechanisms offered actually produce the predicted outcome — or do they prove too much, contradict themselves, or only predict speed? |
| N5 | Evidence Audit | `05-evidence-audit.md` | Is the cited evidence probative, or merely accurate? |
| N6 | Analogy Court | `06-analogy-court.md` | Do the analogies hold at the mechanism level — and does the dominance pattern predict substitution, stratification, or hybridization? |
| N7 | Transition Shape & Political Economy | `07-transition-shape.md` | Even if the endpoint is right, what path gets there — who must agree, who defends the incumbent, and does change arrive smoothly or by punctuation? |
| **Phase III — Convergence** |
| N8 | Regime Split & Recomposition | `08-RECOMPOSITION.md` | In which regimes does the claim hold and in which is it blocked — and what do the legs sum to? |
| N9 | Semantic Dissolution Check | `09-semantic-check.md` | Will this resolve empirically or dissolve semantically — and what do we pre-commit to counting? |
| N10 | Adversarial Pass | `10-ADVERSARIAL.md` | What is the best case for the opposite verdict, who holds it seriously, and what world-states vindicate them? |
| N11 | Verdict & Watchboard | `11-VERDICT.md` | What, finally, is the answer — as resolvable statements with probabilities, falsifiers, indicators, and an accounting of the tree itself? |

Run them in order. The order is logical dependency: each node consumes the outputs of earlier ones, and several nodes exist specifically to check work done upstream (N10 checks everything). Skipping ahead produces exactly the broad gesturing this skill exists to prevent.

## Execution disciplines

These six rules are the difference between a ledger and a diary. They are the part of the skill that everything else depends on.

### 1. Log-then-advance
Write each node's file — findings, branches, weights, selection — **before beginning the next node**. The point is temporal commitment: once N3's durability sort is on disk, N6 can't quietly bend an analogy to fit a conclusion you've already fallen for. If later work forces a revision of an earlier node, do not silently edit. Append a dated `## REVISED` block to the earlier file stating what changed, what forced it, and how the change propagates downstream. Belief updates are good; invisible ones are not.

### 2. Branch enumeration
Every node ends by enumerating **2–5 possible outcomes of that node's question** (not of the whole prediction), each with a coarse weight and — critically — a sentence on *what evidence or argument would have selected it*. Then select one (or a weighted split) and write the why-chain. This is what makes the tree a tree rather than a corridor: the road not taken is recorded at the fork, so a reader (or a future revision) can re-enter at any node and see what it would take to exit differently.

### 3. Sensitivity threading
Every node records its **downstream dependencies**: which later nodes consume this output, and what happens to the final verdict if this node flips. N11 aggregates these into the verdict's fragility profile. A verdict is only as strong as its weakest load-bearing node, and this threading is how you find out which node that is — often a surprise.

### 4. Durable premises get the five W's
Whenever the durability sort (N3) marks a premise as an invariant — or any node's leaf terminates in one — record it with all five W's, each as a short concrete phrase:

- **Who** holds or enforces it (nature, an institution, a market, everyone with a body)
- **What** the constraint actually is, stated plainly
- **When** it holds — the horizon it survives, and any date or condition past which it stops being safe to lean on
- **Where** it applies — which regimes, geographies, or market segments; durability is often regional
- **Why** it survives — the reason it can't be legislated, priced, or fashioned away

A "durable" premise missing any W is not yet sorted; the missing W is usually where the premise turns out to be mutable. The five-W block lives in the node file next to the durability table row it annotates.

### 5. The fact register
Every factual claim the analysis leans on gets a row in the register (kept in `00-INTAKE.md`, appended throughout): the claim, its source status (`verified` / `assumed-from-user` / `model-recall-unverified`), confidence, and which nodes rely on it. When the user says "assume the facts are correct," that's an instruction to mark them `assumed-from-user` — not an instruction to stop tracking which conclusions inherit that assumption.

### 6. Confidence grammar
All probability talk uses this fixed vocabulary, everywhere in the ledger:

| Term | Band |
|------|------|
| near-certain | 93–99% |
| very likely | 80–93% |
| likely | 65–80% |
| lean | 55–65% |
| coin flip | 45–55% |
| lean against | 35–45% |
| unlikely | 20–35% |
| very unlikely | 7–20% |
| near-impossible | 1–7% |

Three propagation rules. **Weakest-link**: a verdict's confidence cannot exceed that of its weakest load-bearing node. **Horizon widening**: every doubling of horizon widens bands — at 100 years, nothing that depends on a mutable premise deserves better than "likely"; at 200 years, only claims blocked or carried by definitional invariants (physics, arithmetic, positional scarcity) may exceed it. **Abstraction widening**: each step up the abstraction ladder (physical tech → systems → markets → institutions → values) weakens the available invariants, so bands widen again. Never emit a point probability without naming its sensitivities. The full grammar, ladder, and catalogs are in `references/heuristics.md` — read it alongside the node library.

## Adapting to claim shape

The core chain is fixed; what varies is which nodes expand. Diagnose the claim's shape(s) in N0 and record the node plan — a claim can be more than one shape at once (a headline claim of one shape frequently rides on a premise-claim of another; diagnose and expand for both).

| Claim shape | Expand | Watch for |
|-------------|--------|-----------|
| Technology substitution ("X replaces Y") | N3 (physical invariants: geometry, throughput, thermodynamics), N6 (full dominance audit) | Survivorship bias in N1; boundary asymmetry in N5 |
| Infrastructure & systems | N3 (network topology, right-of-way), N7 (public-goods consensus costs) | Governance failure mistaken for category property |
| Institutional / ideological ("A-ism beats B-ism") | N2 (shared premises — the rivals' common basement is the biggest attack surface), N7 (punctuated equilibrium, incumbent coalitions, reflexivity), N9 (these claims usually dissolve semantically) | No dominance ordering exists on contested value axes — extinction is structurally unavailable, expect hybridization |
| Company / market ("$CO wins the category") | N4 (add competitive-response sub-test: what do rivals do in reply?), N1 (base rates for category leaders persisting) | Extrapolating a moat made of current prices |
| Scientific / paradigm ("theory T will be overturned") | N5 (add anomaly audit: what does the current paradigm fail to explain?), N1 (base rate of paradigm shifts per anomaly load) | Confusing sociology of the field with the evidence |
| Cultural / behavioral ("people will stop doing X") | N7 (cohort replacement math — most cultural change is generational turnover, not persuasion), N3 (status dynamics: is X positional?) | Positional goods never saturate; nothing erodes status scarcity |
| Personal / career ("this profession is dead") | N1 (base rates of profession extinction vs transformation), N8 (regime split by task composition within the job) | "The job changes" resolving as both true and false |

## The output ledger

Templates for every file live in `templates/`. Use them — they carry field-by-field instructions in comments, and their structure is what makes runs comparable across predictions. File-by-file:

- `00-INTAKE.md` — from `templates/00-INTAKE.md`. Verbatim capture, canonical claim register (C1…Cn with horizons and resolution criteria), the pre-tree interview record, definitional work, shape diagnosis, node plan, fact register, mode declarations.
- `01…07-*.md` — from `templates/node-entry.md`, one per node. Same 11-section skeleton every time: question, inputs, procedure, findings, branches, selection, flip conditions, downstream dependencies, confidence, fact-register additions, open questions.
- `08-RECOMPOSITION.md` — from `templates/08-RECOMPOSITION.md`. Regime partition, per-claim reassembly, weakest-link accounting.
- `10-ADVERSARIAL.md` — from `templates/10-ADVERSARIAL.md`. Steelman of the opposite verdict, rival live forecasts, flip-list, normative residue.
- `11-VERDICT.md` — from `templates/11-VERDICT.md`. The deliverable: per-claim resolvable statements, probability bands, one-line compressions, fragility profile, falsifiers, watchboard, node accounting.

Node files should be *long where the thinking is* — findings sections of 300–800 words per claim are normal for a full run, and N3's durability table plus prose regularly runs longer. Length is not the goal; inspectability of the why-chain is. A reader should be able to open any node file cold and reconstruct why the tree went the way it went from that point.

## Delivery

When N11 is written:

1. Give the user the verdict **in the conversation**: the one-line compression per claim, the probability bands, and the single most load-bearing node — a few paragraphs, not a repaste of the file.
2. Send `11-VERDICT.md` (and, if they want the whole trail, a zip of the run directory) via the file-delivery tool available in the environment.
3. Offer — once, in one line — a rendered summary artifact if the environment supports publishing and the user seems likely to revisit or share the analysis. The watchboard makes these natural living documents: a later session can re-open the ledger, check indicators, and append `## REVISED` blocks.

## Anti-patterns

The full catalog with tells and fixes is in `references/heuristics.md` § Anti-patterns. The eight that account for most failed forecasts, as a checklist to run at N10:

**Borrowed strength** (compound claim's strongest leg carrying its weakest) · **Vibe-level analogy** (mapping imagery instead of mechanism) · **Forward simulation** (narrating a future instead of sorting constraints) · **Boundary asymmetry** (costs counted for one side, externalized for the other) · **Governance-as-physics** (one bad implementation convicting a whole category) · **Velocity–destination confusion** (a mechanism that predicts *faster* being read as predicting *wins*) · **Old ≠ antiquated** (a thing's age mistaken for its obsolescence; antiquated means dominated-and-abandoned) · **Point-probability theater** (a number with no named sensitivities).

## What the target output reads like

There is deliberately no worked example bundled with this skill: examples anchor future runs on their domains and their verdict shapes, and every prediction deserves a tree grown from its own premises. Calibrate instead against these properties. A good run's ledger reads such that any node file opened cold lets a reader reconstruct why the tree went the way it went from that point. Its durability table names each premise concretely enough to be argued with. Its verdicts are split wherever the analysis found regime boundaries, reported split, never averaged. Each claim compresses to one sentence that carries the finding. The watchboard rows are observables with thresholds and dates, not restatements of the claim. And the node accounting states plainly where a broad gesture would have stopped and what the remaining nodes added.
