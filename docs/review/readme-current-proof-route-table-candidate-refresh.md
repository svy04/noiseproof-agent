# README Current Proof Route Table-candidate Refresh

Status: implemented.

Phase marker: readme current proof route table-candidate refresh v0.

## Purpose

Keep the first-screen README proof route aligned with the current public issue body and the latest table-candidate downstream reviewer path.

The README top fast path previously still named the workflow failure auto-created dashboard runtime proof as the latest route, while issue #1 and the newer reviewer-facing markers point reviewers to the uploaded PDF table-candidate downstream runtime proof.

## Current Route

The top README fast path now points to:

```text
uploaded PDF table-candidate downstream runtime proof
docs/review/uploaded-pdf-table-candidate-downstream-provenance-runtime-smoke.md
docs/review/uploaded-pdf-table-candidate-downstream-provenance-remote-verification.md
docs/review/external-reviewer-pdf-table-candidate-downstream-runtime-request-refresh.md
docs/review/external-review-issue-body-pdf-table-candidate-downstream-runtime-refresh.md
docs/review/external-feedback-current-state-pdf-table-candidate-downstream-runtime-issue-verification.md
docs/review/external-feedback-current-state-pdf-table-candidate-downstream-runtime-issue-verification-remote-verification.md
retrieval_candidate_table_candidate_count -> 1
```

## Preserved State

The external feedback state remains pending:

```text
candidate_count=0
draft_count=0
self_authored_comment
external reviewer feedback remains pending
```

## Boundary

This is README route clarity only.

It is not a new runtime smoke.

It is not external reviewer feedback.

It is not hosted deployment evidence.

It is not customer validation.

It is not Braincrew acceptance.

It is not robust PDF extraction.

It is not OCR.

It is not table extraction.

It does not extract table contents.

It is not layout fidelity evidence.

It is not Evidence Ledger generation.

It is not Critic / Noise Gate behavior.

It is not final report generation.

It is not product-complete.

## Next Gate

```text
external reviewer feedback v0 if qualifying outside feedback exists, owner-runtime manual live embedding smoke v0 only when OPENAI_API_KEY is configured by the owner, or another source-first product gate selected from docs/GOAL.md
```
