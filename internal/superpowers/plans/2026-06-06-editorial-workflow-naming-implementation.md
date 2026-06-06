# Editorial Workflow Naming Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a lightweight naming and readability governance system for public Frugal AI knowledge base pages and internal templates.

**Architecture:** Add one Markdown naming registry as the source of truth, update editorial workflow and templates to reference it, rename the active public guide and operations labels, then add a conservative local audit script that reports drift without rewriting files. Keep file paths stable in this iteration to avoid breaking existing GitBook links.

**Tech Stack:** Markdown, GitBook `SUMMARY.md`, Python 3 standard library, shell checks with `rg` and `git diff --check`.

---

## Scope Check

The approved spec is one cohesive editorial-governance change, not multiple independent product subsystems. The implementation can proceed as one plan because each task produces a testable layer:

1. naming registry;
2. guide/workflow updates;
3. template updates;
4. active public naming changes;
5. local audit.

Legacy stub pages under `docs/` remain out of scope unless linked from `docs/SUMMARY.md`.

## File Structure

Create:

- `internal/naming-registry.md`  
  Source of truth for approved names, role labels, title patterns, and discouraged variants.

- `internal/tools/editorial_audit.py`  
  Conservative local audit for linked public docs and internal templates.

Modify:

- `internal/editorial-guide.md`  
  Add audience and naming guidance that references the registry.

- `internal/editor-workflow.md`  
  Add the naming/readability gate and audit command.

- `internal/templates/landing-page-template.md`  
  Use approved site, guide, and service names.

- `internal/templates/guide-template.md`  
  Make guide titles service/task-led and add naming-registry reminders.

- `internal/templates/runbook-template.md`  
  Use service-level operations naming.

- `internal/templates/hardware-profile-template.md`  
  Add `At a glance` and use `Mac mini 24 GB` style.

- `internal/templates/runtime-card-template.md`  
  Add `At a glance` and first-use role explanation pattern.

- `internal/templates/framework-card-template.md`  
  Add `At a glance` and first-use role explanation pattern.

- `internal/templates/model-card-template.md`  
  Keep the reader-first structure and align registry language.

- `docs/SUMMARY.md`  
  Change active navigation labels to approved forms.

- `docs/README.md`  
  Change first-path wording from offline-chat wording to `Local AI chat service`.

- `docs/getting-started/quickstart.md`  
  Change reader-facing path wording and remove direct second person.

- `docs/getting-started/offline-chat-service.md`  
  Keep the file path stable, but change H1 and visible page language to `Local AI chat service`.

- `docs/operations/open-webui-ops.md`  
  Keep the file path stable, but change H1 and visible page language to `Local AI chat service operations`.

- Active component pages under `docs/components/`  
  Add or adjust `At a glance` sections and approved hardware capitalization.

Do not rename files in this implementation. File renames can be considered after GitBook redirects and old links are handled.

---

### Task 1: Add Naming Registry

**Files:**
- Create: `internal/naming-registry.md`

- [ ] **Step 1: Create the naming registry**

Use `apply_patch` to add:

```markdown
# Frugal AI Naming Registry

Internal maintainer reference. This file is not published in the Frugal AI knowledge base.

Use this registry before creating or revising public pages under `docs/` and templates under `internal/templates/`.

## Audience

The Frugal AI knowledge base serves two audiences:

- education stakeholders who need purpose, risk, cost, governance, and institutional fit in plain language;
- developers and maintainers who need exact component names, model tags, settings, commands, and source links.

The first screen of a public page should work for stakeholders. Developer details can appear lower on the page.

## Site Name

| Use | Approved form |
| --- | --- |
| Published reader experience | Frugal AI knowledge base |

Avoid using `GitBook`, `docs`, `documentation site`, or casual variants when referring to the published reader experience. Use `GitBook` only when discussing the publishing platform or GitBook-specific syntax.

## Page Type Names

| Page type | Purpose |
| --- | --- |
| Landing page | Route readers into the Frugal AI knowledge base |
| Guide | Complete one practical task |
| Concept | Explain a decision, principle, or trade-off |
| Component card | Explain fit, limits, and links for one component |
| Model card | Explain model identity, practical fit, settings, and limits |
| Hardware card | Explain local hardware fit, memory budget, and limits |
| Runbook | Operate, maintain, and recover a service |
| Reference page | Define terms or collect source links |

## Service Names

| Use | Approved name | Avoid |
| --- | --- | --- |
| First build guide | Local AI chat service | Offline chat service |
| Operations page | Local AI chat service operations | Open WebUI operations |
| Future tool-using workflow | Institutional AI agent pilot | AI agent for the current chat-only path |

Reserve `AI agent` for future paths that include tool use, workflow actions, agent orchestration, or other agentic behaviour beyond local chat.

## Hardware Names

Hardware names should include memory only when memory is central to whether a documented path works.

Use `GB`, not `Gb`, for memory.

| Use | Approved name | First mention |
| --- | --- | --- |
| Current first path hardware | Mac mini 24 GB | Mac mini with 24 GB unified memory |
| Future higher-capability hardware | NVIDIA DGX Spark | NVIDIA DGX Spark |

Do not include memory in the DGX Spark title unless future pages distinguish multiple DGX Spark memory configurations.

## Component Names

| Component type | Approved name | First-use explanation |
| --- | --- | --- |
| Environment | Development environment | Development environment for local testing |
| Runtime | Ollama | Ollama, the local model runtime |
| Interface | Open WebUI | Open WebUI, the browser chat interface |
| Model | Qwen3.5-9B | Qwen3.5-9B, the first-path local model |
| Model | Qwen3.6-35B-A3B | Qwen3.6-35B-A3B, a future MoE evaluation model |
| Model | Gemma 4 12B | Gemma 4 12B, a future dense multimodal evaluation model |

## Navigation Labels

Use role prefixes for component pages in `docs/SUMMARY.md`:

- `Hardware: Mac mini 24 GB`
- `Environment: Development`
- `Runtime: Ollama`
- `Model: Qwen3.5-9B`
- `Model: Qwen3.6-35B-A3B`
- `Model: Gemma 4 12B`
- `Interface: Open WebUI`

Use reader-facing service names for guide and operations pages:

- `Local AI chat service`
- `Local AI chat service operations`

## Title Patterns

| Page type | Sidebar pattern | H1 pattern |
| --- | --- | --- |
| Guide | `Local AI chat service` | `Local AI chat service` |
| Operations | `Local AI chat service operations` | `Local AI chat service operations` |
| Hardware card | `Hardware: Mac mini 24 GB` | `Mac mini 24 GB` |
| Runtime card | `Runtime: Ollama` | `Ollama` |
| Model card | `Model: Qwen3.5-9B` | `Qwen3.5-9B` |
| Interface card | `Interface: Open WebUI` | `Open WebUI` |

## Reader-Friendly Explanations

| Term | First-use explanation |
| --- | --- |
| runtime | the software that runs the model |
| interface | the browser or application people use to chat with the model |
| open-weight model | a model whose weights are available for local use under a specific licence |
| Mixture of Experts | a model design that activates part of a larger model for each token |
| MoE | Use only after `Mixture of Experts` has been expanded |
| context window | the amount of text and other input the model can consider at once |
| multimodal | able to work with more than one input type, such as text and images |

## Discouraged Terms

| Avoid | Prefer |
| --- | --- |
| cheap AI | Frugal AI |
| fully cloudless | local-first |
| Open WebUI operations, as a public service title | Local AI chat service operations |
| Offline chat service, as the public guide title | Local AI chat service |
| Mac Mini | Mac mini |
| Mac mini 24Gb | Mac mini 24 GB |
| open models, when licence is unclear | open-weight models |
| replacing teachers | teacher-in-the-loop |
```

- [ ] **Step 2: Verify the registry is clean**

Run:

```bash
git diff --check -- internal/naming-registry.md
```

Expected: no output.

- [ ] **Step 3: Commit the registry**

Run:

```bash
git add internal/naming-registry.md
git commit -m "Add editorial naming registry"
```

Expected: commit succeeds.

---

### Task 2: Update Editorial Guide

**Files:**
- Modify: `internal/editorial-guide.md`

- [ ] **Step 1: Add registry and audience guidance**

Use `apply_patch` to add this paragraph after the existing sentence that points to `internal/editor-workflow.md`:

```markdown
For approved public names, sidebar labels, hardware names, service names, and reader-friendly term explanations, use `internal/naming-registry.md`.
```

Use `apply_patch` to add this section after `## Unified Knowledge Base Voice`:

```markdown
## Audience Model

Write for two audiences at once.

Education stakeholders need to understand purpose, risk, cost, governance, institutional fit, and the role of human oversight without reading commands.

Developers and maintainers need exact component names, model IDs, runtime tags, settings, commands, verification steps, and source links.

The first screen of a public page should answer the stakeholder question: what is this, why does it matter, and what are the limits? Developer details should remain available lower on the page.
```

Use `apply_patch` to add this subsection under `## Writing Rules` after the site-name rule:

```markdown
Use the naming registry before drafting or revising public pages. Service names, hardware names, model names, runtime names, interface names, and sidebar labels should match `internal/naming-registry.md`.

Prefer service-level names over tool-level names when naming guides and runbooks. Use `Local AI chat service` for the current first build guide and `Local AI chat service operations` for the operations page.

Use exact product names where precision matters: `Ollama`, `Open WebUI`, `Qwen3.5-9B`, `Qwen3.6-35B-A3B`, and `Gemma 4 12B`.

Explain unfamiliar technical terms on first use. Expand `Mixture of Experts` before using `MoE`, and explain `runtime`, `interface`, `context window`, and `open-weight model` when they first appear on a page for general readers.

Use `Mac mini 24 GB` for the current hardware card and `Mac mini with 24 GB unified memory` on first mention. Use `GB`, not `Gb`, for memory.
```

- [ ] **Step 2: Verify wording and formatting**

Run:

```bash
git diff --check -- internal/editorial-guide.md
```

Expected: no output.

- [ ] **Step 3: Commit the editorial-guide update**

Run:

```bash
git add internal/editorial-guide.md
git commit -m "Update editorial guide naming rules"
```

Expected: commit succeeds.

---

### Task 3: Update Editor Workflow

**Files:**
- Modify: `internal/editor-workflow.md`

- [ ] **Step 1: Add naming registry to source material**

In `### 3. Gather Source Material`, change the source order so `internal/naming-registry.md` is explicitly checked before templates:

```markdown
Use source material in this order:

1. Existing public pages in `docs/`
2. Naming decisions in `internal/naming-registry.md`
3. Internal templates and planning notes in `internal/`
4. Official project documentation
5. COL Frugal AI sources
6. External reference docs for structure only
```

- [ ] **Step 2: Add naming gate**

Add this new section after `### 4. Choose the Pattern`:

```markdown
### 5. Apply the Naming Gate

Before drafting, choose approved names from `internal/naming-registry.md`.

Check:

- site name: `Frugal AI knowledge base`;
- first guide name: `Local AI chat service`;
- operations page name: `Local AI chat service operations`;
- hardware name: `Mac mini 24 GB`;
- runtime name: `Ollama`;
- interface name: `Open WebUI`;
- model names exactly as listed in the registry.

Use service-level names for guides and operations pages. Use product names inside component pages and technical details.
```

Then renumber the following workflow headings by one where needed. Keep heading text otherwise unchanged.

- [ ] **Step 3: Add audit command**

In `Final Editorial Pass`, add:

```markdown
Run the local editorial audit before publication:

```bash
python3 internal/tools/editorial_audit.py
```

Expected result:

```text
No editorial audit warnings.
```
```

Add this checklist item:

```markdown
- Naming and readability audit passes.
```

- [ ] **Step 4: Verify workflow formatting**

Run:

```bash
git diff --check -- internal/editor-workflow.md
```

Expected: no output.

- [ ] **Step 5: Commit the workflow update**

Run:

```bash
git add internal/editor-workflow.md
git commit -m "Add naming gate to editor workflow"
```

Expected: commit succeeds.

---

### Task 4: Update Templates for Reader-First Naming

**Files:**
- Modify: `internal/templates/landing-page-template.md`
- Modify: `internal/templates/guide-template.md`
- Modify: `internal/templates/runbook-template.md`
- Modify: `internal/templates/hardware-profile-template.md`
- Modify: `internal/templates/runtime-card-template.md`
- Modify: `internal/templates/framework-card-template.md`
- Modify: `internal/templates/model-card-template.md`

- [ ] **Step 1: Update landing-page template names**

In `internal/templates/landing-page-template.md`, replace first-path references with:

```markdown
## Start here

Use [Local AI chat service](../getting-started/offline-chat-service.md) for the first build path.
```

Keep the page title as:

```markdown
# Welcome to Frugal AI Knowledge Base
```

- [ ] **Step 2: Update guide template**

In `internal/templates/guide-template.md`, add this sentence after the opening placeholder paragraph:

```markdown
Choose the guide title from `internal/naming-registry.md` when the guide belongs to an approved public path.
```

Use this example in the component map if an example is present:

```markdown
| Service | Local AI chat service |
```

- [ ] **Step 3: Update runbook template**

Change the H1 placeholder from:

```markdown
# [Service] operations
```

to:

```markdown
# [Service name] operations
```

Add this sentence after the opening paragraph:

```markdown
Use the service name from `internal/naming-registry.md`; do not use an implementation tool as the public runbook title when the page operates a broader service.
```

- [ ] **Step 4: Add `At a glance` to hardware template**

In `internal/templates/hardware-profile-template.md`, add this section after the introduction:

```markdown
## At a glance

| Question | Answer |
| --- | --- |
| Current role | [How this hardware is used in the Frugal AI knowledge base] |
| Best fit | [Plain-language workload fit] |
| Memory | [Use GB, not Gb] |
| Main caution | [Most important hardware limit] |
```

- [ ] **Step 5: Add `At a glance` to runtime template**

In `internal/templates/runtime-card-template.md`, add this section after the introduction:

```markdown
## At a glance

| Question | Answer |
| --- | --- |
| Current role | [How this runtime is used] |
| Best fit | [Plain-language fit] |
| Runs | [Local machine/server/device] |
| Main caution | [Most important runtime limit] |
```

- [ ] **Step 6: Add `At a glance` to framework template**

In `internal/templates/framework-card-template.md`, add this section after the introduction:

```markdown
## At a glance

| Question | Answer |
| --- | --- |
| Current role | [How this interface or framework is used] |
| Best fit | [Plain-language user workflow] |
| Requires | [Main dependency] |
| Main caution | [Most important interface or framework limit] |
```

- [ ] **Step 7: Align model template registry language**

In `internal/templates/model-card-template.md`, replace the second paragraph after the H1 with:

```markdown
Build from the top down: reader decision first, technical details later. Use `internal/naming-registry.md` for approved model, runtime, hardware, and service names. Leave out any section that would contain only placeholders, unverified claims, or a statement that the information is unavailable.
```

- [ ] **Step 8: Verify template checks**

Run:

```bash
git diff --check -- internal/templates
```

Expected: no output.

Run:

```bash
rg -n "Offline chat service|Open WebUI operations|Mac Mini|24Gb" internal/templates
```

Expected: no output.

- [ ] **Step 9: Commit template updates**

Run:

```bash
git add internal/templates
git commit -m "Align templates with naming registry"
```

Expected: commit succeeds.

---

### Task 5: Rename Active Public Guide and Operations Labels

**Files:**
- Modify: `docs/SUMMARY.md`
- Modify: `docs/README.md`
- Modify: `docs/getting-started/quickstart.md`
- Modify: `docs/getting-started/offline-chat-service.md`
- Modify: `docs/operations/open-webui-ops.md`
- Modify: `docs/components/hardware/mac-mini-24gb.md`
- Modify: `docs/components/runtimes/ollama.md`
- Modify: `docs/components/frameworks/open-webui.md`
- Modify: `docs/components/environments/development.md`

- [ ] **Step 1: Update navigation labels**

In `docs/SUMMARY.md`, change:

```markdown
* [Offline chat service](getting-started/offline-chat-service.md)
* [Hardware: Mac Mini 24 GB](components/hardware/mac-mini-24gb.md)
* [Open WebUI operations](operations/open-webui-ops.md)
```

to:

```markdown
* [Local AI chat service](getting-started/offline-chat-service.md)
* [Hardware: Mac mini 24 GB](components/hardware/mac-mini-24gb.md)
* [Local AI chat service operations](operations/open-webui-ops.md)
```

- [ ] **Step 2: Update guide title and description**

In `docs/getting-started/offline-chat-service.md`, change the frontmatter description to:

```yaml
description: Build a private local AI chat service with Ollama, Qwen3.5-9B, and Open WebUI.
```

Change the H1 to:

```markdown
# Local AI chat service
```

In the first paragraph, use:

```markdown
This guide builds a private local AI chat service with Ollama, Qwen3.5-9B, and Open WebUI. It is a development path for learning how the first Frugal AI stack works before pilot or production decisions are made.
```

- [ ] **Step 3: Update operations title and description**

In `docs/operations/open-webui-ops.md`, change the frontmatter description to:

```yaml
description: Operate, update, back up, and troubleshoot the local AI chat service.
```

Change the H1 to:

```markdown
# Local AI chat service operations
```

In the first paragraph, use:

```markdown
This runbook covers routine operation for the local AI chat service built with Open WebUI, Ollama, and the local model profile.
```

- [ ] **Step 4: Update landing-page and quickstart references**

In `docs/README.md` and `docs/getting-started/quickstart.md`, replace visible links and headings that say `Offline chat service` with `Local AI chat service`.

Replace direct second-person headings such as:

```markdown
## What you will build
```

with:

```markdown
## Build outcome
```

Use this sentence where needed:

```markdown
The first path builds a local AI chat service that runs on the documented development machine.
```

- [ ] **Step 5: Update hardware name**

In `docs/components/hardware/mac-mini-24gb.md`, change:

```markdown
# Mac Mini 24 GB
```

to:

```markdown
# Mac mini 24 GB
```

Use this first mention near the top:

```markdown
The current first path uses a Mac mini with 24 GB unified memory as the documented development machine.
```

- [ ] **Step 6: Add `At a glance` to active component pages**

Add an `At a glance` section near the top of each active component page that does not already have one:

- `docs/components/hardware/mac-mini-24gb.md`
- `docs/components/runtimes/ollama.md`
- `docs/components/frameworks/open-webui.md`
- `docs/components/environments/development.md`

Use this pattern and adapt values per page:

```markdown
## At a glance

| Question | Answer |
| --- | --- |
| Current role | [one plain-language sentence] |
| Best fit | [one plain-language sentence] |
| Main caution | [one plain-language sentence] |
```

For `docs/components/runtimes/ollama.md`, use:

```markdown
| Current role | Runs the local model for the first Frugal AI path. |
| Best fit | Local model testing and development on a single machine. |
| Main caution | Model size and context length still need to fit available memory. |
```

For `docs/components/frameworks/open-webui.md`, use:

```markdown
| Current role | Provides the browser chat interface for the local AI chat service. |
| Best fit | A familiar chat interface for local testing and demonstrations. |
| Main caution | It is an interface, not the full governance or production operations layer. |
```

For `docs/components/environments/development.md`, use:

```markdown
| Current role | Defines the assumptions for the local development path. |
| Best fit | Learning, testing, and small demonstrations before pilot decisions. |
| Main caution | Development defaults should not be treated as production settings. |
```

For `docs/components/hardware/mac-mini-24gb.md`, use:

```markdown
| Current role | Development hardware for the first local AI chat service path. |
| Best fit | Small local models, short guide contexts, and single-user testing. |
| Main caution | Larger models and long contexts can exceed available memory. |
```

- [ ] **Step 7: Verify public docs**

Run:

```bash
git diff --check -- docs
```

Expected: no output.

Run:

```bash
rg -n "Offline chat service|Open WebUI operations|Mac Mini|24Gb|\\byou\\b|\\byour\\b" docs/README.md docs/SUMMARY.md docs/getting-started docs/operations docs/components
```

Expected: no output.

- [ ] **Step 8: Commit public naming updates**

Run:

```bash
git add docs
git commit -m "Use service-level names in public docs"
```

Expected: commit succeeds.

---

### Task 6: Add Local Editorial Audit

**Files:**
- Create: `internal/tools/editorial_audit.py`
- Modify: `internal/editor-workflow.md`

- [ ] **Step 1: Create audit script**

Use `apply_patch` to add `internal/tools/editorial_audit.py`:

```python
#!/usr/bin/env python3
"""Conservative editorial audit for the Frugal AI knowledge base."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DOCS = ROOT / "docs"
SUMMARY = DOCS / "SUMMARY.md"
TEMPLATES = ROOT / "internal" / "templates"


SUMMARY_REQUIRED_LINES = [
    "* [Local AI chat service](getting-started/offline-chat-service.md)",
    "* [Hardware: Mac mini 24 GB](components/hardware/mac-mini-24gb.md)",
    "* [Environment: Development](components/environments/development.md)",
    "* [Runtime: Ollama](components/runtimes/ollama.md)",
    "* [Model: Qwen3.5-9B](components/models/qwen-3.5-9b.md)",
    "* [Model: Qwen3.6-35B-A3B](components/models/qwen-3.6-35b-a3b.md)",
    "* [Model: Gemma 4 12B](components/models/gemma-4-12b.md)",
    "* [Interface: Open WebUI](components/frameworks/open-webui.md)",
    "* [Local AI chat service operations](operations/open-webui-ops.md)",
]


PUBLIC_FORBIDDEN_PATTERNS = [
    (re.compile(r"\bOffline chat service\b"), "Use `Local AI chat service` for the active public guide title."),
    (re.compile(r"\bOpen WebUI operations\b"), "Use `Local AI chat service operations` for the active public operations title."),
    (re.compile(r"\bMac Mini\b"), "Use `Mac mini`."),
    (re.compile(r"\b24Gb\b|\b24GB\b"), "Use `24 GB` for memory."),
    (re.compile(r"\bGitBook\b"), "Use `Frugal AI knowledge base` unless discussing GitBook syntax or publishing internals."),
    (re.compile(r"\bdocumentation site\b|\bdocs site\b|\bthese docs\b|\bthis docs\b", re.IGNORECASE), "Use `Frugal AI knowledge base` for the reader-facing site."),
    (re.compile(r"\byou\b|\byour\b|\byours\b", re.IGNORECASE), "Avoid direct second person in public docs."),
    (re.compile(r"\bnot found\b|\bcannot be found\b|\bcould not be found\b|\bnot available\b", re.IGNORECASE), "Remove empty or unverifiable filler sections."),
]


PUBLIC_PLACEHOLDER_PATTERNS = [
    (
        re.compile(
            r"\[(?:value|model name|guide title|runtime tag|official source|file|url|source|component|service name)[^\]]*\]",
            re.IGNORECASE,
        ),
        "Remove placeholder bracket text from public pages.",
    ),
    (re.compile(r"\b(?:" + "|".join(("TB" + "D", "TO" + "DO")) + r")\b", re.IGNORECASE), "Remove unfinished placeholder text from public pages."),
]


TEMPLATE_FORBIDDEN_PATTERNS = [
    (re.compile(r"\bOffline chat service\b"), "Use `Local AI chat service` in templates."),
    (re.compile(r"\bOpen WebUI operations\b"), "Use `Local AI chat service operations` in templates when naming the service runbook."),
    (re.compile(r"\bMac Mini\b"), "Use `Mac mini`."),
    (re.compile(r"\b24Gb\b|\b24GB\b"), "Use `24 GB` for memory."),
    (re.compile(r"\byou\b|\byour\b|\byours\b", re.IGNORECASE), "Avoid direct second person in templates."),
]


TECHNICAL_ABBREVIATIONS = {
    "MoE": "Mixture of Experts",
    "GGUF": "GGUF",
    "KV cache": "KV cache",
    "RoPE": "RoPE",
}


def linked_public_docs() -> list[Path]:
    linked = {SUMMARY}
    summary_text = SUMMARY.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+\.md)\)", summary_text):
        if target.startswith(("http://", "https://", "/")):
            continue
        path = (DOCS / target).resolve()
        try:
            path.relative_to(DOCS.resolve())
        except ValueError:
            continue
        if path.exists():
            linked.add(path)
    return sorted(linked)


def template_docs() -> list[Path]:
    if not TEMPLATES.exists():
        return []
    return sorted(TEMPLATES.glob("*.md"))


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def add_pattern_warnings(warnings: list[str], path: Path, text: str, patterns: list[tuple[re.Pattern[str], str]]) -> None:
    for pattern, message in patterns:
        for match in pattern.finditer(text):
            warnings.append(f"{path.relative_to(ROOT)}:{line_number(text, match.start())}: {message}")


def has_heading(text: str, heading: str) -> bool:
    return re.search(rf"^## {re.escape(heading)}$", text, flags=re.MULTILINE) is not None


def first_body_block(text: str) -> str:
    without_frontmatter = re.sub(r"^---\n.*?\n---\n", "", text, flags=re.DOTALL)
    parts = re.split(r"\n## ", without_frontmatter, maxsplit=1)
    return parts[0]


def needs_at_a_glance(path: Path) -> bool:
    parts = path.parts
    return (
        "components" in parts
        and any(section in parts for section in ("hardware", "runtimes", "frameworks", "models", "environments"))
    )


def add_structure_warnings(warnings: list[str], path: Path, text: str) -> None:
    if path.suffix != ".md":
        return
    if path.is_relative_to(DOCS) and needs_at_a_glance(path) and not has_heading(text, "At a glance"):
        warnings.append(f"{path.relative_to(ROOT)}:1: Add an `At a glance` section near the top.")
    if path.is_relative_to(TEMPLATES):
        names_requiring_at_a_glance = (
            "model-card-template.md",
            "hardware-profile-template.md",
            "runtime-card-template.md",
            "framework-card-template.md",
        )
        if path.name in names_requiring_at_a_glance and not has_heading(text, "At a glance"):
            warnings.append(f"{path.relative_to(ROOT)}:1: Template should include an `At a glance` section.")


def add_first_screen_warnings(warnings: list[str], path: Path, text: str) -> None:
    if not path.is_relative_to(DOCS):
        return
    first = first_body_block(text)
    for abbreviation, expansion in TECHNICAL_ABBREVIATIONS.items():
        if abbreviation in first and expansion not in first:
            warnings.append(
                f"{path.relative_to(ROOT)}:1: Explain `{abbreviation}` before using it in the first screen."
            )


def add_summary_warnings(warnings: list[str]) -> None:
    text = SUMMARY.read_text(encoding="utf-8")
    for required in SUMMARY_REQUIRED_LINES:
        if required not in text:
            warnings.append(f"{SUMMARY.relative_to(ROOT)}:1: Missing required navigation label: {required}")


def main() -> int:
    warnings: list[str] = []
    add_summary_warnings(warnings)

    for path in linked_public_docs():
        text = path.read_text(encoding="utf-8")
        add_pattern_warnings(warnings, path, text, PUBLIC_FORBIDDEN_PATTERNS)
        add_pattern_warnings(warnings, path, text, PUBLIC_PLACEHOLDER_PATTERNS)
        add_structure_warnings(warnings, path, text)
        add_first_screen_warnings(warnings, path, text)

    for path in template_docs():
        text = path.read_text(encoding="utf-8")
        add_pattern_warnings(warnings, path, text, TEMPLATE_FORBIDDEN_PATTERNS)
        add_structure_warnings(warnings, path, text)

    if warnings:
        print("Editorial audit warnings:")
        for warning in warnings:
            print(f"- {warning}")
        return 1

    print("No editorial audit warnings.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 2: Run script syntax check**

Run:

```bash
python3 -m py_compile internal/tools/editorial_audit.py
```

Expected: no output.

- [ ] **Step 3: Verify audit passes after previous fixes**

Run:

```bash
python3 internal/tools/editorial_audit.py
```

Expected:

```text
No editorial audit warnings.
```

- [ ] **Step 4: Add audit command to workflow if not already present**

If Task 3 did not already add the command, add this to `internal/editor-workflow.md` under final checks:

```markdown
```bash
python3 internal/tools/editorial_audit.py
```
```

- [ ] **Step 5: Commit audit**

Run:

```bash
git add internal/tools/editorial_audit.py internal/editor-workflow.md
git commit -m "Add editorial audit"
```

Expected: commit succeeds.

---

### Task 7: Final Verification Pass

**Files:**
- Verify: all changed files

- [ ] **Step 1: Run whitespace check**

Run:

```bash
git diff --check HEAD~5..HEAD
```

Expected: no output.

- [ ] **Step 2: Run editorial audit**

Run:

```bash
python3 internal/tools/editorial_audit.py
```

Expected:

```text
No editorial audit warnings.
```

- [ ] **Step 3: Check direct second person in active public docs**

Run:

```bash
rg -n "\byou\b|\byour\b|\byours\b" docs/README.md docs/SUMMARY.md docs/getting-started docs/operations docs/components
```

Expected: no output.

- [ ] **Step 4: Check old naming**

Run:

```bash
rg -n "Offline chat service|Open WebUI operations|Mac Mini|24Gb|24GB" docs internal/templates internal/editorial-guide.md internal/editor-workflow.md internal/naming-registry.md
```

Expected output may include only intentional discouraged-term examples in `internal/naming-registry.md` and audit-rule examples in `internal/tools/editorial_audit.py`. If public docs or templates appear, fix them before continuing.

- [ ] **Step 5: Check worktree**

Run:

```bash
git status --short
```

Expected: no output.

---

## Spec Coverage Review

This plan covers every approved spec requirement:

- naming registry: Task 1;
- editorial guide update: Task 2;
- editor workflow update: Task 3;
- template update: Task 4;
- active public naming changes: Task 5;
- audit script: Task 6;
- audit and final verification: Task 7;
- internal plan location: this plan is saved under `internal/superpowers/plans/`.

## Implementation Notes

Do not rename `docs/getting-started/offline-chat-service.md` or `docs/operations/open-webui-ops.md` in this iteration. The visible page titles and navigation labels change, while file paths remain stable.

Use frequent commits as listed in the tasks. If a task reveals unrelated dirty changes, leave them untouched and commit only the files named in that task.
