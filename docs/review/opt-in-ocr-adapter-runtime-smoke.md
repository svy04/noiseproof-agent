# Opt-in OCR Adapter Runtime Smoke

Status: implemented.

Phase marker: `opt_in_ocr_adapter_runtime_smoke_v0`.

This gate adds an opt-in PyMuPDF OCR smoke harness for one committed synthetic
image-only PDF fixture. It follows the PyMuPDF documented OCR path:
`Page.get_textpage_ocr()` invokes Tesseract-OCR and accepts a `tessdata`
folder. The default CI path does not run OCR because no owner-provided tessdata
directory is configured.

Artifacts:

- `packages/ingestion/pdf_quality/opt_in_ocr_adapter_runtime_smoke.py`
- `apps/api/app/services/opt_in_ocr_adapter_runtime_smoke_command.py`
- `apps/api/tests/test_opt_in_ocr_adapter_runtime_smoke.py`
- `examples/pdf-extraction-quality/ocr-runtime-fixtures/ocr-runtime-provenance.json`
- `examples/pdf-extraction-quality/ocr-runtime-fixtures/ocr-smoke-text-image.pdf`
- `examples/pdf-extraction-quality/ocr-runtime-fixtures/generate_ocr_runtime_fixtures.py`

CI evidence:

```text
owner_runtime_input_status -> missing_tessdata_prefix
opt_in_enabled -> false
tessdata_prefix_present -> false
ocr_calls_attempted -> false
```

Owner-runtime path:

```powershell
cd apps/api
$env:NOISEPROOF_ENABLE_PYMUPDF_OCR='true'
$env:NOISEPROOF_TESSDATA_PREFIX='<local-tessdata-dir-outside-repo>'
$env:CI='false'
uv run python -m app.services.opt_in_ocr_adapter_runtime_smoke_command --run-owner-runtime-smoke --output <runtime-report-path-outside-repo>
uv run python -m app.services.opt_in_ocr_adapter_runtime_smoke_command --validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>
```

Boundaries:

- opt-in smoke harness and missing-input CI path only
- not OCR evidence until owner runtime succeeds
- not robust PDF extraction evidence
- not image/chart interpretation evidence
- not layout fidelity evidence
- not hosted deployment evidence
- not external reviewer feedback
- not customer validation
- not Braincrew acceptance
- not product-complete

Next gate: `owner_runtime_pymupdf_ocr_smoke_with_tessdata_v0`.
