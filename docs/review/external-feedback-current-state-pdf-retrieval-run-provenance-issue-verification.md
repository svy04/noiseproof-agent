# External Feedback Current-state PDF Retrieval-run Provenance Issue Verification

Status: live external review issue current-state screen only.

Phase marker: external feedback current-state PDF retrieval-run provenance issue verification v0.

## Purpose

This gate verifies the current public issue #1 state after the owner-authored PDF retrieval-run provenance issue-body refresh.

It checks whether the issue body still exposes the uploaded PDF retrieval-run provenance runtime proof and whether any public comment currently qualifies as external reviewer feedback v0.

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
  "updatedAt": "2026-06-04T06:48:07Z",
  "state": "OPEN",
  "starts_with_request": true,
  "first_codepoint": 35,
  "has_pdf_retrieval_run_provenance_runtime_proof": true,
  "has_pdf_retrieval_run_provenance_runtime_link": true,
  "has_pdf_retrieval_run_provenance_request_refresh": true,
  "has_candidate_parsers_marker": true,
  "has_source_provenance_boundary_marker": true,
  "has_external_feedback_boundary": true,
  "comment_count": 1,
  "screened_comment_count": 1,
  "candidate_count": 0,
  "draft_count": 0
}
```

Text markers:

```text
updatedAt: 2026-06-04T06:48:07Z
starts_with_request: true
first_codepoint: 35
has_pdf_retrieval_run_provenance_runtime_proof: true
has_pdf_retrieval_run_provenance_runtime_link: true
has_pdf_retrieval_run_provenance_request_refresh: true
has_candidate_parsers_marker: true
has_source_provenance_boundary_marker: true
has_external_feedback_boundary: true
comment_count: 1
screened_comment_count: 1
candidate_count: 0
draft_count: 0
does_not_close_gate: true
```

## Linked Proof Still Visible

Uploaded PDF retrieval-run provenance runtime proof:

```text
docs/review/uploaded-pdf-retrieval-run-provenance-runtime-smoke.md
```

External reviewer PDF retrieval-run provenance request refresh:

```text
docs/review/external-reviewer-pdf-retrieval-run-provenance-request-refresh.md
```

The issue body currently includes:

```text
candidate_parsers -> pdf-pymupdf
source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only
```

## Comment Screen

The JSON payload was written as UTF-8 without BOM, then the existing local screeners were run against that payload:

```text
python -m packages.review.external_feedback_cli --input <issue.json> --repository-owner svy04
python -m packages.review.external_feedback_acceptance_cli --input <screen.json>
```

The first attempt wrote the screen JSON with PowerShell `Tee-Object`, which produced a UTF-16 file that the acceptance CLI could not decode. The successful command wrote the screen JSON with `System.Text.UTF8Encoding($false)`. This was a shell encoding issue, not product-code behavior.

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

This is not Evidence Ledger generation.

This is not Noise Gate behavior.

This is not report generation.

This is not customer validation, Braincrew acceptance, production readiness, embedding generation, semantic retrieval quality evidence, LLM output, automatic failure-case creation, or product-complete.

## Next Gate

```text
external reviewer feedback v0
```
