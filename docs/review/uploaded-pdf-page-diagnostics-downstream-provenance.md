# Uploaded PDF Page Diagnostics Downstream Provenance

Status: route-level implementation proof.

Phase marker: uploaded PDF page diagnostics downstream provenance v0.

This phase makes PDF page diagnostics travel beyond `POST /documents/upload-preview` into explicit upload chunk persistence and document retrieval-run candidate provenance.

## Implemented Path

```text
POST /documents/upload-chunks
  -> document.profile_json
  -> document_chunks.metadata_json
  -> POST /documents/{document_id}/retrieval-runs
  -> retrieval_runs.metadata_json
  -> retrieval candidate metadata
```

The downstream metadata carries:

```text
page_diagnostics_available
layout_block_diagnostics_available
extraction_scope
page_text_char_counts
extracted_page_count
empty_page_count
text_block_count
image_block_count
```

The retrieval-run provenance boundary remains:

```text
retrieval_run_candidate_chunk_metadata_only
```

## Allowed Claim

Uploaded digital PDF page diagnostics can now be preserved in explicit uploaded-file-to-chunks persistence and summarized through persisted document retrieval-run candidate metadata.

## Boundary

This is route-level implementation proof and test coverage.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not customer validation.

This is not Braincrew acceptance.

This is not robust PDF extraction.

This is not OCR.

This is not table extraction.

This is not layout fidelity.

This is not raw file storage.

This is not full parsed text persistence.

This does not generate embeddings.

This does not prove semantic retrieval quality.

This does not generate Evidence Ledger entries.

This does not run a Noise Gate.

This does not generate a report.

This is not product-complete.

## Test Coverage

```text
test_uploaded_pdf_page_diagnostics_flow_into_chunk_and_retrieval_provenance
```

The test verifies `POST /documents/upload-chunks` and `POST /documents/{document_id}/retrieval-runs` preserve page diagnostics including `page_text_char_counts`, `empty_page_count`, `text_block_count`, and `image_block_count`.

## Next Gate

Next recommended gate: local Docker/FastAPI runtime smoke for uploaded PDF page diagnostics downstream provenance if runtime proof is needed, external reviewer feedback v0 if qualifying outside feedback exists, or another source-first product gate selected from `docs/GOAL.md`.
