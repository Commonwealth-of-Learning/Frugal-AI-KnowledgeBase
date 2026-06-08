---
description: Self-hosted LLM gateway used as the sovereignty envelope for local-first AI.
icon: shield-halved
---

# LiteLLM

_Layer: [Gateway](../../concepts/how-the-stack-fits-together.md) (sovereignty envelope)._

LiteLLM is a self-hosted, open-source AI gateway. In the Frugal AI knowledge base it provides the Gateway layer: a single OpenAI-compatible endpoint in front of local and, optionally, external models, where redaction, routing, and audit logging are enforced.

## At a glance

| Question | Answer |
| --- | --- |
| Current role | Candidate gateway for the Gateway layer. |
| Best fit | One governed endpoint over local Ollama, with personal-data redaction and audit logging. |
| Local fit | Runs locally alongside Ollama and Open WebUI as a lightweight proxy. |
| Inputs | OpenAI-compatible requests from any application. |
| Main caution | Redaction needs the Presidio services running, and cloud burst must stay redacted and approved-only. |

## When to use it

Use LiteLLM when there is more than one model or application, or any external routing, so that governance has one home. For a single local model used by one application, the gateway is optional.

## Requirements

- The local AI chat service, or another local runtime, as the default model.
- Python on the host for the proxy.
- For redaction: Microsoft Presidio analyzer and anonymiser services, run locally.

## Frugal fit

| Factor | Fit |
| --- | --- |
| Local operation | Runs fully local; no external calls unless a provider is configured. |
| Resource use | Lightweight proxy; redaction adds two small local services. |
| Replaceability | Open-source and OpenAI-compatible, so applications are not tied to it. |
| Governance | Redaction, approved destinations, and audit logging are enforced at one boundary. |

## Compatibility

- Local models through Ollama, and other local runtimes such as vLLM.
- External providers, when controlled cloud burst is enabled and approved.
- Personal-data redaction through Presidio, configurable per language.

## Limits

- Multi-team access control, budgets, and single sign-on are pilot-scale features beyond the first slice.
- Redaction quality depends on the configured entity types and confidence thresholds.
- Cloud burst sends content outside the machine and must be redacted and limited to approved providers.

## Used by

Follow [AI gateway](../../getting-started/ai-gateway.md) to put LiteLLM in front of the local AI chat service.

## Links

- [LiteLLM AI gateway documentation](https://docs.litellm.ai/docs/simple_proxy)
- [LiteLLM Ollama provider](https://docs.litellm.ai/docs/providers/ollama)
- [LiteLLM Presidio PII masking guardrail](https://docs.litellm.ai/docs/proxy/guardrails/pii_masking_v2)
