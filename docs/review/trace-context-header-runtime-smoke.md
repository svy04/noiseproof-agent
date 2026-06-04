# Trace Context Header Runtime Smoke

Status: implemented.

Phase marker:

```text
trace context header runtime smoke v0
```

## Purpose

Record live HTTP evidence that the trace context header middleware is visible through `uvicorn`, not only through TestClient.

## Environment

```text
uvicorn on 127.0.0.1:8011
endpoint: GET /health
```

Docker was not required for this smoke because `/health` does not need PostgreSQL.

## Commands

```bash
cd apps/api
uv run uvicorn app.main:app --host 127.0.0.1 --port 8011
curl -i http://127.0.0.1:8011/health
curl -i -H "traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01" http://127.0.0.1:8011/health
curl -i -H "traceparent: not-a-trace" http://127.0.0.1:8011/health
```

## Observed Results

```text
GET /health without traceparent -> 200
traceparent: 00-ae5bb187448db50306e51f19b26dfa9f-14bfcefc58772785-01
x-noiseproof-trace-source: generated_traceparent
x-noiseproof-trace-boundary: local_header_propagation_no_distributed_tracing
```

```text
GET /health with valid traceparent -> 200
traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
x-noiseproof-trace-source: incoming_traceparent
x-noiseproof-trace-boundary: local_header_propagation_no_distributed_tracing
```

```text
GET /health with invalid traceparent -> 200
traceparent: 00-f710707bc4bb4908e01e250d2e745390-f5907af446d3c172-01
x-noiseproof-trace-source: invalid_traceparent_generated_fallback
x-noiseproof-trace-boundary: local_header_propagation_no_distributed_tracing
```

## Boundary

This is local live HTTP evidence only.

It is not hosted observability.
It is not distributed tracing.
It is not OpenTelemetry.
It is not trace export.
It is not span storage.
It is not cross-service trace proof.
It is not customer validation.
