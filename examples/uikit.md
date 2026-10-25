# UIKit Examples

These examples show how to use **uikit-accessibility-auditor** with common UIKit patterns. They are illustrative scenarios, not executed runtime tests.

---

## Example 1 — Icon-only UIBarButtonItem

### Input

```swift
navigationItem.rightBarButtonItem = UIBarButtonItem(
    image: UIImage(systemName: "square.and.arrow.up"),
    style: .plain,
    target: self,
    action: #selector(share)
)
```

### Prompt

```text
Use the uikit-accessibility-auditor skill.
Audit this for VoiceOver discoverability and provide a patch-ready diff.
```

### Expected output (summary)

**Needs runtime verification**
- Inspect the resolved label first; native controls can provide semantics without an explicit assignment. If the Share action is not understandable, use the conditional patch. The snippet alone does not justify P0.

**Conditional patch if the resolved label is unclear**
```diff
 navigationItem.rightBarButtonItem = UIBarButtonItem(
     image: UIImage(systemName: "square.and.arrow.up"),
     style: .plain,
     target: self,
     action: #selector(share)
 )
+navigationItem.rightBarButtonItem?.accessibilityLabel = "Share"
```

---

## Example 2 — Group a table cell into a single element

### Input

```swift
titleLabel.text = "Invoice #0042"
subtitleLabel.text = "Due in 7 days"
amountLabel.text = "€320.00"
```

### Prompt

```text
Use the uikit-accessibility-auditor skill.
Audit this UITableViewCell for VoiceOver navigation. Suggest grouping and an accessible label/value.
```

### Expected output (summary)

**Optional improvement, subject to runtime verification**
- Multiple labels are not inherently a defect. If they represent one invoice and separate stops impede comprehension, consider the summary below. Inspect existing cell semantics and independent actions before replacing them.

**Suggested patch (for a summary cell without independently actionable children)**
```diff
+isAccessibilityElement = true
+accessibilityLabel = "Invoice number 42"
+accessibilityValue = "Due in 7 days. Amount €320.00"
+titleLabel.isAccessibilityElement = false
+subtitleLabel.isAccessibilityElement = false
+amountLabel.isAccessibilityElement = false
```

---

## Example 3 — Dynamic Type with custom font

### Input

```swift
titleLabel.font = UIFont(name: "AvenirNext-DemiBold", size: 16)
subtitleLabel.font = UIFont(name: "AvenirNext-Regular", size: 13)
```

### Prompt

```text
Use the uikit-accessibility-auditor skill.
Audit for Dynamic Type support and provide a minimal fix using UIFontMetrics.
```

### Expected output (summary)

**P1 if no scaling is configured elsewhere**
- The shown fonts are unscaled. Check the complete label configuration before concluding that the screen fails Dynamic Type; apply the patch if no existing scaling path is present.

**Suggested patch**
```diff
-titleLabel.font = UIFont(name: "AvenirNext-DemiBold", size: 16)
+titleLabel.font = UIFontMetrics(forTextStyle: .headline)
+    .scaledFont(for: UIFont(name: "AvenirNext-DemiBold", size: 16) ?? .preferredFont(forTextStyle: .headline))
+titleLabel.adjustsFontForContentSizeCategory = true

-subtitleLabel.font = UIFont(name: "AvenirNext-Regular", size: 13)
+subtitleLabel.font = UIFontMetrics(forTextStyle: .subheadline)
+    .scaledFont(for: UIFont(name: "AvenirNext-Regular", size: 13) ?? .preferredFont(forTextStyle: .subheadline))
+subtitleLabel.adjustsFontForContentSizeCategory = true
```

---

## Manual verification
Use the relevant checks in [the UIKit checklist](../skills/uikit-accessibility-auditor/checklist.md).
- With VoiceOver enabled, activate Share: it announces “Share” and opens the share flow once.
- Navigate to the invoice cell: its number, due date, and amount are available. If selection and reuse are part of the real cell implementation, check them separately; the summary patch does not implement those behaviors.
- At the largest Dynamic Type sizes, verify both custom-font labels grow without clipping essential content.
- Use Voice Control, Switch Control, and Full Keyboard Access to reach and activate changed controls.

Regression risk: grouping hides child elements. Keep independent controls reachable; only add the `.button` trait with `accessibilityTraits.insert(.button)` if the cell actually activates an action, and synchronize selection/disabled traits with its state. These are expected checks, not recorded test results.
