# Runtime DB schema default verification

Status: accepted

## Scope

Docker runtime verification performed for the workflow-version schema defaults.

This verifies the local PostgreSQL schema default state only. It does not verify workflow execution semantics, retrieval quality, Evidence Ledger quality, Noise Gate quality, dashboard analytics, or distributed tracing.

## Environment

- Date: 2026-05-30
- Docker server: 29.4.3
- Compose service: `db`
- Container: `noiseproof-agent-db`
- Port mapping from local `.env`: `55432 -> 5432`
- Database: `noiseproof`

## Commands

```powershell
docker compose up -d db
docker compose ps
docker compose exec -T db psql -U noiseproof -d noiseproof -c "SELECT table_name, column_default FROM information_schema.columns WHERE table_schema = 'public' AND column_name = 'workflow_version' AND table_name IN ('agent_runs', 'workflow_runs') ORDER BY table_name;"
Get-Content -Path db\migrations\010_workflow_version_defaults.sql | docker compose exec -T db psql -U noiseproof -d noiseproof
docker compose exec -T db psql -U noiseproof -d noiseproof -c "SELECT table_name, column_default FROM information_schema.columns WHERE table_schema = 'public' AND column_name = 'workflow_version' AND table_name IN ('agent_runs', 'workflow_runs') ORDER BY table_name;"
```

## Initial observed defaults before applying migration 010

```text
agent_runs    | 'phase5.5-collection-plan-preview'::text
workflow_runs | 'phase24-workflow-run-schema'::text
```

Interpretation:

The existing Docker volume predated Phase 42. Fresh init SQL was already fixed, but this local runtime database still carried stale executable defaults until the forward migration was applied.

## Migration application

```text
ALTER TABLE
ALTER TABLE
```

No volume deletion was performed.

## Observed defaults after applying migration 010

```text
agent_runs    | 'phase40-lineage-warning-code-dashboard'::text
workflow_runs | 'phase40-lineage-warning-code-dashboard'::text
```

## Boundary

This verification proves that the current local Docker database can be brought to the current workflow-version defaults by applying `db/migrations/010_workflow_version_defaults.sql`.

It does not prove that all future environments run migrations automatically. A later gate may add a migration runner or an explicit migration command to the runbook if needed.
