# Apple accessibility updates for SwiftUI

Documentation reviewed: 2026-10-25. Confirm current SDK/platform availability before recommending an API.

Read this reference when auditing SwiftUI controls, preferences, media, or release-readiness claims. Load only the sections relevant to the supplied UI.

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

## Release evidence and runtime checks

- For core reading tasks, verify Accessibility Nutrition Labels evidence on the applicable platform; a screen audit does not establish app-wide support.
- When assessing a Larger Text declaration, verify core tasks at a minimum of 200% under the applicable platform criteria. This is a declaration threshold, not a universal maximum; also test extreme supported sizes where applicable.

## Reading implementation

- Long-form or paginated text must support granular navigation, continuous reading, and text selection where the product experience requires reading.
- Prefer standard accessible text views such as `TextEditor` or selectable `Text` before building custom-rendered text.
- Separate text elements that form one reading flow should be linked or ordered so VoiceOver and Speak Screen can continue without dead stops.
- Page turns, document boundaries, and custom-rendered text should expose enough structure for VoiceOver, Speak Screen, and Accessibility Reader.
- A label alone does not make custom-rendered or scanned text navigable or selectable; prefer native text or bridge to the platform text-input APIs when the reading experience requires full fidelity.

Tools to consider:
- `TextEditor` or selectable `Text` for standard reading behavior
- `accessibilityLinkedGroup(id:in:)` links elements starting in iOS/iPadOS 14 and macOS 11. Verify continuous text-navigation behavior separately on the target OS; symbol availability alone does not establish that newer reading behavior is supported
- `.accessibilityAddTraits(.causesPageTurn)` on the last text element, paired with a working accessibility scroll action, when paginated content must continue a VoiceOver read-all gesture across pages
- Categorized text-selection actions using the edit category where supported; preserve system actions and verify discovery in the Edit rotor
- UIKit/AppKit text-input APIs through representables when custom-rendered text needs line navigation, selection, and text geometry

## Media playback

- Prefer standard playback controls and authored subtitles; do not implement transcription as part of an accessibility audit.
- Keep style previews clear of controls; test subtitle selection and authored-caption rendering.
- Media playback screens must provide subtitle selection, respect the person's system subtitle style, and prefer standard AVKit playback controls when possible.
- On iOS/macOS 27 or later, verify generated subtitles can be selected when the device, language, and media source support them, and expose subtitle-style preview instead of forcing users to leave playback to compare styles.
- Custom players must preserve accessible subtitle selection and style-preview behavior rather than replacing it with a visual-only menu. Preview may temporarily replace active captions: stop it when dismissed and verify captions resume. Selecting a subtitle style changes the system preference.

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

## API evidence — 2026-11-14

- `accessibilityAdjustableAction(_:)` supplies adjustable actions; do not copy UIKit’s `.adjustable` trait into SwiftUI.
- `accessibilityLinkedGroup(id:in:)` is available from iOS/iPadOS 14 and macOS 11. This dates the symbol, not every subsequent text-navigation behavior; verify the latter on the supported OS.
- [SwiftUI AccessibilityTraits](https://developer.apple.com/documentation/swiftui/accessibilitytraits)
- [Adjustable actions](https://developer.apple.com/documentation/swiftui/view/accessibilityadjustableaction(_:))
- [Linked groups](https://developer.apple.com/documentation/swiftui/view/accessibilitylinkedgroup(id:in:))

## Form and modal sources

- [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields)
- [Writing: field hints and actionable errors](https://developer.apple.com/design/human-interface-guidelines/writing)
- [Modality](https://developer.apple.com/design/human-interface-guidelines/modality)
- [SwiftUI accessibility focus](https://developer.apple.com/videos/play/wwdc2021/10119/)

## Additional framework sources

- [SwiftUI accessibility direct touch](https://developer.apple.com/documentation/swiftui/view/accessibilitydirecttouch(_:))
- [SwiftUI page-turn trait](https://developer.apple.com/documentation/swiftui/accessibilitytraits/causespageturn)
- [WWDC26 – Refine accessibility for custom controls](https://developer.apple.com/videos/play/wwdc2026/220/)
- [WWDC26 – Enhance the accessibility of your reading app](https://developer.apple.com/videos/play/wwdc2026/219/)
- [WWDC25 – Evaluate your app for Accessibility Nutrition Labels](https://developer.apple.com/videos/play/wwdc2025/224/)
- [WWDC25 – Make your Mac app more accessible to everyone](https://developer.apple.com/videos/play/wwdc2025/229/)
- [WWDC25 – Customize your app for Assistive Access](https://developer.apple.com/videos/play/wwdc2025/238/)
- [SwiftUI accessibility action categories](https://developer.apple.com/documentation/swiftui/accessibilityactioncategory)
