# Fresh DB API smoke verification

## Status

Accepted.

## Scope

This review verifies that the API can start against an isolated fresh Docker database after the lightweight migration runner applies all pending SQL migrations.

The goal is a small service-path smoke check, not a hosted deployment claim.

## Verification environment

```text
Date: 2026-05-30
Compose project: noiseproof-agent-api-smoke
Database port: POSTGRES_PORT=55435
API port: 8018
Database URL: postgresql://noiseproof:noiseproof@localhost:55435/noiseproof
```

## Commands

```powershell
POSTGRES_PORT=55435 docker compose -p noiseproof-agent-api-smoke up -d db
docker compose -p noiseproof-agent-api-smoke exec -T db pg_isready -U noiseproof -d noiseproof

cd apps/api
$env:DATABASE_URL="postgresql://noiseproof:noiseproof@localhost:55435/noiseproof"
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8018

Invoke-RestMethod http://127.0.0.1:8018/health
Invoke-RestMethod http://127.0.0.1:8018/ops/summary
Invoke-RestMethod http://127.0.0.1:8018/documents -Method Post -ContentType "application/json" -Body '{...}'
Invoke-RestMethod http://127.0.0.1:8018/documents

POSTGRES_PORT=55435 docker compose -p noiseproof-agent-api-smoke down -v
```

## Migration runner evidence

Before apply:

```text
Applied migrations: 0
Pending migrations: 9
pending 002_evidence_ledger_entries.sql
pending 003_noise_gate_records.sql
pending 004_report_records.sql
pending 005_workflow_trace_ids.sql
pending 006_child_agent_run_ids.sql
pending 007_workflow_runs.sql
pending 008_child_workflow_run_ids.sql
pending 009_stage_input_manifest.sql
pending 010_workflow_version_defaults.sql
```

Apply result:

```text
Applied migrations: 0
Pending migrations: 9
applied 002_evidence_ledger_entries.sql
applied 003_noise_gate_records.sql
applied 004_report_records.sql
applied 005_workflow_trace_ids.sql
applied 006_child_agent_run_ids.sql
applied 007_workflow_runs.sql
applied 008_child_workflow_run_ids.sql
applied 009_stage_input_manifest.sql
applied 010_workflow_version_defaults.sql
```

After apply:

```text
Applied migrations: 9
Pending migrations: 0
```

## API smoke evidence

GET /health:

```text
status_code: 200
status: ok
service: noiseproof-agent-api
workflow_version: phase40-lineage-warning-code-dashboard
```

GET /ops/summary before document create:

```text
status_code: 200
status: placeholder
document_count: 0
workflow_version: phase40-lineage-warning-code-dashboard
```

POST /documents:

```text
status_code: 201
source_type: markdown
source_uri: sample://fresh-db-api-smoke.md
title: Sample fresh DB smoke document
source_date: 2026-05-30
status: registered
```

GET /documents:

```text
status_code: 200
title: Sample fresh DB smoke document
source_uri: sample://fresh-db-api-smoke.md
status: registered
```

GET /ops/summary after document create:

```text
status_code: 200
document_count: 1
workflow_version: phase40-lineage-warning-code-dashboard
```

## Cleanup

The isolated test volume was removed with:

```powershell
POSTGRES_PORT=55435 docker compose -p noiseproof-agent-api-smoke down -v
```

## Boundary

This verifies a local API smoke path against a fresh migrated Docker DB. It does not claim hosted deployment readiness, production migration orchestration, rollback behavior, file parsing, robust PDF extraction, persisted chunks, embeddings, semantic retrieval, LLM-backed workflow execution, dashboard polish, or free-form final answer generation.

## Next gate

The next bounded gate should be application evidence index refresh v0: update the application-facing docs so reviewers can find the newest migration/runtime verification artifacts without implying the product is complete.
