# SwiftUI Examples

These examples show how to use **swiftui-accessibility-auditor** with small, realistic SwiftUI snippets.
These are illustrative scenarios, not executed runtime tests. System-provided semantics must be checked before concluding that an explicit modifier is missing.

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

**Needs runtime verification**
- A system symbol may already supply a useful label. Inspect what VoiceOver announces; use the optional patch only if it does not describe the Save action. A missing explicit modifier alone does not justify P0.

**Conditional patch if the resolved label is unclear**
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

**P1**
- The custom row has only a tap gesture; expose a standard control with a predictable activation path. The snippet does not establish a core-task blocker, so P0 is not justified.

**Optional cleanup after inspecting announcements**
- If the decorative symbol introduces unrelated speech, hide it while preserving both text labels. Do not infer a duplicate announcement without checking the resolved element.

**Suggested replacement**
```swift
Button(action: openPlanDetails) {
    HStack(spacing: 12) {
        Image(systemName: "sparkles")
            .accessibilityHidden(true)
        VStack(alignment: .leading) {
            Text("Pro Plan")
            Text("Renews monthly")
                .font(.subheadline)
                .foregroundStyle(.secondary)
        }
    }
}
.buttonStyle(.plain)
```

The native button supplies its role and activation behavior. Verify that both labels are announced and that the replacement preserves the intended tap area and appearance.

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

**Needs runtime verification**
- `lineLimit(1)` can truncate a value in a constrained layout, but this snippet does not prove clipping. Verify the actual width and text size before assigning severity. Apply the conditional patch only if truncation is reproduced.

**Conditional patch after reproducing truncation**
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
Use the relevant checks in [the SwiftUI checklist](../skills/swiftui-accessibility-auditor/checklist.md).
- With VoiceOver enabled, navigate to Save and activate it: it announces its purpose and saves once.
- Navigate to the plan row: it announces both “Pro Plan” and “Renews monthly”; activation opens details once.
- At the largest accessibility text size, verify that the total remains fully readable; removing `lineLimit` alone may not solve a constrained layout.
- Use Voice Control and Switch Control on the changed controls; verify clear names, reachable actions, and one activation per request.
- With Keyboard navigation enabled on macOS, use Tab and Space to reach and activate the native plan button. Test Full Keyboard Access separately on iPadOS where applicable.

Regression risk: grouping or explicit labels can hide content/actions; changes to hit areas or text wrapping can affect layout. These are expected checks, not recorded test results.
