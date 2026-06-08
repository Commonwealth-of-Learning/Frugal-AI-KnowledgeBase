---
description: Open-source coding agent for the Application layer, governed by review and the gateway.
icon: robot
---

# OpenCode

_Layer: [Application](../../concepts/how-the-stack-fits-together.md) (agent)._

OpenCode is an open-source, terminal-first coding agent. In the Frugal AI knowledge base it is the first Application-layer agent: it reads, writes, and runs code locally, with model calls routed through the gateway.

## At a glance

- **Current role** — First coding-agent application in the knowledge base.
- **Best fit** — Developer and maintainer coding tasks on the local stack, under review.
- **Local fit** — Runs on the development machine; coding quality depends on the model and its memory.
- **Interface** — Routes model calls to any OpenAI-compatible endpoint, such as the gateway.
- **Main caution** — An agent with file and shell access; gate its actions and route egress through the gateway.

## When to use it

Use OpenCode for developer coding tasks where an agent that can read, edit, and run code saves time, and where a person reviews its changes. It is developer facing, not a learner-facing application.

## Requirements

- A local model through the gateway, or another OpenAI-compatible endpoint.
- A project directory to scope the agent to.
- Review of changes before they are kept.

## Frugal fit

| Factor | Fit |
| --- | --- |
| Local operation | Runs locally; model calls can stay on the machine through the gateway. |
| Resource use | Coding agents benefit from stronger models, which need more memory. |
| Replaceability | Works with any OpenAI-compatible model behind the gateway. |
| Governance | A built-in Plan mode and a permission system gate file and command actions. |

## Compatibility

- Local models through the [gateway](../gateways/litellm.md) or a local runtime.
- Controlled cloud burst for harder tasks, governed by the gateway.

## Limits

- File edits and shell commands are real side effects; run with review and scoped permissions.
- Coding quality on small local models is limited.
- Developer facing; not for learner-facing use without separate safeguards.

## Used by

Follow [Coding agent](../../getting-started/coding-agent.md) to run OpenCode on the local stack.

## Links

- [OpenCode documentation](https://opencode.ai/docs/)
- [OpenCode models and providers](https://opencode.ai/docs/models/)
- [OpenCode agents and permissions](https://opencode.ai/docs/permissions/)
