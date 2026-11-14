# Apple accessibility updates for AppKit

Documentation reviewed: 2026-10-25. Confirm current SDK/platform availability before recommending an API.

Read this reference when auditing AppKit controls, workspace preferences, media, or release-readiness claims. Load only the sections relevant to the supplied UI.

## Controls and keyboard navigation

- Prefer native AppKit controls and standard views; preserve their roles, actions, values, and focus behavior.
- Keyboard navigation must be enabled and testable with Tab and Shift-Tab. Custom controls need visible focus and an equivalent keyboard activation path.
- Keep the key-view loop predictable; pointer-only gestures, context menus, or drag/drop must not be the only way to perform an action.
- Do not transplant UIKit traits or SwiftUI environment values to `NSView`; use the documented AppKit accessibility APIs and availability checks.
- Preserve independently actionable table and outline children when grouping accessible content.
- Verify VoiceOver roles, selected state, and values for custom cells and rows after reload or selection changes.
- Check Voice Control or Switch Control where the app supports them, especially for custom actions and grouped controls.

## Preferences and visual changes

- Read `NSWorkspace.shared.accessibilityDisplayShouldReduceMotion`, `accessibilityDisplayShouldReduceTransparency`, `accessibilityDisplayShouldIncreaseContrast`, and `accessibilityDisplayShouldDifferentiateWithoutColor` where applicable.
- Observe `NSWorkspace.accessibilityDisplayOptionsDidChangeNotification` using `NSWorkspace.shared.notificationCenter`, then re-read the current values.
- Test live changes for Reduce Motion, Reduce Transparency, Increase Contrast, Differentiate Without Color, and Dark Mode. State must remain understandable without color alone.
- Keep translucent materials, window resizing, toolbars, sidebars, and menu items legible and keyboard reachable as preferences change.

## Release evidence and runtime checks

- Map tested core tasks to Accessibility Nutrition Labels evidence for the applicable platform; a screen audit does not establish app-wide support.
- When assessing a Larger Text declaration, verify core tasks at a minimum of 200% under the applicable platform criteria. This is a declaration threshold, not a universal maximum; also test extreme supported sizes where applicable.
- For long-form or paginated text, verify VoiceOver Read All, text navigation, selection, and continuation across shared elements and page boundaries.
- Announce meaningful dynamic updates without moving focus unnecessarily; preserve the current task when content refreshes.
- Use Accessibility Inspector and runtime checks to distinguish documented behavior from assumptions.

## Reading implementation

- Long-form or paginated text must support granular navigation, continuous reading, and text selection where the product experience requires reading.
- Prefer `NSTextView` or SwiftUI text views that already support accessible reading behavior before building custom-rendered text.
- Custom-rendered text, scanned pages, or canvas-like reading surfaces should expose text structure instead of a single image or generic group.
- Page turns, document boundaries, and separate text regions should preserve read-all flow for VoiceOver, Speak Screen, and Accessibility Reader where available.

Tools to consider:
- `NSTextView` for standard accessible reading, navigation, and selection behavior
- SwiftUI `TextEditor` or selectable `Text` when embedded SwiftUI is appropriate
- `accessibilitySharedTextUIElements` when separate text elements must form one VoiceOver reading flow (use availability checks)
- Platform-supported reading actions and notifications for paginated content; do not translate UIKit `.causesPageTurn` or `.screenChanged` directly into AppKit APIs

## Media playback

- Prefer standard playback controls and authored subtitles; do not implement transcription as part of an accessibility audit.
- Keep style previews clear of controls; test subtitle selection and authored-caption rendering.
- Media playback screens must expose subtitle selection, respect system subtitle styles, and prefer `AVPlayerView` or standard Media Accessibility controls when possible.
- On macOS 27 or later, expose supported generated or translated subtitle tracks and identify them clearly in custom menus.
- Provide subtitle-style preview during playback through `AVPlayerView`, `AVLegibleMediaOptionsMenuController`, or an equivalent accessible custom flow.
- Availability-gate newer media APIs and preserve authored-subtitle and system-style behavior on earlier macOS releases. Subtitle previews may temporarily hide captions; stop the preview and restore them when dismissed. Style selection changes the system preference.

## Optional UI automation

- `XCUIVoiceOverService` and `XCUIDevice.voiceOverService` were labeled beta in the consulted documentation. Confirm SDK, platform, and runtime support before using them.
- If used, enable VoiceOver only for the test, navigate, verify `currentSpeech`, and restore the original VoiceOver state in cleanup even when a test fails. Manual checks remain required.

## Sources

- [Make your Mac app more accessible to everyone (WWDC25)](https://developer.apple.com/videos/play/wwdc2025/229/)
- [NSWorkspace accessibility display transparency](https://developer.apple.com/documentation/appkit/nsworkspace/accessibilitydisplayshouldreducetransparency)
- [Discover generated subtitles and subtitle styles (WWDC26)](https://developer.apple.com/videos/play/wwdc2026/256/?time=463)
- [Accessibility Nutrition Labels (Tech Talk)](https://developer.apple.com/videos/play/tech-talks/111433/?time=1084)
- [XCUIVoiceOverService](https://developer.apple.com/documentation/xcuiautomation/xcuivoiceoverservice)
- [VoiceOver automation (WWDC26)](https://developer.apple.com/videos/play/wwdc2026/8005/)

## Form and modal sources

- [Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields)
- [Writing: field hints and actionable errors](https://developer.apple.com/design/human-interface-guidelines/writing)
- [Modality](https://developer.apple.com/design/human-interface-guidelines/modality)

## Additional framework sources

- [Keyboard Navigation and Focus (macOS)](https://developer.apple.com/documentation/appkit/nsresponder)
- [AppKit shared text UI elements](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/accessibilitysharedtextuielements)
- [AVKit legible media options menu](https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller)
- [WWDC26 – Modernize your AppKit app](https://developer.apple.com/videos/play/wwdc2026/289/)
- [WWDC26 – Refine accessibility for custom controls](https://developer.apple.com/videos/play/wwdc2026/220/)
- [WWDC26 – Enhance the accessibility of your reading app](https://developer.apple.com/videos/play/wwdc2026/219/)
- [WWDC25 – Evaluate your app for Accessibility Nutrition Labels](https://developer.apple.com/videos/play/wwdc2025/224/)
- [AppKit announcement requests](https://developer.apple.com/documentation/appkit/nsaccessibility-swift.struct/notification/announcementrequested)
