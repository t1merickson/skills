---
name: transitional-interfaces
description: Design the connection between two interface states, not the states themselves — deciding what relationship a transition has to carry, whether continuity can replace navigation chrome, and what the transition does when the data isn't there yet. Use when a flow moves between views, when a list gains or loses items, when choosing between pushing a screen, expanding inline, and presenting a sheet, when a static comp specifies two screens but nothing about how one becomes the other, or when an interface "feels jarring" or "like a glitch" without an obvious cause. Structural decisions only — hand easing curves and durations to `animate`.
---

# Transitional Interfaces

An architecture skill. It does ONE thing: decide what happens *between* two states, when that decision changes the structure of the interface rather than its polish. It does not pick easing curves or durations (that's `animate`), hunt a codebase for animation opportunities (that's `find-animation-opportunities`), review a motion diff (that's `review-animations`), or name an effect (that's `animation-vocabulary`).

It runs upstream of all of them. By the time you're choosing a curve, this skill's decision is already made — usually by default, usually badly.

One skill sits above it: `spatial-interfaces` models the whole space an interface occupies. This skill designs a single edge on that map. If you can't name where the two states live relative to each other, the model is missing and that's the thing to fix first.

## The claim

A static comp specifies states. It says nothing about the connection between them, so the connection gets built by default, and the default is a cut: one state replaced by another in a single frame.

Almost nothing outside a screen behaves that way. A cut between *related* states reads as a glitch, because the user's spatial model of the interface breaks and gets silently rebuilt. Time is the dimension a comp can't show, and it's the one that says how two states are related.

The consequence that matters: **a transition is not decoration applied to a state change. It is the only channel that carries the relationship between the two states.** Cut the transition and the relationship goes unstated, leaving the user to reconstruct it from memory and navigation chrome.

That's why this is structural rather than cosmetic. Deciding the transition sometimes changes what the screens *are*.

## The one question

Before anything else, name the relationship between the outgoing and incoming state. Everything follows from it, and there are only a handful of answers. The named patterns are Material's motion taxonomy, which is the most widely implemented vocabulary for this and worth using so the decision survives being handed to someone else.

| Relationship | What the transition must carry | Named pattern | Default that fails it |
|---|---|---|---|
| **Same object, more detail** | Identity held across the change — this is the thing you touched | Container transform | Cut or push; the object reads as replaced by a different one |
| **Container and its contents** | You went inside this, and here's where inside is | Container transform | Cross-fade — no containment, no exit path |
| **Peers in a set** (next photo, sibling tab) | Lateral position on an axis, and that the axis has extent | Shared axis | Fade — loses direction and any sense of how much remains |
| **Member joining or leaving a set** | Where it came from, and the set making room | Two-beat insert (below) | Instant insert; rows jump and nothing explains why |
| **Peer views with no spatial relation** | A change of context, with no false continuity implied | Fade through | A shared-element transition, which fabricates an identity that isn't there |
| **Genuinely unrelated** | Nothing. A cut is correct | — | An elaborate transition inventing a relationship |

The last two rows are the ones people skip. Motion that asserts a relationship the interface doesn't have is worse than a cut, because the user spends attention decoding a connection that doesn't exist. The restraint rule here is the same one `find-animation-opportunities` enforces; this skill just reaches it earlier.

## Membership changes are two beats, not one

When an item joins a set:

1. **The set makes room.** Existing items move apart to open a gap.
2. **The item fills the space that was made for it.**

Two beats, slightly overlapped — not one simultaneous blur. The gap is what explains the arrival: the set visibly accommodates something, and then the something is there. It matches how adding to a physical stack works, which is why it needs no explanation.

Removal runs backwards: the item leaves, then the set closes. Run those together and the eye can't distinguish a removal from a re-sort.

The generalization: **any change to a set's membership is two events — the set changing shape, and the member arriving or leaving.** Collapse them into one and you discard the half that explains the other.

## Choosing how to go deeper

Three structures, and the choice is a layout decision wearing motion's clothes.

**Push to another screen.** Correct when the destination is genuinely a different place — a different task, a different object, or somewhere reachable by other routes. The old objection was that a horizontal slide tells you nothing except that you went one step along an axis with no visible extent. That objection is now only half true: shared-element transitions mean a push can carry the object with it, so "new screen" no longer has to mean "the thing you touched disappeared." If you push, push *with* the object.

**Expand in place.** Correct when the detail is *about* the item and the likely next action is returning to the set or moving to a sibling. The item becomes a container you open where it sits; if it needs the full screen, the rest of the set recedes within the same view rather than being swapped out. This is the structure that most often removes chrome, because containment is shown rather than described.

**Present a sheet over the origin.** Correct for a task concerning the item where the set should stay visible and the dismissal should be obvious and cheap. The origin visible behind the sheet does the same work as inline expansion's containment cue, without restructuring the underlying view. Detents make this a range rather than a binary, which is often the honest answer when "how much detail" depends on the item.

The payoff of the second and third: you can drop the machinery that explains how deep a user is buried. Breadcrumb trails, back-chains, and "‹ Back to Settings" labels are compensation for a transition that failed to show containment. Show it and the chrome becomes redundant — subject to the limit below.

## Where continuity cannot carry the load

"The user saw how they got there" is only true of a user who was there and watched. It fails for:

- **Deep links and restored sessions.** They arrive inside the expanded state having seen no transition. If the only exit affordance was the animation, there is now no exit.
- **Reduced motion.** Under `prefers-reduced-motion: reduce` the transition collapses to a cut or a cross-fade, taking the spatial information with it.
- **Time away.** Continuity is working memory, and working memory expires. It does not survive a lunch break the way a visible label does.
- **Anyone who looked away** during the 300ms carrying the meaning.

So let continuity replace *redundant* chrome, never *necessary* chrome. The test: is the state still escapable and legible in a screenshot of its resting frame, with no motion history? If not, keep an explicit affordance and let the transition reinforce it instead of replacing it.

Reduced motion deserves the same care as a structural decision, not a suppression at the end. Reduce the *motion*, keep the *meaning*: hold the containment cue statically — the expanded item still visually nested inside the set — and cross-fade rather than translate. Opacity is generally tolerated where large transforms are not.

## When the data isn't there yet

The two-beat insert above assumes the item exists. Often it doesn't yet — the row is optimistic and the write is still in flight.

- **Never gate a transition on a network round trip.** A 200ms motion that waits for a fetch is a 900ms stall, and it converts your nicest transition into your slowest interaction. Animate optimistically and reconcile after.
- **A failed write cannot be undone with the removal animation.** Playing the insert backwards reads as *the user removed it*. Failure needs its own treatment — the row staying put and marking itself failed, with a retry — or the user learns their action silently didn't happen.
- **Don't animate speculative content into a position it may not keep.** If the server decides sort order, either insert where it will land or don't animate placement at all. An item that slides into place and then jumps elsewhere is worse than one that simply appears.
- **Skeletons are a transition too.** A skeleton that doesn't match the shape of what replaces it produces a second, unplanned transition at the moment of load.

## The tools are no longer the excuse

The historical reason interfaces shipped cuts was that continuity was hard to build. It isn't anymore, and a proposal to cut should no longer be defended on implementation cost.

- **View Transitions API** — `document.startViewTransition()` with `view-transition-name` gives shared-element transitions natively. Same-document support is broad (Chrome 111+, Firefox 133+, Safari 18+). Cross-document is Chromium and Safari 18.2+ with Firefox still in progress, so treat MPA transitions as progressive enhancement, not a guarantee.
- **FLIP** — First/Last/Invert/Play, the technique underneath most layout animation. Still the fallback where View Transitions aren't available, and still worth understanding, since it's what the API automates.
- **Shared layout in animation libraries** — a `layoutId`-style shared identifier across two components animates the change automatically; this is the cheapest path to inline expansion in a component framework.
- **`matchedGeometryEffect`** on SwiftUI, and container transform on Android, for the native equivalents.
- **`@starting-style` and `transition-behavior: allow-discrete`** close the old gap where elements entering and leaving the DOM (including popovers and dialogs in the top layer) couldn't be animated without JavaScript.

## What this skill does not decide

Once relationship and structure are settled, hand off:

- Curve, duration, spring constants → `animate`, with values from `motion-values.md` (`/Users/Commons/Developer/Personal/design-brain/topics/motion-values.md`).
- Native equivalents → `apple-native-motion`.
- Whether the animation is well built → `review-animations`.
- The overall model these states live in, and whether the product can afford another navigation axis → `spatial-interfaces`.

Do not specify milliseconds here. A structural decision expressed in exact timings gets argued about on the timings.

## The current failure mode

The old argument for motion was made to people shipping static interfaces, and it won. The failure now runs the other way: motion everywhere, most of it carrying no information, each piece defensible alone and exhausting in aggregate.

The functional test sorts both cases. Does this transition state a relationship that is actually true of these two states? If yes, it's structure. If it's there to look considered, it's embellishment, and embellishment on the critical path has a measurable cost — responsiveness is a tracked metric now, and a transition that delays the response to an input is a regression whatever it looks like.

Two states with nothing between them is a bug. Two states with a story between them that isn't true is a worse one.
