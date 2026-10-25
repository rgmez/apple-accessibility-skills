# AppKit Examples

These examples show how to use **appkit-accessibility-auditor** with common AppKit patterns. They are illustrative scenarios, not executed runtime tests.

---

## Example 1 — Icon-only NSButton

### Input

```swift
let button = NSButton(
    image: NSImage(systemSymbolName: "gearshape", accessibilityDescription: nil)!,
    target: self,
    action: #selector(openSettings)
)
```

### Prompt

```text
Use the appkit-accessibility-auditor skill.
Audit this button for VoiceOver. Provide a patch-ready diff.
```

### Expected output (summary)

**Needs runtime verification**
- Inspect the resolved role and label before adding an override. If the Settings action is not understandable, apply the conditional patch; no essential-task blocker is demonstrated by this snippet.

**Conditional patch if the resolved label is unclear**
```diff
 let button = NSButton(
     image: NSImage(systemSymbolName: "gearshape", accessibilityDescription: nil)!,
     target: self,
     action: #selector(openSettings)
 )
+button.setAccessibilityLabel("Settings")
```

---

## Example 2 — Keyboard focus in a custom view

### Input

```swift
final class ClickableCardView: NSView {
    var onActivate: (() -> Void)?

    override func mouseDown(with event: NSEvent) {
        onActivate?()
    }
}
```

### Prompt

```text
Use the appkit-accessibility-auditor skill.
Audit this custom control for keyboard operability and VoiceOver role/label.
Suggest minimal changes without rewriting the component.
```

### Expected output (summary)

**P1**
- The shown custom view has mouse handling but no keyboard or accessibility activation path. Use P0 only if this blocks a demonstrated essential task.

The outline below adds semantics and activation only. It is not a complete keyboard-accessibility fix: the host must put the view in the key-view loop and provide a visible focus indicator.

**Suggested patch (outline)**
```diff
 final class ClickableCardView: NSView {
     var onActivate: (() -> Void)?

+    override var acceptsFirstResponder: Bool { true }
+    override func isAccessibilityElement() -> Bool { true }
+    override func keyDown(with event: NSEvent) {
+        switch event.keyCode {
+        case 36, 49: // Return, Space
+            onActivate?()
+        default:
+            super.keyDown(with: event)
+        }
+    }
+
+    override func accessibilityRole() -> NSAccessibility.Role? { .button }
+    override func accessibilityLabel() -> String? { "Open details" }
+    override func accessibilityPerformPress() -> Bool {
+        onActivate?()
+        return true
+    }

     override func mouseDown(with event: NSEvent) {
         onActivate?()
     }
 }
```

---

## Example 3 — Table row summary

### Input

```swift
// View-based NSTableView with a custom cell view that shows:
// Title: "Invoice #0042", Subtitle: "Due in 7 days", Amount: "€320.00"
```

### Prompt

```text
Use the appkit-accessibility-auditor skill.
Audit a view-based NSTableView row for VoiceOver comprehension. Suggest a concise accessible label/value strategy.
```

### Expected output (summary)

**Insufficient context for a confirmed finding**
- The input describes visible content but provides no accessibility implementation or runtime output. Inspect the row and cells before concluding that any data is missing or too fragmented.

**Conditional approach after inspecting the existing row**
- Expose the row (or primary cell) with:
  - Label: "Invoice number 42"
  - Value: "Due in 7 days. Amount €320.00"
- Ensure selection state is discoverable.

---

## Manual verification
Use the relevant checks in [the AppKit checklist](../skills/appkit-accessibility-auditor/checklist.md).
- With VoiceOver enabled, navigate to Settings and activate it: the purpose is announced and the settings flow opens once.
- Enable Keyboard navigation in macOS settings. For the partial card patch, verify Space/Return and VoiceOver activation each fire once. Key-view-loop integration and visible focus are pending requirements for the real host; do not report them as solved by this outline.
- Read invoice rows with VoiceOver and change selection with arrow keys: number, due date, amount, and selected state remain discoverable.
- Use Voice Control and Switch Control to reach changed controls and activate their exposed actions.

Regression risk: custom keyboard handling must preserve unhandled keys and disabled-state behavior. Grouping must not hide independent row controls. These are expected checks, not recorded test results.
