# Uploaded PDF Page Diagnostics Downstream Provenance Runtime Smoke

Status: local runtime smoke evidence.

Phase marker: uploaded PDF page diagnostics downstream provenance runtime smoke v0.

This smoke records local Docker PostgreSQL plus live FastAPI HTTP evidence that uploaded PDF page diagnostics flow into explicit upload chunk persistence and persisted document retrieval-run candidate provenance.

## Environment

```text
Docker version 29.4.3, build 055a478
Docker Compose version v5.1.3
API image -> sha256:a69174a92e26a93cf40cee3c956912b65ed27fe2f19f3c6500d756d4339c49c0
API started -> 2026-06-05T11:31:39.668022223Z
Applied migrations: 23
Pending migrations: 0
```

## Commands

```powershell
docker compose config
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

The PDF was generated in memory with PyMuPDF and uploaded as multipart `application/pdf`.

## Observed

```text
GET /health -> 200
health_status -> ok
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/retrieval-runs -> 201
GET /retrieval-runs -> 200
parser -> pdf-pymupdf
document_id -> d95c8938-32eb-4e57-a49a-9dd20cc8f2f2
chunk_count -> 1
retrieval_id -> 486378b8-42d6-4950-9a0b-845d4683847a
retrieval_status -> completed
retrieval_result_count -> 1
document_profile_page_diagnostics_available -> true
document_profile_layout_block_diagnostics_available -> true
document_profile_extraction_scope -> digital_text_page_diagnostics
document_profile_page_text_char_counts -> [39]
document_profile_extracted_page_count -> 1
document_profile_empty_page_count -> 0
document_profile_text_block_count -> 1
document_profile_image_block_count -> 0
chunk_metadata_page_diagnostics_available -> true
chunk_metadata_layout_block_diagnostics_available -> true
chunk_metadata_extraction_scope -> digital_text_page_diagnostics
chunk_metadata_page_text_char_counts -> [39]
chunk_metadata_extracted_page_count -> 1
chunk_metadata_empty_page_count -> 0
chunk_metadata_text_block_count -> 1
chunk_metadata_image_block_count -> 0
retrieval_metadata_page_diagnostics_available -> true
retrieval_metadata_layout_block_diagnostics_available -> true
retrieval_metadata_extraction_scope -> digital_text_page_diagnostics
retrieval_metadata_page_text_char_counts -> [39]
retrieval_metadata_extracted_page_count -> 1
retrieval_metadata_empty_page_count -> 0
retrieval_metadata_text_block_count -> 1
retrieval_metadata_image_block_count -> 0
retrieval_candidate_page_diagnostics_available -> true
retrieval_candidate_layout_block_diagnostics_available -> true
retrieval_candidate_extraction_scope -> digital_text_page_diagnostics
retrieval_candidate_page_text_char_counts -> [39]
retrieval_candidate_extracted_page_count -> 1
retrieval_candidate_empty_page_count -> 0
retrieval_candidate_text_block_count -> 1
retrieval_candidate_image_block_count -> 0
source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only
candidate_source_types -> ['pdf']
candidate_parsers -> ['pdf-pymupdf']
digital_pdf_text_extraction -> true
robust_pdf_extraction -> false
latest_listed_id_matches -> true
raw_file_storage -> false
parsed_text_storage -> false
```

## Allowed Claim

NoiseProof has local runtime evidence that uploaded digital PDF page diagnostics can flow into explicit upload chunk metadata and persisted document retrieval-run candidate metadata through live FastAPI HTTP.

## Boundary

This is local runtime evidence only.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not robust PDF extraction.

This is not OCR.

This is not table extraction.

This is not layout fidelity.

This is not raw file storage.

This has no raw uploaded byte storage.

This is not full parsed text persistence.

This has no full parsed text persistence.

This adds no embeddings.

This adds no semantic retrieval quality evidence.

This is not Evidence Ledger generation.

This adds no Noise Gate behavior.

This adds no report generation.

This is not production readiness.

This is not product-complete.

## Next Gate

The next external evidence gate remains:

```text
external reviewer feedback v0
```
