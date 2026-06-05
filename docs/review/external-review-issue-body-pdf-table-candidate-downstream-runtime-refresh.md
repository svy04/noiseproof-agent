# External Review Issue Body PDF Table-candidate Downstream Runtime Refresh

Status: owner-authored issue body edit.

Phase marker: external review issue body PDF table-candidate downstream runtime refresh v0.

This records the owner-authored issue #1 body refresh that routes external reviewers to the uploaded PDF table-candidate downstream runtime proof.

Live issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

## Live Issue Verification

Observed after edit:

```text
updatedAt: 2026-06-05T20:48:53Z
url: https://github.com/svy04/noiseproof-agent/issues/1
starts_with_request: true
first_codepoint: 35
body_length: 7534
comment_count: 1
has_pdf_table_candidate_downstream_runtime_proof: true
has_pdf_table_candidate_downstream_remote_verification: true
has_pdf_table_candidate_downstream_request_refresh: true
has_pdf_table_candidate_downstream_issue_body_record: true
has_retrieval_candidate_table_count: true
has_external_feedback_boundary: true
```

## Latest Proof Routed

uploaded PDF table-candidate downstream runtime proof:

```text
docs/review/uploaded-pdf-table-candidate-downstream-provenance-runtime-smoke.md
docs/review/uploaded-pdf-table-candidate-downstream-provenance-remote-verification.md
docs/review/external-reviewer-pdf-table-candidate-downstream-runtime-request-refresh.md
docs/review/external-review-issue-body-pdf-table-candidate-downstream-runtime-refresh.md
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/retrieval-runs -> 201
GET /retrieval-runs -> 200
document_profile_table_candidate_count -> 1
chunk_metadata_table_candidate_count -> 1
retrieval_metadata_table_candidate_count -> 1
retrieval_candidate_table_candidate_count -> 1
table_extraction_performed -> false
source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only
raw_file_storage -> false
parsed_text_storage -> false
```

## What Changed

Issue #1 now puts the uploaded PDF table-candidate downstream runtime proof in the `Latest Proof To Inspect` section.

The issue also links this record:

```text
docs/review/external-review-issue-body-pdf-table-candidate-downstream-runtime-refresh.md
```

## Boundary

This is owner-authored issue body routing only.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not customer validation.

This is not Braincrew acceptance.

This is not robust PDF extraction.

This is not OCR.

This is not table extraction.

This does not extract table contents.

This is not layout fidelity.

This is not raw file storage.

This is not full parsed text persistence.

This is not semantic retrieval quality evidence.

This is not Evidence Ledger generation.

This is not Noise Gate behavior.

This is not report generation.

This is not product-complete.

Self-authored issue edits or comments do not close the external reviewer feedback v0 gate.

## Next Gate

Next recommended gate: external feedback current-state PDF table-candidate downstream runtime issue verification v0, to screen issue #1 after this owner-authored routing edit and keep external reviewer feedback pending unless a qualifying outside comment exists.
