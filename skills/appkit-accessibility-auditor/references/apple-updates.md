# Apple accessibility updates for AppKit

Documentation reviewed: 2026-10-25. Confirm current SDK/platform availability before recommending an API.

Read this reference when auditing AppKit controls, workspace preferences, media, or release-readiness claims.

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

## Media and text

- Standard media players already provide subtitle support. Prefer `AVPlayerView` and standard Media Accessibility controls with authored subtitles.
- A custom `AVPlayerLayer` style preview may temporarily replace active captions. Position the preview away from controls, stop it when dismissed, and verify active captions resume. Choosing a style updates the system subtitle-style preference.
- Verify subtitle selection, authored subtitles, generated or translated track labeling where supported, and style preview. Do not implement transcription manually for an accessibility audit.
- Map tested core tasks to Accessibility Nutrition Labels evidence for the applicable platform; a screen audit does not establish app-wide support.
- When assessing a Larger Text declaration, verify core tasks at a minimum of 200% under the applicable platform criteria. This is a declaration threshold, not a universal maximum; also test extreme supported sizes where applicable.
- For long-form or paginated text, verify VoiceOver Read All, text navigation, selection, and continuation across shared elements and page boundaries.
- Announce meaningful dynamic updates without moving focus unnecessarily; preserve the current task when content refreshes.
- Use Accessibility Inspector and runtime checks to distinguish documented behavior from assumptions.

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
