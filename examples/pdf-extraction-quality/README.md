# PDF Extraction Quality Fixtures

This directory defines the fixture packet for future PDF extraction quality work.

Manifest: `examples/pdf-extraction-quality/fixture-manifest.json`.

Phase marker: PDF extraction quality fixture packet v0.

The packet is intentionally manifest-only. It does not include binary PDF files yet. Future binary fixtures must include provenance, redistribution boundaries, expected spans, expected warnings, and quality metrics before any robust PDF extraction claim changes.

Current boundary:

```text
robust_pdf_extraction_claimed: false
binary_pdf_fixtures_included: false
quality_gate_required_before_robust_claim: true
```

Use this packet to test future adapters for born-digital text, table-heavy reports, deterministic table-adapter rows, scanned/image PDFs, encrypted PDFs, image-heavy PDFs, multi-column layouts, and no-extractable-text cases.

The table-heavy fixture includes `expected_table_rows` and the evaluator reports `table_cell_recall`. This is a contract for future table extraction adapters only; it does not claim table extraction is implemented.

The `deterministic_table_adapter_pdf` fixture records the tiny PyMuPDF table adapter's local deterministic 2x2 output in `observations.json`. It is manifest/observation evidence for evaluator plumbing only, not binary fixture evidence, not default `PdfParser` table extraction, and not robust PDF extraction evidence.

`missing-runtime-observations.json` records a bounded observation pack for the four fixture roles that were missing in the Phase 870 matrix: scanned-image OCR boundary, image-heavy diagnostics boundary, multi-column layout boundary, and no-extractable-text failure boundary. It keeps `robust_pdf_extraction_claimed: false` and does not claim OCR, image/chart interpretation, layout fidelity, or robust PDF extraction.

`licensed-real-world-candidates.json` records a metadata-only candidate pack for future real-world PDF fixture downloads. It includes source URLs, license-source URLs, expected signals, and known risks, while keeping `download_status: candidate_metadata_only`, `binary_files_committed: false`, and `robust_pdf_extraction_claimed: false`. No external PDF binaries are committed in this gate.
