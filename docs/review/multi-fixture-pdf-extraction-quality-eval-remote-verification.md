# Multi-fixture PDF Extraction Quality Eval Remote Verification

Phase 871 records remote workflow verification for the Phase 870
multi-fixture PDF extraction quality eval after it was pushed to `main`.

Phase marker: multi-fixture PDF extraction quality eval remote verification v0.

Remote verification markers:

```text
verified_head_sha -> 0c9cf904fdb28f431338b683ded0d89d30fdbd88
branch -> main
commit -> feat: add multi-fixture pdf extraction quality matrix
CI run `27491985623`: success
CI job_id -> 81258771544
CI job_name -> api-smoke
External Feedback Screen run `27491985622`: success
External Feedback Screen job_id -> 81258771520
External Feedback Screen job_name -> screen
```

Remote CI step evidence included:

```text
Compile API and local packages -> success
Check PDF extraction quality report staleness -> success
Check multi-fixture PDF extraction quality report staleness -> success
Check live embedding domain qrels owner-runtime runner missing input -> success
Run API smoke tests -> success
```

Verified Phase 870 artifacts:

- `packages/ingestion/pdf_quality/multi_fixture.py`
- `apps/api/app/services/multi_fixture_pdf_extraction_quality_command.py`
- `docs/evaluation/multi-fixture-pdf-extraction-quality-report.md`
- `docs/review/multi-fixture-pdf-extraction-quality-eval.md`
- `.github/workflows/ci.yml`

This is remote workflow verification only. It is not a new local runtime smoke,
not robust PDF extraction evidence, not OCR evidence, not layout fidelity
evidence, not hosted deployment evidence, not external reviewer feedback, not
customer validation, not Braincrew acceptance, and not product-complete.
