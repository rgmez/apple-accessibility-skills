# Apple Accessibility Skills

Accessibility audit skills for Apple platforms, designed for AI-assisted development tools
such as Cursor, Claude, Codex, and skills.sh-compatible agents.

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
- Prioritized findings (P0 / P1 / P2)
- Concrete, patch-ready code suggestions
- A short manual testing checklist

---

## Why this exists

Accessibility issues often surface when:
- responsibilities are implicit
- UI intent lives only in developers’ heads
- code reviews focus on visuals instead of semantics

When accessibility is treated as a first-class concern, these issues become visible early.

These skills are designed to:
- surface accessibility problems during everyday development
- provide clear, minimal fixes
- respect platform differences between iOS and macOS
- avoid unnecessary refactors or stylistic changes

---

## How to use the skills

These skills are intended to be used with AI agents that support external skill files.

Typical prompts look like:

> “Review this SwiftUI view for iOS and macOS accessibility.  
> Return prioritized findings and a patch-ready diff.”

> “Audit this AppKit screen using the AppKit Accessibility Auditor, focusing on VoiceOver roles and keyboard navigation.”

The agent will then apply the rules defined in the corresponding `SKILL.md` file.

---

## Install by environment

### Option A: skills.sh CLI

You can install these skills using the `skills` CLI (no global install required):

```bash
# Install a single skill
npx skills add rgmez/apple-accessibility-skills@swiftui-accessibility-auditor
npx skills add rgmez/apple-accessibility-skills@uikit-accessibility-auditor
npx skills add rgmez/apple-accessibility-skills@appkit-accessibility-auditor
```

Useful commands:

```bash
# List skills available in this repo
npx skills list rgmez/apple-accessibility-skills

# List installed skills
npx skills list

# Update installed skills
npx skills update
```

Telemetry: the CLI collects anonymous install telemetry by default. To opt out:

```bash
DISABLE_TELEMETRY=1 npx skills add rgmez/apple-accessibility-skills@swiftui-accessibility-auditor
```

### Option B: Cursor (manual local install)

1. Clone this repository locally.
2. Use the `skills/` folder as your skill source.
3. Ask Cursor to apply one platform skill at a time.

Suggested prompt:

> "Use the UIKit Accessibility Auditor on this screen and return P0/P1/P2 findings with patch-ready fixes."

### Option C: Claude / Codex (adapter-guided)

Use adapter docs for tool-specific framing:
- `docs/adapters/claude.md`
- `docs/adapters/codex.md`
- `docs/adapters/cursor.md`

Then route to the target skill through:
- `AGENTS.md`

---

## Verification after install

Run one smoke prompt and confirm response shape:

> "Audit this SwiftUI view for accessibility and return: P0/P1/P2 findings, patch-ready snippets, and manual checklist steps."

Expected:
- findings grouped by P0/P1/P2
- patch-ready edits
- verification steps referencing the platform checklist

---

## Repository structure

```
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
│   │   ├── SKILL.md
│   │   └── checklist.md
│   ├── uikit-accessibility-auditor/
│   │   ├── SKILL.md
│   │   └── checklist.md
│   └── appkit-accessibility-auditor/
│       ├── SKILL.md
│       └── checklist.md
└── examples/
```

### Structure rationale

- Each skill lives in its own folder, following the `skills.sh` discovery format
- `SKILL.md` defines role, guardrails, output contract, and verification protocol
- `checklist.md` provides human-facing, manual verification steps
- Checklists are not installable skills; they support the main skill
- `docs/skill-canonical-standard.md` keeps section and schema consistency across all skills
- `AGENTS.md` provides low-overhead routing to the right platform skill
- `examples/` is reserved for usage samples and real-world audits

---

## Design principles

- Accessibility is treated as a **design and engineering concern**, not a final checklist
- Every suggested change must have a clear justification
- Platform conventions are respected (SwiftUI ≠ UIKit ≠ AppKit)
- Changes should be minimal, localized, and safe

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

Repository process references:
- Contribution rules: `CONTRIBUTING.md`
- Changelog and release tracking: `CHANGELOG.md`
- Release workflow: `docs/releasing.md`

---

## License

MIT License.  
Use freely in personal, commercial, and open-source projects.
