# PDF Extraction Quality Observation Smoke Index

Phase marker: PDF extraction quality observation smoke index v0.

Status: implemented.

Purpose: give external reviewers one compact map for the current PDF observation smokes before any robust PDF extraction claim changes.

Indexed observation smokes:

| Smoke | Proof surface | What it shows | Boundary |
| --- | --- | --- | --- |
| Digital text | `docs/review/pdf-extraction-quality-digital-text-observation-smoke.md` | `digital_pdf_text_extraction -> true`; `robust_pdf_extraction -> false` | Local PyMuPDF digital-text parser smoke only |
| Table candidate | `docs/review/pdf-extraction-quality-table-candidate-observation-smoke.md` | `table_candidate_count -> positive`; `table_extraction_performed -> false` | Candidate diagnostics only; no table rows extracted |
| No text | `docs/review/pdf-extraction-quality-no-text-observation-smoke.md` | `failure_case_candidate -> pdf_no_extractable_text`; `failure_case_candidate_correctness -> 1` | Expected failure candidate only; no OCR claim |
| Encrypted | `docs/review/pdf-extraction-quality-encrypted-observation-smoke.md` | `failure_case_candidate -> pdf_encrypted_requires_password`; `password_required -> true` | Authorization boundary only; no decryption attempted |

Common observation path:

```text
PdfParser
-> ParseResult
-> packages/ingestion/pdf_quality/observation.py
-> PDF extraction quality evaluator
-> local smoke assertion
```

Common preserved markers:

```text
parser -> pdf-pymupdf
robust_pdf_extraction -> false
table_extraction_performed -> false
table_rows_extracted -> 0
```

This index is useful because it separates four different PDF realities that should not be collapsed into one claim:

- readable born-digital text
- table-like layout that is only detected as a candidate
- PDFs that open but yield no extractable digital text
- PDFs that require a password

## Boundary

This is not new runtime evidence.

This is not decryption evidence.

This is not robust PDF extraction evidence.

This is not robust PDF extraction implementation.

This is not OCR implementation.

This is not table extraction implementation.

This is not hosted deployment evidence.

This is not product-complete.

Next recommended gate: either add a committed observation report that groups these four local smokes, or move back to the broader external-review proof route only if reviewer navigation needs another refresh.
