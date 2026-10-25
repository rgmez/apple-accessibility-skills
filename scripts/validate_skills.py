#!/usr/bin/env python3
"""Validate Agent Skills metadata and this repository's audit contract."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

import yaml

ALLOWED_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
SECTIONS = (
    "Role", "Inputs you can receive", "Non-goals", "Guardrails", "Audit checklist",
    "Output contract", "Verification protocol", "Style rules", "Example request",
    "References", "Version",
)
SEMVER = re.compile(r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)")


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject duplicate YAML keys instead of silently losing metadata."""


def unique_mapping(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str):
            raise ValueError("YAML mapping keys must be strings")
        if key in mapping:
            raise ValueError(f"Duplicate YAML key: {key}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def validate_skill(path: Path) -> list[str]:
    content = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.S)
    if not match:
        return ["Missing YAML frontmatter"]
    try:
        data = yaml.load(match.group(1), Loader=UniqueKeyLoader)
    except (yaml.YAMLError, ValueError) as error:
        return [f"Invalid YAML: {error}"]
    if not isinstance(data, dict):
        return ["Frontmatter must be a mapping"]
    errors = []
    unknown = set(data) - ALLOWED_FIELDS
    if unknown:
        errors.append(f"Unsupported top-level fields: {', '.join(sorted(unknown))}")
    name = data.get("name")
    if not isinstance(name, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append("Invalid skill name")
    elif name != path.parent.name:
        errors.append("Name must match the skill directory")
    description = data.get("description")
    if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
        errors.append("Description must be a nonempty string of at most 1024 characters")
    for field in ("compatibility", "license", "allowed-tools"):
        if field in data and (not isinstance(data[field], str) or not data[field].strip()):
            errors.append(f"{field} must be a nonempty string")
    if isinstance(data.get("compatibility"), str) and len(data["compatibility"]) > 500:
        errors.append("compatibility exceeds 500 characters")
    metadata = data.get("metadata")
    if not isinstance(metadata, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in metadata.items()):
        errors.append("Repository metadata must be a string-to-string mapping")
        metadata = {}
    version = metadata.get("version", "")
    if not SEMVER.fullmatch(version):
        errors.append("metadata.version must be a quoted major.minor.patch version")
    body = content[match.end():]
    headings = re.findall(r"^## (.+)$", body, re.M)
    missing = [section for section in SECTIONS if headings.count(section) != 1]
    if missing:
        errors.append(f"Required sections missing or duplicated: {', '.join(missing)}")
    elif [headings.index(s) for s in SECTIONS] != sorted(headings.index(s) for s in SECTIONS):
        errors.append("Required sections are out of order")
    footer = re.search(r"^## Version\s*\n+([^\n]+)\s*\Z", body, re.M)
    if not footer or footer.group(1).strip() != version:
        errors.append("Final Version section must match metadata.version")
    if not (path.parent / "checklist.md").is_file() or "[checklist.md](checklist.md)" not in body:
        errors.append("Missing skill-relative checklist reference or file")
    if re.search(r"\[TODO:", body):
        errors.append("Unfinished scaffold placeholder")
    return errors


def validate_repository(root: Path) -> list[str]:
    paths = sorted((root / "skills").glob("*/SKILL.md"))
    if not paths:
        return ["No skills found"]
    errors = []
    for path in paths:
        errors.extend(f"{path.relative_to(root)}: {error}" for error in validate_skill(path))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate_repository(args.root)
    if errors:
        print("\n".join(errors))
        return 1
    print("Skill metadata, audit contract, and versions are valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
