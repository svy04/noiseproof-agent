# Uploaded PDF Downstream Handoff Application Refresh

Phase marker: uploaded PDF downstream handoff application refresh v0.

This refresh surfaces the local runtime proof for uploaded PDF downstream handoff in the application-facing documentation set.

It adds no runtime behavior.

## Primary Proof

```text
docs/review/uploaded-pdf-downstream-handoff-runtime-smoke.md
```

The runtime smoke records local Docker PostgreSQL plus live FastAPI HTTP evidence for:

```text
POST /documents/upload-preview
POST /documents/upload-chunk-preview
POST /documents/upload-chunks
GET /documents/{document_id}/chunks
POST /documents/upload-retrieval-preview
```

Observed PDF handoff markers:

```text
parser -> pdf-pymupdf
digital_pdf_text_extraction -> true
robust_pdf_extraction -> false
chunk_text_contains_pdf_text -> true
retrieval_text_contains_pdf_text -> true
replacement_decode_warning_present -> false
```

Observed persistence boundary:

```text
explicit_upload_to_chunks_no_raw_file_storage
chunk_text_only_no_raw_file_storage
raw_file_storage -> false
parsed_text_storage -> false
```

## Application Surface Updated

This refresh points the following reader surfaces to the uploaded PDF downstream handoff runtime proof:

- `README.md`
- `docs/GOAL.md`
- `docs/runbook.md`
- `docs/application/portfolio-index.md`
- `docs/application/braincrew-role-map.md`
- `docs/review/application-ready-review.md`
- `docs/review/external-reader-proof-path.md`

## Allowed Claim

NoiseProof has local Docker DB plus FastAPI HTTP evidence that uploaded digital PDF bytes can flow through PyMuPDF extraction into upload chunk preview, explicit upload-to-chunks persistence, listed chunk lookup, and upload retrieval preview.

## Boundaries

This is not hosted deployment evidence.

It is not external reviewer feedback, not customer validation, not Braincrew acceptance, not robust PDF extraction, not OCR, not table extraction, not layout fidelity, not raw uploaded byte storage, not full parsed text persistence, not embeddings, not semantic retrieval quality evidence, not Evidence Ledger generation, not Noise Gate behavior, not report generation, not LLM output, not automatic failure-case creation, and not product-complete.

External reviewer feedback v0 remains open.

## Next Product Candidate

The next reviewer-facing gate can refresh external review request surfaces:

```text
external reviewer PDF downstream handoff request refresh v0
```
