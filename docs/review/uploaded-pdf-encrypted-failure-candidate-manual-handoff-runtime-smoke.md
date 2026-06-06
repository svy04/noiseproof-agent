# Uploaded PDF Encrypted Failure Candidate Manual Handoff Runtime Smoke

Status: verified.

Phase marker: uploaded PDF encrypted failure candidate manual handoff runtime smoke v0.

## Purpose

Verify that a password-protected uploaded PDF failure candidate can move from persisted document metadata into a preview-only failure-case draft, and then into a persisted failure case only after human confirmation.

This closes the handoff after the encrypted PDF operations counter: the system should not only count the password-required PDF, but also preserve enough failure metadata for an operator to create a reviewable failure case.

## Environment

```text
FastAPI URL: http://127.0.0.1:8001
health_status=ok
local Docker PostgreSQL: running
runtime file: runtime-encrypted-manual-handoff-phase681.pdf
pdf_bytes=1495
```

The smoke generated a temporary password-protected PDF with PyMuPDF and deleted it after the run.

## Runtime Flow

```text
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/failure-case-draft-preview -> 200
POST /failure-cases -> 201
GET /failure-cases -> 200
```

## Observed Markers

```text
runtime-encrypted-manual-handoff-phase681.pdf
pre_failure_case_count -> 10
document_id -> 5689ba72-1e99-4dfb-b461-38b49bfd9c20
document_status -> chunk_handoff_no_chunks
upload_failure_type -> pdf_encrypted_requires_password
upload_encrypted -> True
upload_password_required -> True
upload_extraction_scope -> encrypted_pdf_password_required
upload_chunk_count -> 0
draft_failure_type -> pdf_encrypted_requires_password
draft_fix_status -> draft
draft_persistence_boundary -> preview_only_not_persisted
human_confirmation_required -> True
draft_source_stage -> persisted_document_failure_case_candidate
draft_next_action_contains_authorized_password -> True
draft_next_action_contains_approved_decryption -> True
mid_failure_case_count -> 10
draft_failure_case_count_delta -> 0
persisted_failure_case_id -> 2ace560d-86bc-4394-bf98-a4dedfb5db82
persisted_failure_type -> pdf_encrypted_requires_password
persisted_fix_status -> open
persisted_next_action_contains_authorized_password -> True
persisted_next_action_contains_approved_decryption -> True
post_failure_case_count -> 11
failure_case_count_delta -> 1
temp_pdf_removed -> True
```

## Interpretation

The draft-preview route preserved the encrypted PDF failure type and password/decryption next action without creating a failure case.

Only the explicit human-confirmed `POST /failure-cases` call persisted a failure case.

## Boundary

This is local Docker PostgreSQL plus live FastAPI runtime evidence only.

It is not automatic failure-case creation, not hosted deployment evidence, not external reviewer feedback, not customer validation, not Braincrew acceptance, not robust PDF extraction, not OCR, not table extraction, not layout fidelity, not decryption, not password bypass, not downstream retrieval evidence, and not product-complete.

## Verification Commands

```text
uv run --project apps/api pytest apps/api/tests/test_routes.py::test_persisted_encrypted_pdf_failure_candidate_draft_preserves_password_next_action -q
uv run --project apps/api pytest apps/api/tests/test_docs.py::test_uploaded_pdf_encrypted_failure_candidate_manual_handoff_runtime_smoke_is_recorded -q
```

## Next Gate

Remote verification for this runtime-smoke proof after push, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, or another source-first product gate selected from the current repository state.
