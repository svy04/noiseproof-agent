# External Reviewer Persisted Document Failure Candidate Draft Runtime Request Refresh

Status: request infrastructure only.

Phase marker: external reviewer persisted document failure candidate draft runtime request refresh v0.

This refresh points reviewer-facing request surfaces to the persisted document failure candidate draft preview runtime proof.

It does not edit the live public issue body. A live issue-body update must stay in a separate issue-body refresh gate if needed.

It does not add runtime behavior.

## Latest Proof To Inspect

persisted document failure candidate draft preview runtime proof:

```text
docs/review/persisted-document-failure-candidate-draft-preview-runtime-smoke.md
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/failure-case-draft-preview -> 200
GET /failure-cases -> 200
```

Observed runtime markers:

```text
preview_only_not_persisted
human_confirmation_required -> true
pdf_no_extractable_text
chunk_handoff_no_chunks
persisted_document_failure_case_candidate
metadata-derived from document profile_json
failure_case_count_delta -> 0
```

## Reviewer Surfaces Refreshed

- `CONTRIBUTING.md`
- `.github/ISSUE_TEMPLATE/external-review-feedback.md`
- `docs/review/external-review-request.md`
- `docs/review/external-reader-proof-path.md`
- `docs/review/external-reviewer-brief.md`
- `docs/review/external-reviewer-link-map.md`
- `docs/review/external-reviewer-shortlist.md`
- `docs/application/portfolio-index.md`
- `README.md`
- `docs/GOAL.md`
- `docs/runbook.md`

## Allowed Claim

External reviewers can now reach the latest local runtime proof that a persisted no-text PDF failure candidate can be turned into a preview-only manual failure-case draft without creating `failure_cases`.

## Boundary

This is request infrastructure only.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not customer validation.

This is not Braincrew acceptance.

This does not prove that any reviewer has inspected the repository.

This does not edit the live public issue body.

This adds no runtime behavior, schema, migration, endpoint, hosted deployment, robust PDF extraction, OCR, table extraction, layout fidelity, raw uploaded byte storage, full parsed text persistence, embedding generation, semantic retrieval quality evidence, Evidence Ledger generation, Noise Gate behavior, report generation, LLM output, automatic failure-case creation, automatic root-cause analysis, or product-complete claim.

Explicit boundary markers:

```text
not automatic failure-case creation
not robust PDF extraction
not OCR
not product-complete
```

## Next Gate

If this proof should be routed through the live public issue, add a separate issue-body refresh gate. Until then, issue #1 external reviewer feedback remains pending.
