---
description: [Model role in the Frugal AI knowledge base.]
icon: [gitbook-icon-name]
---

# [Model Name]

[Describe the model in one short paragraph. State why it is included in the current path.]

## Identity

| Field | Value |
| --- | --- |
| Model ID | `[official/model-id]` |
| Runtime tag | `[runtime-tag]` |
| Source | [Official source](URL) |
| Modality | [Text/multimodal/etc.] |
| Languages | [Source-listed languages] |
| Model licence | [Licence name and link] |
| Local guide context | [Context used by the guide] |

## Source confidence

| Claim | Value | Confidence |
| --- | --- | --- |
| Parameter count | [value] | [source-listed/estimated] |
| Download size | [value] | [source-listed/measured] |
| Context window | [value] | [source-listed/tested locally] |
| Memory use in guide context | [value] | [measured/estimated] |

Do not publish benchmark values unless they were measured in the documented environment or clearly labelled as source-listed.

## Reference settings

Use this section to separate source-listed model defaults, runtime-specific defaults, and Frugal AI guide defaults. Keep it short. Do not paste launch commands or long shell scripts.

| Profile | Context | Temperature | Top-p | Top-k | Min-p | Penalty | Thinking mode | Source |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Frugal AI guide setting | [guide context] | [set/unspecified] | [set/unspecified] | [set/unspecified] | [set/unspecified] | [set/unspecified] | [enabled/disabled/unspecified] | [Guide/runtime] |
| Source reference setting | [source context] | [value] | [value] | [value] | [value or not listed] | [value or not listed] | [enabled/disabled/optional] | [Official model page/runtime guide] |

Add runtime notes only when they change operation:

- State whether settings are for Ollama, llama.cpp, Unsloth GGUF, MLX, vLLM, or another runtime.
- Label family-level settings when the source does not list the exact checkpoint.
- Record whether thinking mode is on by default, optional, or unsupported in the documented runtime.
- Record context as a measured guide value when the guide uses less than the source-listed maximum.
- For multimodal models, record input ordering, visual token budget, audio/video limits, and backend support only when source-listed.

## Why this model fits the path

- [Fit reason 1]
- [Fit reason 2]
- [Fit reason 3]

## Frugal fit

| Factor | Fit |
| --- | --- |
| Local operation | [How it runs locally] |
| Resource use | [How it fits the hardware profile] |
| Replaceability | [How it can be swapped later] |
| Governance | [Licence, data, or review considerations] |

## Good for

- [Use case 1]
- [Use case 2]
- [Use case 3]

## Not suitable for

- [Anti-use case 1]
- [Anti-use case 2]

## Limits

- [Known limit 1]
- [Known limit 2]
- [Known limit 3]

## Used by

- [Guide](../../getting-started/[file].md)

## Links

- [Official model page](URL)
- [Runtime library page](URL)
