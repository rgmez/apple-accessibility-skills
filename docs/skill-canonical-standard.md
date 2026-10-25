# Skill Canonical Standard

This document defines the required schema for every skill in this repository.

## Frontmatter Requirements

Each `SKILL.md` must include:

```yaml
---
name: <skill-name>
description: <what it does + when to use it>
metadata:
  version: "1.6.0"
  supported-runtimes: "cursor, claude, codex, skills.sh"
---
```

Notes:
- `name` must stay stable to avoid breaking installs.
- `description` should be concise and action-oriented.
- `metadata.version` is a quoted semantic version tracking behavior/output changes and matches the final Version section.
- `metadata` values must be strings. Runtime distribution information belongs here.
- Use optional `compatibility` only as a string for actual environment requirements, not a list of products.
- Follow the [Agent Skills specification](https://agentskills.io/specification); run `python3 scripts/validate_skills.py` with the development dependencies installed.

## Required Section Order

All skill files must use this order:

1. Role
2. Inputs you can receive
3. Non-goals
4. Guardrails
5. Audit checklist
6. Output contract
7. Verification protocol
8. Style rules
9. Example request
10. References
11. Version

## Guardrails (Mandatory)

- Prefer minimal, localized changes.
- Do not propose architecture rewrites unless blocker-level.
- Do not invent APIs.
- Do not modify user-facing copy unless accessibility requires it.
- Make assumptions explicit when context is missing.

## Output Contract (Mandatory)

Every response must include:

- Findings grouped by priority (`P0`, `P1`, `P2`)
- Patch-ready changes for confirmed findings only
- Manual verification checklist references

If no issue is demonstrated, state that explicitly and provide relevant pending checks without inventing a finding or patch. Separate insufficient context from confirmed defects. P0 requires a demonstrated essential-task blocker.

Each finding must include:
- location and supporting code/runtime evidence
- what is wrong
- why it matters
- exact fix

## Verification Protocol (Mandatory)

Each response must end with:
- concrete manual test steps
- expected accessibility outcomes
- explicit note on regression risk

Skill responses should reference the skill-relative `checklist.md` and select checks relevant to the finding. This is a validation reference, not a request to create files in the audited project. Distinguish performed checks from pending checks and code-level evidence from runtime evidence.
