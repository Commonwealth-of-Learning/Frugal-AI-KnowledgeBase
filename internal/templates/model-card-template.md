---
description: [Model role in the Frugal AI knowledge base.]
icon: [gitbook-icon-name]
---

# [Model Name]

[Describe the model in one short paragraph. State whether it is used in a current guide or is a candidate for evaluation.]

Build from the top down: reader decision first, technical details later. Use `internal/naming-registry.md` for approved model, runtime, hardware, and service names. Leave out any section that would contain only placeholders, unverified claims, or a statement that the information is unavailable.

## At a glance

Use this table to answer the practical questions first. Keep only rows with verified, useful content.

| Question | Answer |
| --- | --- |
| Current role | [Used in the first path / candidate for a future path] |
| Best fit | [Plain-language task or scenario] |
| Local fit | [Fits the documented hardware / needs a measured setup path] |
| Model type | [Dense or MoE, with active parameter count if relevant] |
| Inputs | [Text, image, audio, video, or runtime-specific subset] |
| Main caution | [Most important operational limit] |

## Good for

- [Use case 1]
- [Use case 2]
- [Use case 3]

## Not suitable for

- [Anti-use case 1]
- [Anti-use case 2]

## Frugal fit

| Factor | Fit |
| --- | --- |
| Local operation | [How it runs locally] |
| Resource use | [How it fits the hardware profile] |
| Replaceability | [How it can be swapped later] |
| Governance | [Licence, data, or review considerations] |

## Reference settings

Use this section to separate source-listed model defaults, runtime-specific defaults, and Frugal AI guide defaults. Keep it short. Do not paste launch commands or long shell scripts. Leave this section out when settings are not verified or not useful for the page job.

| Profile | Context | Temperature | Top-p | Top-k | Min-p | Penalty | Thinking mode | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Profile name] | [context] | [value] | [value] | [value] | [value] | [value] | [enabled/disabled/optional] | [source] |

Add runtime notes only when they change operation:

- State whether settings are for Ollama, llama.cpp, Unsloth GGUF, MLX, vLLM, or another runtime.
- Label family-level settings when the source does not list the exact checkpoint.
- Record whether thinking mode is on by default, optional, or unsupported in the documented runtime.
- Record context as a measured guide value when the guide uses less than the source-listed maximum.
- For multimodal models, record input ordering, visual token budget, audio/video limits, and backend support only when source-listed.

## Technical details

| Field | Value |
| --- | --- |
| Model ID | `[official/model-id]` |
| Runtime tag | `[runtime-tag]` |
| Source | [Official source](URL) |
| Architecture | [Short source-listed architecture summary] |
| Model licence | [Licence name and link] |

## Source confidence

| Claim | Value | Confidence |
| --- | --- | --- |
| Parameter count | [value] | [source-listed/estimated] |
| Download size | [value] | [source-listed/measured] |
| Context window | [value] | [source-listed/tested locally] |

Do not publish benchmark values unless they were measured in the documented environment or clearly labelled as source-listed.

## Limits

- [Known limit 1]
- [Known limit 2]
- [Known limit 3]

## Used by

Leave this section out for candidate models that are not used by a public Frugal AI guide.

- [Guide](../../getting-started/[file].md)

## Links

- [Official model page](URL)
- [Runtime library page](URL)
