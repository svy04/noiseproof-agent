# Real-world Table Extraction Evidence Gate

Phase marker: real_world_table_extraction_evidence_gate_v0.

This report records sanitized PyMuPDF table extraction observations for temporary owner-runtime real-world PDF downloads.

It is real-world table extraction evidence, not robust PDF extraction evidence.

## Gate Result

table_extraction_gate_status -> passed
previous_gate -> cross_publisher_real_world_pdf_fixture_gate_v0
observed_fixture_count -> 3
table_extraction_observed_fixture_count -> 3
distinct_publisher_count -> 2
total_page_count -> 125
total_table_count -> 124
total_table_rows_extracted -> 847
total_table_cell_count -> 7902
has_cross_publisher_coverage -> true
has_table_extraction_evidence -> true
has_ocr_evidence -> false
has_layout_fidelity_evidence -> false
can_claim_real_world_table_extraction_evidence -> true
can_claim_robust_pdf_extraction -> false

## Publishers

- U.S. Bureau of Economic Analysis
- U.S. Energy Information Administration

## Fixtures

| Fixture | Publisher | Pages | Tables | Rows | Cells | SHA-256 |
|---|---|---:|---:|---:|---:|---|
| eia_steo_full_2026_06 | U.S. Energy Information Administration | 60 | 81 | 500 | 7012 | 21555ad32b90f7f0c8d49f87799b4956234c5505403a14102661cb247d32387f |
| bea_nipa_glossary_2019 | U.S. Bureau of Economic Analysis | 35 | 35 | 265 | 530 | 991c6335ffb794cf8f7731a4bff770b810f63693d44af23f0edc8ffecab89cb6 |
| bea_nipa_chapter_04_2024 | U.S. Bureau of Economic Analysis | 30 | 8 | 82 | 360 | 59b198518591d8e3651fc3a9b9576dec304429668d737be53688dd50ddf5aada |

## Passed Checks

- real_world_table_extraction_observed
- cross_publisher_coverage_visible
- source_policy_visible
- sha256_visible
- external_binaries_not_committed
- raw_extracted_text_not_committed
- raw_table_rows_not_committed

## Remaining Blocked Reasons

- ocr_evidence_missing
- layout_fidelity_evidence_missing

## Warnings

- PyMuPDF find_tables/Table.extract produced table row and shape counts for three temporary owner-runtime real-world PDF downloads.
- No PDF binaries, download caches, raw extracted text, or raw table rows are committed.
- This evidence records table extraction output only; OCR and layout fidelity remain missing.
- MuPDF emitted structure-tree format warnings for the EIA observation; layout fidelity is not claimed.

## Next Gate

- real_world_ocr_evidence_gate_v0

## Boundary Notes

- real-world table extraction evidence
- cross-publisher table extraction observation
- sanitized table metrics only
- no external PDF binaries committed
- no download cache committed
- no raw extracted text committed
- no raw table rows committed
- not robust PDF extraction evidence
- not arbitrary-market PDF parsing evidence
- not OCR evidence
- not layout fidelity evidence
- not hosted deployment evidence
- not external reviewer feedback
- not product-complete

## Boundary

This is a deterministic report over sanitized owner-runtime table observations.

It does not commit external PDF binaries, download caches, raw extracted text, or raw table rows.

It does not run OCR, prove layout fidelity, prove arbitrary-market PDF parsing reliability, or prove robust PDF extraction.

This is not hosted deployment evidence.

This is not external reviewer feedback.

This is not product-complete.
