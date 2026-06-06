# Frugal AI Editor Workflow

Internal maintainer workflow. This file stays under `internal/` and is not published in the Frugal AI knowledge base.

Use this workflow when creating, reviewing, or revising public pages under `docs/`.

## Recommendation

Keep this workflow as a separate document from `internal/editorial-guide.md`.

The editorial guide defines voice, tone, terminology, and page patterns. The editor workflow defines the repeatable review process. Keeping them separate prevents the style guide from becoming a project-management checklist, while still allowing both documents to reference each other.

## Template Review Findings

The templates in `internal/templates/` are useful scaffolds, but the developed public docs are now more restrained than several templates.

Use the current docs as the stronger examples:

- Landing page: `docs/README.md`
- Guide: `docs/getting-started/offline-chat-service.md`
- Concept: `docs/concepts/frugal-ai-principles.md`
- Stack explanation: `docs/concepts/how-the-stack-fits-together.md`
- Component card: `docs/components/runtimes/ollama.md`
- Model card: `docs/components/models/qwen-3.5-9b.md`
- Runbook: `docs/operations/open-webui-ops.md`

Template risks to watch:

- `guide-template.md` is too thin. It misses fit and limits, component map, next step, and source confidence.
- `stack-template.md` is command-heavy and can encourage setup scripts before the reader understands the stack.
- `runtime-card-template.md` and `framework-card-template.md` include quick install commands that may duplicate guides.
- `model-card-template.md` includes performance tables that can invite unverified benchmark claims.
- `runbook-template.md` encourages exact commands, but the developed runbooks need shorter command blocks, verification, and recovery ownership.
- Several templates use second-person phrasing or placeholders that should be rewritten before publication.

The templates should be treated as outlines, not copy-ready page drafts.

## Editorial Workflow

### 1. Classify the Page

Decide the page type before drafting:

| Page type | Primary purpose | Use |
| --- | --- | --- |
| Landing page | Route readers into the Frugal AI knowledge base | `docs/README.md` pattern |
| Guide | Complete one practical task | guide pattern |
| Concept | Explain a decision or principle | concept pattern |
| Component card | Explain fit, limits, and links for one component | component pattern |
| Model card | Explain model identity, fit, and limits | model pattern |
| Runbook | Operate and recover a service | runbook pattern |
| Legacy stub | Preserve an old link while redirecting readers | short moved/retired page |

Do not add a public page only because source material exists. Add a page when it supports a guide, reader path, or operational need.

### 2. Define the Reader Job

Write one sentence that defines the page job:

```text
This page helps [reader role] decide/build/operate/verify [specific thing].
```

Use that sentence to keep the page focused. Remove sections that do not support the job.

### 3. Gather Source Material

Use source material in this order:

1. Existing public pages in `docs/`
2. Naming decisions in `internal/naming-registry.md`
3. Internal templates and planning notes in `internal/`
4. Official project documentation
5. COL Frugal AI sources
6. External reference docs for structure only

For facts that can change, verify against primary sources before publishing:

- model names, tags, sizes, licences, and context windows;
- install methods and command flags;
- hardware requirements and memory figures;
- product names and upstream URLs;
- security or data-governance claims.

Label values as measured, source-listed, expected, or estimated.

### 4. Choose the Pattern

Use the editorial guide page patterns as the source of truth.

Do not paste a template directly into `docs/`. Instead:

1. Copy the relevant heading pattern.
2. Remove placeholders.
3. Replace generic sections with page-specific reader tasks.
4. Keep only commands that are needed for the documented task.
5. Add verification before troubleshooting.

Template sections are optional. If a section has no useful content, no verified source, or only a statement that the information could not be found, leave the section out. Do not publish empty headings, placeholder rows, or "not available" filler.

### 5. Apply the Naming Gate

Before drafting, choose approved names from `internal/naming-registry.md`.

Check:

- site name: `Frugal AI knowledge base`;
- first guide name: `Local AI chat service`;
- operations page name: `Local AI chat service operations`;
- hardware name: `Mac mini 24 GB`;
- runtime name: `Ollama`;
- framework name: `Open WebUI`;
- model names exactly as listed in the registry.

Use service-level names for guides and operations pages. Use product names inside component pages and technical details.

### 6. Draft With the Frugal AI Voice

Draft rules:

- Use "Frugal AI knowledge base" for the site name.
- Avoid direct second person in public docs.
- Use British/Commonwealth spelling.
- Keep introductions grounded and short.
- Put the practical path before policy framing.
- Use education examples, not generic enterprise examples.
- Explain trade-offs without vendor-hostile language.
- State what is not covered.

Preferred sentence shape:

```text
The local service keeps prompts and chat history on the machine.
```

Avoid:

```text
You can keep your prompts and chat history on your machine.
```

### 7. Apply the Technical Writing Gate

Before review, check technical content:

- One command per shell block where possible.
- No long shell scripts on landing, concept, or component pages.
- No heredocs in public guides unless a maintained file would be worse.
- No local usernames, private paths, tokens, or machine-specific values.
- Every command has a purpose and a verification step.
- Custom code is avoided unless the page is explicitly about code.
- Wide tables are avoided when GitBook rendering is fragile.
- Markdown tables have matching header and separator columns.

For procedures, prefer this sequence:

1. Explain the step.
2. Show the command.
3. State expected output or verification.
4. Mention the common exception only if it is likely.

### 8. Review Page Structure

Check the page against its type.

Landing pages:

- grounded definition;
- first practical path;
- entry cards;
- reader-path table or list;
- stack map;
- proof points;
- scope boundaries;
- future paths clearly marked.

Guides:

- outcome;
- fit and limits;
- time and prerequisites;
- component map;
- steps;
- verification;
- troubleshooting;
- next step.

Component cards:

- what it is;
- when to use it;
- requirements;
- Frugal fit;
- compatibility;
- limits;
- verification or links.

Runbooks:

- scope;
- start and stop;
- health checks;
- maintenance;
- backup and recovery;
- troubleshooting;
- escalation notes.

### 9. Review Navigation

Before linking a page from `docs/SUMMARY.md`, confirm:

- the page supports the current local AI chat service path or a direct reader need;
- the title is short enough for the GitBook sidebar;
- the section does not create one-child nesting;
- legacy stubs remain unlinked unless they preserve existing URLs;
- internal files are not linked from public pages.

Use role labels in sidebar component titles when the page name alone is ambiguous:

```text
Hardware: Mac mini 24 GB
Environment: Development environment
Runtime: Ollama
Model: Qwen3.5-9B
Model: Qwen3.6-35B-A3B
Model: Gemma 4 12B
Framework: Open WebUI
```

### 10. Final Editorial Pass

Run the local editorial audit before publication:

```bash
python3 internal/tools/editorial_audit.py
```

Expected result:

```text
No editorial audit warnings.
```

Run this checklist:

- The first paragraph states the page purpose plainly.
- The site is called "Frugal AI knowledge base".
- Direct second person has been removed unless needed for safety.
- Claims about performance, memory, or compatibility are labelled.
- Empty or unverified template sections have been removed.
- The page distinguishes development, pilot, and production scope.
- Teacher-in-the-loop or human review is named where learner-facing AI is involved.
- Links point to existing files.
- GitBook tables and cards are syntactically valid.
- No internal files, planning notes, or templates are linked.
- Local editorial audit passes.

Useful local checks:

```bash
git diff --check
```

```bash
rg -n "\byou\b|\byour\b" docs
```

```bash
rg -n "^\\|" docs/README.md
```

### 11. Publish Decision

Use this decision rule:

| State | Action |
| --- | --- |
| Draft is internal, speculative, or planning-only | Keep under `internal/` |
| Draft is useful but not ready for navigation | Keep under `docs/` only if it preserves an old link; otherwise keep internal |
| Draft supports the current public path | Add or keep it in `docs/SUMMARY.md` |
| Draft introduces a new path | Add supporting components, safeguards, and operations first |

## Template Set

The templates in `internal/templates/` now reflect this workflow:

| Template | Use |
| --- | --- |
| `landing-page-template.md` | Public entry page for the Frugal AI knowledge base |
| `concept-page-template.md` | Principles, definitions, and decision framing |
| `guide-template.md` | One practical build or setup task |
| `stack-template.md` | Layer map and operating assumptions for a path |
| `hardware-profile-template.md` | Hardware fit, memory budget, and limits |
| `runtime-card-template.md` | Runtime fit, settings, compatibility, and limits |
| `model-card-template.md` | Model identity, source confidence, fit, and limits |
| `framework-card-template.md` | Interface or framework fit, requirements, and limits |
| `runbook-template.md` | Operation, health checks, maintenance, recovery, and escalation |

When a template and the editorial guide disagree, follow the editorial guide and update the template.

## Editor Roles

For lightweight edits, one editor can run the full workflow.

For high-risk pages, split review into three roles:

| Role | Focus |
| --- | --- |
| Technical reviewer | Commands, facts, compatibility, verification |
| Editorial reviewer | Voice, structure, spelling, reader path |
| Institutional reviewer | Data governance, teacher role, public-sector fit |

High-risk pages include production deployment, learner-facing AI, assessment, data ingestion, identity access, and any page making benchmark or compliance claims.
