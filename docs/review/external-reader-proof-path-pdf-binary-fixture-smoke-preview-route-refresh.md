# External-reader Proof Path PDF Binary Fixture Smoke Preview Route Refresh

Status: implemented.

Phase marker: external-reader proof path PDF binary fixture smoke preview route refresh v0.

## Purpose

Route first-pass external reviewers to the Phase 783/784 PDF binary fixture smoke preview runtime proof chain without making any new runtime, upload, or PDF extraction claim.

This refresh makes the live FastAPI preview route easier to find from the compact proof path, link map, and 90-second shortlist.

## Updated Artifacts

```text
docs/review/external-reader-proof-path.md
docs/review/external-reviewer-link-map.md
docs/review/external-reviewer-shortlist.md
README.md
docs/GOAL.md
docs/runbook.md
docs/application/portfolio-index.md
apps/api/tests/test_docs.py
```

## Routed Proof Chain

```text
docs/review/pdf-binary-fixture-smoke-preview-runtime-smoke.md
docs/review/pdf-binary-fixture-smoke-preview-runtime-smoke-remote-verification.md
GET /documents/pdf-binary-fixture-smoke-preview
apps/api/app/services/pdf_binary_fixture_smoke_preview.py
apps/api/app/routes/documents.py
apps/api/app/schemas.py
```

## Route Markers

```text
GET /documents/pdf-binary-fixture-smoke-preview
fixture_source_boundary=repo_synthetic_binary_fixtures_only_no_arbitrary_upload
persistence_boundary=preview_only_not_persisted
claim_boundary=binary_fixture_smoke_only_not_robust_pdf_extraction
fixture_count=2
passed_count=2
failed_count=0
document_count_delta=0
agent_run_count=1
table_adapter_rows=[[Segment, Growth], [Enterprise, 12%]]
CI run `27073528326`
External Feedback Screen run `27073528323`
remote verification follow-up CI run `27073643829`
remote verification follow-up External Feedback Screen run `27073643828`
```

## Boundary

This is reviewer route hygiene only.

It is not new runtime evidence.
It is not the runtime smoke itself.
It is not arbitrary uploaded-file behavior.
It is not document persistence evidence.
It is not robust PDF extraction evidence.
It is not robust PDF extraction implementation.
It is not OCR implementation.
It is not default PdfParser table extraction.
It is not table extraction evidence for arbitrary market PDFs.
It is not hosted deployment evidence.
It is not external reviewer feedback.
It is not customer validation.
It is not Braincrew acceptance.
It is not product-complete.

## Next Gate

Next gate: remote verification for this reader-route refresh after push, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from the current repository state.
