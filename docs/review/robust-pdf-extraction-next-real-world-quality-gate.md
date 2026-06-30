# Robust PDF Extraction Next Real-world Quality Gate

Phase `robust_pdf_extraction_next_real_world_quality_gate_v0` adds a
deterministic quality gate over the existing multi real-world PDF parse
observation matrix.

## What Changed

Added:

- `packages/ingestion/pdf_quality/real_world_quality_gate.py`
- `apps/api/app/services/robust_pdf_real_world_quality_gate_command.py`
- `docs/evaluation/robust-pdf-real-world-quality-gate-report.md`
- `apps/api/tests/test_robust_pdf_real_world_quality_gate.py`

Updated:

- `apps/api/app/services/proof_gap_registry.py`
- `.github/workflows/ci.yml`
- `README.md`
- `docs/GOAL.md`
- `docs/MASTER-SPEC.md`
- `docs/runbook.md`
- `docs/application/portfolio-index.md`
- `docs/review/proof-gap-action-surface.md`

## Gate Result

The current matrix is useful but still blocked:

```text
quality_gate_status -> blocked
observed_fixture_count -> 3
distinct_publisher_count -> 1
digital_text_coverage_ratio -> 1.0000
has_cross_publisher_coverage -> false
has_table_extraction_evidence -> false
has_ocr_evidence -> false
has_layout_fidelity_evidence -> false
can_claim_robust_pdf_extraction -> false
```

## Why It Is Blocked

The current real-world evidence uses one publisher family only and still has no
table extraction evidence, OCR evidence, or layout fidelity evidence.

Blocked reasons:

```text
cross_publisher_coverage_missing
table_extraction_evidence_missing
ocr_evidence_missing
layout_fidelity_evidence_missing
```

## Boundary

This is a deterministic quality-gate report over existing sanitized
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
uv run pytest tests/test_robust_pdf_real_world_quality_gate.py -q
```

Observed result before implementation:

```text
1 error
```

Focused verification after implementation:

```text
uv run pytest tests/test_proof_gap_action_surface_current_state_refresh.py tests/test_routes.py::test_ops_summary_and_dashboard_surface_current_proof_gap_registry tests/test_routes.py::test_ops_proof_gap_action_surface_exposes_gap_details_without_closing_gap tests/test_multi_real_world_pdf_parse_observation_matrix.py tests/test_robust_pdf_real_world_quality_gate.py -q
18 passed in 8.15s
```

Report staleness verification:

```text
uv run python -m app.services.robust_pdf_real_world_quality_gate_command --matrix ..\..\examples\pdf-extraction-quality\multi-real-world-pdf-parse-observations.json --output ..\..\docs\evaluation\robust-pdf-real-world-quality-gate-report.md --check
robust_pdf_real_world_quality_gate_report_current
quality_gate_status=blocked
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
1283 passed in 59.16s
```

## Next Gate

```text
cross_publisher_real_world_pdf_fixture_gate_v0
```

Do not use this gate to claim robust PDF extraction.
