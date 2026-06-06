# Workflow Proof Bundle Reviewer Checklist Dashboard Runtime Smoke

Status: accepted.

Phase marker: workflow proof bundle reviewer checklist dashboard runtime smoke v0.

## Purpose

Verify the workflow proof bundle `reviewer_checklist` dashboard discovery path against local Docker PostgreSQL plus live FastAPI HTTP.

This smoke checks that a reviewer can move from `GET /ops/dashboard` to the existing workflow proof bundle route through the `reviewer checklist` link, and that the linked proof bundle returns the expected read-only checklist.

## Environment

```text
Docker version: 29.4.3
Docker Compose version: v5.1.3
Compose project: noiseproof-phase659
POSTGRES_PORT=55448
database container: noiseproof-phase659-db-1
database status: healthy
DATABASE_URL: postgresql://noiseproof:noiseproof@127.0.0.1:55448/noiseproof
FastAPI URL: http://127.0.0.1:8105
```

Migration runner status:

```text
Applied migrations: 0
Pending migrations: 23
Applied migrations: 23
Pending migrations: 0
```

## Commands

```powershell
$env:POSTGRES_PORT='55448'
docker compose -p noiseproof-phase659 config
docker compose -p noiseproof-phase659 up -d db
docker compose -p noiseproof-phase659 ps db
docker compose -p noiseproof-phase659 exec -T db pg_isready -U noiseproof -d noiseproof

$env:DATABASE_URL='postgresql://noiseproof:noiseproof@127.0.0.1:55448/noiseproof'
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8105
```

Then:

```text
GET  /health
POST /workflow-runs/execute-preview
GET  /ops/dashboard
GET  /workflow-runs/{id}/proof-bundle
```

Cleanup:

```text
stopped_process: 83528
docker compose -p noiseproof-phase659 down -v -> completed
```

## Observed Result

```text
health_status: ok
workflow_version: phase40-lineage-warning-code-dashboard
execute_preview_status_code: 201
workflow_run_id: 4bef642c-3293-43a0-b0f5-fd9e43d2e3d5
workflow_trace_id: 812bd4be-f552-4d5f-b3a9-2463d783cc30
GET /ops/dashboard -> 200
dashboard_contains_reviewer_checklist_link: true
dashboard_contains_reviewer_checklist_boundary: true
dashboard_contains_not_hosted_observability: true
GET /workflow-runs/{id}/proof-bundle -> 200
proof_bundle_reviewer_checklist_count: 4
reviewer_checklist_ids: detail_counts,lineage_links,trace_lookup,failure_case_handoff
proof_bundle_has_trace_lookup_available: true
proof_bundle_boundary: read_model_only_existing_records_no_new_storage
proof_surface_count: 3
warning_count: 2
```

The dashboard link target was:

```text
GET /workflow-runs/{id}/proof-bundle
```

The link label was:

```text
reviewer checklist
```

## Interpretation

The local dashboard now routes a reviewer from a workflow row to the proof bundle checklist without requiring the reviewer to already know that `reviewer_checklist` exists in the JSON response.

The linked proof bundle returned four checklist items:

```text
detail_counts
lineage_links
trace_lookup
failure_case_handoff
```

The checklist remains a read-only inspection guide over existing workflow detail, lineage, trace, and failure-case surfaces.

## Boundary

This smoke is local Docker PostgreSQL plus live FastAPI HTTP evidence only.

It is not new endpoint behavior, not schema work, not migration work, not new storage, not distributed tracing, not hosted observability, not LLM output, not embedding generation, not semantic retrieval quality evidence, not Evidence Ledger quality evidence, not Noise Gate quality evidence, not report quality evidence, not external reviewer feedback, not hosted deployment evidence, not customer validation, not Braincrew acceptance, and not product-complete.

The dashboard discovery link makes an existing proof surface easier to inspect. It does not make the underlying workflow, lineage, trace, or report claims stronger than their existing evidence.
