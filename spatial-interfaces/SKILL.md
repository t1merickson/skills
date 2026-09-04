---
name: spatial-interfaces
description: "Map interface contexts, entry and exit routes, hierarchy, and navigation complexity when the user requests information architecture work or a product has confusing destinations, arbitrary-entry failures, or structural changes across sizes. Do not use for single-screen layout, visual styling, animation tuning, or adding a straightforward route whose place is already clear."
---

# Spatial interfaces

This skill draws the product map. `transitional-interfaces` designs one connection on that map. Designing the edge without the map is how products acquire individually reasonable screens and no navigable whole. Do not use this skill to pick animation curves or polish a single screen.

The claim is simple: interface structure becomes learnable when places and directions stay coherent enough to form spatial memory. The goal is not a literal simulated building. It is a product a teammate or returning user could sketch roughly from memory.

## Draw the map

Represent every meaningful context, its parent or peers, routes in, routes out, and persistent anchors. An indented outline is enough when a diagram would add ceremony. Mark hubs, dead ends, duplicate destinations, hidden regions, and contexts whose only purpose is forwarding elsewhere.

Run the sketch test: hide the comps and ask a teammate to redraw the whole product as one bird's-eye diagram from memory, then explain how to get home. If they draw a list of screens rather than a structure, or cannot place a context without recounting the path they took, extra labels may be treating a structural problem as copy.

## Count navigation dimensions

Each device adds state the user must track:

| Device | Added state |
|---|---|
| push/navigation stack | depth and return path |
| tabs | lateral peer position |
| carousel | another lateral axis and extent |
| sheet/modal | suspended origin plus dismissal |
| drawer | hidden edge region and open/closed mode |
| zoom/context scale | current scale plus escape route |
| nested scroll | competing gesture ownership |

Treat these as a budget rather than a menu. Two or three coherent dimensions can be legible; five or six freely combined become a maze. Name what a new dimension replaces or why it earns its cost. Flag nested modals, carousels inside same-axis scrolling, drawers that imply false peer relationships, and states whose only exit is browser- or gesture-history.

## Test arbitrary entry

Deep links, notifications, search, restoration, keyboard commands, VoiceOver traversal, and automation can enter without showing the route. For every context ask:

- Can a still frame say where this is and what it belongs to?
- Is there an outward route besides a historical Back action?
- Does focus land somewhere meaningful?
- Does the structure remain legible without motion, hover, or spatial vision?

Continuity may remove redundant chrome, never necessary orientation or escape.

## Re-budget at each size

A visible desktop sidebar may become a modal drawer on a phone; that changes the model, not just the layout. Draw the smallest supported size and input mode first, then compare larger forms. Check keyboard, pointer, touch, switch, and screen-reader routes where the product supports them.

Motion may imply where things live, but it should not make people watch the whole journey. Literal is not the goal; legible is. Keep direction consistent with the map, compress travel aggressively, and let resting states remain self-explanatory.

Budget attention as well as dimensions. Every independently moving element asks for another eye movement. Animate the state change, not a chorus of decorations around it; motion should lead attention to what matters next, not catch it for its own sake. Use `transitional-interfaces` for a specific edge.

## Output

Produce:

1. the bird's-eye map;
2. the dimensional budget by device and breakpoint;
3. axis collisions, false peers, dead ends, and return-path failures;
4. arbitrary-entry and assistive-navigation failures;
5. ranked structural changes, with affected routes and tradeoffs.

Rank by user frequency and recovery cost, not theoretical impurity.
