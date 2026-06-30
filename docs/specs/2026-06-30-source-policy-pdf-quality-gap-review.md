# Source-policy PDF Quality Gap Review Spec

Status: draft for implementation.

Phase marker: `source_policy_pdf_quality_gap_review_v0`.

Previous gate: `source_policy_pdf_parse_quality_matrix_v0`.

Recommended next gate after this spec:
`source_policy_no_native_text_failure_route_v0`.

## Purpose

Review the six blocker cells from the source-policy PDF parse quality matrix and
select the smallest inspectable next gate.

This gate does not add runtime evidence. It does not download, parse, OCR,
extract tables, compare rendered pages, or inspect images. It is a decision
review over the existing quality matrix.

## Source-first Basis

This gate uses existing source cards:

- Model Cards: keep capability, caveat, and limitation visible in the same
  artifact.
- Datasheets for Datasets: keep source policy, collection route, omissions, and
  recommended use visible before fixture evidence is used.
- Docling and Unstructured: treat PDF parsing as separable stages and avoid one
  undifferentiated "PDF works" claim.
- PyMuPDF OCR: keep OCR explicit and dependency-aware; do not silently upgrade
  no-native-text into OCR quality evidence.
- OCR-D evaluation: OCR quality must be measured, not implied by a parser
  failure or a single OCR path.

## Input

```text
examples/pdf-extraction-quality/source-policy-pdf-parse-quality-matrix.json
```

## Outputs

```text
examples/pdf-extraction-quality/source-policy-pdf-quality-gap-review.json
docs/evaluation/source-policy-pdf-quality-gap-review-report.md
docs/review/source-policy-pdf-quality-gap-review.md
packages/ingestion/pdf_quality/source_policy_pdf_quality_gap_review.py
apps/api/app/services/source_policy_pdf_quality_gap_review_command.py
apps/api/tests/test_source_policy_pdf_quality_gap_review.py
```

## Decision Rule

Rank the six blocker cells by:

1. Can the next gate be inspectable without new PDF downloads?
2. Can the next gate preserve a real observed failure without claiming quality?
3. Does the next gate reduce a robust-PDF blocker while staying small?
4. Does the next gate avoid external reviewer dependency?
5. Does the next gate avoid source-access blockers?

The selected next gate is:

```text
source_policy_no_native_text_failure_route_v0
```

Why:

```text
The NARA no-native-text cell already has source-policy-reviewed observation
metadata and a structured failure_case_candidate. A next gate can preserve that
failure route without downloading PDFs, running OCR, or claiming OCR quality.
```

## Boundaries

Do not:

- download PDFs
- commit external PDF binaries
- commit raw text
- run OCR
- claim OCR quality
- extract tables
- compare rendered pages
- interpret images or charts
- call LLMs
- add retrieval
- generate Evidence Ledger entries
- run Noise Gate
- build a dashboard

## Acceptance

- The review contains exactly six reviewed gap cells.
- `selected_next_gate` is `source_policy_no_native_text_failure_route_v0`.
- The NARA no-native-text cell is selected because it is a real observed
  failure route that can be preserved without new downloads or OCR.
- All stronger quality claims remain blocked.
- The report regenerates byte-for-byte through a CLI `--check` command.
- README, GOAL, MASTER-SPEC, runbook, portfolio index, external-reader proof
  path, proof-gap action surface, proof-gap registry, and CI reference the gate.
