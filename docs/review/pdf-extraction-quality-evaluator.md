# PDF Extraction Quality Evaluator

Phase marker: PDF extraction quality evaluator v0.

Status: implemented.

Purpose: add a deterministic evaluator over the Phase 703 fixture manifest so future PDF extraction observations can be scored before any robust PDF extraction claim changes.

Implemented code:

```text
packages/ingestion/pdf_quality/fixture.py
packages/ingestion/pdf_quality/evaluator.py
examples/pdf-extraction-quality/fixture-manifest.json
apps/api/tests/test_pdf_extraction_quality.py
```

The evaluator compares caller-provided observations against the manifest. It does not open PDF files, run OCR, extract tables, or interpret layout. It only scores declared observations against expected spans, expected warnings, and expected failure-case candidates.

Output fields:

```text
manifest_metric_only_not_robust_pdf_extraction
observed_fixture_count
not_evaluated_fixture_count
expected_span_recall
warning_correctness
failure_case_candidate_correctness
```

The evaluator also reports:

```text
not robust PDF extraction evidence
not OCR evidence
not table extraction evidence
not hosted deployment evidence
```

## Boundary

This is not robust PDF extraction implementation.

This is not OCR implementation.

This is not table extraction implementation.

This is not hosted deployment evidence.

This is not product-complete.

Next recommended gate: generate a committed PDF extraction quality report from a small observation fixture, still without claiming robust extraction.
