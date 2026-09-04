# Interface-integrity failure lenses

Use this reference for a full interaction audit or to select the few lenses relevant to a consequential flow. These are not twelve mandatory sections in every report. They are ways to locate broken promises between a person and a product.

## 1. Make the ordinary action findable

- Are frequent and state-critical actions visible before hover, right-click, a hidden gesture, or onboarding?
- Do scrollbars, clipping, pagination, or other cues reveal that more content exists and roughly where the person is?
- Does an overflow menu contain genuinely secondary work, or did “cleanliness” displace the primary action into memory and exploration?
- Can a person recover the route later without replaying a tour?

Possible is not the same as discoverable. A shortcut or expert gesture is an accelerator only when an ordinary route also exists.

## 2. Make controls keep their promises

- Does each control look like the kind of thing it is: button, field, link, selector, toggle, disclosure, or status?
- Does the symbol describe the current state or the action that will happen next, and is that distinction unambiguous?
- Do identical-looking controls behave alike, and do different-looking controls signal a meaningful difference?
- Do grouping and placement imply the correct object and scope?

Familiar symbols and shapes carry learned contracts. Novelty must repay the prediction cost it creates.

## 3. Make consequential language resolve the decision

- Do labels name the verb, object, and scope where misunderstanding has a cost?
- Do the prompt and action label agree, especially for deletion, replacement, sharing, authorization, or cancellation?
- Can negation be replaced with a direct statement of the resulting state?
- Is the interface asking for information it already has?

Generic dialog mechanics such as “OK,” “Yes,” and “Cancel” are poor substitutes for an action when the consequence matters.

## 4. Keep the interface stable while it is used

- Can a pointer, finger, focus ring, or switch target finish the approach it began?
- Does hover reveal information without swapping, moving, or covering the intended target?
- Does local input respond immediately, even when final work is asynchronous?
- Does motion explain identity, containment, progress, or causality rather than delaying the task?

Pointer movement is not consent. Spatial stability is a correctness property because the target embodies the person's plan.

## 5. Treat attention as user-owned

- Does an alert, modal, notification, survey, upsell, tutorial, or update deserve to outrank the active task right now?
- Can the interruption be dismissed, deferred, or handled in context?
- Does the product announce a non-event, repeat an already visible result, or demand acknowledgement for routine success?
- Can onboarding be skipped and revisited without blocking use?

Use the least interruptive surface that still matches urgency and consequence. Every producer cannot declare itself urgent without destroying the channel.

## 6. Make chrome earn its space

- Does a larger viewport reveal at least as much useful content and context as a smaller one?
- Are full labels truncated while decorative margins, overlays, headers, or panels consume available room?
- Are type, contrast, and target sizes legible at the real operating distance?
- Does “Show more” save more space and attention than it costs?

Density is not automatically good and whitespace is not automatically bad. The test is whether each region helps the person understand or operate the work.

## 7. Protect the ordinary path before exceptional features

- Can a first-time and returning person reliably create, open, save, copy, attach, share, search, filter, pause, cancel, and resume where those actions belong?
- Does a local action depend unnecessarily on network, account, promotion, or policy machinery?
- Does the empty or welcome state expose the obvious first action?
- Can the interface prevent impossible states instead of explaining them after the fact?

An advanced feature does not offset a missing basic act. Test the primary job before admiring the feature inventory.

## 8. Keep retrieval honest

- Do exact matches, filters, sort order, dates, and “recent” mean what their labels promise?
- Are approximate matches, recommendations, promotions, or remote results visibly distinct from requested results?
- Does the interface admit that no result exists instead of padding the answer with noise?
- Are active filters and ordering controls visible near the result they govern?

Retrieval answers the person's question. Recommendation answers a different question and must not silently take its place.

## 9. Preserve agency over durable state

- Does the product change names, settings, files, authentication, playback, subscriptions, or defaults without a clear request?
- Is declining, opting out, or undoing comparable in clarity and effort to accepting?
- Is identity actually required for the task, or merely useful to the product?
- Are automation and “recommended” defaults understandable, reversible, and bounded?

Convenience is automation that preserves intent. Silent mutation with an obscure escape route is loss of control.

## 10. Design for real bodies, inputs, languages, and machines

- Do visible bounds match hit targets, including during motion?
- Can the core path work with keyboard and relevant assistive input, not only an ideal pointer or touch sequence?
- Does state survive grayscale, increased contrast, reduced motion, long text, localization, and mixed writing direction?
- Does ordinary hardware remain responsive enough to preserve cause and effect?
- Do loading, failure, cancellation, and recovery receive the same design attention as success?

Accessibility, localization, and performance are not separate polish passes when they determine whether the ordinary interaction works.

## 11. Give repeated truth one authority

- When state, status, selection, naming, or controls appear in several places, which source is authoritative?
- Can cached, cross-device, optimistic, or asynchronous copies visibly disagree?
- Does one operation have several incompatible models across screens or products?
- Do stale notifications or selections survive after the underlying event changes?

Duplication is not inherently wrong. Contradiction is: it forces the person to reverse-engineer which surface to trust.

## 12. Design for the physical situation

- How much attention, precision, reach, time, and working memory does the real setting permit?
- What do vibration, motion, glare, noise, gloves, fatigue, divided attention, or urgency do to the abstract control?
- Does the interaction match the person's mental model of the physical process?
- Are safety-critical or destructive choices unmistakably different from routine ones?
- Does the control offer choices that make sense in the actual situation rather than merely exposing implementation range?

Context changes error cost. A pattern acceptable at a desk may be negligent in a vehicle, workshop, public kiosk, or emergency workflow.

## Cross-cutting diagnosis

Several lenses often point to one root cause:

- “Clean” presentation may have hidden complexity instead of removing it.
- A popup, animation, autoplay, and recommendation can all be competing claims on user-owned attention.
- A misleading status may originate in data authority, asynchronous code, product policy, and copy at once.
- Complexity compounds at boundaries: accounts across services, files across devices, and state across views need explicit ownership.

Fix the shared cause when possible. Twelve local cosmetic patches around one broken authority or product rule will drift apart again.

## Provenance and limits

These lenses work backwards from *The Grumpy Guide to Worst Practices*, a synthesis of 1,800 Grumpy Website posts spanning July 2017 through August 2026. The source is valuable as a long-running field diary of friction and broken product relationships, not as a random sample or controlled usability study.

Use its recurring failures to form questions and catch risks. Do not use them to estimate industry prevalence, claim that an example describes the current version of a product, or replace direct observation of the product and people under review. Many original posts depend on images or video, historical tags are sparse, and categories overlap.
