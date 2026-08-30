---
name: transitional-interfaces
description: Design the connection between two interface states, not the states themselves — deciding what relationship a transition has to carry and whether continuity can replace navigation chrome. Use when a flow moves between views, when a list gains or loses items, when deciding between slide-over navigation and inline expansion, when a static comp specifies two screens but nothing about how one becomes the other, or when an interface "feels jarring" or "like a glitch" without an obvious cause. Structural decisions only — hand easing curves and durations to `animate`.
---

# Transitional Interfaces

An architecture skill. It does ONE thing: decide what happens *between* two states, when that decision changes the structure of the interface rather than its polish. It does not pick easing curves or durations (that's `animate`), hunt a codebase for animation opportunities (that's `find-animation-opportunities`), review a motion diff (that's `review-animations`), or name an effect (that's `animation-vocabulary`).

It runs upstream of all of them. By the time you're choosing a curve, this skill's decision is already made — usually by default, usually badly.

Based on Pasquale D'Silva's [Transitional Interfaces](https://medium.com/@pasql/transitional-interfaces-926eb80d64e3) (April 2013). See § Where the 2013 argument needs updating.

## The claim

A static comp specifies states. It says nothing about the connection between them, so the connection gets built by default — and the default is a cut. One state is replaced by another in a single frame.

Nothing in the physical world behaves that way. A cut between related states reads as a glitch, because the user's spatial model of the interface is broken and silently rebuilt. D'Silva's framing: animation "leverages an overlooked dimension — time! An invisible fabric which stitches space together."

The consequence that matters: **a transition is not decoration applied to a state change. It is the only channel that carries the relationship between the two states.** If the transition is a cut, the relationship is unstated, and the user reconstructs it from memory and navigation chrome instead.

This is why the skill is structural. Deciding the transition sometimes changes what the screens *are*.

## The one question

Before anything else, name the relationship between the outgoing and incoming state. Everything follows from this, and it has only a few answers:

| Relationship | What the transition must carry | Default that fails it |
|---|---|---|
| **Same object, more detail** | This is the thing you touched, opened up | Slide to a new screen — the object appears to be replaced by a different object |
| **Container and its contents** | You went inside this, and here's where "inside" is | Cross-fade — no containment, no exit path |
| **Peers in a set** (next photo, next tab) | Lateral movement, position within the set | Fade — loses the axis and the sense of how many remain |
| **New object entering a set** | Where it came from, and the set making room | Instant insert — items below jump, nothing explains why |
| **Genuinely unrelated views** | Nothing. A cut is correct | An elaborate transition inventing a relationship that isn't there |

The last row is the one people skip. If two states have no relationship, animating between them fabricates one, and the user spends attention decoding a connection that doesn't exist. Restraint here is the same rule `find-animation-opportunities` enforces; this skill just gets there earlier.

## Insertion into a set: two beats, not one

The article's clearest recipe, and it generalizes. When an item joins a list:

1. **The set makes room.** Existing items move apart to open a gap.
2. **The item fills the space it made.**

Two beats, slightly overlapped, not one simultaneous blur. D'Silva's reason: "the list needs to make room for the item, and then the new item (which came from somewhere) fills in the space… we have the contextual hook of space — mirroring the way you'd add something to a stack of things in real life."

Removal runs it backwards: the item leaves, then the set closes the gap. If those happen at once, the eye can't tell whether the item was removed or the list re-sorted.

The generalization: **any change to a set's membership is two events — the set changing shape, and the member arriving or leaving.** Collapse them into one and you've thrown away the half that explains the other.

## The drill-down decision

This is the part of the article with real teeth, and it's a layout decision disguised as a motion one.

The default for "show me more about this item" is a horizontal slide to a new screen. D'Silva's objection: "The direction of sliding doesn't really give you any useful clues outside of a linear chain of views." The item you touched is gone, replaced by a screen about it. Sliding tells you only that you went one step deeper on an axis with no visible extent.

The alternative: **treat the item as a container you prod for more detail, in place.** The item expands where it sits; if it needs the whole screen, the rest of the list recedes within the same view rather than being swapped out.

Choose inline expansion when the detail is *about* the item and the user's next action is likely to be returning to the set or moving to a sibling. Choose a new screen when the detail is genuinely a different place — a different task, a different object, or something a user could arrive at by other routes.

The payoff D'Silva names: "you can remove the need to explain how deep a user is embedded into sub-views. You can scrap the display of a hierarchical navigation, because the user saw how they got there." Breadcrumbs, back-button chains, and "‹ Back to Settings" labels are all compensation for a transition that failed to show containment. Fix the transition and the chrome becomes redundant.

## Where continuity cannot carry the whole load

This is the article's weakest claim and it needs a guard. "The user saw how they got there" is only true for a user who *was there and watched*. It fails for:

- **Deep links and restored sessions.** The user arrives inside the expanded state having seen no transition. If the only exit affordance was the animation, there is now no exit.
- **Reduced motion.** Under `prefers-reduced-motion` the transition is reduced to a cut or a fade, taking the spatial information with it.
- **Returning after time away.** Continuity is working memory, and working memory expires. It does not survive a coffee break the way a visible label does.
- **Anyone who looked away** during the 300ms that carried the meaning.

So: let continuity replace *redundant* chrome, never *load-bearing* chrome. The test is whether the state is still escapable and legible in a screenshot of its resting state, with no motion history. If it isn't, keep an explicit affordance and let the transition reinforce it instead of replacing it.

## What this skill does not decide

Once the relationship and the structure are settled, hand off:

- Curve, duration, spring constants → `animate`, with values from `motion-values.md` (`/Users/Commons/Developer/Personal/design-brain/topics/motion-values.md`).
- Native equivalents → `apple-native-motion`.
- Whether the animation is well built → `review-animations`.

Do not specify milliseconds here. A structural decision expressed in exact timings gets argued about on the timings.

## Where the 2013 argument needs updating

The essay predates most of what constrains motion now. Read it with these corrections:

- **`prefers-reduced-motion` did not exist.** Every structural decision above needs a reduced-motion answer, and "the transition explains the hierarchy" needs a static fallback that explains it too.
- **Speed expectations moved.** 2013-era demos are slow by current standards. The structure of a transition transfers; its pacing does not.
- **"Delight" was the enemy then; sluggishness is the enemy now.** D'Silva was arguing against static interfaces to an audience that shipped cuts. The current failure mode is the opposite — motion everywhere, none of it informative. His functional test still sorts both: does this carry information, or is it embellishment?
- **His exemplars are period references.** Clear, Willcall, and Facebook.app as they existed in 2013. Cite the patterns, not the apps; don't claim any of them still behaves this way without checking.
