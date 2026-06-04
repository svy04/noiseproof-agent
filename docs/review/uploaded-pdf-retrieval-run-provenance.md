# Uploaded PDF Retrieval-run Provenance

Status: bounded route-level product proof.

Phase marker: uploaded PDF retrieval-run provenance v0.

## Purpose

This gate keeps uploaded PDF parser provenance visible when PDF-derived chunks are used to create a persisted document retrieval run.

Before this gate, uploaded PDF bytes could pass through PyMuPDF extraction into persisted chunk rows, and document retrieval runs could use those chunks. The retrieval run still did not summarize whether the matched candidate chunks came from `pdf-pymupdf`.

After this gate, `POST /documents/upload-chunks` stores minimal parser provenance on derived chunk metadata, and `POST /documents/{document_id}/retrieval-runs` summarizes candidate provenance in `retrieval_runs.metadata_json`.

## Implemented

```text
chunk metadata now records parser for upload chunk handoffs
PDF chunk metadata records digital_pdf_text_extraction and robust_pdf_extraction
document chunk retrieval run metadata records candidate_source_types
document chunk retrieval run metadata records candidate_parsers
document chunk retrieval run metadata records digital_pdf_text_extraction for PDF candidates
document chunk retrieval run metadata records robust_pdf_extraction for PDF candidates
route coverage for uploaded PDF -> chunks -> retrieval-run provenance
```

Observed route-level test markers:

```text
upload parser -> pdf-pymupdf
chunk metadata parser -> pdf-pymupdf
chunk metadata digital_pdf_text_extraction -> true
chunk metadata robust_pdf_extraction -> false
retrieval metadata candidate_source_types -> ["pdf"]
retrieval metadata candidate_parsers -> ["pdf-pymupdf"]
retrieval metadata digital_pdf_text_extraction -> true
retrieval metadata robust_pdf_extraction -> false
source_provenance_boundary -> retrieval_run_candidate_chunk_metadata_only
```

## Boundary

This is route-level test evidence only.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not robust PDF extraction.

OCR, table extraction, and layout fidelity are not claimed.

This does not store raw uploaded bytes.

This does not store full parsed text.

This does not generate embeddings.

This does not prove semantic retrieval quality.

This does not create Evidence Ledger entries, Noise Gate records, reports, or failure cases automatically.

This does not call an LLM.

This is not production readiness or product-complete.

## Tests

```text
uv run pytest -q tests/test_routes.py -k "uploaded_pdf_chunk_retrieval_run_keeps_pdf_parser_provenance"
```

## Next Gate

```text
external reviewer feedback v0 remains pending, or select the next source-first product gate
```
