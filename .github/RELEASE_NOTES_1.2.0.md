## Summary

- Expanded the Apple accessibility auditor skills beyond VoiceOver and Dynamic Type to cover more non-touch input paths.
- Strengthened custom control guidance for SwiftUI, UIKit, and AppKit so patch suggestions include accessible activation paths.
- Adjusted example severity guidance to better match the P0/P1/P2 output contract.

## Why this release

This release makes the skills better at catching issues that affect users who rely on Voice Control, Switch Control, Full Keyboard Access, or custom accessibility actions. It also closes gaps where previous guidance could label a view as a button without ensuring it was actually activatable through assistive technologies.

## Highlights

### SwiftUI

- Custom tappable views using `.onTapGesture` now require explicit accessible activation when they cannot be replaced with `Button`.
- Checklists now include Voice Control and Switch Control validation for labels, grouping, scan order, and custom actions.
- Guidance calls out deployment target awareness for newer accessibility APIs.

### UIKit

- Added audit coverage for Voice Control, Switch Control, and Full Keyboard Access.
- Added guidance for `accessibilityActivate()`, `accessibilityCustomActions`, and `accessibilityUserInputLabels`.
- Reclassified the Dynamic Type fixed-font example from `P0` to `P1`.

### AppKit

- Custom `NSView` controls now require an accessibility press/action path where applicable.
- Added guidance for non-pointer activation, voice-friendly labels, Switch Control scan order, and discoverable custom actions.

## Compatibility notes

- No breaking changes.
- Existing skill names and install paths remain valid.
- Skill behavior/output guidance changed, so SwiftUI, UIKit, and AppKit skill versions are now `1.2.0`.

## Test plan

- [x] Validate all local Markdown links with `scripts/check_markdown_local_links.py`.
- [x] Validate whitespace with `git diff --check`.
- [x] Validate output contract consistency against the changed skill/checklist files.
