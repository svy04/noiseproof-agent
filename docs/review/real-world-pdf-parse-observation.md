# Real-world PDF Parse Observation

Phase 889 adds real-world PDF parse observation v0.

This is a bounded owner-runtime observation over the already hashed BEA fixture
`bea_nipa_glossary_2019`.

It records PyMuPDF digital-text parser metadata only.

It does not commit external PDF binaries, download caches, or raw extracted text.

## Evidence

- observation: `examples/pdf-extraction-quality/real-world-pdf-parse-observation.json`
- report: `docs/evaluation/real-world-pdf-parse-observation-report.md`
- command: `app.services.real_world_pdf_parse_observation_command`
- test: `apps/api/tests/test_real_world_pdf_parse_observation.py`

## Observed Counts

- page_count -> 35
- extracted_page_count -> 35
- empty_page_count -> 0
- text_char_count -> 92219
- text_block_count -> 420
- image_block_count -> 1
- table_candidate_count -> 35
- table_extraction_performed -> false
- ocr_calls_attempted -> false
- binary_files_committed -> false
- download_cache_committed -> false
- can_claim_robust_pdf_extraction -> false

## Boundary

This is a single real-world PDF parse observation only.

This is not robust PDF extraction evidence.

This is not arbitrary market PDF parsing evidence.

This is not OCR, table extraction, layout fidelity, hosted deployment, external
reviewer feedback, customer validation, Braincrew acceptance, or product-complete
evidence.

Next gate: `multi_real_world_pdf_parse_observation_matrix_v0`.
