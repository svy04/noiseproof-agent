# Retrieval-run-linked Evidence Ledger Runtime Smoke v0

Date: 2026-06-02

Status: local Docker DB plus live FastAPI HTTP smoke completed.

## Why This Smoke Exists

The route-level test proves API behavior in memory. This smoke checks the persistence path against the local PostgreSQL/pgvector service, migration runner, and live HTTP calls.

## Environment

```text
Docker version: 29.4.3
Database: pgvector/pgvector:pg16
Published port: localhost:55432
API: http://127.0.0.1:8000
```

## Migration Observation

Before applying the new migration:

```text
Applied migrations: 12
Pending migrations: 1
pending 014_evidence_ledger_retrieval_run_id.sql
```

After applying:

```text
Applied migrations: 13
Pending migrations: 0
```

## HTTP Sequence

Observed live HTTP calls:

```text
GET /health -> 200
POST /documents -> 201
POST /documents/{document_id}/chunks -> 201
POST /documents/{document_id}/chunks -> 201
POST /documents/{document_id}/retrieval-runs -> 201
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger -> 201
GET /evidence-ledgers -> 200
```

## Observed Linkage

```json
{
  "health_status": "ok",
  "document_id": "86b19b95-1e4d-4d80-9737-289a9106591c",
  "demand_chunk_id": "31d1d3c2-d922-4f2a-9b98-dcb7cb15be5f",
  "retrieval_run_id": "832f21c6-53ee-407b-ad55-f85bec4082c4",
  "retrieval_result_count": 1,
  "retrieval_candidate_chunk_ids": "31d1d3c2-d922-4f2a-9b98-dcb7cb15be5f",
  "ledger_status": "supported",
  "ledger_retrieval_run_id": "832f21c6-53ee-407b-ad55-f85bec4082c4",
  "ledger_source_id": "31d1d3c2-d922-4f2a-9b98-dcb7cb15be5f",
  "ledger_stored_entry_count": 1,
  "listed_first_retrieval_run_id": "832f21c6-53ee-407b-ad55-f85bec4082c4"
}
```

The persisted Evidence Ledger row kept the same `retrieval_run_id` as the retrieval run used for the handoff.

## Boundary Warnings Observed

```text
Evidence Ledger entries were generated from a persisted retrieval_run over document_chunks.
This handoff uses stored candidate_chunk_ids; it makes no LLM call, creates no embeddings, and does not perform semantic retrieval.
This handoff does not judge final truth or provide financial advice.
Evidence Ledger Preview does not judge final truth or generate a final report.
Entries are derived from retrieval candidates and must still pass a future Critic / Noise Gate.
```

## Claim Boundary

Allowed claim:

```text
Local Docker runtime evidence exists for a persisted retrieval-run-to-Evidence-Ledger handoff.
```

Forbidden claims:

```text
This is not hosted deployment evidence.
This is not external reviewer feedback.
This is not customer validation.
This is not semantic retrieval.
This is not embeddings.
This is not LLM judgment.
This is not Noise Gate or report generation.
This is not financial advice.
```
