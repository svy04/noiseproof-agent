# Failure-case persistence smoke verification

## Status

Accepted.

## Scope

This review verifies that the failure-case persistence API works against an isolated fresh Docker database after the lightweight migration runner applies all pending migrations.

The goal is a narrow failure-ledger smoke check. It does not test automated failure detection or production incident handling.

## Verification environment

```text
Date: 2026-05-30
Compose project: noiseproof-agent-failure-smoke
Database port: POSTGRES_PORT=55436
API port: 8019
Database URL: postgresql://noiseproof:noiseproof@localhost:55436/noiseproof
```

## Commands

```powershell
POSTGRES_PORT=55436 docker compose -p noiseproof-agent-failure-smoke up -d db
docker compose -p noiseproof-agent-failure-smoke exec -T db pg_isready -U noiseproof -d noiseproof

cd apps/api
$env:DATABASE_URL="postgresql://noiseproof:noiseproof@localhost:55436/noiseproof"
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8019

Invoke-RestMethod http://127.0.0.1:8019/health
Invoke-RestMethod http://127.0.0.1:8019/ops/summary
Invoke-RestMethod http://127.0.0.1:8019/failure-cases -Method Post -ContentType "application/json" -Body '{...}'
Invoke-RestMethod http://127.0.0.1:8019/failure-cases
Invoke-RestMethod http://127.0.0.1:8019/ops/summary

POSTGRES_PORT=55436 docker compose -p noiseproof-agent-failure-smoke down -v
```

## Migration runner evidence

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

Final migration status:

```text
Applied migrations: 9
Pending migrations: 0
```

## API smoke evidence

GET /health:

```text
status_code: 200
status: ok
workflow_version: phase40-lineage-warning-code-dashboard
```

GET /ops/summary before failure creation:

```text
status_code: 200
failure_case_count: 0
```

POST /failure-cases:

```text
status_code: 201
failure_type: parser_timeout
description: Parser preview exceeded local smoke timeout.
root_cause: simulated parser timeout
fix_status: open
next_action: Record parser timeout and keep the source out of report generation until retried.
```

GET /failure-cases:

```text
status_code: 200
failure_type: parser_timeout
root_cause: simulated parser timeout
fix_status: open
```

GET /ops/summary after failure creation:

```text
status_code: 200
failure_case_count: 1
```

## Cleanup

The isolated test volume was removed with:

```powershell
POSTGRES_PORT=55436 docker compose -p noiseproof-agent-failure-smoke down -v
```

## Boundary

This verifies local failure-case persistence against a fresh migrated Docker DB. It does not claim automatic failure classification, production incident handling, hosted deployment readiness, distributed tracing, external observability, LLM-backed failure analysis, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

## Next gate

The next bounded gate should be failure-case application evidence refresh v0: expose this failure-ledger smoke artifact in application-facing docs without implying automatic failure detection.
