# AppKit Examples

These examples show how to use **appkit-accessibility-auditor** with common AppKit patterns.

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

**P0**
- Button has no accessibility label.

**Suggested patch**
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

**P0**
- Not operable via keyboard (mouse-only).
- No accessibility role/label; not discoverable by VoiceOver.

**Suggested patch (outline)**
```diff
 final class ClickableCardView: NSView {
     var onActivate: (() -> Void)?

+    override var acceptsFirstResponder: Bool { true }
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

**P1**
- Row content is visually clear but not summarized for VoiceOver.

**Suggested approach**
- Expose the row (or primary cell) with:
  - Label: "Invoice number 42"
  - Value: "Due in 7 days. Amount €320.00"
- Ensure selection state is discoverable.

---

## Manual verification
- VoiceOver (macOS): reading order + roles
- Keyboard navigation: Tab/Shift-Tab, arrows in tables
- Focus ring visibility on interactive elements
