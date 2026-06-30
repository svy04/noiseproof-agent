# Real-world Layout Fidelity Evidence Gate

Phase `real_world_layout_fidelity_evidence_gate_v0` records one sanitized
layout-metadata sanity observation from a temporary owner-runtime BEA PDF
download.

## What Changed

Added:

- `examples/pdf-extraction-quality/real-world-layout-fidelity-evidence.json`
- `packages/ingestion/pdf_quality/real_world_layout_fidelity_evidence.py`
- `apps/api/app/services/real_world_layout_fidelity_evidence_gate_command.py`
- `docs/evaluation/real-world-layout-fidelity-evidence-gate-report.md`
- `apps/api/tests/test_real_world_layout_fidelity_evidence_gate.py`

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
layout_gate_status -> passed
observed_fixture_count -> 1
layout_observed_fixture_count -> 1
publisher -> U.S. Bureau of Economic Analysis
fixture_id -> bea_open_source_software_innovation_wp_2022_10
total_page_count -> 30
observed_page_count -> 1
total_block_count -> 20
total_text_block_count -> 16
total_text_blocks_with_bbox_in_page_bounds -> 16
expected_markers_found_count -> 7
expected_marker_order_observed -> true
can_claim_real_world_layout_fidelity_evidence -> true
can_claim_robust_pdf_extraction -> false
```

## Evidence Shape

The committed evidence is sanitized metadata only:

```text
source URL
license/source policy URL
HTTP metadata
SHA-256
byte size
page count
observed page index
page geometry
block counts
bbox samples without text
expected marker hit booleans
marker order sanity result
warnings
```

The repo does not commit:

```text
external PDF binaries
download caches
local PDF paths
raw extracted text
raw block text
screenshots
rendered page images
```

## Remaining Blockers

The layout blocker is reduced for one BEA fixture, but robust PDF extraction
remains blocked because the current evidence is too small to generalize.

Remaining blocked reasons:

```text
robust_pdf_generalization_missing
arbitrary_market_pdf_coverage_missing
```

## Boundary

This is real-world layout metadata sanity evidence over one sanitized
owner-runtime observation.

Boundaries:

- not robust PDF extraction evidence
- not arbitrary-market PDF parsing evidence
- not arbitrary-market layout fidelity evidence
- not natural reading order correctness evidence
- not rendered visual fidelity evidence
- not hosted deployment evidence
- not external reviewer feedback
- not customer validation
- not Braincrew acceptance
- not product-complete

## Verification

RED test before implementation:

```text
uv run pytest tests/test_real_world_layout_fidelity_evidence_gate.py -q
ModuleNotFoundError: No module named 'packages.ingestion.pdf_quality.real_world_layout_fidelity_evidence'
```

Focused verification after implementation:

```text
uv run pytest tests/test_real_world_layout_fidelity_evidence_gate.py -q
```

Report staleness verification:

```text
uv run python -m app.services.real_world_layout_fidelity_evidence_gate_command --evidence ..\..\examples\pdf-extraction-quality\real-world-layout-fidelity-evidence.json --output ..\..\docs\evaluation\real-world-layout-fidelity-evidence-gate-report.md --check
```

## Next Gate

```text
robust_pdf_extraction_generalization_gap_review_v0
```

Do not use this gate to claim robust PDF extraction.
