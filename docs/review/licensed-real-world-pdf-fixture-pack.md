# Licensed Real-world PDF Fixture Pack

Phase 884 adds licensed real-world PDF fixture pack v0.

Status: implemented as a metadata-only candidate pack.

Purpose: identify real-world PDF candidates with visible source and license
boundaries before downloading, hashing, parsing, or committing any external
PDF binaries.

Artifacts:

- `examples/pdf-extraction-quality/licensed-real-world-candidates.json`
- `packages/ingestion/pdf_quality/licensed_real_world_fixture_pack.py`
- `apps/api/app/services/licensed_real_world_fixture_pack_command.py`
- `docs/evaluation/licensed-real-world-pdf-fixture-pack-report.md`
- `apps/api/tests/test_licensed_real_world_pdf_fixture_pack.py`

Report markers:

```text
phase_marker -> licensed_real_world_pdf_fixture_pack_v0
candidate_count -> 4
downloaded_candidate_count -> 0
binary_files_committed -> false
robust_pdf_extraction_claimed -> false
can_claim_robust_pdf_extraction -> false
recommended_next_gate -> owner_approved_real_world_pdf_download_and_hash_v0
```

Candidate roles:

```text
digital_text_tables
long_report_tables
multi_column_article
article_with_figures
```

Source/license basis:

- BLS copyright information: `https://www.bls.gov/opub/copyright-information.htm`
- BLS Monthly Labor Review about/copyright note: `https://www.bls.gov/opub/mlr/about.htm`
- BEA copyright FAQ, retained as a future source option: `https://www.bea.gov/help/faq/147`

The candidate pack intentionally uses stable or archive-style URLs where
possible and avoids mutable current-release URLs for committed evidence.

Boundaries:

- candidate metadata only
- no external PDF binaries committed
- no PDF download performed
- no sha256 hash evidence yet
- not robust PDF extraction evidence
- not arbitrary market PDF parsing evidence
- not OCR evidence
- not table extraction evidence
- not layout fidelity evidence
- not hosted deployment evidence
- not external reviewer feedback
- not customer validation
- not Braincrew acceptance
- not product-complete

Next gate: `owner_approved_real_world_pdf_download_and_hash_v0`.
