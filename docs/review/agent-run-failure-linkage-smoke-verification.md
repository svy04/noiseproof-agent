# Agent-run failure linkage smoke verification

## Status

Accepted.

## Scope

This review verifies that a manually created failure case can be linked to a persisted `agent_runs` row through `failure_cases.agent_run_id` on an isolated fresh migrated Docker database.

The goal is narrow foreign-key provenance smoke. It does not claim automatic failure detection, workflow-level failure causality, or incident-management behavior.

## Verification environment

```text
Date: 2026-05-30
Compose project: noiseproof-agent-failure-link-smoke
Database port: POSTGRES_PORT=55437
API port: 8020
Database URL: postgresql://noiseproof:noiseproof@localhost:55437/noiseproof
```

## Commands

```powershell
POSTGRES_PORT=55437 docker compose -p noiseproof-agent-failure-link-smoke up -d db
docker compose -p noiseproof-agent-failure-link-smoke exec -T db pg_isready -U noiseproof -d noiseproof

cd apps/api
$env:DATABASE_URL="postgresql://noiseproof:noiseproof@localhost:55437/noiseproof"
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8020

Invoke-RestMethod http://127.0.0.1:8020/health
Invoke-RestMethod http://127.0.0.1:8020/agent-runs -Method Post -ContentType "application/json" -Body '{...}'
Invoke-RestMethod http://127.0.0.1:8020/failure-cases -Method Post -ContentType "application/json" -Body '{...}'
Invoke-RestMethod http://127.0.0.1:8020/failure-cases
Invoke-RestMethod http://127.0.0.1:8020/agent-runs
Invoke-RestMethod http://127.0.0.1:8020/ops/summary

POSTGRES_PORT=55437 docker compose -p noiseproof-agent-failure-link-smoke down -v
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

POST /agent-runs:

```text
status_code: 201
user_question: Why did parser preview fail for the uploaded market note?
workflow_version: phase40-lineage-warning-code-dashboard
status: failed
error_message: simulated parser timeout for smoke verification
trace_json.smoke: agent-run-failure-linkage
```

POST /failure-cases:

```text
status_code: 201
agent_run_id: d276bdc4-ae46-4759-90a1-086094251fcf
failure_type: linked_parser_timeout
root_cause: simulated parser timeout
fix_status: open
```

GET /failure-cases:

```text
status_code: 200
agent_run_id: d276bdc4-ae46-4759-90a1-086094251fcf
failure_type: linked_parser_timeout
root_cause: simulated parser timeout
```

GET /agent-runs:

```text
status_code: 200
id: d276bdc4-ae46-4759-90a1-086094251fcf
status: failed
trace_json.smoke: agent-run-failure-linkage
```

GET /ops/summary:

```text
status_code: 200
agent_run_count: 1
failure_case_count: 1
```

## Cleanup

The isolated test volume was removed with:

```powershell
POSTGRES_PORT=55437 docker compose -p noiseproof-agent-failure-link-smoke down -v
```

## Boundary

This verifies local `agent_run_id` linkage for manually created failure cases on a fresh migrated Docker DB. It does not claim automatic failure detection, complete workflow failure causality, repair automation, hosted deployment evidence, distributed tracing, external observability, LLM-backed failure analysis, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

## Next gate

The next bounded gate should be agent-run failure linkage application refresh v0: expose this linked-failure proof in application-facing docs without implying automatic detection or full workflow causality.
