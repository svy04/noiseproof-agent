# Missing PDF Runtime Observation Pack

Phase 872 adds missing PDF runtime observation pack v0.

Purpose: fill the four runtime-observation gaps surfaced by the Phase 870
multi-fixture matrix without claiming robust PDF extraction.

This gate adds:

- `examples/pdf-extraction-quality/missing-runtime-observations.json`
- `packages/ingestion/pdf_quality/missing_runtime_pack.py`
- `app.services.missing_pdf_runtime_observation_pack_command`
- `docs/evaluation/missing-pdf-runtime-observation-pack-report.md`

The pack covers the previously missing roles:

```text
scanned_image_pdf
image_heavy_pdf
multi_column_layout_pdf
no_extractable_text_pdf
```

Report markers:

```text
phase_marker -> missing_pdf_runtime_observation_pack_v0
fixture_count -> 8
base_observed_fixture_count -> 4
pack_observed_fixture_count -> 4
combined_observed_fixture_count -> 8
remaining_missing_runtime_observation_count -> 0
robust_pdf_extraction_claimed -> false
can_claim_robust_pdf_extraction -> false
```

The pack follows the source-first boundary already recorded in
`docs/review/robust-pdf-extraction-source-first-strategy-review.md`: PyMuPDF
is a digital-text/page-diagnostics baseline, OCR must be explicit, image/chart
interpretation is not text extraction, and layout fidelity is not proven by raw
text extraction order.

Reproduce locally:

```powershell
cd apps/api
uv run python -m app.services.missing_pdf_runtime_observation_pack_command `
  --fixture ../../examples/pdf-extraction-quality `
  --base-observations ../../examples/pdf-extraction-quality/observations.json `
  --pack ../../examples/pdf-extraction-quality/missing-runtime-observations.json `
  --output ../../docs/evaluation/missing-pdf-runtime-observation-pack-report.md `
  --check
uv run pytest tests/test_missing_pdf_runtime_observation_pack.py -q
```

CI now checks the report with:

```text
Check missing PDF runtime observation pack report staleness
```

Next recommended gate: `ocr_layout_image_fixture_adapter_runtime_pack_v0`.

This is a missing-runtime-observation pack only. It is not robust PDF extraction
implementation, not OCR implementation, not image/chart interpretation
evidence, not layout fidelity evidence, not hosted deployment evidence, not
external reviewer feedback, and not product-complete.
