# SwiftUI Examples

These examples show how to use **swiftui-accessibility-auditor** with small, realistic SwiftUI snippets.
Each example includes: input code, an agent prompt, and a patch-style suggestion.

---

## Example 1 — Icon-only button

### Input

```swift
Button(action: save) {
    Image(systemName: "tray.and.arrow.down")
}
```

### Prompt

```text
Use the swiftui-accessibility-auditor skill.
Audit this SwiftUI snippet for iOS + macOS accessibility and return P0/P1/P2 findings with a patch-ready diff.
```

### Expected output (summary)

**P0**
- Icon-only button has no meaningful accessibility label.

**Suggested patch**
```diff
 Button(action: save) {
-    Image(systemName: "tray.and.arrow.down")
+    Image(systemName: "tray.and.arrow.down")
+        .accessibilityLabel("Save")
 }
```

---

## Example 2 — Decorative image inside a card row

### Input

```swift
HStack(spacing: 12) {
    Image(systemName: "sparkles")
    VStack(alignment: .leading) {
        Text("Pro Plan")
        Text("Renews monthly")
            .font(.subheadline)
            .foregroundStyle(.secondary)
    }
}
.onTapGesture { openPlanDetails() }
```

### Prompt

```text
Use the swiftui-accessibility-auditor skill.
Audit this row for VoiceOver semantics and reading order. Provide a minimal patch.
```

### Expected output (summary)

**P0**
- The row is tappable but not exposed as a single actionable element, causing confusing VoiceOver navigation.

**P1**
- Decorative icon should be hidden from accessibility.

**Suggested patch**
```diff
 HStack(spacing: 12) {
-    Image(systemName: "sparkles")
+    Image(systemName: "sparkles")
+        .accessibilityHidden(true)
     VStack(alignment: .leading) {
         Text("Pro Plan")
         Text("Renews monthly")
             .font(.subheadline)
             .foregroundStyle(.secondary)
     }
 }
 .onTapGesture { openPlanDetails() }
+ .contentShape(Rectangle())
+ .accessibilityElement(children: .combine)
+ .accessibilityAddTraits(.isButton)
+ .accessibilityLabel("Pro Plan")
+ .accessibilityHint("Opens plan details")
```

---

## Example 3 — Dynamic Type resilience in a compact layout

### Input

```swift
HStack {
    Text("Total")
        .font(.headline)
    Spacer()
    Text("€1,234.56")
        .font(.headline)
        .lineLimit(1)
}
.padding(.horizontal, 16)
```

### Prompt

```text
Use the swiftui-accessibility-auditor skill.
Audit this layout for large Dynamic Type sizes. Suggest minimal changes to avoid losing meaning.
```

### Expected output (summary)

**P1**
- `lineLimit(1)` may truncate important values at large text sizes.

**Suggested patch**
```diff
 HStack {
     Text("Total")
         .font(.headline)
     Spacer()
     Text("€1,234.56")
         .font(.headline)
-        .lineLimit(1)
+        .multilineTextAlignment(.trailing)
 }
 .padding(.horizontal, 16)
```

---

## Manual verification
After applying changes, validate using:
- VoiceOver (iOS) / VoiceOver (macOS)
- Large Dynamic Type (AX sizes)
- Keyboard navigation on macOS (Tab/Shift-Tab where applicable)
