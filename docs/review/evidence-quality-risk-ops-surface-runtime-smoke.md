# Evidence Quality Risk Ops Surface Runtime Smoke

Phase marker: evidence quality risk ops surface runtime smoke v0

## Scope

Verify the Phase 689 ops summary/dashboard counts against local Docker PostgreSQL and a live FastAPI process.

## Environment

```text
Docker version: 29.4.3
Docker Compose version: v5.1.3
Compose project: noiseproof-phase689
POSTGRES_PORT: 55450
API port: 8107
DATABASE_URL: postgresql://noiseproof:noiseproof@localhost:55450/noiseproof
```

## Commands

```powershell
$env:POSTGRES_PORT='55450'
docker compose -p noiseproof-phase689 up -d db

uv run python -m app.migration_runner --database-url postgresql://noiseproof:noiseproof@localhost:55450/noiseproof

$env:DATABASE_URL='postgresql://noiseproof:noiseproof@localhost:55450/noiseproof'
uv run uvicorn app.main:app --host 127.0.0.1 --port 8107
```

## Observed Evidence

Migration runner:

```text
Applied migrations: 0
Pending migrations: 23
applied 002_evidence_ledger_entries.sql
...
applied 024_workflow_stage_events.sql
```

Live HTTP server logs:

```text
POST /evidence-ledgers HTTP/1.1 -> 201 Created
GET /ops/summary HTTP/1.1 -> 200 OK
GET /ops/dashboard HTTP/1.1 -> 200 OK
```

`GET /ops/summary` after one persisted weak Evidence Ledger row:

```text
weakly_supported_evidence_count    : 1
low_confidence_evidence_count      : 1
missing_source_date_evidence_count : 1
evidence_quality_risk_count        : 1
```

`GET /ops/dashboard` contained:

```text
Weak Evidence -> true
Low Confidence Evidence -> true
Missing Source Dates -> true
Evidence quality risk counts are operations metadata -> true
```

## Boundary

This is local runtime evidence only. It proves the new persisted-row ops counts and dashboard markers work against a fresh local PostgreSQL database. It is not hosted deployment evidence, not final truth adjudication, not retrieval quality evidence, not Evidence Ledger quality evidence, not embedding generation, not an LLM call, not external reviewer feedback, and not product-complete.

## Cleanup

```powershell
docker compose -p noiseproof-phase689 down -v
```
