---
name: transitional-interfaces
description: Design the structural connection between two related interface states. Use when a static design omits how identity, containment, position, or set membership survives a state change.
---

# Transitional interfaces

This skill decides one edge on the map from `spatial-interfaces`. It does not choose curves, durations, or library syntax.

## Name the relationship

Start with the truth the connection must carry:

| Relationship | Structural choice |
|---|---|
| same object, more detail | preserve identity; expand or transform its container |
| container and contents | show entering/leaving that container |
| peers on an ordered axis | carry direction and position among peers |
| member joining/leaving a set | show both membership and the set making/closing room |
| different contexts with no spatial relation | fade through or cut without inventing continuity |
| genuinely unrelated states | a cut may be correct |

If the states have no defensible relationship, motion that fabricates one is worse than a cut. If they are related and identity vanishes in one frame, the connection is underspecified.

## Choose the structural form

- **Push/navigate** when the destination is a distinct place reachable through other routes.
- **Expand in place** when the detail belongs to the selected item and return to the set is the likely next move.
- **Sheet/popover** when the task concerns the item but its origin should remain visible and cheaply recoverable.

For insertion, let the set make room and the member occupy it. For removal, let the member leave and then close the gap. These may overlap, but the eye must be able to distinguish a membership change from a re-sort.

## Preserve truth under real conditions

- Do not gate response on a network round trip. Reconcile optimistic state explicitly; failure should not masquerade as user removal.
- Place optimistic content only where it can remain, or avoid promising placement before the server decides order.
- Match skeleton geometry to the content that replaces it.
- Reduced Motion keeps identity and containment in the resting states, using a calmer transition such as a crossfade.
- Deep links, restoration, missed motion, and time away mean the destination still needs orientation and an exit in a screenshot.
- Focus, accessibility announcements, and input ownership move with the visual state; continuity that strands keyboard or screen-reader users is not continuity.

## Implement after the decision

Use the project's existing primitives first: platform transitions, layout animation, shared-element APIs, or a measured FLIP implementation. Check current support when choosing a web or native API; browser versions and framework capability belong in implementation research, not this stable skill.

Do not specify milliseconds here. Hand curve, spring, and reduced-motion implementation to the platform motion guidance, then verify the rendered interaction can be interrupted and does not delay input.

## Output

State the two endpoints, their relationship, chosen structural form, identity/containment cue, enter and exit paths, arbitrary-entry fallback, reduced-motion equivalent, focus/accessibility handoff, data-latency behavior, and the implementation evidence still needed.
