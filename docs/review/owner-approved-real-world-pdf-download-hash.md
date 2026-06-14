# Owner-approved Real-world PDF Download and Hash

Phase 887 adds owner-approved real-world PDF download/hash v0.

This is a bounded owner-runtime evidence gate.

It records one accessible BEA PDF download/hash observation and four BLS
runtime 403 observations.

It does not commit external PDF binaries or download caches.

## Evidence

- manifest: `examples/pdf-extraction-quality/owner-approved-real-world-download-hash.json`
- report: `docs/evaluation/owner-approved-real-world-pdf-download-hash-report.md`
- command: `app.services.owner_approved_real_world_pdf_download_hash_command`
- test: `apps/api/tests/test_owner_approved_real_world_pdf_download_hash.py`

## Observed Counts

- downloaded_fixture_count -> 1
- blocked_fixture_count -> 4
- binary_files_committed -> false
- download_cache_committed -> false
- parser_calls_attempted -> false
- ocr_calls_attempted -> false
- table_extraction_attempted -> false
- can_claim_robust_pdf_extraction -> false

## Downloaded Fixture

- `bea_nipa_glossary_2019`
- source: `https://www.bea.gov/resources/methodologies/nipa-handbook/pdf/glossary.pdf`
- content type: `application/pdf`
- byte size: `315727`
- SHA-256: `991c6335ffb794cf8f7731a4bff770b810f63693d44af23f0edc8ffecab89cb6`

## Blocked Runtime Attempts

The four BLS candidate URLs from
`examples/pdf-extraction-quality/licensed-real-world-candidates.json` returned
HTTP 403 in this owner runtime. No download/hash claim is made for those
fixtures.

## Boundary

This is download/hash metadata only.

This is not robust PDF extraction evidence.

This is not arbitrary market PDF parsing evidence.

This is not OCR, table extraction, layout fidelity, hosted deployment, external
reviewer feedback, customer validation, Braincrew acceptance, or product-complete
evidence.

Next gate: `real_world_pdf_parse_observation_without_robust_claim_v0`.
