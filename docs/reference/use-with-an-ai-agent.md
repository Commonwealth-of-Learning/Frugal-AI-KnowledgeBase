---
description: "Machine-readable endpoints of the knowledge base — Markdown pages, the llms.txt index, and an MCP server — and how the coding agent uses them."
icon: robot
---

# Use the knowledge base with an AI agent

The Frugal AI knowledge base is written for people and for the agents that help maintain the stack. The [coding agent](../getting-started/coding-agent.md) is the builder's tool: a local team uses it to extend and maintain the components documented here, and it works best when it can read the same pages it is implementing.

## Machine-readable endpoints

The publishing platform generates machine-readable views of every published page automatically (see the platform's [LLM-ready docs guide](https://gitbook.com/docs/ai-and-search/llm-ready-docs)):

- every page is also served as plain Markdown — add `.md` to the page URL;
- `llms.txt` at the site root indexes the Markdown pages so agents can discover them;
- `llms-full.txt` carries the full site content in a single file for use as context;
- an MCP server exposes the published pages as resources for agents that speak the Model Context Protocol.

Confirm the endpoints on the published domain before relying on them: open `<site URL>/llms.txt` in a browser and check that the index lists the expected pages.

## Point the coding agent at the knowledge base

Two practical patterns, in frugal order:

1. **Offline and fully local** — clone the knowledge base repository next to the project and let the agent read the pages as files. No network access is needed, which suits the local-first default.
2. **Published site as context** — record the site's `llms.txt` URL in the project's `AGENTS.md` (see the [coding agent](../getting-started/coding-agent.md) guide) so the agent knows where to look up component pages, runbooks, and conventions when asked.

## Governance note

Fetching published pages over the network is tool egress: it does not pass the [gateway](../concepts/gateway-layer.md). Treat it like any other tool capability under the [Application layer](../concepts/application-layer.md) governance surfaces — allowlist the knowledge-base domain for the agent, and prefer the offline clone when the build should stay local.

## For maintainers

Each page's one-sentence `description` frontmatter doubles as its entry in the generated index, so a clear description serves the sidebar and agent retrieval at once.

## Related pages

- [Coding agent](../getting-started/coding-agent.md)
- [Application layer](../concepts/application-layer.md)
- [Orchestration layer](../concepts/orchestration-layer.md)
- [Glossary](glossary.md)
