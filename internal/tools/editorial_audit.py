#!/usr/bin/env python3
"""Local editorial audit for linked Frugal AI public docs."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


ROOT = Path.cwd()
DOCS_DIR = ROOT / "docs"
SUMMARY_PATH = DOCS_DIR / "SUMMARY.md"
TEMPLATES_DIR = ROOT / "internal" / "templates"

REQUIRED_SUMMARY_ENTRIES = (
    "* [Local AI chat service](getting-started/offline-chat-service.md)",
    "* [Local AI chat service operations](operations/open-webui-ops.md)",
    "* [Hardware: Mac mini 24 GB](components/hardware/mac-mini-24gb.md)",
    "* [Environment: Development environment](components/environments/development.md)",
    "* [Runtime: Ollama](components/runtimes/ollama.md)",
    "* [Model: Qwen3.5-9B](components/models/qwen-3.5-9b.md)",
    "* [Model: Qwen3.6-35B-A3B](components/models/qwen-3.6-35b-a3b.md)",
    "* [Model: Gemma 4 12B](components/models/gemma-4-12b.md)",
    "* [Framework: Open WebUI](components/frameworks/open-webui.md)",
)

COMPONENT_PARTS = {"hardware", "runtimes", "frameworks", "models", "environments"}

TEMPLATES_REQUIRING_AT_A_GLANCE = (
    "model-card-template.md",
    "hardware-profile-template.md",
    "runtime-card-template.md",
    "framework-card-template.md",
)

PLACEHOLDER_NAMES = (
    "value",
    "model name",
    "guide title",
    "runtime tag",
    "official source",
    "file",
    "url",
    "source",
    "component",
    "service name",
)


@dataclass(frozen=True)
class Warning:
    path: Path
    line: int
    message: str

    def format(self) -> str:
        return f"- {relative_path(self.path)}:{self.line}: {self.message}"


@dataclass(frozen=True)
class LinkedDoc:
    path: Path
    summary_line: int
    target: str


@dataclass(frozen=True)
class PatternCheck:
    regex: re.Pattern[str]
    message: str


PUBLIC_CHECKS = (
    PatternCheck(
        re.compile(r"\boffline chat service\b", re.IGNORECASE),
        'use "Local AI chat service" instead of "offline chat service"',
    ),
    PatternCheck(
        re.compile(r"\bOpen WebUI operations\b", re.IGNORECASE),
        'use "Local AI chat service operations" as the public service title',
    ),
    PatternCheck(re.compile(r"\bMac Mini\b"), 'use "Mac mini"'),
    PatternCheck(re.compile(r"\b24(?:Gb|GB)\b"), 'use "24 GB" for memory spelling'),
    PatternCheck(re.compile(r"\bGitBook\b"), 'use "Frugal AI knowledge base" for the public site name'),
    PatternCheck(
        re.compile(r"\b(?:you|your|yours)\b", re.IGNORECASE),
        "avoid direct second person in public docs",
    ),
    PatternCheck(
        re.compile(r"\b(?:not found|cannot be found|could not be found|not available)\b", re.IGNORECASE),
        "omit empty or unverifiable filler instead of publishing it",
    ),
    PatternCheck(
        re.compile(r"\[(?:" + "|".join(re.escape(name) for name in PLACEHOLDER_NAMES) + r")\]", re.IGNORECASE),
        "replace bracketed placeholder before publication",
    ),
    PatternCheck(re.compile(r"\b(?:TODO|TBD)\b", re.IGNORECASE), "replace TODO/TBD placeholder before publication"),
)

TEMPLATE_CHECKS = (
    PatternCheck(
        re.compile(r"\boffline chat service\b", re.IGNORECASE),
        'use "Local AI chat service" instead of "offline chat service"',
    ),
    PatternCheck(
        re.compile(r"\bOpen WebUI operations\b", re.IGNORECASE),
        'use "Local AI chat service operations" as the public service title',
    ),
    PatternCheck(re.compile(r"\bMac Mini\b"), 'use "Mac mini"'),
    PatternCheck(re.compile(r"\b24(?:Gb|GB)\b"), 'use "24 GB" for memory spelling'),
    PatternCheck(
        re.compile(r"\b(?:you|your|yours)\b", re.IGNORECASE),
        "avoid direct second person in templates",
    ),
)


def main() -> int:
    warnings: list[Warning] = []

    summary_text = read_text(SUMMARY_PATH)
    if summary_text is None:
        warnings.append(Warning(SUMMARY_PATH, 1, "docs/SUMMARY.md is required"))
        return print_result(warnings)

    warnings.extend(check_required_summary_entries(summary_text))

    linked_docs, link_warnings = discover_linked_docs(summary_text)
    warnings.extend(link_warnings)

    public_paths = [SUMMARY_PATH]
    seen = {SUMMARY_PATH.resolve()}
    for linked_doc in linked_docs:
        resolved = linked_doc.path.resolve()
        if resolved not in seen:
            seen.add(resolved)
            public_paths.append(linked_doc.path)

    for path in public_paths:
        text = read_text(path)
        if text is None:
            continue
        warnings.extend(scan_patterns(path, text, PUBLIC_CHECKS))
        warnings.extend(check_first_screen_abbreviations(path, text))
        if is_linked_component_page(path):
            warnings.extend(require_at_a_glance(path, text, "linked component page"))

    warnings.extend(check_templates())

    return print_result(warnings)


def read_text(path: Path) -> str | None:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def relative_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def check_required_summary_entries(summary_text: str) -> list[Warning]:
    warnings: list[Warning] = []
    stripped_lines = {line.strip() for line in summary_text.splitlines()}
    lines = summary_text.splitlines()

    for required_entry in REQUIRED_SUMMARY_ENTRIES:
        if required_entry in stripped_lines:
            continue

        target = required_entry.rsplit("(", 1)[1].rstrip(")")
        line_number = 1
        for index, line in enumerate(lines, start=1):
            if f"({target})" in line:
                line_number = index
                break
        warnings.append(Warning(SUMMARY_PATH, line_number, f"required summary entry missing: {required_entry}"))

    return warnings


def discover_linked_docs(summary_text: str) -> tuple[list[LinkedDoc], list[Warning]]:
    linked_docs: list[LinkedDoc] = []
    warnings: list[Warning] = []
    link_pattern = re.compile(r"\[[^\]]+\]\(([^)]+)\)")

    for line_number, line in enumerate(summary_text.splitlines(), start=1):
        for match in link_pattern.finditer(line):
            target = match.group(1).strip()
            if not target or is_external_or_anchor(target):
                continue
            target_path = clean_target(target)
            if not target_path.endswith(".md"):
                continue

            path = (DOCS_DIR / target_path).resolve()
            if not is_under(path, DOCS_DIR.resolve()):
                warnings.append(Warning(SUMMARY_PATH, line_number, f"linked path escapes docs/: {target}"))
                continue

            linked_path = Path(path)
            linked_docs.append(LinkedDoc(linked_path, line_number, target))
            if not linked_path.exists():
                warnings.append(Warning(SUMMARY_PATH, line_number, f"linked public doc does not exist: {target}"))

    return linked_docs, warnings


def is_external_or_anchor(target: str) -> bool:
    lowered = target.lower()
    return lowered.startswith(("http://", "https://", "mailto:", "#"))


def clean_target(target: str) -> str:
    target = target.split("#", 1)[0].split("?", 1)[0]
    return unquote(target)


def is_under(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
    except ValueError:
        return False
    return True


def scan_patterns(path: Path, text: str, checks: tuple[PatternCheck, ...]) -> list[Warning]:
    warnings: list[Warning] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        for check in checks:
            if check.regex.search(line):
                warnings.append(Warning(path, line_number, check.message))
    return warnings


def is_linked_component_page(path: Path) -> bool:
    try:
        relative = path.resolve().relative_to(DOCS_DIR.resolve())
    except ValueError:
        return False
    parts = relative.parts
    return len(parts) >= 3 and parts[0] == "components" and parts[1] in COMPONENT_PARTS


def require_at_a_glance(path: Path, text: str, label: str) -> list[Warning]:
    if re.search(r"^## At a glance\s*$", text, re.MULTILINE):
        return []
    return [Warning(path, 1, f'{label} must include "## At a glance"')]


def check_first_screen_abbreviations(path: Path, text: str) -> list[Warning]:
    first_block = first_visible_block(text)
    if "Mixture of Experts" in first_block:
        return []
    match = re.search(r"\bMoE\b", first_block)
    if not match:
        return []
    line_number = first_block[: match.start()].count("\n") + 1 + frontmatter_line_offset(text)
    return [
        Warning(
            path,
            line_number,
            'expand "MoE" as "Mixture of Experts" before using the abbreviation on the first screen',
        )
    ]


def first_visible_block(text: str) -> str:
    body = strip_frontmatter(text)
    lines: list[str] = []
    for line in body.splitlines():
        if line.startswith("## "):
            break
        lines.append(line)
    return "\n".join(lines)


def strip_frontmatter(text: str) -> str:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return text
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return "\n".join(lines[index + 1 :])
    return text


def frontmatter_line_offset(text: str) -> int:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return 0
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return index + 1
    return 0


def check_templates() -> list[Warning]:
    warnings: list[Warning] = []
    if not TEMPLATES_DIR.is_dir():
        return warnings

    for path in sorted(TEMPLATES_DIR.glob("*.md")):
        text = read_text(path)
        if text is None:
            continue
        warnings.extend(scan_patterns(path, text, TEMPLATE_CHECKS))

    for template_name in TEMPLATES_REQUIRING_AT_A_GLANCE:
        path = TEMPLATES_DIR / template_name
        text = read_text(path)
        if text is None:
            warnings.append(Warning(path, 1, 'template must include "## At a glance"'))
            continue
        warnings.extend(require_at_a_glance(path, text, "template"))

    return warnings


def print_result(warnings: list[Warning]) -> int:
    if not warnings:
        print("No editorial audit warnings.")
        return 0

    print("Editorial audit warnings:")
    for warning in sorted(warnings, key=lambda item: (relative_path(item.path), item.line, item.message)):
        print(warning.format())
    return 1


if __name__ == "__main__":
    sys.exit(main())
