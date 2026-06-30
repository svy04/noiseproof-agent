# Robust PDF Generalization Gap Review

## What Changed

This gate adds `robust_pdf_extraction_generalization_gap_review_v0`.

It reviews the current real-world PDF evidence chain after the layout fidelity
metadata sanity gate and records why the evidence still cannot support robust
PDF extraction wording.

Generated report:

```text
docs/evaluation/robust-pdf-generalization-gap-review-report.md
```

Sanitized review packet:

```text
examples/pdf-extraction-quality/robust-pdf-generalization-gap-review.json
```

## Gate Result

```text
review_status -> passed
generalization_gap_status -> open
evidence_chain_count -> 5
covered_capability_count -> 5
missing_capability_count -> 6
can_claim_robust_pdf_extraction -> false
recommended_next_gate -> multi_publisher_modality_stratified_pdf_eval_v0
```

## What Is Covered In A Limited Way

```text
digital_text_parse_observation
cross_publisher_fixture_coverage
table_extraction_observation
ocr_observation
layout_metadata_sanity_observation
```

## What Remains Missing

```text
labeled_layout_ground_truth
natural_reading_order_benchmark
rendered_visual_fidelity_comparison
image_chart_interpretation_evidence
arbitrary_market_pdf_coverage
external_reviewer_validation
```

## Source Patterns Used

- PyMuPDF text extraction surfaces
- Docling document conversion pipeline
- Unstructured partitioning elements and metadata
- DocLayNet labeled layout ground truth
- PubLayNet document layout benchmark

## Boundary

This is not robust PDF extraction evidence.

This is not arbitrary-market PDF parsing evidence.

This is not natural reading order correctness evidence.

This is not rendered visual fidelity evidence.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.

This gate does not add new runtime evidence. It does not download PDFs, parse
PDFs, run OCR, extract tables, call LLMs, commit external PDF binaries, commit
download caches, or commit raw extracted text.

## Next Gate

```text
multi_publisher_modality_stratified_pdf_eval_v0
```

The next gate should turn the missing capabilities into a stratified evaluation
matrix before any robust-PDF claim is considered.
