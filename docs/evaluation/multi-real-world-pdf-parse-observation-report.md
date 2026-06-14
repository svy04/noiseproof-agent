# Multi Real-world PDF Parse Observation Matrix

Phase marker: multi_real_world_pdf_parse_observation_matrix_v0.

This report records PyMuPDF digital-text observations for multiple real-world BEA PDFs.

It is not robust PDF extraction evidence.

## Aggregate

| Metric | Value |
|---|---:|
| observed_fixture_count | 3 |
| parsed_fixture_count | 3 |
| total_page_count | 95 |
| total_extracted_page_count | 95 |
| total_empty_page_count | 0 |
| total_text_char_count | 217555 |
| total_text_block_count | 1594 |
| total_image_block_count | 887 |
| total_table_candidate_count | 43 |
| table_extraction_performed | false |
| ocr_calls_attempted | false |
| binary_files_committed | false |
| download_cache_committed | false |
| raw_extracted_text_committed | false |
| can_claim_multi_real_world_pdf_parse_observation | true |
| can_claim_robust_pdf_extraction | false |

## Fixtures

| Fixture | Pages | Text chars | Text blocks | Image blocks | Table candidates | SHA-256 |
|---|---:|---:|---:|---:|---:|---|
| bea_nipa_glossary_2019 | 35 | 92219 | 420 | 1 | 35 | 991c6335ffb794cf8f7731a4bff770b810f63693d44af23f0edc8ffecab89cb6 |
| bea_nipa_chapter_04_2024 | 30 | 65113 | 355 | 1 | 8 | 59b198518591d8e3651fc3a9b9576dec304429668d737be53688dd50ddf5aada |
| bea_open_source_software_innovation_wp_2022_10 | 30 | 60223 | 819 | 885 | 0 | c95fe4445f42271d90b233944078fcbba76c75dab93ed678e8c08f721797ad83 |

## Warnings

- PyMuPDF digital-text extraction was observed for three BEA PDFs only.
- PyMuPDF text order may not equal natural reading order; layout fidelity is not claimed.
- Table candidates are diagnostics only; table extraction was not performed.
- OCR was not attempted.
- No external PDF binaries, download caches, or raw extracted text are committed.

## Next Gate

- multi_real_world_pdf_parse_observation_matrix_remote_verification_v0

## Boundary Notes

- multiple real-world PDF parse observations
- owner-runtime observation only
- no external PDF binaries committed
- no download cache committed
- no raw extracted text committed
- not robust PDF extraction evidence
- not arbitrary market PDF parsing evidence
- not OCR evidence
- not table extraction evidence
- not layout fidelity evidence
- not hosted deployment evidence
- not external reviewer feedback
- not product-complete

## Boundary

This is a multi-fixture real-world PDF parse observation matrix only.

It records sanitized metadata, byte hashes, and PyMuPDF digital-text diagnostics for three BEA PDFs.

It does not commit external PDF binaries, download caches, or raw extracted text.

It does not prove table extraction, OCR, layout fidelity, arbitrary market PDF reliability, or robust PDF extraction.

This is not hosted deployment evidence.

This is not product-complete.
