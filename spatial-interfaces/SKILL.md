---
name: spatial-interfaces
description: Design the whole model an interface occupies — where things live, how contexts connect, and how much dimensional complexity a product can afford — rather than one screen or one transition. Use when navigation feels confusing without a single screen being at fault, when adding a drawer, carousel, modal, or tab bar to something that already has several, when users get lost or can't find their way back, when planning information architecture for an app, when auditing an existing product's structure, or when a layout must adapt across sizes. Produces maps and structural decisions — hand individual state changes to `transitional-interfaces` and timing to `animate`.
---

# Spatial Interfaces

An architecture skill. It does ONE thing: model the space an interface occupies and decide where things live in it. It does not design the connection between two specific states (that's `transitional-interfaces`), pick curves or durations (that's `animate`), or review a motion diff (that's `review-animations`).

The relationship to `transitional-interfaces` is exact: **this skill draws the map, that one designs a single edge on it.** Doing the edge without the map is how products end up with individually reasonable screens and no navigable whole.

## The claim

People reason spatially without effort. You can find a light switch in the dark, know which pocket your phone is in, and remember which side of the kitchen the glasses are on — all without deliberate thought, because the brain keeps physical models cheaply and queries them fast.

Software that maps onto a spatial model borrows that machinery. Software that doesn't forces the user to hold an arbitrary graph in working memory instead, which is expensive and fails under load. The difference shows up as "I can't find it" and "how do I get back," which get misdiagnosed as labeling or discoverability problems and treated with more chrome.

**The goal is an interface a user could sketch from memory.** Not accurately — roughly, the way anyone can sketch the floor plan of a house they've spent a day in.

## Draw the map first

The failure this prevents: designing screens as a flat row of comps, deciding navigation afterward, and discovering the structure only once it's built.

Before laying out screens, draw the model — on paper, a whiteboard, anything looser than pixels. It is not a screen layout. It's a bird's-eye view of contexts and the connections between them, and it deliberately extends past the edges of the screen, because most of the model is off-screen at any moment. Off-screen position is still position: a thing that slides in from the left lives to the left, and it should still live there an hour later.

The map should show, for every context: where it sits relative to its neighbors, what routes reach it, and what routes leave. If a context has one route in and one route out, it's a corridor and probably shouldn't be its own context. If it has seven, it's a hub and needs to look like one.

### The sketch test

The diagnostic, and it's brutally effective: **try to draw the whole product as one bird's-eye diagram, from memory.** Anyone on the team, not just the person who built it.

If you get lost drawing it, users are lost using it. Products that fail this test share a signature — carousels inside modals inside list views inside drawers, each reasonable in isolation. Nobody decided to build a maze; each addition was a local decision that never got checked against the whole.

Run the test when structure changes, not just at the end. It costs ten minutes.

## The dimensional budget

Every navigation device introduces an axis the user has to model. They are not free and they are not additive in cost — they multiply, because the user must track their position on all of them at once.

| Device | Axis it adds |
|---|---|
| Nav stack / push | Depth along one horizontal line |
| Tab bar | Lateral position among peers |
| Carousel | A second lateral axis, usually with no visible extent |
| Modal / sheet | Depth on z, plus a suspended state to return from |
| Drawer / hamburger | An off-screen region on one edge |
| Zoom / contextual scale | Scale as a dimension, with a return-to-scale problem |
| Scroll region inside another scroll region | An axis that collides with its parent |

Two or three of these is a legible product. Five or six, freely combined, is the maze. **Treat them as a budget rather than a menu**: when adding one, name the one it replaces, or justify why this product can afford another.

The specific combinations that reliably hurt: a carousel inside a scroll view (axis collision — neither gesture is predictable), a modal launched from a modal (no coherent return path), and a drawer whose items each lead somewhere structurally different (the drawer implies peers; the destinations aren't).

## Motion states where things are

Once the map exists, motion is how it gets taught. A thing that enters from a place and exits to a place has an address; a thing that fades in from nowhere doesn't.

This makes **exit direction a design decision, not a leftover.** Where an item goes when it leaves says what happened to it and whether it can come back:

- Sliding off and stopping just short of the edge implies a holding area — that the item still exists somewhere and could be brought back. If the product has an undo, an archive, or a trash, this is the honest exit.
- Accelerating away without slowing implies gone for good. It's the right choice only for genuine destruction, and using it for a recoverable action is a lie the interface tells.
- Falling, folding, or draining in place implies consumed or resolved rather than relocated.

Pick the one that matches what actually happened to the data. This is the cheapest place to fix "where did it go?" complaints, and it's usually free.

## Imply space; don't make people travel through it

The trap on the other side: an interface so committed to spatial literalism that it makes the user watch the journey.

Space can be implied with a fraction of the distance. A view that displaces a short way while the incoming view arrives reads as lateral movement just as clearly as a full-width slide, and takes a fraction of the time. The eye needs enough of the movement to infer direction, not the whole trip.

The reason to care is responsiveness, not elegance. Time spent describing space is time the interface isn't responding, and thoroughly-explained space is a product that feels slow. **Literal is not the goal; legible is.** When they conflict, cut the distance and keep the direction.

Related: prefer to keep motion on axes already in the model. A flow that moves along one axis and then abruptly introduces a second one for a sub-step makes the user extend their model for a single screen. Continuing on the existing axis is usually both simpler to build and easier to hold.

## The economy of attention

Motion is what the eye tracks, so every animated element is a claim on attention, and the claims compete.

The cost isn't measured in milliseconds, it's measured in eye movements. Each element that moves independently is another thing to follow; each is another small physical and mental commitment. A screen where six things animate on entry has spent six units of attention to deliver one state change.

Practical consequences:

- **Lead the eye, don't catch it.** Motion should point at where the user's attention needs to go next. Motion that merely draws notice to itself is a tax with no return.
- **Animate the state change, not the decorations on it.** An icon flipping through a morph while the view behind it is also transitioning splits attention between a large meaningful change and a small meaningless one. The small one usually wins, which is the wrong outcome.
- **Excess oscillation is attention theft.** A spring that wobbles several times holds the eye hostage waiting for it to settle. Intent reads as one considered overshoot; more than that reads as an unresolved question.
- **The best motion here is close to invisible.** If people describe an interface as feeling good rather than looking animated, that's the target. Motion the user *notices* in product UI is usually a defect, however well made.

## Structure that survives arbitrary entry

The historical version of this argument assumed users walk the map from the entrance. They don't:

- **Deep links and notifications teleport people into the middle.** Any context reachable by URL, notification, or share sheet must be legible with no arrival path — it needs to say where it is and offer a way outward that isn't just "back."
- **Search bypasses the map entirely.** Every product has it, and it's frequently the primary navigation. This doesn't make the model less important — the destination still has to make sense on arrival — but it does mean the map cannot be the *only* way to reach anything.
- **Restored sessions resume mid-model.** If the state is only comprehensible given the transition that created it, a cold launch into it is a dead end.

The test: take a screenshot of any context, hand it to someone, and ask where they are and how they'd get out. If the answer depends on having watched the journey, the context needs an explicit anchor.

## The model changes shape across sizes

Responsive layout is not just reflow — it changes the dimensional budget. A sidebar visible alongside content costs zero navigation dimensions. The same sidebar as a drawer on a small screen costs one, plus a mode to be in and get out of.

So the small-size layout is usually the one that's structurally expensive, and it's the one to model first. Check the budget at every breakpoint rather than only at the size the design was made in. A product that's legible on a desktop and a maze on a phone has usually never had its map drawn at phone size.

## Where formulas end

Published motion specifications and standardized easing sets are useful defaults and a good way to keep a team consistent. They are not verdicts. A value that measures correctly and feels wrong is wrong, and the eye is the instrument of record.

Use house values (`motion-values.md` at `/Users/Commons/Developer/Personal/design-brain/topics/motion-values.md`) as the starting position and the tie-breaker, and depart from them deliberately when a specific transition needs it — noting why, so the departure reads as a decision rather than drift.

## What this skill does not decide

- A single state-to-state connection → `transitional-interfaces`.
- Curves, durations, spring constants → `animate`.
- Native equivalents → `apple-native-motion`.
- Whether motion code is well built → `review-animations`.

## Output

When run as an audit, produce: the bird's-eye map (as a diagram or an indented outline if drawing isn't available), the dimensional budget with each device named and counted, the specific combinations creating axis collisions or return-path problems, and the contexts that fail the arbitrary-entry test. Rank by how many users hit each one, not by how offensive it is structurally.
