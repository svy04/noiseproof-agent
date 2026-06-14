# External Review Issue Body Local OTel Span Export Runtime Route Refresh

Phase marker: external review issue body local OTel span export runtime route refresh v0.

Status: implemented.

## Purpose

Record the owner-authored issue #1 body update that routes `Latest Proof To Inspect` to the local OTel span export runtime proof chain.

This is a live public issue body edit record. It is still not external reviewer feedback.

## Live Issue

```text
issue: https://github.com/svy04/noiseproof-agent/issues/1
updatedAt: 2026-06-14T04:23:17Z
comment_count: 1
starts_with_request: true
first_codepoint: 35
has_leading_bom: false
has_local_otel_latest_proof: true
has_local_otel_route_remote_verification: true
old_semantic_quality_claim_gate_latest_label_present: false
```

## Latest Proof To Inspect

The live issue now routes reviewers to:

```text
docs/review/local-otel-span-export.md
docs/review/local-otel-span-export-runtime-smoke.md
docs/review/external-reader-proof-path-local-otel-span-export-runtime-route-refresh.md
docs/review/external-reader-proof-path-local-otel-span-export-runtime-route-refresh-remote-verification.md
```

Route markers:

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
CI run `27488097835`
External Feedback Screen run `27488097834`
```

## Boundary

This is owner-authored issue body routing only.

It is not external reviewer feedback.

It is not new runtime evidence beyond the linked proof chain.

It is not distributed tracing.

It is not hosted observability.

It is not external collector integration.

It is not OpenTelemetry Collector deployment.

It is not production monitoring.

It is not cross-service trace proof.

It is not hosted deployment evidence.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.
