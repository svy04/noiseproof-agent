# Uploaded PDF No-text Failure Candidate Runtime Smoke

Status: local runtime smoke evidence.

Phase marker: uploaded PDF no-text failure candidate runtime smoke v0.

This smoke records local Docker PostgreSQL plus live FastAPI HTTP evidence that uploaded PDFs with no embedded digital text preserve the `pdf_no_extractable_text` failure candidate through explicit upload-to-chunks metadata handoff.

## Environment

```text
Docker version 29.4.3, build 055a478
Docker Compose version v5.1.3
API image -> sha256:1f4d797db60cdca60436b0da3b3fc53dd0a5be0983348b10042ebb0997dcb8a0
API started -> 2026-06-05T12:26:40.269145364Z
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
```

The PDF was generated as a valid one-page blank PDF with no embedded text blocks and uploaded as multipart `application/pdf`.

## Observed

```text
GET /health -> 200
health_status -> ok
POST /documents/upload-chunks -> 201
parser -> pdf-pymupdf
document_id -> 36f515de-30aa-4ffc-ba02-a2e16d563d1e
document_status -> chunk_handoff_no_chunks
chunk_count -> 0
chunks_length -> 0
failure_case_candidate.failure_type -> pdf_no_extractable_text
failure_case_candidate.root_cause -> The PDF may be scanned, image-only, encrypted, or otherwise lacking embedded digital text.
page_text_char_counts -> [0]
empty_page_count -> 1
extracted_page_count -> 0
robust_pdf_extraction -> false
raw_file_storage -> false
parsed_text_storage -> false
no_digital_text_warning -> true
no_chunks_warning -> true
```

## Allowed Claim

NoiseProof has local runtime evidence that uploaded PDFs with no embedded digital text do not silently look like successful chunk handoffs. The running API preserves `pdf_no_extractable_text`, `chunk_handoff_no_chunks`, zero chunk count, page diagnostics, and the `robust_pdf_extraction=false` boundary in document metadata.

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
