#!/usr/bin/env python3
"""Local editorial audit for linked Frugal AI public docs."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
DOCS_DIR = ROOT / "docs"
SUMMARY_PATH = DOCS_DIR / "SUMMARY.md"
TEMPLATES_DIR = ROOT / "internal" / "templates"
PLANS_DIR = ROOT / "internal" / "plans"
NAMING_REGISTRY_PATH = ROOT / "internal" / "naming-registry.md"

LAYER_SECTIONS = ("Infrastructure", "Inference", "Orchestration", "Gateway", "Application")
ALLOWED_ROLE_PREFIXES = (
    "Hardware",
    "Environment",
    "Runtime",
    "Serving engine",
    "Model",
    "Gateway",
    "Interface",
    "Agent",
    "Platform",
)

REQUIRED_SUMMARY_ENTRIES = (
    "* [Local AI chat service](getting-started/offline-chat-service.md)",
    "* [Math tutor](getting-started/math-tutor.md)",
    "* [Curriculum knowledge assistant](getting-started/curriculum-assistant.md)",
    "* [AI gateway](getting-started/ai-gateway.md)",
    "* [Coding agent](getting-started/coding-agent.md)",
    "* [Manim animator](getting-started/manim-animator.md)",
    "* [Operations overview](operations/operations-overview.md)",
    "* [Local AI chat service operations](operations/open-webui-ops.md)",
    "* [Hardware: Mac mini 24 GB](components/hardware/mac-mini-24gb.md)",
    "* [Hardware: NVIDIA DGX Spark](components/hardware/nvidia-dgx-spark.md)",
    "* [Environment: Development](components/environments/development.md)",
    "* [Environment: Pilot](components/environments/pilot.md)",
    "* [Environment: Production](components/environments/production.md)",
    "* [Runtime: Ollama](components/runtimes/ollama.md)",
    "* [Runtime: LM Studio](components/runtimes/lm-studio.md)",
    "* [Serving engine: vLLM](components/runtimes/vllm.md)",
    "* [Model: Qwen3.5-9B](components/models/qwen-3.5-9b.md)",
    "* [Model: Qwen3.6-35B-A3B](components/models/qwen-3.6-35b-a3b.md)",
    "* [Model: Gemma 4 12B](components/models/gemma-4-12b.md)",
    "* [Interface: Open WebUI](components/frameworks/open-webui.md)",
    "* [Gateway: LiteLLM](components/gateways/litellm.md)",
    "* [Platform: Dify](components/orchestration/dify.md)",
    "* [Agent: OpenCode](components/applications/opencode.md)",
)

COMPONENT_PARTS = {"hardware", "runtimes", "frameworks", "models", "environments", "gateways", "applications", "orchestration"}

TEMPLATES_REQUIRING_AT_A_GLANCE = (
    "model-card-template.md",
    "hardware-profile-template.md",
    "environment-profile-template.md",
    "runtime-card-template.md",
    "framework-card-template.md",
)

PLACEHOLDER_CUE_WORDS = (
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
    "fit",
    "out-of-scope",
    "requirement",
    "setting",
    "claim",
    "limit",
    "example",
    "title",
    "path",
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


@dataclass(frozen=True)
class SourceLine:
    number: int
    text: str


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
    PatternCheck(
        re.compile(r"\b(?:you|your|yours)\b", re.IGNORECASE),
        "avoid direct second person in public docs",
    ),
    PatternCheck(
        re.compile(r"\b(?:not found|cannot be found|could not be found|not available)\b", re.IGNORECASE),
        "omit empty or unverifiable filler instead of publishing it",
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
    PatternCheck(re.compile(r"\bFrugal AI Knowledge Base\b"), 'use "Frugal AI knowledge base" for the site name'),
    PatternCheck(
        re.compile(r"\b(?:GitBook(?!-icon-name)|documentation site|docs site|these docs|this docs)\b", re.IGNORECASE),
        'use "Frugal AI knowledge base" for the site name',
    ),
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
    warnings.extend(check_summary_structure(summary_text))

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
        warnings.extend(check_public_site_names(path, text))
        warnings.extend(scan_public_placeholders(path, text))
        warnings.extend(check_first_screen_abbreviations(path, text))
        warnings.extend(check_frontmatter(path, text))
        if is_linked_component_page(path):
            warnings.extend(require_at_a_glance(path, text, "linked component page"))

    warnings.extend(check_templates())
    warnings.extend(check_internal_plans())
    warnings.extend(check_port_allocations())

    return print_result(warnings)


def check_frontmatter(path: Path, text: str) -> list[Warning]:
    """Flag YAML frontmatter that will fail to parse at build time.

    The common breakage is an unquoted scalar value containing a colon-space
    (or a trailing colon), which YAML reads as a nested mapping. This check is
    intentionally stdlib-only and does not import a YAML library.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return []

    closing = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            closing = index
            break
    if closing is None:
        return [Warning(path, 1, "frontmatter opening --- has no closing ---")]

    warnings: list[Warning] = []
    for index in range(1, closing):
        line = lines[index]
        if not line.strip() or line[0] in (" ", "\t"):
            continue  # blank line or block-scalar continuation
        match = re.match(r"^([A-Za-z0-9_.-]+):(?:\s+(.*))?$", line)
        if not match:
            continue
        value = (match.group(2) or "").strip()
        if value in ("", "|", ">", "|-", ">-", "|+", ">+"):
            continue  # empty value or block-scalar indicator
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
            continue  # already quoted
        if ": " in value or value.endswith(":"):
            warnings.append(
                Warning(
                    path,
                    index + 1,
                    f'frontmatter value for "{match.group(1)}" contains a colon; '
                    "quote the value or remove the colon",
                )
            )
    return warnings


def check_internal_plans() -> list[Warning]:
    """Validate frontmatter of internal plan files, which downstream tooling parses."""
    warnings: list[Warning] = []
    if not PLANS_DIR.is_dir():
        return warnings
    for path in sorted(PLANS_DIR.glob("*.md")):
        text = read_text(path)
        if text is not None:
            warnings.extend(check_frontmatter(path, text))
    return warnings


def check_summary_structure(summary_text: str) -> list[Warning]:
    """Enforce the layered navigation: expected layer sections and approved role prefixes."""
    warnings: list[Warning] = []
    lines = summary_text.splitlines()
    headers = {line[3:].strip() for line in lines if line.startswith("## ")}
    for layer in LAYER_SECTIONS:
        if layer not in headers:
            warnings.append(Warning(SUMMARY_PATH, 1, f"missing expected layer section: ## {layer}"))

    link_pattern = re.compile(r"^\*\s*\[([^\]]+)\]\(([^)]+)\)")
    for line_number, line in enumerate(lines, start=1):
        match = link_pattern.match(line.strip())
        if not match:
            continue
        label, target = match.group(1), match.group(2).strip()
        if not target.startswith("components/"):
            continue
        prefix = label.split(":", 1)[0].strip() if ":" in label else label
        if prefix not in ALLOWED_ROLE_PREFIXES:
            warnings.append(
                Warning(
                    SUMMARY_PATH,
                    line_number,
                    f'component entry "{label}" should start with an approved role prefix: '
                    + ", ".join(ALLOWED_ROLE_PREFIXES),
                )
            )
    return warnings


def check_port_allocations() -> list[Warning]:
    """Prevent host-port collisions: registry duplicates, and guide bindings missing from the registry."""
    warnings: list[Warning] = []
    registered: dict[str, str] = {}
    registry_text = read_text(NAMING_REGISTRY_PATH)
    if registry_text is not None:
        in_section = False
        for line in registry_text.splitlines():
            stripped = line.strip()
            if stripped.startswith("## "):
                in_section = stripped.lower() == "## port allocations"
                continue
            if not in_section:
                continue
            match = re.match(r"\|\s*(\d{2,5})\s*\|\s*([^|]+?)\s*\|", line)
            if match:
                port, service = match.group(1), match.group(2).strip()
                if port in registered:
                    warnings.append(
                        Warning(
                            NAMING_REGISTRY_PATH,
                            1,
                            f"duplicate host port {port} in Port Allocations: {registered[port]} and {service}",
                        )
                    )
                else:
                    registered[port] = service

    binding = re.compile(r"-p\s+(?:\d{1,3}(?:\.\d{1,3}){3}:)?(\d{2,5}):\d{2,5}")
    for path in sorted(DOCS_DIR.rglob("*.md")):
        text = read_text(path)
        if text is None:
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            for match in binding.finditer(line):
                host_port = match.group(1)
                if host_port not in registered:
                    warnings.append(
                        Warning(
                            path,
                            line_number,
                            f"host port {host_port} is bound in a guide but is not in the Port Allocations registry (internal/naming-registry.md)",
                        )
                    )
    return warnings


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


def check_public_site_names(path: Path, text: str) -> list[Warning]:
    warnings: list[Warning] = []
    patterns = (
        re.compile(r"\bFrugal AI Knowledge Base\b"),
        re.compile(r"\b(?:GitBook(?!-icon-name)|documentation site|docs site|these docs|this docs)\b", re.IGNORECASE),
    )

    for line_number, line in enumerate(text.splitlines(), start=1):
        if is_allowed_landing_title(path, line):
            continue
        if any(pattern.search(line) for pattern in patterns):
            warnings.append(Warning(path, line_number, 'use "Frugal AI knowledge base" for the public site name'))

    return warnings


def is_allowed_landing_title(path: Path, line: str) -> bool:
    return path.resolve() == (DOCS_DIR / "README.md").resolve() and line.strip() == "# Welcome to Frugal AI Knowledge Base"


def scan_public_placeholders(path: Path, text: str) -> list[Warning]:
    warnings: list[Warning] = []
    reference_labels = collect_reference_labels(text)

    for line_number, line in enumerate(text.splitlines(), start=1):
        for placeholder in bracketed_placeholder_candidates(line, reference_labels):
            warnings.append(
                Warning(path, line_number, f"replace bracketed placeholder before publication: [{placeholder}]")
            )

    return warnings


def collect_reference_labels(text: str) -> set[str]:
    labels: set[str] = set()

    for line in text.splitlines():
        match = re.match(r"^[ \t]{0,3}\[([^\[\]\n]+)\]:", line)
        if match:
            labels.add(normalize_reference_label(match.group(1)))

    return labels


def bracketed_placeholder_candidates(line: str, reference_labels: set[str] | None = None) -> list[str]:
    candidates: list[str] = []
    reference_labels = reference_labels or set()

    for match in re.finditer(r"\[([^\[\]\n]+)\]", line):
        if is_markdown_link_or_image(line, match, reference_labels):
            continue

        content = match.group(1).strip()
        if is_placeholder_content(content):
            candidates.append(content)

    return candidates


def is_markdown_link_or_image(line: str, match: re.Match[str], reference_labels: set[str]) -> bool:
    if match.start() > 0 and line[match.start() - 1] == "!":
        return True

    next_char_index = match.end()
    if next_char_index < len(line) and line[next_char_index] in "([":
        return True

    if next_char_index < len(line) and line[next_char_index] == ":" and is_reference_definition(line, match):
        return True

    if match.start() > 0 and line[match.start() - 1] == "]":
        return True

    return normalize_reference_label(match.group(1)) in reference_labels


def is_reference_definition(line: str, match: re.Match[str]) -> bool:
    return re.match(r"^[ \t]{0,3}\[[^\[\]\n]+\]:", line[: match.end() + 1]) is not None


def normalize_reference_label(label: str) -> str:
    return re.sub(r"\s+", " ", label.strip().lower())


def is_placeholder_content(content: str) -> bool:
    normalized = re.sub(r"[\s_]+", " ", content.strip().lower())
    normalized = re.sub(r"\s*-\s*", "-", normalized)

    return any(has_placeholder_cue(normalized, cue) for cue in PLACEHOLDER_CUE_WORDS)


def has_placeholder_cue(normalized_content: str, cue: str) -> bool:
    normalized_cue = re.sub(r"\s*-\s*", "-", cue.lower())
    pattern = r"(?<![a-z0-9])" + re.escape(normalized_cue) + r"(?![a-z0-9])"
    return re.search(pattern, normalized_content) is not None


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
    expansion_seen = False
    for source_line in first_screen_lines(text):
        events = []
        events.extend((match.start(), "expansion") for match in re.finditer(r"Mixture of Experts", source_line.text))
        events.extend((match.start(), "abbreviation") for match in re.finditer(r"\bMoE\b", source_line.text))

        for _position, event_type in sorted(events):
            if event_type == "expansion":
                expansion_seen = True
            elif not expansion_seen:
                return [
                    Warning(
                        path,
                        source_line.number,
                        'expand "MoE" as "Mixture of Experts" before using the abbreviation on the first screen',
                    )
                ]

    return []


def first_screen_lines(text: str) -> list[SourceLine]:
    lines = text.splitlines()
    first_screen: list[SourceLine] = []
    body_start = 0

    if lines and lines[0].strip() == "---":
        for index in range(1, len(lines)):
            if lines[index].strip() == "---":
                first_screen.extend(frontmatter_description_lines(lines[1:index], start_line=2))
                body_start = index + 1
                break

    for index in range(body_start, len(lines)):
        line = lines[index]
        if line.startswith("## "):
            break
        first_screen.append(SourceLine(index + 1, line))

    return first_screen


def frontmatter_description_lines(lines: list[str], start_line: int) -> list[SourceLine]:
    description_lines: list[SourceLine] = []
    in_description_block = False

    for offset, line in enumerate(lines):
        line_number = start_line + offset
        stripped = line.strip()

        if in_description_block:
            if line.startswith((" ", "\t")) and stripped:
                description_lines.append(SourceLine(line_number, stripped))
                continue
            in_description_block = False

        match = re.match(r"^description:\s*(.*)$", line)
        if not match:
            continue

        value = match.group(1).strip()
        if value in {"|", ">", "|-", ">-", "|+", ">+"}:
            in_description_block = True
        elif value:
            description_lines.append(SourceLine(line_number, strip_matching_quotes(value)))

    return description_lines


def strip_matching_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    return value


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
