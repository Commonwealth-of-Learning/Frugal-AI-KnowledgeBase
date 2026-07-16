---
description: Readiness checklist for moving a Frugal AI service from pilot to production.
icon: building
---

# Production environment

_Scope: a deployment environment, not a [stack layer](../../concepts/how-the-stack-fits-together.md); it applies across all layers._

A production environment runs a Frugal AI service as a dependable, governed service for real users. It is the stage after a successful [pilot](pilot.md). Production is where the annex's Minimum Government Baseline must be fully met and sustained; see the [reference architecture](../../reference/sovereign-education-ai-reference-architecture.md).

{% hint style="info" %}
Use this page as a production-readiness checklist. Do not treat the development guides as production deployment instructions.
{% endhint %}

## At a glance

- **Current role** — Defines assumptions for a dependable, governed deployment for real users.
- **Best fit** — A service that has passed a pilot and needs reliable, supported operation.
- **Hardware fit** — Sized and measured for the production workload, beyond the pilot's single node where concurrency requires it.
- **Main caution** — Production needs security, monitoring, and recovery commitments a pilot does not.

## Production readiness checklist

- **Ownership** — A named service owner, support route, escalation path, and change-approval process.
- **Security** — Security review, role-based access control, key rotation, patching, encryption, and incident response.
- **Data protection** — Approved data classification, retention, deletion, audit-log access, and privacy-airlock controls.
- **Human review** — Documented risk tiers, approval gates, and sampling or audit processes for teacher-only outputs.
- **Reliability** — Monitoring, alerting, backup, restore, rollback, and availability targets tested under expected load.
- **Capacity** — Measured concurrency, latency, memory, storage, and cloud-burst limits for the production workload.
- **Accessibility and localisation** — Review of language coverage, accessibility, curriculum fit, and support materials.
- **Lifecycle** — Model, runtime, gateway, and application update policy, including regression checks before release.
- **Interoperability** — Single sign-on and role integration, export and import of approved content artefacts, machine-readable audit-log export for oversight, and LMS or EMIS integration that does not ingest unnecessary learner records. The [reference architecture](../../reference/sovereign-education-ai-reference-architecture.md) sets these out as procurement-relevant behaviours; none is a documented build path yet.

## What stays out of scope

This page does not prescribe a serving topology, high-availability design, or national deployment model. Those choices should follow a measured pilot, local procurement and data-protection requirements, and component-specific runbooks.

## Related pages

- [Pilot environment](pilot.md)
- [Operations overview](../../operations/operations-overview.md)
