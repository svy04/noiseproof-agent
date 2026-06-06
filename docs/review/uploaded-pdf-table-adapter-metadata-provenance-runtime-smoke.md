# Uploaded PDF Table Adapter Metadata Provenance Runtime Smoke

Status: local runtime smoke evidence.

Phase marker: uploaded PDF table adapter metadata provenance runtime smoke v0.

This smoke records local Docker PostgreSQL plus live FastAPI HTTP evidence that
default `PdfParser` table-adapter metadata survives the explicit uploaded-PDF
chunk persistence path and persisted document retrieval-run response metadata.

It is a runtime smoke record for one deterministic synthetic PDF fixture, not a
broad PDF parsing, table extraction, or retrieval quality claim.

## Environment

```text
Docker version 29.4.3, build 055a478
Docker Compose version v5.1.3
Compose project -> noiseproof-phase797
POSTGRES_PORT=55459
API port -> 8120
noiseproof-phase797-db-1 -> healthy
Applied migrations: 23
Pending migrations: 0
```

## Commands

```powershell
$env:POSTGRES_PORT = "55459"
docker compose -p noiseproof-phase797 config
docker compose -p noiseproof-phase797 up -d db
cd apps/api
$env:DATABASE_URL = "postgresql://noiseproof:noiseproof@localhost:55459/noiseproof"
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8120
```

HTTP smoke:

```text
GET /health
POST /documents/upload-chunks
GET /documents
GET /documents/{document_id}/chunks
POST /documents/{document_id}/retrieval-runs
GET /retrieval-runs
```

The PDF was generated in memory with PyMuPDF, using drawn grid lines and text
labels to create one simple table-shaped candidate.

## Observed

```text
GET /health -> 200
health_status -> ok
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/retrieval-runs -> 201
GET /retrieval-runs -> 200
parser -> pdf-pymupdf
document_id -> dd5bc736-f707-45e5-95df-481217d989b1
chunk_id -> ba658de6-feb8-46f6-b94b-ac07a826054f
chunk_count -> 1
retrieval_id -> 935fa915-cfb3-4a42-b8b9-5715d9165c42
retrieval_status -> completed
retrieval_result_count -> 1
document_profile_default_pdf_parser_table_adapter_metadata -> true
document_profile_table_adapter_extraction_performed -> true
document_profile_table_adapter_engine -> pymupdf-find_tables-extract
chunk_metadata_default_pdf_parser_table_adapter_metadata -> true
chunk_metadata_table_adapter_extraction_performed -> true
chunk_metadata_table_adapter_engine -> pymupdf-find_tables-extract
retrieval_metadata_default_pdf_parser_table_adapter_metadata -> true
retrieval_metadata_table_adapter_extraction_performed -> true
retrieval_candidate_default_pdf_parser_table_adapter_metadata -> true
retrieval_candidate_table_adapter_extraction_performed -> true
table_adapter.extracted_table_rows -> [[Segment, Growth], [Enterprise, 12%]]
table_adapter.robust_pdf_extraction -> false
document_profile_table_extraction_performed -> false
chunk_metadata_table_extraction_performed -> false
retrieval_metadata_table_extraction_performed -> false
retrieval_candidate_table_extraction_performed -> false
table_extraction_performed remains false
source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only
candidate_source_types -> [pdf]
candidate_parsers -> [pdf-pymupdf]
raw_file_storage -> false
parsed_text_storage -> false
all_required_markers_passed -> true
```

## Allowed Claim

NoiseProof has local runtime evidence that default `PdfParser` table-adapter
metadata can survive uploaded PDF chunk persistence and persisted document
retrieval-run provenance through live FastAPI HTTP.

## Boundary

This is local runtime evidence only.

It is not hosted deployment evidence.
It is not external reviewer feedback.
It is not customer validation.
It is not Braincrew acceptance.
It is not robust PDF extraction evidence.
It is not table extraction evidence for arbitrary market PDFs.
It is not OCR implementation.
It is not layout fidelity evidence.
It is not raw file storage.
It is not full parsed text persistence.
It is not embedding generation.
It is not semantic retrieval quality evidence.
It is not Evidence Ledger generation.
It is not Noise Gate behavior.
It is not final report generation.
It is not production readiness.
It is not product-complete.

## Next Gate

Next gate: remote verification after push, external reviewer feedback v0 if
qualifying outside feedback exists, or another source-first product gate
selected from the current repository state.
