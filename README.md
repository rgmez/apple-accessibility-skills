# Apple Accessibility Skills

Accessibility audit skills for Apple platforms, designed to be used with AI-assisted development tools such as Cursor or VS Code agents.

These skills focus on **reasoning about accessibility**, not blindly adding modifiers.
They are meant to make accessibility concerns explicit, reviewable, and intentional.

---

## What this repository contains

A small set of platform-specific accessibility auditor skills:

- **SwiftUI Accessibility Auditor**  
  For SwiftUI views on iOS, iPadOS, and macOS.

- **UIKit Accessibility Auditor**  
  For UIKit-based apps on iOS and iPadOS.

- **AppKit Accessibility Auditor**  
  For AppKit-based macOS applications.

Each skill audits UI code and returns:
- Prioritized findings (P0 / P1 / P2).
- Concrete, patch-ready code suggestions.
- A short manual testing checklist.

---

## Why this exists

Accessibility issues often surface when:
- responsibilities are implicit.
- UI intent lives only in developers’ heads.
- code reviews focus on visuals instead of semantics.

When accessibility is treated as a first-class concern, these issues become visible early.

These skills are designed to:
- surface accessibility problems during everyday development.
- provide clear, minimal fixes.
- respect platform differences between iOS and macOS.
- avoid unnecessary refactors or stylistic changes.

---

## How to use the skills

These skills are intended to be used with AI agents that support external skill files.

Typical prompts look like:

> "Review this SwiftUI view for iOS and macOS accessibility.  
> Return prioritized findings and a patch-ready diff."

> "Audit this AppKit screen using the AppKit Accessibility Auditor, focusing on VoiceOver roles and keyboard navigation."

The agent will then apply the rules defined in the corresponding `.skill.md` file.

---

## Repository structure

```
apple-accessibility-skills/
├── README.md
├── AGENTS.md
├── skills/
│   ├── swiftui-accessibility.skill.md
│   ├── uikit-accessibility.skill.md
│   ├── appkit-accessibility.skill.md
│   └── checklists/
│       ├── swiftui.md
│       ├── uikit.md
│       └── appkit.md
└── examples/
```

---

## Design principles

- Accessibility is treated as a **design and engineering concern**, not a final checklist.
- Every suggested change must have a clear justification.
- Platform conventions are respected (SwiftUI ≠ UIKit ≠ AppKit).
- Changes should be minimal, localized, and safe.

---

## Who this is for

- iOS and macOS developers
- Teams using AI-assisted code reviews
- Developers who want accessibility feedback without heavy tooling
- Anyone who prefers explicit intent over implicit assumptions

---

## References

The skills are based on Apple’s official accessibility guidance, including:

- Apple Human Interface Guidelines – Accessibility  
- SwiftUI, UIKit, and AppKit accessibility documentation

Specific references are listed inside each skill file.

---

## License

MIT License.  
Use freely in personal, commercial, and open-source projects.
