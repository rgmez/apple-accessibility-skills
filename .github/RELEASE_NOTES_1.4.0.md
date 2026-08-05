## Summary

- Expanded WWDC26 accessibility coverage for SwiftUI, UIKit, and AppKit auditor skills.
- Added stronger review guidance for accessible reading experiences, custom-rendered text, direct touch, and complex custom controls.
- Updated all three skill versions to `1.4.0`.

## Why this release

This is a coverage polish release. After another pass over Apple's WWDC26 accessibility sessions, the skills now cover two areas that deserved more explicit audit guidance: long-form reading experiences and complex custom controls. These are common places where apps can look polished visually while still failing VoiceOver, Speak Screen, Switch Control, keyboard, or direct-touch users.

## Highlights

### Reading experiences

- Added checks for granular text navigation, continuous reading, text selection, page turns, and separate text regions.
- Added guidance for `TextEditor`, selectable `Text`, `UITextView`, `UITextInput`, `UITextInteraction`, and `NSTextView`.
- Added checks for custom-rendered text, scanned pages, and canvas-like reading surfaces so they do not collapse into a single inaccessible image or label.

### Custom controls

- Expanded custom-control guidance around purpose, value/state, available actions, and interaction feedback.
- Added direct-touch guidance for gesture-heavy surfaces, including when standard activation or custom actions are a better fit.
- Strengthened checks for drag/drop, context menus, reorder, swipe actions, and generated actions so they remain usable without touch-only or pointer-only interaction.

### References

- Added WWDC26 references for custom controls, reading apps, generated subtitles, UIKit modernization, and AppKit modernization where relevant.

## Compatibility notes

- No breaking changes.
- Existing skill names and install paths remain valid.
- Skill behavior/output guidance changed, so SwiftUI, UIKit, and AppKit skill versions are now `1.4.0`.

## Test plan

- [x] Validate all local Markdown links with `scripts/check_markdown_local_links.py`.
- [x] Validate whitespace with `git diff --check`.
- [x] Confirm output contract consistency against `docs/skill-canonical-standard.md`.
- [x] Confirm changed checklists match the updated skill instructions.
- [x] Confirm the Docs Checks workflow is green on `main`.
