# Multi-publisher Modality-stratified PDF Eval

## What Changed

This gate adds `multi_publisher_modality_stratified_pdf_eval_v0`.

It turns the robust-PDF generalization gap review into a deterministic
publisher/modality/failure-class matrix.

Generated report:

```text
docs/evaluation/multi-publisher-modality-stratified-pdf-eval-report.md
```

Sanitized matrix packet:

```text
examples/pdf-extraction-quality/multi-publisher-modality-stratified-pdf-eval.json
```

## Gate Result

```text
matrix_status -> passed
coverage_status -> partial
robust_pdf_eval_status -> blocked
publisher_stratum_count -> 3
modality_stratum_count -> 9
matrix_cell_count -> 12
covered_limited_cell_count -> 6
missing_cell_count -> 6
can_claim_robust_pdf_extraction -> false
recommended_next_gate -> targeted_real_world_pdf_fixture_expansion_v0
```

## Covered Limited Cells

```text
bea_digital_text_parse
eia_digital_text_parse
bea_table_extraction
eia_table_extraction
nara_ocr_text
bea_layout_metadata
```

## Missing Cells

```text
multi_publisher_reading_order
multi_publisher_rendered_visual_fidelity
multi_publisher_labeled_layout_ground_truth
multi_publisher_image_chart_interpretation
multi_publisher_no_extractable_text_failure
external_reviewer_validation
```

## Boundary

This is not robust PDF extraction evidence.

This is not arbitrary-market PDF parsing evidence.

This is not table extraction benchmark evidence.

This is not OCR quality benchmark evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.

This gate does not add new runtime evidence. It does not download PDFs, parse
PDFs, run OCR, extract tables, call LLMs, commit external PDF binaries, commit
download caches, commit raw extracted text, commit screenshots, or commit page
images.

## Next Gate

```text
targeted_real_world_pdf_fixture_expansion_v0
```

The next gate should add a source-policy-reviewed candidate plan for the
missing cells before any new owner-runtime downloads or parser calls.
