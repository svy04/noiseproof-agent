# Uploaded File Retrieval Persistence Runtime Smoke

Phase marker: uploaded file retrieval persistence runtime smoke v0.

Status: local runtime evidence.

This smoke uses Docker because the claim depends on PostgreSQL/pgvector persistence and live FastAPI HTTP calls, not only in-memory route tests.

## Commands

```powershell
docker compose up -d db
docker compose ps
cd apps/api
$env:DATABASE_URL="postgresql://noiseproof:noiseproof@localhost:55432/noiseproof"
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8035
```

The live HTTP smoke then used:

```powershell
GET /health
POST /documents/upload-chunks
POST /documents/{document_id}/retrieval-runs
GET /retrieval-runs
```

The JSON POST body was sent through `Invoke-RestMethod -ContentType application/json` to avoid shell quoting ambiguity.

## Observed Result

```text
docker compose ps -> db healthy
Applied migrations: 12
Pending migrations: 0
GET /health -> 200
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/retrieval-runs -> 201
GET /retrieval-runs -> 200
health_status -> ok
upload_status -> chunked_metadata_only
document_id -> d09e2296-6bf6-486c-84e7-7f01b56e23cc
upload_chunk_count -> 4
retrieval_status -> completed
retrieval_result_count -> 2
retrieval_missing_evidence_count -> 0
metadata_source_table -> document_chunks
metadata_document_id -> d09e2296-6bf6-486c-84e7-7f01b56e23cc
metadata_candidate_chunk_ids -> 3bbef26c-44a2-467a-8255-55be7791bb0a,687cc699-2c34-4eae-a90a-79cf1ad86b54
retrieval_list_count -> 4
latest_listed_id_matches -> True
latest_listed_candidate_chunk_ids -> 3bbef26c-44a2-467a-8255-55be7791bb0a,687cc699-2c34-4eae-a90a-79cf1ad86b54
first_candidate_source_table -> document_chunks
first_candidate_chunk_id -> 3bbef26c-44a2-467a-8255-55be7791bb0a
```

First candidate text:

```text
improved in Q1.
- Channel checks still show delayed enterprise renewals.
- Revenue grew 12%, but gross margin
```

Warning sample:

```text
Document retrieval uses existing document_chunks rows as the source table.
This retrieval run stores candidate_chunk_ids only and does not generate Evidence Ledger entries.
This retrieval run is not financial advice.
```

## Boundary

This is local runtime evidence only.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not customer validation.

It is not Braincrew acceptance.

It is not production readiness.

It adds no schema, migration, retrieval-candidates table, embeddings, semantic retrieval, Evidence Ledger records, Noise Gate records, report records, LLM output, financial advice, or product-complete claim.

Explicit non-claims:

```text
no Evidence Ledger generation
not financial advice
no hosted deployment evidence
no external reviewer feedback
```

## Next Gate

The next product packaging gate should be:

```text
uploaded file retrieval persistence application refresh v0
```
