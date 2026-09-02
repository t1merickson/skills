---
name: apple-native-motion
description: Apple's fluid-motion physics as SwiftUI and UIKit code — springs, gesture handoff, interruption, and reduced motion. Use when adding or reviewing motion in a native iOS or macOS project.
---

# Apple Native Motion

Use four principles throughout: immediate response, momentum that follows the gesture, interruption at any point, and restraint proportional to frequency. This skill turns those principles into Swift.

## What earns motion

The frequency gate applies exactly as on the web, and stricter on macOS:

- Keyboard-initiated or 100+/day actions: no animation.
- Tens/day: reduced motion — small, fast, opacity-first.
- Occasional: standard springs.
- Rare or first-run: delight is allowed.
- macOS baseline: rarer and smaller than iOS. Desktop users live in the app all day.

When unsure whether a moment earns motion at all, ask four questions: how often it occurs, what meaning the motion carries, whether it delays response, and whether the interaction still works without it. If the motion has no functional answer, leave it out.

## Springs are the default for direct manipulation

For controls that can be interrupted or retargeted, prefer a spring over a fixed easing curve. Linear and ease-in-out animation remain appropriate for indeterminate progress, opacity changes, and other non-physical effects. SwiftUI springs preserve continuity when their target changes; do not defeat that with a completion gate.

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

## Gestures: 1:1 tracking, then momentum-aware settling

During a drag, the view tracks the finger exactly — no animation while the gesture is live. On release, let the projected endpoint influence the destination:

```swift
.gesture(
    DragGesture()
        .onChanged { value in
            offset = value.translation          // 1:1, no animation
        }
        .onEnded { value in
            let projected = value.predictedEndTranslation  // destination estimate
            let target = nearestDetent(to: projected)
            withAnimation(.spring(duration: 0.4, bounce: 0.1)) {
                offset = target
            }
        }
)
```

Use `predictedEndTranslation` to choose the destination when momentum should affect intent. It is a projected endpoint, not a reusable velocity value. If the animation API accepts initial velocity, derive and normalize velocity for that API explicitly; otherwise test the release and interruption rather than claiming automatic gesture-velocity transfer.

Rubber-band resistance at boundaries: divide the overshoot, don't clamp it.

```swift
let overshoot = value.translation.height - limit
offset = limit + overshoot / 3
```

## Interruption

Never gate a gesture on an animation finishing. SwiftUI retargets springs mid-flight when the animated value changes — the standard failure is *defeating* that with `isAnimating` flags, `DispatchQueue.asyncAfter` chains, or `Task.sleep` sequencing. For multi-stage motion, verify interruption explicitly; a phase or keyframe sequence is not automatically appropriate for direct manipulation.

## Reduced motion

Honor it always. Replace movement/scale with opacity; keep the state change.

```swift
@Environment(\.accessibilityReduceMotion) private var reduceMotion
@Environment(\.accessibilityPrefersCrossFadeTransitions) private var prefersCrossFade

.animation(reduceMotion || prefersCrossFade ? .easeOut(duration: 0.1) : .spring(duration: 0.35), value: state)
// For entrances: swap slide/scale transitions for .opacity when reduceMotion is true.
```

## UIKit and AppKit

In UIKit, use `UIViewPropertyAnimator` with `UISpringTimingParameters(dampingRatio:initialVelocity:)` for interruptible motion. Convert gesture velocity to the unit-relative value the API expects. Fixed `UIView.animate` calls are fine for non-interactive opacity and housekeeping effects, not for motion a finger can retarget.

In AppKit, use `NSAnimationContext` for brief non-interactive property changes. During direct manipulation, update the property without animation, then animate to the chosen resting state using a model that supports cancellation and retargeting. AppKit has no drop-in equivalent of `UIViewPropertyAnimator`; test interruption in the actual control rather than assuming it.

## Before calling motion done

- Every spring interruptible: mid-animation input retargets, nothing queues or blocks.
- Gestures track 1:1 while live; release uses predicted end when momentum is part of the interaction.
- Press feedback on down, not up.
- Reduce Motion produces a working, calmer app — verify in Settings/System Settings, not just by reading the code.
- Frequent keyboard actions do not acquire decorative motion or input delay.
- macOS: motion is rarer and smaller than the iOS equivalent would be.
