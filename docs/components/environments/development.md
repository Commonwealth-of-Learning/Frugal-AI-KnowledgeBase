---
description: Assumptions for the local development path.
icon: flask
---

# Development environment

The development environment is a local, single-user setup for learning, testing, and demonstration. It is not a shared pilot service or production deployment.

## At a glance

| Question | Answer |
| --- | --- |
| Current role | Defines the assumptions for the local development path. |
| Best fit | Learning, testing, and small demonstrations before pilot decisions. |
| Next environment | [Pilot environment](pilot.md) for controlled shared use. |
| Main caution | Development defaults should not be treated as production settings. |

## When to use it

Use this environment when:

- One person is setting up and operating the service.
- Downtime is acceptable.
- Data stays on the local machine.
- The goal is to learn the stack and validate usefulness.

## Defaults

| Setting | Default | Rationale |
| --- | --- | --- |
| Runtime | Ollama | Simple local setup with a local API. |
| Model size | 7B-9B class | Good fit for a 24 GB Mac. |
| Context | 8K for the first path | Keeps memory use predictable. |
| Users | One local user | Simplifies access control and operations. |
| Data | Local only | Supports the Frugal AI sovereignty goal. |

## What changes before pilot

Before this becomes a shared pilot, decide:

- Who owns support.
- How accounts are managed.
- What data may be entered.
- How backups are stored.
- How model and prompt changes are logged.
- What human review is required for education use.

## Related pages

Start with [Quickstart](../../getting-started/quickstart.md), then follow [Local AI chat service](../../getting-started/offline-chat-service.md).

For controlled shared use, see [Pilot environment](pilot.md).
