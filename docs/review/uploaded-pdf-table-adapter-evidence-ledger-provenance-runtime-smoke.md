# Uploaded PDF Table Adapter Evidence Ledger Provenance Runtime Smoke

Status: local runtime smoke evidence.

Phase marker: uploaded PDF table adapter Evidence Ledger provenance runtime smoke v0.

This smoke records local Docker PostgreSQL plus live FastAPI HTTP evidence that
bounded default `PdfParser` table-adapter metadata survives the explicit
uploaded-PDF chunk persistence path, persisted document-chunk retrieval, and
retrieval-run-linked Evidence Ledger persistence into stored Evidence Ledger row
metadata.

It is a runtime smoke record for one deterministic synthetic PDF fixture, not a
broad PDF parsing, table extraction, Evidence Ledger quality, or truth claim.

## Environment

```text
Docker version 29.4.3, build 055a478
Docker Compose version v5.1.3
Compose project -> noiseproof-phase806
POSTGRES_PORT=55460
API port -> 8121
noiseproof-phase806-db-1 -> healthy
Applied migrations: 23
Pending migrations: 0
```

## Commands

```powershell
$env:POSTGRES_PORT = "55460"
docker compose -p noiseproof-phase806 config
docker compose -p noiseproof-phase806 up -d db
cd apps/api
$env:DATABASE_URL = "postgresql://noiseproof:noiseproof@localhost:55460/noiseproof"
uv run python -m app.migration_runner
uv run python -m app.migration_runner --status
uv run uvicorn app.main:app --host 127.0.0.1 --port 8121
```

HTTP smoke:

```text
GET /health
POST /documents/upload-chunks
POST /documents/{document_id}/retrieval-runs
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger
GET /evidence-ledgers?retrieval_run_id={retrieval_run_id}
```

The PDF was generated in memory with PyMuPDF, using drawn grid lines and text
labels to create one simple table-shaped candidate.

## Observed

```text
GET /health -> 200
POST /documents/upload-chunks -> 201
POST /documents/{document_id}/retrieval-runs -> 201
POST /retrieval-runs/{retrieval_run_id}/evidence-ledger -> 201
GET /evidence-ledgers?retrieval_run_id={retrieval_run_id} -> 200
document_id -> 1e3358e0-85f1-4a37-a299-d7d5550a7493
chunk_id -> ef40e7e1-76c2-4970-8c3f-254003f87708
retrieval_run_id -> 3409326b-1845-4d98-86d1-a61854fe1f89
evidence_ledger_entry_id -> 62e54026-d7bd-40fc-ad30-14c60487d9db
stored_entry_count -> 1
document_profile_default_pdf_parser_table_adapter_metadata -> True
chunk_metadata_default_pdf_parser_table_adapter_metadata -> True
retrieval_metadata_default_pdf_parser_table_adapter_metadata -> True
evidence_entry_default_pdf_parser_table_adapter_metadata -> True
listed_entry_default_pdf_parser_table_adapter_metadata -> True
table_adapter.extracted_table_rows -> [['Segment', 'Growth'], ['Enterprise', '12%']]
table_adapter.robust_pdf_extraction -> False
table_extraction_performed remains false -> False
source_provenance_boundary -> evidence_ledger_entry_metadata_from_retrieval_run_candidate_chunk
persistence_boundary -> retrieval_run_linked_evidence_ledger_no_llm_no_embeddings
warning_boundary_present -> True
all_required_markers_passed -> True
```

## Allowed Claim

NoiseProof has local runtime evidence that bounded default `PdfParser`
table-adapter metadata can survive uploaded PDF chunk persistence, persisted
document-chunk retrieval, and retrieval-run-linked Evidence Ledger persistence
into stored Evidence Ledger row metadata through live FastAPI HTTP.

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
It is not final truth adjudication.
It is not Noise Gate behavior.
It is not final report generation.
It is not production readiness.
It is not product-complete.

## Cleanup

```powershell
Stop-Process -Id 38640 -Force
docker compose -p noiseproof-phase806 down -v
```

## Next Gate

Next gate: remote verification after push, external reviewer feedback v0 if
qualifying outside feedback exists, or another source-first product gate
selected from the current repository state.
