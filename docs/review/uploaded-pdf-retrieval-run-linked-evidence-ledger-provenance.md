# Uploaded PDF Retrieval-run-linked Evidence Ledger Provenance

Status: implemented

Phase marker: uploaded PDF retrieval-run-linked Evidence Ledger provenance v0

## Goal

Preserve uploaded digital PDF parser/source provenance when retrieval-run candidate chunks are converted into persisted Evidence Ledger entries.

This gate keeps the boundary small: it stores source provenance metadata on Evidence Ledger rows generated from an existing retrieval run. It does not change retrieval behavior, Evidence Ledger judgment logic, Noise Gate behavior, or report generation.

## Implemented Surface

- `db/migrations/018_evidence_ledger_metadata_json.sql` adds `evidence_ledger_entries.metadata_json`.
- `db/init/001_schema.sql` now includes `metadata_json JSONB NOT NULL DEFAULT '{}'::jsonb` for fresh databases.
- `packages/ingestion/types.py` carries `EvidenceLedgerEntry.metadata_json`.
- `packages/ingestion/evidence/ledger.py` copies candidate metadata into each generated entry.
- `apps/api/app/db.py` persists `metadata_json` with Evidence Ledger rows.
- `apps/api/app/schemas.py` exposes `metadata_json` in `EvidenceLedgerEntryOut`.
- `apps/api/app/services/retrieval_run_evidence.py` marks the handoff boundary in candidate metadata before persistence.

## Route-level Proof Path

The focused route test exercises this path:

1. `POST /documents/upload-chunks`
2. `POST /documents/{document_id}/retrieval-runs`
3. `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`
4. `GET /evidence-ledgers?retrieval_run_id=`

Observed provenance markers:

```text
metadata_json.parser -> pdf-pymupdf
metadata_json.digital_pdf_text_extraction -> true
metadata_json.robust_pdf_extraction -> false
metadata_json.source_provenance_boundary -> evidence_ledger_entry_metadata_from_retrieval_run_candidate_chunk
metadata_json.persistence_boundary -> retrieval_run_linked_evidence_ledger_no_llm_no_embeddings
```

## Boundaries

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not robust PDF extraction, OCR, table extraction, or layout fidelity evidence.

This is not raw file storage or full parsed text persistence.

This is not Noise Gate behavior.

This is not report generation.

This is not LLM, embedding, or semantic retrieval evidence.

This is not product-complete or production-readiness evidence.

## Next Gate

The next bounded gate can be uploaded PDF retrieval-run-linked Evidence Ledger provenance runtime smoke v0, external reviewer feedback v0 if a qualifying external comment exists, or another source-first product gate selected from `docs/GOAL.md`.
