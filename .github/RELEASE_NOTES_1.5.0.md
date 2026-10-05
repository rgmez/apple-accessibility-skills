## Summary

- Updated all three accessibility auditor skills to `1.5.0`.
- Completed WWDC26 reading, custom-control, and subtitle guidance with OS-specific availability.
- Added instrumented verification, conditional Assistive Access and Accessibility Nutrition Labels evaluation, and Edit rotor guidance.
- Corrected examples that could hide essential text or imply an unsupported button action.

## Highlights

- SwiftUI grouping now distinguishes containers, combined elements, and replacement representations. Keyboard focus and accessibility focus are reviewed independently, including initial focus on iOS/macOS 26 or later.
- UIKit guidance preserves existing traits and state during cell reuse, keeps independently actionable children reachable, and exposes selected-text actions in the Edit rotor.
- AppKit guidance uses platform-specific notifications and localized announcement payloads while preserving the current task and focus.
- Accessibility Inspector and optional audits in compatible existing UI test targets complement manual verification. Reports distinguish executed checks from pending checks.
- Checklists are references relative to each installed skill, rather than files to create in the audited project.
- Linked text guidance identifies iOS 27 availability; generated subtitles identify iOS/macOS 27 availability and supported-device/language/source constraints.

## Compatibility notes

- Existing skill names and installation paths remain unchanged.
- New APIs require documented OS/platform availability checks and accessible fallbacks.
- Assistive Access and App Store declarations are evaluated only when relevant to the requested scope.

## Validation

- Passed Markdown lint using the repository configuration.
- Passed local Markdown link validation and `git diff --check`.
- Passed YAML metadata, canonical section order, checklist reference, and `1.5.0` version consistency checks for all three skills.
- Runtime VoiceOver, keyboard, media, and Assistive Access checks require a consuming app; documentation validation does not establish those outcomes.
