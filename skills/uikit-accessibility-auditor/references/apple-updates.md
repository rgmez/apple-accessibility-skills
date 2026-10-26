# Apple accessibility updates for UIKit

Documentation reviewed: 2026-10-25. Confirm current SDK/platform availability before recommending an API.

Read this reference when auditing UIKit controls, preferences, media, or release-readiness claims.

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

## Media and text

- Standard media players already provide subtitle support. Prefer `AVPlayerViewController`, standard legible-media controls, and authored subtitles where possible.
- A custom `AVPlayerLayer` style preview may temporarily replace active captions. Position the preview away from controls, stop it when dismissed, and verify active captions resume. Choosing a style updates the system subtitle-style preference.
- Verify subtitle selection, authored subtitles, and style preview with supported media. Do not implement transcription manually for an accessibility audit.
- Map tested core tasks to Accessibility Nutrition Labels evidence on iOS or iPadOS; a passing screen audit does not establish app-wide support.
- When assessing a Larger Text declaration, verify core tasks at a minimum of 200% under the applicable platform criteria. This is a declaration threshold, not a universal maximum; also test extreme supported sizes where applicable.
- For long-form or paginated text, verify Read All, text navigation, selection, and continuation across page boundaries using standard text views where possible.
- Keep screen and layout announcements focused; do not announce every high-frequency value update.
- Use Accessibility Inspector and runtime device checks to distinguish documented behavior from assumptions.

## Optional UI automation

- `XCUIVoiceOverService` and `XCUIDevice.voiceOverService` were labeled beta in the consulted documentation. Confirm SDK, platform, and runtime support before using them.
- If used, enable VoiceOver only for the test, navigate, verify `currentSpeech`, and restore the original VoiceOver state in cleanup even when a test fails. Manual checks remain required.

## Sources

- [UIKit accessibility](https://developer.apple.com/documentation/uikit/accessibility)
- [Discover generated subtitles and subtitle styles (WWDC26)](https://developer.apple.com/videos/play/wwdc2026/256/?time=463)
- [Accessibility Nutrition Labels (Tech Talk)](https://developer.apple.com/videos/play/tech-talks/111433/?time=1084)
- [XCUIVoiceOverService](https://developer.apple.com/documentation/xcuiautomation/xcuivoiceoverservice)
- [VoiceOver automation (WWDC26)](https://developer.apple.com/videos/play/wwdc2026/8005/)
