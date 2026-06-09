---
description: Put a local AI gateway in front of the chat service for redaction, routing, audit logging, and controlled cloud burst.
icon: shield-halved
---

# AI gateway

This guide puts a local AI gateway in front of the [Local AI chat service](offline-chat-service.md). The gateway gives every application one endpoint, redacts personal data before a model sees it, logs requests for audit, and — only if enabled — routes narrowly scoped tasks to an approved external provider. It is the first [Gateway layer](../concepts/gateway-layer.md) build: the point where the sovereignty envelope becomes enforceable in software.

{% hint style="info" %}
Level: intermediate. This is a development path. It runs on the same machine as the chat service and keeps the local model as the default. External routing is optional and stays off until configured.
{% endhint %}

## Fit and limits

- **Good for** — A single governed endpoint, personal-data redaction, audit logging, and optional controlled cloud burst.
- **Not for** — Production multi-team access control, budgets, or single sign-on; those are pilot-scale and out of scope here.
- **Governance** — The gateway is the sovereignty envelope: redaction and approved destinations are enforced at this boundary.
- **Caution** — Cloud burst sends content outside the machine. Keep it off unless a task needs it, and redact before egress.

## Prerequisites

- The [Local AI chat service](offline-chat-service.md) is built and running, with Ollama, Qwen3.5-9B, and Open WebUI.
- Python is available on the host for the gateway, and Docker for the redaction services.

## Component map

| Layer | This build uses |
| --- | --- |
| Application | [Open WebUI](../components/frameworks/open-webui.md), pointed at the gateway |
| Gateway | [LiteLLM](../components/gateways/litellm.md) with a personal-data redaction guardrail |
| Inference | [Ollama](../components/runtimes/ollama.md) with [Qwen3.5-9B](../components/models/qwen-3.5-9b.md) |
| Infrastructure | [Mac mini 24 GB](../components/hardware/mac-mini-24gb.md) |

## 1. Create the gateway configuration

Create `litellm-config.yaml` with one local model behind a single name:

```yaml
model_list:
  - model_name: qwen3.5-dev
    litellm_params:
      model: ollama_chat/qwen3.5-dev
      api_base: http://localhost:11434
```

## 2. Start the gateway

Install the gateway on the host:

```bash
pip install 'litellm[proxy]'
```

Set a master key and start it:

```bash
export LITELLM_MASTER_KEY="sk-local-gateway"
```

```bash
litellm --config litellm-config.yaml
```

The gateway serves an OpenAI-compatible endpoint on port 4000. Check it:

```bash
curl http://localhost:4000/health/readiness
```

## 3. Point the chat interface at the gateway

In Open WebUI, open Admin Settings, then Connections, then add an OpenAI API connection with base URL `http://host.docker.internal:4000/v1` and the master key set above.

Save, select `qwen3.5-dev` in the model list, and send a test message. Chat now runs through the gateway. The direct Ollama connection can then be removed so that every request passes the boundary.

## 4. Redact personal data

Redaction is the airlock: personal data is masked before any model sees it. LiteLLM uses Microsoft Presidio for this, run as two local services.

Start the Presidio analyzer:

```bash
docker run -d -p 5002:3000 --name presidio-analyzer mcr.microsoft.com/presidio-analyzer
```

Start the Presidio anonymiser:

```bash
docker run -d -p 5001:3000 --name presidio-anonymizer mcr.microsoft.com/presidio-anonymizer
```

Tell the gateway where they are:

```bash
export PRESIDIO_ANALYZER_API_BASE="http://localhost:5002"
export PRESIDIO_ANONYMIZER_API_BASE="http://localhost:5001"
```

Add a redaction guardrail to `litellm-config.yaml`:

```yaml
guardrails:
  - guardrail_name: redact-pii
    litellm_params:
      guardrail: presidio
      mode: pre_call
      default_on: true
      pii_entities_config:
        PERSON: MASK
        EMAIL_ADDRESS: MASK
        PHONE_NUMBER: MASK
        CREDIT_CARD: BLOCK
```

Restart the gateway. Personal data is now masked before the model, and the original is kept only in the gateway log. Redaction language is set with `presidio_language` for non-English content, which matters in multilingual education settings.

## 5. Controlled cloud burst (optional)

Cloud burst sends a narrowly scoped task to an approved external provider, and only after redaction. Keep the local model as the default and the fallback. For example, the [math tutor](math-tutor.md) answers routine questions on the local model and bursts a genuinely hard problem to a stronger model, with the prompt redacted first.

Add one approved provider to `litellm-config.yaml`:

```yaml
  - model_name: cloud-burst
    litellm_params:
      model: openai/<approved-model>
      api_base: https://<approved-endpoint>/v1
      api_key: os.environ/CLOUD_BURST_KEY
```

Keep the local model as the fallback so requests use it when the external provider is unavailable (see the LiteLLM routing documentation for fallback options). Apply the `redact-pii` guardrail to the cloud-burst model as well, so nothing leaves the machine before personal data is masked. Restrict use of `cloud-burst` to tasks that genuinely need it, and block learner free text and identifiers by default.

## Verify

| Check | Expected result |
| --- | --- |
| Gateway responds | `http://localhost:4000/health/readiness` returns a ready status. |
| Chat works through the gateway | Open WebUI returns a reply using `qwen3.5-dev` through the gateway. |
| Redaction works | A prompt with a sample name or email reaches the model masked; the gateway log shows the masked form. |
| Local default | With no external provider enabled, no request leaves the machine. |
| Fallback | With cloud burst configured but offline, requests fall back to the local model. |

## Governance and review

This build operationalises the sovereignty envelope in the [sovereign education-AI reference architecture](../reference/sovereign-education-ai-reference-architecture.md):

- redaction runs before any model sees a prompt;
- only configured providers can be reached, and the local model is the default;
- cloud burst is limited to de-identified, narrowly scoped tasks, with learner free text and identifiers blocked;
- requests, routes, and redactions are logged for review;
- learner-facing output still follows the risk tiers, with Tier 1 approval before any learner release.

## Troubleshooting

| Problem | Check | Fix |
| --- | --- | --- |
| Open WebUI cannot reach the gateway | Connection base URL | Use `http://host.docker.internal:4000/v1`, and confirm the gateway is running. |
| The model is not listed | Gateway config | Confirm `model_name` in `litellm-config.yaml` matches the model selected in Open WebUI. |
| Redaction does not apply | Presidio services | Confirm both Presidio containers are running and the analyzer and anonymiser URLs are set. |
| A request reaches an external provider unmasked | Guardrail scope | Apply the `redact-pii` guardrail to every model, including `cloud-burst`. |

## Next step

Use [Local AI chat service operations](../operations/open-webui-ops.md) to run the gateway, manage keys, and review the audit log.
