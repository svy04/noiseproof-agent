# PDF Binary Fixture Smoke Preview Runtime Smoke

Status: verified.

Phase marker: PDF binary fixture smoke preview runtime smoke v0.

## Purpose

Record local Docker PostgreSQL plus live FastAPI HTTP evidence that `GET /documents/pdf-binary-fixture-smoke-preview` exposes the repository's synthetic PDF binary fixture parser/adapter smoke through an API preview without accepting arbitrary uploads or creating document rows.

This verifies the route and response boundary through a live local service path. It does not expand PDF parsing capability.

## Runtime Environment

```text
Docker version 29.4.3
Docker Compose version v5.1.3
Compose project: noiseproof-phase783
POSTGRES_PORT=55457
FastAPI URL: http://127.0.0.1:8118
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
preview_packet=pdf_binary_fixture_provenance_packet_v0
fixture_source_boundary=repo_synthetic_binary_fixtures_only_no_arbitrary_upload
persistence_boundary=preview_only_not_persisted
claim_boundary=binary_fixture_smoke_only_not_robust_pdf_extraction
robust_pdf_extraction_claimed=False
fixture_count=2
passed_count=2
failed_count=0
binary_born_digital_text.parser=pdf-pymupdf
binary_born_digital_text.digital_pdf_text_extraction=True
binary_deterministic_table_adapter.table_candidate_count=1
binary_deterministic_table_adapter.table_adapter.table_extraction_performed=True
table_adapter_rows=[[Segment, Growth], [Enterprise, 12%]]
document_count_before=0
document_count_after=0
document_count_delta=0
agent_run_count=1
failure_case_count=0
warning_count=3
```

Cleanup:

```text
uvicorn stopped
docker compose -p noiseproof-phase783 down -v -> completed
docker compose -p noiseproof-phase783 ps --format json -> no services
GET-NetTCPConnection -LocalPort 8118 -> no listening process
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

Next gate: remote verification for this runtime-smoke proof after push, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from the current repository state.
