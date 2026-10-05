# UIKit Accessibility Checklist

This checklist is derived from Apple's official accessibility guidance and is intended for **manual verification** after applying changes suggested by the UIKit Accessibility Auditor.

Use VoiceOver, Dynamic Type, and touch interaction to validate behavior.

---

## VoiceOver Labels & Values
- [ ] All actionable elements have meaningful accessibility labels
- [ ] Labels match visible text where possible for predictable Voice Control commands
- [ ] Icon-only buttons are understandable without visual context
- [ ] Changing states expose updated accessibility values
- [ ] Hints are used only when they add meaningful guidance

## Traits & Roles
- [ ] Correct traits are applied (button, header, selected, disabled)
- [ ] Custom controls expose appropriate roles and states
- [ ] Cell reuse preserves existing traits and refreshes selected/disabled state
- [ ] Grouping does not hide independently actionable children

## Reading Order & Grouping
- [ ] VoiceOver navigation order is logical
- [ ] Complex cells are grouped appropriately
- [ ] No unnecessary VoiceOver stops inside a single cell

## Dynamic Type
- [ ] Text scales with the user's preferred content size category
- [ ] Custom fonts scale using UIFontMetrics
- [ ] Layout supports large text without clipping important content

## Touch Targets & Interaction
- [ ] Tap targets are large enough for comfortable interaction
- [ ] Custom hit areas respond consistently
- [ ] Interactive elements are discoverable via VoiceOver
- [ ] Custom gesture-driven controls expose an accessible activation path
- [ ] Custom controls expose purpose, value/state, available actions, and interaction feedback
- [ ] Direct interaction is reserved for controls that genuinely need raw gestures
- [ ] Single-axis adjustable controls support increment/decrement and announce synchronized values
- [ ] Multidimensional or discrete gestures have named UIAccessibilityCustomAction alternatives
- [ ] Passthrough/direct-touch controls use a meaningful activation point and avoid announcement flooding
- [ ] Direct-touch interactions retain alternatives for Switch Control, Voice Control, and Full Keyboard Access

## Voice Control, Switch Control & Keyboard
- [ ] Voice Control "Show names" exposes clear, non-duplicated labels
- [ ] Switch Control can reach controls in a logical scan order
- [ ] Full Keyboard Access can focus and activate interactive elements
- [ ] Secondary actions are exposed through custom actions when hidden behind gestures

## Reading & Text Experiences
- [ ] Long-form text supports granular navigation, continuous reading, and text selection where relevant
- [ ] `UITextView` or standard text views are preferred over custom-rendered text when possible
- [ ] Custom-rendered text or scanned pages expose text structure instead of a single image/label
- [ ] Page turns and separate text regions preserve read-all flow for VoiceOver, Speak Screen, and Accessibility Reader
- [ ] Linked text views move across elements with the Lines rotor without dead ends
- [ ] Custom text implements UITextInput text ranges, tokenizer, geometry, and selection updates when full reading fidelity is required
- [ ] Read-all turns pages and resumes at the correct next text element
- [ ] Selected-text custom actions appear in the Edit rotor and preserve system actions

## Screen Changes & Announcements
- [ ] Screen transitions are announced when appropriate
- [ ] Dynamic content updates are communicated clearly
- [ ] Announcements are not overused

## Color & State
- [ ] States are not conveyed by color alone
- [ ] Error/success/selection states are understandable via VoiceOver

## WWDC26 / OS 27 Readiness
- [ ] Resizable iPhone apps, iPhone Mirroring, and iPad windowing preserve Dynamic Type, focus, and VoiceOver order
- [ ] Layout and accessibility behavior do not depend on `UIScreen.main`, fixed screen bounds, idiom, or orientation checks
- [ ] Tab/sidebar changes, prominent tabs, navigation bar minimization, and menu image visibility do not hide important actions
- [ ] Liquid Glass, translucent materials, and scroll edge effects remain legible with Reduce Transparency and Increase Contrast
- [ ] Media screens expose subtitle selection and respect system subtitle styles
- [ ] Supported generated/translated subtitle tracks are clearly identified and selectable
- [ ] Subtitle style preview is available during playback and remains accessible with VoiceOver and keyboard input
- [ ] New APIs are gated by documented OS/platform availability with authored-subtitle fallbacks
- [ ] Drag/drop, context menus, Siri/App Intents entry points, and generated actions expose purpose, value, actions, and feedback without touch-only interaction

---

## Instrumented Verification and Scope
- [ ] Accessibility Inspector checks the affected screens when a runnable app is available
- [ ] Compatible existing UI tests audit representative screen states where useful; false positives are investigated before filtering
- [ ] Automated results are supplemented with manual assistive-technology checks
- [ ] Results identify the OS/device, checks performed, and checks still pending
- [ ] App Store support declarations, when in scope, are backed by tested core tasks rather than one passing screen

## Assistive Access (when supported or requested)
- [ ] Essential tasks remain available in the tailored iOS/iPadOS experience
- [ ] The integration uses APIs appropriate to the framework and deployment target

## Final validation
- [ ] Screen is usable with VoiceOver enabled
- [ ] Screen works at extreme Dynamic Type sizes
- [ ] Screen remains operable with non-touch input where relevant
- [ ] No accessibility regressions introduced
