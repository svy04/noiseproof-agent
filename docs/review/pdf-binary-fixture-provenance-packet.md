# PDF Binary Fixture Provenance Packet

Status: implemented.

Phase marker: PDF binary fixture provenance packet v0.

## Purpose

Add a small synthetic binary PDF fixture packet with explicit provenance, redistribution, hash, and claim-boundary metadata before any real-world binary PDF fixture is introduced.

This keeps the project moving from manifest-only PDF quality plumbing toward inspectable binary inputs, while preserving that robust PDF extraction is still not claimed.

## Implemented Artifacts

```text
examples/pdf-extraction-quality/binary-fixtures/provenance.json
examples/pdf-extraction-quality/binary-fixtures/README.md
examples/pdf-extraction-quality/binary-fixtures/generate_synthetic_fixtures.py
examples/pdf-extraction-quality/binary-fixtures/born-digital-text.pdf
examples/pdf-extraction-quality/binary-fixtures/deterministic-table-adapter.pdf
packages/ingestion/pdf_quality/binary_fixture.py
apps/api/tests/test_pdf_extraction_quality.py
apps/api/tests/test_docs.py
```

## Provenance Packet

```text
packet -> pdf_binary_fixture_provenance_packet_v0
claim_boundary -> synthetic_binary_fixture_provenance_only_not_robust_pdf_extraction
binary_pdf_fixtures_included -> true
robust_pdf_extraction_claimed -> false
```

## Fixtures

```text
binary_born_digital_text
path -> born-digital-text.pdf
source_kind -> synthetic_generated
redistribution_allowed -> true
sha256 -> 45a4b5b288a15a297690f2c002b82da45cdbae306bdfe579054bf4ceaf13530f
size_bytes -> 871

binary_deterministic_table_adapter
path -> deterministic-table-adapter.pdf
source_kind -> synthetic_generated
redistribution_allowed -> true
sha256 -> f083e1bb3f421f46723cfc4ad8a3b96c97f0624d0e33d1ee978136f01a509354
size_bytes -> 1872
expected_table_rows -> [[Segment, Growth], [Enterprise, 12%]]
```

## Validation

`packages/ingestion/pdf_quality/binary_fixture.py` loads the packet and validates:

- fixture ids are unique
- source kind is `synthetic_generated`
- redistribution is explicitly allowed
- robust PDF extraction is not claimed
- fixture paths stay inside the fixture directory
- each PDF file exists
- recorded SHA-256 and `size_bytes` match the committed binary file

## Boundary

This is synthetic binary fixture provenance only.

It is not robust PDF extraction evidence.
It is not robust PDF extraction implementation.
It is not OCR implementation.
It is not default PdfParser table extraction.
It is not table extraction evidence for arbitrary market PDFs.
It is not external data redistribution.
It is not hosted deployment evidence.
It is not external reviewer feedback.
It is not product-complete.

## Next Gate

Next gate: parser/adapter smoke over these binary fixtures, remote verification after push, external-reader route refresh if this packet should become reviewer-facing, or a future real-world binary fixture gate with explicit license and redistribution review.
