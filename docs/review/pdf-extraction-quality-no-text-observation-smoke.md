# PDF Extraction Quality No-text Observation Smoke

Phase marker: PDF extraction quality no-text observation smoke v0.

Status: implemented.

Purpose: prove that a PDF which opens but yields no extractable digital text preserves its failure-case candidate when converted into a PDF quality observation.

Implemented code:

```text
packages/ingestion/pdf_quality/observation.py
packages/ingestion/parsers/pdf.py
apps/api/tests/test_pdf_extraction_quality.py
```

Observed smoke markers:

```text
parser -> pdf-pymupdf
failure_case_candidate -> pdf_no_extractable_text
failure_case_candidate_correctness -> 1
robust_pdf_extraction -> false
not robust PDF extraction evidence
```

The smoke uses a minimal local PDF that opens but has no embedded digital text. The parser emits `pdf_no_extractable_text`; the observation adapter carries the failure type, description, and next action; the evaluator scores the expected failure candidate without treating the result as extraction quality evidence.

## Boundary

This is not robust PDF extraction implementation.

This is not OCR implementation.

This is not table extraction implementation.

This is not hosted deployment evidence.

This is not product-complete.

Next recommended gate: encrypted PDF observation smoke, or a committed no-text observation report that keeps failure candidates inspectable.
