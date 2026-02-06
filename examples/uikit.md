# UIKit Examples

These examples show how to use **uikit-accessibility-auditor** with common UIKit patterns.

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

**P0**
- Icon-only bar button has no accessibility label.

**Suggested patch**
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

**P1**
- Multiple labels create too many VoiceOver stops; the cell should expose a concise summary.

**Suggested patch (typical approach)**
```diff
+isAccessibilityElement = true
+accessibilityTraits = [.button]
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

**P0**
- Fonts do not scale with content size category.

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
- VoiceOver: navigation order + announcements
- Dynamic Type: largest sizes
- Tap targets: comfortable hit areas
