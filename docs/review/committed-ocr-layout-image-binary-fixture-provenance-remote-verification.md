# Committed OCR Layout Image Binary Fixture Provenance Remote Verification

Status: implemented.

Purpose: record remote workflow verification for the committed OCR/layout/image
binary fixture provenance gate after it was pushed to `main`.

Verified artifact:

- `docs/review/committed-ocr-layout-image-binary-fixture-provenance.md`
- `docs/evaluation/committed-ocr-layout-image-binary-fixture-provenance-report.md`
- `examples/pdf-extraction-quality/binary-fixtures/ocr-layout-image-provenance.json`

Remote verification markers:

```text
verified_head_sha -> e151dba810aaa7af4897727dd1a88415685cf632
branch -> main
commit -> feat: add committed ocr layout image fixture provenance
ci_run -> 27493138288
ci_job_id -> 81262073564
ci_job_name -> api-smoke
ci_conclusion -> success
external_feedback_screen_run -> 27493138291
external_feedback_screen_job_id -> 81262073535
external_feedback_screen_job_name -> screen
external_feedback_screen_conclusion -> success
```

Remote CI step evidence included:

```text
Compile API and local packages -> success
Check OCR layout image fixture adapter runtime pack report staleness -> success
Check committed OCR layout image binary fixture provenance report staleness -> success
Run API smoke tests -> success
```

Boundaries:

- remote workflow verification only
- not the product gate itself
- not robust PDF extraction evidence
- not OCR evidence
- not image/chart interpretation evidence
- not layout fidelity evidence
- not hosted deployment evidence
- not external reviewer feedback
- not customer validation
- not Braincrew acceptance
- not product-complete
