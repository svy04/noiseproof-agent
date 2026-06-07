# HTTP Trace Context Run Metadata

Status: implemented.

Phase marker:

```text
http trace context run metadata v0
```

## Purpose

Capture the local HTTP trace context in `agent_runs.trace_json` for endpoints that use `run_with_trace()`.

This follows the W3C Trace Context `traceparent` shape while keeping the implementation explicitly smaller than distributed tracing:

```text
https://www.w3.org/TR/trace-context/
https://opentelemetry.io/docs/languages/python/instrumentation/
```

## Implemented Behavior

The FastAPI middleware resolves the request `traceparent` as before:

```text
generated_traceparent
incoming_traceparent
invalid_traceparent_generated_fallback
```

For traced endpoints, `run_with_trace()` now records these fields in `agent_runs.trace_json`:

```text
http_traceparent
http_trace_source
http_trace_context_boundary
distributed_tracing: false
opentelemetry_span_export: false
```

The boundary value remains:

```text
local_header_propagation_no_distributed_tracing
```

## Verified Behavior

Focused route test:

```text
tests/test_routes.py::test_run_trace_captures_http_trace_context_without_distributed_tracing_claim
```

The test sends a valid incoming W3C-shaped `traceparent` to:

```text
POST /collection-plans/preview
```

It then verifies:

```text
response traceparent equals incoming traceparent
agent_runs.trace_json.http_traceparent equals incoming traceparent
agent_runs.trace_json.http_trace_source equals incoming_traceparent
agent_runs.trace_json.http_trace_context_boundary equals local_header_propagation_no_distributed_tracing
agent_runs.trace_json.distributed_tracing is false
agent_runs.trace_json.opentelemetry_span_export is false
```

## Boundary

This is local run metadata capture only.

It is not distributed tracing.
It is not OpenTelemetry span export.
It is not hosted observability.
It is not cross-service trace proof.
It is not trace sampling.
It is not trace export.
It is not span storage.
It is not production observability.
It is not external reviewer feedback.
It is not product-complete.
