# PDF Binary Fixture Smoke Preview Response Contract Runtime Smoke

Status: verified.

Phase marker: pdf binary fixture smoke preview response contract runtime smoke v0.

## Purpose

Record local Docker PostgreSQL plus live FastAPI HTTP evidence that
`GET /documents/pdf-binary-fixture-smoke-preview` exposes the Phase 790
`reviewer_summary` and `response_contract` fields through the actual local
service path.

This verifies the response contract at runtime. It does not expand PDF parsing
capability and does not accept arbitrary uploads.

## Runtime Environment

```text
Docker version 29.4.3
Docker Compose version v5.1.3
Compose project: noiseproof-phase791
POSTGRES_PORT=55458
FastAPI URL: http://127.0.0.1:8119
```

## Migration State

Fresh DB migration runner output:

```text
Applied migrations: 0
Pending migrations: 23
Applied migrations: 23
Pending migrations: 0
```

## HTTP Smoke

```text
GET /health -> 200
GET /documents/pdf-binary-fixture-smoke-preview -> 200
reviewer_summary.api_surface=GET /documents/pdf-binary-fixture-smoke-preview
reviewer_summary.fixture_source_boundary=repo_synthetic_binary_fixtures_only_no_arbitrary_upload
reviewer_summary.persistence_boundary=preview_only_not_persisted
reviewer_summary.claim_boundary=binary_fixture_smoke_only_not_robust_pdf_extraction
reviewer_summary.fixture_count=2
reviewer_summary.passed_count=2
reviewer_summary.failed_count=0
reviewer_summary.document_count_delta=0
response_contract.contract=pdf_binary_fixture_smoke_preview_response_contract_v0
response_contract.truth_scope=repo_synthetic_binary_fixture_smoke_only
response_contract.not_claimed includes robust_pdf_extraction
table_adapter_rows=[[Segment, Growth], [Enterprise, 12%]]
document_count_before=0
document_count_after=0
document_count_delta=0
agent_run_count_before=0
agent_run_count_after=1
failure_case_count_before=0
failure_case_count_after=0
```

Observed `response_contract.not_claimed`:

```text
arbitrary_uploaded_file_behavior
document_persistence
robust_pdf_extraction
default_pdf_parser_table_extraction
hosted_deployment
external_reviewer_feedback
product_complete
```

Cleanup:

```text
uvicorn stopped
docker compose -p noiseproof-phase791 down -v -> completed
docker compose -p noiseproof-phase791 ps --format json -> no services
GET-NetTCPConnection -LocalPort 8119 -> no listening process
```

## Boundary

This is local runtime evidence only.

It is not hosted deployment evidence.
It is not external reviewer feedback.
It is not customer validation.
It is not Braincrew acceptance.
It is not arbitrary uploaded-file behavior.
It is not document persistence evidence.
It is not retrieval behavior.
It is not Evidence Ledger generation.
It is not robust PDF extraction evidence.
It is not robust PDF extraction implementation.
It is not OCR implementation.
It is not default PdfParser table extraction.
It is not table extraction evidence for arbitrary market PDFs.
It is not product-complete.

## Next Gate

Next gate: remote verification for this runtime-smoke proof after push,
external reviewer feedback v0 if qualifying outside feedback exists, or another
source-first product gate selected from the current repository state.
