# External Review Issue Body Persisted Document Failure Candidate Manual Handoff Runtime Refresh

Status: owner-authored issue body edit.

Phase marker: external reviewer persisted document failure candidate manual handoff runtime issue-body refresh v0.

Issue:

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

This document records that the live public external review issue body now routes reviewers to the persisted document failure candidate manual handoff runtime proof.

## Live Issue Verification

Observed after edit:

```text
updatedAt: 2026-06-05T14:15:36Z
comment_count: 1
starts_with_request: true
first_codepoint: 35
has_persisted_document_failure_candidate_manual_handoff_runtime_proof: true
has_persisted_document_failure_candidate_manual_handoff_request_refresh: true
has_persisted_document_failure_candidate_manual_handoff_issue_body_record: true
has_failure_case_count_delta_1: true
has_human_fix_status_boundary: true
has_confirm_endpoint_boundary: true
has_external_feedback_boundary: true
```

## Latest Proof Routed

persisted document failure candidate manual handoff runtime proof:

```text
docs/review/persisted-document-failure-candidate-manual-handoff-runtime-smoke.md
docs/review/external-reviewer-persisted-document-failure-candidate-manual-handoff-runtime-request-refresh.md
docs/review/external-review-issue-body-persisted-document-failure-candidate-manual-handoff-runtime-refresh.md
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/failure-case-draft-preview -> 200
POST /failure-cases -> 201
GET /failure-cases -> 200
preview_only_not_persisted
human_confirmation_required -> true
human changes draft.fix_status from draft to open
pdf_no_extractable_text
chunk_handoff_no_chunks
failure_case_count_delta -> 1
```

## What Changed

Issue #1 now puts the persisted document failure candidate manual handoff runtime proof in the `Latest Proof To Inspect` section.

The issue also links this record:

```text
docs/review/external-review-issue-body-persisted-document-failure-candidate-manual-handoff-runtime-refresh.md
```

The previous persisted document failure candidate draft preview runtime routing remains below it as a previous issue-body routing proof.

## Boundary

This is an owner-authored issue body edit.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not customer validation.

This is not Braincrew acceptance.

This is not automatic failure-case creation.

This is not a confirm endpoint.

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

Next recommended gate: external feedback current-state persisted document failure candidate manual handoff runtime issue verification v0, to screen issue #1 after this owner-authored routing edit and keep external reviewer feedback pending unless a qualifying outside comment exists.
