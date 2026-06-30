# Source-policy PDF Parse Quality Matrix Spec

Status: draft for implementation.

Phase marker: `source_policy_pdf_parse_quality_matrix_v0`.

Previous gate: `source_policy_pdf_parse_observation_v0`.

Recommended next gate after this spec: `source_policy_pdf_quality_gap_review_v0`.

## Purpose

Turn the source-policy PDF parse observation packet into a small quality-claim
matrix before any stronger parser wording is allowed.

This gate does not improve parsing. It makes the current parser evidence easier
to inspect by showing which missing evidence roles are still blocked after the
PyMuPDF parse-observation gate.

## Source-first Basis

This gate follows the master-spec source assimilation rule:

- Model Cards: keep capability, intended use, metrics, caveats, and boundaries
  visible together.
- Datasheets for Datasets: keep source policy, collection method, omissions,
  and recommended use visible before using fixtures as evidence.
- RAGAS and ALCE: keep quality surfaces separate; citation or parse metadata is
  not truth.
- Docling and Unstructured source cards: treat PDF parsing as a pipeline with
  layout/table/OCR/image boundaries, not as one generic text-extraction claim.

The local adaptation is a deterministic matrix over the existing sanitized
source-policy parse observation packet.

## Inputs

- `examples/pdf-extraction-quality/source-policy-pdf-parse-observations.json`

## Outputs

- `examples/pdf-extraction-quality/source-policy-pdf-parse-quality-matrix.json`
- `docs/evaluation/source-policy-pdf-parse-quality-matrix-report.md`
- `docs/review/source-policy-pdf-parse-quality-matrix.md`
- `packages/ingestion/pdf_quality/source_policy_pdf_parse_quality_matrix.py`
- `apps/api/app/services/source_policy_pdf_parse_quality_matrix_command.py`

## Matrix Cells

The matrix must preserve these six evidence roles:

1. `multi_publisher_rendered_visual_fidelity`
2. `multi_publisher_labeled_layout_ground_truth`
3. `multi_publisher_no_extractable_text_failure`
4. `multi_publisher_reading_order`
5. `multi_publisher_image_chart_interpretation`
6. `external_reviewer_validation`

## Required Summary Fields

- `phase_marker`
- `previous_gate`
- `quality_status`
- `matrix_status`
- `matrix_cell_count`
- `observed_fixture_cell_count`
- `native_text_observed_cell_count`
- `no_native_text_failure_cell_count`
- `blocked_download_cell_count`
- `external_route_cell_count`
- `quality_claim_ready_cell_count`
- `quality_blocked_cell_count`
- `can_claim_source_policy_pdf_parse_quality_matrix`
- `can_claim_robust_pdf_extraction`
- `can_claim_rendered_visual_fidelity`
- `can_claim_labeled_layout_ground_truth`
- `can_claim_reading_order`
- `can_claim_image_chart_interpretation`
- `can_claim_ocr_quality`
- `can_claim_external_validation`
- `next_gate`

## Boundaries

Do not:

- download PDFs
- commit external PDF binaries
- commit raw text
- run OCR
- extract tables
- compare rendered pages
- interpret images or charts
- call LLMs
- add retrieval
- generate Evidence Ledger entries
- run Noise Gate
- build a dashboard

This gate can claim only that a source-policy parse quality matrix exists.

It cannot claim robust PDF extraction, arbitrary-market PDF parsing reliability,
OCR quality, table extraction benchmark quality, layout fidelity, rendered
visual fidelity, image/chart interpretation, external validation, hosted
deployment, or product completeness.

## Acceptance

- The matrix contains exactly six cells.
- Every source-policy parse-observation route is preserved as a matrix cell.
- Every stronger quality claim remains blocked.
- The report regenerates byte-for-byte through a CLI `--check` command.
- README, GOAL, MASTER-SPEC, runbook, portfolio index, external-reader proof
  path, proof-gap action surface, proof-gap registry, and CI reference the gate.
