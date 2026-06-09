# Interface / Application Card Template

Thin scaffold for Application-layer component cards (interfaces, agents, and other applications). The canonical structure is the live exemplars: `docs/components/applications/open-webui.md` (Interface) and `docs/components/applications/opencode.md` (Agent). Heading patterns are owned by `internal/editorial-guide.md` (Component Pages); when this file and the editorial guide disagree, follow the editorial guide and update this file.

## Heading pattern

```text
---
description: Component role in the Frugal AI knowledge base.
icon: gitbook-icon-name
---
# Component name
_Layer:_ tag linking to the stack page, directly under the H1.
Intro: what it provides and which user experience it enables.
## At a glance
                                  (bold-label list: Current role / Best fit / Requires / Provider connection / Data location / Main caution)
## When to use it
## Requirements
## What it provides
## Frugal fit
## Compatibility
## Limits
## Used by
## Links
```

## Reminders

- Use the approved role prefix in the sidebar title (`Interface:`, `Agent:`) from the naming registry.
- For agents, state the three governance surfaces: local actions (review, scoped permissions), model egress through the gateway, and tool egress (tools and MCP servers allowlisted, no network access by default).
- Full setup belongs in the relevant guide; label untested deployment patterns as candidate until measured locally.
- State where application data is stored and what stays local.
