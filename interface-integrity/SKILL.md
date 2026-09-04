---
name: interface-integrity
description: "Design or audit interactive product behavior when the user asks whether controls, state, feedback, interruptions, retrieval, or recovery are predictable and trustworthy, or explicitly requests review of a consequential flow. Do not use for static visual styling, isolated copy edits, animation mechanics, navigation-map work, or routine implementation with no interaction decision."
---

# Interface integrity

An interface is a set of promises. Its appearance, words, placement, and response should let a person predict what will happen, do the ordinary thing, know what happened, and remain in control. Treat failures here as product-correctness failures, not merely taste or polish.

This skill is for a real interaction decision or flow-level audit. Keep a scoped change scoped. Do not turn every button edit into a twelve-part review.

## Name the contract before judging the screen

Establish:

- the person and physical situation;
- the ordinary job they came to do;
- the object and state they believe they are acting on;
- the visible action and expected consequence;
- what feedback establishes success, progress, or failure;
- what can be undone, cancelled, retried, or recovered;
- which product needs, if any, are allowed to interrupt the task.

Write the critical interaction as a plain contract:

> When the person performs **action** on **object**, the product will produce **result**. It will show **feedback**. If the operation fails, it preserves **state** and offers **recovery**.

If that sentence needs hidden conditions, contradictory verbs, or several meanings for the same state, the design is not ready for visual polish.

## Hold five invariants

- **Findable:** the ordinary action has a visible, recognizable route. Hover, context menus, gestures, shortcuts, and onboarding may accelerate discovery; they cannot be the only route to essential work.
- **Predictable:** a control's form, label, location, and current appearance agree about what it is and what activating it will do. State and action are not interchangeable.
- **Stable:** targets do not move, change identity, or become covered while the person approaches or operates them. Feedback begins close enough to the action that cause and result remain legible.
- **Truthful:** progress, filters, search, status, selection, and completion report reality. An honest empty result is better than unrelated filler; a failure never wears success styling.
- **Recoverable:** cancellation, undo, retry, drafts, preserved input, and safe defaults keep a routine mistake or transient failure from becoming loss.

## Walk the ordinary path first

Trace the shortest normal path through entry, action, progress, completion, and return. Include the empty, loading, failed, cancelled, and resumed states where they can occur.

For each consequential step, record:

| Question | Evidence to seek |
|---|---|
| What is the person's intent? | The ordinary job in their language, not the product's feature name. |
| How do they find the action? | A visible control, menu, label, affordance, or established convention. |
| What do they predict? | The control's semantics, object, scope, and current state. |
| What happens immediately? | Stable target behavior and local acknowledgement. |
| What establishes completion? | One authoritative resulting state, not ceremonial confirmation. |
| What if it fails or is abandoned? | Preserved work, explicit consequence, and a credible recovery route. |

Do not let an ambitious edge feature compensate for a broken Create, Open, Save, Search, Copy, Share, Pause, Cancel, or Back path. Capability inventory is not interaction quality.

## Review the system, not just the pixels

Read [references/failure-lenses.md](references/failure-lenses.md) for a full audit or when a flow crosses several components, surfaces, devices, or teams. Use only the lenses implicated by a narrow task.

Look beyond the visible control when the cause lives in:

- copy that contradicts state or scope;
- asynchronous code that reports completion too early;
- duplicated state with no single authority;
- product policy that forces an account, interruption, promotion, or destructive default;
- responsive layout that hides information as space increases;
- performance that makes ordinary hardware or input methods second-class;
- automation that changes durable state without intelligible consent or reversal.

The smallest durable fix may cross copy, interaction design, implementation, data ownership, and product policy. Name that honestly instead of polishing the symptom in one layer.

## Rank by human consequence

Prioritize findings by:

1. frequency of the affected ordinary path;
2. consequence of a wrong prediction or failed action;
3. cost and clarity of recovery;
4. whether the failure blocks, misleads, interrupts, or merely annoys;
5. confidence in the evidence.

Separate an observed failure from a plausible risk. Preserve deliberate tradeoffs and existing strengths. Do not present personal preference, corpus frequency, or a familiar anecdote as user research about this product.

## Verify under non-ideal conditions

Exercise the actual interface with the relevant combinations of:

- keyboard, pointer, touch, screen reader, and reduced-motion settings;
- long or localized labels, mixed directionality, zoom or text scaling;
- slow network or hardware, delayed completion, partial data, and retry;
- empty, invalid, duplicate, stale, offline, cancelled, and destructive states;
- narrow and wide layouts, scrolling, focus changes, and arbitrary entry;
- repeated use, where animation, onboarding, or confirmation becomes tax.

Check that visible hit areas match interactive hit areas, targets remain stable during approach, state does not depend on color alone, and every durable mutation has the promised authority and recovery behavior.

## Report a useful verdict

Lead with whether the ordinary path is understandable and dependable. For each material finding, give:

1. the evidence and affected path;
2. the promise the interface makes;
3. how behavior breaks that promise;
4. the human consequence and realistic severity;
5. the smallest structural fix;
6. the verification that would prove the fix.

End with unresolved tradeoffs or evidence gaps. A good review leaves the team knowing what to change and how to tell whether it worked, not merely feeling scolded.
