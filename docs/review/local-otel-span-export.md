# Local OpenTelemetry Span Export

Status: implemented.

Phase marker: local OpenTelemetry span export v0.

Purpose: add an opt-in, local-only OpenTelemetry span export surface so request-level spans can be inspected without claiming distributed tracing, hosted observability, or external collector integration.

## Source-first Basis

OpenTelemetry Python documentation describes manual instrumentation through the API and SDK. The official setup uses an SDK `TracerProvider` and a span processor/exporter for applications.

This gate follows that shape with `opentelemetry-sdk` and an in-memory exporter only.

## Implemented Artifacts

```text
apps/api/pyproject.toml
apps/api/uv.lock
apps/api/app/services/otel_span_export.py
apps/api/app/settings.py
apps/api/app/main.py
apps/api/app/routes/traces.py
apps/api/app/services/trace_context.py
apps/api/tests/test_routes.py
```

## Runtime Switch

```text
NOISEPROOF_ENABLE_OTEL_SPAN_EXPORT=true
```

Default state:

```text
span_export_enabled: false
span_export_boundary: disabled_no_span_export
```

Enabled local state:

```text
span_export_enabled: true
span_export_boundary: local_in_memory_otel_span_export_not_distributed_tracing
```

## Inspection Endpoint

```text
GET /traces/otel-spans/local
```

The endpoint returns:

```text
span_export_enabled
span_export_boundary
span_count
spans
non_claims
```

Request responses also include:

```text
x-noiseproof-otel-span-export
```

## Trace Metadata

When local span export is enabled, preview endpoint `agent_runs.trace_json` records:

```text
opentelemetry_span_export: true
opentelemetry_span_export_boundary: local_in_memory_otel_span_export_not_distributed_tracing
distributed_tracing: false
```

## Boundary

This is local in-memory OpenTelemetry span export only.

This is not distributed tracing.

This is not hosted observability.

This is not external collector integration.

This is not OpenTelemetry Collector deployment.

This is not production monitoring.

This is not cross-service trace proof.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.
