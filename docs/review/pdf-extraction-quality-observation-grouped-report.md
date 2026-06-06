# PDF Extraction Quality Observation Grouped Report

Phase marker: PDF extraction quality observation grouped report v0.

Status: implemented.

Purpose: summarize the four local PDF observation smokes as one reviewer-facing report without creating new runtime evidence or changing any robust PDF extraction claim.

Source index:

```text
docs/review/pdf-extraction-quality-observation-smoke-index.md
```

Grouped observations:

| Observation id | Source smoke | Current marker | What remains unproven |
| --- | --- | --- | --- |
| `digital_text_observation` | `docs/review/pdf-extraction-quality-digital-text-observation-smoke.md` | `digital_pdf_text_extraction -> true`; `robust_pdf_extraction -> false` | Multi-column layout, OCR, table extraction, and robust PDF extraction |
| `table_candidate_observation` | `docs/review/pdf-extraction-quality-table-candidate-observation-smoke.md` | `table_candidate_count -> positive`; `table_extraction_performed -> false`; `table_rows_extracted -> 0` | Actual table row extraction and table semantics |
| `no_text_observation` | `docs/review/pdf-extraction-quality-no-text-observation-smoke.md` | `failure_case_candidate -> pdf_no_extractable_text`; `failure_case_candidate_correctness -> 1` | OCR recovery and image-heavy PDF extraction |
| `encrypted_observation` | `docs/review/pdf-extraction-quality-encrypted-observation-smoke.md` | `failure_case_candidate -> pdf_encrypted_requires_password`; `password_required -> true` | Password handling, authorization flow, and decryption |

Current grouped conclusion:

```text
grouped_report_only_not_new_runtime_evidence
parser -> pdf-pymupdf
digital_pdf_text_extraction -> true
table_candidate_count -> positive
table_extraction_performed -> false
failure_case_candidate -> pdf_no_extractable_text
failure_case_candidate -> pdf_encrypted_requires_password
robust_pdf_extraction -> false
```

Interpretation:

- The current parser can extract simple born-digital text in a local smoke.
- The current parser can surface table-like candidates, but does not extract table rows.
- The current parser can preserve a structured no-text failure candidate.
- The current parser can preserve encrypted/password-required failure metadata without attempting decryption.

## Boundary

This is not new runtime evidence.

This is not decryption evidence.

This is not robust PDF extraction evidence.

This is not robust PDF extraction implementation.

This is not OCR implementation.

This is not table extraction implementation.

This is not hosted deployment evidence.

This is not product-complete.

Next recommended gate: remote verification for this grouped report after push, or return to the broader source-first product gate queue.
