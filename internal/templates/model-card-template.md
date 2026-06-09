# Model Card Template

Thin scaffold. The canonical structure is the live exemplar: `docs/components/models/qwen-3.5-9b.md`. Heading patterns are owned by `internal/editorial-guide.md` (Component Pages); when this file and the editorial guide disagree, follow the editorial guide and update this file.

## Heading pattern

```text
---
description: Model role in the Frugal AI knowledge base.
icon: gitbook-icon-name
---
# Model name                      (exact name from the naming registry)
_Layer:_ tag linking to the stack page, directly under the H1.
Intro: one short paragraph; state whether the model is used by a guide or is a candidate.
## At a glance
                                  (bold-label list: Current role / Best fit / Local fit / Model type / Inputs / Main caution)
## Good for
## Not suitable for
## Frugal fit
<details> Reference settings and Source confidence </details>
## Technical details              (model ID, runtime tag, source, licence)
## Limits
## Used by                        (omit for candidate models)
## Links
```

## Reminders

- Keep "At a glance" as a compact bold-label list, not a table; collapse reference settings and source-confidence tables into `<details>` so readable content leads.
- Label every figure as measured, source-listed, expected, or estimated; no benchmark values unless measured in the documented environment or clearly source-listed.
- Expand "Mixture of Experts" before using "MoE" on the first screen.
- Include an "Agentic readiness" line in At a glance: tool-calling support, its reliability caveat, and which guide exercises it (label claims as source-listed until measured).
- Use exact model IDs and runtime tags from the naming registry; note where a runtime tag differs from the model name.
- Leave out any section that would hold only placeholders or unverified claims.
