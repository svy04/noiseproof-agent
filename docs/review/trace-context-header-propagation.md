# Trace Context Header Propagation

Status: implemented.

Phase marker:

```text
trace context header propagation v0
```

## Purpose

Expose a small request trace boundary on every FastAPI response so local API calls are easier to inspect.

This follows the shape of the W3C Trace Context `traceparent` header:

```text
https://www.w3.org/TR/trace-context/
```

## Implemented Behavior

Every response includes:

```text
traceparent
x-noiseproof-trace-source
x-noiseproof-trace-boundary
```

Source values:

```text
generated_traceparent
incoming_traceparent
invalid_traceparent_generated_fallback
```

Boundary header:

```text
x-noiseproof-trace-boundary: local_header_propagation_no_distributed_tracing
```

Behavior:

- valid incoming `traceparent` is accepted and returned
- missing `traceparent` generates a local fallback
- invalid `traceparent` generates a local fallback
- all generated values use W3C-shaped version `00`, 32 hex trace id, 16 hex parent id, and flags `01`

## Boundary

This is local header propagation only.

It is not distributed tracing.
It adds no OpenTelemetry.
It adds no hosted observability.
It adds no trace export.
It adds no span storage.
It adds no database schema or migration.
It adds no cross-service trace proof.
It adds no production observability claim.

## Verification

Focused tests:

```bash
cd apps/api
uv run pytest -q tests/test_routes.py -k "trace_context_header"
uv run pytest -q tests/test_docs.py -k "trace_context_header_propagation"
```

Expected route behaviors:

```text
GET /health without traceparent -> generated traceparent
GET /health with valid traceparent -> incoming traceparent echoed
GET /health with invalid traceparent -> generated fallback
```
