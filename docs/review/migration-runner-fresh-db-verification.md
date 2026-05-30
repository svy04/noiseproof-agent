# Migration runner fresh DB verification

## Status

Accepted.

## Scope

This review verifies the lightweight SQL migration runner on an isolated fresh Docker Compose database.

The goal is narrower than production migration orchestration. It checks that a database initialized from `db/init/001_schema.sql` can still accept the pending SQL files in `db/migrations/*.sql` through the runner and record them in `schema_migrations`.

## Verification environment

```text
Date: 2026-05-30
Compose project: noiseproof-agent-fresh
Database port: POSTGRES_PORT=55433
Database URL: postgresql://noiseproof:noiseproof@localhost:55433/noiseproof
```

The verification used an isolated Compose project so it did not mutate the normal local database volume.

## Commands

```powershell
POSTGRES_PORT=55433 docker compose -p noiseproof-agent-fresh up -d db
cd apps/api
$env:DATABASE_URL="postgresql://noiseproof:noiseproof@localhost:55433/noiseproof"
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
docker compose -p noiseproof-agent-fresh exec -T db psql -U noiseproof -d noiseproof -c "SELECT table_name, column_default FROM information_schema.columns WHERE table_schema = 'public' AND table_name IN ('agent_runs', 'workflow_runs') AND column_name = 'workflow_version' ORDER BY table_name;"
docker compose -p noiseproof-agent-fresh exec -T db psql -U noiseproof -d noiseproof -c "SELECT filename FROM schema_migrations ORDER BY filename;"
POSTGRES_PORT=55433 docker compose -p noiseproof-agent-fresh down -v
```

## Initial runner status

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

## Runner apply result

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

## Final runner status

```text
Applied migrations: 9
Pending migrations: 0
```

## Schema default check

```text
table_name   | column_default
-------------+------------------------------------------------
agent_runs    | 'phase40-lineage-warning-code-dashboard'::text
workflow_runs | 'phase40-lineage-warning-code-dashboard'::text
```

## schema_migrations check

```text
002_evidence_ledger_entries.sql
003_noise_gate_records.sql
004_report_records.sql
005_workflow_trace_ids.sql
006_child_agent_run_ids.sql
007_workflow_runs.sql
008_child_workflow_run_ids.sql
009_stage_input_manifest.sql
010_workflow_version_defaults.sql
```

## Cleanup

The isolated test volume was removed with:

```powershell
POSTGRES_PORT=55433 docker compose -p noiseproof-agent-fresh down -v
```

## Boundary

This verifies the apply path on a fresh local Docker database. It does not claim hosted deployment safety, rollback support, environment promotion, production backup coverage, Alembic parity, API-based migration execution, dashboard migration visibility, LLM behavior, embeddings, semantic retrieval, autonomous workflow execution, or free-form final answer generation.

## Next gate

The next bounded gate should be migration runner runbook cleanup v0: make the runbook's old manual SQL migration path clearly secondary to the runner, while preserving manual commands as emergency/debug references.
