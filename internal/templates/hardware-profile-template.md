---
description: [Hardware role in the Frugal AI knowledge base.]
icon: [gitbook-icon-name]
---

# [Device Name]

[Describe the device in one short paragraph. State whether this is a development, pilot, or production profile.]

## At a glance

| Question | Answer |
| --- | --- |
| Current role | [How this hardware is used in the Frugal AI knowledge base] |
| Best fit | [Plain-language workload fit] |
| Memory | [Use GB, not Gb] |
| CPU or chip | [Specify the CPU, chip, or architecture. For Mac mini profiles, use Apple M4 or newer.] |
| Environment fit | [Development, pilot, or production] |
| Main caution | [Most important hardware limit] |

## When to use it

Use this profile when:

- [Suitable scenario 1]
- [Suitable scenario 2]
- [Suitable scenario 3]

## Specifications

| Field | Value |
| --- | --- |
| Environment fit | [Development, pilot, or production] |
| CPU or chip | [e.g., Apple M4 or newer, NVIDIA Grace Blackwell] |
| Memory | [e.g., 24 GB unified] |
| GPU or accelerator | [e.g., Apple integrated GPU, NVIDIA Blackwell] |
| Storage | [e.g., 512 GB SSD] |
| Operating system | [e.g., macOS 15+] |
| Network assumption | [e.g., local/offline capable] |

## Memory budget

| Use | Expected allocation | Confidence |
| --- | --- | --- |
| Operating system and background services | [value] | [measured/source-listed/estimated] |
| Runtime and application overhead | [value] | [measured/source-listed/estimated] |
| Available for model and context | [value] | [measured/source-listed/estimated] |

State the measurement method when values are measured. Label planning values as estimates.

## What fits

| Model class | Quantisation | Context | Fit | Confidence |
| --- | --- | --- | --- | --- |
| [e.g., 7B-9B] | [e.g., Q4] | [e.g., 8K] | [Comfortable/tight/not suitable] | [measured/source-listed/estimated] |
| [e.g., 14B] | [e.g., Q4] | [e.g., 8K] | [Comfortable/tight/not suitable] | [measured/source-listed/estimated] |

## Frugal fit

| Factor | Fit |
| --- | --- |
| Cost discipline | [How this profile supports cost control] |
| Local control | [How data and operation stay local] |
| Operational load | [Skills and maintenance required] |
| Replaceability | [What can be swapped later] |

## Compatibility

| Runtime or framework | Status | Notes |
| --- | --- | --- |
| [Runtime](../runtimes/[file].md) | [Tested/Untested/Expected] | [Integration notes] |

## Limits

- [Limit 1]
- [Limit 2]
- [Limit 3]

## Used by

- [Guide or stack page](../../getting-started/[file].md)
