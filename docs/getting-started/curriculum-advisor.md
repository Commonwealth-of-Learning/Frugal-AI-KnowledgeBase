---
description: Build a curriculum advisor that answers from approved documents using RAG on Dify, with teacher review.
icon: book-open-reader
---

# Curriculum advisor

This guide builds a curriculum advisor that answers from approved curriculum documents — syllabi, textbooks, and teacher guides — using retrieval-augmented generation (RAG) on [Dify](https://dify.ai/), with local models. It grounds answers in vetted sources, so the advisor draws on the curriculum instead of guessing and says when something is not covered.

It is the curriculum advisor from the [example applications](../concepts/example-applications.md) matrix, and the knowledge-layer counterpart to the [math tutor](math-tutor.md): the tutor's orchestration is a tool; this advisor's orchestration is retrieval.

{% hint style="info" %}
Level: intermediate. Expected time: about 45 minutes, plus model downloads. This is the heaviest example in the knowledge base: Dify runs several containers and needs an embedding model as well as an LLM, so it wants more memory than the chat service. It is a development path; a teacher reviews answers before learner use.
{% endhint %}

## Why Dify here

The [math tutor](math-tutor.md) shows orchestration with a single Open WebUI tool. RAG over a document collection is heavier: it needs ingestion, an embedding model, a vector index, and retrieval settings. Dify is an orchestration platform that provides these together. For a single light advisor, Open WebUI's built-in knowledge feature is a lighter option; this guide uses Dify because it suits richer retrieval and multi-step workflows, and it shows that the Orchestration layer is substitutable.

## Fit and limits

- **Good for** — Grounded answers from approved curriculum documents, with an "it is not covered" fallback.
- **Not for** — Learner-facing release without review, or ingestion of unvetted web content.
- **Governance** — Approved documents only; Tier 1 (learner-facing): a teacher approves answers before learner use.
- **Caution** — Dify is a multi-container platform; retrieval quality depends on the documents, chunking, and the embedding model.

## Prerequisites

- The [Local AI chat service](offline-chat-service.md) is built, so Docker and Ollama are installed and running.
- Ollama is running with two models: an LLM for answers (Gemma 4 12B), and an embedding model such as `nomic-embed-text`.
- More memory than the first chat path: Dify's containers plus an LLM and an embedding model are expected to use noticeably more than the chat service's measured ~9.3 GB, so a 24 GB machine has less headroom; measure on the target machine before a pilot.

## Component map

| Layer | This build uses |
| --- | --- |
| Application | A Dify chat application |
| Orchestration | [Dify](../components/orchestration/dify.md) knowledge base and retrieval (RAG) |
| Inference | [Ollama](../components/runtimes/ollama.md) serving an LLM and an embedding model |
| Infrastructure | [Mac mini 24 GB](../components/hardware/mac-mini-24gb.md), or more memory |

This build substitutes two layers at once: Dify provides the Orchestration layer (retrieval) and, through its own chat interface, the Application layer in place of Open WebUI. It connects Dify directly to Ollama on the same machine, so its model calls do not yet pass the [gateway](ai-gateway.md) built in the previous step. Routing Dify's LLM through the gateway endpoint, as the chat service does, would bring those calls inside the envelope; doing so end to end, including the embedding model, is further work in this guide.

## 1. Run Dify

Dify ships a Docker Compose stack. Install and start it by following the [Dify self-host documentation](https://docs.dify.ai/en/getting-started/install-self-hosted/docker-compose): in short, clone the repository, copy `.env.example` to `.env`, and run `docker compose up -d` in its `docker` directory, then open the dashboard at `http://localhost`.

## 2. Connect the local models

Pull the embedding model if it is not already present (the chat service pulled the LLM):

```bash
ollama pull nomic-embed-text
```

In Dify, open Settings, then Model Provider, then Ollama, and add two models with the base URL `http://host.docker.internal:11434`:

- the LLM, named exactly as in `ollama list`;
- the embedding model, for example `nomic-embed-text`, with model type Embedding.

Dify runs in Docker and reaches Ollama on the host through `host.docker.internal`.

## 3. Build the knowledge base from approved documents

In the Knowledge section, create a knowledge base and upload only approved, vetted curriculum documents — national syllabi, approved textbook chapters, and teacher guides. Do not ingest unvetted web content.

Configure indexing:

- the High Quality index, using the embedding model from step 2;
- chunk sizes suited to the documents (smaller chunks improve retrieval accuracy; overlap preserves context);
- hybrid search (semantic plus keyword) for retrieval, with a sensible Top K and score threshold.

Save and process; the knowledge base is ready when processing completes.

## 4. Create the advisor

Create an application, select the LLM from step 2, and set instructions that keep it grounded:

```text
Answer only from the attached curriculum knowledge base.
If the answer is not in the knowledge base, say that it is not covered.
```

Attach the knowledge base, enable Citation and Attribution so each answer shows the documents it drew from, then publish and run the app.

## Verify

| Check | Expected result |
| --- | --- |
| Models connected | The LLM and the embedding model appear under the Ollama provider. |
| Knowledge processed | The uploaded documents show as processed in the knowledge base. |
| Grounded answer | A question covered by the documents is answered from them. |
| Honest fallback | A question outside the documents returns "it is not covered", not a guess. |
| Sources shown | An answer displays which approved document it drew from. |
| Reviewed | Answers are treated as drafts for teacher review before learner use. |

## Governance and review

This build sits in Tier 1 (high-risk, learner-facing) of the risk-tiered teacher-in-the-loop in the [sovereign education-AI reference architecture](../reference/sovereign-education-ai-reference-architecture.md): the knowledge base holds only approved, version-controlled documents; answers are grounded in the curriculum; a teacher approves answers before learners see them; and the advisor runs locally with no external egress. Align the documents to the local curriculum and language, as in [example applications](../concepts/example-applications.md). In this development path the Tier 1 approval gate is procedural: the teacher operates the single-user interface and learners have no direct access. The reference architecture expects a technically enforced approval gate for learner-facing deployment, which is further work before any learner-facing pilot.

Approval assumes [AI literacy](../reference/glossary.md): the reviewing teacher knows the model can misread or overstate a source, and checks answers against the cited documents before learners see them.

## Troubleshooting

| Problem | Check | Fix |
| --- | --- | --- |
| Dify cannot reach Ollama | Base URL | Use `http://host.docker.internal:11434`, and confirm `ollama serve` is running. |
| No embedding model to select | Ollama models | Pull an embedding model such as `nomic-embed-text` and add it in Dify with model type Embedding. |
| Answers ignore the documents | Knowledge base | Confirm processing completed and the knowledge base is attached to the app. |
| The machine slows down | Memory | Dify plus two models is heavy; close other applications or use a machine with more memory. |

## Next step

For richer multi-step workflows at pilot scale, Dify is also the platform for the Advanced curriculum row in [example applications](../concepts/example-applications.md). Use the [Operations overview](../operations/operations-overview.md) for operating added components.
