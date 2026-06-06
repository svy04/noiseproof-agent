# Runtime Persistence Verification

Status: verified.

Phase marker: Phase 1.5 runtime persistence verification.

## Purpose

Verify that the local Docker PostgreSQL/pgvector service can run and that the current FastAPI code can persist and read the Day 2 metadata boundaries.

This closes the earlier "Docker runtime verification was not performed in this environment" gap for local persistence.

## Environment Observed

```text
Docker version 29.4.3
Docker Compose version v5.1.3
Docker context -> desktop-linux
DB image -> pgvector/pgvector:pg16
POSTGRES_PORT=55432
DATABASE_URL=postgresql://noiseproof:noiseproof@localhost:55432/noiseproof
```

`docker compose config` succeeded.

`docker compose up -d db` left `noiseproof-agent-db-1` running and healthy.

`docker compose exec -T db pg_isready -U noiseproof -d noiseproof` returned:

```text
/var/run/postgresql:5432 - accepting connections
```

## Schema Evidence

The local PostgreSQL container reported the expected public tables, including:

```text
documents
agent_runs
failure_cases
document_chunks
retrieval_runs
evidence_ledger_entries
noise_gate_records
report_records
uploaded_raw_files
workflow_runs
workflow_stage_events
```

This is runtime schema visibility, not fresh-database migration proof.

## API Runtime Evidence

An existing Docker `api` container was already using port `8000`, so the current local source tree was verified with:

```text
uv run uvicorn app.main:app --host 127.0.0.1 --port 8001
```

Observed HTTP results:

```text
GET /health -> 200
GET /ops/summary -> 200
POST /documents -> 201
POST /agent-runs -> 201
POST /failure-cases -> 201
GET /documents -> 200
GET /agent-runs -> 200
GET /failure-cases -> 200
```

Persisted row ids:

```text
document -> 8b5f6062-85a0-4fca-bc37-eb821025fa2f -> Phase 1.5 Runtime Document
agent_run -> dc453904-9321-490c-8119-0e6eef7cacb2 -> Phase 1.5 runtime persistence smoke?
failure_case -> 6af7c6ea-c1ec-4811-ba90-b18fc98dd17b -> runtime_smoke_placeholder
```

The three ids were confirmed with a direct SQL lookup in the Docker PostgreSQL container.

## Boundary

This is local Docker runtime persistence evidence only.

It is not hosted deployment evidence.

It is not a fresh-database migration-run proof.

It is not production readiness.

It is not production auth, identity, RBAC, ABAC, or tenant isolation.

It is not robust PDF extraction.

It is not embedding generation.

It is not semantic retrieval quality evidence.

It is not Evidence Ledger quality evidence.

It is not external reviewer feedback.

It is not customer validation.

It is not Braincrew acceptance.

It is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, local runtime smoke for uploaded PDF encrypted failure candidate if needed, or another source-first product gate selected from docs/GOAL.md
```
