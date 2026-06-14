# Real-world PDF Parse Observation

Phase marker: real_world_pdf_parse_observation_without_robust_claim_v0.

This report records one owner-runtime PyMuPDF digital-text parse observation for a real-world BEA PDF.

It is not robust PDF extraction evidence.

## Aggregate

| Metric | Value |
|---|---:|
| observed_fixture_count | 1 |
| parsed_fixture_count | 1 |
| page_count | 35 |
| extracted_page_count | 35 |
| empty_page_count | 0 |
| text_char_count | 92219 |
| text_block_count | 420 |
| image_block_count | 1 |
| table_candidate_count | 35 |
| table_extraction_performed | false |
| ocr_calls_attempted | false |
| binary_files_committed | false |
| download_cache_committed | false |
| can_claim_real_world_pdf_parse_observation | true |
| can_claim_robust_pdf_extraction | false |

## Fixture

- fixture_id: `bea_nipa_glossary_2019`
- publisher: U.S. Bureau of Economic Analysis
- parser: `pdf-pymupdf`
- source download/hash gate: `owner_approved_real_world_pdf_download_and_hash_v0`

## Warnings

- PDF text extraction uses PyMuPDF for digital text only; OCR, table extraction, and layout fidelity are not claimed.
- PyMuPDF table candidate diagnostics found potential tables but does not extract table contents.
- PyMuPDF table extraction adapter output only; robust PDF extraction is not claimed.

## Next Gate

- multi_real_world_pdf_parse_observation_matrix_v0

## Boundary Notes

- single real-world PDF parse observation only
- owner-runtime observation only
- no external PDF binaries committed
- no download cache committed
- not robust PDF extraction evidence
- not arbitrary market PDF parsing evidence
- not OCR evidence
- not table extraction evidence
- not layout fidelity evidence
- not hosted deployment evidence
- not external reviewer feedback
- not product-complete

## Boundary

This is a single real-world PDF parse observation only.

It records PyMuPDF digital-text parser metadata for one BEA PDF.

It does not prove table extraction, OCR, layout fidelity, arbitrary market PDF reliability, or robust PDF extraction.

This is not hosted deployment evidence.

This is not product-complete.
