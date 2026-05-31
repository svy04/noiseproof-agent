# Failure-case workflow parent linkage fresh DB verification

## Status

Accepted.

This is local fresh migrated Docker DB evidence, not hosted deployment evidence.

## Scope

This smoke verifies that the new nullable `failure_cases.workflow_run_id` schema works through a real FastAPI process backed by an isolated fresh migrated PostgreSQL database.

The goal is narrow runtime proof. It does not add automatic failure-case creation, automatic failure-case persistence, incident classification, hosted deployment evidence, or complete workflow failure causality.

## Verification environment

```text
Date: 2026-05-31
Compose project: noiseproof-agent-workflow-link-smoke
Database port: POSTGRES_PORT=55440
API port: 8024
Database URL: postgresql://noiseproof:noiseproof@localhost:55440/noiseproof
Workflow run id: 19cf894c-22c1-417f-9472-fbc01b654f2b
```

## Commands

```powershell
$env:POSTGRES_PORT='55440'
docker compose -p noiseproof-agent-workflow-link-smoke up -d db
docker compose -p noiseproof-agent-workflow-link-smoke exec -T db pg_isready -U noiseproof -d noiseproof

cd apps/api
$env:DATABASE_URL="postgresql://noiseproof:noiseproof@localhost:55440/noiseproof"
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8024

Invoke-RestMethod http://127.0.0.1:8024/health
Invoke-RestMethod http://127.0.0.1:8024/workflow-runs -Method Post -ContentType "application/json" -Body '{...}'
Invoke-RestMethod http://127.0.0.1:8024/failure-cases -Method Post -ContentType "application/json" -Body '{...}'
Invoke-RestMethod http://127.0.0.1:8024/failure-cases
Invoke-RestMethod http://127.0.0.1:8024/ops/summary

docker compose -p noiseproof-agent-workflow-link-smoke down -v
```

## Migration runner evidence

Before apply:

```text
Applied migrations: 0
Pending migrations: 10
pending 002_evidence_ledger_entries.sql
pending 003_noise_gate_records.sql
pending 004_report_records.sql
pending 005_workflow_trace_ids.sql
pending 006_child_agent_run_ids.sql
pending 007_workflow_runs.sql
pending 008_child_workflow_run_ids.sql
pending 009_stage_input_manifest.sql
pending 010_workflow_version_defaults.sql
pending 011_failure_case_workflow_run_id.sql
```

Apply result:

```text
Applied migrations: 0
Pending migrations: 10
applied 002_evidence_ledger_entries.sql
applied 003_noise_gate_records.sql
applied 004_report_records.sql
applied 005_workflow_trace_ids.sql
applied 006_child_agent_run_ids.sql
applied 007_workflow_runs.sql
applied 008_child_workflow_run_ids.sql
applied 009_stage_input_manifest.sql
applied 010_workflow_version_defaults.sql
applied 011_failure_case_workflow_run_id.sql
```

After apply:

```text
Applied migrations: 10
Pending migrations: 0
```

## API smoke evidence

GET /health:

```text
health_status: ok
```

POST /workflow-runs:

```text
workflow_status: failed
workflow_run_id: 19cf894c-22c1-417f-9472-fbc01b654f2b
```

POST /failure-cases:

```text
persisted_workflow_run_id: 19cf894c-22c1-417f-9472-fbc01b654f2b
persisted_workflow_run_id_matches: true
```

GET /failure-cases:

```text
listed_failure_case_count: 1
listed_workflow_run_id: 19cf894c-22c1-417f-9472-fbc01b654f2b
listed_workflow_run_id_matches: true
```

GET /ops/summary:

```text
ops_failure_case_count: 1
```

## Cleanup

The isolated test volume was removed with:

```powershell
docker compose -p noiseproof-agent-workflow-link-smoke down -v
```

## Boundary

This verifies local manual workflow-parent failure-case linkage against a fresh migrated Docker DB. It is not automatic failure-case creation, automatic failure detection, automatic failure-case persistence, a confirm endpoint, hosted deployment evidence, production incident handling, complete workflow failure causality, distributed tracing, external observability, LLM-backed failure analysis, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

## Next bounded gate

The next bounded gate should be:

```text
failure-case workflow parent linkage application refresh v0
```

That gate should expose this runtime proof in application-facing docs without implying automatic failure-case creation, hosted deployment evidence, or complete workflow failure causality.
