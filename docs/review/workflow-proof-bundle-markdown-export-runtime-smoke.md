# Workflow Proof Bundle Markdown Export Runtime Smoke

Status: accepted.

Phase marker: workflow proof bundle markdown export runtime smoke v0.

## Purpose

Verify the workflow proof bundle markdown export against local Docker PostgreSQL plus live FastAPI HTTP.

This smoke checks that a reviewer can move from `GET /ops/dashboard` to the markdown proof bundle export for a freshly created deterministic workflow preview.

## Environment

```text
Docker version: 29.4.3
Docker Compose version: v5.1.3
Compose project: noiseproof-phase666
POSTGRES_PORT=55449
database container: noiseproof-phase666-db-1
database status: healthy
DATABASE_URL: postgresql://noiseproof:noiseproof@127.0.0.1:55449/noiseproof
FastAPI URL: http://127.0.0.1:8106
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
$env:POSTGRES_PORT='55449'
docker compose -p noiseproof-phase666 config
docker compose -p noiseproof-phase666 up -d db
docker compose -p noiseproof-phase666 ps db
docker compose -p noiseproof-phase666 exec -T db pg_isready -U noiseproof -d noiseproof

$env:DATABASE_URL='postgresql://noiseproof:noiseproof@127.0.0.1:55449/noiseproof'
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8106
```

Then:

```text
GET  /health
POST /workflow-runs/execute-preview
GET  /ops/dashboard
GET  /workflow-runs/{id}/proof-bundle/markdown
GET  /workflow-runs/{id}/proof-bundle
```

Cleanup:

```text
stopped_process: 79068
docker compose -p noiseproof-phase666 down -v -> completed
```

## Observed Result

```text
health_status_code: 200
health_status: ok
workflow_version: phase40-lineage-warning-code-dashboard
execute_preview_status_code: 201
workflow_run_id: 49a344bb-dbb4-46d4-bdcb-a0edbb20126c
workflow_trace_id: b1cfd8dc-8360-4efa-9638-a0acf1ef9bf2
dashboard_status_code: 200
dashboard_contains_proof_markdown_link: true
dashboard_contains_get_only_boundary: true
GET /workflow-runs/{id}/proof-bundle/markdown -> 200
markdown_status_code: 200
markdown_content_type: text/markdown; charset=utf-8
markdown_starts_with_heading: true
markdown_contains_reviewer_checklist: true
markdown_contains_boundary: true
markdown_contains_not_hosted_observability: true
markdown_contains_not_product_complete: true
proof_bundle_status_code: 200
proof_bundle_reviewer_checklist_count: 4
proof_bundle_warning_count: 2
proof_bundle_boundary: read_model_only_existing_records_no_new_storage
proof_surface_count: 3
```

The dashboard link target was:

```text
GET /workflow-runs/{id}/proof-bundle/markdown
```

The link label was:

```text
proof markdown
```

## Interpretation

The local dashboard now routes a reviewer from a workflow row to a markdown rendering of the workflow proof bundle without requiring manual URL construction or JSON inspection first.

The markdown export includes:

```text
# Workflow Proof Bundle
## Summary Counts
## Proof Surfaces
## Reviewer Checklist
## Warnings
## Boundary
```

The markdown export remains a read-only rendering of the existing workflow proof bundle read model.

## Boundary

This smoke is local Docker PostgreSQL plus live FastAPI HTTP evidence only.

It is not new storage.

It is not a new workflow execution path.

It is not distributed tracing.

It is not hosted observability.

It is not hosted deployment evidence.

It is not semantic retrieval quality evidence.

It is not embedding generation.

It is not Evidence Ledger quality evidence.

It is not Noise Gate quality evidence.

It is not report quality evidence.

It is not external reviewer feedback.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.

## Notes

An earlier PowerShell `Invoke-WebRequest` attempt raised a local client-side `NullReferenceException` and produced invalid empty-id 404 requests. This was not used as the acceptance smoke.

The accepted smoke used Python standard-library HTTP requests against the same live FastAPI process and returned the 200 results recorded above.

## Next Gate

```text
external-reader proof path markdown export route refresh v0 if this proof should become the latest reviewer route, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
