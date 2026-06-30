# Robust PDF Extraction Next Real-world Quality Gate Spec

title: Robust PDF extraction next real-world quality gate

status: implemented

date: 2026-06-30

target_gate: `robust_pdf_extraction_next_real_world_quality_gate_v0`

## current_repo_state

At selection time, the robust-PDF action surface pointed to
`robust_pdf_extraction_next_real_world_quality_gate_v0`.

Existing local inputs:

- `examples/pdf-extraction-quality/multi-real-world-pdf-parse-observations.json`
- `docs/review/multi-real-world-pdf-parse-observation.md`
- `docs/evaluation/multi-real-world-pdf-parse-observation-report.md`
- `docs/review/multi-real-world-pdf-parse-observation-remote-verification.md`

The existing matrix records three BEA real-world PDFs with PyMuPDF digital-text
observations. It does not include cross-publisher coverage, OCR evidence, table
extraction evidence, layout fidelity evidence, committed external binaries, raw
extracted text, or hosted deployment evidence.

## sources_to_absorb

Use existing source cards:

- Model Cards: expose intended use, caveats, status, and next evidence.
- Datasheets for Datasets: expose source policy, composition, omissions, and
  maintenance boundaries for fixture data.
- Docling and Unstructured: keep digital text, table extraction, OCR, layout,
  and typed-element extraction separate.
- SLSA Provenance: keep observed inputs, generated report, and verification
  command explicit.
- Diataxis: keep reviewer-facing review artifact separate from generated
  evaluation report and runbook instructions.

No new source card is required for this gate because the source basis was
already assimilated.

## non_goals

- Do not download new external PDFs.
- Do not commit external PDF binaries, download caches, or raw extracted text.
- Do not implement OCR, table extraction, layout reconstruction, embeddings, or
  retrieval.
- Do not claim robust PDF extraction.
- Do not claim arbitrary market PDF parsing reliability.
- Do not claim hosted deployment or external reviewer feedback.

## implementation_scope

Create:

- `packages/ingestion/pdf_quality/real_world_quality_gate.py`
- `apps/api/app/services/robust_pdf_real_world_quality_gate_command.py`
- `docs/evaluation/robust-pdf-real-world-quality-gate-report.md`
- `docs/review/robust-pdf-extraction-next-real-world-quality-gate.md`
- `apps/api/tests/test_robust_pdf_real_world_quality_gate.py`

Update:

- `apps/api/app/services/proof_gap_registry.py`
- `.github/workflows/ci.yml`
- `README.md`
- `docs/GOAL.md`
- `docs/MASTER-SPEC.md`
- `docs/runbook.md`
- `docs/application/portfolio-index.md`
- `docs/review/proof-gap-action-surface.md`

## data_or_api_contract

No API endpoint or database schema changes.

The quality gate consumes the existing multi real-world PDF matrix and produces
a deterministic summary/report with:

```text
phase_marker
input_matrix_phase
quality_gate_status
observed_fixture_count
distinct_publisher_count
digital_text_coverage_ratio
has_cross_publisher_coverage
has_table_extraction_evidence
has_ocr_evidence
has_layout_fidelity_evidence
can_claim_robust_pdf_extraction
blocked_reasons
passed_checks
next_gate
```

Expected result for current data:

```text
quality_gate_status -> blocked
can_claim_robust_pdf_extraction -> false
next_gate -> cross_publisher_real_world_pdf_fixture_gate_v0
```

## tests

Write RED tests first:

```text
uv run pytest tests/test_robust_pdf_real_world_quality_gate.py -q
```

Expected before implementation:

```text
FAIL because the module, command, report, and review artifact do not exist.
```

Then implement the smallest deterministic quality gate and report generator.

## docs_to_update

Update the proof surfaces so reviewers understand this as a quality gate that
keeps the robust-PDF claim blocked.

## stop_conditions

Stop if:

- the existing matrix is missing or stale;
- local data would require downloading new PDFs to satisfy the gate;
- the gate starts implying robust PDF extraction, OCR, table extraction, layout
  fidelity, or arbitrary market PDF reliability.

If stopped, report:

```text
planned_path:
actual_state:
blocking_mismatch:
why_this_blocks_the_gate:
minimum_action_to_resume:
```

## claim_boundaries

This gate is a deterministic quality-gate report over existing observations.

It is not robust PDF extraction evidence, not arbitrary-market PDF parsing
evidence, not OCR evidence, not table extraction evidence, not layout fidelity
evidence, not hosted deployment evidence, not external reviewer feedback, not
customer validation, not Braincrew acceptance, and not product-complete.

## next_gate_if_passed

```text
cross_publisher_real_world_pdf_fixture_gate_v0
```

The current matrix uses one publisher family only. The next local evidence
should add source-policy-reviewed, non-BEA real-world fixture coverage before
any stronger robust-PDF claim is considered.
