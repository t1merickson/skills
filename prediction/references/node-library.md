# Node Library — full procedures

This file is the complete specification of every node in the Durability Tree. Each entry gives: the question the node answers, why the node exists (the failure mode it prevents), the procedure, what the node must produce and decide, the typical branch space, and the node's own failure modes. Read the whole file before a first run; re-read a node's entry when it activates in expanded form for the claim shape at hand.

Deliberately absent: worked examples. Examples anchor future runs on their domains and verdict shapes; every prediction deserves a tree grown from its own premises. Where an entry needs to convey "how concrete" or "how long," it says so directly.

## Table of contents

- [N0 — Intake, Interview & Canonicalization](#n0--intake-interview--canonicalization)
- [N1 — Reference Class & Base Rates](#n1--reference-class--base-rates)
- [N2 — Decomposition & Shared Premises](#n2--decomposition--shared-premises)
- [N3 — Load-Bearing Analysis & Durability Sort](#n3--load-bearing-analysis--durability-sort)
- [N4 — Mechanism Stress-Test](#n4--mechanism-stress-test)
- [N5 — Evidence Audit](#n5--evidence-audit)
- [N6 — Analogy Court](#n6--analogy-court)
- [N7 — Transition Shape & Political Economy](#n7--transition-shape--political-economy)
- [N8 — Regime Split & Recomposition](#n8--regime-split--recomposition)
- [N9 — Semantic Dissolution Check](#n9--semantic-dissolution-check)
- [N10 — Adversarial Pass](#n10--adversarial-pass)
- [N11 — Verdict & Watchboard](#n11--verdict--watchboard)

---

## N0 — Intake, Interview & Canonicalization

**Question:** What is actually being claimed, about what, by when, and what would count as true?

**Why it exists:** Messy predictions smuggle their conclusions inside their vocabulary. Predicates like "antiquated," "dead," "wins," "replaces" can each resolve true and false simultaneously depending on definitions nobody wrote down. Most bad forecasting arguments are not wrong; they are *unresolvable*, and unresolvable claims let the arguer claim victory under any outcome. Canonicalization is the single highest-leverage step in the chain: a claim made resolvable is half answered. And because the definitional choices often belong to the person who brought the prediction, this node is also where the user is interviewed — before the tree takes any shape they didn't choose.

**Procedure:**

1. **Capture verbatim.** Paste the user's prediction exactly as given — the whole message, thread, or transcript. The original wording is evidence about what the predictor actually believes; N9 needs it to check for definitional drift, N11 to verify the verdict answers what was asked rather than a convenient restatement.
2. **Draft the claim extraction.** One sentence often bundles several claims. Assign IDs: C1, C2, … Include implicit claims that do argumentative work — a universal "law," an offered mechanism, an evidence-claim — even when phrased as truisms. This draft is preliminary; it exists so the interview can ask informed questions.
3. **Run the pre-tree interview** (attended sessions — full mechanics in SKILL.md § Setup). Ask only what changes the tree: horizons; the intended meaning of each vague predicate (offer candidate resolvable definitions); scope priority among the drafted claims; facts to stipulate vs verify; depth; purpose and stakes; optionally the user's own stance and preferred outcome. Binding rules: the user owns meanings, horizons, and scope; asserted facts enter the register as `assumed-from-user`; stated preferences are logged for N10's residue disclosure and bind nothing. Unattended: skip, choose defaults, state each one.
4. **Finalize the claim register.** Incorporate the interview: re-extract, merge, or drop claims per the user's scope answers. Attach an explicit horizon to every claim; flag any horizon you supplied yourself.
5. **Do the definitional work.** For each vague predicate, fix a resolvable definition — the user's if they chose one, otherwise yours, defended in a sentence. Distinguish properties the predicate might conflate (being old versus being dominated-and-abandoned; changing form versus ceasing to exist; losing share versus losing the niche). Do this before forming any view of the verdict, and if a definition choice by itself predetermines a verdict, record that in bold: it is a finding, not a footnote.
6. **Diagnose claim shape(s)** against the adaptation table in SKILL.md. A bundle can span shapes. Record which nodes will run expanded and why — this is the **node plan**, and it is the written answer to "how many nodes does this question require."
7. **Declare modes** (reasoning-first vs research; full vs compact) per the interview or defaults, and open the **fact register** with any facts the user supplied, marked `assumed-from-user`.

**Produce & decide:** the verbatim capture; the interview record (Q&A verbatim, plus how each answer shaped what follows); a canonical claim register with per-claim horizons and *functional* resolution criteria; fixed definitions with rejected alternatives; the shape diagnosis; the node plan; the opened fact register. The decisions owned here: what counts as a distinct claim, what each vague predicate means, and which nodes will run expanded.

**Branch space:** This node rarely branches on truth — it branches on *framing*: which decomposition to adopt, which definition of each vague predicate to fix. Enumerate the 2–3 plausible definitions per predicate and record which was fixed and why.

**Failure modes:** Canonicalizing into a claim easier to attack than the user's actual claim (strawman-by-intake). Fixing a definition after seeing which verdict it produces. Dropping implicit claims as "just rhetoric" — they are usually the engine of the argument. Asking interview questions whose answers change nothing (each question spends the user's attention; ask only tree-changing ones).

---

## N1 — Reference Class & Base Rates

**Question:** What kind of claim is this, and how often do claims of this kind come true?

**Why it exists:** Every prediction arrives wearing its favorite precedent. The reference class is chosen *by the arguer*, and the choice is usually the argument. This node takes the choice back: assign the class deliberately, pull the base rate from the whole class — including the members nobody remembers — and set a prior before touching the specifics.

**Procedure:**

1. **Assign the reference class(es)** for each claim. Name the class precisely — not a broad genre but a shape-and-scale-matched class ("predictions of full substitution of an entrenched, infrastructure-scale incumbent within a century" is a class; "technology predictions" is not). If two classes fit, carry both and note where their base rates diverge.
2. **Run the survivorship sweep.** List the class's famous successes — then force-list its *failures*: confident same-shape predictions that did not resolve. Failures are systematically underweighted in memory because nothing memorializes them. Keep listing until failures at least match successes, or you can defend why they can't.
3. **Extract the pattern of outcomes,** not just the rate. Ask what the class's *modal* outcome actually was: full extinction of the incumbent, partial displacement into a defended niche, coexistence, absorption of the challenger, reversal. Treat any generalization you're tempted to assert (for instance, that extinction is rare and retreat-to-niche common in substitution classes, or that rival grand systems tend to get demoted rather than defeated) as a hypothesis the sweep must confirm or overturn for *this* class — never as an assumption imported into it.
4. **Set the prior** per claim, in confidence-grammar terms, and write the sentence: "Walking in, before specifics, a claim of this shape resolves true about X% of the time, so the prior is ___."
5. **Note what would make this claim an outlier** from its class — the specific findings Phase II would need to establish for the claim to beat its base rate.

**Produce & decide:** the named class(es) per claim with the naming defended; the survivorship sweep with failures listed; the class's outcome pattern; a prior per claim in grammar terms; the outlier conditions. The decision owned here: the prior — and whether the class is well-formed enough to supply one (if not, declare it and widen all downstream bands).

**Branch space:** prior-favors-claim / prior-against-claim / class-ambiguous-carry-both / class-degenerate (no real precedents — the analysis will lean entirely on N3–N7; log that bands must widen).

**Failure modes:** Letting the arguer's precedent choose the class. Sampling only remembered successes. Using the base rate as the verdict instead of the prior — the whole point of Phase II is that specifics can beat the class.

---

## N2 — Decomposition & Shared Premises

**Question:** What separable legs does the claim bundle, and what premises do the rivals secretly share?

**Why it exists:** Compound claims launder weak legs through strong ones: a highly plausible leg lends its credibility to a contested one, and a false universal "law" rides along unexamined because it's phrased as common sense. Severing the legs — and scoring them independently forever after — is where split verdicts come from, and split verdicts are usually the truth. The second job only bites for rival-system claims: **rivals share premises**, and shared premises are invisible to both sides precisely because no one is arguing about them.

**Procedure:**

1. **Unbundle** the canonical claims into their finest separately-evaluable legs. For each leg record: what it asserts, what it depends on, which other legs it is *actually* independent of. Hidden independence matters as much as hidden dependence — a leg that survives even if its famous sibling falls should be marked as protected.
2. **Draw the dependency graph.** Some legs are premises of others. A refuted premise-leg weakens its dependents; a refuted dependent leaves the premise untouched. Write the arrows down — N8 recomposes along them and N11's fragility profile is built from them.
3. **Refuse borrowed strength — permanently.** From this node on, every leg is scored alone. If a later node's finding on one leg makes another *feel* stronger without an arrow in the graph, that is the launder reasserting itself; name it and cut it.
4. **For rival-system claims, decompose both sides into four strata:** *mechanisms* (the causal machinery by which the system delivers what it delivers), *instruments* (the current implementations of those mechanisms), *demands* (what the system's constituents actually want from it), and *premises* (what it assumes about the world). Instruments are the most mutable stratum and mechanisms the least — a "system X is doomed" claim is very often true about an instrument and false about the mechanism, and telling those apart is this step's yield.
5. **Hunt the shared premises.** Ask: what do both rivals assume that neither argues for? Shared premises are the largest attack surface for external shocks, because a shock through the shared basement hits both combatants while their famous disagreement stays untouched upstairs. A prediction that "A beats B" can be wrong not because B wins but because the A-vs-B axis dissolves — and this step is the only place that outcome becomes visible in advance.

**Produce & decide:** the leg inventory; the dependency graph (arrows explicit); for rival-system claims, the four-strata table per side and the shared-premise list. The decisions owned here: the grain of decomposition, and which dependencies are real arrows versus rhetorical adjacency.

**Branch space:** clean-decomposition / legs-inseparable (rare; document why and carry the bundle whole with widened bands) / decomposition-reveals-the-real-claim (common: the headline claim turns out to be a corollary of an unstated one — promote the unstated claim to the register via a REVISED block in N0).

**Failure modes:** Decomposing so finely that legs lose meaning. Missing implicit premise-legs. Doing the severing here and quietly re-bundling at N8 — watch for verdict language asserting "and therefore the broader claim" with no licensing arrow.

---

## N3 — Load-Bearing Analysis & Durability Sort

**Question:** What does the incumbent's advantage actually rest on, and which of those premises survive the horizon?

**Why it exists:** This is the heart of the method, and the reason it beats forward simulation. The question is never "will the challenger improve?" — the answer is always yes. The question is "**what is the incumbent's advantage made of?**" If it is made of costs, the challenger's improvement erodes it. If it is made of constraints no technology moves, no amount of improvement touches it. A long-horizon forecast doesn't require predicting decades of events; it requires correctly classifying a handful of present-tense premises by durability. That classification is checkable *now*, which is what makes long-horizon reasoning tractable at all.

**Procedure:**

1. **For each leg, list what the attacked thing rests on.** Name each advantage concretely enough to be sorted and argued with — a unit-cost figure at a stated utilization, a physical throughput or capacity limit, an owned asset, a legal privilege, a labor structure, a habit, a network of complements — never as a virtue-word. The prediction is usually attacking only one or two of these while gesturing at all of them; the full list is what exposes that.
2. **Sort every premise into three bins:**
   - **Invariant (wall):** survives the horizon regardless of technology. Physics and geometry; thermodynamics; arithmetic and definitional truths; game-theoretic gradients (defection, free-riding, principal–agent slippage, Goodhart's law — any metric under optimization pressure stops measuring); information constraints that are incentive-shaped (preference privacy, misreporting, credibility of commitments); **positional scarcity** (goods defined by rank cannot be made abundant — the deepest invariant, the last one standing at the longest horizons).
   - **Parameterized (dial):** a real constraint whose *position* technology moves. Computation cost; coordination and transaction costs (the boundary between market coordination and internal hierarchy sits where these dictate, and it moves); communication cost; enforcement and surveillance cost; energy cost; measurement precision. Note that many claimed impossibilities decompose into a computational component (dial) and an incentive component (wall) — sort the components, never the slogan. Misfiling a dial as a wall makes you the person insisting a thing is impossible while it ships; misfiling a wall as a dial makes you the person predicting it every decade.
   - **Mutable:** prices and cost structures, ownership models, regulation, organizational forms, business models, governance quality, fashion, specific firms and institutions. Anything that has changed within living memory is presumptively mutable at a century.
3. **Apply the master heuristic at the right rung** of the abstraction ladder (full ladder in `heuristics.md`): the lower the rung, the harder the walls; each step up, the invariants get fewer and softer, and bands must widen accordingly.
4. **Apply horizon adjustment.** Bins migrate with horizon: at long horizons treat all mutables as fully realized; at the longest horizons even human-regularity "walls" earn an asterisk, leaving only definitional invariants at full strength (rules in `heuristics.md` § Horizon rules). Log which premises changed bins under adjustment.
5. **Sort the challenger's premises too.** The challenger also rests on things; challengers routinely depend on the same class of goods or constraints the argument declares doomed, and finding that dependency here feeds the contradiction test at N4. Also check whether any wall that blocks the incumbent's replacement *reappears on the challenger's side* — a constraint that binds both parties reshapes the whole verdict.
6. **Render the pass/block finding per leg:** the leg *passes* where it attacks only mutables and dials; it is *blocked* where a wall carries the incumbent's advantage; it *splits* where different regimes lean on different bins — hand the split directly to N8; it *hinges on a dial* where the verdict depends on how far a dial moves — name the dial, its current position, direction, and rate.

**Produce & decide:** the durability table per leg (premise, bin, horizon-adjusted status, consequence), covering incumbent *and* challenger premises; the pass/block/split/hinges finding per leg with the carrying premise named. Every premise binned as an invariant gets a five-W block next to its table row (SKILL.md discipline 4): who holds or enforces it, what the constraint plainly is, when it holds and past what condition it stops being safe, where it applies, and why it can't be legislated, priced, or fashioned away. A missing W usually marks the spot where the premise is actually a dial or a mutable. The decisions owned here: every bin assignment — each is a checkable claim about the world, and together they are most of the verdict.

**Branch space:** passes-clean / blocked-by-named-wall / splits-by-regime / hinges-on-named-dial (a legitimate leaf: the deliverable becomes which dial, watched how). Ambiguous bin assignments are themselves findings — log them and put the premise on the watchboard.

**Failure modes:** Sorting by vividness instead of durability. Misfiling dials, in either direction. Forgetting the challenger's own premises. Stopping at the first wall found instead of completing the table — the full table is what N8 partitions on.

---

## N4 — Mechanism Stress-Test

**Question:** Do the causal mechanisms offered actually produce the predicted outcome?

**Why it exists:** Predictions usually come with a mechanism, and mechanisms feel more rigorous than trend lines — which makes a *broken* mechanism more dangerous than no mechanism. The three characteristic breaks: proving too much, internal contradiction, and velocity–destination confusion. A mechanism that survives all three, scoped correctly, is the strongest thing a forecast can own; most don't survive at full strength, but almost all salvage into something narrower and true. Salvage, don't just demolish — the scoped version is usually the argument's best insight.

**Procedure:** For each mechanism in the argument (N0/N2 will have registered them as claims):

1. **Proves-too-much test.** Universalize it. If the mechanism were a law, what long-lived counterexamples would have to not exist — and do they conspicuously exist anyway? A mechanism that predicts the disappearance of things that visibly persist is not a law. Find the scope condition that separates its hits from its misses, and keep the scoped version.
2. **Internal-contradiction test.** Trace the mechanism's own dependencies against the argument's other commitments — in particular, whether the challenger's own stack depends on the class of things the mechanism declares doomed. An argument that undercuts its own premises doesn't lose everything, but the contradiction marks exactly where its scope ends.
3. **Velocity–destination test.** Many true mechanisms predict *rates*, and arguments spend them as *outcomes*. A mechanism explaining why one side iterates or adapts faster does not by itself predict survival: slow-moving things with invariant advantages persist indefinitely. Label every surviving mechanism VELOCITY or DESTINATION. Velocity mechanisms feed N7 (they shape the transition); only DESTINATION mechanisms may support an endpoint verdict.
4. **Competitive-response test** (expanded for company/market claims). The mechanism assumes the world holds still. What do rivals, complements, substitutes, and regulators do *in response* to the mechanism operating — and does the mechanism survive the response? A mechanism that dies on first contact with an obvious countermove was never load-bearing.
5. **Write the salvage.** For each mechanism: the strongest *scoped* version that survives all tests, what it now predicts, and what it no longer predicts. Then re-check every leg that depended on the mechanism (per the N2 graph): did the leg need the full-strength version or only the scoped one?

**Produce & decide:** per mechanism — test results, the VELOCITY/DESTINATION label, the salvaged scoped version, and the re-check of dependent legs. The decisions owned here: the labels and the scope conditions; these determine which mechanisms are allowed anywhere near the endpoint verdict.

**Branch space (per mechanism):** holds-as-stated (rare) / holds-scoped (common — record the scope) / velocity-only / broken (record which test killed it, and what if anything the dependent legs have left).

**Failure modes:** Demolishing without salvaging. Accepting a velocity mechanism as a destination one because it is vivid. Universalizing against a strawman instead of the mechanism's best form.

---

## N5 — Evidence Audit

**Question:** Is the cited evidence probative, or merely accurate?

**Why it exists:** The most persuasive evidence in future-claims arguments is *true and irrelevant*. A figure can be perfectly factual and support nothing, because the comparison it sits inside is rigged — usually unintentionally — by where the boundaries were drawn. When the user has stipulated "assume the facts are correct," this node becomes *more* important, not less: with accuracy stipulated, probativeness is the only question left.

**Procedure:** For each evidence item in the argument, and each fact you find yourself relying on:

1. **Boundary-symmetry test.** Are the cost/benefit boundaries drawn identically for both sides of the comparison? A comparison where one side's figure is fully loaded and the other's is marginal — or where one side's externalities are counted and the other's are excluded — measures the boundary, not the rivals. Redraw both boundaries at matched scope before letting the numbers speak; expect sign flips.
2. **Denominator test.** Per-unit figures are ratios; interrogate the denominator. A ratio measured during a utilization collapse (or spike) is evidence about utilization, not about the technology or system. Ask what the numerator did on its own.
3. **Representativeness test.** Is the cited instance representative of its category? Rule: **when within-category variance exceeds the between-category gap, the evidence convicts an implementation, not an idea.** The same test catches the higher-abstraction version: comparing an *actually existing* instance of one system against an *idealized* version of its rival is a category error whichever direction it runs.
4. **Recency/trend test.** Is the datum a point on a curve? Which direction is the curve moving, at what rate — and is the rate itself durable (dial) or a one-off?
5. **Register and grade everything.** Each item enters the fact register with status and confidence, and each gets a probativeness grade: PROBATIVE (survives all tests and bears on a load-bearing premise) / WEAKENED (survives with reduced scope) / NON-PROBATIVE (accurate but irrelevant after correction). Where an item is downgraded, record what narrower claim it *does* support — evidence rarely evaporates; it usually relocates. Only PROBATIVE items may appear in the verdict's support.

**Produce & decide:** the graded evidence table; corrected comparisons at matched boundaries; the relocation note for every downgraded item; fact-register updates. The decisions owned here: the grades — and they are decisions about *relevance*, not truth.

**Branch space (per item):** supports-claim / supports-narrower-claim (state it) / convicts-implementation-not-category / neutralized. In research mode add: verified / contradicted-by-source.

**Failure modes:** Auditing only the opposing side's evidence — your own supporting facts get the same knives. Treating an audit kill as a refutation of the claim (neutralized evidence leaves a claim unsupported, not false). Skipping the register because the facts "seem fine."

---

## N6 — Analogy Court

**Question:** Do the offered analogies hold at the mechanism level — and what does the dominance pattern predict?

**Why it exists:** Analogies are how people think about the future, and they are almost always argued at the level of imagery rather than mechanism. An analogy is a *claim that two situations share causal structure* — so try it like a claim: identify the mechanism that drove the outcome in the source case, and check whether the target case has that mechanism. The court metaphor is procedural: the analogy gets a fair hearing, both sides argue, and a written verdict says exactly where it holds and where it breaks.

**Procedure:** For each analogy — offered by the argument, or introduced by you (introduce candidates deliberately; the court exists to try them, and a better analogy than the argument's own is a common and valuable output):

1. **Extract the source mechanism.** Why did the outcome happen in the source case, mechanically? Name the axes of competition, which side won each, and what made the outcome stick (in historical full-replacement cases, the sealing mechanism is typically collapse of the loser's support ecosystem below viability, making reversal impossible — check what actually sealed *this* source case rather than assuming).
2. **Run the dominance audit on the target.** List the axes on which the challenger beats the incumbent and the axes on which it loses, using axes *anyone materially weights*, not the axes either side's marketing emphasizes. The pattern is the prediction:
   - **Full dominance** (challenger wins every weighted axis) → substitution/extinction. Rare.
   - **Partial dominance** (wins some, loses others) → **stratification**: the incumbent retreats to the axes it wins. The modal case.
   - **No dominance ordering** (the axes themselves are contested values, weighted differently by different people with no shared scoreboard) → **hybridization**: extinction is structurally unavailable because there is nothing to lose *on*. The usual case for rival value-systems.
3. **Check ecosystem-collapse conditions.** Does the target incumbent's support ecosystem (suppliers, skills, institutions, complements) collapse below viability if volume falls substantially? If not, dormancy-and-revival stays available and "extinct" verdicts weaken to "dormant."
4. **For idea-targets, apply the revival asymmetry.** Artifacts die when their ecosystems die; ideas hibernate and get recombined or revived. An analogy from an artifact source to an idea target must be discounted for revival dynamics, whatever else it gets right.
5. **Issue the written verdict per analogy:** HOLDS / HOLDS-IN-REGIME (name the regime — feeds N8 directly) / BREAKS (name the mechanism the target lacks). Where the court introduced a better analogy, say what it predicts differently and why it maps more closely.

**Produce & decide:** per analogy — the extracted source mechanism, the dominance audit table, the ecosystem check, the written verdict. The decisions owned here: the verdicts, and the choice of which court-introduced analogies deserve a hearing.

**Branch space:** the per-analogy verdicts above, plus court-introduces-better-analogy. Note when an introduced analogy *strengthens* the user's claim beyond its original form — the court is not only a demolition site.

**Failure modes:** Vibe-level mapping. Auditing dominance only on the challenger's favorite axes. Forgetting that partial dominance is a *prediction* (stratification), not a tie.

---

## N7 — Transition Shape & Political Economy

**Question:** Even if the endpoint is right, what path gets there — and does the path change the answer?

**Why it exists:** Endpoint reasoning silently assumes the transition is free. It isn't, and for institution-shaped claims the transition *is* most of the question. Two facts dominate: individuals can defect from products but not from institutions, so institutional change requires collective action and arrives in punctuated bursts; and incumbents are defended by coalitions, not by efficiency, so arrangements can outlive their justification by decades. A verdict that ignores path is a verdict about a frictionless world.

**Procedure:**

1. **Count the veto points.** For each leg: who must agree for the predicted change, and who must merely *not resist*? Place the leg on the consensus spectrum, from single-party adoption decisions at one extreme to society-wide collective choices at the other. This is where N4's salvaged VELOCITY mechanisms cash in — they predict relative speed along this spectrum.
2. **Classify the defection mode.** Individual-defection changes diffuse smoothly along adoption curves. Collective-defection changes exhibit punctuated equilibrium, and the historical punctuation marks are systemic shocks. If the leg requires collective defection, the honest forecast states *what kind of shock* opens the window — and confidence about *timing* collapses even where confidence about *direction* survives. Report the two separately, always.
3. **Map the incumbent coalition.** Who loses from the change, how organized are they, and what institutional weapons do they hold (rule-making, licensing, procurement, agenda control)? Locked-in mediocrity — an inefficient arrangement persisting because its defenders sit on the levers — is always on the branch list, and at shorter horizons it is often the modal branch.
4. **Check reflexivity** (institution- and culture-shaped claims). Social systems read forecasts about themselves and metabolize critiques — absorbing the opposition's demands is a survival strategy available to institutions and unavailable to artifacts. Physical systems do not read your analysis. Reflexive targets make forecasts partially self-defeating or self-fulfilling; widen bands and note the feedback's direction.
5. **Estimate transition costs and who bears them.** A transition that strands a politically-protected asset class arrives far later than its cost-benefit math suggests. For cultural claims, run **cohort replacement math**: where change happens by generational turnover rather than persuasion, the floor on timing is demographic — count the cohorts and check the claim's horizon against the count. Identify any slow-turnover stock (physical, legal, or human) whose replacement rate sets a timing floor regardless of how the technology or argument moves.
6. **Feed the finding forward:** transition analysis modifies *timing and shape*, and sometimes converts a verdict into the distinct resolution "endpoint right, horizon too short" — flag that outcome explicitly wherever it is live.

**Produce & decide:** per leg — the veto-point count, defection-mode classification, coalition map, reflexivity note, timing floors with the stock that sets them, and the transition-shape finding (smooth / punctuated / blocked / endpoint-right-horizon-wrong). The decisions owned here: direction-vs-timing confidence, stated separately.

**Branch space:** smooth-diffusion / punctuated-needs-shock (name the shock class) / blocked-by-coalition-within-horizon / reflexive-self-modifying / endpoint-right-horizon-wrong.

**Failure modes:** Treating politics as noise around the "real" techno-economic answer — for institutional claims the politics *is* the mechanism. Using punctuated equilibrium as an excuse for unfalsifiable timing (the watchboard must still name observable precursors). Forgetting reflexivity cuts both ways.

---

## N8 — Regime Split & Recomposition

**Question:** In which regimes does the claim hold, in which is it blocked — and what do the legs sum to?

**Why it exists:** "It depends" is where lazy analysis stops; this node is where rigorous analysis makes "it depends" *pay*. Most long-horizon claims are true somewhere and false somewhere else, along boundaries N3 already located (different regimes lean on different premise-bins). Partitioning converts one unresolvable claim into several resolvable ones. Recomposition then reassembles per-leg, per-regime findings into claim-level verdicts *without re-bundling what N2 severed*.

**Procedure:**

1. **Choose partition dimensions from the durability table,** never from convention. Partition where the *binding premise changes bin* — a dimension along which one regime's incumbent leans on a wall while another regime's leans only on mutables. Candidate dimension types: intensity or density of use; physical vs digital substrate; governance or trust regime; task or component composition within a bundled activity. Two or three dimensions maximum — partitions multiply.
2. **Issue per-regime findings** for each leg: passes / blocked / hinges-on-dial, with the carrying premise and its bin named per regime, each citing the N3 table row it comes from.
3. **Recompose along the N2 dependency graph.** Premise-legs propagate with their N4 labels attached: a premise that failed as a law but survived scoped weakens only the dependents that needed the law form. Follow the arrows, not the vibes, and quote the arrow that licenses every "therefore."
4. **Apply weakest-link accounting.** Each claim-level verdict inherits the confidence of its weakest load-bearing node — name that node explicitly. If the weakest link embarrasses the verdict, the remedies are more work on that node or wider bands; averaging it away against stronger nodes is prohibited.
5. **State the recomposed verdicts** in confidence-grammar bands, per claim, per horizon, per regime — with all wideners (horizon, abstraction) already applied. This file is the verdict's engine room; N11 formats, but N8 decides.

**Produce & decide:** the partition with its defense; the per-regime findings table; the recomposition prose following the graph; the weakest-link table; the recomposed verdicts. The decisions owned here: the partition dimensions and every band.

**Branch space:** clean-split (regimes partition the claim exhaustively) / dominant-regime (one regime is most of the world — say which and why) / fractal-split (regimes subdivide further; stop at the grain the horizon can support and declare the remainder unknown).

**Failure modes:** Partitioning on convenient rather than binding dimensions. Re-bundling severed legs in the recomposed prose. Averaging across regimes into one mushy number — the split *is* the answer; report it split.

---

## N9 — Semantic Dissolution Check

**Question:** Will this claim resolve empirically or dissolve semantically — and what do we pre-commit to counting?

**Why it exists:** A large fraction of long-horizon bets never get to be wrong: they dissolve. The function survives under a different name; the name survives on a different function; or the question loses its referents entirely and stops being one anyone asks. Pre-committing resolution language now is the only defense — after the fact, every party reads the drift in their own favor, and the forecast becomes retroactively unfalsifiable.

**Procedure:**

1. **For each claim, enumerate the dissolution routes:** function-survives-name-dies; name-survives-function-dies; axis-dissolves (the organizing question gets demoted to a non-question); definitional drift in the predicate itself.
2. **Rate dissolution risk** (low / medium / high) per claim. Heuristic: risk rises with horizon and with abstraction — low-rung claims at short horizons mostly resolve empirically; high-rung claims at the longest horizons dissolve more often than they resolve.
3. **Write the pre-commitments.** For each medium-or-higher risk: "If [functional description] exists but is called [something else] or operated by [someone else], this claim resolves ___." Anchor in *functional* terms — mechanism-in-use, share of the function performed, throughput, ownership structure of the activity — never in names, brands, or banners. Pay special attention to the challenger-rebuilds-the-incumbent route: where the challenger's winning configuration would functionally reconstitute the incumbent under new branding, decide *now* which way that counts.
4. **Flag claims that are irreducibly semantic** — where, after honest effort, no functional resolution exists. Report them in N11 as unresolvable-as-stated rather than laundering them into fake precision; propose the nearest resolvable neighbor and answer that instead, labeled as such.

**Produce & decide:** per claim — dissolution routes, risk rating, written pre-commitments in functional language, and any irreducibly-semantic flags with the nearest resolvable neighbor named. The decision owned here: what counts, committed before the verdict exists.

**Branch space (per claim):** resolves-empirically / dissolves-unless-precommitted (attach the pre-commitment) / irreducibly-semantic (demote in N11, answer the neighbor).

**Failure modes:** Writing pre-commitments *after* the verdict (they will favor it — this is why N9 precedes N10 and N11). Anchoring in names. Treating dissolution as failure — correctly forecasting that a question will dissolve is itself a strong forecast, sometimes the strongest available.

---

## N10 — Adversarial Pass

**Question:** What is the best case for the opposite verdict, who holds it seriously, and what world-states vindicate them?

**Why it exists:** Every node so far was performed by the same analyst, subject to the same drift toward coherence — a tree grown by one hand leans one way. The adversarial pass is the institutional correction: argue the other side *using this ledger*, not a strawman of it. The standard is uncomfortable: each steelman must be strong enough that a smart partisan of the opposite verdict would sign it. Verdicts that survive get shipped; verdicts that wobble get their bands widened or their nodes reworked. Both outcomes are wins.

**Procedure:**

1. **Steelman the opposite verdict from inside the ledger.** For each claim-level verdict from N8, construct the best argument that the *other* branch at each load-bearing node was correct — attacking the named weakest links first: the bin assignments most contestable in N3, the reference class choice, any definitional fixing at N0 that predetermined an outcome. If the steelman requires an argument the tree never considered, that is an upstream gap: REVISED block first, then attack the repaired tree.
2. **Enumerate the rival live forecasts** — positions actually held by serious people, stated fairly enough that a holder would sign the summary, each with its vindication condition: the observable world-state under which *they* were right and this ledger wrong. These become watchboard rows, not debris.
3. **Compile the flip-list.** From the sensitivity threads (§7 of every node file): the minimal set of node-flips that reverses each verdict, ranked by plausibility. A verdict whose flip-list is a single plausible item is fragile *and ships flagged as fragile*, whatever its band says.
4. **Run the anti-pattern checklist** (`heuristics.md`) over the whole ledger — including this file.
5. **Disclose the normative residue.** Where the analysis touches values: state that the forecast is not an endorsement; name where the analyst's own sympathies (and the user's stated preferences from the intake interview) could plausibly have leaned on a sort, a definition, or a band; and identify what in the ledger binds the verdict to observables regardless — the functional pre-commitments are the usual answer. Naming the lean is the available honesty; claiming to have none is not.
6. **Disposition each finding:** verdict-stands / bands-widened (REVISED block in N8) / node-reworked (REVISED upstream, dependents re-run) / verdict-reversed (rare; when it happens, the ledger shows exactly which node was wrong — which is the system working).

**Produce & decide:** per verdict — the signed-quality steelman with an honest assessment, the rival-forecast table with vindication conditions, the ranked flip-list with a fragility call, the checklist results, the residue disclosure, and the dispositions with their REVISED trails. The decision owned here: whether each verdict ships as-is, widened, reworked, or reversed.

**Branch space:** the dispositions above, per claim.

**Failure modes:** Steelmanning the weakest opposing argument. Running the checklist as a checkbox. Treating a survived adversarial pass as added confidence — it caps overconfidence; it never adds.

---

## N11 — Verdict & Watchboard

**Question:** What, finally, is the answer — and how will we know if it's going wrong?

**Why it exists:** The user started with a messy gesture at the future; they are owed binary-adjacent statements they could, in principle, bet on — plus the honest accounting of what would change the answer. The verdict is also the tree's audit: it must be *derivable* from the node files with no new reasoning. Anything appearing here for the first time belongs in an upstream node — put it there and re-derive. The watchboard is what makes the forecast a living object rather than a hot take with footnotes.

**Procedure:**

1. **Restate the original prediction verbatim,** then render per-claim verdicts: resolvable statement (with N9 pre-commitments baked into the wording), horizon, regime splits, band in confidence grammar, and the weakest-link node named inline. Splits are reported split, never averaged.
2. **Write the one-line compression per claim** — the single sentence that carries the whole finding, of the form "the claim passes/blocks/splits because [carrying premise, bin]." If a claim can't be compressed to one line, its analysis isn't finished; find the unresolved node.
3. **Publish the fragility profile:** the flip-list per verdict, load-bearing nodes ranked, and — in plain words — the single most load-bearing judgment in the whole tree.
4. **List falsifiers** — near-term observables that would show each verdict going wrong *early*, visible within years, not restatements of the claim at horizon. A verdict with no near-term falsifier says so explicitly; that fact is itself worth knowing.
5. **Build the watchboard:** for every dial the analysis hinges on, every declared unknown, and every rival forecast — indicator, current reading, threshold, expected observation window, and the *specific* revision each trigger causes ("move [claim × regime] one band toward/away from the claim"). Written so a future session can re-open the ledger, check the board, and append REVISED blocks without re-deriving the tree.
6. **Do the node accounting:** which nodes ran expanded and whether the expansion earned its cost; which were decisive (the verdict's content traces to them); which contributed nothing for this claim shape (honest feedback for the skill itself); where a broad gesture would have stopped — typically at the reference-class vibe — and what the remaining nodes added; and the count: how many nodes did truly attempting this question require?
7. **Verify terminality.** Walk every leaf: invariant / probability-with-named-sensitivities / declared-unknown-with-watch-indicator. Anything else — back upstream; the tree isn't done. "Only time will tell" appearing anywhere in the file means the audit failed: the watchboard exists so that time *telling* is scheduled and legible.
8. **Deliver** per SKILL.md: conversational summary (compressions, bands, most load-bearing node), send the verdict file, offer the run-directory zip and the artifact once.

**Produce & decide:** the verdict file in full — verdicts, compressions, fragility profile, falsifiers, watchboard, node accounting, terminality audit, honest limits. The decision owned here: none new — and that absence is the audit; this node formats and certifies what N8 decided and N10 stress-tested.

**Branch space:** none. If writing the verdict surfaces a new branch, that's an upstream gap: REVISED block, re-run dependents, then return.

**Failure modes:** New arguments appearing at the verdict. Hedging language that undoes the binary-adjacent commitment. A watchboard of unobservables. Skipping node accounting — it is the skill's own feedback loop and half the reason the ledger exists.
