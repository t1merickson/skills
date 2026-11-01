# Heuristics — the durability ladder, catalogs, confidence rules, and anti-patterns

Companion to `node-library.md`. The node library says *what to do at each step*; this file holds the reusable knowledge the steps draw on. N3 leans on the ladder and catalogs; every node leans on the confidence rules; N10 runs the anti-pattern catalog as a checklist.

## The abstraction ladder

The master heuristic — *technology erodes costs, not geometry* — is true as stated only at the bottom rung. Each step up the ladder, the available invariants get weaker and fewer, which is why confidence bands must widen with abstraction even when the reasoning feels equally tight. Locate the claim's rung during N0; apply the rung's phrasing during N3.

| Rung | Domain | Master heuristic | Strongest invariants available | Character of the invariants |
|------|--------|------------------|-------------------------------|------------------------------|
| L1 | Physical technology | Technology erodes **costs**, not **geometry** | Physics, thermodynamics, geometry | Walls. 100% durable at any horizon. |
| L2 | Infrastructure & systems | Technology erodes **operating costs**, not **network topology** | Throughput per unit of space, right-of-way geometry, queueing math | Walls, but regime-dependent — which topology binds depends on density. |
| L3 | Firms & markets | Competition erodes **margins**, not moats built on **physics or network effects** | Network effects, economies of scale floors, switching-cost math | Semi-durable. Network effects feel like walls and have historically been dials (they invert when interop is forced or the graph migrates). |
| L4 | Institutions & ideologies | Technology erodes **calculation and coordination costs**, not **incentive gradients** | Game theory: defection, free-riding, principal–agent, Goodhart; preference privacy and misreporting | Walls made of strategy, not matter. Durable against compute; softened only by changes to the players themselves. |
| L5 | Values, status, culture | **Nothing erodes positional scarcity** | Status is zero-sum by definition; attention is finite; authenticity is scarce *because* copyable | The deepest wall. Survives abundance in everything material — the last invariant standing at 200 years. |

Two ladder corollaries. **Cross-rung attacks are the strongest attacks:** a shock originating at a lower rung that propagates into premises the higher rung's combatants *share* beats any same-rung argument, because rivals do not defend their common basement. **Cross-rung analogies are the weakest analogies:** a source case from a low rung applied to a target on a high rung must survive the revival-asymmetry discount — artifacts die, ideas hibernate.

## The three catalogs

Sorting bins for N3. When a premise seems to fit two bins, that ambiguity is a finding — log it and put the premise on the watchboard.

### Invariants (walls)

- **Physics & geometry:** space, throughput per unit of physical corridor, speed-of-light latency, land area.
- **Thermodynamics:** energy floors for moving mass; heat dissipation.
- **Arithmetic & definitional truths:** zero-sum structures; positional scarcity (a good defined by rank cannot be made abundant); rebound identities (efficiency gains that raise total use).
- **Game-theoretic gradients:** incentive to defect, free-ride, misreport; principal–agent slippage; Goodhart's law (any metric under optimization pressure stops measuring); adverse selection.
- **Information constraints that are incentive-shaped:** preference privacy (people *won't* reveal, distinct from *can't compute*), tacit knowledge, credibility of commitments.
- **Slow biology** — human lifespan, development time, cognitive throughput. *Asterisk at 200 years:* biotech and AI mediation make these the first "invariants" to soften; treat as walls at 25y, load-bearing-with-asterisk at 100y, dials at 200y.
- **Geography:** distance, climate bands, resource placement. Softened only by transport-cost dials, never deleted.

### Dials (parameterized constraints technology moves)

- **Computation cost** — the computational component of many claimed impossibilities; it moves fast and in one direction.
- **Coordination & transaction costs** — set the boundary between market coordination and internal hierarchy; the boundary moves toward larger internally-coordinated islands as these costs fall.
- **Communication cost** — distance-as-barrier; remote coordination.
- **Enforcement & surveillance cost** — what property regimes are practical; what contraband is stoppable; what work is monitorable.
- **Energy cost** — the master input; a large move re-sorts every downstream premise.
- **Measurement precision** — what can be priced, contracted on, or optimized (and hence Goodharted — a dial that *feeds* a wall).

For every dial the analysis leans on, record: current position, direction, rate, and any known floor or ceiling. "Hinges on a dial" is a legitimate leaf — *which* dial, watched *how*, is the deliverable.

### Mutables

Prices and cost structures; ownership models; regulation and law; business models; org forms (the joint-stock corporation is a legal technology, not a law of nature); governance quality; fashion and taste; specific firms, parties, agencies. Presumption: anything that has changed within living memory is mutable at 100 years. At long horizons the analytical *risk* inverts — the common error isn't calling a mutable a wall, it's failing to notice how much of the incumbent's advantage was mutable all along.

## Horizon rules

- **~10 years:** institutions effectively fixed; only prices, products, and fashions move freely. Most "X is dead" claims at 10y are velocity claims in costume.
- **~25 years:** mutables move; dials move visibly; institutions bend, rarely break without a shock.
- **~100 years:** all mutables fully realized — no argument may lean on a current price, firm, regulation, or org form surviving. Dials assumed substantially moved (state direction, not endpoint). Institutions: assume at least one punctuation event; forecast direction, not dates.
- **~200 years:** only definitional invariants (physics, arithmetic, positional scarcity) and game-theoretic gradients hold at full strength; slow-biology invariants get the asterisk. Claims carried by anything weaker cap at "likely."

**Band-widening rule of thumb:** each doubling of horizon widens every band one step unless the claim is carried or blocked by a wall that survives the longer horizon. Walls are what let a 200-year claim stay "very likely" — nothing else does.

## Confidence grammar

| Term | Band | Betting intuition |
|------|------|-------------------|
| near-certain | 93–99% | would lay 20:1 |
| very likely | 80–93% | would lay 5:1 |
| likely | 65–80% | would lay 2:1 |
| lean | 55–65% | slight edge, small stakes |
| coin flip | 45–55% | no edge worth staking |
| lean against | 35–45% | slight edge against |
| unlikely | 20–35% | would take 2:1 against |
| very unlikely | 7–20% | would take 5:1 against |
| near-impossible | 1–7% | would take 20:1 against |

Reserve 0% and 100% for logical impossibility/necessity — empirical claims never earn them.

**Propagation rules:**

1. **Weakest link:** a verdict's confidence ≤ its weakest load-bearing node's confidence. Name the node whenever you state the verdict.
2. **Horizon widening:** per the rules above.
3. **Abstraction widening:** L4–L5 claims widen one band relative to the same reasoning at L1–L2 — strategic invariants are softer than physical ones, and reflexivity (targets that read forecasts about themselves) adds noise no analysis removes.
4. **No naked numbers:** every band ships with its sensitivity list. "Likely (would flip if [named dial] crosses [named threshold])" is a forecast; "likely" alone is a mood.
5. **Independence is earned:** combine probabilities across legs only where N2's dependency graph shows no arrow. Correlated legs move together — treating them as independent manufactures fake precision, and it always inflates confidence in the compound claim, never deflates it.

## Anti-pattern catalog

Fourteen recurring failures. Each: the tell (how it looks in the ledger) and the fix. N10 runs this as a checklist over the whole tree — including over N10 itself.

1. **Borrowed strength.** Compound claim's plausible leg lends credibility to its weak legs. *Tell:* verdict prose says "and therefore the broader claim…" without an N2 arrow licensing it. *Fix:* re-sever; score legs alone; check every "therefore" against the dependency graph.
2. **Vibe-level analogy.** Mapping imagery, not mechanism. *Tell:* the analogy never names the mechanism that drove the source outcome. *Fix:* N6 procedure — extract mechanism, audit dominance, written verdict.
3. **Forward simulation.** Narrating a future year-by-year and mistaking narrative coherence for probability. *Tell:* ledger contains scenario fiction; confidence rises with vividness. *Fix:* return to N3; sort constraints; scenarios only as *illustrations* of already-sorted outcomes, never as evidence.
4. **Survivorship sampling.** Base rate built from remembered successes. *Tell:* the N1 sweep lists only the class's famous successes and stops. *Fix:* force-list failures until they at least match successes or you can defend why they can't.
5. **Boundary asymmetry.** Cost/benefit boundaries drawn differently per side. *Tell:* one side's figure "fully loaded," the other's marginal; externalities counted once. *Fix:* redraw at matched scope before comparing; expect sign flips.
6. **Governance-as-physics.** One implementation's failure convicting the category. *Tell:* worst (or best) instance treated as representative; idealized-vs-actual comparisons. *Fix:* within-variance vs between-gap test at N5.
7. **Velocity–destination confusion.** A mechanism predicting *faster* spent as predicting *wins*. *Tell:* iteration-speed evidence cited for an endpoint verdict. *Fix:* N4 labels; only DESTINATION mechanisms support endpoints.
8. **Old ≠ antiquated.** Age read as obsolescence. *Tell:* "X is 150 years old" doing argumentative work. *Fix:* antiquated = dominated-and-abandoned; check for the domination, not the birthday.
9. **Proves-too-much mechanisms.** A "law" that predicts the disappearance of things that conspicuously exist. *Tell:* universal quantifiers ("everything," "always," "inevitably"). *Fix:* universalize at N4; find the scope condition; keep the scoped version.
10. **Point-probability theater.** Precise numbers with no sensitivity structure. *Tell:* "73%" with no flip-list. *Fix:* grammar bands + named sensitivities, always.
11. **Retrofit logging.** Writing node files after the verdict is chosen. *Tell:* zero REVISED blocks anywhere (real trees revise); every branch weight conveniently favoring the final answer. *Fix:* log-then-advance is the discipline; REVISED blocks are its receipts and their presence is evidence of health.
12. **Hidden normative residue.** Preference smuggled as forecast. *Tell:* verdict language turns approving/disapproving ("thankfully," "unfortunately"); durability sort keeps landing where the analyst's sympathies live. *Fix:* N10 disclosure; state the lean; separate "will" from "ought" in so many words.
13. **Semantic escape (unhedged).** Verdict wording that lets the claim win under any outcome. *Tell:* resolution criteria anchored in names, or the phrase "in some sense." *Fix:* N9 pre-commitments in functional terms, written before the verdict.
14. **The unfalsifiable hedge.** "Only time will tell," "it depends," "the truth is somewhere in between" as terminal moves. *Tell:* a leaf that is none of invariant / probability-with-sensitivities / unknown-with-indicator. *Fix:* the terminality criterion. "It depends" must become a regime split with per-regime verdicts; "time will tell" must become a watchboard row with a date. That conversion is the entire difference between this skill's output and a shrug.
