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

Use this packet to test future adapters for born-digital text, table-heavy reports, scanned/image PDFs, encrypted PDFs, image-heavy PDFs, multi-column layouts, and no-extractable-text cases.
