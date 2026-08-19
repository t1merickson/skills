---
name: apple-native-motion
description: Apple's fluid-motion physics as actual SwiftUI code — springs, gesture handoff, interruption, reduced motion — for iOS and macOS apps. Use when adding or reviewing motion in a SwiftUI (or UIKit) project. The web skills (apple-design, animate, improve-animations, review-animations) carry the same doctrine in CSS/JS; this is the native translation.
---

# Apple Native Motion

The `apple-design` skill holds the doctrine (response, momentum, interruptibility, restraint) with web code. This skill is the same physics in Swift. Read `apple-design` for the *why*; take the code from here.

## What earns motion (unchanged from the doctrine)

The frequency gate applies exactly as on the web, and stricter on macOS:

- Keyboard-initiated or 100+/day actions: no animation.
- Tens/day: reduced motion — small, fast, opacity-first.
- Occasional: standard springs.
- Rare or first-run: delight is allowed.
- macOS baseline: rarer and smaller than iOS. Desktop users live in the app all day.

When unsure whether a moment earns motion at all, run it through `find-animation-opportunities`' four-question gate (frequency, purpose, speed, function) — the gate is platform-agnostic even though that skill's recipes are CSS.

## Springs are the default

Never `.linear` or `.easeInOut` for interactive UI. SwiftUI springs are interruptible and velocity-preserving by default — the two properties the whole doctrine is built on. You get retargeting for free; don't defeat it.

```swift
// Preferred modern form (iOS 17+/macOS 14+): duration + bounce
.animation(.spring(duration: 0.35, bounce: 0.15), value: isExpanded)

// Built-in presets, in order of how often you should reach for them:
.smooth   // no bounce — default for most UI
.snappy   // small bounce — buttons, toggles, small elements
.bouncy   // visible bounce — playful, rare/delight moments only

// Older form when targeting earlier OS versions:
.animation(.spring(response: 0.35, dampingFraction: 0.85), value: isExpanded)
```

Translation table from the web doctrine's spring vocabulary:

| Doctrine says | SwiftUI |
| --- | --- |
| Critically damped, no overshoot | `.smooth`, or `bounce: 0` / `dampingFraction: 1.0` |
| Slight overshoot for physicality | `.snappy`, or `bounce: 0.15` / `dampingFraction: 0.8–0.85` |
| Playful bounce (rare moments) | `.bouncy`, or `bounce: 0.3` / `dampingFraction: 0.6–0.7` |
| "Sub-300ms UI" duration budget | `duration:`/`response:` 0.2–0.35 for UI elements; sheets and full-screen moves up to ~0.5 |

## Press feedback

Respond on touch-down, never on release. The doctrine's press values (scale ~0.97, fast in) translate directly:

```swift
.scaleEffect(isPressed ? 0.97 : 1)
.animation(.snappy(duration: 0.16), value: isPressed)
```

Use a `ButtonStyle` with `configuration.isPressed` so it's down-state, not tap-completion. Add haptics (`.sensoryFeedback` on iOS) for state changes that deserve weight; never on macOS unless it's a Force Touch trackpad idiom.

## Gestures: 1:1 tracking, then velocity handoff

During a drag, the view tracks the finger exactly — no animation while the gesture is live. On release, project momentum and hand the gesture's velocity to the spring:

```swift
.gesture(
    DragGesture()
        .onChanged { value in
            offset = value.translation          // 1:1, no animation
        }
        .onEnded { value in
            let projected = value.predictedEndTranslation  // momentum projection
            let target = nearestDetent(to: projected)
            withAnimation(.spring(duration: 0.4, bounce: 0.1)) {
                offset = target                  // spring inherits velocity automatically
            }
        }
)
```

Decide the destination from `predictedEndTranslation` (where the throw was headed), not the raw position. Small flick, big intent.

Rubber-band resistance at boundaries: divide the overshoot, don't clamp it.

```swift
let overshoot = value.translation.height - limit
offset = limit + overshoot / 3
```

## Interruption

Never gate a gesture on an animation finishing. SwiftUI retargets springs mid-flight when the animated value changes — the standard failure is *defeating* that with `isAnimating` flags, `DispatchQueue.asyncAfter` chains, or `Task.sleep` sequencing. If you find completion-blocking, that's the bug. For multi-stage motion use `PhaseAnimator` or `KeyframeAnimator`, which remain interruptible.

## Reduced motion

Honor it always. Replace movement/scale with opacity; keep the state change.

```swift
@Environment(\.accessibilityReduceMotion) private var reduceMotion

.animation(reduceMotion ? .easeOut(duration: 0.1) : .spring(duration: 0.35), value: state)
// For entrances: swap slide/scale transitions for .opacity when reduceMotion is true.
```

## UIKit/AppKit carve-out

When a view lives in UIKit (per `ios-design`'s carve-outs), use `UIViewPropertyAnimator` — it is the interruptible, scrubbable primitive — with `UISpringTimingParameters(dampingRatio:initialVelocity:)`. Convert gesture velocity to the unit-relative `initialVelocity` the API expects. Never `UIView.animate(withDuration:)` for anything a finger can interrupt.

## Before calling motion done

- Every spring interruptible: mid-animation input retargets, nothing queues or blocks.
- Gestures track 1:1 while live; release uses predicted end, not raw position.
- Press feedback on down, not up.
- Reduce Motion produces a working, calmer app — verify in Settings/System Settings, not just by reading the code.
- Nothing keyboard-initiated animates.
- macOS: motion is rarer and smaller than the iOS equivalent would be.
