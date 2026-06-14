# Multi-fixture OCR Adapter Eval

Phase 882 adds multi-fixture OCR adapter eval v0.

Purpose: combine the existing 8-role PDF fixture matrix with one sanitized
owner-runtime OCR smoke observation, without claiming robust PDF extraction.

This gate adds:

- `examples/pdf-extraction-quality/owner-runtime-ocr-smoke-observation.json`
- `packages/ingestion/pdf_quality/multi_fixture_ocr_adapter_eval.py`
- `apps/api/app/services/multi_fixture_ocr_adapter_eval_command.py`
- `apps/api/tests/test_multi_fixture_ocr_adapter_eval.py`
- `docs/evaluation/multi-fixture-ocr-adapter-eval-report.md`

Report markers:

```text
phase_marker -> multi_fixture_ocr_adapter_eval_v0
base_fixture_count -> 8
base_observed_fixture_count -> 8
owner_runtime_ocr_smoke_count -> 1
combined_fixture_signal_count -> 9
owner_runtime_ocr_expected_spans_found -> true
robust_pdf_extraction_claimed -> false
can_claim_robust_pdf_extraction -> false
```

Signal boundary markers:

```text
ocr_smoke_text_image_pdf -> owner_runtime_ocr_smoke_passed
scanned_image_pdf -> base_scanned_role_still_boundary_only
image_heavy_pdf -> image_diagnostics_only
multi_column_layout_pdf -> layout_diagnostics_only
```

Reproduce locally:

```powershell
cd apps/api
uv run python -m app.services.multi_fixture_ocr_adapter_eval_command `
  --fixture ../../examples/pdf-extraction-quality `
  --base-observations ../../examples/pdf-extraction-quality/observations.json `
  --missing-pack ../../examples/pdf-extraction-quality/missing-runtime-observations.json `
  --owner-ocr-observation ../../examples/pdf-extraction-quality/owner-runtime-ocr-smoke-observation.json `
  --output ../../docs/evaluation/multi-fixture-ocr-adapter-eval-report.md `
  --check
uv run pytest tests/test_multi_fixture_ocr_adapter_eval.py -q
```

CI now checks the report with:

```text
Check multi-fixture OCR adapter eval report staleness
```

Next recommended gate: `licensed_real_world_pdf_fixture_pack_v0`.

This is a multi-fixture OCR adapter evaluation surface only. It is not robust
PDF extraction evidence, not arbitrary market PDF OCR evidence, not image/chart
interpretation evidence, not layout fidelity evidence, not hosted deployment
evidence, not external reviewer feedback, and not product-complete.

Boundary phrases: not robust PDF extraction evidence; not arbitrary market PDF OCR evidence.
