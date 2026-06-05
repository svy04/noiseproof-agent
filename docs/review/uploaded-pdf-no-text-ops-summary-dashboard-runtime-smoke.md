# Uploaded PDF No-text Ops Summary Dashboard Runtime Smoke

Status: local Docker/FastAPI runtime evidence.

Phase marker: uploaded PDF no-text ops summary dashboard runtime smoke v0.

## Purpose

This smoke verifies that the no-text PDF metadata counts added to `/ops/summary` and `/ops/dashboard` work through a live local FastAPI container backed by Docker PostgreSQL.

It uses count deltas because the local database already contained prior no-text PDF smoke rows.

## Environment

```text
Docker version 29.4.3, build 055a478
Docker Compose version v5.1.3
API image -> sha256:eb1b11b065f3e02734b75cda9c79ab510ecd5df59f8e8234714dad7acf5d2799
API image created -> 2026-06-05T13:05:02.718722648Z
Applied migrations: 23
Pending migrations: 0
```

## Commands

```text
docker compose config
docker compose --profile api up -d --build api
docker compose --profile api ps
DATABASE_URL=postgresql://noiseproof:noiseproof@localhost:55432/noiseproof uv run --project apps/api python -m app.migration_runner --status
```

HTTP smoke:

```text
GET /health -> 200
GET /ops/summary -> 200
POST /documents/upload-chunks -> 201
GET /ops/summary -> 200
GET /ops/dashboard -> 200
```

## Observed Markers

```text
health_status -> ok
parser -> pdf-pymupdf
document_status -> chunk_handoff_no_chunks
failure_case_candidate.failure_type -> pdf_no_extractable_text
raw_file_storage -> false
parsed_text_storage -> false
```

Summary counts:

```text
pre_chunk_handoff_no_chunks_count -> 2
post_chunk_handoff_no_chunks_count -> 3
chunk_handoff_no_chunks_count -> 3
summary_count_delta -> 1
pre_pdf_no_text_failure_candidate_count -> 2
post_pdf_no_text_failure_candidate_count -> 3
pdf_no_text_failure_candidate_count -> 3
pdf_no_text_failure_candidate_delta -> 1
summary_note_has_no_text -> true
```

Dashboard markers:

```text
dashboard_contains_no_text_pdf_handoffs -> true
dashboard_contains_pdf_no_text_failure_candidates -> true
dashboard_contains_metadata_boundary -> true
No-text PDF Handoffs
PDF No-text Failure Candidates
metadata-derived from document profile_json
```

## Allowed Claim

In the local Docker/FastAPI runtime, uploading a valid blank PDF with no embedded digital text increments the no-text PDF ops summary counts by one and makes the count visible in the plain operations dashboard.

## Boundary

This is local runtime evidence only.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not customer validation.

This is not Braincrew acceptance.

This is not robust PDF extraction.

This is not OCR.

This is not table extraction.

This is not layout fidelity evidence.

This is not raw file storage.

This is not parsed text persistence.

This is not full parsed text persistence.

This is not automatic failure-case creation.

This is not Evidence Ledger generation.

This is not Noise Gate behavior.

This is not report generation.

This is not product-complete.

## Next Gate

External reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, or another source-first product gate selected from `docs/GOAL.md`.
