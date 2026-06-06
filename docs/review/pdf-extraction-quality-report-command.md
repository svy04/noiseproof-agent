# PDF Extraction Quality Report Command

Phase marker: PDF extraction quality report command v0.

Status: implemented.

Purpose: make `docs/evaluation/pdf-extraction-quality-report.md` reproducible and stale-checkable from the committed fixture manifest and observations.

Implemented artifacts:

```text
apps/api/app/services/pdf_extraction_quality_report_command.py
.github/workflows/ci.yml
apps/api/tests/test_pdf_extraction_quality.py
apps/api/tests/test_docs.py
```

Command behavior:

```text
pdf_extraction_quality_report_current
pdf_extraction_quality_report_stale
pdf_extraction_quality_report_regeneration_failed
```

CI now runs:

```text
Check PDF extraction quality report staleness
python -m app.services.pdf_extraction_quality_report_command
```

The command checks byte-for-byte regeneration and exits `3` if the committed report is stale. Failure output preserves `not robust PDF extraction evidence`.

## Boundary

This is not robust PDF extraction implementation.

This is not OCR implementation.

This is not table extraction implementation.

This is not hosted deployment evidence.

This is not product-complete.

Next recommended gate: a PyMuPDF digital-text observation smoke that feeds actual parser output into this evaluator, still without robust extraction claims.
