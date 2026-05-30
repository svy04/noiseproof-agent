# Failure-case draft fresh DB handoff smoke verification

## Status

Accepted.

This is local fresh migrated Docker DB evidence, not hosted deployment evidence.

## Scope

This smoke verifies that the manual draft-to-persistence handoff works through a real FastAPI process backed by an isolated fresh migrated PostgreSQL database.

The goal is narrow runtime proof. It does not add automatic persistence, a confirm endpoint, incident classification, or complete workflow failure causality.

## Verification environment

```text
Date: 2026-05-30
Compose project: noiseproof-agent-draft-handoff-smoke
Database port: POSTGRES_PORT=55438
API port: 8022
Database URL: postgresql://noiseproof:noiseproof@localhost:55438/noiseproof
Workflow run id: 70aa76f2-f8fb-4a57-a507-73de2e310ddd
```

## Commands

```powershell
POSTGRES_PORT=55438 docker compose -p noiseproof-agent-draft-handoff-smoke up -d db
docker compose -p noiseproof-agent-draft-handoff-smoke exec -T db pg_isready -U noiseproof -d noiseproof

cd apps/api
$env:DATABASE_URL="postgresql://noiseproof:noiseproof@localhost:55438/noiseproof"
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8022

Invoke-RestMethod http://127.0.0.1:8022/health
Invoke-RestMethod http://127.0.0.1:8022/failure-cases/draft-preview -Method Post -ContentType "application/json" -Body '{...}'
Invoke-RestMethod http://127.0.0.1:8022/failure-cases
Invoke-RestMethod http://127.0.0.1:8022/failure-cases -Method Post -ContentType "application/json" -Body '{...}'
Invoke-RestMethod http://127.0.0.1:8022/failure-cases
Invoke-RestMethod http://127.0.0.1:8022/ops/summary

POSTGRES_PORT=55438 docker compose -p noiseproof-agent-draft-handoff-smoke down -v
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
status: ok
workflow_version: phase40-lineage-warning-code-dashboard
```

POST /failure-cases/draft-preview:

```text
preview_persistence_boundary: preview_only_not_persisted
preview_human_confirmation_required: true
draft_failure_type: workflow_stage_error
draft_fix_status: draft
```

GET /failure-cases before manual handoff:

```text
before_failure_case_count: 0
```

POST /failure-cases with human-confirmed draft:

```text
persisted_failure_type: workflow_stage_error
persisted_fix_status: open
persisted_root_cause: RuntimeError: simulated evidence persistence failure
```

GET /failure-cases after manual handoff:

```text
after_failure_case_count: 1
```

GET /ops/summary:

```text
ops_failure_case_count: 1
```

## Cleanup

The isolated test volume was removed with:

```powershell
POSTGRES_PORT=55438 docker compose -p noiseproof-agent-draft-handoff-smoke down -v
```

## Boundary

This verifies local draft-to-persistence handoff against a fresh migrated Docker DB. It does not claim automatic failure detection, automatic failure-case persistence, a confirm endpoint, hosted deployment evidence, production incident handling, complete workflow failure causality, distributed tracing, external observability, LLM-backed failure analysis, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

## Next gate

The next bounded gate should be failure-case draft fresh-db handoff application refresh v0: expose this runtime proof in application-facing docs without implying automatic persistence, hosted deployment evidence, or complete workflow failure causality.
