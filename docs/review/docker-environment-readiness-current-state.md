# Docker Environment Readiness Current-state

Status: implemented.

Phase marker: docker environment readiness current-state v0.

## Purpose

Verify that the local Docker environment is ready to support NoiseProof runtime proof work.

Docker is needed here because NoiseProof persistence and service claims depend on PostgreSQL/pgvector behavior, ordered SQL migrations, and live FastAPI HTTP calls against a database-backed service. Unit tests alone cannot prove those runtime boundaries.

## Observed Environment

```text
Docker version `29.4.3`
Docker Compose version `v5.1.3`
Docker server version `29.4.3`
Ubuntu -> Running -> 2
docker-desktop -> Running -> 2
```

## Compose Check

```text
docker compose config -> passed
compose project used for isolated smoke -> noiseproof-phase611
POSTGRES_PORT=55440
```

The rendered config used the `pgvector/pgvector:pg16` database service, a project-scoped network, a project-scoped volume, and the repo-local `db/init` SQL directory.

## Runtime Check

```text
docker compose -p noiseproof-phase611 up -d db -> started
initial pg_isready -> no response while health was starting
later db status -> healthy
pg_isready -> accepting connections
extensions -> pgcrypto, vector
migration apply -> applied 002 through 024
migration status -> pending migrations 0
GET /health -> 200
GET /ops/summary -> 200
docker compose -p noiseproof-phase611 down -v -> cleaned up
```

Observed `/health` response:

```json
{
  "status": "ok",
  "service": "noiseproof-agent-api",
  "workflow_version": "phase40-lineage-warning-code-dashboard"
}
```

Observed `/ops/summary` response had `status=placeholder`, zero records in the fresh database, and notes preserving the boundaries around deterministic previews, metadata-derived PDF diagnostics, raw file guard records, and still-unimplemented semantic retrieval/distributed tracing/final report generation.

## Boundary

This is local Docker environment readiness evidence only.

This is not hosted deployment evidence.

This is not production orchestration.

This is not Kubernetes readiness.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not robust PDF extraction.

This is not table extraction.

This is not semantic retrieval quality evidence.

This is not live OpenAI provider evidence.

This is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
