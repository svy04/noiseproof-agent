# Committed OCR Layout Image Binary Fixture Provenance

Status: implemented.

Phase marker: `committed_ocr_layout_image_binary_fixture_provenance_v0`.

This gate commits synthetic binary PDF fixtures for the OCR, image-heavy,
multi-column layout, and no-extractable-text roles that were previously covered
only by adapter-runtime observation metadata.

Artifacts:

- `examples/pdf-extraction-quality/binary-fixtures/ocr-layout-image-provenance.json`
- `examples/pdf-extraction-quality/binary-fixtures/scanned-image.pdf`
- `examples/pdf-extraction-quality/binary-fixtures/image-heavy.pdf`
- `examples/pdf-extraction-quality/binary-fixtures/multi-column-layout.pdf`
- `examples/pdf-extraction-quality/binary-fixtures/no-extractable-text.pdf`
- `examples/pdf-extraction-quality/binary-fixtures/generate_ocr_layout_image_fixtures.py`
- `packages/ingestion/pdf_quality/ocr_layout_image_binary_fixture.py`
- `apps/api/app/services/committed_ocr_layout_image_binary_fixture_provenance_command.py`
- `docs/evaluation/committed-ocr-layout-image-binary-fixture-provenance-report.md`

Report markers:

```text
committed_fixture_count -> 4
parser_observed_fixture_count -> 4
robust_pdf_extraction_claimed -> false
can_claim_robust_pdf_extraction -> false
claim_boundary -> committed_ocr_layout_image_binary_fixture_provenance_only_not_robust_pdf_extraction
```

The committed fixtures are synthetic and redistributable inside the repository.
The provenance packet pins SHA-256 and byte size for each PDF so fixture drift is
visible in tests and CI.

Boundary:

- committed synthetic binary fixture provenance only
- not robust PDF extraction evidence
- not OCR evidence
- not image/chart interpretation evidence
- not layout fidelity evidence
- not hosted deployment evidence
- not external reviewer feedback
- not customer validation
- not Braincrew acceptance
- not product-complete

Next gate: `opt_in_ocr_adapter_runtime_smoke_v0`, only if an OCR adapter is
explicitly introduced and tested without claiming broad PDF extraction.
