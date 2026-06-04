# External Feedback Current-state PDF Retrieval-run-linked Evidence Ledger Provenance Issue Verification

Status: live external review issue current-state screen only.

Phase marker: external feedback current-state PDF retrieval-run-linked Evidence Ledger provenance issue verification v0.

## Purpose

This gate verifies the current public issue #1 state after the owner-authored PDF retrieval-run-linked Evidence Ledger provenance issue-body refresh.

It checks whether the issue body still exposes the uploaded PDF retrieval-run-linked Evidence Ledger provenance runtime proof and whether any public comment currently qualifies as external reviewer feedback v0.

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
  "updatedAt": "2026-06-04T07:43:00Z",
  "state": "OPEN",
  "starts_with_request": true,
  "first_codepoint": 35,
  "has_pdf_retrieval_run_linked_evidence_ledger_runtime_proof": true,
  "has_pdf_retrieval_run_linked_evidence_ledger_runtime_link": true,
  "has_pdf_retrieval_run_linked_evidence_ledger_request_refresh": true,
  "has_metadata_json_parser_marker": true,
  "has_source_provenance_boundary_marker": true,
  "has_ledger_retrieval_run_match_marker": true,
  "has_external_feedback_boundary": true,
  "comment_count": 1,
  "screened_comment_count": 1,
  "candidate_count": 0,
  "draft_count": 0
}
```

Text markers:

```text
updatedAt: 2026-06-04T07:43:00Z
starts_with_request: true
first_codepoint: 35
has_pdf_retrieval_run_linked_evidence_ledger_runtime_proof: true
has_pdf_retrieval_run_linked_evidence_ledger_runtime_link: true
has_pdf_retrieval_run_linked_evidence_ledger_request_refresh: true
has_metadata_json_parser_marker: true
has_source_provenance_boundary_marker: true
has_ledger_retrieval_run_match_marker: true
has_external_feedback_boundary: true
comment_count: 1
screened_comment_count: 1
candidate_count: 0
draft_count: 0
does_not_close_gate: true
```

## Linked Proof Still Visible

Uploaded PDF retrieval-run-linked Evidence Ledger provenance runtime proof:

```text
docs/review/uploaded-pdf-retrieval-run-linked-evidence-ledger-provenance-runtime-smoke.md
```

External reviewer PDF retrieval-run-linked Evidence Ledger provenance request refresh:

```text
docs/review/external-reviewer-pdf-retrieval-run-linked-evidence-ledger-provenance-request-refresh.md
```

The issue body currently includes:

```text
metadata_json.parser -> pdf-pymupdf
metadata_json.source_provenance_boundary -> evidence_ledger_entry_metadata_from_retrieval_run_candidate_chunk
ledger_retrieval_run_id_matches -> true
```

## Comment Screen

The live issue JSON was written to a UTF-8 no-BOM temporary file, then the existing local screeners were run against that payload:

```text
uv run --project apps/api python -m packages.review.external_feedback_cli --input <issue.json> --repository-owner svy04
uv run --project apps/api python -m packages.review.external_feedback_acceptance_cli --input <screen.json>
```

Screening result:

```json
{
  "status": "pending",
  "candidate_count": 0,
  "next_gate": "external reviewer feedback v0",
  "does_not_close_gate": true,
  "warnings": [],
  "screened_comments": [
    {
      "author_login": "svy04",
      "classification": "non_qualifying",
      "reasons": [
        "self_authored_comment"
      ]
    }
  ]
}
```

Acceptance draft result:

```json
{
  "status": "pending",
  "draft_count": 0,
  "next_gate": "external reviewer feedback v0",
  "does_not_close_gate": true,
  "warnings": [
    "No candidate comments were available for acceptance drafting."
  ],
  "drafts": []
}
```

Screening text markers:

```text
self_authored_comment
non_qualifying
candidate_count: 0
draft_count: 0
```

This preserves the external reviewer feedback v0 gate as pending.

## Boundary

This is a live issue screen after an owner-authored issue body edit.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not robust PDF extraction.

This is not OCR.

This is not table extraction.

This is not layout fidelity evidence.

This is not raw file storage.

This is not full parsed text persistence.

This is not Noise Gate behavior.

This is not report generation.

This is not customer validation, Braincrew acceptance, production readiness, embedding generation, semantic retrieval quality evidence, LLM output, automatic failure-case creation, or product-complete.

## Next Gate

```text
external reviewer feedback v0 remains pending, or select the next source-first product gate
```
