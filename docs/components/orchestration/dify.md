---
description: Open-source orchestration platform for RAG and multi-step AI workflows on local models.
icon: diagram-project
---

# Dify

_Layer: [Orchestration](../../concepts/how-the-stack-fits-together.md) (platform)._

Dify is an open-source orchestration platform for building RAG and multi-step AI applications. In the Frugal AI knowledge base it is the heavier Orchestration-layer option, used when retrieval over a document collection or a multi-step workflow outgrows a single Open WebUI tool.

## At a glance

- **Current role** — Orchestration platform for the curriculum advisor.
- **Best fit** — RAG over approved documents, and multi-step workflows, on local models.
- **Local fit** — Self-hosted with Docker Compose; runs several containers, so it needs more memory than the chat service.
- **Interface** — Connects to local models through Ollama; reached on the host at port 80.
- **Main caution** — A multi-container platform; retrieval quality depends on the documents, chunking, and the embedding model.

## When to use it

Use Dify when an application needs retrieval over a document collection, an embedding model, or multi-step workflows — more than a single tool provides. For a simple tool-using assistant, an Open WebUI tool (as in the math tutor) is the lighter choice.

## Requirements

- Docker, for the Dify Compose stack.
- Ollama serving an LLM and an embedding model, for example `nomic-embed-text`.
- More memory than the first chat path.

## Frugal fit

| Factor | Fit |
| --- | --- |
| Local operation | Self-hosted; connects to local models with no external API required. |
| Resource use | Heavier than the chat service; runs several containers and a second, embedding, model. |
| Replaceability | Open-source; an application can move to a lighter substrate if its needs shrink. |
| Governance | Pairs with approved-document knowledge bases and the gateway for any external routing. |

## Compatibility

- Local models through Ollama, for both the LLM and the embedding model.
- Knowledge bases built from approved documents for RAG.
- Routed through the [gateway](../gateways/litellm.md) when external models are used.

## Limits

- A multi-container platform; more to run and operate than the chat service.
- Retrieval quality depends on document quality, chunking, and the embedding model.
- A full operations runbook for Dify is further work; see the [operations overview](../../operations/operations-overview.md).

## Used by

Follow [Curriculum advisor](../../getting-started/curriculum-advisor.md) to build a RAG application on Dify.

## Links

- [Dify documentation](https://docs.dify.ai/)
- [Dify self-host with Docker Compose](https://docs.dify.ai/en/getting-started/install-self-hosted/docker-compose)
