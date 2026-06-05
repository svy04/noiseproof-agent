# Persisted Document Failure Candidate Draft Preview

Status: implemented.

Phase marker: persisted document failure candidate draft preview v0.

## Purpose

This gate lets an operator preview a manual failure-case draft from an already persisted document failure candidate.

Before this gate, uploaded-file failure-case draft preview existed for multipart upload flows, but a persisted no-text PDF document required manually inspecting `profile_json` and then hand-writing a draft.

This endpoint does not persist a failure case.

## Endpoint

```text
POST /documents/{document_id}/failure-case-draft-preview
```

Input:

```text
document_id
```

Output shape:

```text
draft
source_summary
persistence_boundary -> preview_only_not_persisted
human_confirmation_required -> true
warnings
```

The preview is metadata-derived from document profile_json:

```text
document.status -> chunk_handoff_no_chunks
document.source_type -> pdf
document.profile_json.failure_case_candidate.failure_type -> pdf_no_extractable_text
source_summary.stage -> persisted_document_failure_case_candidate
```

## Test Evidence

Route test:

```text
apps/api/tests/test_routes.py::test_persisted_no_text_pdf_document_failure_case_draft_preview_without_persistence
```

The test verifies:

```text
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/failure-case-draft-preview -> 200
persistence_boundary -> preview_only_not_persisted
human_confirmation_required -> true
draft.failure_type -> pdf_no_extractable_text
draft.fix_status -> draft
source_summary.document_status -> chunk_handoff_no_chunks
source_summary.stage -> persisted_document_failure_case_candidate
failure_cases -> []
```

## Allowed Claim

An operator can now turn a persisted document-level failure candidate into a preview-only failure-case draft without re-uploading the file and without automatically creating a `failure_cases` row.

## Boundary

This is preview-only.

This does not create failure_cases.

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

This is not Evidence Ledger generation.

This is not Noise Gate behavior.

This is not report generation.

This is not product-complete.

## Next Gate

Local Docker/FastAPI runtime smoke for persisted document failure candidate draft preview if runtime evidence is needed, external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, or another source-first product gate selected from `docs/GOAL.md`.
