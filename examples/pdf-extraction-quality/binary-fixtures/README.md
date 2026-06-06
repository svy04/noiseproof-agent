# PDF Binary Fixtures

Phase marker: PDF binary fixture provenance packet v0.

This directory contains synthetic PDF fixtures generated for local NoiseProof quality checks.

Files:

- `born-digital-text.pdf`
- `deterministic-table-adapter.pdf`
- `generate_synthetic_fixtures.py`
- `provenance.json`

The provenance packet records each fixture's source kind, generator, redistribution boundary, SHA-256 hash, file size, expected spans, expected table rows, and no-robust-extraction boundary.

Boundary:

```text
synthetic binary fixture provenance only
not external data redistribution
not default PdfParser table extraction
not robust PDF extraction evidence
not OCR evidence
not product-complete
```
