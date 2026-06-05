# External Feedback Current-state PDF Table-candidate Downstream Runtime Issue Verification

Status: live external review issue current-state screen only.

Phase marker: external feedback current-state PDF table-candidate downstream runtime issue verification v0.

## Purpose

This gate verifies the current public issue #1 state after the owner-authored PDF table-candidate downstream runtime issue-body refresh.

It checks whether the issue body still exposes the uploaded PDF table-candidate downstream runtime proof links and whether any public comment currently qualifies as external reviewer feedback v0.

It does not judge PDF parsing quality.

It does not accept feedback.

It does not close external reviewer feedback v0.

## Live Issue

```text
https://github.com/svy04/noiseproof-agent/issues/1
```

Observed current state:

```json
{
  "updatedAt": "2026-06-05T20:48:53Z",
  "has_pdf_table_candidate_downstream_runtime_proof": true,
  "has_pdf_table_candidate_downstream_remote_verification": true,
  "has_pdf_table_candidate_downstream_request_refresh": true,
  "has_pdf_table_candidate_downstream_issue_body_record": true,
  "has_retrieval_candidate_table_count": true,
  "starts_with_request": true,
  "first_codepoint": 35,
  "body_length": 7534,
  "comment_count": 1,
  "screened_comment_count": 1,
  "owner_comment_count": 1,
  "candidate_count": 0,
  "draft_count": 0,
  "classification": "non_qualifying",
  "reason": "self_authored_comment",
  "status": "pending"
}
```

Text markers:

```text
updatedAt: 2026-06-05T20:48:53Z
has_pdf_table_candidate_downstream_runtime_proof: true
has_pdf_table_candidate_downstream_remote_verification: true
has_pdf_table_candidate_downstream_request_refresh: true
has_pdf_table_candidate_downstream_issue_body_record: true
has_retrieval_candidate_table_count: true
starts_with_request: true
first_codepoint: 35
body_length: 7534
comment_count: 1
screened_comment_count: 1
owner_comment_count: 1
candidate_count: 0
draft_count: 0
classification: non_qualifying
reason: self_authored_comment
status: pending
does_not_close_gate: true
```

## Linked Proof Still Visible

Uploaded PDF table-candidate downstream runtime proof:

```text
docs/review/uploaded-pdf-table-candidate-downstream-provenance-runtime-smoke.md
```

Uploaded PDF table-candidate downstream remote verification:

```text
docs/review/uploaded-pdf-table-candidate-downstream-provenance-remote-verification.md
```

External reviewer request refresh:

```text
docs/review/external-reviewer-pdf-table-candidate-downstream-runtime-request-refresh.md
```

External review issue-body refresh record:

```text
docs/review/external-review-issue-body-pdf-table-candidate-downstream-runtime-refresh.md
```

The issue body currently includes:

```text
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/retrieval-runs -> 201
GET /retrieval-runs -> 200
document_profile_table_candidate_count -> 1
chunk_metadata_table_candidate_count -> 1
retrieval_metadata_table_candidate_count -> 1
retrieval_candidate_table_candidate_count -> 1
source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only
```

## Comment Screen

The only current issue comment is owner-authored by `svy04`.

Screening result:

```text
self_authored_comment
classification: non_qualifying
candidate_count: 0
draft_count: 0
status: pending
```

This preserves the external reviewer feedback v0 gate as pending.

```text
external reviewer feedback v0 gate remains pending
```

## Boundary

This is a live issue screen after an owner-authored issue body edit.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not robust PDF extraction.

This is not OCR.

This is not table extraction.

This is not table-content extraction.

This is not layout fidelity evidence.

This is not raw file storage.

This is not full parsed text persistence.

This is not semantic retrieval quality evidence.

This is not Evidence Ledger generation.

This is not Critic / Noise Gate behavior.

This is not final report generation.

This is not customer validation, Braincrew acceptance, production readiness, embedding generation, LLM output, automatic failure-case creation, or product-complete.

This is not product-complete.

## Next Gate

Next recommended gate: external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when `OPENAI_API_KEY` is configured by the owner, or another source-first product gate selected from `docs/GOAL.md`.
