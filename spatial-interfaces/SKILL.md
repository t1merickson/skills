---
name: spatial-interfaces
description: Model where interface contexts live, how people enter and leave them, and how much navigation complexity a product can afford. Use for information architecture, confusing navigation, or cross-size structural audits.
---

# Spatial interfaces

This skill draws the product map. `transitional-interfaces` designs one connection on that map. Do not use this skill to pick animation curves or polish a single screen.

## Draw the map

Represent every meaningful context, its parent or peers, routes in, routes out, and persistent anchors. An indented outline is enough when a diagram would add ceremony. Mark hubs, dead ends, duplicate destinations, hidden regions, and contexts whose only purpose is forwarding elsewhere.

Run the sketch test: can a teammate redraw the rough product structure from memory and explain how to get home? If not, extra labels may be treating a structural problem as copy.

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

Treat these as a budget. Name what a new dimension replaces or why it earns its cost. Flag nested modals, carousels inside same-axis scrolling, drawers that imply false peer relationships, and states whose only exit is browser- or gesture-history.

## Test arbitrary entry

Deep links, notifications, search, restoration, keyboard commands, VoiceOver traversal, and automation can enter without showing the route. For every context ask:

- Can a still frame say where this is and what it belongs to?
- Is there an outward route besides a historical Back action?
- Does focus land somewhere meaningful?
- Does the structure remain legible without motion, hover, or spatial vision?

Continuity may remove redundant chrome, never necessary orientation or escape.

## Re-budget at each size

A visible desktop sidebar may become a modal drawer on a phone; that changes the model, not just the layout. Draw the smallest supported size and input mode first, then compare larger forms. Check keyboard, pointer, touch, switch, and screen-reader routes where the product supports them.

Motion may imply where things live, but it should not make people watch the whole journey. Keep direction consistent with the map and let resting states remain self-explanatory. Use `transitional-interfaces` for a specific edge.

## Output

Produce:

1. the bird's-eye map;
2. the dimensional budget by device and breakpoint;
3. axis collisions, false peers, dead ends, and return-path failures;
4. arbitrary-entry and assistive-navigation failures;
5. ranked structural changes, with affected routes and tradeoffs.

Rank by user frequency and recovery cost, not theoretical impurity.
