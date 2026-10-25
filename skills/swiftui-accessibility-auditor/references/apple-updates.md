# Apple accessibility updates for SwiftUI

Documentation reviewed: 2026-10-25. Confirm current SDK/platform availability before recommending an API.

Read this reference when auditing SwiftUI controls, preferences, media, or release-readiness claims.

## Controls and semantics

- Prefer native SwiftUI controls and their system styles; they already provide platform semantics, actions, and focus behavior.
- For a custom control, first consider `accessibilityRepresentation` to expose an equivalent native control.
- Use `accessibilityChildren` when synthetic data needs to be represented as accessible child elements.
- SF Symbols may provide useful default labels. Inspect the resulting element before adding a label; do not flag a useful automatic label.
- On supported SDKs, `accessibilityLabel(_:isEnabled:)` and `accessibilityLabel { label in ... }` can conditionally modify a label while preserving the existing label. Gate each use by documented platform availability.
- Use `accessibilityActions` or named `accessibilityAction`s for actions otherwise only exposed on hover or through gestures, keeping the underlying behavior synchronized.
- For drag and drop, expose meaningful `accessibilityDragPoint` and `accessibilityDropPoint` destinations when the interaction has named destinations.

## Preferences and visual changes

- Test live changes for Differentiate Without Color, Increase Contrast, and Dark Mode; state must remain understandable without color alone.
- `accessibilityShowBorders` reflects a dedicated Show Borders setting on macOS 27 and later. On earlier macOS versions its value follows Increase Contrast; verify compiler/SDK support separately.
- `accessibilityReduceHighlightingEffects` minimizes highlighting or flashing effects. Verify the supported platform and behavior at runtime.
- `accessibilityPlayAnimatedImages == false` stops animated images from autoplaying. This preference is independent of Reduce Motion.
- Preserve readable focus, contrast, and semantics when materials, scroll effects, or resizable windows change.

## Media and text

- Standard media players already provide subtitle support. Prefer system playback controls and authored subtitles.
- A custom `AVPlayerLayer` style preview may temporarily replace active captions. Position the preview away from controls, stop it when dismissed, and verify active captions resume. Choosing a style updates the system subtitle-style preference.
- Test subtitle selection, authored subtitle rendering, and style preview on supported media and platforms. Do not implement transcription manually for an accessibility audit.
- For core reading tasks, verify Accessibility Nutrition Labels evidence on the applicable platform; a screen audit does not establish app-wide support.
- When assessing a Larger Text declaration, verify core tasks at a minimum of 200% under the applicable platform criteria. This is a declaration threshold, not a universal maximum; also test extreme supported sizes where applicable.

## Optional UI automation

- `XCUIVoiceOverService` and `XCUIDevice.voiceOverService` were labeled beta in the consulted documentation. Confirm SDK, platform, and runtime support before using them.
- If used, enable VoiceOver only for the test, navigate, verify `currentSpeech`, and restore the original VoiceOver state in cleanup even when a test fails. Manual checks remain required.

## Sources

- [Catch up on accessibility in SwiftUI (WWDC24)](https://developer.apple.com/videos/play/wwdc2024/10073/)
- [SwiftUI accessibilityRepresentation](https://developer.apple.com/documentation/swiftui/view/accessibilityrepresentation(representation:))
- [SwiftUI accessibilityShowBorders](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityshowborders)
- [SwiftUI accessibilityReduceHighlightingEffects](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityreducehighlightingeffects)
- [SwiftUI accessibilityPlayAnimatedImages](https://developer.apple.com/documentation/swiftui/environmentvalues/accessibilityplayanimatedimages)
- [Discover generated subtitles and subtitle styles (WWDC26)](https://developer.apple.com/videos/play/wwdc2026/256/?time=463)
- [Accessibility Nutrition Labels (Tech Talk)](https://developer.apple.com/videos/play/tech-talks/111433/?time=1084)
- [XCUIVoiceOverService](https://developer.apple.com/documentation/xcuiautomation/xcuivoiceoverservice)
- [VoiceOver automation (WWDC26)](https://developer.apple.com/videos/play/wwdc2026/8005/)
