---
description: Assumptions for a production deployment. Further work.
icon: building
---

# Production environment

_Scope: a deployment environment, not a [stack layer](../../concepts/how-the-stack-fits-together.md); it applies across all layers._

A production environment runs a Frugal AI service as a dependable, governed service for real users. It is the stage after a successful [pilot](pilot.md). Production is where the annex's Minimum Government Baseline must be fully met and sustained; see the [reference architecture](../../reference/sovereign-education-ai-reference-architecture.md).

{% hint style="info" %}
This environment is not yet documented in full. This page records the shape of the work; the detailed guidance is further work.
{% endhint %}

## At a glance

- **Current role** — Defines assumptions for a dependable, governed deployment for real users.
- **Best fit** — A service that has passed a pilot and needs reliable, supported operation.
- **Hardware fit** — Sized and measured for the production workload, beyond the pilot's single node where concurrency requires it.
- **Main caution** — Production needs security, monitoring, and recovery commitments a pilot does not.

## What production adds beyond a pilot

- security review;
- service monitoring and alerting;
- incident response;
- lifecycle and model-update policy;
- capacity and concurrency testing;
- accessibility and language review;
- formal data-protection approval.

## Further work

Detailed production guidance — serving topology, high availability, monitoring, and a production operations runbook — is not yet written. Add it only after a pilot has run and the supporting components and operations pages exist.

## Related pages

- [Pilot environment](pilot.md)
- [Operations overview](../../operations/operations-overview.md)
