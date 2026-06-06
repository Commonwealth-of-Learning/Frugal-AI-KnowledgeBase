---
description: Browser chat interface for local models.
icon: comments
---

# Open WebUI

Open WebUI provides the browser chat interface for the local AI chat service. It connects to a local model runtime such as Ollama and gives users a familiar chat experience.

## At a glance

| Question | Answer |
| --- | --- |
| Current role | Provides the browser chat interface for the local AI chat service. |
| Best fit | A familiar chat interface for local testing and demonstrations. |
| Provider connection | Connects to the Ollama API, normally on port `11434`. |
| Data location | Chat data, settings, uploads, and users live in the Open WebUI data volume. |
| Main caution | It is an interface, not the full governance or production operations layer. |

## When to use it

Use Open WebUI for:

- A local ChatGPT-like interface.
- Conversation history on the local machine.
- A fast way to demonstrate a local model.
- A simple first application layer on top of Ollama.

## Requirements

- A running model runtime, such as [Ollama](../runtimes/ollama.md).
- Docker Desktop for the path in this guide.
- About 1-2 GB of extra memory for the application, depending on use.
- A reachable Ollama URL. For the current Docker path, use `http://host.docker.internal:11434`.

## Deployment patterns

| Pattern | Best fit | Image | Ollama connection |
| --- | --- | --- | --- |
| Host Ollama with Open WebUI in Docker | Current Mac mini development path | `ghcr.io/open-webui/open-webui:main` | `OLLAMA_BASE_URL=http://host.docker.internal:11434` |
| Integrated Ollama container | DGX Spark development and pilot candidate | `ghcr.io/open-webui/open-webui:ollama` | Bundled Ollama inside the container |

The host-Ollama pattern keeps the runtime visible to local terminal tools such as `ollama list` and `ollama ps`. The integrated-Ollama pattern keeps model data in a separate `open-webui-ollama` Docker volume and is better suited to GPU-backed DGX Spark evaluation.

## Model management

Open WebUI can discover Ollama models from the configured provider, pull models from the model selector, and manage the Ollama connection through Admin Settings > Connections > Ollama.

For reasoning models, the Ollama runtime may need an appropriate reasoning parser before thinking blocks display cleanly in Open WebUI.

## Frugal fit

| Factor | Fit |
| --- | --- |
| Local operation | Runs locally in Docker. |
| Data control | Chat data stays in the local Open WebUI volume. |
| Replaceability | Can later be replaced by another app layer or a custom interface. |
| Operational load | Simple enough for a first local path, but still needs backup and update steps. |

## Limits

- This page covers a single-machine development setup.
- Multi-user pilots need clearer account, backup, and support rules.
- Document upload in a chat interface is not the same as a governed RAG system.
- Updates should preserve the data volume. Shared or pilot deployments should pin versions and review release notes before upgrading.

## Used by this guide

Follow [Local AI chat service](../../getting-started/offline-chat-service.md) to run Open WebUI and connect it to Ollama.

Use [Local AI chat service operations](../../operations/open-webui-ops.md) after setup.

## Links

- [Open WebUI](https://openwebui.com)
- [Open WebUI GitHub](https://github.com/open-webui/open-webui)
- [Open WebUI Ollama guide](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-ollama/)
- [Open WebUI update guide](https://docs.openwebui.com/getting-started/updating/)
- [NVIDIA Open WebUI with Ollama on DGX Spark](https://build.nvidia.com/spark/open-webui/overview)
