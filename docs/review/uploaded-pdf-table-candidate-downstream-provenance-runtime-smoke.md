# Uploaded PDF Table-candidate Downstream Provenance Runtime Smoke

Status: local runtime smoke evidence.

Phase marker: uploaded PDF table-candidate downstream provenance runtime smoke v0.

This smoke records local Docker PostgreSQL plus live FastAPI HTTP evidence that uploaded PDF table-candidate diagnostics flow into explicit upload chunk persistence and persisted document retrieval-run candidate provenance.

It is a runtime smoke record for one small fixture, not a broad PDF parsing, table extraction, or retrieval quality claim.

## Environment

```text
Docker version 29.4.3, build 055a478
Docker Compose version v5.1.3
API image -> noiseproof-agent-api@sha256:db20c10218c68e19e1f7c5be54d47d525b672426a1e0e7e1623abbb763af63c3
API started -> 2026-06-05T20:25:11.839214186Z
noiseproof-agent-db -> healthy
noiseproof-agent-api -> Up, 0.0.0.0:8000->8000/tcp
Applied migrations: 23
Pending migrations: 0
```

## Commands

```powershell
docker compose --profile api up -d --build api
docker compose --profile api ps
$env:DATABASE_URL = "postgresql://noiseproof:noiseproof@localhost:55432/noiseproof"
uv run --project apps/api python -m app.migration_runner --status
```

HTTP smoke:

```text
GET /health
POST /documents/upload-chunks
POST /documents/{document_id}/retrieval-runs
GET /retrieval-runs
```

The PDF was generated in memory with PyMuPDF, using drawn grid lines and text labels to create one simple table-shaped candidate.

## Observed

```text
GET /health -> 200
health_status -> ok
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/retrieval-runs -> 201
GET /retrieval-runs -> 200
parser -> pdf-pymupdf
document_id -> 0052ef6d-7d84-4b3d-9ba8-dbb924f39415
chunk_count -> 1
retrieval_id -> c8e12cdb-f7f6-445f-967d-fc5eee916b75
retrieval_status -> completed
retrieval_result_count -> 1
document_profile_table_candidate_diagnostics_available -> true
document_profile_table_candidate_count -> 1
document_profile_table_candidate_page_counts -> [1]
document_profile_table_candidate_shapes -> page_index=0,row_count=2,col_count=2,cell_count=4
document_profile_table_extraction_performed -> false
chunk_metadata_table_candidate_diagnostics_available -> true
chunk_metadata_table_candidate_count -> 1
chunk_metadata_table_candidate_page_counts -> [1]
chunk_metadata_table_candidate_shapes -> page_index=0,row_count=2,col_count=2,cell_count=4
chunk_metadata_table_extraction_performed -> false
retrieval_metadata_table_candidate_diagnostics_available -> true
retrieval_metadata_table_candidate_count -> 1
retrieval_metadata_table_candidate_page_counts -> [1]
retrieval_metadata_table_candidate_shapes -> page_index=0,row_count=2,col_count=2,cell_count=4
retrieval_metadata_table_extraction_performed -> false
retrieval_candidate_table_candidate_diagnostics_available -> true
retrieval_candidate_table_candidate_count -> 1
retrieval_candidate_table_candidate_page_counts -> [1]
retrieval_candidate_table_candidate_shapes -> page_index=0,row_count=2,col_count=2,cell_count=4
retrieval_candidate_table_extraction_performed -> false
source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only
candidate_source_types -> [pdf]
candidate_parsers -> [pdf-pymupdf]
digital_pdf_text_extraction -> true
robust_pdf_extraction -> false
raw_file_storage -> false
parsed_text_storage -> false
```

## Allowed Claim

NoiseProof has local runtime evidence that uploaded PDF table-candidate diagnostics can flow into explicit upload chunk metadata and persisted document retrieval-run candidate metadata through live FastAPI HTTP.

## Boundary

This is local runtime evidence only.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not robust PDF extraction.

This is not OCR.

This is not table extraction.

This does not extract table contents.

This is not layout fidelity.

This is not raw file storage.

This is not full parsed text persistence.

This adds no embeddings.

This adds no semantic retrieval quality evidence.

This is not Evidence Ledger generation.

This adds no Noise Gate behavior.

This adds no report generation.

This is not production readiness.

This is not product-complete.

## Next Gate

Next recommended gate: external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, or another source-first product gate selected from `docs/GOAL.md`.
