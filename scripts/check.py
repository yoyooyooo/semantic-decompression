#!/usr/bin/env python3
"""Static checks for the semantic-decompression Skill package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []

EXPECTED = [
    "SKILL.md",
    "README.md",
    "README_EN.md",
    "VERSION",
    "CHANGELOG.md",
    "references/decompression-lenses.md",
    "references/multi-source-boundaries.md",
    "evals/evals.json",
    "evals/trigger-eval.json",
    "evals/multi-source-evals.json",
]

ACTIVE_TEXT_FILES = [
    ROOT / "SKILL.md",
    ROOT / "README.md",
    ROOT / "README_EN.md",
    ROOT / "references/decompression-lenses.md",
    ROOT / "references/multi-source-boundaries.md",
]


def fail(message: str) -> None:
    ERRORS.append(message)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except OSError as exc:
        fail(f"cannot read {path.relative_to(ROOT)}: {exc}")
        return ""


def check_expected_files() -> None:
    for relative in EXPECTED:
        if not (ROOT / relative).is_file():
            fail(f"missing required file: {relative}")
    if (ROOT / "references/repository-corpus-mode.md").exists():
        fail("stale reference still exists: references/repository-corpus-mode.md")
    if (ROOT / "evals/repository-evals.json").exists():
        fail("stale eval file still exists: evals/repository-evals.json")


def check_frontmatter() -> None:
    text = read(ROOT / "SKILL.md")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("SKILL.md has invalid YAML front matter delimiters")
        return
    frontmatter = match.group(1)
    if not re.search(r"(?m)^name:\s*semantic-decompression\s*$", frontmatter):
        fail("SKILL.md front matter has the wrong name")
    description_match = re.search(r"(?ms)^description:\s*>-\n((?:  .+\n?)+)", frontmatter)
    if not description_match:
        fail("SKILL.md front matter is missing a folded description")
    else:
        description = " ".join(line.strip() for line in description_match.group(1).splitlines())
        if not 120 <= len(description) <= 1024:
            fail(f"description length is outside 120..1024 characters: {len(description)}")


def iter_objects(value: Any):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from iter_objects(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_objects(child)


def check_json_and_file_references() -> None:
    for path in sorted((ROOT / "evals").rglob("*.json")):
        try:
            data = json.loads(read(path))
        except json.JSONDecodeError as exc:
            fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
            continue
        for obj in iter_objects(data):
            files = obj.get("files")
            if files is None:
                continue
            if not isinstance(files, list) or not all(isinstance(item, str) for item in files):
                fail(f"files must be a string list in {path.relative_to(ROOT)}")
                continue
            for relative in files:
                target = ROOT / relative
                if not target.is_file():
                    fail(f"missing eval file reference in {path.relative_to(ROOT)}: {relative}")


LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def check_markdown_links() -> None:
    for path in sorted(ROOT.rglob("*.md")):
        text = read(path)
        for raw_target in LINK_RE.findall(text):
            target = raw_target.strip().split("#", 1)[0]
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"link escapes package in {path.relative_to(ROOT)}: {raw_target}")
                continue
            if not resolved.exists():
                fail(f"broken relative link in {path.relative_to(ROOT)}: {raw_target}")


def check_bilingual_entry_links() -> None:
    if "[English](README_EN.md)" not in read(ROOT / "README.md"):
        fail("README.md is missing the English entry link")
    if "[中文](README.md)" not in read(ROOT / "README_EN.md"):
        fail("README_EN.md is missing the Chinese entry link")


def check_active_text() -> None:
    private_patterns = {
        "macOS user path": re.compile(r"/Users/[^/\s]+/"),
        "Linux user path": re.compile(r"/home/[^/\s]+/"),
        "Windows user path": re.compile(r"[A-Za-z]:\\\\Users\\\\"),
    }
    stale_terms = [
        "Repository and Corpus Mode",
        "Authority Ladder",
        "Term Registry",
        "Current-State Gate",
        "Coverage Contract",
    ]
    for path in ACTIVE_TEXT_FILES:
        text = read(path)
        if "—" in text or "–" in text:
            fail(f"dash character found in {path.relative_to(ROOT)}")
        for label, pattern in private_patterns.items():
            if pattern.search(text):
                fail(f"{label} found in {path.relative_to(ROOT)}")
        if path.name != "multi-source-boundaries.md":
            for term in stale_terms:
                if term in text:
                    fail(f"stale repository-mode term in {path.relative_to(ROOT)}: {term}")


def check_trigger_eval() -> None:
    path = ROOT / "evals/trigger-eval.json"
    try:
        data = json.loads(read(path))
    except json.JSONDecodeError:
        return
    if not isinstance(data, list):
        fail("trigger-eval.json must be an array")
        return
    positives = sum(item.get("should_trigger") is True for item in data if isinstance(item, dict))
    negatives = sum(item.get("should_trigger") is False for item in data if isinstance(item, dict))
    if positives < 8 or negatives < 8:
        fail(f"trigger eval needs at least 8 positives and 8 negatives, found {positives}/{negatives}")


def main() -> int:
    check_expected_files()
    check_frontmatter()
    check_json_and_file_references()
    check_markdown_links()
    check_bilingual_entry_links()
    check_active_text()
    check_trigger_eval()

    if ERRORS:
        for error in ERRORS:
            print(f"FAIL: {error}")
        print(f"checks: {len(ERRORS)} failure(s)")
        return 1

    json_count = len(list((ROOT / "evals").rglob("*.json")))
    markdown_count = len(list(ROOT.rglob("*.md")))
    print(f"checks: ok ({markdown_count} Markdown files, {json_count} JSON files)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
