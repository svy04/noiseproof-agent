# External Review Issue Body Persisted Document Failure Candidate Draft Runtime Refresh

Status: owner-authored issue body edit.

Phase marker: external reviewer persisted document failure candidate draft runtime issue-body refresh v0.

Issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

This document records that the live public external review issue body now routes reviewers to the persisted document failure candidate draft preview runtime proof.

## Live Issue Verification

Observed after edit:

```text
updatedAt: 2026-06-05T13:42:17Z
comment_count: 1
starts_with_request: true
first_codepoint: 35
has_persisted_document_failure_candidate_draft_runtime_proof: true
has_persisted_document_failure_candidate_draft_request_refresh: true
has_persisted_document_failure_candidate_draft_issue_body_record: true
has_preview_only_not_persisted: true
has_failure_case_count_delta: true
has_external_feedback_boundary: true
```

## Latest Proof Routed

persisted document failure candidate draft preview runtime proof:

```text
docs/review/persisted-document-failure-candidate-draft-preview-runtime-smoke.md
docs/review/external-reviewer-persisted-document-failure-candidate-draft-runtime-request-refresh.md
docs/review/external-review-issue-body-persisted-document-failure-candidate-draft-runtime-refresh.md
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/failure-case-draft-preview -> 200
GET /failure-cases -> 200
preview_only_not_persisted
human_confirmation_required -> true
pdf_no_extractable_text
chunk_handoff_no_chunks
persisted_document_failure_case_candidate
metadata-derived from document profile_json
failure_case_count_delta -> 0
```

## What Changed

Issue #1 now puts the persisted document failure candidate draft preview runtime proof in the `Latest Proof To Inspect` section.

The issue also links this record:

```text
docs/review/external-review-issue-body-persisted-document-failure-candidate-draft-runtime-refresh.md
```

The previous uploaded PDF no-text failure candidate runtime routing remains below it as a previous issue-body routing proof.

## Boundary

This is an owner-authored issue body edit.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not customer validation.

This is not Braincrew acceptance.

This is not automatic failure-case creation.

This is not automatic root-cause analysis.

This is not robust PDF extraction.

This is not OCR.

This is not table extraction.

This is not layout fidelity.

This is not raw file storage.

This is not parsed text persistence.

This is not full parsed text persistence.

This is not semantic retrieval quality evidence.

This is not Evidence Ledger generation.

This is not Noise Gate behavior.

This is not report generation.

This is not product-complete.

Self-authored issue edits or comments do not close the external reviewer feedback v0 gate.

## Next Gate

Next recommended gate: external feedback current-state persisted document failure candidate draft runtime issue verification v0, to screen issue #1 after this owner-authored routing edit and keep external reviewer feedback pending unless a qualifying outside comment exists.
