# Apple Accessibility Skills Router

Use this file to route quickly to the correct skill with minimal context loading.

## Use this when

- You need to choose the right accessibility auditor for a code task.

## Skip this when

- The framework is already clear and you are already inside the matching `SKILL.md`.

## Jump to

- SwiftUI files (`View`, modifiers, `@State`, `NavigationStack`) -> `skills/swiftui-accessibility-auditor/SKILL.md`
- UIKit files (`UIViewController`, `UIView`, table/collection cells) -> `skills/uikit-accessibility-auditor/SKILL.md`
- AppKit files (`NSView`, `NSViewController`, `NSTableView`, `NSOutlineView`) -> `skills/appkit-accessibility-auditor/SKILL.md`

## Routing rules

- Load one platform skill by default.
- Load multiple skills only for mixed-framework code paths.
- Keep requests framework-specific to reduce token usage.

## Quick request skeleton

"Use the <framework> Accessibility Auditor. Return P0/P1/P2 findings, patch-ready fixes, and manual verification steps."
