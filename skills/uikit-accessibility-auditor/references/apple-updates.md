# Apple accessibility updates for UIKit

Documentation reviewed: 2026-10-25. Confirm current SDK/platform availability before recommending an API.

Read this reference when auditing UIKit controls, preferences, media, or release-readiness claims. Load only the sections relevant to the supplied UI.

## Platform evidence

Session sources checked: 2026-10-26. Use the linked Apple material as evidence for the specific behavior described, then confirm individual API availability against the project's SDK and deployment target.

- [Modernize your UIKit app (WWDC26)](https://developer.apple.com/videos/play/wwdc2026/278/) documents resizable iPhone Mirroring and iPhone apps on iPad in iOS/macOS 27.
- [Customize your app for Assistive Access (WWDC25)](https://developer.apple.com/videos/play/wwdc2025/238/) documents the SwiftUI `AssistiveAccess` scene in iOS/iPadOS 26; it is not a UIKit scene API.

## Controls and semantics

- Prefer native UIKit controls and standard containers; preserve their roles, actions, traits, focus, and state behavior.
- For a custom control, expose purpose, value, state, and an activation path for VoiceOver, Voice Control, Switch Control, and Full Keyboard Access.
- Do not add a label when a native control already exposes a correct visible name. Inspect the accessibility element first.
- Use documented availability checks for newer APIs and retain a supported fallback; do not infer availability from a WWDC year.
- Preserve authored labels and values when adding custom actions; a custom action must not hide the control's primary activation.
- For cells and cards, group related content only when independently actionable children remain reachable.
- Check Voice Control names, Switch Control scan order, and Full Keyboard Access activation whenever grouping or custom gestures change.

## Preferences and visual changes

- Observe UIKit accessibility preference changes through the documented `UIAccessibility` notifications and re-read the current values after notification.
- Use `traitCollection.accessibilityContrast` when contrast-dependent behavior is needed; verify the affected view updates after trait changes.
- Test Differentiate Without Color, Increase Contrast, and Dark Mode live. Error, selection, and status must remain understandable without color alone.
- For animation and flashing preferences, use only platform APIs available to the deployment target and verify their runtime behavior. Do not invent exact symbol names from preference descriptions.
- Resizable iPhone and iPad layouts, mirrored screens, and changing bars must preserve Dynamic Type, focus order, and VoiceOver order.

## Release evidence and runtime checks

- Map tested core tasks to Accessibility Nutrition Labels evidence on iOS or iPadOS; a passing screen audit does not establish app-wide support.
- When assessing a Larger Text declaration, verify core tasks at a minimum of 200% under the applicable platform criteria. This is a declaration threshold, not a universal maximum; also test extreme supported sizes where applicable.
- For long-form or paginated text, verify Read All, text navigation, selection, and continuation across page boundaries using standard text views where possible.
- Keep screen and layout announcements focused; do not announce every high-frequency value update.
- Use Accessibility Inspector and runtime device checks to distinguish documented behavior from assumptions.

## Reading implementation

- Long-form or paginated text must support granular navigation, continuous reading, and text selection where the product experience requires reading.
- Prefer `UITextView` or other standard text views that already support accessible text navigation and selection.
- Custom-rendered text, scanned pages, or canvas-like reading surfaces should adopt text input/accessibility APIs instead of exposing the page as a single image or label.
- Page turns, document boundaries, and separate text regions should preserve read-all flow for VoiceOver, Speak Screen, and Accessibility Reader.
- Connect separate text views with `accessibilityNextTextNavigationElement` and `accessibilityPreviousTextNavigationElement` when line/word/character navigation must continue across elements.
- For custom-rendered or scanned text, implement the full `UITextInput` contract, including text ranges, tokenizer, text geometry, and selection updates; a label or custom action alone is insufficient.

Tools to consider:
- `UITextView` and `UITextInput` for granular accessible text navigation and selection
- `UITextInteraction` when custom text needs visible selection behavior
- `accessibilityNextTextNavigationElement` / `accessibilityPreviousTextNavigationElement` for cross-element reading navigation (introduced in iOS 18)
- `.causesPageTurn` on the last text element and `accessibilityScroll(_:)` for read-all continuation across paginated content
- `UIAccessibilityCustomAction.editCategory` for actions on selected text; preserve the superclass actions and verify discovery in the Edit rotor

## Media playback

- Prefer standard playback controls and authored subtitles; do not implement transcription as part of an accessibility audit.
- Keep style previews clear of controls; test subtitle selection and authored-caption rendering.
- Media playback screens must expose subtitle selection, respect system subtitle styles, and prefer `AVPlayerViewController`, `AVLegibleMediaOptionsMenuController`, or equivalent standard controls when possible.
- On iOS/iPadOS 27 or later, when supported by the device, language, and media source, expose generated subtitle choices and identify translated/generated tracks clearly.
- Provide subtitle-style preview during playback through standard AVKit/Media Accessibility controls or an equivalent accessible custom flow; do not make people leave the player to compare styles.
- Gate newer APIs by documented OS/platform availability and retain authored-subtitle and system-style fallbacks on earlier deployment targets. Subtitle previews may temporarily hide captions; stop the preview and restore them when dismissed. Style selection changes the system preference.

## Optional UI automation

- `XCUIVoiceOverService` and `XCUIDevice.voiceOverService` were labeled beta in the consulted documentation. Confirm SDK, platform, and runtime support before using them.
- If used, enable VoiceOver only for the test, navigate, verify `currentSpeech`, and restore the original VoiceOver state in cleanup even when a test fails. Manual checks remain required.

## Sources

- [UIKit accessibility](https://developer.apple.com/documentation/uikit/accessibility)
- [Discover generated subtitles and subtitle styles (WWDC26)](https://developer.apple.com/videos/play/wwdc2026/256/?time=463)
- [Accessibility Nutrition Labels (Tech Talk)](https://developer.apple.com/videos/play/tech-talks/111433/?time=1084)
- [XCUIVoiceOverService](https://developer.apple.com/documentation/xcuiautomation/xcuivoiceoverservice)
- [VoiceOver automation (WWDC26)](https://developer.apple.com/videos/play/wwdc2026/8005/)

## Form and modal sources

- [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields)
- [Writing: field hints and actionable errors](https://developer.apple.com/design/human-interface-guidelines/writing)
- [Modality](https://developer.apple.com/design/human-interface-guidelines/modality)

## Additional framework sources

- [UIKit text navigation elements](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitynexttextnavigationelement)
- [UIKit UITextInput](https://developer.apple.com/documentation/uikit/uitextinput)
- [UIKit direct interaction trait](https://developer.apple.com/documentation/uikit/uiaccessibilitytraits/allowsdirectinteraction)
- [AVKit legible media options menu](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller)
- [WWDC26 – Refine accessibility for custom controls](https://developer.apple.com/videos/play/wwdc2026/220/)
- [WWDC26 – Enhance the accessibility of your reading app](https://developer.apple.com/videos/play/wwdc2026/219/)
- [WWDC25 – Evaluate your app for Accessibility Nutrition Labels](https://developer.apple.com/videos/play/wwdc2025/224/)
- [UIKit custom-action edit category](https://developer.apple.com/documentation/uikit/uiaccessibilitycustomaction/editcategory)
