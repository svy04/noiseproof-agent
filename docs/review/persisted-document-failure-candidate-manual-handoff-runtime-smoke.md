# Persisted Document Failure Candidate Manual Handoff Runtime Smoke

Status: local Docker/FastAPI runtime evidence.

Phase marker: persisted document failure candidate manual handoff runtime smoke v0.

## Purpose

This smoke verifies that the persisted document failure candidate manual handoff works through live FastAPI HTTP backed by Docker PostgreSQL.

It reuses the existing `POST /failure-cases` persistence endpoint. It does not add a confirm endpoint and does not make failure-case creation automatic.

## Environment

```text
Docker version 29.4.3, build 56be731
Docker Compose version v5.1.3
API image -> sha256:3a59622dbab86b5a16a98c68aab2afe9165c4555e7dfe375cd445d6a04f9fece
API image created -> 2026-06-05T13:58:36.534754872Z
Applied migrations: 23
Pending migrations: 0
```

## Commands

```text
docker compose --profile api up -d --build api
DATABASE_URL=postgresql://noiseproof:noiseproof@localhost:55432/noiseproof uv run --project apps/api python -m app.migration_runner --status
```

HTTP smoke:

```text
GET /health -> 200
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/failure-case-draft-preview -> 200
POST /failure-cases -> 201
GET /failure-cases -> 200
```

## Observed Markers

```text
document_id -> 1d6ce0fd-c685-481e-8608-1c573a3a8f32
document_status -> chunk_handoff_no_chunks
parser -> pdf-pymupdf
chunk_count -> 0
failure_case_candidate.failure_type -> pdf_no_extractable_text
persistence_boundary -> preview_only_not_persisted
human_confirmation_required -> true
draft.initial_fix_status -> draft
human changes draft.fix_status from draft to open
persisted_failure_case_id -> 646fe4ff-078c-4e96-be0c-1de6f41ec4ae
persisted_failure_type -> pdf_no_extractable_text
persisted_fix_status -> open
persisted_agent_run_id -> null
persisted_workflow_run_id -> null
source_summary.stage -> persisted_document_failure_case_candidate
source_summary.document_status -> chunk_handoff_no_chunks
pre_failure_case_count -> 4
post_failure_case_count -> 5
failure_case_count_delta -> 1
```

## Allowed Claim

In the local Docker/FastAPI runtime, a persisted document failure candidate can be previewed, manually confirmed by changing `draft.fix_status` from `draft` to `open`, and submitted through the existing `POST /failure-cases` endpoint.

## Boundary

This is local runtime evidence only.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not automatic failure-case creation.

This is not automatic root-cause analysis.

This is not a confirm endpoint.

This is not robust PDF extraction.

This is not OCR.

This is not table extraction.

This is not layout fidelity evidence.

This is not Evidence Ledger generation.

This is not Noise Gate behavior.

This is not report generation.

This is not product-complete.

## Next Gate

External reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, or another source-first product gate selected from `docs/GOAL.md`.
