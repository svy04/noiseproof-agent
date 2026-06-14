# Owner-approved Real-world PDF Download and Hash

Phase marker: owner_approved_real_world_pdf_download_and_hash_v0.

This report records owner-approved real-world PDF download/hash metadata.

No external PDF binaries or download caches are committed in this gate.

It is not robust PDF extraction evidence.

## Aggregate

| Metric | Value |
|---|---:|
| downloaded_fixture_count | 1 |
| blocked_fixture_count | 4 |
| binary_files_committed | false |
| download_cache_committed | false |
| parser_calls_attempted | false |
| ocr_calls_attempted | false |
| table_extraction_attempted | false |
| can_claim_real_world_pdf_download_hash | true |
| can_claim_robust_pdf_extraction | false |

## Downloaded and Hashed Fixtures

| Fixture | Publisher | HTTP | Content type | Bytes | SHA-256 |
|---|---|---:|---|---:|---|
| bea_nipa_glossary_2019 | U.S. Bureau of Economic Analysis | 200 | application/pdf | 315727 | 991c6335ffb794cf8f7731a4bff770b810f63693d44af23f0edc8ffecab89cb6 |

## Blocked Runtime Attempts

| Fixture | Publisher | HTTP | Download status | Boundary |
|---|---|---:|---|---|
| bls_employment_situation_2025_01 | U.S. Bureau of Labor Statistics | 403 | blocked_403_in_owner_runtime | runtime access blocked; no download/hash claim for this fixture |
| bls_women_labor_force_databook_2016 | U.S. Bureau of Labor Statistics | 403 | blocked_403_in_owner_runtime | runtime access blocked; no download/hash claim for this fixture |
| bls_monthly_labor_review_2011_06 | U.S. Bureau of Labor Statistics Monthly Labor Review | 403 | blocked_403_in_owner_runtime | runtime access blocked; no download/hash claim for this fixture |
| bls_beyond_numbers_not_in_labor_force_2015 | U.S. Bureau of Labor Statistics | 403 | blocked_403_in_owner_runtime | runtime access blocked; no download/hash claim for this fixture |

## Next Gate

- real_world_pdf_parse_observation_without_robust_claim_v0

## Boundary Notes

- download/hash metadata only
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

This is download/hash metadata only.

It records source URLs, runtime HTTP status, byte size, SHA-256, and binary non-commitment.

It does not parse, OCR, chunk, retrieve, evaluate, or generate reports from these PDFs.

This is not robust PDF extraction implementation.

This is not arbitrary market PDF parsing evidence.

This is not hosted deployment evidence.

This is not product-complete.
