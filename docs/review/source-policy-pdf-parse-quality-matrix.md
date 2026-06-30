# Source-policy PDF Parse Quality Matrix

Phase marker: `source_policy_pdf_parse_quality_matrix_v0`.

Previous gate: `source_policy_pdf_parse_observation_v0`.

Next gate: `source_policy_pdf_quality_gap_review_v0`.

## Purpose

This gate turns the source-policy PDF parse observation packet into a small
quality-claim blocker matrix.

It does not add new runtime evidence. It does not improve parsing. It makes the
current evidence easier to inspect before stronger parser wording is allowed.

## Borrowed Source-first Patterns

- Model Cards: capability, caveat, and boundary stay visible together.
- Datasheets for Datasets: source policy, collection route, omissions, and
  recommended use stay visible.
- RAGAS and ALCE: keep quality surfaces separate instead of treating one smooth
  artifact as proof.
- Docling and Unstructured source cards: PDF parsing has separate layout,
  table, OCR, visual, and image/chart boundaries.

## Result

```text
matrix_status -> passed
quality_status -> blocked
matrix_cell_count -> 6
observed_fixture_cell_count -> 3
native_text_observed_cell_count -> 2
no_native_text_failure_cell_count -> 1
blocked_download_cell_count -> 2
external_route_cell_count -> 1
quality_claim_ready_cell_count -> 0
quality_blocked_cell_count -> 6
can_claim_source_policy_pdf_parse_quality_matrix -> true
can_claim_robust_pdf_extraction -> false
can_claim_rendered_visual_fidelity -> false
can_claim_labeled_layout_ground_truth -> false
can_claim_reading_order -> false
can_claim_image_chart_interpretation -> false
can_claim_ocr_quality -> false
can_claim_external_validation -> false
```

## Artifacts

```text
examples/pdf-extraction-quality/source-policy-pdf-parse-quality-matrix.json
docs/evaluation/source-policy-pdf-parse-quality-matrix-report.md
packages/ingestion/pdf_quality/source_policy_pdf_parse_quality_matrix.py
apps/api/app/services/source_policy_pdf_parse_quality_matrix_command.py
apps/api/tests/test_source_policy_pdf_parse_quality_matrix.py
```

## Boundary

This is a deterministic quality-claim blocker matrix over the existing
source-policy PDF parse observation packet.

It does not download PDFs, parse PDFs, run OCR, extract tables, compare rendered
pages, interpret images or charts, call LLMs, chunk, retrieve, generate Evidence
Ledger entries, run Noise Gate, or build a dashboard.

It is not robust PDF extraction evidence.

It is not arbitrary-market PDF parsing evidence.

It is not OCR quality evidence.

It is not table extraction benchmark evidence.

It is not layout fidelity evidence.

It is not rendered visual fidelity evidence.

It is not image/chart interpretation evidence.

It is not hosted deployment evidence.

It is not external reviewer feedback.

It is not product-complete.
