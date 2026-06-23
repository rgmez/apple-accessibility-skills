## Summary

- Added WWDC26 / SDK 2027 readiness checks to the SwiftUI, UIKit, and AppKit accessibility auditor skills.
- Expanded manual validation coverage for resizable layouts, Liquid Glass legibility, media subtitles, clearer labels, and non-touch interaction paths.
- Updated all three skill versions to `1.3.0`.

## Why this release

This release keeps the Apple accessibility auditor skills current with the WWDC26 platform direction. It helps reviewers catch accessibility regressions introduced by resizable iPhone apps, iPhone Mirroring, iPad windowing, Liquid Glass materials, generated subtitle flows, dynamic menus, and Siri/App Intents entry points.

## Highlights

### SwiftUI

- Added checks for resizable windows, iPhone Mirroring, iPad windowing, toolbar overflow, and focus stability.
- Added guidance for Liquid Glass legibility, reorderable containers, swipe actions, drag/drop, media subtitles, App Intents, and clear action naming.

### UIKit

- Added checks for SDK 2027 adaptivity risks including `UIScreen.main`, fixed bounds, idiom, and orientation assumptions.
- Added guidance for tab/sidebar changes, prominent tabs, navigation bar minimization, menu image visibility, media subtitle controls, drag/drop, and Siri/App Intents entry points.

### AppKit

- Added checks for resizable windows, sidebars, toolbars, menu image visibility, Liquid Glass legibility, and media subtitle controls.
- Strengthened guidance for pointer-independent access to drag/drop, context menus, generated actions, and clear toolbar/menu naming.

## Compatibility notes

- No breaking changes.
- Existing skill names and install paths remain valid.
- Skill behavior/output guidance changed, so SwiftUI, UIKit, and AppKit skill versions are now `1.3.0`.

## Test plan

- [x] Validate all local Markdown links with `scripts/check_markdown_local_links.py`.
- [x] Validate whitespace with `git diff --check`.
- [x] Validate output contract consistency against the changed skill/checklist files.
- [x] Confirm the Docs Checks workflow is green on `main`.
