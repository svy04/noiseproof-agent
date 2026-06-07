# Local OpenTelemetry Span Export Runtime Smoke

Phase marker: Dockerized local OpenTelemetry span export runtime smoke v0.

## Purpose

Verify that the Phase 850 opt-in local OpenTelemetry span export surface works through the Dockerized FastAPI service, not only through TestClient.

This proof also records a small configuration defect found during the smoke: `NOISEPROOF_ENABLE_OTEL_SPAN_EXPORT=true` was initially passed to the shell, but `docker-compose.yml` did not forward it into the `api` service environment. The fix was to add the flag to the `api.environment` block and guard it with `apps/api/tests/test_compose.py`.

## Runtime Environment

```text
docker_server: 29.4.3
docker_operating_system: Docker Desktop
docker_os_type: linux
docker_compose_version: v5.1.3
compose_project: noiseproof-phase851
POSTGRES_PORT: 15451
API_PORT: 18051
NOISEPROOF_ENABLE_OTEL_SPAN_EXPORT: true
```

## Commands

```powershell
$env:POSTGRES_PORT='15451'
$env:API_PORT='18051'
$env:NOISEPROOF_ENABLE_OTEL_SPAN_EXPORT='true'
docker compose -p noiseproof-phase851 --profile api config
docker compose -p noiseproof-phase851 --profile api up -d --build --force-recreate db api
curl.exe -sS -D - http://127.0.0.1:18051/health -o -
curl.exe -sS http://127.0.0.1:18051/agent-runs
curl.exe -sS http://127.0.0.1:18051/ops/summary
curl.exe -sS http://127.0.0.1:18051/traces/otel-spans/local
docker compose -p noiseproof-phase851 --profile api down -v
```

## Compose Config Observation

```text
NOISEPROOF_ENABLE_OTEL_SPAN_EXPORT: "true"
published API port: "18051"
published PostgreSQL port: "15451"
```

## Runtime Observations

`GET /health` returned `200 OK` and included:

```text
x-noiseproof-otel-span-export: local_in_memory_enabled
x-noiseproof-trace-boundary: local_header_propagation_no_distributed_tracing
```

`GET /agent-runs` returned:

```json
[]
```

`GET /ops/summary` returned `200 OK` with the existing operations placeholder/count surface.

`GET /traces/otel-spans/local` returned:

```json
{
  "span_export_enabled": true,
  "span_export_boundary": "local_in_memory_otel_span_export_not_distributed_tracing",
  "span_count": 4,
  "non_claims": {
    "distributed_tracing": false,
    "external_collector": false,
    "hosted_observability": false,
    "production_monitoring": false,
    "product_complete": false
  }
}
```

Observed span names included:

```text
HTTP GET /health
HTTP GET /agent-runs
HTTP GET /ops/summary
```

Each observed span included `http.request.method`, `url.path`, `noiseproof.http_traceparent`, `noiseproof.http_trace_source`, `noiseproof.otel_boundary`, and `http.response.status_code` attributes.

## Cleanup

```text
docker compose -p noiseproof-phase851 --profile api down -v -> completed
noiseproof-phase851_noiseproof_pgdata -> removed
noiseproof-phase851_default network -> removed
```

## Boundaries

- local Docker/FastAPI runtime evidence only
- local in-memory OpenTelemetry span export only
- not distributed tracing
- not hosted observability
- not external collector integration
- not OpenTelemetry Collector deployment
- not production monitoring
- not cross-service trace proof
- not hosted deployment evidence
- not external reviewer feedback
- not product-complete
