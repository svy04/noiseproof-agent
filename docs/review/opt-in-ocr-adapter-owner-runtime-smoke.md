# Opt-in OCR Adapter Owner-runtime Smoke

Status: implemented.

Purpose: record an owner-runtime PyMuPDF OCR smoke over one committed synthetic
image-only PDF fixture after Tesseract/tessdata was provided locally.

This closes the previously pending owner-runtime OCR smoke input for the
single committed fixture. It does not close robust PDF extraction.

Verified artifact:

- `examples/pdf-extraction-quality/ocr-runtime-fixtures/ocr-smoke-text-image.pdf`
- `examples/pdf-extraction-quality/ocr-runtime-fixtures/ocr-runtime-provenance.json`
- `packages/ingestion/pdf_quality/opt_in_ocr_adapter_runtime_smoke.py`
- `apps/api/app/services/opt_in_ocr_adapter_runtime_smoke_command.py`

Owner-runtime smoke markers:

```text
phase_marker -> opt_in_ocr_adapter_runtime_smoke_v0
run_source -> owner_runtime_pymupdf_ocr_smoke
run_status -> report_written
fixture_id -> ocr_smoke_text_image_pdf
fixture_sha256 -> f961080dcf4163f554e3c8e3f55825a49357b43010adceff78eea8591ddadc2c
fixture_size_bytes -> 2122181
ocr_engine -> pymupdf_get_textpage_ocr
language -> eng
page_count -> 1
ocr_page_count -> 1
ocr_performed -> true
ocr_calls_attempted -> true
recognized_text -> ocr smoke text
expected_spans_found -> true
robust_pdf_extraction_claimed -> false
can_claim_robust_pdf_extraction -> false
tessdata_path_printed -> false
tessdata_path_committed_to_repo -> false
```

Validator markers:

```text
phase_marker -> opt-in OCR adapter owner-runtime smoke validator v0
validation_status -> accepted
accepted_owner_runtime_smoke -> true
missing_or_failed_checks -> []
report_path_allowed -> true
validator_performs_ocr -> false
tessdata_path_printed -> false
tessdata_path_committed_to_repo -> false
```

Source basis:

- PyMuPDF `Page.get_textpage_ocr()` invokes Tesseract-OCR and accepts a
  caller-provided tessdata folder.
- The fixture is synthetic, committed, and image-only so the OCR claim is
  deliberately narrow and inspectable.

Boundaries:

- owner-runtime OCR smoke over one synthetic fixture only
- not robust PDF extraction evidence
- not arbitrary market PDF OCR evidence
- not image/chart interpretation evidence
- not layout fidelity evidence
- not hosted deployment evidence
- not external reviewer feedback
- not customer validation
- not Braincrew acceptance
- not product-complete
