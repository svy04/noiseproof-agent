# PDF Binary Fixture Smoke Preview Response Contract

Status: implemented.

Phase marker: PDF binary fixture smoke preview response contract v0.

## Purpose

Make `GET /documents/pdf-binary-fixture-smoke-preview` easier to inspect by adding compact response fields that summarize the proof boundary without requiring a reviewer to dig through nested fixture data first.

This is response-shape clarity only. It does not broaden the API's truth scope.

## Added Response Fields

```text
reviewer_summary
response_contract
```

`reviewer_summary` records:

```text
api_surface: GET /documents/pdf-binary-fixture-smoke-preview
fixture_source_boundary: repo_synthetic_binary_fixtures_only_no_arbitrary_upload
persistence_boundary: preview_only_not_persisted
claim_boundary: binary_fixture_smoke_only_not_robust_pdf_extraction
fixture_count: 2
passed_count: 2
failed_count: 0
document_count_delta: 0
table_adapter_rows: [[Segment, Growth], [Enterprise, 12%]]
```

`response_contract` records:

```text
contract: pdf_binary_fixture_smoke_preview_response_contract_v0
truth_scope: repo_synthetic_binary_fixture_smoke_only
not_claimed:
- arbitrary_uploaded_file_behavior
- document_persistence
- robust_pdf_extraction
- default_pdf_parser_table_extraction
- hosted_deployment
- external_reviewer_feedback
- product_complete
```

## Updated Artifacts

```text
apps/api/app/schemas.py
apps/api/app/services/pdf_binary_fixture_smoke_preview.py
apps/api/tests/test_routes.py
apps/api/tests/test_docs.py
```

## Boundary

This is response contract clarity only.

It is not new runtime evidence.
It is not arbitrary uploaded-file behavior.
It is not document persistence evidence.
It is not robust PDF extraction evidence.
It is not default PdfParser table extraction.
It is not table extraction evidence for arbitrary market PDFs.
It is not hosted deployment evidence.
It is not external reviewer feedback.
It is not customer validation.
It is not Braincrew acceptance.
It is not product-complete.

## Next Gate

Next gate: local Docker/FastAPI runtime smoke for this response contract if runtime proof is needed, remote verification after push, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from the current repository state.
