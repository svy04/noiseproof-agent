# Source-policy No-native-text Failure Route Spec

Status: draft for implementation.

Phase marker: `source_policy_no_native_text_failure_route_v0`.

Previous gate: `source_policy_pdf_quality_gap_review_v0`.

Recommended next gate after this spec:
`source_policy_no_native_text_ocr_readiness_review_v0`.

## Purpose

Preserve the NARA no-native-text observation as an explicit source-policy
failure route before any OCR work starts.

This gate does not run OCR. It does not improve parsing. It turns the existing
source-policy parse observation and quality gap review into an inspectable
failure-route packet.

## Source-first Basis

This gate uses existing source cards:

- Model Cards: disclose limitations next to capability claims.
- Datasheets for Datasets: keep source policy, collection route, and omissions
  visible before using a fixture as evidence.
- PyMuPDF OCR: OCR is an explicit Tesseract-backed path, not an implicit rescue
  path for no-native-text PDFs.
- OCR-D evaluation: OCR quality requires measurable evaluation and cannot be
  inferred from a no-text failure candidate.
- Source-policy PDF Quality Gap Review: selected this route as the smallest
  inspectable next gate because it preserves an already observed failure without
  new downloads or OCR calls.

## Inputs

```text
examples/pdf-extraction-quality/source-policy-pdf-parse-observations.json
examples/pdf-extraction-quality/source-policy-pdf-parse-quality-matrix.json
examples/pdf-extraction-quality/source-policy-pdf-quality-gap-review.json
```

## Outputs

```text
examples/pdf-extraction-quality/source-policy-no-native-text-failure-route.json
docs/evaluation/source-policy-no-native-text-failure-route-report.md
docs/review/source-policy-no-native-text-failure-route.md
packages/ingestion/pdf_quality/source_policy_no_native_text_failure_route.py
apps/api/app/services/source_policy_no_native_text_failure_route_command.py
apps/api/tests/test_source_policy_no_native_text_failure_route.py
```

## Required Route Fields

- `route_status`
- `selected_failure_route`
- `fixture_id`
- `publisher`
- `source_url`
- `policy_source_url`
- `failure_type`
- `root_cause`
- `fix_status`
- `page_count`
- `empty_page_count`
- `text_char_count`
- `ocr_calls_performed`
- `parser_calls_performed`
- `can_claim_source_policy_no_native_text_failure_route`
- `can_claim_ocr_quality`
- `can_claim_robust_pdf_extraction`

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

- Exactly one failure route is preserved.
- The route is the NARA `no_native_text_observed` candidate.
- The route keeps `page_count -> 4`, `empty_page_count -> 4`, and
  `text_char_count -> 0` visible.
- OCR remains not performed and OCR quality remains unclaimed.
- The report regenerates byte-for-byte through a CLI `--check` command.
- README, GOAL, MASTER-SPEC, runbook, portfolio index, external-reader proof
  path, proof-gap action surface, proof-gap registry, and CI reference the gate.
