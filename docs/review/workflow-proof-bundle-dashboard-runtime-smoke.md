# Workflow Proof Bundle Dashboard Runtime Smoke

Status: accepted.

Phase marker: workflow proof bundle dashboard runtime smoke v0.

## Purpose

Verify the workflow proof bundle dashboard link against local Docker PostgreSQL plus live FastAPI HTTP.

This smoke checks that a reviewer can move from `GET /ops/dashboard` to the existing workflow proof bundle route for a freshly created deterministic workflow preview.

## Environment

```text
Docker version: 29.4.3
Docker Compose version: v5.1.3
database container: noiseproof-agent-db
database status: healthy
database port: 55432 -> 5432
DATABASE_URL: postgresql://noiseproof:noiseproof@127.0.0.1:55432/noiseproof
FastAPI URL: http://127.0.0.1:8062
```

Migration runner status:

```text
Applied migrations: 21
Pending migrations: 0
```

## Commands

```powershell
docker compose up -d db
docker compose ps
$env:DATABASE_URL='postgresql://noiseproof:noiseproof@127.0.0.1:55432/noiseproof'
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8062
```

Then:

```text
GET  /health
POST /workflow-runs/execute-preview
GET  /ops/dashboard
GET  /workflow-runs/{id}/proof-bundle
```

## Observed Result

```text
health_status_code: 200
health_status: ok
workflow_version: phase40-lineage-warning-code-dashboard
execute_preview_status_code: 201
workflow_run_id: 6f065799-2d31-4351-b80b-3164280db813
workflow_trace_id: 9c04c41f-dc5b-4d04-8a94-e4c819177425
dashboard_status_code: 200
dashboard_contains_detail_link: true
dashboard_contains_lineage_link: true
dashboard_contains_proof_bundle_link: true
proof_bundle_status_code: 200
proof_bundle_link_label: proof bundle
bundle_boundary: read_model_only_existing_records_no_new_storage
proof_surface_count: 3
```

The dashboard link target was:

```text
GET /workflow-runs/{id}/proof-bundle
```

## Interpretation

The plain operations dashboard can now route a reviewer from a workflow row to:

```text
detail
lineage
proof bundle
```

The proof bundle remains a read model over existing workflow detail, derived lineage, and trace lookup records. The dashboard link only reduces inspection friction.

## Boundary

This smoke is local Docker PostgreSQL plus live FastAPI HTTP evidence only.

It is:

- not new endpoint behavior
- not schema work
- not migration work
- not new lineage storage
- direct Evidence Ledger -> Noise Gate -> Report stage links are now represented by Phase 530 workflow-created link tables; this dashboard smoke remains bounded to dashboard navigation behavior
- not distributed tracing
- not hosted observability
- not LLM output
- not embedding generation
- not retrieval expansion
- not report generation
- not external reviewer feedback
- not hosted deployment evidence
- not customer validation
- not Braincrew acceptance
- not product-complete

The dashboard link makes an existing proof surface easier to inspect. It does not make the proof stronger than the underlying workflow detail, lineage, and trace lookup records.
