# HTTP Trace Context Docker Runtime Smoke

Status: verified.

Phase marker: http trace context docker runtime smoke v0.

Purpose: record that the Phase 824 HTTP trace context run metadata behavior is visible through a Dockerized FastAPI API service backed by local Docker PostgreSQL.

## Why Docker Is Needed Here

Docker is needed to make the API, PostgreSQL/pgvector, startup wiring, environment variables, and service health boundaries inspectable without relying on the host machine's global Python or PostgreSQL state.

For this gate, Docker specifically proves that the trace context capture path works through the containerized API and a real local database row, not only through in-process route tests.

## Runtime Environment

```text
Docker version 29.4.3, build 055a478
Docker Compose version v5.1.3
Compose project: noiseproof-phase826
API_PORT=18080
POSTGRES_PORT=55462
```

## Commands

```powershell
$env:API_PORT='18080'
$env:POSTGRES_PORT='55462'
docker compose -p noiseproof-phase826 --profile api config
docker compose -p noiseproof-phase826 --profile api up -d --build api
docker compose -p noiseproof-phase826 --profile api ps
```

Runtime cleanup:

```powershell
docker compose -p noiseproof-phase826 --profile api down -v
```

Cleanup completed after the smoke.

## HTTP Smoke Evidence

Request:

```text
POST /collection-plans/preview -> 200
traceparent: 00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01
```

Follow-up inspection:

```text
GET /agent-runs -> 200
```

Observed runtime result:

```json
{
  "health_status": "ok",
  "health_service": "noiseproof-agent-api",
  "workflow_version": "phase40-lineage-warning-code-dashboard",
  "collection_plan_status": 200,
  "agent_runs_status": 200,
  "run_id": "9f7fcf84-5d04-42f9-9fec-15bdd968669b",
  "traceparent_expected": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01",
  "traceparent_recorded": "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01",
  "trace_source": "incoming_traceparent",
  "trace_boundary": "local_header_propagation_no_distributed_tracing",
  "distributed_tracing": false,
  "opentelemetry_span_export": false
}
```

## Verified Fields

```text
agent_runs.trace_json.http_traceparent
agent_runs.trace_json.http_trace_source
agent_runs.trace_json.http_trace_context_boundary
agent_runs.trace_json.distributed_tracing
agent_runs.trace_json.opentelemetry_span_export
```

## Boundary

This is local Docker runtime evidence only.

It is not hosted deployment evidence.

It is not distributed tracing.

It is not OpenTelemetry span export.

It is not hosted observability.

It is not cross-service trace proof.

It is not production readiness.

It is not external reviewer feedback.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.

Next gate: remote verification for this runtime-smoke proof after push, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, hosted observability only with an explicit deployment target, or another source-first product gate selected from current repository state.
