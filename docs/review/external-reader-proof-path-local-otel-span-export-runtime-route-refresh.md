# External-reader Proof Path Local OTel Span Export Runtime Route Refresh

Phase marker: external-reader proof path local OTel span export runtime route refresh v0.

## Purpose

Route first-pass external reviewers to the local OpenTelemetry span export proof chain without converting that route into a distributed tracing, hosted observability, or production monitoring claim.

## Routed Artifacts

```text
docs/review/local-otel-span-export.md
docs/review/local-otel-span-export-runtime-smoke.md
docs/review/external-reader-proof-path.md
docs/review/external-reviewer-link-map.md
docs/review/external-reviewer-shortlist.md
```

## Route Markers

```text
NOISEPROOF_ENABLE_OTEL_SPAN_EXPORT=true
GET /health -> 200
x-noiseproof-otel-span-export: local_in_memory_enabled
GET /agent-runs -> 200
GET /ops/summary -> 200
GET /traces/otel-spans/local
span_export_enabled=true
span_count=4
local_in_memory_otel_span_export_not_distributed_tracing
```

## Reader-facing Boundary

This route points reviewers to the Dockerized local FastAPI runtime proof that request-level spans can be inspected in memory when the opt-in flag is enabled.

It is route hygiene only.

It is not new runtime evidence.

It is not distributed tracing.

It is not hosted observability.

It is not external collector integration.

It is not OpenTelemetry Collector deployment.

It is not production monitoring.

It is not cross-service trace proof.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not product-complete.
