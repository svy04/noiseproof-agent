# Real-world Table Extraction Evidence Gate

Phase `real_world_table_extraction_evidence_gate_v0` records sanitized table
extraction output from temporary owner-runtime real-world PDF downloads.

## What Changed

Added:

- `examples/pdf-extraction-quality/real-world-table-extraction-evidence.json`
- `packages/ingestion/pdf_quality/real_world_table_extraction_evidence.py`
- `apps/api/app/services/real_world_table_extraction_evidence_gate_command.py`
- `docs/evaluation/real-world-table-extraction-evidence-gate-report.md`
- `apps/api/tests/test_real_world_table_extraction_evidence_gate.py`

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
table_extraction_gate_status -> passed
observed_fixture_count -> 3
table_extraction_observed_fixture_count -> 3
distinct_publisher_count -> 2
total_table_count -> 124
total_table_rows_extracted -> 847
total_table_cell_count -> 7902
has_table_extraction_evidence -> true
can_claim_real_world_table_extraction_evidence -> true
can_claim_robust_pdf_extraction -> false
```

## Evidence Shape

The committed evidence is sanitized metadata only:

```text
source URL
license/source policy URL
SHA-256
page count
table extraction engine
table count
row count
cell count
table shape sample
warnings
```

The repo does not commit:

```text
external PDF binaries
download caches
raw extracted text
raw table rows
```

## Remaining Blockers

The table extraction blocker is reduced for the listed real-world fixtures, but
robust PDF extraction remains blocked because OCR and layout fidelity evidence
are still missing.

Remaining blocked reasons:

```text
ocr_evidence_missing
layout_fidelity_evidence_missing
```

## Boundary

This is real-world table extraction evidence over sanitized owner-runtime
observations.

Boundaries:

- not robust PDF extraction evidence
- not arbitrary-market PDF parsing evidence
- not OCR evidence
- not layout fidelity evidence
- not hosted deployment evidence
- not external reviewer feedback
- not customer validation
- not Braincrew acceptance
- not product-complete

## Verification

RED test before implementation:

```text
uv run pytest tests/test_real_world_table_extraction_evidence_gate.py -q
ModuleNotFoundError: No module named 'packages.ingestion.pdf_quality.real_world_table_extraction_evidence'
```

Focused verification after implementation:

```text
uv run pytest tests/test_real_world_table_extraction_evidence_gate.py -q
4 passed in 0.23s
```

Report staleness verification:

```text
uv run python -m app.services.real_world_table_extraction_evidence_gate_command --evidence ..\..\examples\pdf-extraction-quality\real-world-table-extraction-evidence.json --output ..\..\docs\evaluation\real-world-table-extraction-evidence-gate-report.md --check
real_world_table_extraction_evidence_gate_report_current
table_extraction_gate_status=passed
not robust PDF extraction evidence
```

Adjacent proof-gap verification:

```text
uv run pytest tests/test_proof_gap_action_surface_current_state_refresh.py tests/test_routes.py::test_ops_summary_and_dashboard_surface_current_proof_gap_registry tests/test_routes.py::test_ops_proof_gap_action_surface_exposes_gap_details_without_closing_gap tests/test_robust_pdf_real_world_quality_gate.py tests/test_cross_publisher_real_world_pdf_fixture_gate.py tests/test_real_world_table_extraction_evidence_gate.py -q
16 passed in 4.36s
```

Full verification:

```text
uv run pytest -q
1291 passed in 41.35s
```

## Next Gate

```text
real_world_ocr_evidence_gate_v0
```

Do not use this gate to claim robust PDF extraction.
