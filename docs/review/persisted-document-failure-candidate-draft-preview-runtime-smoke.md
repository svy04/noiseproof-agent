# Persisted Document Failure Candidate Draft Preview Runtime Smoke

Status: local Docker/FastAPI runtime evidence.

Phase marker: persisted document failure candidate draft preview runtime smoke v0.

## Purpose

This smoke verifies that a persisted document row with `profile_json.failure_case_candidate` can be read back through live FastAPI HTTP and converted into a preview-only failure-case draft without creating a `failure_cases` row.

It specifically exercises the handoff from `POST /documents/upload-chunks` to `POST /documents/{document_id}/failure-case-draft-preview` against the local Docker PostgreSQL database.

## Environment

```text
Docker version 29.4.3, build 56be731
Docker Compose version v5.1.3
API image -> sha256:c611784879df1a897e7ee41716b6aa1ef5efff6a425b6248dbbd03bf226e6162
API image created -> 2026-06-05T13:25:18.530203767Z
Applied migrations: 23
Pending migrations: 0
```

## Commands

```text
docker compose --profile api config
docker compose --profile api up -d --build api
docker compose --profile api ps
DATABASE_URL=postgresql://noiseproof:noiseproof@localhost:55432/noiseproof uv run --project apps/api python -m app.migration_runner --status
```

HTTP smoke:

```text
GET /health -> 200
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/failure-case-draft-preview -> 200
GET /failure-cases -> 200
```

## Observed Markers

```text
health_status -> ok
document_id -> cfafd615-3700-428b-be28-d1d4abb91a84
document_status -> chunk_handoff_no_chunks
source_type -> pdf
parser -> pdf-pymupdf
chunk_count -> 0
page_text_char_counts -> 0
failure_case_candidate.failure_type -> pdf_no_extractable_text
draft.failure_type -> pdf_no_extractable_text
draft.fix_status -> draft
draft.agent_run_id -> null
draft.workflow_run_id -> null
persistence_boundary -> preview_only_not_persisted
human_confirmation_required -> true
source_summary.stage -> persisted_document_failure_case_candidate
source_summary.document_status -> chunk_handoff_no_chunks
warnings -> metadata-derived from document profile_json
pre_failure_case_count -> 4
post_failure_case_count -> 4
failure_case_count_delta -> 0
```

## Allowed Claim

In the local Docker/FastAPI runtime, a valid blank uploaded PDF can create a persisted document metadata row with a no-text failure candidate, and `POST /documents/{document_id}/failure-case-draft-preview` can turn that persisted candidate into a preview-only manual failure-case draft without creating `failure_cases`.

## Boundary

This is local runtime evidence only.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not customer validation.

This is not Braincrew acceptance.

This is not automatic failure-case creation.

This is not automatic root-cause analysis.

This is not robust PDF extraction.

This is not OCR.

This is not table extraction.

This is not layout fidelity evidence.

This is not raw file storage.

This is not parsed text persistence.

This is not full parsed text persistence.

This is not Evidence Ledger generation.

This is not Noise Gate behavior.

This is not report generation.

This is not product-complete.

## Next Gate

External reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, or another source-first product gate selected from `docs/GOAL.md`.
