# Inspecting a running Mac app

Everything here needs the app running. These checks find what a source read structurally cannot: an incomplete menu, an unlabeled button, a window that forgets itself, a sheet that ignores Escape.

## Getting it running

Build with the project's own tooling — `make build`, `make run`. Don't hand-write `xcodebuild`.

```bash
open -a "<App>.app"                      # or the path make build produced
pgrep -x "<App>"                         # confirm it launched and stayed up
```

If it won't build, stop. Report the error as finding #1 and say the dynamic audit didn't run.

## Permission gate

The menu and accessibility queries below drive System Events, which needs Accessibility permission for the process running them (Terminal, or the host app). Test it first:

```bash
osascript -e 'tell application "System Events" to tell process "Finder" to get name of every menu bar item of menu bar 1'
```

A list of menu names means you're authorized. Error `-1743` means you are not — tell the user to grant it under System Settings → Privacy & Security → Accessibility, and skip to the visual checks. Don't try to grant it yourself.

## The menu bar sweep

This is mechanical, and it is the highest-value dynamic check on macOS.

```bash
APP="<App>"   # process name, as pgrep sees it

# Top-level menus
osascript -e "tell application \"System Events\" to tell process \"$APP\" to get name of every menu bar item of menu bar 1"

# Every item in one menu, with its shortcut key and whether it's enabled
osascript -e "tell application \"System Events\" to tell process \"$APP\" to get {name, value of attribute \"AXMenuItemCmdChar\" of it, enabled} of every menu item of menu 1 of menu bar item \"Edit\" of menu bar 1"
```

`missing value` in the name position is a separator. `missing value` in the shortcut position means no key equivalent.

Walk every top-level menu. Compare against the required set in [audit-map.md](audit-map.md#3-menu-bar-and-commands), and record:

- Menus absent entirely — especially Edit, and especially its Undo.
- Items present with no key equivalent where convention has one.
- **Items enabled when they should not be.** Run the query with nothing selected, then again with a selection, and diff. Copy, Cut, Delete, and Select All that stay enabled with an empty selection are doing no validation. Undo enabled with an empty stack is the same bug.
- Items whose titles aren't Title Case.
- Features you found in the source that appear in no menu.

Submenus nest: `menu 1 of menu item "Sort By" of menu 1 of menu bar item "View" of menu bar 1`.

## The accessibility tree

```bash
# What's in the front window
osascript -e "tell application \"System Events\" to tell process \"$APP\" to get {role, name, description} of every UI element of window 1"

# Buttons, with labels and state — unlabeled controls show as missing value
osascript -e "tell application \"System Events\" to tell process \"$APP\" to get {role, title, description, enabled, focused} of every button of window 1"

# A specific attribute
osascript -e "tell application \"System Events\" to tell process \"$APP\" to get value of attribute \"AXSize\" of window 1"
```

`title`, `name`, and `description` all `missing value` on an interactive element is an accessibility finding: VoiceOver reads it as its role alone. Note the role and position so the finding is locatable.

For a full audit rather than spot checks, use **Accessibility Inspector** (Xcode → Open Developer Tool → Accessibility Inspector). Point it at the app, run its audit, and it lists unlabeled elements, contrast failures, and hit-target problems directly. Faster and more complete than walking the tree by hand — use the shell queries for specific questions and the Inspector for coverage.

## Window state restoration

The test that catches the most-felt bug on macOS:

1. Launch. Resize the window to something distinctive and move it. Change the sidebar width, select something, scroll down, open the inspector.
2. Quit with ⌘Q. Not force-quit — that's a different code path.
3. Relaunch.
4. Record what came back and what didn't.

Then:
- Close the last window and click the Dock icon. A window should reopen. Nothing happening is a missing `applicationShouldHandleReopen`.
- Resize to the smallest the window allows and look for clipped content.
- Enter full screen, then exit. Then tile it to half the screen (macOS 15+) and look at the layout.
- With an external display attached, move the window to it, quit, disconnect, relaunch. The window must not come back off screen.

Capture screenshots of the broken states — one window at a time, by window id. Read the `window-capture` skill first; never the full screen.

## Keyboard-only pass

Turn on System Settings → Keyboard → Keyboard navigation, then put the mouse down and try to use the app.

- Tab through the main window. Note every control you cannot reach and every point where the ring vanishes or the chain loops.
- Open each sheet and dialog. Escape must cancel, Return must commit the safe default.
- In lists and tables: arrow keys move selection, Return opens, Delete removes.
- Try the app's primary task start-to-finish without the mouse. Where you get stuck is the finding.

## Settings and appearance pass

Change the setting, look at the app, change it back. Each one takes seconds and each catches a different class of breakage.

```bash
# Appearance
osascript -e 'tell app "System Events" to tell appearance preferences to set dark mode to true'
osascript -e 'tell app "System Events" to tell appearance preferences to set dark mode to false'
```

Accessibility settings have no scripting interface — set them in System Settings → Accessibility → Display, and reset them after:

| Setting | What breaks |
| --- | --- |
| Increase contrast | Custom colors that were only checked at default contrast; vanished borders |
| Reduce transparency | Materials replaced by opaque fills — text that relied on vibrancy becomes unreadable |
| Reduce motion | Animations that should cross-fade instead of moving; a transition that becomes a jump-cut |
| Differentiate without color | Status conveyed by color alone |
| A non-default accent color | Hardcoded blue |

Take a screenshot in each state and compare. Increase contrast and reduce transparency together is the harshest combination and the one that exposes the most.

## Logs while it runs

```bash
log stream --predicate 'subsystem == "<your.bundle.id>"' --level debug
log show --last 5m --predicate 'process == "<App>"' --style compact
```

Constraint warnings, failed file reads, unhandled errors, and permission denials appear here and nowhere in the UI. A screen that looks right while the log fills with errors is a finding.

## Performance while it runs

```bash
xcrun xctrace record --template 'Time Profiler' --attach "<App>" --output trace.trace
```

Drive the app's main task during the recording, then open the trace. Look for main-thread work during interaction and any hang over 250 ms. Time launch separately: quit, start the timer, launch, stop when the window is interactive.

## Cleanup

Reset everything you changed: appearance, accessibility settings, keyboard navigation. Quit the app. Say in the report which settings you toggled, so the user knows what to check if something feels off afterward.
