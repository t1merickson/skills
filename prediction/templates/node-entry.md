# N{{n}} — {{Node name}}

<!-- Universal skeleton for nodes N1–N7 and N9 (N0, N8, N10, N11 have dedicated templates).
     Instantiate as NN-<node-slug>.md. Replace blockquote guidance with content.
     The 11 sections are fixed — same skeleton every node, every run — because comparability
     across nodes and across runs is what makes the ledger auditable. If a section is truly
     empty for this node, write "None" and one sentence why; never delete the section. -->

**Run:** `{{slug}}` · **Node:** N{{n}} of the plan in 00-INTAKE §5 · **Mode:** {{standard/expanded}} · **Date:** {{...}}
**Claims covered:** {{C1, C2, ...}}

## 1. Question this node answers

> One sentence, from the node library — restated in this prediction's terms, not copied generically. If you cannot restate it concretely for this claim, the node may not apply as planned; check the node plan before proceeding.

## 2. Inputs

> What this node consumes from upstream: specific findings (cite file §), the claims in scope, relevant fact-register rows (F#). Listing inputs is what keeps the dependency threading honest — if a "finding" appears in §4 that has no ancestor here and no new-fact row in §10, it teleported in, which is retrofit's tell.

- From `{{file}}` §{{n}}: {{finding}}
- Fact register: F{{...}}

## 3. Procedure

> What was actually done, as numbered steps mapped to the node-library procedure — including steps attempted that produced nothing (a dominance audit that found no clean axes is a result). Deviations from the library procedure are allowed and must be stated with reasons.

## 4. Findings

> The analysis itself — the longest section, prose-first, one subsection per claim in scope. Write it so a reader who opens THIS FILE COLD can reconstruct the reasoning without the conversation: state the argument, not just its conclusion. Tables where the node produces sorts or audits (N3's durability table, N5's evidence grades, N6's dominance audit). For a full run expect 300–800 words per claim here; compact mode compresses wording, never reasoning steps.

### {{C1}}

### {{C2}}

## 5. Branches

> Enumerate 2–5 possible outcomes OF THIS NODE'S QUESTION (not of the overall prediction), each with a coarse weight summing to ~1.0, and — the part that makes the tree re-enterable — what evidence or argument WOULD HAVE selected it. If you cannot articulate a selector for a branch, it isn't a real branch; replace it. A node where one branch gets ~1.0 is either trivially settled (fine — say why) or under-imagined (anti-pattern check).

| Branch | Weight | What would have selected it |
|--------|--------|-----------------------------|
| {{outcome A}} | {{0.x}} | {{selector}} |
| {{outcome B}} | {{0.x}} | {{selector}} |

## 6. Selection & why-chain

> The branch selected (or the weighted split carried forward), then the why-chain: the reasoning from §4 findings to this selection, step by step. Every "because" should trace to a §4 finding, an upstream input (§2), or a register fact — that's the chain a reader audits.

## 7. Flip conditions

> What specific evidence, argument, or world-state reverses THIS NODE's selection. Concrete and observable where possible ("a named observable crossing a named threshold by a named date"), not generic ("new information"). These feed N10's flip-list and N11's watchboard verbatim — write them so they can be pasted there unchanged.

## 8. Downstream dependencies

> Which later nodes consume this selection, and what happens to the final verdict if this node flips: "flips C1-dense verdict one band toward the claim" / "no verdict impact; timing only." If the answer is "nothing depends on this," ask whether the node needed to run expanded — note it for N11's accounting either way.

## 9. Confidence

> Band (confidence grammar) for this node's selection, the dominant source of uncertainty in one sentence, and which register facts cap it. Apply the wideners (horizon, abstraction) where they bite and say so.

## 10. Fact-register additions

> New facts first relied on in this node — append them to 00-INTAKE §7 and list the row numbers here. "None" is common and fine.

## 11. Open questions carried forward

> What this node leaves unresolved, tagged with the node expected to resolve it. An open question no downstream node will resolve becomes a declared-unknown leaf — flag it now so N11 can give it a watch indicator rather than discovering the gap at delivery.

<!-- ## REVISED — {{date, forcing node}}
What changed: ... · What forced it: ... · Downstream effects re-run: ... -->
