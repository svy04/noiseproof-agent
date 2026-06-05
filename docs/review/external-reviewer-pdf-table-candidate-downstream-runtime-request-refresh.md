# External Reviewer PDF Table-candidate Downstream Runtime Request Refresh

Status: request infrastructure only.

Phase marker: external reviewer PDF table-candidate downstream runtime request refresh v0.

This refresh points reviewer-facing request surfaces to the uploaded PDF table-candidate downstream runtime proof and its remote verification.

It does not edit the live public issue body. The live issue body is handled by a separate issue-body refresh gate if needed.

It does not add runtime behavior.

## Latest Proof To Inspect

uploaded PDF table-candidate downstream runtime proof:

```text
docs/review/uploaded-pdf-table-candidate-downstream-provenance-runtime-smoke.md
docs/review/uploaded-pdf-table-candidate-downstream-provenance-remote-verification.md
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/retrieval-runs -> 201
GET /retrieval-runs -> 200
```

Observed downstream diagnostics markers:

```text
document_profile_table_candidate_count -> 1
chunk_metadata_table_candidate_count -> 1
retrieval_metadata_table_candidate_count -> 1
retrieval_candidate_table_candidate_count -> 1
document_profile_table_candidate_shapes -> page_index=0,row_count=2,col_count=2,cell_count=4
chunk_metadata_table_extraction_performed -> false
retrieval_metadata_table_extraction_performed -> false
retrieval_candidate_table_extraction_performed -> false
source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only
raw_file_storage -> false
parsed_text_storage -> false
```

Remote verification:

```text
head_sha -> adf8b7a6a714e119cbaa2db88f77fa89665f3b56
CI run 27038450094 -> success
External Feedback Screen run 27038450101 -> success
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

External reviewers can now reach the latest local runtime proof and remote workflow verification that uploaded PDF table-candidate metadata flows into explicit upload chunk metadata and persisted document retrieval-run candidate metadata.

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
not table extraction
```

## Next Gate

If this proof should be routed through the live public issue, add a separate issue-body refresh gate. Until then, issue #1 external reviewer feedback remains pending.
