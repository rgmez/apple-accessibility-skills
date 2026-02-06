# SwiftUI Accessibility Checklist

This checklist is derived from Apple's official accessibility guidance and is intended for **manual verification** after applying changes suggested by the SwiftUI Accessibility Auditor.

Use VoiceOver, Dynamic Type, and keyboard navigation where applicable.

---

## VoiceOver & Semantics
- [ ] All icon-only buttons have a clear, meaningful label
- [ ] No duplicated announcements (parent + child announcing same text)
- [ ] Headers are correctly exposed as headers
- [ ] Related elements are grouped logically when appropriate
- [ ] Reading order matches the visual and logical layout

## Dynamic Type
- [ ] Text scales correctly up to the largest accessibility sizes
- [ ] Important information is not lost due to truncation
- [ ] Layout adapts naturally without relying on minimumScaleFactor
- [ ] No fixed font sizes block text scaling

## Focus & Keyboard Navigation (macOS / iPad)
- [ ] Screen is fully usable with keyboard only
- [ ] Focus order is predictable and logical
- [ ] Custom components can receive focus when needed
- [ ] Focus is not trapped or lost after interactions

## Color & Contrast
- [ ] Information is not conveyed by color alone
- [ ] States (error, selected, disabled) are understandable without color
- [ ] System or semantic colors are preferred where possible

## Touch Targets (iOS)
- [ ] Tappable elements are at least ~44x44 pt
- [ ] Hit areas are expanded without changing visual layout when needed

## Motion
- [ ] Animations are subtle and do not block interaction
- [ ] Reduce Motion preferences are respected where applicable

---

## Final validation
- [ ] Screen is usable with VoiceOver enabled
- [ ] Screen remains usable at extreme text sizes
- [ ] No new accessibility regressions introduced
