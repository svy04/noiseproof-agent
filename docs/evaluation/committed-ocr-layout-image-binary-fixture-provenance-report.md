# Committed OCR Layout Image Binary Fixture Provenance

Phase marker: committed_ocr_layout_image_binary_fixture_provenance_v0.

This report records committed synthetic binary PDF fixtures for OCR, image-heavy, layout, and empty-text roles.

It is not robust PDF extraction evidence.

## Aggregate

| Metric | Value |
|---|---:|
| committed_fixture_count | 4 |
| parser_observed_fixture_count | 4 |
| robust_pdf_extraction_claimed | false |
| can_claim_robust_pdf_extraction | false |

## Per-fixture Provenance

| Fixture | Path | Parser | Boundary | Failure candidate | Expected spans found |
|---|---|---|---|---|---:|
| scanned_image_pdf | scanned-image.pdf | pdf-pymupdf | ocr_adapter_not_implemented | pdf_no_extractable_text | true |
| image_heavy_pdf | image-heavy.pdf | pdf-pymupdf | image_diagnostics_only | none | true |
| multi_column_layout_pdf | multi-column-layout.pdf | pdf-pymupdf | layout_diagnostics_only | none | true |
| no_extractable_text_pdf | no-extractable-text.pdf | pdf-pymupdf | empty_text_failure_boundary | pdf_no_extractable_text | true |

## Next Evidence Needed

- explicit opt-in OCR adapter runtime smoke before scanned-image text coverage claims
- image/chart interpretation adapter evidence before image-heavy truth claims
- reading-order and layout diagnostics before layout fidelity claims
- real-world PDF fixture license and redistribution review before external PDF evidence

## Boundary Notes

- not robust PDF extraction evidence
- not OCR evidence
- not image/chart interpretation evidence
- not layout fidelity evidence
- not hosted deployment evidence
- not product-complete

## Boundary

This is committed synthetic binary fixture provenance only.

This is not robust PDF extraction implementation.

This is not OCR implementation.

This is not image/chart interpretation evidence.

This is not layout fidelity evidence.

This is not hosted deployment evidence.

This is not product-complete.
