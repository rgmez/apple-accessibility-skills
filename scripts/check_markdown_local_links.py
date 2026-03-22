#!/usr/bin/env python3
"""
Validate local Markdown links.

Checks links in *.md files and fails if a relative/root-local target does not
exist in the repository. External URLs are ignored.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


LINK_RE = re.compile(r"!?\[[^\]]+\]\(([^)]+)\)")
FENCED_BLOCK_RE = re.compile(r"```[\s\S]*?```", re.MULTILINE)


def iter_markdown_files(root: Path):
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        yield path


def strip_code_blocks(content: str) -> str:
    return FENCED_BLOCK_RE.sub("", content)


def normalize_link_target(raw: str) -> str:
    target = raw.strip()

    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1]

    if " " in target and not target.startswith(("http://", "https://")):
        target = target.split(" ", 1)[0]

    target = target.split("#", 1)[0].split("?", 1)[0]
    return unquote(target)


def is_external(target: str) -> bool:
    return target.startswith(("http://", "https://", "mailto:", "tel:", "#")) or target == ""


def resolve_target(md_path: Path, target: str, repo_root: Path) -> Path:
    if target.startswith("/"):
        return (repo_root / target.lstrip("/")).resolve()
    return (md_path.parent / target).resolve()


def main() -> int:
    repo_root = Path.cwd().resolve()
    failures: list[str] = []

    for md in iter_markdown_files(repo_root):
        content = strip_code_blocks(md.read_text(encoding="utf-8"))
        for match in LINK_RE.finditer(content):
            raw_target = match.group(1)
            target = normalize_link_target(raw_target)

            if is_external(target):
                continue

            resolved = resolve_target(md, target, repo_root)
            if not resolved.exists():
                failures.append(
                    f"{md.relative_to(repo_root)} -> missing link target: {raw_target}"
                )

    if failures:
        print("Broken local markdown links found:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Local markdown links look good.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
