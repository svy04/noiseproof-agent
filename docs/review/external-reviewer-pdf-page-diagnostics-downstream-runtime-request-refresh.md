# External Reviewer PDF Page Diagnostics Downstream Runtime Request Refresh

Status: request infrastructure only.

Phase marker: external reviewer PDF page diagnostics downstream runtime request refresh v0.

This refresh points reviewer-facing request surfaces to the uploaded PDF page diagnostics downstream runtime proof.

It does not edit the live public issue body. The live issue body is handled by a separate issue-body refresh gate if needed.

It does not add runtime behavior.

## Latest Proof To Inspect

uploaded PDF page diagnostics downstream runtime proof:

```text
docs/review/uploaded-pdf-page-diagnostics-downstream-provenance-runtime-smoke.md
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/retrieval-runs -> 201
GET /retrieval-runs -> 200
```

Observed downstream diagnostics markers:

```text
document_profile_page_text_char_counts -> [39]
chunk_metadata_page_text_char_counts -> [39]
retrieval_metadata_page_text_char_counts -> [39]
retrieval_candidate_page_text_char_counts -> [39]
document_profile_empty_page_count -> 0
chunk_metadata_text_block_count -> 1
retrieval_metadata_image_block_count -> 0
source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only
raw_file_storage -> false
parsed_text_storage -> false
```

## Reviewer Surfaces Refreshed

- `CONTRIBUTING.md`
- `.github/ISSUE_TEMPLATE/external-review-feedback.md`
- `docs/review/external-review-request.md`
- `docs/review/external-reader-proof-path.md`
- `docs/review/external-reviewer-brief.md`
- `docs/review/external-reviewer-link-map.md`
- `docs/application/portfolio-index.md`
- `README.md`
- `docs/GOAL.md`
- `docs/runbook.md`

## Allowed Claim

External reviewers can now reach the latest local runtime proof that uploaded PDF page diagnostics flow into explicit upload chunk metadata and persisted document retrieval-run candidate metadata.

## Boundary

This is request infrastructure only.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not customer validation.

This is not Braincrew acceptance.

This does not prove that any reviewer has inspected the repository.

This does not edit the live public issue body.

This adds no runtime behavior, schema, migration, endpoint, hosted deployment, robust PDF extraction, OCR, table extraction, layout fidelity, raw uploaded byte storage, full parsed text persistence, embedding generation, semantic retrieval quality evidence, Evidence Ledger generation, Noise Gate behavior, report generation, LLM output, automatic failure-case creation, or product-complete claim.

Explicit boundary marker:

```text
not robust PDF extraction
```

## Next Gate

If this proof should be routed through the live public issue, add a separate issue-body refresh gate. Until then, issue #1 external reviewer feedback remains pending.
