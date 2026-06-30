# Cross-publisher Real-world PDF Fixture Gate

Phase `cross_publisher_real_world_pdf_fixture_gate_v0` adds one EIA
Short-Term Energy Outlook owner-runtime observation to the existing BEA
real-world PDF matrix.

## What Changed

Added:

- `examples/pdf-extraction-quality/cross-publisher-real-world-pdf-observation.json`
- `packages/ingestion/pdf_quality/cross_publisher_real_world_fixture.py`
- `apps/api/app/services/cross_publisher_real_world_pdf_fixture_gate_command.py`
- `docs/evaluation/cross-publisher-real-world-pdf-fixture-gate-report.md`
- `apps/api/tests/test_cross_publisher_real_world_pdf_fixture_gate.py`

Updated:

- `docs/research/source-assimilation-registry.md`
- `apps/api/app/services/proof_gap_registry.py`
- `.github/workflows/ci.yml`
- `README.md`
- `docs/GOAL.md`
- `docs/MASTER-SPEC.md`
- `docs/runbook.md`
- `docs/application/portfolio-index.md`
- `docs/review/proof-gap-action-surface.md`

## Gate Result

```text
cross_publisher_gate_status -> passed
base_observed_fixture_count -> 3
added_observed_fixture_count -> 1
combined_observed_fixture_count -> 4
distinct_publisher_count -> 2
has_cross_publisher_coverage -> true
can_claim_cross_publisher_real_world_pdf_fixture_coverage -> true
can_claim_robust_pdf_extraction -> false
```

## Added Fixture

```text
fixture_id -> eia_steo_full_2026_06
publisher -> U.S. Energy Information Administration
title -> Short-Term Energy Outlook, June 2026
source_url -> https://www.eia.gov/outlooks/steo/pdf/steo_full.pdf
license_source_url -> https://www.eia.gov/about/copyrights_reuse.php
publication_page_url -> https://www.eia.gov/outlooks/steo/
page_count -> 60
text_char_count -> 249238
table_candidate_count -> 58
```

## Remaining Blockers

The cross-publisher blocker is reduced, but robust PDF extraction remains
blocked because there is still no table extraction evidence, OCR evidence, or
layout fidelity evidence.

Remaining blocked reasons:

```text
table_extraction_evidence_missing
ocr_evidence_missing
layout_fidelity_evidence_missing
```

## Boundary

This is cross-publisher fixture coverage over sanitized owner-runtime
observations.

Boundaries:

- not robust PDF extraction evidence
- not arbitrary-market PDF parsing evidence
- not OCR evidence
- not table extraction evidence
- not layout fidelity evidence
- not hosted deployment evidence
- not external reviewer feedback
- not customer validation
- not Braincrew acceptance
- not product-complete

## Verification

RED test before implementation:

```text
uv run pytest tests/test_cross_publisher_real_world_pdf_fixture_gate.py -q
ModuleNotFoundError: No module named 'packages.ingestion.pdf_quality.cross_publisher_real_world_fixture'
```

Focused verification after implementation:

```text
uv run pytest tests/test_proof_gap_action_surface_current_state_refresh.py tests/test_routes.py::test_ops_summary_and_dashboard_surface_current_proof_gap_registry tests/test_routes.py::test_ops_proof_gap_action_surface_exposes_gap_details_without_closing_gap tests/test_robust_pdf_real_world_quality_gate.py tests/test_cross_publisher_real_world_pdf_fixture_gate.py -q
12 passed in 4.12s
```

Report staleness verification:

```text
uv run python -m app.services.cross_publisher_real_world_pdf_fixture_gate_command --base-matrix ..\..\examples\pdf-extraction-quality\multi-real-world-pdf-parse-observations.json --observation ..\..\examples\pdf-extraction-quality\cross-publisher-real-world-pdf-observation.json --output ..\..\docs\evaluation\cross-publisher-real-world-pdf-fixture-gate-report.md --check
cross_publisher_real_world_pdf_fixture_gate_report_current
cross_publisher_gate_status=passed
not robust PDF extraction evidence
```

Compile verification:

```text
uv run python -m compileall app ..\..\packages\ingestion
exit code 0
```

Full verification:

```text
uv run pytest -q
1287 passed in 47.47s
```

## Next Gate

```text
real_world_table_extraction_evidence_gate_v0
```

Do not use this gate to claim robust PDF extraction.
