# Uploaded PDF Table Adapter Noise Gate Provenance Runtime Smoke

Status: local runtime smoke evidence.

Phase marker: uploaded PDF table adapter Noise Gate provenance runtime smoke v0.

This smoke records local Docker PostgreSQL plus live FastAPI HTTP evidence that
bounded uploaded-PDF table-adapter metadata can survive the explicit
uploaded-PDF chunk persistence path, persisted document-chunk retrieval,
retrieval-run-linked Evidence Ledger persistence, and retrieval-run-linked
Noise Gate persistence into the stored Noise Gate `stage_input_manifest`.

It is a runtime smoke record for one deterministic synthetic PDF fixture, not a
broad PDF parsing, table extraction, Noise Gate quality, or truth claim.

## Environment

```text
Docker version 29.4.3, build 055a478
Docker Compose version v5.1.3
Compose project -> noiseproof-phase815
POSTGRES_PORT=55461
API port -> 8122
noiseproof-phase815-db-1 -> healthy
Applied migrations: 23
Pending migrations: 0
```

## Commands

```powershell
$env:POSTGRES_PORT = "55461"
docker compose -p noiseproof-phase815 config
docker compose -p noiseproof-phase815 up -d db
cd apps/api
$env:DATABASE_URL = "postgresql://noiseproof:noiseproof@localhost:55461/noiseproof"
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8122
```

HTTP smoke:

```text
GET /health
POST /documents/upload-chunks
POST /documents/{document_id}/retrieval-runs
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger
POST /retrieval-runs/{retrieval_run_id}/noise-gate
GET /noise-gates
```

The PDF was generated in memory with PyMuPDF, using drawn grid lines and text
labels to create one simple table-shaped candidate.

## Observed

```text
GET /health -> 200
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/retrieval-runs -> 201
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger -> 201
POST /retrieval-runs/{retrieval_run_id}/noise-gate -> 201
GET /noise-gates -> 200
document_id -> ab134b28-62ea-4175-9c66-77fa35dc1104
chunk_id -> 2176b945-b304-428a-a7be-9205d55daf5a
retrieval_run_id -> 0f511e15-f665-40b8-9411-3bc6c0b251be
evidence_ledger_entry_id -> a3718b48-2895-466b-94bd-e9fc29a43ea8
noise_gate_id -> 826c1bc9-8ee0-4ca6-a769-4ed4c1df6fbf
listed_noise_gate_count -> 1
manifest_input_evidence_ledger_entry_ids -> ['a3718b48-2895-466b-94bd-e9fc29a43ea8']
document_profile_default_pdf_parser_table_adapter_metadata -> True
chunk_metadata_default_pdf_parser_table_adapter_metadata -> True
retrieval_metadata_default_pdf_parser_table_adapter_metadata -> True
evidence_entry_default_pdf_parser_table_adapter_metadata -> True
default_pdf_parser_table_adapter_metadata -> True
listed_manifest_default_pdf_parser_table_adapter_metadata -> True
table_adapter_extraction_performed -> True
table_adapter.table_extraction_engine -> pymupdf-find_tables-extract
table_adapter.robust_pdf_extraction -> False
table_adapter.extracted_table_rows -> [['Segment', 'Growth'], ['Enterprise', '12%']]
table_extraction_performed -> False
source_provenance_boundary -> evidence_ledger_entry_metadata_from_retrieval_run_candidate_chunk
source_pdf_table_adapter_provenance_boundary -> noise_gate_stage_input_manifest_from_evidence_ledger_entry_metadata
handoff_performs_pdf_table_extraction -> False
warning_preserved_metadata -> True
warning_no_pdf_table_extraction -> True
all_required_markers_passed -> True
```

Noise Gate warnings included:

```text
Uploaded PDF table-adapter metadata was preserved into Noise Gate stage_input_manifest as provenance only.
Noise Gate handoff does not perform PDF table extraction and is not robust PDF extraction evidence.
```

## Allowed Claim

NoiseProof has local runtime evidence that bounded default `PdfParser`
table-adapter metadata can survive uploaded PDF chunk persistence, persisted
document-chunk retrieval, retrieval-run-linked Evidence Ledger persistence, and
retrieval-run-linked Noise Gate persistence into the stored Noise Gate
`stage_input_manifest` through live FastAPI HTTP.

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
It is not Evidence Ledger quality evidence.
It is not Noise Gate quality evidence.
It is not final truth adjudication.
It is not final report generation.
It is not production readiness.
It is not product-complete.

## Cleanup

```powershell
Stop-Process -Id 26956 -Force
docker compose -p noiseproof-phase815 down -v
```

## Next Gate

Next gate: remote verification after push, external-reader route refresh if
this proof should become reviewer-facing, external reviewer feedback v0 if
qualifying outside feedback exists, or another source-first product gate
selected from the current repository state.
