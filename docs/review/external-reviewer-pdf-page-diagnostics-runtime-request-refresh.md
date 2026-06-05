# External Reviewer PDF Page Diagnostics Runtime Request Refresh

Status: request infrastructure only.

Phase marker: external reviewer PDF page diagnostics runtime request refresh v0.

This refresh points reviewer-facing request surfaces to the uploaded PDF page diagnostics runtime proof.

It does not edit the live public issue body. The live issue body is handled by a separate issue-body refresh gate if needed.

It does not add runtime behavior.

## Latest Proof To Inspect

uploaded PDF page diagnostics proof:

```text
docs/review/uploaded-pdf-page-diagnostics-runtime-smoke.md
POST /documents/upload-preview
```

Observed PDF diagnostics markers:

```text
parser -> pdf-pymupdf
digital_pdf_text_extraction -> true
robust_pdf_extraction -> false
page_diagnostics_available -> true
layout_block_diagnostics_available -> true
extraction_scope -> digital_text_page_diagnostics
page_text_char_counts -> [39]
extracted_page_count -> 1
empty_page_count -> 0
text_block_count -> 1
image_block_count -> 0
document_count_delta -> 0
persistence_boundary -> preview_only_not_persisted
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

External reviewers can now reach the latest local runtime proof that uploaded digital PDF page diagnostics are returned by `POST /documents/upload-preview` from the standard review entry surfaces.

## Boundary

This is request infrastructure only.

This is not external reviewer feedback.

This is not hosted deployment evidence.

This is not customer validation.

This is not Braincrew acceptance.

This does not prove that any reviewer has inspected the repository.

This does not edit the live public issue body.

This adds no runtime behavior, schema, migration, endpoint, hosted deployment, robust PDF extraction, OCR, table extraction, layout fidelity, raw uploaded byte storage, parsed text persistence, embedding generation, semantic retrieval quality evidence, Evidence Ledger generation, Noise Gate behavior, report generation, LLM output, automatic failure-case creation, or product-complete claim.

Explicit boundary marker:

```text
not robust PDF extraction
```

## Next Gate

If this proof should be routed through the live public issue, add a separate issue-body refresh gate. Until then, issue #1 external reviewer feedback remains pending.
