# Uploaded PDF Retrieval-run-linked Evidence Ledger Provenance Runtime Smoke

Status: local Docker DB plus live FastAPI HTTP smoke completed.

Phase marker: uploaded PDF retrieval-run-linked Evidence Ledger provenance runtime smoke v0.

This smoke records local runtime evidence that the Phase 352 route-level/schema provenance path works against the Docker PostgreSQL service, migration runner, rebuilt FastAPI API container, multipart uploaded digital PDF bytes, and persisted Evidence Ledger rows.

## Environment

```text
Docker version 29.4.3
Docker Compose version v5.1.3
DB image -> sha256:00ba258a66dac104fd5171074a0084462a64a1369d8513f3d0a634e2f24d15bc
DB status -> running
DB health -> healthy
API image -> sha256:4f7b97f9eb60f8335fcb8c70d3a76d76569abe66331f484c8fea696ce74b0f23
API started -> 2026-06-04T07:19:39.22618694Z
```

## Commands

```powershell
docker version --format "Docker version {{.Server.Version}}"
docker compose version
docker compose config
docker compose --profile api config
docker compose --profile api up -d --build api
docker compose --profile api ps
cd apps/api
$env:DATABASE_URL='postgresql://noiseproof:noiseproof@localhost:55432/noiseproof'
uv run python -m app.migration_runner --status
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
```

HTTP smoke:

```text
GET /health
POST /documents/upload-chunks
POST /documents/{document_id}/retrieval-runs
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger
GET /evidence-ledgers?retrieval_run_id=
```

The PDF was generated in memory with PyMuPDF and uploaded as multipart `application/pdf`. No PDF file was committed to the repository.

## Migration Observation

Before applying the new migration:

```text
Applied migrations: 16
Pending migrations: 1
pending 018_evidence_ledger_metadata_json.sql
```

Apply command:

```text
Applied migrations: 16
Pending migrations: 1
applied 018_evidence_ledger_metadata_json.sql
```

After applying:

```text
Applied migrations: 17
Pending migrations: 0
```

## Observed HTTP Results

```text
GET /health -> 200
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/retrieval-runs -> 201
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger -> 201
GET /evidence-ledgers?retrieval_run_id= -> 200
health_status -> ok
document_id -> 415a41f3-5f04-424a-b069-9e3c6906d723
chunk_id -> a19c53ec-53d6-456e-8ff0-48e0908825d8
retrieval_run_id -> 5e873891-9e40-435c-b350-dc96325038e9
ledger_entry_id -> 9fd9a061-9aad-4d2b-8cb3-911e4d636f88
upload_parser -> pdf-pymupdf
upload_digital_pdf_text_extraction -> true
upload_robust_pdf_extraction -> false
retrieval_candidate_parsers -> pdf-pymupdf
retrieval_digital_pdf_text_extraction -> true
retrieval_robust_pdf_extraction -> false
metadata_json.parser -> pdf-pymupdf
metadata_json.digital_pdf_text_extraction -> true
metadata_json.robust_pdf_extraction -> false
metadata_json.source_provenance_boundary -> evidence_ledger_entry_metadata_from_retrieval_run_candidate_chunk
metadata_json.persistence_boundary -> retrieval_run_linked_evidence_ledger_no_llm_no_embeddings
metadata_json.chunk_id_matches_source_id -> true
metadata_json.document_id_matches_upload -> true
metadata_json.retrieval_run_id_matches -> true
ledger_retrieval_run_id_matches -> true
ledger_source_id_matches_chunk_id -> true
listed_metadata_parser -> pdf-pymupdf
listed_retrieval_run_id_matches -> true
stored_entry_count -> 1
all_required_markers_passed -> true
```

## Allowed Claim

NoiseProof has local Docker runtime evidence that uploaded digital PDF bytes can flow through upload chunk persistence, document retrieval-run persistence, retrieval-run-linked Evidence Ledger persistence, and filtered Evidence Ledger listing while preserving PDF parser/source provenance in `evidence_ledger_entries.metadata_json`.

## Boundary / Non-claims

This is local runtime evidence only.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not robust PDF extraction.

This is digital PDF text only.

OCR, table extraction, and layout fidelity are not claimed.

This is not raw file storage.

This is not full parsed text persistence.

This adds no embeddings.

This adds no semantic retrieval quality evidence.

This is not Noise Gate behavior.

This is not report generation.

This is not LLM judgment.

This is not production readiness.
