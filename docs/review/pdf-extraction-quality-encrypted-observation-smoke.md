# PDF Extraction Quality Encrypted Observation Smoke

Phase marker: PDF extraction quality encrypted observation smoke v0.

Status: implemented.

Purpose: prove that encrypted PDF authorization boundaries survive the parser-to-observation-to-evaluator path without attempting decryption.

Implemented code:

```text
packages/ingestion/pdf_quality/observation.py
packages/ingestion/parsers/pdf.py
apps/api/tests/test_pdf_extraction_quality.py
```

Observed smoke markers:

```text
parser -> pdf-pymupdf
encrypted -> true
password_required -> true
failure_case_candidate -> pdf_encrypted_requires_password
failure_case_candidate_correctness -> 1
robust_pdf_extraction -> false
not decryption evidence
not robust PDF extraction evidence
```

The smoke uses a locally generated password-protected PDF. The parser returns the structured `pdf_encrypted_requires_password` failure candidate, and the observation adapter preserves `encrypted` and `password_required` metadata for evaluation. No password is supplied and no decryption is attempted.

## Boundary

This is not decryption evidence.

This is not robust PDF extraction evidence.

This is not robust PDF extraction implementation.

This is not OCR implementation.

This is not table extraction implementation.

This is not hosted deployment evidence.

This is not product-complete.

Next recommended gate: add a compact PDF observation smoke index that summarizes digital text, table candidate, no-text, and encrypted observation boundaries for external reviewers.
