# Runtime Card Template

Thin scaffold for runtime and serving-engine cards. The canonical structure is the live exemplar: `docs/components/runtimes/ollama.md` (serving engine: `docs/components/runtimes/vllm.md`). Heading patterns are owned by `internal/editorial-guide.md` (Component Pages); when this file and the editorial guide disagree, follow the editorial guide and update this file.

## Heading pattern

```text
---
description: Runtime role in the Frugal AI knowledge base.
icon: gitbook-icon-name
---
# Runtime name
_Layer:_ tag linking to the stack page, directly under the H1.
Intro: what the runtime does and why it is in the path.
## At a glance
                                  (bold-label list: Current role / Best fit / Runs / Main caution)
## When to use it
## What it provides
## Requirements
## Frugal fit
## Compatibility                  (status labelled Tested / Untested / Expected)
## Limits
## Used by
## Links
```

## Reminders

- Full setup belongs in the relevant guide; a card carries at most a one-command stable quick reference.
- Use upstream default ports; register any host port a guide exposes in the naming registry.
- Distinguish local development runtimes from serving engines, and name which environment each fits.
- Label compatibility claims (Tested / Untested / Expected) rather than implying everything is verified.
