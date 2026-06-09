# Hardware Profile Template

Thin scaffold. The canonical structure is the live exemplar: `docs/components/hardware/mac-mini-24gb.md`. Heading patterns are owned by `internal/editorial-guide.md` (Component Pages); when this file and the editorial guide disagree, follow the editorial guide and update this file.

## Heading pattern

```text
---
description: Hardware role in the Frugal AI knowledge base.
icon: gitbook-icon-name
---
# Device name                     (from the naming registry, e.g. Mac mini 24 GB)
_Layer:_ tag linking to the stack page, directly under the H1.
Intro: one short paragraph; state whether this is a development, pilot, or production profile.
## At a glance
                                  (bold-label list: Current role / Best fit / Memory / CPU or chip / Environment fit / Main caution)
## When to use it
## Specifications
## Memory budget                  (allocation table with a Confidence column)
## What fits                      (model class / quantisation / context / fit, with confidence)
## Frugal fit
## Compatibility
## Limits
## Used by
```

## Reminders

- Every memory and fit figure carries a confidence label: measured, source-listed, or estimated; state the measurement method for measured values.
- Use `GB`, not `Gb`; first mention spells out the configuration ("Mac mini with 24 GB unified memory").
- Label planning values as estimates; what-fits rows are guidance, not guarantees.
- Untested hardware is a candidate profile until measured locally.
