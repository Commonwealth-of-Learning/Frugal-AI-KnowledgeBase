# Editorial Workflow and Naming Consistency Design

## Purpose

This design improves the Frugal AI knowledge base editorial workflow so public pages and internal templates use consistent names, plain-language structure, and reader-friendly explanations for educational institution partners.

The target audience has two groups:

- education stakeholders who need to understand purpose, risk, cost, governance, and institutional fit;
- developers and maintainers who need exact component names, model tags, runtime settings, commands, and source links.

The first screen of each public page should be clear to stakeholders. Technical details should remain available lower on the page for developers.

## Scope

This design applies to:

- public pages under `docs/`;
- internal templates under `internal/templates/`;
- internal editorial guidance in `internal/editorial-guide.md`;
- internal workflow guidance in `internal/editor-workflow.md`;
- a new internal naming registry;
- a local editorial audit for names and basic readability signals.

Legacy stub pages under `docs/` remain out of scope unless they are linked from `docs/SUMMARY.md` or reused as active public content.

## Current Problems

The current workflow defines voice, page types, source confidence, and navigation checks, but naming consistency still depends on manual review.

Specific gaps:

- no single registry for approved names and discouraged variants;
- service names sometimes foreground tools rather than user outcomes;
- hardware names do not yet have a documented rule for including memory;
- component names are not automatically checked across public pages and templates;
- reader-friendliness is reviewed manually rather than checked consistently.

## Design Direction

Use a lightweight governance system:

1. Add `internal/naming-registry.md` as the source of truth for approved names.
2. Update `internal/editorial-guide.md` with audience and naming rules.
3. Update `internal/editor-workflow.md` with a naming and readability gate.
4. Update internal templates so they follow approved names and reader-first structure.
5. Add a local audit that reports naming and readability warnings with file paths and line numbers.

The registry defines terms. The workflow defines when editors check them. The audit makes drift visible.

## Naming Registry

The naming registry should be a plain Markdown file that editors can read without understanding scripts.

Required sections:

- audience;
- site name;
- page type names;
- navigation labels;
- approved service names;
- approved component names;
- hardware naming rules;
- model naming rules;
- runtime and interface naming rules;
- reader-friendly explanations for technical terms;
- discouraged terms and replacements;
- title and sidebar patterns.

### Approved Site Name

Use `Frugal AI knowledge base` in public-facing copy.

Avoid using `GitBook`, `docs`, `documentation site`, or casual variants when referring to the published reader experience. Use `GitBook` only when discussing the publishing platform or GitBook-specific syntax.

### Approved Service Names

Use service-level names for current public paths:

| Use | Approved name |
| --- | --- |
| First build guide | `Local AI chat service` |
| Operations page | `Local AI chat service operations` |

Avoid `Offline chat service` as the primary public name. It is narrower than the intended institutional use case.

Avoid `Open WebUI operations` as the primary public name. It foregrounds the tool rather than the service being operated.

Reserve `AI agent` for future paths that include tool use, workflow actions, agent orchestration, or other agentic behaviour beyond local chat.

### Approved Hardware Names

Hardware names should include memory only when memory is central to whether a documented path works.

Use `GB`, not `Gb`, for memory.

Approved names:

| Use | Approved name | First mention |
| --- | --- | --- |
| Current first path hardware | `Mac mini 24 GB` | `Mac mini with 24 GB unified memory` |
| Future higher-capability hardware | `NVIDIA DGX Spark` | `NVIDIA DGX Spark` |

Do not include memory in the DGX Spark title unless future pages distinguish multiple DGX Spark memory configurations.

### Approved Component Names

Use exact product and model names:

| Component type | Approved name |
| --- | --- |
| Runtime | `Ollama` |
| Interface | `Open WebUI` |
| Model | `Qwen3.5-9B` |
| Model | `Qwen3.6-35B-A3B` |
| Model | `Gemma 4 12B` |
| Environment | `Development environment` |

First use should explain the role when the term may be unfamiliar:

- `Ollama, the local model runtime`
- `Open WebUI, the browser chat interface`
- `Mixture of Experts`, with `MoE` only after expansion
- `open-weight model`, with licence details kept precise

### Navigation Label Patterns

`docs/SUMMARY.md` should use short labels with role prefixes when a component name alone is ambiguous:

- `Hardware: Mac mini 24 GB`
- `Environment: Development`
- `Runtime: Ollama`
- `Model: Qwen3.5-9B`
- `Model: Qwen3.6-35B-A3B`
- `Model: Gemma 4 12B`
- `Interface: Open WebUI`

Guides and operations pages should use reader-facing service names:

- `Local AI chat service`
- `Local AI chat service operations`

## Reader-Friendly Page Structure

Public pages should use progressive disclosure.

For stakeholders:

- page purpose appears in the first paragraph;
- practical fit appears before detailed commands or settings;
- limits and cautions are visible early;
- technical abbreviations are expanded on first use.

For developers:

- exact model IDs, runtime tags, settings, and source links remain available;
- commands stay in procedural guides and runbooks, not concept or landing pages;
- source confidence is clear for facts that can change.

Model, hardware, and component pages should prefer early sections such as:

- `At a glance`;
- `Good for`;
- `Not suitable for`;
- `Frugal fit`.

Technical details and source confidence tables should appear after these practical sections.

## Automated Audit

The audit should be a local command that reports warnings. It should not rewrite files automatically.

The first implementation can be a small script under an internal tools location, for example `internal/tools/editorial-audit.*`, with a documented command in the editor workflow.

The audit should check public docs and internal templates.

### Naming Checks

The audit should flag:

- inconsistent site names;
- public use of `GitBook`, `docs`, or `documentation site` when referring to the reader-facing site;
- `Gb` where `GB` is intended for memory;
- old service names such as `Offline chat service`;
- old operations names such as `Open WebUI operations` when the page is referring to the service;
- component names that differ from the registry;
- sidebar labels that do not follow approved patterns.

### Readability Checks

The audit should flag:

- direct second person in public docs;
- placeholder text such as `[value]`, `TBD`, or `TODO`;
- empty or unverifiable section language such as `not found`, `cannot be found`, or `not available`;
- missing `At a glance` sections on model, hardware, and component pages;
- over-technical first paragraphs where abbreviations such as `MoE`, `GGUF`, `KV cache`, or `RoPE` appear without explanation.

The audit should remain conservative. It should catch likely drift, not try to replace human editorial judgement.

## Editor Workflow Changes

Add a naming and readability gate before publication:

1. Classify the page type.
2. Choose approved names from `internal/naming-registry.md`.
3. Draft for two audiences: stakeholder first, developer second.
4. Use plain-language opening sections.
5. Run the local audit.
6. Apply human review:
   - stakeholder review for purpose, risk, governance, and institutional fit;
   - developer review for exact names, settings, commands, and source claims;
   - editorial review for voice, structure, and naming consistency.
7. Link the page from `docs/SUMMARY.md` only when it supports a current public path or a clearly marked future path.

## Template Changes

Templates should make the correct pattern easy to follow:

- replace `Offline chat service` examples with `Local AI chat service`;
- replace `Open WebUI operations` examples with `Local AI chat service operations` where the service is the user-facing subject;
- use `Mac mini 24 GB`, not `Mac Mini 24 GB` or `Mac mini 24Gb`;
- include `At a glance` in model, hardware, and component templates;
- keep commands out of landing, concept, and component templates unless the page type requires them;
- remind editors to remove unused or unverified sections.

## Success Criteria

The design is successful when:

- public navigation uses approved service, component, and hardware names;
- internal templates use the same naming system as public pages;
- the current guide and operations page use `Local AI chat service` naming;
- model and hardware pages can be understood from the first screen by readers with little technical background;
- developers can still find exact IDs, tags, settings, and sources lower on the page;
- a local audit reports naming and readability warnings before publication;
- legacy stub pages do not drive active naming unless they are linked or reused.

## Out Of Scope

This design does not:

- rewrite all public pages;
- create the audit implementation;
- decide future DGX Spark guide content;
- define production deployment policy;
- create a public-facing style guide.

Those changes belong in the implementation plan after this design is reviewed.

## Implementation Notes

The implementation should be incremental:

1. Add `internal/naming-registry.md`.
2. Update `internal/editorial-guide.md`.
3. Update `internal/editor-workflow.md`.
4. Update templates.
5. Rename active public guide and operations titles and navigation labels.
6. Add the local audit.
7. Run the audit and fix public docs and templates.

Use a focused commit sequence if the implementation becomes large.
