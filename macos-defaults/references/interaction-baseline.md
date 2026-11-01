# macOS interaction baseline

Read this when implementing or auditing launch and restoration, long-running work, failure and recovery, localization, onboarding, or help. It is a decision guide, not a frozen specification. Recheck the current Human Interface Guidelines and the deployed SDK when exact APIs or platform behavior matter. Last reviewed 2026-09-03.

## Launch and restoration

- Show a useful window and meaningful content as quickly as the work permits. macOS does not need a launch screen, and an artificial branding delay makes a fast app feel slow.
- Restore the last valid working state at the granularity the app actually owns: open windows, document or navigation selection, sidebar and inspector visibility, scroll position, and unfinished work where preservation is safe.
- Treat restoration data as a hint, not an invariant. If a file, account, display, permission, or saved frame is no longer valid, recover to the closest useful state instead of reproducing an unusable window or failing launch.
- Avoid startup alerts. When launch discovers a recoverable problem, open the app and explain it near the affected content with a concrete next action.
- A menu-bar utility still needs a clear first useful state, Settings route, quit path, relaunch behavior, and a way to recover if its status item is hidden or unavailable.

Current source: [Launching — Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/launching/).

## Responsiveness and progress

- Put something truthful on screen immediately: loaded content, a stable skeleton or placeholder, or the portion already available. Do not make the whole interface wait for work that affects only one region.
- Keep unrelated navigation, reading, editing, and window management available during long work. If an operation must block a scope, block only that scope and make the boundary visible.
- Use determinate progress when the amount of work can be measured, and keep it accurate enough that it earns trust. Use indeterminate progress only while the remaining work is genuinely unknown.
- Put progress near the work it describes. Promote it to a broader app-level surface only when the work outlives or affects the current view.
- Offer Cancel or Pause when the operation can stop safely. Make the consequence clear: cancellation may keep completed results, roll back partial output, or leave a resumable checkpoint.
- A progress indicator is not permission to leave the main thread blocked. Verify interaction and window responsiveness under representative load.

Current sources: [Loading](https://developer.apple.com/design/human-interface-guidelines/loading) and [Progress indicators](https://developer.apple.com/design/human-interface-guidelines/progress-indicators).

## Feedback, errors, and recovery

- Put passive status and validation near the object, field, or action it describes. Feedback should answer what changed without forcing the person to dismiss routine success.
- An actionable error names what failed, states what happened to the person's work, and offers a next step. Preserve drafts, selections, inputs, and recoverable partial results across the failure.
- Reserve alerts for uncommon, important situations that require an immediate choice. Avoid them for routine status, reversible edits, or information that can live in context.
- Write specific alert titles and action buttons. Prefer verbs that describe the result over generic labels such as “OK” or “Yes.” Support the standard cancellation path when cancellation is possible.
- Register reversible edits with Undo and name the actual operation. After an undo or recovery action, make the resulting state visible; a command that silently changes hidden state does not build confidence.
- For irreversible external effects, explain the boundary before execution and provide the strongest available recovery route afterward.

Current sources: [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback), [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts), and [Undo and redo](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo).

## Localization and adaptable layout

- Keep user-visible text in localized resources or String Catalogs. Avoid assembling sentences from fragments whose grammar or word order may change by language.
- Format dates, times, durations, numbers, measurements, currency, lists, plurals, and names with locale-aware system APIs rather than hand-built templates.
- Express interface geometry with leading and trailing relationships. Let standard frameworks mirror navigation and layout direction instead of applying a blanket transform.
- Do not mirror media controls, charts, handwriting, clocks, or directional symbols blindly. Mirror when direction communicates interface flow; preserve orientation when it belongs to the represented object or data.
- Test long translations, text expansion, right-to-left direction, mixed left-to-right and right-to-left content, truncation, wrapping, menus, tables, and the smallest supported window.
- Localization failures are often structural rather than textual. A translated label that exists but clips the recovery action is still a broken workflow.

Current sources: [Layout](https://developer.apple.com/design/human-interface-guidelines/layout) and [Right to left](https://developer.apple.com/design/human-interface-guidelines/right-to-left).

## Discoverability, onboarding, and help

- Make the core workflow usable before onboarding. A person who skips, dismisses, forgets, or never sees the introduction still needs to find the app's main actions through familiar controls, menus, labels, and state.
- Start onboarding after launch, keep it brief and skippable, and avoid asking people to memorize a tour before they have context. Teach a novel gesture, mental model, or consequence at the moment it becomes relevant.
- Prefer contextual tips and short helper text for app-specific behavior. Do not narrate standard Mac controls or restate a visible label.
- Give unfamiliar or symbol-only controls concise tooltips and action-named accessibility labels. Consequential actions deserve visible words when an icon alone could be misread.
- Put durable documentation, commands, and support routes in the Help menu when the app has enough depth to need them. Let people return to help after onboarding rather than treating the first-run flow as the only explanation.
- If repeated onboarding seems necessary, inspect the interface first. The durable repair may be a clearer label, menu command, empty state, default, or progressive disclosure point.

Current sources: [Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding) and [Offering help](https://developer.apple.com/design/human-interface-guidelines/offering-help).

## Conditional concerns

Document autosave and versions, file management, notifications, printing, account setup, collaboration, and multiwindow document architecture are not universal to every Mac app, but they become baseline-quality concerns as soon as the app activates them. Consult the current HIG and framework documentation rather than copying a generic implementation into every project.
