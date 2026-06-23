# Apple Accessibility Skills

Most accessibility bugs are not caused by bad intentions.

They happen because semantics are implicit, review focus stays on visuals, and nobody writes down what must stay usable with assistive tech.

This repository gives you practical audit skills for Apple UI frameworks:

- SwiftUI
- UIKit
- AppKit

The goal is simple: find real issues early, propose minimal fixes, and keep behavior stable.

## Current coverage

The skills audit core Apple accessibility concerns and newer platform risks:

- VoiceOver, Voice Control, Switch Control, keyboard navigation, and Dynamic Type
- semantic labels, traits, grouping, reading order, state, and custom actions
- contrast, non-color cues, touch targets, motion preferences, and readable materials
- WWDC26 / SDK 2027 readiness for resizable layouts, iPhone Mirroring, Liquid Glass, media subtitles, clearer labels, and non-touch interaction paths

## Quick rules

- Prioritize user impact over stylistic preferences.
- Keep fixes minimal and localized.
- Do not change copy or layout unless accessibility requires it.
- Return findings by severity (`P0`, `P1`, `P2`).
- Always include manual verification steps.

## Quick Start (30s)

1. Pick the framework skill in `skills/`.
2. Run one audit request on a real screen.
3. Apply only `P0`/`P1` first.
4. Validate with the matching `checklist.md`.

## Non-goals

- Rewriting architecture.
- Re-styling UI for preference.
- Adding accessibility modifiers blindly.
- Replacing product decisions with generic best-practice advice.

## Before vs after

```swift
// Before (looks fine, fails in VoiceOver)
Button(action: onClose) {
    Image(systemName: "xmark")
}

// After (minimal and explicit)
Button(action: onClose) {
    Image(systemName: "xmark")
}
.accessibilityLabel("Close")
.accessibilityHint("Dismisses this screen")
```

## What this repository contains

- `skills/swiftui-accessibility-auditor/`
- `skills/uikit-accessibility-auditor/`
- `skills/appkit-accessibility-auditor/`
- platform checklists for manual verification
- review anti-patterns in `docs/review-red-flags.md`
- adapter docs under `docs/adapters/`
- canonical skill schema in `docs/skill-canonical-standard.md`

## Choose the right skill

- SwiftUI views and modifiers:
  - `skills/swiftui-accessibility-auditor/SKILL.md`
- UIKit screens and cells:
  - `skills/uikit-accessibility-auditor/SKILL.md`
- AppKit windows/views/tables:
  - `skills/appkit-accessibility-auditor/SKILL.md`

Routing helper:

- `AGENTS.md`

## Install by environment

### Option A: skills.sh CLI

```bash
npx skills add rgmez/apple-accessibility-skills@swiftui-accessibility-auditor
npx skills add rgmez/apple-accessibility-skills@uikit-accessibility-auditor
npx skills add rgmez/apple-accessibility-skills@appkit-accessibility-auditor
```

Useful commands:

```bash
npx skills list rgmez/apple-accessibility-skills
npx skills list
npx skills update
```

Telemetry opt-out example:

```bash
DISABLE_TELEMETRY=1 npx skills add rgmez/apple-accessibility-skills@swiftui-accessibility-auditor
```

### Option B: Cursor (manual local install)

1. Clone this repository locally.
2. Use `skills/` as your skill source.
3. Apply one platform skill per audit.

Suggested request text:

> "Audit this UIKit screen for accessibility. Return P0/P1/P2 findings, patch-ready changes, and manual verification steps."

### Option C: Claude / Codex (adapter-guided)

- `docs/adapters/claude.md`
- `docs/adapters/codex.md`
- `docs/adapters/cursor.md`

Then route through:

- `AGENTS.md`

## Verification after install

Run one smoke check:

> "Audit this SwiftUI view for accessibility and return P0/P1/P2 findings, patch-ready snippets, and a manual checklist."

Expected output:

- findings grouped by priority
- patch-ready edits
- clear manual verification steps

## Repository structure

```text
apple-accessibility-skills/
├── README.md
├── AGENTS.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── docs/
│   ├── skill-canonical-standard.md
│   ├── releasing.md
│   └── adapters/
├── skills/
│   ├── swiftui-accessibility-auditor/
│   ├── uikit-accessibility-auditor/
│   └── appkit-accessibility-auditor/
└── examples/
```

## Who this is for

- iOS and macOS developers
- teams that want accessibility reviewed in day-to-day work
- reviewers who want patch-ready guidance instead of generic advice

## References

- Apple Human Interface Guidelines – Accessibility
- SwiftUI accessibility docs
- UIKit accessibility docs
- AppKit accessibility docs

Process references:

- `CONTRIBUTING.md`
- `CHANGELOG.md`
- `docs/releasing.md`
- `docs/review-red-flags.md`

## License

MIT License.
See [LICENSE](LICENSE).
