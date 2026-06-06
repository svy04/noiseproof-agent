# NoiseProof Agent

A noise-resilient data agent for messy market intelligence.

This project ingests messy documents and market data, evaluates chunking and retrieval strategies, detects contradictory evidence, and generates claim-bounded reports with citations. It is not a trading bot and does not provide buy/sell recommendations.

## External Reviewer Fast Path

Start with `docs/review/external-reader-proof-path.md`.

That file is the 5-minute repository-native path for reviewing what this project currently proves. It points to the README, portfolio index, failure-case workflow parent proof index, failure-case workflow review queue proof index, application-ready review, and Braincrew role map.

Boundary: this fast path is not hosted deployment evidence, not automatic failure-case creation beyond the local v0 workflow failure path, and not complete workflow failure causality.

Latest product ops surface: `docs/review/evidence-quality-risk-ops-surface.md` records that persisted Evidence Ledger rows now drive `weakly_supported_evidence_count`, `low_confidence_evidence_count`, `missing_source_date_evidence_count`, and `evidence_quality_risk_count` in `GET /ops/summary`, while `GET /ops/dashboard` renders `Weak Evidence`, `Low Confidence Evidence`, `Missing Source Dates`, and `Evidence Quality Risk Rows`. Evidence quality risk ops surface v0: implemented. This is operations metadata only, not final truth adjudication, not retrieval quality evidence, not embedding generation, not an LLM call, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Latest product ops runtime smoke: `docs/review/evidence-quality-risk-ops-surface-runtime-smoke.md` records local Docker PostgreSQL plus live FastAPI HTTP proof under `noiseproof-phase689` with `POSTGRES_PORT=55450`, `POST /evidence-ledgers -> 201`, `GET /ops/summary -> 200`, and `GET /ops/dashboard -> 200`. Evidence quality risk ops surface runtime smoke v0: verified. This is local runtime evidence only, not hosted deployment evidence, not final truth adjudication, not retrieval quality evidence, not embedding generation, not external reviewer feedback, and not product-complete.

Latest product ops runtime smoke remote verification: `docs/review/evidence-quality-risk-ops-surface-runtime-smoke-remote-verification.md` records that commit `2344fe63d79c51558a73716af35c6031d6194001` passed CI run `27059770935` and External Feedback Screen run `27059770929`. Evidence quality risk ops surface runtime smoke remote verification v0: implemented. This is remote workflow verification only, not the local runtime smoke itself, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Latest proof routing now points reviewers to the evidence-quality risk ops proof chain through `docs/review/external-reader-proof-path-evidence-quality-risk-ops-route-refresh.md`. External-reader proof path evidence quality risk ops route refresh v0: implemented. This is reviewer routing only; it is not new runtime evidence, not a live issue body edit, not final truth adjudication, not retrieval quality evidence, not Evidence Ledger quality evidence, not embedding generation, not an LLM call, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Latest proof route remote verification: `docs/review/external-reader-proof-path-evidence-quality-risk-ops-route-refresh-remote-verification.md` records that commit `b16792e0e06076a440e0cb3d072a204b1271c322` passed CI run `27060113992` and External Feedback Screen run `27060113984`. External-reader proof path evidence quality risk ops route refresh remote verification v0: implemented. This is remote workflow verification only, not the reader-route refresh itself, not new runtime evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Latest product handoff: `docs/review/evidence-quality-risk-failure-case-draft-preview.md` records `POST /evidence-ledgers/{entry_id}/failure-case-draft-preview`, a preview-only manual handoff from persisted Evidence Ledger quality-risk rows to a failure-case draft. Evidence quality risk failure-case draft preview v0: implemented. This is not automatic failure-case creation, not final truth adjudication, not retrieval quality evidence, not Evidence Ledger quality evidence, not an LLM call, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Latest product handoff runtime smoke: `docs/review/evidence-quality-risk-failure-case-draft-preview-runtime-smoke.md` records local Docker PostgreSQL plus live FastAPI HTTP proof under `noiseproof-phase694` with `POSTGRES_PORT=55451`, `Pending migrations: 0`, weak-row draft preview `200`, clean-row `409`, missing-row `404`, and `failure_case_count_delta -> 0`. Evidence quality risk failure-case draft preview runtime smoke v0: verified. This is local runtime evidence only, not hosted deployment evidence, not automatic failure-case creation, not final truth adjudication, not Evidence Ledger quality evidence, not external reviewer feedback, and not product-complete.

Latest product handoff runtime smoke remote verification: `docs/review/evidence-quality-risk-failure-case-draft-preview-runtime-smoke-remote-verification.md` records that commit `7865ccfe608c4d2ceba714c9ded22c2eecc601b2` passed CI run `27060589358` and External Feedback Screen run `27060589349`. Evidence quality risk failure-case draft preview runtime smoke remote verification v0: implemented. This is remote workflow verification only, not the local runtime smoke itself, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Latest proof routing now points reviewers to the evidence-quality draft preview proof chain through `docs/review/external-reader-proof-path-evidence-quality-draft-preview-route-refresh.md`. External-reader proof path evidence quality draft preview route refresh v0: implemented. This is reviewer routing only; it is not new runtime evidence, not a live issue body edit, not automatic failure-case creation, not final truth adjudication, not retrieval quality evidence, not Evidence Ledger quality evidence, not embedding generation, not an LLM call, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Latest proof route remote verification: `docs/review/external-reader-proof-path-evidence-quality-draft-preview-route-refresh-remote-verification.md` records that commit `c2024456f449b9ab65272ba51c0cbfb71e32879f` passed CI run `27060871797` and External Feedback Screen run `27060871781`. External-reader proof path evidence quality draft preview route refresh remote verification v0: implemented. This is remote workflow verification only, not the reader-route refresh itself, not new runtime evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Latest external review issue routing: `docs/review/external-review-issue-body-evidence-quality-draft-preview-route-refresh.md` records that issue #1 now routes `Latest Proof To Inspect` to the Evidence quality failure-case draft preview proof chain and no longer labels the workflow markdown proof as latest. External review issue body evidence quality draft preview route refresh v0: implemented. This is owner-authored issue body routing only, not external reviewer feedback, not hosted deployment evidence, not customer validation, not Braincrew acceptance, and not product-complete.

Latest external-feedback current state: `docs/review/external-feedback-current-state-evidence-quality-draft-preview-issue-verification.md` records that after the Evidence quality draft preview issue routing, issue #1 still has `candidate_count=0`, `draft_count=0`, `reason=self_authored_comment`, and `status=pending`. External feedback current-state evidence quality draft preview issue verification v0: implemented. This is current-state issue screening only, not external reviewer feedback, not hosted deployment evidence, not customer validation, not Braincrew acceptance, and not product-complete.

GOAL current-state snapshot after Phase 700 v0: implemented. `docs/GOAL.md` now starts its accepted-state section with a compact Phase 700 orientation block naming the latest reviewer route, issue route, pending feedback state, missing `OPENAI_API_KEY`, unimplemented robust PDF extraction, unimplemented hosted deployment evidence, and `product_complete: false`. This is documentation navigation only, not new runtime evidence, not external reviewer feedback, and not product-complete.

Robust PDF extraction source-first strategy review v0: implemented. `docs/review/robust-pdf-extraction-source-first-strategy-review.md` records the current `parser: pdf-pymupdf` boundary, `digital_pdf_text_extraction: true`, `robust_pdf_extraction: false`, `table_extraction_performed: false`, and a source-first adapter ladder for digital text, tables, OCR, and quality-ledger evaluation. This is strategy review only, not robust PDF extraction implementation, not OCR implementation, not table extraction implementation, not hosted deployment evidence, and not product-complete.

PDF extraction quality fixture packet v0: implemented. `docs/review/pdf-extraction-quality-fixture-packet.md` and `examples/pdf-extraction-quality/fixture-manifest.json` define fixture roles and quality metrics for future PDF extraction evaluation before any robust extraction claim. This is manifest-only fixture planning, not binary PDF fixture evidence, not robust PDF extraction implementation, not OCR implementation, not table extraction implementation, not hosted deployment evidence, and not product-complete.

PDF extraction quality evaluator v0: implemented. `packages/ingestion/pdf_quality/evaluator.py` scores caller-provided PDF extraction observations against `examples/pdf-extraction-quality/fixture-manifest.json` with `expected_span_recall`, `warning_correctness`, and `failure_case_candidate_correctness`, while preserving `manifest_metric_only_not_robust_pdf_extraction`. This is evaluator plumbing only, not robust PDF extraction implementation, not OCR implementation, not table extraction implementation, not hosted deployment evidence, and not product-complete.

PDF extraction quality report v0: implemented. `docs/evaluation/pdf-extraction-quality-report.md` is generated from `examples/pdf-extraction-quality/observations.json` and the Phase 704 evaluator, recording `observed_fixture_count = 3`, `not_evaluated_fixture_count = 4`, and `manifest_metric_only_not_robust_pdf_extraction`. This is partial evaluator output only, not robust PDF extraction evidence, not OCR evidence, not table extraction evidence, not hosted deployment evidence, and not product-complete.

PDF extraction quality report command v0: implemented. `apps/api/app/services/pdf_extraction_quality_report_command.py` regenerates or checks `docs/evaluation/pdf-extraction-quality-report.md`, and CI now runs `Check PDF extraction quality report staleness`. This is reproducibility plumbing only, not robust PDF extraction implementation, not OCR implementation, not table extraction implementation, not hosted deployment evidence, and not product-complete.

PDF extraction quality digital-text observation smoke v0: implemented. `packages/ingestion/pdf_quality/observation.py` converts actual `pdf-pymupdf` `ParseResult` output into evaluator observations; tests feed a minimal born-digital PDF through `PdfParser`, preserving `digital_pdf_text_extraction -> true`, `robust_pdf_extraction -> false`, `observed_fixture_count -> 1`, and `not_evaluated_fixture_count -> 6`. This is local deterministic parser smoke only, not robust PDF extraction implementation, not OCR implementation, not table extraction implementation, not hosted deployment evidence, and not product-complete.

PDF extraction quality table-candidate observation smoke v0: implemented. `packages/ingestion/pdf_quality/observation.py` now carries `table_candidate_count` and `table_candidate_page_counts` from `pdf-pymupdf` parser metadata while keeping `table_extraction_performed -> false`, `table_rows_extracted -> 0`, and `table_row_coverage -> 0`. This is local deterministic parser smoke only, not robust PDF extraction implementation, not OCR implementation, not table extraction implementation, not hosted deployment evidence, and not product-complete.

PDF extraction quality no-text observation smoke v0: implemented. `packages/ingestion/pdf_quality/observation.py` now carries `pdf_no_extractable_text` failure-candidate type, description, and next action from a PDF that opens but yields no digital text; the evaluator records `failure_case_candidate_correctness -> 1` while preserving `robust_pdf_extraction -> false`. This is local deterministic parser smoke only, not robust PDF extraction implementation, not OCR implementation, not table extraction implementation, not hosted deployment evidence, and not product-complete.

PDF extraction quality encrypted observation smoke v0: implemented. `packages/ingestion/pdf_quality/observation.py` now carries `encrypted -> true`, `password_required -> true`, and `pdf_encrypted_requires_password` failure-candidate metadata from a locally generated password-protected PDF; the evaluator records `failure_case_candidate_correctness -> 1` while preserving `robust_pdf_extraction -> false`. This is local deterministic parser smoke only, not decryption evidence, not robust PDF extraction implementation, not OCR implementation, not table extraction implementation, not hosted deployment evidence, and not product-complete.

PDF extraction quality observation smoke index v0: implemented. `docs/review/pdf-extraction-quality-observation-smoke-index.md` gives external reviewers one compact map across the digital-text, table-candidate, no-text, and encrypted PDF observation smokes while preserving `robust_pdf_extraction -> false`, `table_extraction_performed -> false`, and the no-decryption boundary. This is reviewer navigation only, not new runtime evidence, not robust PDF extraction implementation, not OCR implementation, not table extraction implementation, not decryption evidence, not hosted deployment evidence, and not product-complete.

PDF extraction quality observation grouped report v0: implemented. `docs/review/pdf-extraction-quality-observation-grouped-report.md` summarizes the digital-text, table-candidate, no-text, and encrypted local PDF observation smokes as one reviewer-facing report with `grouped_report_only_not_new_runtime_evidence`. This is report navigation only, not new runtime evidence, not robust PDF extraction implementation, not OCR implementation, not table extraction implementation, not decryption evidence, not hosted deployment evidence, and not product-complete.

PDF extraction quality observation grouped report remote verification v0: implemented. `docs/review/pdf-extraction-quality-observation-grouped-report-remote-verification.md` records that commit `e1dbefdbf0f3a13a9f7247fa03aaee8db62c35b9` passed CI run `27063162767` and External Feedback Screen run `27063162754` after the grouped report push. This is remote workflow verification only, not new runtime evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

upload PDF quality preview API v0: implemented. `POST /documents/upload-pdf-quality-preview` returns `quality_observation` from `packages/ingestion/pdf_quality/observation.py` with `quality_boundary -> pdf_quality_observation_preview_only_no_robust_extraction_claim` and `persistence_boundary -> preview_only_not_persisted`. This is preview-only API behavior, not document persistence, not retrieval, not Evidence Ledger generation, not decryption evidence, not robust PDF extraction implementation, not OCR implementation, not table extraction implementation, not hosted deployment evidence, and not product-complete.

upload PDF quality preview runtime smoke v0: verified. `docs/review/upload-pdf-quality-preview-runtime-smoke.md` records local Docker PostgreSQL plus live FastAPI HTTP proof under `noiseproof-phase715` with `POSTGRES_PORT=55453`, `Pending migrations: 0`, `GET /health -> 200`, born-digital upload `200`, encrypted upload `200`, `document_count_delta=0`, `digital_text_extraction=True`, `digital_robust_pdf_extraction=False`, `encrypted_password_required=True`, `encrypted_failure_type=pdf_encrypted_requires_password`, `quality_boundary=pdf_quality_observation_preview_only_no_robust_extraction_claim`, and `persistence_boundary=preview_only_not_persisted`. This is local runtime evidence only, not hosted deployment evidence, not external reviewer feedback, not document persistence evidence for this preview route, not robust PDF extraction implementation, not OCR implementation, not table extraction implementation, not decryption evidence, and not product-complete.

upload PDF quality preview runtime smoke remote verification v0: implemented. `docs/review/upload-pdf-quality-preview-runtime-smoke-remote-verification.md` records that commit `b78bcdc45a1a2f7c9a1d5a42e5a467df4e376bd0` passed CI run `27063793616` and External Feedback Screen run `27063793624` after the Phase 715 runtime smoke documentation was pushed. This is remote workflow verification only, not the local runtime smoke itself, not hosted deployment evidence, not external reviewer feedback, not robust PDF extraction implementation, not decryption evidence, and not product-complete.

External-reader proof path upload PDF quality preview route refresh v0: implemented. `docs/review/external-reader-proof-path-upload-pdf-quality-preview-route-refresh.md` adds the upload PDF quality preview API/runtime/remote-verification proof chain to `docs/review/external-reader-proof-path.md` and `docs/review/external-reviewer-link-map.md`. This is reader-route alignment only, not new runtime evidence, not a live issue body edit, not hosted deployment evidence, not external reviewer feedback, not robust PDF extraction implementation, not decryption evidence, and not product-complete.

External-reader proof path upload PDF quality preview route refresh remote verification v0: implemented. `docs/review/external-reader-proof-path-upload-pdf-quality-preview-route-refresh-remote-verification.md` records that commit `fe227e21e215aca507364562cf6ad278bb6e2479` passed CI run `27064024263` and External Feedback Screen run `27064024276` after the route refresh was pushed. This is remote workflow verification only, not the route refresh itself, not new runtime evidence, not a live issue body edit, not hosted deployment evidence, not external reviewer feedback, not robust PDF extraction implementation, not decryption evidence, and not product-complete.

External review issue body upload PDF quality preview route refresh v0: implemented. `docs/review/external-review-issue-body-upload-pdf-quality-preview-route-refresh.md` records that issue #1 now routes `Latest Proof To Inspect` to the upload PDF quality preview proof chain, with `updatedAt: 2026-06-06T13:59:24Z`, `comment_count: 1`, `starts_with_request: true`, and `old_evidence_quality_latest_label_present: false`. This is owner-authored issue body routing only, not external reviewer feedback, not hosted deployment evidence, not customer validation, not Braincrew acceptance, not robust PDF extraction implementation, not decryption evidence, and not product-complete.

External feedback current-state upload PDF quality preview issue verification v0: implemented. `docs/review/external-feedback-current-state-upload-pdf-quality-preview-issue-verification.md` records that after the upload PDF quality preview issue routing, issue #1 still has `comment_count: 1`, `owner_comment_count: 1`, `candidate_count: 0`, `draft_count: 0`, `classification: non_qualifying`, `reason: self_authored_comment`, and `status: pending`. This is current-state issue screening only, not external reviewer feedback, not hosted deployment evidence, not customer validation, not Braincrew acceptance, and not product-complete.

External feedback current-state upload PDF quality preview issue verification remote verification v0: implemented. `docs/review/external-feedback-current-state-upload-pdf-quality-preview-issue-verification-remote-verification.md` records that commit `8d4e543b2180bfd305a8752a44d4f9417f7da1c7` passed CI run `27064547630` and External Feedback Screen run `27064547631` after the Phase 720 current-state issue verification was pushed. This is remote workflow verification only, not the current-state issue screen itself, not external reviewer feedback, not hosted deployment evidence, not customer validation, not Braincrew acceptance, and not product-complete.

Upload PDF quality preview summary v0: implemented. `docs/review/upload-pdf-quality-preview-summary.md` records that `POST /documents/upload-pdf-quality-preview` now returns `quality_summary` with compact reviewer-facing PDF boundary fields, including `page_count`, `extracted_page_count`, `password_required`, `robust_pdf_extraction`, `table_extraction_performed`, `failure_case_candidate`, and `reviewer_boundary -> summary_only_not_robust_pdf_extraction_evidence`. This is response-shape inspectability only, not extracted text storage, not document persistence, not robust PDF extraction evidence, not OCR implementation, not table extraction implementation, not decryption evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Upload PDF quality preview summary remote verification v0: implemented. `docs/review/upload-pdf-quality-preview-summary-remote-verification.md` records that commit `88fad0320f98f6e34684814191ad06272217b308` passed CI run `27064845105` and External Feedback Screen run `27064845096` after the Phase 722 summary field was pushed. This is remote workflow verification only, not the summary implementation itself, not new runtime evidence, not hosted deployment evidence, not external reviewer feedback, not robust PDF extraction evidence, and not product-complete.

Upload PDF quality preview summary runtime smoke v0: verified. `docs/review/upload-pdf-quality-preview-summary-runtime-smoke.md` records local Docker PostgreSQL plus live FastAPI HTTP proof under `noiseproof-phase724` with `POSTGRES_PORT=55454`, `Pending migrations: 0`, `GET /health -> 200`, born-digital upload `200`, encrypted upload `200`, `digital_quality_summary_present=True`, `encrypted_quality_summary_present=True`, `digital_summary_boundary=summary_only_not_robust_pdf_extraction_evidence`, `encrypted_summary_failure_case=pdf_encrypted_requires_password`, and `document_count_delta=0`. This is local runtime evidence only, not hosted deployment evidence, not external reviewer feedback, not document persistence evidence for this preview route, not robust PDF extraction evidence, not OCR implementation, not table extraction implementation, not decryption evidence, and not product-complete.

Upload PDF quality preview summary runtime smoke remote verification v0: implemented. `docs/review/upload-pdf-quality-preview-summary-runtime-smoke-remote-verification.md` records that commit `87cbed97b244e941060d844b8edc342a843b24f0` passed CI run `27065207880` and External Feedback Screen run `27065207869` after the Phase 724 runtime-smoke proof was pushed. This is remote workflow verification only, not the local runtime smoke itself, not new runtime evidence, not hosted deployment evidence, not external reviewer feedback, not robust PDF extraction evidence, and not product-complete.

External-reader proof path upload PDF quality preview summary route refresh v0: implemented. `docs/review/external-reader-proof-path-upload-pdf-quality-preview-summary-route-refresh.md` routes first-pass reviewers to the compact upload PDF quality preview summary proof chain, including `quality_summary`, `summary_only_not_robust_pdf_extraction_evidence`, `digital_quality_summary_present=True`, `encrypted_quality_summary_present=True`, `digital_summary_robust_pdf_extraction=False`, `encrypted_summary_failure_case=pdf_encrypted_requires_password`, and `document_count_delta=0`. This is reader-route alignment only, not new runtime evidence, not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not robust PDF extraction evidence, and not product-complete.

Historical predecessor compatibility: Latest proof routing now points reviewers to the workflow proof bundle markdown export runtime smoke at `docs/review/workflow-proof-bundle-markdown-export-runtime-smoke.md` was the Phase 667 route marker, not the current first route. It preserves the workflow proof bundle reviewer checklist dashboard runtime smoke at `docs/review/workflow-proof-bundle-reviewer-checklist-dashboard-runtime-smoke.md` and the report markdown local inspection paths proof chain as predecessor inspection proof. This is reviewer routing only; it is not new runtime evidence, not external reviewer feedback, not hosted deployment evidence, not distributed tracing, not hosted observability, not semantic retrieval quality evidence, not embedding generation, not Evidence Ledger quality evidence, not Noise Gate quality evidence, not report quality evidence, and not product-complete.

Focused recent intake proof: `docs/review/external-reader-proof-path-encrypted-pdf-handoff-ops-route-refresh.md` now routes reviewers to `docs/review/uploaded-pdf-encrypted-failure-candidate-handoff-ops.md`, `docs/review/uploaded-pdf-encrypted-failure-candidate-handoff-ops-runtime-smoke.md`, and `docs/review/uploaded-pdf-encrypted-failure-candidate-handoff-ops-remote-verification.md`. It surfaces `pdf_encrypted_failure_candidate_count` / `PDF Encrypted Failure Candidates` as password-protected PDF failure metadata in operations views. External-reader proof path encrypted PDF handoff ops route refresh v0: implemented. This is focused route alignment only; it is not new runtime evidence, not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not robust PDF extraction, not decryption, and not product-complete.

Latest focused intake route remote verification: `docs/review/external-reader-proof-path-encrypted-pdf-handoff-ops-route-refresh-remote-verification.md` records that commit `f94b06e80423565775c7da658f62c15028dabf38` passed CI run `27057767562` and External Feedback Screen run `27057767542`. External-reader proof path encrypted PDF handoff ops route refresh remote verification v0: implemented. This is remote workflow evidence only, not external reviewer feedback, not hosted deployment evidence, not robust PDF extraction, not decryption, and not product-complete.

Latest focused intake issue routing: `docs/review/external-review-issue-body-encrypted-pdf-handoff-ops-route-refresh.md` records that issue #1 now includes the uploaded PDF encrypted handoff ops proof chain while preserving the workflow markdown proof as the latest primary proof. External review issue body encrypted PDF handoff ops route refresh v0: implemented. This is owner-authored issue routing only, not external reviewer feedback, not hosted deployment evidence, and not product-complete.

Latest external-feedback screen after focused intake issue routing: `docs/review/external-feedback-current-state-encrypted-pdf-handoff-ops-issue-verification.md` records `status: pending`, `candidate_count: 0`, and `reason: self_authored_comment` after issue #1 was refreshed. External feedback current-state encrypted PDF handoff ops issue verification v0: implemented. This is current-state issue screening only, not external reviewer feedback, not hosted deployment evidence, and not product-complete.

Latest focused intake manual handoff runtime proof: `docs/review/uploaded-pdf-encrypted-failure-candidate-manual-handoff-runtime-smoke.md` records that an encrypted uploaded PDF can move from persisted document `failure_case_candidate` into `POST /documents/{document_id}/failure-case-draft-preview`, then into `POST /failure-cases` only after human confirmation. Uploaded PDF encrypted failure candidate manual handoff runtime smoke v0: verified. This is local runtime evidence only, not automatic failure-case creation, not hosted deployment evidence, not robust PDF extraction, not decryption, and not product-complete.

Latest focused intake manual handoff remote verification: `docs/review/uploaded-pdf-encrypted-failure-candidate-manual-handoff-runtime-smoke-remote-verification.md` records that commit `2bafa95d3d282337cd442438018c4736883d8c92` passed CI run `27058294029` and External Feedback Screen run `27058294024`. Uploaded PDF encrypted failure candidate manual handoff runtime smoke remote verification v0: verified. This is remote workflow evidence only, not external reviewer feedback, not hosted deployment evidence, and not product-complete.

Latest focused intake manual handoff issue routing: `docs/review/external-review-issue-body-encrypted-pdf-manual-handoff-route-refresh.md` records that issue #1 now includes the uploaded PDF encrypted manual handoff proof and its remote verification while preserving the workflow markdown latest proof. External review issue body encrypted PDF manual handoff route refresh v0: implemented. This is owner-authored issue routing only, not external reviewer feedback, not hosted deployment evidence, and not product-complete.

Latest external-feedback screen after manual handoff issue routing: `docs/review/external-feedback-current-state-encrypted-pdf-manual-handoff-issue-verification.md` records `status: pending`, `candidate_count: 0`, and `reason: self_authored_comment` after issue #1 was refreshed with the uploaded PDF encrypted manual handoff proof route. External feedback current-state encrypted PDF manual handoff issue verification v0: implemented. This is current-state issue screening only, not external reviewer feedback, not hosted deployment evidence, and not product-complete.

Latest recorded remote verification state: the external-reader workflow markdown route refresh commit `2c5fd10a990887cd6baeb288aa7c83918dc303ba` passed CI run `27055679959` and External Feedback Screen run `27055679968`; see `docs/review/external-reader-proof-path-workflow-markdown-runtime-route-refresh-remote-verification.md`. This is workflow evidence only, not external feedback, not hosted deployment evidence, not semantic retrieval quality evidence, not embedding generation, not Evidence Ledger quality evidence, not Noise Gate quality evidence, not report quality evidence, and not hosted runtime product proof.

Historical predecessor route remote verification compatibility: the workflow proof bundle markdown export runtime smoke documentation commit `4e6112694dfd8649006512c4614424e03801f8fb` passed CI run `27055470517` and External Feedback Screen run `27055470521`. This is archived workflow evidence only, not external feedback, not hosted deployment evidence, not semantic retrieval quality evidence, not embedding generation, not Evidence Ledger quality evidence, not Noise Gate quality evidence, not report quality evidence, and not hosted runtime product proof.

Historical predecessor route remote verification compatibility: the external-reader proof path workflow checklist dashboard runtime route refresh commit `264d99a592fb9f050570d3239c1cf17a41c6e6bc` passed CI run `27054455690` and External Feedback Screen run `27054455683`; see `docs/review/external-reader-proof-path-workflow-checklist-dashboard-runtime-route-refresh-remote-verification.md`. This is archived workflow evidence only, not external feedback, not hosted deployment evidence, not semantic retrieval quality evidence, not embedding generation, not Evidence Ledger quality evidence, not Noise Gate quality evidence, not report quality evidence, and not hosted runtime product proof.

Historical predecessor remote verification compatibility: the workflow checklist dashboard runtime smoke commit `9c8db9d1e9a6660729bf2861b0a27879340ce049` passed CI run `27054251119` and External Feedback Screen run `27054251122`. This remains archived workflow evidence only, not external feedback, not hosted deployment evidence, and not runtime product proof.

Historical predecessor route compatibility: Latest proof routing now points reviewers to the report markdown local inspection paths proof at `docs/review/report-markdown-local-inspection-paths.md`, plus `docs/review/report-markdown-local-inspection-paths-runtime-smoke.md` and `docs/review/report-markdown-local-inspection-paths-runtime-smoke-remote-verification.md`. This remains predecessor report-inspection proof, not the current first route.

Historical predecessor remote verification compatibility: Latest recorded remote verification state: the report markdown local inspection issue verification was remotely checked by CI run `27052979808` and External Feedback Screen run `27052979809`; see `docs/review/external-feedback-current-state-report-markdown-local-inspection-issue-verification-remote-verification.md`. This remains archived workflow evidence only, not external feedback, not hosted deployment evidence, and not runtime product proof.

Latest repository push verification state: Phase 654 artifact commit `5dd5b246a6f562ca5fcc5377c24e7b25170461ce` passed CI run `27053207711` and External Feedback Screen run `27053207694`. This verifies the current pushed repository state, not external reviewer feedback, not hosted deployment evidence, and not product-complete behavior.

Runtime persistence verification: done; see `docs/review/runtime-persistence-verification.md`. This is local Docker/FastAPI/PostgreSQL evidence only, not hosted deployment evidence or product-complete.

Latest external-feedback state: pending after workflow markdown issue verification; candidate_count=0; draft_count=0; self-authored comment only.

Latest external-feedback remote workflow check: Phase 671 current-state workflow markdown issue verification commit `ea58f7ecedb2d0f3a5e839d6ba2c62def3e1bee4` passed CI run `27056276600` and External Feedback Screen run `27056276610`. This is remote workflow evidence only, not external reviewer feedback, not hosted deployment evidence, and not product-complete behavior.

Historical predecessor feedback compatibility: Latest external-feedback state: pending after workflow checklist dashboard runtime issue verification; candidate_count=0; draft_count=0; self-authored comment only.

Historical predecessor feedback compatibility: Latest external-feedback state: pending after workflow checklist dashboard runtime issue-body refresh; candidate_count=0; draft_count=0; self-authored comment only.

Historical predecessor feedback compatibility: Latest external-feedback state: pending after workflow checklist dashboard runtime route refresh; candidate_count=0; draft_count=0; self-authored comment only.

Historical predecessor feedback compatibility: Latest external-feedback state: pending after report markdown local inspection issue verification; candidate_count=0; draft_count=0; self-authored comment only.

Issue screen baseline: issue #1 starts with `## Request`, first codepoint `35`, no leading BOM, `candidate_count=0`, and `draft_count=0`. The older BOM-removal workflow runs remain archived as request-surface hygiene, not the current proof route, not external reviewer feedback, not hosted deployment evidence, and not product-complete.

## What This Is

NoiseProof Agent is a planned RAG/agent service for market intelligence work where the input data is inconsistent, noisy, and difficult to trust.

Current implemented capability groups:

- service skeleton, metadata persistence, PostgreSQL schema, migration runner, and CI
- document profiling, parser boundaries, uploaded digital PDF text extraction, chunk strategy comparison, and lexical retrieval
- deterministic embedding preview, collection planning, Evidence Ledger, Noise Gate, and report markdown exports
- persisted evidence/gate/report records, trace lookup, filters, workflow parents, and derived lineage
- trace headers, ops dashboard, failure-case persistence, stage events, manual provenance, and proof paths

Detailed phase history lives in `docs/GOAL.md`, `docs/application/portfolio-index.md`, and the phase-specific `docs/review/*` artifacts. This README now keeps the first-pass narrative focused on what the project currently demonstrates and what it still does not claim.
The product thesis:

> A good data agent does not start by answering well. It starts by preventing unsupported answers from passing.

## What This Is Not

NoiseProof Agent is not a trading bot.

This repository will not build:

- buy/sell signals
- automatic order execution
- return prediction
- stock recommendations
- financial advice
- real-time trading infrastructure
- reinforcement-learning trading logic
- a large-scale data lake
- a multi-tenant SaaS v1
- polished UI before evidence, logging, and evaluation work

Correct questions for this system:

- What happened?
- What evidence supports it?
- Which sources conflict?
- Which claims are weak?
- What data is missing?
- Why should this conclusion not be trusted yet?

Incorrect questions for this system:

- Should I buy?
- Should I sell?
- What is the target price?
- How much return will this make?

## Why This Exists

Market intelligence work often starts with mixed inputs: PDFs, CSVs, news pages, internal notes, reports, and stale or conflicting sources. LLMs can turn that mess into a confident answer too quickly.

NoiseProof Agent is designed to make unsupported answers harder to pass. The main artifact is not a fluent answer. The main artifact is an inspectable trail: source profiles, retrieval runs, evidence spans, contradictions, blocked claims, limitations, run logs, and failure cases.

## Target User Problem

The target user is a market researcher, analyst, founder, or operator who needs to read messy market material without accidentally treating weak evidence as a strong conclusion.

They need a system that can:

- ingest mixed document formats
- profile source quality
- compare chunk strategies
- retrieve source-linked evidence
- record which claims are supported, weak, contradicted, unsupported, or blocked
- show why a final report should or should not be trusted

## Planned Architecture

```text
Source Upload / URL Input
  -> Document Profiler
  -> Parser Selector
  -> Chunk Strategy Experiment
  -> Collection Plan Preview
  -> Indexing
  -> Retrieval
  -> Evidence Ledger
  -> Analysis Draft
  -> Critic / Noise Gate
  -> Claim-bounded Report
  -> Run Log / Failure Case
```

Implementation status:

Current status groups:

- docs: briefs, ADRs, runbook, review artifacts
- service: health, ops/dashboard, routes, migrations, CI
- ingestion/RAG: profiles, parsers, chunks, retrieval, collection plans
- evidence/report: ledgers, gates, reports, traces, filters
- proof: runtime smokes, reviewer routes, feedback screen

Latest proof routing marker: Report markdown local inspection paths proof route v0.
Latest runtime proof marker: Report markdown local inspection paths runtime smoke v0.
Latest workflow dashboard marker: failure-case workflow dashboard proofs summarized below.
Latest product gate marker: Report markdown local inspection paths v0: implemented.
Latest external-feedback state: pending after report markdown local inspection issue verification; candidate_count=0; draft_count=0; self-authored comment only.
Latest remote workflow check: Phase 654 artifact commit `5dd5b246a6f562ca5fcc5377c24e7b25170461ce` passed CI run `27053207711` and External Feedback Screen run `27053207694`.
Latest status-coherence marker: README top current-state coherence refresh v0.

Detailed implementation history remains in the lower detailed Implementation Status section, `docs/GOAL.md`, and phase-specific `docs/review/*`.

Still planned/unclaimed near the top:

- polished web UI
- robust PDF extraction
- robust PDF extraction implementation; source-first strategy review exists at `docs/review/robust-pdf-extraction-source-first-strategy-review.md`
- upload-preview auto-persistence
- embedding generation, vector quality evidence, LLM calls
- hosted deployment evidence
- local token guard exists; production auth/identity unclaimed
- production background workers and complete causality
- free-form reports

## Implementation Status

Major implementation milestones:
- README proof-marker archive review v0: implemented
- README proof-marker archive extraction v0: implemented
- README proof-marker archive application refresh v0: implemented
- README proof-marker archive external path review v0: implemented
- README proof-marker archive external path refresh v0: implemented
- Application current-claim compression review v0: implemented
- Application current-claim compression v0: implemented
- Braincrew role-map runtime proof compression review v0: implemented
- Braincrew role-map runtime proof compression v0: implemented
- Application proof surface final scan review v0: implemented
- Application-ready summary compression v0: implemented
- External-reader final proof-path dry-read review v0: implemented
- External-reader proof path next-gate refresh v0: implemented
- Application package final consistency review v0: implemented
- Portfolio site handoff review v0: implemented
- Portfolio site proof artifact route verification v0: implemented
- Demo transcript capture v0: implemented
- Local browser screenshot walkthrough v0: implemented
- External review request packet v0: implemented
- External feedback intake criteria v0: implemented
- External reviewer brief v0: implemented
- External reviewer live proof route refresh v0: implemented
- External reviewer link map v0: implemented
- External review root guide v0: implemented
- External review issue body encoding verification v0: implemented
- External review issue body root-guide verification v0: implemented
- External review issue body link-map verification v0: implemented
- External review issue template link-map refresh v0: implemented
- External review issue label verification v0: implemented
- External review owner request comment verification v0: implemented
- External reviewer outreach packet v0: implemented
- External feedback qualification preview v0: implemented
- External feedback screening CLI v0: implemented
- External feedback screening workflow v0: implemented
- External feedback screening workflow verification v0: implemented
- Owner-approved product continuation decision v0: implemented
- File upload preview v0: implemented
- Uploaded file chunk preview v0: implemented
- Uploaded file retrieval preview v0: implemented
- Uploaded file Evidence Ledger preview v0: implemented
- Uploaded file Noise Gate preview v0: implemented
- Uploaded file report preview v0: implemented
- Uploaded file failure-case draft preview v0: implemented
- Uploaded file failure-case manual handoff smoke v0: implemented
- Uploaded file proof path index refresh v0: implemented
- Uploaded file runtime smoke packet v0: implemented
- Persisted uploaded file intake review v0: implemented
- Uploaded file intake manifest preview v0: implemented
- Uploaded file intake manifest runtime smoke v0: implemented
- Uploaded file intake manifest application refresh v0: implemented
- Uploaded file intake manifest persistence schema v0: implemented
- Uploaded file intake manifest persistence repository review v0: implemented
- Uploaded file intake manifest persistence repository v0: implemented
- Uploaded file intake manifest persistence endpoint review v0: implemented
- Uploaded file intake manifest persistence endpoint v0: implemented
- Uploaded file intake manifest persistence runtime smoke v0: implemented
- Uploaded file intake manifest persistence application refresh v0: implemented
- Uploaded file parsed document persistence v0: implemented
- Uploaded file parsed document persistence runtime smoke v0: implemented
- Uploaded file parsed document persistence application refresh v0: implemented
- External reviewer parsed-document persistence request refresh v0: implemented
- External reviewer parsed-document persistence issue-body refresh v0: implemented
- Uploaded file chunk persistence review v0: implemented
- Uploaded file chunk persistence schema v0: implemented
- Uploaded file chunk persistence repository v0: implemented
- Uploaded file chunk persistence runtime smoke v0: implemented
- Uploaded file chunk persistence application refresh v0: implemented
- Uploaded file retrieval persistence application refresh v0: implemented
- Embedding endpoint runtime smoke v0: implemented
- Semantic retrieval persistence endpoint v0: implemented
- Semantic retrieval persistence runtime smoke v0: implemented
- Semantic retrieval persistence application refresh v0: implemented

For exhaustive phase history, use `docs/GOAL.md`.

Not implemented yet:

- robust PDF extraction
- production authorization for stored raw uploads
- production malware scanning evidence for stored raw uploads
- implicit upload-preview auto-persistence; explicit uploaded-file-to-chunks handoff exists through `POST /documents/upload-chunks`
- autonomous workflow execution endpoints
- production background failure-case workers, retry automation, and root-cause automation; local v0 workflow failure auto failure-case creation exists inside `POST /workflow-runs/execute-preview`
- embedding generation and vector search quality evidence beyond the deterministic local hash preview
- full distributed tracing or hosted observability

Historical latest-marker compatibility: Latest proof-boundary marker: Architecture ClamAV proof boundary refresh v0.
Historical latest-marker compatibility: Latest external-feedback state: pending after workflow failure auto-created dashboard runtime issue verification; candidate_count=0; self-authored comment only.
Historical latest-marker compatibility: Latest workflow dashboard runtime marker: Workflow failure auto-created failure-case dashboard runtime smoke v0
Historical latest-marker compatibility: README top current-state coherence refresh v0: implemented
Historical latest-marker compatibility: Workflow proof bundle reviewer checklist v0: implemented
Historical latest-marker compatibility: Workflow proof bundle reviewer checklist dashboard discovery v0: implemented
Historical latest-marker compatibility: Workflow proof bundle reviewer checklist dashboard discovery remote verification v0: implemented
Historical latest-marker compatibility: Workflow proof bundle reviewer checklist dashboard runtime smoke v0: implemented
Historical latest-marker compatibility: External-reader proof path workflow checklist dashboard runtime route refresh remote verification v0: implemented
Historical latest-marker compatibility: External review issue body workflow checklist dashboard runtime route refresh v0: implemented
Historical latest-marker compatibility: External feedback current-state workflow checklist dashboard runtime issue verification v0: implemented
Historical latest-marker compatibility: External feedback current-state workflow checklist dashboard runtime issue verification remote verification v0: implemented
Historical latest-marker compatibility: Workflow proof bundle markdown export v0: implemented
Historical latest-marker compatibility: Workflow proof bundle markdown export runtime smoke v0: implemented
Historical latest-marker compatibility: External-reader proof path workflow markdown runtime route refresh v0: implemented
Historical latest-marker compatibility: External-reader proof path workflow markdown runtime route refresh remote verification v0: implemented
Historical latest-marker compatibility: External review issue body workflow markdown runtime route refresh v0: implemented
Historical latest-marker compatibility: External feedback current-state workflow markdown issue verification v0: implemented
Historical latest-marker compatibility: External feedback current-state workflow markdown issue verification remote verification v0: implemented
Historical latest-marker compatibility: Latest external-feedback state: pending after persisted document failure candidate manual handoff issue verification; candidate_count=0; self-authored comment only.
Historical latest-marker compatibility: Latest runtime proof marker: Report markdown stage input links runtime smoke v0.
Historical latest-marker compatibility: Latest runtime proof marker: Report markdown source provenance export runtime smoke v0.
Historical latest-marker compatibility: Latest runtime proof marker: Workflow failure auto failure-case creation runtime smoke v0.
Historical latest-marker compatibility: Latest workflow dashboard runtime marker: Workflow dashboard failure-case counts runtime smoke v0: implemented.
Historical latest-marker compatibility: Latest product gate marker: Report markdown stage input links v0: implemented.
Historical latest-marker compatibility: Latest product gate marker: Report markdown source provenance export v0: implemented.
Historical latest-marker compatibility: Latest product gate marker: Retrieval run semantic provenance inspectability v0: implemented.
Historical latest-marker compatibility: Latest product gate marker: Workflow failure auto failure-case creation v0: implemented.
Historical latest-marker compatibility: Latest reviewer-routing marker: Persisted document failure candidate manual handoff runtime issue-body refresh v0.
Historical latest-marker compatibility: Latest external-feedback state: pending after workflow failure auto-creation runtime issue verification; candidate_count=0; self-authored comment only.

Retrieval run semantic provenance runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP verified `GET /retrieval-runs` returns `is_semantic_retrieval_run=true`, `retrieval_mode=semantic_persisted`, `query_vector_source=caller_provided_vector`, and `persistence_boundary=semantic_retrieval_run_only_no_evidence_ledger`, while `GET /ops/dashboard` renders `Retrieval Mode`, `Query Vector Source`, and `Persistence Boundary`. This is local read-surface runtime evidence only, not embedding generation, semantic retrieval quality evidence, hosted deployment evidence, external reviewer feedback, or product-complete.

Retrieval run semantic provenance runtime smoke remote verification v0: implemented. Boundary: CI run `27043472010` and External Feedback Screen run `27043472009` succeeded on head `31af13a55399a0f5526a3523f035a7ab5c16fa78`; this is remote workflow verification only, not external reviewer feedback, hosted deployment evidence, semantic retrieval quality evidence, or product-complete.

External review issue body retrieval run semantic provenance runtime refresh v0: implemented. Boundary: issue #1 now points reviewers to `docs/review/retrieval-run-semantic-provenance-runtime-smoke.md`, `docs/review/retrieval-run-semantic-provenance-runtime-smoke-remote-verification.md`, and `docs/review/external-review-issue-body-retrieval-run-semantic-provenance-runtime-refresh.md`; this is owner-authored issue body routing only, not external reviewer feedback, hosted deployment evidence, semantic retrieval quality evidence, embedding generation, or product-complete.

External feedback current-state retrieval run semantic provenance issue verification v0: implemented. Boundary: issue #1 still has only owner-authored feedback after the retrieval run semantic provenance issue-body refresh, with `candidate_count=0`, `draft_count=0`, `reason=self_authored_comment`, and `status=pending`; this is current-state issue screening only, not external reviewer feedback, hosted deployment evidence, semantic retrieval quality evidence, embedding generation, or product-complete.

External feedback current-state retrieval run semantic provenance issue verification remote verification v0: implemented. Boundary: CI run `27044739630` and External Feedback Screen run `27044739628` succeeded on head `4e58ebe228cd3d4e9d0573e393cfdd0ef04d0dc1`; external reviewer feedback v0 remains pending with `candidate_count=0`, `draft_count=0`, and `reason=self_authored_comment`. This is remote workflow verification only, not external reviewer feedback, hosted deployment evidence, semantic retrieval quality evidence, embedding generation, or product-complete.

Retrieval-run-linked Evidence Ledger semantic source provenance v0: implemented. Boundary: `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger` now preserves source retrieval provenance from semantic persisted runs in response warnings, stored Evidence Ledger entry metadata, listed Evidence Ledger rows, and agent-run trace metadata. This is route-level source-provenance preservation only, not semantic retrieval quality evidence, embedding generation, Evidence Ledger quality evidence, hosted deployment evidence, external reviewer feedback, or product-complete.

Retrieval-run-linked Evidence Ledger semantic source provenance runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP verified semantic persisted retrieval-run provenance survives into Evidence Ledger warnings, stored entry metadata, listed rows, and agent-run trace metadata, including `handoff_performs_semantic_retrieval=false`. This is local runtime source-provenance evidence only, not semantic retrieval quality evidence, embedding generation, Evidence Ledger quality evidence, hosted deployment evidence, external reviewer feedback, or product-complete.

Retrieval-run-linked Evidence Ledger semantic source provenance runtime smoke remote verification v0: implemented. Boundary: CI run `27045552652` and External Feedback Screen run `27045552666` succeeded on head `27b8ab349604defe5543a43627df730fd72c6383`; this is remote workflow verification only, not the local runtime smoke itself, semantic retrieval quality evidence, embedding generation, Evidence Ledger quality evidence, hosted deployment evidence, external reviewer feedback, or product-complete.

External review issue body retrieval-run-linked Evidence Ledger semantic source provenance runtime refresh v0: implemented. Boundary: issue #1 now routes reviewers to `docs/review/retrieval-run-linked-evidence-ledger-semantic-source-provenance.md`, `docs/review/retrieval-run-linked-evidence-ledger-semantic-source-provenance-runtime-smoke.md`, and `docs/review/retrieval-run-linked-evidence-ledger-semantic-source-provenance-runtime-smoke-remote-verification.md`; this is owner-authored issue body routing only, not external reviewer feedback, hosted deployment evidence, semantic retrieval quality evidence, embedding generation, Evidence Ledger quality evidence, or product-complete.

External feedback current-state retrieval-run-linked Evidence Ledger semantic source provenance issue verification v0: implemented. Boundary: issue #1 still has only owner-authored feedback after the semantic source provenance issue-body refresh, with `candidate_count=0`, `draft_count=0`, `reason=self_authored_comment`, and `status=pending`; this is current-state issue screening only, not external reviewer feedback, hosted deployment evidence, semantic retrieval quality evidence, embedding generation, Evidence Ledger quality evidence, or product-complete.

External feedback current-state retrieval-run-linked Evidence Ledger semantic source provenance issue verification remote verification v0: implemented. Boundary: CI run `27046055674` and External Feedback Screen run `27046055690` succeeded on head `af50f77563c270131eefd2ce75dbbf197c584b16`; external reviewer feedback remains pending with `candidate_count=0`, `draft_count=0`, and `reason=self_authored_comment`. This is remote workflow verification only, not external reviewer feedback, hosted deployment evidence, semantic retrieval quality evidence, embedding generation, Evidence Ledger quality evidence, or product-complete.

README latest-marker semantic source provenance current-state refresh v0: implemented. Boundary: the README External Reviewer Fast Path now points first-pass readers to the retrieval-run-linked Evidence Ledger semantic source provenance proof chain and the latest recorded issue-screen remote verification. This is README current-state alignment only, not external reviewer feedback, hosted deployment evidence, semantic retrieval quality evidence, embedding generation, Evidence Ledger quality evidence, or product-complete.

README fast-path issue screen baseline cleanup v0: implemented. Boundary: the README External Reviewer Fast Path now presents the issue #1 readability/BOM state as a baseline instead of three stale `Latest issue-*` markers. This is first-pass copy hygiene only, not a new issue edit, not external reviewer feedback, not hosted deployment evidence, and not product-complete.

External-reader proof path semantic source provenance route refresh v0: implemented. Boundary: `docs/review/external-reader-proof-path.md` now starts its current proof route with the retrieval-run-linked Evidence Ledger semantic source provenance proof chain while preserving older report/table proof paths as specialized or historical records. This is reader-route alignment only, not new runtime evidence, not external reviewer feedback, not hosted deployment evidence, not semantic retrieval quality evidence, not Evidence Ledger quality evidence, and not product-complete.

Retrieval-run-linked Gate/Report semantic source provenance v0: implemented. Boundary: `POST /retrieval-runs/{retrieval_run_id}/noise-gate` and `POST /retrieval-runs/{retrieval_run_id}/report` now preserve source retrieval provenance from linked Evidence Ledger row metadata in warnings, stage input manifests, and agent-run traces. This is deterministic route-level provenance preservation only, not semantic retrieval quality evidence, embedding generation, Evidence Ledger quality evidence, Noise Gate quality evidence, report quality evidence, hosted deployment evidence, external reviewer feedback, or product-complete.

Retrieval-run-linked Gate/Report semantic source provenance runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP verified semantic persisted retrieval-run provenance survives through Evidence Ledger metadata into downstream Noise Gate and Report warnings, stage input manifests, and agent-run traces, with `handoff_performs_semantic_retrieval=false`. This is local runtime source-provenance handoff evidence only, not semantic retrieval quality evidence, embedding generation, Evidence Ledger quality evidence, Noise Gate quality evidence, report quality evidence, hosted deployment evidence, external reviewer feedback, or product-complete.

Retrieval-run-linked Gate/Report semantic source provenance runtime smoke remote verification v0: implemented. Boundary: CI run `27048811299` and External Feedback Screen run `27048811288` succeeded on head `7e7995ff5657a8c970683ce6dd0afea1dd350c48`; this is remote workflow verification only, not the local runtime smoke itself, semantic retrieval quality evidence, embedding generation, Evidence Ledger quality evidence, Noise Gate quality evidence, report quality evidence, hosted deployment evidence, external reviewer feedback, or product-complete.

External-reader proof path Gate/Report semantic source provenance route refresh v0: implemented. Boundary: `docs/review/external-reader-proof-path.md` and the README External Reviewer Fast Path now start first-pass readers with the retrieval-run-linked Gate/Report semantic source provenance proof chain while preserving the Evidence Ledger chain as predecessor handoff proof. This is reader-route alignment only, not new runtime evidence, not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not semantic retrieval quality evidence, not embedding generation, not Evidence Ledger quality evidence, not Noise Gate quality evidence, not report quality evidence, and not product-complete.

External-reader proof path Gate/Report semantic source provenance route refresh remote verification v0: implemented. Boundary: CI run `27049168693` and External Feedback Screen run `27049168679` succeeded on head `1b5514d8943e8971e95766a758dd30133a809a88`; this is remote workflow verification only, not the reader-route refresh itself, not a new runtime smoke, not semantic retrieval quality evidence, not embedding generation, not Evidence Ledger quality evidence, not Noise Gate quality evidence, not report quality evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

External review issue body Gate/Report semantic source provenance runtime refresh v0: implemented. Boundary: issue #1 now points reviewers to `docs/review/retrieval-run-linked-gate-report-semantic-source-provenance.md`, `docs/review/retrieval-run-linked-gate-report-semantic-source-provenance-runtime-smoke.md`, `docs/review/retrieval-run-linked-gate-report-semantic-source-provenance-runtime-smoke-remote-verification.md`, and `docs/review/external-review-issue-body-gate-report-semantic-source-provenance-runtime-refresh.md`; this is owner-authored issue body routing only, not external reviewer feedback, hosted deployment evidence, semantic retrieval quality evidence, embedding generation, Evidence Ledger quality evidence, Noise Gate quality evidence, report quality evidence, final truth adjudication, or product-complete.

External feedback current-state Gate/Report semantic source provenance issue verification v0: implemented. Boundary: issue #1 still has only owner-authored feedback after the Gate/Report semantic source provenance issue-body refresh, with `candidate_count=0`, `draft_count=0`, `reason=self_authored_comment`, and `status=pending`; this is current-state issue screening only, not external reviewer feedback, hosted deployment evidence, semantic retrieval quality evidence, embedding generation, Evidence Ledger quality evidence, Noise Gate quality evidence, report quality evidence, or product-complete.

External feedback current-state Gate/Report semantic source provenance issue verification remote verification v0: implemented. Boundary: CI run `27049669832` and External Feedback Screen run `27049669830` succeeded on head `213274f59d730ed840b6a103858df7aaa85b96c9`; external reviewer feedback remains pending with `candidate_count=0`, `draft_count=0`, and `reason=self_authored_comment`. This is remote workflow verification only, not external reviewer feedback, hosted deployment evidence, semantic retrieval quality evidence, embedding generation, Evidence Ledger quality evidence, Noise Gate quality evidence, report quality evidence, or product-complete.

Report markdown source provenance export v0: implemented. Boundary: `GET /reports/{report_record_id}/markdown` now renders a `Source Retrieval Provenance` section from the persisted Report `stage_input_manifest`, including `source_retrieval_mode`, `source_query_vector_source`, `source_is_semantic_retrieval_run`, `source_retrieval_persistence_boundary`, and `handoff_performs_semantic_retrieval`. This is deterministic read-surface inspectability only, not a new report-generation path, not free-form report generation, not an LLM call, not retrieval execution, not semantic retrieval quality evidence, not embedding generation, not Evidence Ledger quality evidence, not Noise Gate quality evidence, not report quality evidence, not hosted deployment evidence, not external reviewer feedback, or product-complete.

Report markdown source provenance export runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP verified `GET /reports/{report_record_id}/markdown -> HTTP/1.1 200 OK` returned `text/markdown; charset=utf-8` and rendered `## Source Retrieval Provenance`, `Source retrieval mode: semantic_persisted`, `Source query vector source: caller_provided_vector`, and `Handoff performs semantic retrieval: false` after a semantic persisted retrieval-run-linked Evidence Ledger, Noise Gate, and Report flow. This is local runtime read-surface evidence only, not hosted deployment evidence, semantic retrieval quality evidence, embedding generation, Evidence Ledger quality evidence, Noise Gate quality evidence, report quality evidence, external reviewer feedback, or product-complete.

Report markdown source provenance export runtime smoke remote verification v0: implemented. Boundary: CI run `27050315671` and External Feedback Screen run `27050315683` succeeded on head `4e75c645e26f1c2a8cc433529b4a7e3f3f214cf2`; this is remote workflow verification only, not the local runtime smoke itself, hosted deployment evidence, semantic retrieval quality evidence, embedding generation, Evidence Ledger quality evidence, Noise Gate quality evidence, report quality evidence, external reviewer feedback, or product-complete.

Report markdown stage input links v0: implemented. Boundary: `GET /reports/{report_record_id}/markdown` now renders `## Stage Input Links` from persisted Report `stage_input_manifest`, including retrieval run id, Evidence Ledger entry ids, and Noise Gate record id when present. This is deterministic markdown read-surface inspectability only, not new retrieval, Evidence Ledger creation, Noise Gate creation, report generation, an LLM call, embedding generation, semantic retrieval quality evidence, Evidence Ledger quality evidence, Noise Gate quality evidence, report quality evidence, hosted deployment evidence, external reviewer feedback, or product-complete.

Report markdown stage input links runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP verified `GET /reports/{report_record_id}/markdown -> HTTP/1.1 200 OK` returned `text/markdown; charset=utf-8` and rendered `## Stage Input Links`, the retrieval run id, two Evidence Ledger entry ids, and the Noise Gate record id from persisted Report `stage_input_manifest`. This is local runtime read-surface evidence only, not hosted deployment evidence, semantic retrieval quality evidence, embedding generation, Evidence Ledger quality evidence, Noise Gate quality evidence, report quality evidence, external reviewer feedback, or product-complete.

Report markdown stage input links runtime smoke remote verification v0: implemented. Boundary: CI run `27051217722` and External Feedback Screen run `27051217725` succeeded on head `633c2c35000bd9098b18e5f4108d61dd6099c4f1`; this is remote workflow verification only, not the local runtime smoke itself, hosted deployment evidence, semantic retrieval quality evidence, embedding generation, Evidence Ledger quality evidence, Noise Gate quality evidence, report quality evidence, external reviewer feedback, or product-complete.

Report markdown local inspection paths v0: implemented. Boundary: `GET /reports/{report_record_id}/markdown` now renders `## Local Inspection Paths` with deterministic local GET surfaces for the current report markdown export, report workflow-trace filter, trace lookup, retrieval-run list, Evidence Ledger list, and Noise Gate list. This is markdown read-surface inspectability only, not new record creation, not new retrieval behavior, not Evidence Ledger creation, not Noise Gate creation, not report generation, not an LLM call, not embedding generation, not semantic retrieval quality evidence, not Evidence Ledger quality evidence, not Noise Gate quality evidence, not report quality evidence, not hosted deployment evidence, not external reviewer feedback, or product-complete.

Report markdown local inspection paths runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP verified `GET /reports/{report_record_id}/markdown -> HTTP/1.1 200 OK` returned `text/markdown; charset=utf-8` and rendered `## Local Inspection Paths`, current report markdown path, current report workflow-trace filter, current workflow trace path, retrieval-run list path, Evidence Ledger list path, and Noise Gate list path after a semantic persisted retrieval-run-linked Evidence Ledger, Noise Gate, and Report flow. This is local runtime read-surface evidence only, not hosted deployment evidence, semantic retrieval quality evidence, embedding generation, Evidence Ledger quality evidence, Noise Gate quality evidence, report quality evidence, external reviewer feedback, or product-complete.

Report markdown local inspection paths runtime smoke remote verification v0: implemented. Boundary: CI run `27051818097` and External Feedback Screen run `27051818098` succeeded on head `10f330cce3fd093fe4160574c6f3af83d26856c0`; this is remote workflow verification only, not the local runtime smoke itself, hosted deployment evidence, semantic retrieval quality evidence, embedding generation, Evidence Ledger quality evidence, Noise Gate quality evidence, report quality evidence, external reviewer feedback, or product-complete.

External-reader proof path report markdown local inspection route refresh v0: implemented. Boundary: `docs/review/external-reader-proof-path.md` and the README External Reviewer Fast Path now start first-pass readers with the report markdown local inspection paths proof chain while preserving the Gate/Report semantic source provenance chain as predecessor proof. This is reader-route alignment only, not new runtime evidence, not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not semantic retrieval quality evidence, not embedding generation, not Evidence Ledger quality evidence, not Noise Gate quality evidence, not report quality evidence, or product-complete.

External-reader proof path report markdown local inspection route refresh remote verification v0: implemented. Boundary: CI run `27052319517` and External Feedback Screen run `27052319510` succeeded on head `cd2ab79a72f27c51c4aee3534b5ffdb666fee683`; this is remote workflow verification only, not the reader-route refresh itself, not hosted deployment evidence, not external reviewer feedback, not semantic retrieval quality evidence, not embedding generation, not Evidence Ledger quality evidence, not Noise Gate quality evidence, not report quality evidence, not an LLM call, and not product-complete.

External review issue body report markdown local inspection route refresh v0: implemented. Boundary: issue #1 now routes first-pass external reviewers to the report markdown local inspection paths proof chain while preserving Gate/Report semantic source provenance as predecessor proof. This is owner-authored issue body routing only, not external reviewer feedback, not hosted deployment evidence, not semantic retrieval quality evidence, not embedding generation, not Evidence Ledger quality evidence, not Noise Gate quality evidence, not report quality evidence, and not product-complete.

External feedback current-state report markdown local inspection issue verification v0: implemented. Boundary: issue #1 was screened after the report markdown local inspection route refresh; it still has `candidate_count=0`, `draft_count=0`, and only a self-authored issue comment. This is current-state issue screening only, not external reviewer feedback, not hosted deployment evidence, not semantic retrieval quality evidence, not embedding generation, not Evidence Ledger quality evidence, not Noise Gate quality evidence, not report quality evidence, and not product-complete.

External feedback current-state report markdown local inspection issue verification remote verification v0: implemented. Boundary: CI run `27052979808` and External Feedback Screen run `27052979809` succeeded on head `e03329dcd1659fb01bf8b879b817f7514c03295b`; this is remote workflow verification only, not the current-state issue screen itself, not external reviewer feedback, not hosted deployment evidence, not semantic retrieval quality evidence, not embedding generation, not Evidence Ledger quality evidence, not Noise Gate quality evidence, not report quality evidence, and not product-complete.

Workflow direct stage links v0: implemented. Boundary: deterministic workflow-created records now create direct local link rows in `noise_gate_evidence_links`, `report_evidence_links`, and `report_noise_gate_links`, surfaced through `GET /workflow-runs/{id}/lineage` as `direct_stage_links`. Standalone gate/report endpoints remain payload-only unless they create explicit links. This is not distributed tracing, hosted observability, autonomous workflow execution, external reviewer feedback, or product-complete.

Workflow direct stage links runtime smoke v0: implemented. Boundary: local Docker PostgreSQL applied `023_workflow_stage_links.sql`, and live FastAPI HTTP verified `POST /workflow-runs/execute-preview` plus `GET /workflow-runs/{id}/lineage` returned `direct_stage_link_count=3` with `direct_stage_link_table`. This is not hosted deployment evidence, external reviewer feedback, distributed tracing, hosted observability, or product-complete.

Workflow stage event log v0: implemented. Boundary: deterministic `POST /workflow-runs/execute-preview` now records local stage event rows in `workflow_stage_events` for retrieval, Evidence Ledger, Noise Gate, and Report stages, surfaced through `GET /workflow-runs/{id}` and `GET /workflow-runs/{id}/proof-bundle` with `workflow_stage_event_count`. This is local workflow observability only, not distributed tracing, hosted observability, autonomous workflow execution, external reviewer feedback, or product-complete.

Workflow failed stage event v0: implemented. Boundary: deterministic `POST /workflow-runs/execute-preview` failures now record the active failed stage in `workflow_stage_events` with `stage_status=failed`, `error_type`, `error_message`, and `failed_stage_boundary`. This improves local failure inspection only; it is not retry behavior, root-cause automation, hosted observability, external reviewer feedback, or product-complete.

Workflow stage event log runtime smoke v0: implemented. Boundary: local Docker PostgreSQL has `024_workflow_stage_events.sql` applied with `Pending migrations: 0`, and live FastAPI HTTP verified `POST /workflow-runs/execute-preview`, `GET /workflow-runs/{id}`, and `GET /workflow-runs/{id}/proof-bundle` returned `detail_stage_event_count=4` and `bundle_stage_event_count=4`. This is not hosted deployment evidence, external reviewer feedback, distributed tracing, hosted observability, autonomous workflow execution, or product-complete.

Workflow failed stage event runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP verified `POST /workflow-runs/execute-preview -> 500`, `GET /workflow-runs/{id} -> 200`, and `GET /workflow-runs/{id}/proof-bundle -> 200` after a smoke-only CHECK constraint forced the Evidence Ledger stage to fail. Observed `workflow_stage_event_count=2`, `retrieval -> completed`, `evidence_ledger -> failed`, and `failure_case_count_delta -> 0`; this is not retry behavior, automatic failure-case creation, hosted deployment evidence, or product-complete.

External reviewer workflow failed stage event runtime request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to `docs/review/workflow-failed-stage-event-runtime-smoke.md` and `docs/review/external-reviewer-workflow-failed-stage-event-runtime-request-refresh.md`; this is not a live issue body edit, external reviewer feedback, hosted deployment evidence, retry behavior, automatic failure-case creation, distributed tracing, hosted observability, or product-complete.

External review issue body workflow failed stage event runtime refresh v0: implemented. Boundary: issue #1 now points reviewers to `docs/review/workflow-failed-stage-event-runtime-smoke.md`, `docs/review/external-reviewer-workflow-failed-stage-event-runtime-request-refresh.md`, and `docs/review/external-review-issue-body-workflow-failed-stage-event-runtime-refresh.md`; this is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, retry behavior, automatic failure-case creation, distributed tracing, hosted observability, or product-complete.

External feedback current-state workflow failed stage event runtime issue verification v0: implemented. Boundary: current issue #1 points to the failed-stage runtime proof, request refresh, and issue-body refresh while screening still reports `candidate_count=0`, `draft_count=0`, `status=pending`, and `self_authored_comment`; this is not external reviewer feedback, hosted deployment evidence, retry behavior, automatic failure-case creation, or product-complete.

Workflow failure auto failure-case creation v0: implemented. Boundary: route-level tests now verify a failed deterministic workflow preview auto-creates one linked local v0 failure case with `failure_case_count -> 1`, `failed_stage: evidence_ledger`, `workflow_stage_error`, `auto_failure_case_id`, `auto_created_from_workflow_failure_local_v0`, and `local_workflow_stage_failure_event_auto_failure_case_local_v0`; this is not retry behavior, root-cause automation, complete workflow failure causality, Docker runtime smoke, hosted deployment evidence, external reviewer feedback, or product-complete.

Workflow failure auto failure-case creation runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP verified `POST /workflow-runs/execute-preview -> 500` under a smoke-only `smoke_fail_auto_failure_case` constraint, then `GET /workflow-runs/{id}`, `GET /workflow-runs/{id}/proof-bundle`, and `GET /failure-cases?workflow_run_id={id}` surfaced `auto_failure_case_id`, `failure_case_count_delta -> 1`, `detail_failure_case_count -> 1`, `bundle_detail_failure_case_count -> 1`, `filtered_failure_case_count -> 1`, `auto_created_from_workflow_failure_local_v0`, and `local_workflow_stage_failure_event_auto_failure_case_local_v0`; this is not retry behavior, root-cause automation, complete workflow failure causality, hosted deployment evidence, external reviewer feedback, or product-complete.

Workflow failure auto-created failure-case dashboard runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP verified a failed deterministic workflow auto-created one linked local v0 failure case and `GET /ops/dashboard -> 200` surfaced the linked failure-case count/filter, workflow parent link, review queue linked count, and auto-created failure-case id; this is not retry behavior, root-cause automation, complete workflow failure causality, hosted deployment evidence, external reviewer feedback, or product-complete.

External reviewer workflow failure auto-created failure-case dashboard runtime request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to `docs/review/workflow-failure-auto-created-failure-case-dashboard-runtime-smoke.md` and `docs/review/external-reviewer-workflow-failure-auto-created-dashboard-runtime-request-refresh.md`; this is not a live issue body edit, external reviewer feedback, hosted deployment evidence, retry behavior, root-cause automation, complete workflow failure causality, production background worker behavior, or product-complete.

External reviewer workflow failure auto-created failure-case dashboard runtime issue-body refresh v0: implemented. Boundary: issue #1 now points reviewers to `docs/review/workflow-failure-auto-created-failure-case-dashboard-runtime-smoke.md`, `docs/review/external-reviewer-workflow-failure-auto-created-dashboard-runtime-request-refresh.md`, and `docs/review/external-review-issue-body-workflow-failure-auto-created-dashboard-runtime-refresh.md`; this is owner-authored issue body routing only, not external reviewer feedback, hosted deployment evidence, retry behavior, root-cause automation, complete workflow failure causality, production background worker behavior, or product-complete.

External feedback current-state workflow failure auto-created dashboard runtime issue verification v0: implemented. Boundary: current issue #1 points to the workflow failure auto-created dashboard runtime proof, request refresh, and issue-body refresh while screening still reports `candidate_count=0`, `draft_count=0`, `status=pending`, and `self_authored_comment`; this is not external reviewer feedback, hosted deployment evidence, retry behavior, root-cause automation, complete workflow failure causality, production background worker behavior, or product-complete.

Compose project isolation v0: implemented. Boundary: `docker-compose.yml` no longer fixes `container_name`, so `docker compose -p noiseproof-phase595` can create project-scoped containers such as `noiseproof-phase595-db-1`; local runtime smoke verified PostgreSQL accepted connections on `POSTGRES_PORT=55439` and project cleanup completed. This is not hosted deployment evidence, production orchestration, a database migration, or product-complete.

Compose service-name runbook refresh v0: implemented. Boundary: future runtime smoke guidance now tells new smokes to use Compose project names plus service commands such as `docker compose -p <project> ps db`, `docker compose -p <project> ps -q db`, and `docker compose -p <project> exec -T db pg_isready -U noiseproof -d noiseproof`; historical proof docs may still mention old fixed container names because they record prior observations. This is not a new runtime smoke, hosted deployment evidence, production orchestration, or product-complete.

Compose service-name runbook refresh remote verification v0: implemented. Boundary: GitHub Actions verified the Phase 596 documentation gate on head `876291ab45ad839b60ec997511bf15cdee4c8bac` with CI run `27036444352` and External Feedback Screen run `27036444321` both successful. This is remote workflow verification only, not a new runtime smoke, external reviewer feedback, hosted deployment evidence, or product-complete.

README current proof route refresh v0: implemented. Boundary: the first-screen README proof route now points to `docs/review/workflow-failure-auto-created-failure-case-dashboard-runtime-smoke.md`, its reviewer request refresh, and its issue-body refresh record. This is route clarity only, not a new runtime smoke, external reviewer feedback, hosted deployment evidence, retry behavior, root-cause automation, complete workflow failure causality, or product-complete.

README current proof route refresh remote verification v0: implemented. Boundary: GitHub Actions verified the Phase 598 README route clarity gate on head `a715258f044bd9ef3992e513e7e54ab82bfaadf0` with CI run `27036879179` and External Feedback Screen run `27036879137` both successful. This is remote workflow verification only, not a new runtime smoke, external reviewer feedback, hosted deployment evidence, or product-complete.

External reviewer workflow failure auto-creation runtime request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to `docs/review/workflow-failure-auto-failure-case-creation-runtime-smoke.md` and `docs/review/external-reviewer-workflow-failure-auto-creation-runtime-request-refresh.md`; this is not a live issue body edit, external reviewer feedback, hosted deployment evidence, retry behavior, root-cause automation, complete workflow failure causality, or product-complete.

External review issue body workflow failure auto-creation runtime refresh v0: implemented. Boundary: issue #1 now points reviewers to `docs/review/workflow-failure-auto-failure-case-creation-runtime-smoke.md`, `docs/review/external-reviewer-workflow-failure-auto-creation-runtime-request-refresh.md`, and `docs/review/external-review-issue-body-workflow-failure-auto-creation-runtime-refresh.md`; this is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, retry behavior, root-cause automation, complete workflow failure causality, or product-complete.

External feedback current-state workflow failure auto-creation runtime issue verification v0: implemented. Boundary: current issue #1 points to the workflow failure auto-created failure-case runtime proof, request refresh, and issue-body refresh while screening still reports `candidate_count=0`, `draft_count=0`, `status=pending`, and `self_authored_comment`; this is not external reviewer feedback, hosted deployment evidence, retry behavior, root-cause automation, complete workflow failure causality, or product-complete.

External reviewer workflow stage event log runtime request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to `docs/review/workflow-stage-event-log-runtime-smoke.md` and `docs/review/external-reviewer-workflow-stage-event-log-runtime-request-refresh.md`; this is not a live issue body edit, external reviewer feedback, hosted deployment evidence, distributed tracing, hosted observability, autonomous workflow execution, or product-complete.

External review issue body workflow stage event log runtime refresh v0: implemented. Boundary: issue #1 now points reviewers to `docs/review/workflow-stage-event-log-runtime-smoke.md`, `docs/review/external-reviewer-workflow-stage-event-log-runtime-request-refresh.md`, and `docs/review/external-review-issue-body-workflow-stage-event-log-runtime-refresh.md`; this is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, distributed tracing, hosted observability, autonomous workflow execution, or product-complete.

External feedback current-state workflow stage event log runtime issue verification v0: implemented. Boundary: current issue #1 has the workflow stage event log runtime proof, request refresh, and issue-body refresh links, but the only screened comment is owner-authored, `candidate_count=0`, `draft_count=0`, and external reviewer feedback remains pending.

External reviewer workflow direct stage links runtime request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to `docs/review/workflow-direct-stage-links-runtime-smoke.md` and `docs/review/external-reviewer-workflow-direct-stage-links-runtime-request-refresh.md`; this is not a live issue body edit, external reviewer feedback, hosted deployment evidence, distributed tracing, hosted observability, autonomous workflow execution, or product-complete.

External review issue body workflow direct stage links runtime refresh v0: implemented. Boundary: issue #1 now points reviewers to `docs/review/workflow-direct-stage-links-runtime-smoke.md`, `docs/review/external-reviewer-workflow-direct-stage-links-runtime-request-refresh.md`, and `docs/review/external-review-issue-body-workflow-direct-stage-links-runtime-refresh.md`; this is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, distributed tracing, hosted observability, autonomous workflow execution, or product-complete.

External feedback current-state workflow direct stage links runtime issue verification v0: implemented. Boundary: current issue #1 has the workflow direct stage links runtime proof, request refresh, and issue-body refresh links, but the only screened comment is owner-authored, `candidate_count=0`, `draft_count=0`, and external reviewer feedback remains pending.

Deterministic text embedding preview v0: implemented. Boundary: local hash preview only; not actual embedding model generation, not persisted, and not vector search quality evidence.

Trace context header propagation v0: implemented. Boundary: local `traceparent` response headers only; not distributed tracing, not OpenTelemetry, and not hosted observability.

Trace context header runtime smoke v0: implemented. Boundary: local uvicorn/curl evidence only; not hosted observability, not distributed tracing, and not cross-service trace proof.

Embedding provider source review v0: implemented. Boundary: official OpenAI embeddings contract reviewed only; no API call, no dependency, no cost-incurring runtime path, and actual embedding model generation remains unproven.

Embedding model provider disabled-path v0: implemented. Boundary: `POST /chunks/embedding-model-preview` reports provider configuration only; no provider call, no embedding vector, no persistence, and no cost.

Embedding model provider live-call review v0: implemented. Boundary: guardrail review only; `allow_provider_call`, timeout, dimension check, redaction, and mocked-client-first test order are documented, but no provider call is implemented.

Embedding model mocked-provider call v0: implemented. Boundary: provider response handling is tested only through an injected mocked client; no live OpenAI provider call, no live provider call in CI, no automatic persistence, and actual live embedding model generation remains unproven.

Embedding model live-provider implementation review v0: implemented. Boundary: owner-runtime live provider implementation requirements are documented, including `OPENAI_API_KEY`, `allow_provider_call`, timeout, secret redaction, provider response dimension check, usage metadata, no live provider call in CI, and manual owner runtime smoke; no live provider call is implemented.

Embedding model live-provider code review v0: implemented. Boundary: the future live provider insertion point is documented as a tiny OpenAI Python SDK adapter behind the existing `get_embedding_provider_client` dependency; dependency addition is deferred and no runtime behavior is added.

Embedding model live-provider dependency review v0: implemented. Boundary: `openai==2.41.0` is recorded as a registry-observed future candidate with `uv.lock`/CI/no-live-call checks; no dependency is installed, no lockfile is changed, and no runtime behavior is added.

Embedding model live-provider dependency addition v0: implemented. Boundary: `openai==2.41.0` is added to `apps/api/pyproject.toml` and `apps/api/uv.lock`; this is dependency metadata only, no app code or route behavior changed, and actual live embedding model generation remains unproven.

Embedding model live-provider adapter disabled-code v0: implemented. Boundary: `OpenAIEmbeddingProviderClient` exists behind fake-client unit tests, but `get_embedding_provider_client` still returns `None`; the route remains unwired and no live provider call occurs in CI or by default.

Embedding model live-provider route wiring review v0: implemented. Boundary: future wiring must require `NOISEPROOF_ENABLE_OPENAI_PROVIDER=true`, `OPENAI_API_KEY`, `allow_provider_call=true`, and `CI` not true; this review adds no runtime behavior and no route wiring.

Embedding model live-provider route wiring opt-in-disabled v0: implemented. Boundary: `get_embedding_provider_client` now returns an `OpenAIEmbeddingProviderClient` only when `NOISEPROOF_ENABLE_OPENAI_PROVIDER=true`, `OPENAI_API_KEY` is configured, `CI` is not true, and timeout is positive; default and CI runtime still make no live provider call, and actual live embedding model generation remains unproven.

Embedding model live-provider error boundary v0: implemented. Boundary: `POST /chunks/embedding-model-preview` now maps `EmbeddingProviderError` from the explicit provider-call branch into HTTP 502 metadata with `provider_call_boundary=owner_runtime_provider_error`, `secret_exposed=false`, and redacted provider error text. This is provider error metadata only, not live embedding generation proof, semantic retrieval quality evidence, hosted deployment evidence, external reviewer feedback, or product-complete.

Embedding model live-provider error boundary remote verification v0: implemented. Boundary: commit `44c7273496198cbd88f43bd5fa030306353dd4ef` passed CI run `27058899825` and External Feedback Screen run `27058899830`; this is remote workflow evidence only, not the local route behavior itself, not live embedding generation proof, not external reviewer feedback, and not product-complete.

Embedding provider readiness ops surface v0: implemented. Boundary: `GET /ops/summary` now exposes `embedding_provider_readiness`, and `GET /ops/dashboard` renders `Embedding Provider Readiness` plus `owner_runtime_opt_in_only` / `readiness_only_not_persisted` boundaries. Ops rendering makes no OpenAI provider call, prints no secret, persists no readiness row, and is not live embedding generation proof.

Embedding provider readiness ops surface remote verification v0: implemented. Boundary: commit `8407bb47e155039cb8526d0aef6429417990cf24` passed CI run `27059262165` and External Feedback Screen run `27059262159`; this is remote workflow verification only, not live embedding generation proof, not external reviewer feedback, hosted deployment evidence, or product-complete.

Embedding model live-provider owner-runtime smoke packet v0: implemented. Boundary: `app.services.embedding_model_live_provider_harness --print-owner-runtime-smoke-packet` emits a no-secret/no-call owner-runtime smoke contract; current local discovery has no `OPENAI_API_KEY`, so live embedding generation proof remains pending.

Embedding model live-provider owner-runtime input discovery v0: implemented. Boundary: `app.services.embedding_model_live_provider_harness --discover-owner-runtime-input` reports owner-runtime readiness booleans without printing secrets or calling the provider; current local status is `missing_openai_api_key`, and actual live embedding model generation remains unproven.

Embedding model live-provider owner-runtime input discovery ci check v0: implemented. Boundary: CI now runs the no-secret discovery command and expects `owner_runtime_input_status=missing_openai_api_key`, `api_calls_attempted=false`, and `openai_api_key_printed=false`; this is not live embedding generation proof.

Embedding model live-provider owner-runtime input discovery ci remote verification v0: implemented. Boundary: remote GitHub Actions run `26988305027` on head `1b4e42b508c9357c58b45f1fed9a990fe542cdb1` completed CI job `api-smoke` successfully and step 9, `Check embedding provider owner runtime input discovery missing state`, concluded success; this is remote missing-input guard evidence only, not live embedding generation proof.

Embedding model live-provider owner-runtime smoke validator v0: implemented. Boundary: `app.services.embedding_model_live_provider_harness --validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>` validates future owner-runtime smoke metadata for `owner_runtime_provider_generated`, dimension 1536, provider dimension check passed, usage metadata present, no printed/logged/committed key, and outside-repo report path; this validator does not call OpenAI and is not live embedding generation proof by itself.

Embedding model live-provider owner-runtime smoke post-run validation command v0: implemented. Boundary: the no-secret smoke packet now includes `--validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>` plus success criteria `accepted_owner_runtime_smoke=true` and `missing_or_failed_checks=[]`; this does not run the smoke and is not live embedding generation proof.

Embedding model live-provider owner-runtime smoke post-run validation cross-shell commands v0: implemented. Boundary: the no-secret smoke packet now includes `post_run_validation_commands.posix` and `.powershell` so future POSIX/PowerShell owner-runtime smoke reports can be validated with the same metadata-only validator step; this does not run the smoke and is not live embedding generation proof.

Embedding model live-provider owner-runtime smoke report contract v0: implemented. Boundary: `--print-owner-runtime-smoke-report-contract` emits the exact secret-free metadata shape a future owner-runtime OpenAI embedding smoke report must satisfy before `--validate-owner-runtime-smoke-report` can accept it; this does not read or print `OPENAI_API_KEY`, call the provider, or prove live embedding generation.

Embedding model live-provider owner-runtime smoke report schema v0: implemented. Boundary: `--print-owner-runtime-smoke-report-schema` emits a strict draft 2020-12 JSON Schema for the same owner-runtime smoke report metadata; this is schema-only and does not read or print `OPENAI_API_KEY`, call the provider, or prove live embedding generation.

Embedding model live-provider owner-runtime smoke report contract alignment v0: implemented. Boundary: `--check-owner-runtime-smoke-report-contract-alignment` verifies that the accepted report contract, JSON Schema required/properties/constants, and authoritative Python validator expected fields are aligned; this is schema/contract/validator alignment only and not live embedding generation proof.

Embedding model live-provider owner-runtime smoke report contract alignment ci remote verification v0: implemented. Boundary: remote GitHub Actions run `26991391227` on head `4dd79f75099989dd155a3dce71000e1b72e7c870` completed CI job `api-smoke` successfully, including `Run API smoke tests`; related External Feedback Screen run `26991391234` succeeded as a workflow screen only, not external reviewer feedback.

External review issue body embedding provider report alignment refresh v0: implemented. Boundary: issue #1 body now points reviewers to the embedding provider report contract, report schema, contract alignment check, and contract alignment CI remote verification; this is owner-authored issue body routing only, not external reviewer feedback or live embedding generation proof.

External feedback current-state embedding provider report alignment issue verification v0: implemented. Boundary: issue #1 current state after the report alignment refresh has `candidate_count=0`, `draft_count=0`, and only `self_authored_comment`; external reviewer feedback remains pending.

Embedding model live-provider owner-runtime smoke response handoff report v0: implemented. Boundary: `--build-owner-runtime-smoke-report-from-response <owner-runtime-response-json-outside-repo> --output <runtime-report-path-outside-repo>` converts a future owner-runtime route response capture into the strict metadata-only report accepted by `--validate-owner-runtime-smoke-report`; this does not call OpenAI, does not persist embeddings, excludes the embedding vector from the report, and is not live embedding generation proof.

Embedding model live-provider owner-runtime smoke packet command-template handoff alignment v0: implemented. Boundary: `--print-owner-runtime-smoke-packet` now includes `response_handoff_command`, `response_handoff_commands`, `emit_response_handoff_report=true`, and `write_response_capture_outside_repo=true` so future owner-runtime route response captures can be converted into strict validator reports outside the repository; this is packet metadata only and is not live embedding generation proof.

Embedding model live-provider owner-runtime smoke packet command-template handoff alignment ci remote verification v0: implemented. Boundary: remote GitHub Actions run `26992724568` on head `fb271d1e59dfde93cb805440554952dc44a43fa4` completed CI job `api-smoke` successfully, including `Run API smoke tests`; related External Feedback Screen run `26992724578` succeeded as a workflow screen only, not external reviewer feedback.

External reviewer embedding provider owner-runtime smoke handoff alignment request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to `docs/review/embedding-model-live-provider-owner-runtime-smoke-response-handoff-report.md`, `docs/review/embedding-model-live-provider-owner-runtime-smoke-packet-command-template-handoff-alignment.md`, `docs/review/embedding-model-live-provider-owner-runtime-smoke-packet-command-template-handoff-alignment-ci-remote-verification.md`, and `docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-handoff-alignment-request-refresh.md`; this is not a live issue body edit, external reviewer feedback, hosted deployment evidence, live embedding generation proof, or product-complete.

External review issue body embedding provider owner-runtime smoke handoff alignment refresh v0: implemented. Boundary: issue #1 body now points reviewers to the embedding provider response handoff, command-template handoff alignment, handoff alignment CI remote verification, and handoff alignment request refresh; this is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, live embedding generation proof, or product-complete.

External feedback current-state embedding provider owner-runtime smoke handoff alignment issue verification v0: implemented. Boundary: issue #1 current state after the handoff alignment issue-body refresh has `candidate_count=0`, `draft_count=0`, and only `self_authored_comment`; external reviewer feedback remains pending.

External reviewer embedding provider owner-runtime smoke packet request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to `docs/review/embedding-model-live-provider-owner-runtime-smoke-packet.md` and `docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-packet-request-refresh.md`; this is not a live issue body edit, external reviewer feedback, hosted deployment evidence, live embedding generation proof, or product-complete.

External reviewer embedding provider owner-runtime smoke validator request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to `docs/review/embedding-model-live-provider-owner-runtime-smoke-validator.md`, `docs/review/embedding-model-live-provider-owner-runtime-smoke-post-run-validation-command.md`, and `docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-validator-request-refresh.md`; this is not a live issue body edit, external reviewer feedback, hosted deployment evidence, live embedding generation proof, or product-complete.

External review issue body embedding provider owner-runtime smoke validator refresh v0: implemented. Boundary: issue #1 body now points reviewers to `docs/review/embedding-model-live-provider-owner-runtime-smoke-validator.md`, `docs/review/embedding-model-live-provider-owner-runtime-smoke-post-run-validation-command.md`, `docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-validator-request-refresh.md`, and `docs/review/external-review-issue-body-embedding-provider-owner-runtime-smoke-validator-refresh.md`; this is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, live embedding generation proof, or product-complete.

External feedback current-state embedding provider owner-runtime smoke validator issue verification v0: implemented. Boundary: issue #1 current state has `candidate_count=0`, `draft_count=0`, and only `self_authored_comment`; external reviewer feedback remains pending.

External review issue body embedding provider owner-runtime smoke packet refresh v0: implemented. Boundary: issue #1 body now points reviewers to `docs/review/embedding-model-live-provider-owner-runtime-smoke-packet.md`, `docs/review/external-reviewer-embedding-provider-owner-runtime-smoke-packet-request-refresh.md`, and `docs/review/external-review-issue-body-embedding-provider-owner-runtime-smoke-packet-refresh.md`; this is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, live embedding generation proof, or product-complete.

External feedback current-state embedding provider owner-runtime smoke packet issue verification v0: implemented. Boundary: issue #1 current state has `candidate_count=0`, `draft_count=0`, and only `self_authored_comment`; external reviewer feedback remains pending.

README latest-marker current-state refresh v0: implemented. Boundary: top markers now point to the current ClamAV proof-boundary, runtime proof, reviewer-routing, and external-feedback pending state.

README latest-marker embedding handoff current-state refresh v0: implemented. Boundary: README top markers now point to the embedding provider handoff alignment issue-body refresh and current-state issue verification; external reviewer feedback remains pending, and this is not live embedding generation proof or product-complete.

README upload handoff claim-boundary refresh v0: implemented. Boundary: explicit uploaded-file-to-chunks handoff exists through `POST /documents/upload-chunks`; implicit upload-preview auto-persistence remains intentionally unclaimed. This is a public-claim cleanup only, not a new product runtime gate.

Raw file download operator-token guard v0: implemented. Boundary: when `NOISEPROOF_RAW_FILE_DOWNLOAD_OPERATOR_TOKEN` is configured, `GET /documents/upload-raw-files/{raw_file_id}/download` requires `X-NoiseProof-Operator-Token` before scan, approval, and rate-limit gates; authorization boundary is `local_v0_operator_token_header_not_production`, not production authorization or authenticated user identity.

Workflow failure-case persistence handoff v0: implemented. Boundary: `POST /failure-cases/workflow-runs/{workflow_run_id}` can create one persisted failure case from an existing failed/blocked/needs-revision workflow parent with `caller_triggered_workflow_failure_case_persistence`; this is not background automation, root-cause automation, complete workflow failure causality, or an LLM-backed repair loop.

Workflow failure-case persistence handoff runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP evidence shows failed workflow parent -> `POST /failure-cases/workflow-runs/{workflow_run_id}` -> persisted linked failure case -> review queue `failure_case_linked`; completed workflows and duplicate handoffs return `409`. This is not hosted deployment evidence, external reviewer feedback, background automation, or complete workflow failure causality.

External reviewer workflow failure-case persistence runtime request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to `docs/review/workflow-failure-case-persistence-handoff-runtime-smoke.md` and `docs/review/external-reviewer-workflow-failure-case-persistence-runtime-request-refresh.md`; this is not a live issue body edit, external reviewer feedback, hosted deployment evidence, background automation, complete workflow failure causality, or product-complete.

External review issue body workflow failure-case persistence runtime refresh v0: implemented. Boundary: issue #1 now points reviewers to `docs/review/workflow-failure-case-persistence-handoff-runtime-smoke.md`, `docs/review/external-reviewer-workflow-failure-case-persistence-runtime-request-refresh.md`, and `docs/review/external-review-issue-body-workflow-failure-case-persistence-runtime-refresh.md`; this is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, background automation, complete workflow failure causality, or product-complete.

External feedback current-state workflow failure-case persistence runtime issue verification v0: implemented. Boundary: current issue #1 has the workflow failure-case persistence runtime proof, request refresh, and issue-body refresh links, but the only screened comment is owner-authored, `candidate_count=0`, `draft_count=0`, and external reviewer feedback remains pending.

Workflow proof bundle read model v0: implemented. Boundary: `GET /workflow-runs/{id}/proof-bundle` collects existing workflow detail, derived lineage, and trace lookup surfaces without new storage, distributed tracing, hosted observability, external reviewer feedback, or product-complete claims.

Workflow proof bundle runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP verified `GET /workflow-runs/{id}/proof-bundle` returns existing detail, lineage, and trace lookup surfaces without distributed tracing, hosted observability, hosted deployment evidence, external reviewer feedback, or product-complete claims.

Workflow proof bundle failure-case links v0: implemented. Boundary: `GET /workflow-runs/{id}` and `GET /workflow-runs/{id}/proof-bundle` now surface linked `failure_cases` plus `failure_case_count`, and `GET /failure-cases?workflow_run_id={id}` filters failure cases by workflow parent. This is a read model only, not automatic failure detection, background automation, complete workflow failure causality, root-cause automation, hosted deployment evidence, external reviewer feedback, or product-complete.

Workflow proof bundle failure-case links runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP verified linked failure cases appear in `GET /workflow-runs/{id}` and `GET /workflow-runs/{id}/proof-bundle`, while `GET /failure-cases?workflow_run_id={id}` filters out an unrelated failure case. This is local runtime evidence only, not automatic failure detection, background automation, complete workflow failure causality, root-cause automation, hosted deployment evidence, external reviewer feedback, or product-complete.

External reviewer workflow proof bundle failure-case links runtime request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to `docs/review/workflow-proof-bundle-failure-case-links-runtime-smoke.md` and `docs/review/external-reviewer-workflow-proof-bundle-failure-case-links-runtime-request-refresh.md`; this is not a live issue body edit, external reviewer feedback, hosted deployment evidence, automatic failure detection, background automation, complete workflow failure causality, or product-complete.

External review issue body workflow proof bundle failure-case links runtime refresh v0: implemented. Boundary: issue #1 now points reviewers to `docs/review/workflow-proof-bundle-failure-case-links-runtime-smoke.md`, `docs/review/external-reviewer-workflow-proof-bundle-failure-case-links-runtime-request-refresh.md`, and `docs/review/external-review-issue-body-workflow-proof-bundle-failure-case-links-runtime-refresh.md`; this is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, automatic failure detection, background automation, complete workflow failure causality, or product-complete.

External feedback current-state workflow proof bundle failure-case links runtime issue verification v0: implemented. Boundary: current issue #1 has the workflow proof bundle failure-case links runtime proof, request refresh, and issue-body refresh links, but the only screened comment is owner-authored, `candidate_count=0`, `draft_count=0`, and external reviewer feedback remains pending.

Workflow dashboard failure-case counts v0: implemented. Boundary: `GET /ops/dashboard` workflow rows now show linked failure-case counts and link nonzero counts to `GET /failure-cases?workflow_run_id={id}`. This is a dashboard read model only, not automatic failure detection, background automation, complete workflow failure causality, root-cause automation, hosted deployment evidence, external reviewer feedback, or product-complete.

Workflow dashboard failure-case counts runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP verified `GET /ops/dashboard` includes the `Linked Failure Cases` workflow column, links a workflow with one linked failure case to `GET /failure-cases?workflow_run_id={id}`, and omits that filter link for an unlinked failed workflow. This is local runtime evidence only, not automatic failure detection, background automation, complete workflow failure causality, root-cause automation, hosted deployment evidence, external reviewer feedback, or product-complete.

External reviewer workflow dashboard failure-case counts runtime request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to `docs/review/workflow-dashboard-failure-case-counts-runtime-smoke.md` and `docs/review/external-reviewer-workflow-dashboard-failure-case-counts-runtime-request-refresh.md`; this is not a live issue body edit, external reviewer feedback, hosted deployment evidence, automatic failure detection, background automation, complete workflow failure causality, or product-complete.

External review issue body workflow dashboard failure-case counts runtime refresh v0: implemented. Boundary: issue #1 now points reviewers to `docs/review/workflow-dashboard-failure-case-counts-runtime-smoke.md`, `docs/review/external-reviewer-workflow-dashboard-failure-case-counts-runtime-request-refresh.md`, and `docs/review/external-review-issue-body-workflow-dashboard-failure-case-counts-runtime-refresh.md`; this is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, automatic failure detection, background automation, complete workflow failure causality, or product-complete.

External feedback current-state workflow dashboard failure-case counts runtime issue verification v0: implemented. Boundary: current issue #1 has the workflow dashboard failure-case counts runtime proof, request refresh, and issue-body refresh links, but the only screened comment is owner-authored, `candidate_count=0`, `draft_count=0`, and external reviewer feedback remains pending.

Workflow review queue dashboard draft-preview method boundary v0: implemented. Boundary: `GET /ops/dashboard` now renders `POST /failure-cases/draft-preview` as a method-aware cue instead of a clickable GET link; this is dashboard method-boundary hardening only, not automatic failure-case creation, background automation, complete workflow failure causality, external reviewer feedback, hosted deployment evidence, or product-complete.

Ops dashboard GET-only link method boundary v0: implemented. Boundary: `GET /ops/dashboard` now states that dashboard links are GET-only inspection routes and POST-only actions render as method cues, not anchors; this is not a route behavior change, automatic failure-case creation, background automation, hosted deployment evidence, external reviewer feedback, or product-complete.

Ops dashboard anchor method metadata v0: implemented. Boundary: clickable `GET /ops/dashboard` anchors now include `data-method="GET"` so inspection links are machine-readable; POST-only actions remain method cues, not anchors. This is not a route behavior change, automatic failure-case creation, background automation, hosted deployment evidence, external reviewer feedback, or product-complete.

Ops dashboard anchor GET smoke v0: implemented. Boundary: local FastAPI test-client smoke verifies each clickable dashboard `data-method="GET"` anchor resolves as a GET 200 inspection route; POST-only actions remain non-clickable method cues. This is not browser automation evidence, hosted deployment evidence, external reviewer feedback, or product-complete.

Ops dashboard anchor GET runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP evidence verified `GET /ops/dashboard` exposed 38 clickable `data-method="GET"` anchors, 25 unique hrefs, and each unique href returned GET 200; POST-only draft preview remained non-clickable. This is not hosted deployment evidence, browser automation evidence, external reviewer feedback, or product-complete.

External reviewer ops dashboard anchor GET runtime request refresh v0: implemented. Boundary: reviewer-facing repository paths now point to `docs/review/ops-dashboard-anchor-get-runtime-smoke.md` and `docs/review/external-reviewer-ops-dashboard-anchor-get-runtime-request-refresh.md`; this is request-surface refresh only, not a live issue body edit, hosted deployment evidence, browser automation evidence, external reviewer feedback, or product-complete.

External review issue body ops dashboard anchor GET runtime refresh v0: implemented. Boundary: issue #1 now points reviewers to `docs/review/ops-dashboard-anchor-get-runtime-smoke.md`, `docs/review/external-reviewer-ops-dashboard-anchor-get-runtime-request-refresh.md`, and `docs/review/external-review-issue-body-ops-dashboard-anchor-get-runtime-refresh.md`; observed `starts_with_request=true`, `first_codepoint=35`, and `comment_count=1`. This is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, browser automation evidence, customer validation, or product-complete.

External feedback current-state ops dashboard anchor GET runtime issue verification v0: implemented. Boundary: current issue #1 has the ops dashboard anchor GET runtime proof, request refresh, and issue-body refresh links, but the only screened comment is owner-authored, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, and external reviewer feedback remains pending. This is not external reviewer feedback, hosted deployment evidence, browser automation evidence, customer validation, or product-complete.

Ops dashboard anchor browser smoke v0: implemented. Boundary: local Playwright browser automation verified `GET /ops/dashboard` rendered 27 clickable anchors, all 27 carried `data-method="GET"`, no `data-method="POST"` anchors existed, and `POST /failure-cases/draft-preview` remained a visible method cue rather than a clickable anchor. This is local browser automation evidence only, not hosted deployment evidence, external reviewer feedback, customer validation, design quality evidence, or product-complete.

External reviewer ops dashboard anchor browser smoke request refresh v0: implemented. Boundary: reviewer-facing repository paths now point to `docs/review/ops-dashboard-anchor-browser-smoke.md` and `docs/review/external-reviewer-ops-dashboard-anchor-browser-smoke-request-refresh.md`; this is request-surface refresh only, not a live issue body edit, hosted deployment evidence, external reviewer feedback, customer validation, design quality evidence, or product-complete.

External review issue body ops dashboard anchor browser smoke refresh v0: implemented. Boundary: issue #1 now points reviewers to `docs/review/ops-dashboard-anchor-browser-smoke.md`, `docs/review/external-reviewer-ops-dashboard-anchor-browser-smoke-request-refresh.md`, and `docs/review/external-review-issue-body-ops-dashboard-anchor-browser-smoke-refresh.md`; observed `starts_with_request=true`, `first_codepoint=35`, and `comment_count=1`. This is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, customer validation, design quality evidence, or product-complete.

External feedback current-state ops dashboard anchor browser smoke issue verification v0: implemented. Boundary: current issue #1 has the ops dashboard anchor browser smoke proof, request refresh, and issue-body refresh links, but the only screened comment is owner-authored, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, and external reviewer feedback remains pending. This is not external reviewer feedback, hosted deployment evidence, customer validation, design quality evidence, or product-complete.

Uploaded raw file storage v0: implemented. Boundary: quarantined PostgreSQL BYTEA storage with metadata-only responses; no download endpoint, no malware scanning, and no robust PDF extraction.

Uploaded raw file storage runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP evidence only; not hosted deployment evidence, not external reviewer feedback, and not malware scanning.

Uploaded raw file storage application refresh v0: implemented. Boundary: the local runtime proof is now surfaced in application-facing docs; not hosted deployment evidence, not external reviewer feedback, and not product-complete.

External reviewer raw file storage request refresh v0: implemented. Boundary: reviewer request surfaces now point to the uploaded raw file storage proof; not external reviewer feedback, not hosted deployment evidence, not malware scanning, and not a download endpoint.

External review issue body raw file storage refresh v0: implemented. Boundary: issue #1 now points to the uploaded raw file storage proof; owner-authored issue edit only, not external reviewer feedback, not hosted deployment evidence, not malware scanning, and not a download endpoint.

External feedback current-state raw file storage issue verification v0: implemented. Boundary: current issue #1 screen still has candidate_count 0 and only a self-authored comment; not external reviewer feedback, not hosted deployment evidence, not malware scanning, and not a download endpoint.

Uploaded raw file storage safety review v0: implemented. Boundary: source-first review keeps raw uploads quarantine-only and selects scan result schema review before any download endpoint; not malware scanning, not a download endpoint, and not hosted deployment evidence.

Uploaded raw file scan result schema review v0: implemented. Boundary: review-only decision to use future `raw_file_scan_results` linked to `uploaded_raw_files(id)` before any scanner or download endpoint; not malware scanning, not runtime evidence, and not product-complete.

Uploaded raw file scan result schema v0: implemented. Boundary: schema-only `raw_file_scan_results` table linked to `uploaded_raw_files(id)` for future scan attempts; not malware scanning, not scanner execution, not ClamAV integration, not a download endpoint, and not runtime evidence.

Uploaded raw file scan result repository review v0: implemented. Boundary: review-only selection of `RawFileScanResultCreate`, `create_raw_file_scan_result`, and `list_raw_file_scan_results`; no repository code, endpoint, scanner execution, ClamAV integration, download endpoint, or runtime evidence.

Uploaded raw file scan result repository v0: implemented. Boundary: repository-only caller-provided scan result persistence through `RawFileScanResultCreate`, `create_raw_file_scan_result`, and `list_raw_file_scan_results`; no endpoint, scanner execution, ClamAV integration, download endpoint, or runtime evidence.

Uploaded raw file scan result endpoint review v0: implemented. Boundary: review-only selection of metadata-only `POST /documents/upload-raw-files/{raw_file_id}/scan-results` and `GET /documents/upload-raw-files/{raw_file_id}/scan-results`; no endpoint code, scanner execution, ClamAV integration, download endpoint, or runtime evidence.

Uploaded raw file scan result endpoint v0: implemented. Boundary: metadata-only caller-provided scan result `POST /documents/upload-raw-files/{raw_file_id}/scan-results` and `GET /documents/upload-raw-files/{raw_file_id}/scan-results`; no scanner execution, ClamAV integration, download endpoint, or runtime evidence.

Uploaded raw file scan result endpoint runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP proof for metadata-only scan result POST/GET and path/body mismatch 400; not scanner execution, not ClamAV integration, not a download endpoint, and not hosted deployment evidence.

External reviewer scan-result endpoint request refresh v0: implemented. Boundary: reviewer request surfaces now point to the uploaded raw file scan result endpoint proof; not external reviewer feedback, not hosted deployment evidence, not malware scanning, and not a download endpoint.

External review issue body scan-result endpoint refresh v0: implemented. Boundary: issue #1 now points to the uploaded raw file scan result endpoint proof; owner-authored issue edit only, not external reviewer feedback, not hosted deployment evidence, not malware scanning, and not a download endpoint.

External feedback current-state scan-result endpoint issue verification v0: implemented. Boundary: current issue #1 screen still has candidate_count 0 and only a self-authored comment; not external reviewer feedback, not hosted deployment evidence, not malware scanning, and not a download endpoint.

Uploaded raw file scanner adapter review v0: implemented. Boundary: review-only selection of `ScannerAdapter`, `ScanAdapterRequest`, and `ScanAdapterResult` before ClamAV or scanner execution; missing scanners and timeouts must map to `scan_error`, not clean.

Uploaded raw file scanner adapter v0: implemented. Boundary: generic scanner adapter types plus unavailable/timeout failure mapping only; not ClamAV integration, not malware scanning, not scanner process execution, and not a download endpoint.

Uploaded raw file ClamAV adapter review v0: implemented. Boundary: review-only selection of `ClamAvScannerAdapter` with `clamscan first`, `clamdscan later`, and conservative subprocess failure mapping; not malware scanning or scanner execution.

Uploaded raw file ClamAV adapter v0: implemented. Boundary: `ClamAvScannerAdapter` maps missing binary, missing temporary path, timeout, unknown return code, clean output, and FOUND output without installing or runtime-verifying ClamAV.

Uploaded raw file ClamAV adapter runtime smoke v0: implemented. Boundary: deterministic command smoke exercises missing/clean/infected/timeout/error mappings through fake runners; not real ClamAV execution, not signature database evidence, not endpoint behavior, and not malware scanning evidence.

External reviewer ClamAV adapter runtime smoke request refresh v0: implemented. Boundary: reviewer request surfaces now point to the deterministic ClamAV adapter smoke proof; not external reviewer feedback, not hosted deployment evidence, not real ClamAV execution, not signature database evidence, and not malware scanning.

External review issue body ClamAV adapter runtime smoke refresh v0: implemented. Boundary: issue #1 now points to the deterministic ClamAV adapter smoke proof; owner-authored issue edit only, not external reviewer feedback, not hosted deployment evidence, not real ClamAV execution, not signature database evidence, and not malware scanning.

External feedback current-state ClamAV adapter runtime smoke issue verification v0: implemented. Boundary: current issue #1 screen still has candidate_count 0 and only a self-authored comment; not external reviewer feedback, not hosted deployment evidence, not real ClamAV execution, not signature database evidence, and not malware scanning.

Uploaded raw file scan execution review v0: implemented. Boundary: source-first review selects a future explicit `POST /documents/upload-raw-files/{raw_file_id}/scan` endpoint and keeps scan execution separate from caller-provided scan result metadata; review-only, not endpoint code, not real ClamAV execution, and not malware scanning evidence.

Uploaded raw file scan execution endpoint v0: implemented. Boundary: explicit `POST /documents/upload-raw-files/{raw_file_id}/scan` writes stored raw bytes to a service-generated temporary scan file, executes the configured scanner adapter, persists metadata-only scan results, and defaults to `scanner-unavailable` / `scan_error`; not real ClamAV execution, not malware scanning evidence, not hosted evidence, and not a download endpoint.

Uploaded raw file scan execution endpoint runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP proof for upload, explicit scan execution, and scan-result listing with default `scanner-unavailable` / `scan_error`; not real ClamAV execution, not malware scanning evidence, not hosted evidence, and not external reviewer feedback.

External reviewer scan execution endpoint request refresh v0: implemented. Boundary: reviewer request surfaces now point to the scan execution endpoint runtime smoke proof; not external reviewer feedback, not hosted deployment evidence, not real ClamAV execution, and not malware scanning.

External review issue body scan execution endpoint refresh v0: implemented. Boundary: issue #1 now points to the scan execution endpoint runtime proof; owner-authored issue edit only, not external reviewer feedback, not hosted deployment evidence, not real ClamAV execution, and not malware scanning.

External feedback current-state scan execution endpoint issue verification v0: implemented. Boundary: current issue #1 screen still has candidate_count 0 and only a self-authored comment; not external reviewer feedback, not hosted deployment evidence, not real ClamAV execution, and not malware scanning.

Uploaded raw file ClamAV runtime verification review v0: implemented. Boundary: review-only selection of a future Dockerized ClamAV + EICAR smoke before changing API defaults or claiming real scanner evidence; not runtime evidence, not malware scanning evidence, and not endpoint verification with real ClamAV.

Dockerized ClamAV EICAR runtime smoke v0: implemented. Boundary: local Dockerized `clamav/clamav:stable` detected container-internal EICAR with `Eicar-Test-Signature`, recording image digest and signature DB version; real ClamAV runtime verified for EICAR only, not production malware scanning evidence, not API endpoint verification with real ClamAV, and not hosted evidence.

ClamAV API integration boundary review v0: implemented. Boundary: review-only decision not to wire Docker CLI execution into the API endpoint and not to change the default scanner yet; selects a future ClamAV service boundary review before endpoint integration.

ClamAV service boundary review v0: implemented. Boundary: review-only decision to design a dedicated ClamAV service/daemon boundary before compose or API code; no clamd exposure, no endpoint integration, no malware scanning evidence.

ClamAV compose service review v0: implemented. Boundary: review-only decision to design a future internal-only `clamav` Docker Compose service before editing compose or API code; no compose code, no clamd runtime verification, no endpoint integration, and no malware scanning evidence.

ClamAV compose service implementation v0: implemented. Boundary: optional internal-only `clamav` Docker Compose service behind the `scanner` profile with no host port publishing and a signature DB volume; not clamd runtime verification, not API endpoint integration, and not malware scanning evidence.

ClamAV compose service config verification v0: implemented. Boundary: `docker compose --profile scanner config` rendered the optional `clamav` service with `profiles: scanner`, `expose: 3310`, no clamd host port publishing, and `clamdscan --ping=1`; not clamd runtime verification, not API endpoint integration, and not malware scanning evidence.

ClamAV compose service runtime smoke v0: implemented. Boundary: local Docker Compose `clamav` service reached healthy state, returned `PONG` to `clamdscan --ping=1`, and exposed no host port bindings; real ClamAV runtime verified for daemon availability only, not API endpoint integration and not malware scanning evidence.

ClamAV compose EICAR runtime smoke v0: implemented. Boundary: local Docker Compose `clamav` service detected container-internal EICAR as `Eicar-Test-Signature`, deleted the temporary file, and kept the payload out of the repo; not API endpoint integration and not production malware scanning evidence.

ClamAV service scanner adapter review v0: implemented. Boundary: review-only decision to add a future `ClamdScannerAdapter` that uses clamd `INSTREAM` over the internal Docker network instead of API temp paths or `clamdscan` subprocesses; no adapter code and no API endpoint integration.

ClamAV service scanner adapter v0: implemented. Boundary: `ClamdScannerAdapter` streams bytes with clamd `INSTREAM` and maps clean, infected, timeout, unavailable, and unexpected responses through unit tests; no API endpoint integration, no default scanner switch, and no real endpoint proof.

ClamAV API service network boundary review v0: implemented. Boundary: review-only decision that host-local FastAPI must not reach ClamAV by publishing unauthenticated clamd TCP; API service integration requires the API runtime to join the same internal Docker network as `clamav`.

ClamAV API compose service review v0: implemented. Boundary: review-only decision to add a future profiled `api` Compose service that joins the same network as `clamav` and uses `CLAMD_HOST=clamav`, while keeping scanner opt-in explicit and clamd host ports unpublished.

ClamAV API compose service implementation v0: implemented. Boundary: added `apps/api/Dockerfile` and a profiled `api` Compose service with `DATABASE_URL` pointing at `db`, `CLAMD_HOST=clamav`, and `NOISEPROOF_SCANNER=unavailable`; not default scanner switch and not endpoint runtime proof.

ClamAV API compose service config verification v0: implemented. Boundary: `docker compose --profile api --profile scanner config` renders the profiled `api` service with `DATABASE_URL` to `db`, `CLAMD_HOST=clamav`, `NOISEPROOF_SCANNER=unavailable`, and no ClamAV host port publishing; not API runtime smoke or endpoint proof.

ClamAV API compose service runtime smoke v0: implemented. Boundary: `docker compose --profile api up -d api` starts the profiled API service and `GET /health` returns `{"status":"ok"}` while `NOISEPROOF_SCANNER=unavailable`; not scan endpoint proof, not endpoint runtime proof with real ClamAV, and not production malware scanning evidence.

ClamAV API endpoint scanner opt-in review v0: implemented. Boundary: review-only decision to add a future explicit `NOISEPROOF_SCANNER=clamd -> ClamdScannerAdapter` path for `POST /documents/upload-raw-files/{raw_file_id}/scan`; default remains `NOISEPROOF_SCANNER=unavailable`, not endpoint runtime proof with real ClamAV, and not malware scanning evidence.

ClamAV API endpoint scanner opt-in implementation v0: implemented. Boundary: `get_scanner_adapter()` now supports explicit `NOISEPROOF_SCANNER=clamd -> ClamdScannerAdapter(host=CLAMD_HOST, port=CLAMD_PORT)` while preserving `NOISEPROOF_SCANNER=clamav -> ClamAvScannerAdapter` and keeping the default unavailable; not endpoint runtime proof with real ClamAV and not malware scanning evidence.

ClamAV API endpoint scanner opt-in runtime smoke v0: implemented. Boundary: local Docker Compose API ran with `NOISEPROOF_SCANNER=clamd` and `POST /documents/upload-raw-files/{raw_file_id}/scan` returned `scanner_name=clamav-clamd`, `scan_status=completed`, `scan_verdict=clean`, and `clamd_response=stream: OK`; clean-file endpoint proof only, not malware detection proof and not EICAR-through-API proof.

ClamAV API endpoint malicious-detection runtime review v0: implemented. Boundary: review-only safety gate for a future EICAR-through-API smoke; clean-file endpoint proof exists and `malicious_detection_verified: false` remains current. Do not store the EICAR payload in the repository, do not bypass OS security controls, and do not claim production malware scanning evidence.

ClamAV API endpoint malicious-detection runtime blocked v0: implemented. Boundary: EICAR-through-API runtime smoke was not completed because the host command was rejected before endpoint request; `payload_committed_to_repo: false`, `malicious_detection_verified: false`, and this is not malware detection proof.

ClamAV API endpoint malicious-detection test harness review v0: implemented. Boundary: review-only plan for a future opt-in harness using an owner-provided runtime-only test signature via `NOISEPROOF_ALLOW_TEST_SIGNATURE_SMOKE=1` and `NOISEPROOF_CLAMAV_TEST_SIGNATURE_TEXT`; `payload_committed_to_repo: false`, no encoded payload is stored, and this is not malware detection proof.

ClamAV API endpoint malicious-detection test harness v0: implemented. Boundary: `app.services.clamav_api_malicious_detection_harness` adds a disabled-by-default opt-in command that returns `not_configured` without API calls unless `NOISEPROOF_ALLOW_TEST_SIGNATURE_SMOKE=1` and `NOISEPROOF_CLAMAV_TEST_SIGNATURE_TEXT` are provided; fake-client tests cover `verified_infected` and `blocked_by_environment`, but this is not malware detection proof.

ClamAV API endpoint malicious-detection harness default smoke v0: implemented. Boundary: default command execution returned `harness_status=not_configured`, `api_calls_attempted=false`, `malicious_detection_verified=false`, `payload_committed_to_repo=false`, and `raw_payload_logged=false`; this is safe no-op evidence, not malware detection proof.

ClamAV API endpoint malicious-detection stdin input review v0: implemented. Boundary: review-only decision to add a stdin-only owner input path before retrying the owner-provided runtime smoke; `NOISEPROOF_CLAMAV_TEST_SIGNATURE_TEXT` remains supported, but no test signature is supplied here, `payload_committed_to_repo=false`, `raw_payload_logged=false`, and this is not malware detection proof.

ClamAV API endpoint malicious-detection stdin input harness v0: implemented. Boundary: `--signature-stdin` lets the opt-in harness accept owner-provided runtime input through stdin, reports `input_source=stdin`, keeps `payload_committed_to_repo=false` and `raw_payload_logged=false`, and has fake-client coverage only; this is not malware detection proof.

ClamAV API endpoint malicious-detection stdin default smoke v0: implemented. Boundary: `uv run python -m app.services.clamav_api_malicious_detection_harness --signature-stdin` with empty stdin returned `harness_status=not_configured`, `input_source=stdin`, `api_calls_attempted=false`, `malicious_detection_verified=false`, `payload_committed_to_repo=false`, and `raw_payload_logged=false`; owner-provided runtime smoke remains pending.

ClamAV API endpoint malicious-detection owner-runtime preflight v0: implemented. Boundary: local Compose preflight shows API up, `GET /health -> 200`, API scanner env `NOISEPROOF_SCANNER=clamd`, `CLAMD_HOST=clamav`, `CLAMD_PORT=3310`, and clamd `PING -> PONG`; owner-provided test signature is absent, no scan endpoint request was made, and this is not malware detection proof.

ClamAV API endpoint malicious-detection owner-input guard v0: implemented. Boundary: `--require-owner-input` returns `exit_code=4`, `required_owner_input_missing=true`, `api_calls_attempted=false`, and `malicious_detection_verified=false` when stdin owner input is absent; owner-provided runtime smoke remains pending and this is not malware detection proof.

ClamAV API endpoint malicious-detection owner runtime smoke packet v0: implemented. Boundary: `--print-owner-runtime-smoke-packet` emits a no-payload packet with `packet_status=ready_for_owner_input`, the stdin command template, success criteria `scanner_name=clamav-clamd`, `scan_status=completed`, `scan_verdict=infected`, `matched_signature=Eicar-Test-Signature`, and no API/scan call; owner-provided runtime smoke remains pending.

ClamAV API endpoint malicious-detection owner runtime smoke validator v0: implemented. Boundary: `--validate-owner-runtime-smoke-report` validates future owner-provided runtime smoke metadata for `verified_infected`, stdin input, no committed/logged payload, and exact `clamav-clamd` infected summary; it does not include a payload, call the API, upload raw bytes, call the scan endpoint, or prove production malware scanning.

ClamAV API endpoint malicious-detection owner runtime smoke validator leak-field hardening v0: implemented. Boundary: the validator now rejects otherwise successful owner runtime smoke JSON reports that include payload-bearing fields such as `test_signature_text` or `encoded_payload`; it reports forbidden field paths only and does not echo values.

ClamAV API endpoint malicious-detection owner runtime smoke report contract v0: implemented. Boundary: `--print-owner-runtime-smoke-report-contract` emits the no-payload accepted/rejected metadata contract for future owner-provided runtime smoke reports; it does not call the API, upload raw bytes, or call the scan endpoint.

ClamAV API endpoint malicious-detection owner runtime smoke report schema v0: implemented. Boundary: `--print-owner-runtime-smoke-report-schema` emits a JSON Schema-shaped accepted report surface using Draft 2020-12 metadata; the Python validator remains authoritative and this is not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke validator strict-shape alignment v0: implemented. Boundary: the validator now rejects unknown top-level and `scan_result_summary` fields such as `template_status` and `scan_result_summary.extra_note`, aligning runtime validation with the schema's `additionalProperties: false` contract.

ClamAV API endpoint malicious-detection owner runtime smoke cross-shell packet v0: implemented. Boundary: `--print-owner-runtime-smoke-packet` now includes POSIX and PowerShell command templates plus `runtime_report_handling` for writing reports outside the repo and validating metadata only; this is not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke report path guard v0: implemented. Boundary: `--validate-owner-runtime-smoke-report` now rejects report JSON paths that resolve inside the repository with `report_path_boundary.report_path_allowed=false`; this is not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke output path guard v0: implemented. Boundary: actual `--signature-stdin --require-owner-input --output` smoke attempts now reject output paths inside the repository with `harness_status=output_path_rejected` before API calls; this is not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke validator handoff report v0: implemented. Boundary: actual `--signature-stdin --require-owner-input --owner-runtime-smoke-report --output` smoke attempts can write a strict validator-accepted metadata shape outside the repository; the handoff report excludes `phase_marker` and `payload_length_bytes`, does not include a test signature payload, and is not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke command-template handoff alignment v0: implemented. Boundary: the packet's singular `command_template` now matches the validator handoff report path by including `--owner-runtime-smoke-report --output <runtime-report-path-outside-repo>`; this updates no-payload command metadata only and is not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke post-run validation command v0: implemented. Boundary: the no-payload packet now includes `post_run_validation_command` for `--validate-owner-runtime-smoke-report <runtime-report-path-outside-repo>` so future owner-provided runtime smoke reports have an explicit metadata validator step; this does not run the smoke and is not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke post-run validation cross-shell commands v0: implemented. Boundary: the no-payload packet now includes `post_run_validation_commands.posix` and `.powershell` so future POSIX/PowerShell owner-runtime smoke reports can be validated with the same metadata-only validator step; this does not run the smoke and is not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke post-run validation success criteria v0: implemented. Boundary: the no-payload packet now states validator success criteria for future owner-runtime smoke reports: `validation_status=accepted`, `accepted_owner_runtime_smoke=true`, and `missing_or_failed_checks=[]`; this does not run the smoke and is not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke empty-marker guard v0: implemented. Boundary: quote-only stdin markers such as `""` and `''`, plus BOM-only stdin from shell empty-pipe behavior, now normalize to missing owner input, returning `not_configured` with `exit_code=4` and `api_calls_attempted=false`; this prevents shell empty-input mistakes from reaching the scan endpoint and is not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke signature-file input v0: implemented. Boundary: `--signature-file <owner-provided-runtime-only-signature-file-outside-repo>` reads owner-provided runtime input from an outside-repo file, rejects inside-repo signature paths with `signature_file_path_allowed=false`, and keeps strict report validation payload-free; this is not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke signature-file read guard v0: implemented. Boundary: missing, directory, unreadable, or undecodable outside-repo signature-file paths now return `signature_file_read_failed` with `exit_code=8`, `api_calls_attempted=false`, and `raw_exception_logged=false`; this is not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke current-readiness recheck v0: implemented. Boundary: local Docker/Compose, API health, `NOISEPROOF_SCANNER=clamd`, and clamd `PONG` were rechecked for the future owner-provided runtime smoke; owner runtime signature input is still absent, no scan request was made, and this is not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke input discovery v0: implemented. Boundary: `--discover-owner-runtime-input` reports whether runtime input appears configured through file, stdin, or environment without reading, printing, logging, uploading, or scanning the payload; current local discovery returns `owner_runtime_input_missing`, and this is not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke input discovery ci check v0: implemented. Boundary: CI now runs the no-payload discovery command and expects `exit_code=4` plus `owner_runtime_input_missing`, proving the missing-input guard path stays inspectable; this does not run the smoke and is not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke input discovery ci remote verification v0: implemented. Boundary: remote GitHub Actions run `26927767832` on head `3089f02` completed CI job `api-smoke` successfully and step 8, `Check ClamAV owner runtime input discovery no-payload missing state`, concluded success; this is remote missing-input guard evidence only, not endpoint malicious-detection runtime proof.

External review issue body owner-runtime input discovery refresh v0: implemented. Boundary: issue #1 now points to the ClamAV owner-runtime input discovery CI remote verification proof; owner-authored issue edit only, not external reviewer feedback, not hosted deployment evidence, and not endpoint malicious-detection runtime proof.

External review issue body BOM cleanup v0: implemented. Boundary: issue #1 now starts directly with `## Request` again after removing a leading UTF-8 byte order mark introduced during the owner-runtime input discovery issue refresh; owner-authored issue edit only, not external reviewer feedback and not endpoint malicious-detection runtime proof.

ClamAV API endpoint malicious-detection owner runtime smoke input-source contract alignment v0: implemented. Boundary: owner-runtime input discovery now distinguishes `discoverable_input_sources=file,stdin,environment` from validator `accepted_input_sources=file,stdin`, and validator rejection now says `input_source must be one of: file, stdin`; this is not endpoint malicious-detection runtime proof and includes no test signature payload.

ClamAV API endpoint malicious-detection owner runtime input-source contract ci check v0: implemented. Boundary: CI now checks the no-payload discovery output for `discoverable_input_sources=file,stdin,environment`, `accepted_input_sources=file,stdin`, and validator acceptance flags; this is CI contract guard evidence only, not endpoint malicious-detection runtime proof.

External review issue body owner-runtime input-source contract refresh v0: implemented. Boundary: issue #1 now points to the owner-runtime input-source contract CI proof from run `26929243011` on head `2c4da65`; owner-authored issue edit only, not external reviewer feedback, not hosted deployment evidence, and not endpoint malicious-detection runtime proof.

External feedback current-state owner-runtime input-source contract issue verification v0: implemented. Boundary: current issue #1 screen after the input-source contract refresh still has `comment_count=1`, `candidate_count=0`, `draft_count=0`, and only a self-authored non-qualifying comment; external reviewer feedback remains pending.

clamav api endpoint malicious-detection owner runtime smoke v0: implemented. Boundary: local Docker FastAPI plus ClamAV endpoint evidence accepted owner-provided stdin input, returned `harness_status=verified_infected`, `scan_verdict=infected`, and `matched_signature=Eicar-Test-Signature`, then cleaned the local raw-file and scan rows. The repository contains metadata only; no test signature payload or encoded payload is included, and this is not production malware scanning evidence.

External reviewer ClamAV malicious-detection request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to `docs/review/clamav-api-endpoint-malicious-detection-owner-runtime-smoke.md`; this is not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, and not production malware scanning evidence.

External review issue body ClamAV malicious-detection refresh v0: implemented. Boundary: issue #1 now points reviewers to the ClamAV API endpoint malicious-detection owner-runtime smoke and its request refresh; owner-authored issue body edit only, not external reviewer feedback, not hosted deployment evidence, and not production malware scanning evidence.

External feedback current-state ClamAV malicious-detection issue verification v0: implemented. Boundary: current issue #1 screen after the ClamAV malicious-detection issue-body refresh still has `comment_count=1`, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, and only a self-authored non-qualifying comment; external reviewer feedback remains pending.

External review issue body readability refresh v0: implemented. Boundary: issue #1 was rewritten as a concise proof-routing request with fast path, latest proof, feedback format, and boundaries; `body_length=3808`, literal `\\r\\n` text absent, owner-authored issue body edit only, not external reviewer feedback.

External feedback current-state issue body readability verification v0: implemented. Boundary: current issue #1 remains concise and sectioned with `body_length=3808`, literal `\\r\\n` text absent, `comment_count=1`, `candidate_count=0`, `draft_count=0`, and only a self-authored non-qualifying comment; external reviewer feedback remains pending.

architecture current-state refresh v0: implemented. Boundary: `docs/architecture.md` separates implemented uploaded-file persistence, chunk/retrieval persistence, caller-provided embeddings, semantic retrieval persistence, and retrieval-run-linked Evidence Ledger / Noise Gate / Report handoffs from still-unproven robust PDF extraction, embedding generation, hosted deployment evidence, external reviewer feedback, and production semantic retrieval quality.

Architecture ClamAV proof boundary refresh v0: implemented. Boundary: `docs/architecture.md` and reviewer-facing current-state surfaces now recognize the local ClamAV endpoint malicious-detection owner-runtime smoke while keeping production malware scanning evidence, hosted deployment evidence, external reviewer feedback, production authorization, and product-complete claims unproven.

External reviewer architecture current-state request refresh v0: implemented. Boundary: reviewer request surfaces now link to `docs/review/architecture-current-state-refresh.md`; this is request infrastructure only, not external reviewer feedback, not hosted deployment evidence, and not endpoint malicious-detection runtime proof.

External review issue body architecture current-state refresh v0: implemented. Boundary: issue #1 now points to the architecture current-state refresh and its reviewer request refresh; owner-authored issue body edit only, not external reviewer feedback, not hosted deployment evidence, and not endpoint malicious-detection runtime proof.

External feedback current-state architecture issue verification v0: implemented. Boundary: current issue #1 screen after the architecture current-state issue-body refresh still has `comment_count=1`, `candidate_count=0`, `draft_count=0`, and only a self-authored non-qualifying comment; external reviewer feedback remains pending.

Uploaded PDF text extraction v0: implemented. Boundary: `POST /documents/upload-preview` can extract digital PDF text with PyMuPDF for uploaded PDF bytes, while keeping `preview_only_not_persisted`; OCR, table extraction, layout fidelity, robust PDF extraction, raw file storage, hosted deployment evidence, and external reviewer feedback are not claimed.

Uploaded PDF page diagnostics v0: implemented. Boundary: `POST /documents/upload-preview` now exposes PyMuPDF page diagnostics including `page_text_char_counts`, `empty_page_count`, `text_block_count`, and `image_block_count` for uploaded digital PDFs; this is not robust PDF extraction, OCR, table extraction, layout fidelity, hosted deployment evidence, or external reviewer feedback.

Uploaded PDF table-candidate diagnostics v0: implemented. Boundary: `POST /documents/upload-preview` now exposes PyMuPDF `find_tables()` candidate metadata including `table_candidate_count`, `table_candidate_page_counts`, `table_candidate_shapes`, and `table_extraction_performed=false` for uploaded digital PDFs; this is not table extraction, does not extract table contents, and is not robust PDF extraction, OCR, layout fidelity, hosted deployment evidence, external reviewer feedback, or product-complete.

Uploaded PDF table-candidate diagnostics runtime smoke v0: implemented. Boundary: local Docker/FastAPI HTTP verified `POST /documents/upload-preview` returns `table_candidate_diagnostics_available=true`, `table_candidate_count=1`, `table_candidate_page_counts=[1]`, `table_candidate_shapes=page_index=0,row_count=2,col_count=2,cell_count=4`, `table_extraction_performed=false`, and `document_count_delta=0` for a preview-only uploaded digital PDF; this is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, table-content extraction, or product-complete.

Uploaded PDF table-candidate downstream provenance runtime smoke v0: implemented. Boundary: local Docker/FastAPI HTTP verified `POST /documents/upload-chunks` and `POST /documents/{document_id}/retrieval-runs` preserve `table_candidate_count=1`, `table_candidate_page_counts=[1]`, `table_candidate_shapes=page_index=0,row_count=2,col_count=2,cell_count=4`, and `table_extraction_performed=false` through document profile metadata, chunk metadata, retrieval metadata, and retrieval candidate metadata; this is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, table-content extraction, raw file storage, full parsed text persistence, Evidence Ledger generation, or product-complete.

Uploaded PDF table-candidate downstream provenance remote verification v0: implemented. Boundary: remote GitHub Actions runs `27038450094` (`CI`) and `27038450101` (`External Feedback Screen`) succeeded on head `adf8b7a6a714e119cbaa2db88f77fa89665f3b56`; this is workflow evidence only, not a new runtime smoke, external reviewer feedback, hosted deployment evidence, robust PDF extraction, table extraction, or product-complete.

Uploaded PDF page diagnostics runtime smoke v0: implemented. Boundary: local Docker/FastAPI HTTP verified `POST /documents/upload-preview` returns `page_text_char_counts=[39]`, `empty_page_count=0`, `text_block_count=1`, `image_block_count=0`, and `document_count_delta=0` for preview-only PDF diagnostics; this is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, or product-complete.

External reviewer PDF page diagnostics runtime request refresh v0: implemented. Boundary: reviewer-facing request surfaces now point to `docs/review/uploaded-pdf-page-diagnostics-runtime-smoke.md`; this is request infrastructure only, not a live public issue body edit, not hosted deployment evidence, not external reviewer feedback, not robust PDF extraction, and not product-complete.

External reviewer PDF page diagnostics runtime issue-body refresh v0: implemented. Boundary: live issue #1 now points reviewers to `docs/review/uploaded-pdf-page-diagnostics-runtime-smoke.md` and `docs/review/external-reviewer-pdf-page-diagnostics-runtime-request-refresh.md`; this is an owner-authored issue body edit only, not external reviewer feedback, not hosted deployment evidence, not robust PDF extraction, and not product-complete.

External feedback current-state PDF page diagnostics runtime issue verification v0: implemented. Boundary: current issue #1 still has `comment_count=1`, `candidate_count=0`, `draft_count=0`, and only a self-authored non-qualifying comment after the PDF page diagnostics issue-body refresh; external reviewer feedback remains pending.

Uploaded PDF page diagnostics downstream provenance v0: implemented. Boundary: `POST /documents/upload-chunks` now preserves PDF page diagnostics in document/chunk metadata and `POST /documents/{document_id}/retrieval-runs` summarizes them from candidate chunk metadata; this is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Evidence Ledger generation, or product-complete.

Uploaded PDF page diagnostics downstream provenance runtime smoke v0: implemented. Boundary: local Docker/FastAPI HTTP verified `POST /documents/upload-chunks` and `POST /documents/{document_id}/retrieval-runs` preserve `page_text_char_counts=[39]`, `empty_page_count=0`, `text_block_count=1`, and `image_block_count=0` through document, chunk, retrieval metadata, and retrieval candidate metadata; this is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Evidence Ledger generation, or product-complete.

External reviewer PDF page diagnostics downstream runtime request refresh v0: implemented. Boundary: reviewer-facing request surfaces now point to `docs/review/uploaded-pdf-page-diagnostics-downstream-provenance-runtime-smoke.md`; this is request infrastructure only, not a live public issue body edit, not hosted deployment evidence, not external reviewer feedback, not robust PDF extraction, and not product-complete.

External reviewer PDF page diagnostics downstream runtime issue-body refresh v0: implemented. Boundary: live issue #1 now points reviewers to `docs/review/uploaded-pdf-page-diagnostics-downstream-provenance-runtime-smoke.md` and `docs/review/external-reviewer-pdf-page-diagnostics-downstream-runtime-request-refresh.md`; this is an owner-authored issue body edit only, not external reviewer feedback, not hosted deployment evidence, not robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Evidence Ledger generation, Noise Gate behavior, report generation, or product-complete.

External feedback current-state PDF page diagnostics downstream runtime issue verification v0: implemented. Boundary: current issue #1 has the PDF page diagnostics downstream runtime proof, request refresh, and issue-body refresh links, but the only screened comment is owner-authored by `svy04`, `candidate_count=0`, `draft_count=0`, and external reviewer feedback remains pending.

README latest-marker PDF downstream current-state refresh v0: implemented. Boundary: README top markers now point to the PDF page diagnostics downstream runtime issue-body refresh and downstream current-state issue verification; external reviewer feedback remains pending, and this is not hosted deployment evidence, robust PDF extraction, live embedding generation proof, or product-complete.

README latest-marker PDF downstream current-state remote verification v0: implemented. Boundary: remote GitHub Actions runs `27013838611` (`CI`) and `27013838639` (`External Feedback Screen`) succeeded on head `308d8e91f46f1f40bb2ef704c7792d12e4809a86`; the screen success is workflow evidence only, not external reviewer feedback, hosted deployment evidence, robust PDF extraction, live embedding generation proof, or product-complete.

Uploaded PDF no-text failure candidate handoff v0: implemented. Boundary: `POST /documents/upload-chunks` now preserves `failure_case_candidate.failure_type=pdf_no_extractable_text`, `chunk_handoff_no_chunks`, `page_text_char_counts=[0]`, `empty_page_count=1`, `extracted_page_count=0`, and `robust_pdf_extraction=false` in document metadata for uploaded PDFs with no embedded digital text; this is not robust PDF extraction, OCR, table extraction, layout fidelity, hosted deployment evidence, external reviewer feedback, or product-complete.

Uploaded PDF encrypted failure candidate v0: implemented. Boundary: `POST /documents/upload-preview` now returns `pdf_encrypted_requires_password`, `encrypted=true`, `password_required=true`, `digital_pdf_text_extraction=false`, and `extraction_scope=encrypted_pdf_password_required` for password-protected PDFs; this is not robust PDF extraction, OCR, table extraction, layout fidelity, decryption, hosted deployment evidence, external reviewer feedback, or product-complete.

Uploaded PDF encrypted failure candidate runtime smoke v0: verified. Boundary: local FastAPI on port 8001 verified `POST /documents/upload-preview -> 200` for `runtime-encrypted-phase673.pdf`, returning `parser=pdf-pymupdf`, `encrypted=true`, `password_required=true`, `digital_pdf_text_extraction=false`, `extraction_scope=encrypted_pdf_password_required`, `failure_case_candidate.failure_type=pdf_encrypted_requires_password`, and `persistence_boundary=preview_only_not_persisted`; see `docs/review/uploaded-pdf-encrypted-failure-candidate-runtime-smoke.md`. This is local runtime evidence only, not robust PDF extraction, decryption, hosted deployment evidence, external reviewer feedback, or product-complete.

Uploaded PDF encrypted failure candidate handoff ops v0: implemented. Boundary: `POST /documents/upload-chunks` now preserves encrypted PDF failure metadata in persisted document `profile_json`, and `/ops/summary` plus `/ops/dashboard` surface `pdf_encrypted_failure_candidate_count` / `PDF Encrypted Failure Candidates`; see `docs/review/uploaded-pdf-encrypted-failure-candidate-handoff-ops.md`. This is metadata-derived operations visibility only, not robust PDF extraction, decryption, hosted deployment evidence, external reviewer feedback, or product-complete.

Uploaded PDF encrypted handoff ops runtime smoke v0: verified. Boundary: local Docker PostgreSQL plus live FastAPI on port 8001 verified encrypted `POST /documents/upload-chunks -> 201`, `post_pdf_encrypted_failure_candidate_count -> 1`, and dashboard `PDF Encrypted Failure Candidates`; see `docs/review/uploaded-pdf-encrypted-failure-candidate-handoff-ops-runtime-smoke.md`. This is local runtime evidence only, not robust PDF extraction, decryption, hosted deployment evidence, external reviewer feedback, or product-complete.

Uploaded PDF encrypted handoff ops remote verification v0: verified. Boundary: commit `eef4636f94d987de701fdfeacf052020afffc4fe` passed CI run `27057453047` and External Feedback Screen run `27057453051`; see `docs/review/uploaded-pdf-encrypted-failure-candidate-handoff-ops-remote-verification.md`. This is remote workflow evidence only, not external reviewer feedback, hosted deployment evidence, robust PDF extraction, decryption, or product-complete.

Uploaded PDF no-text failure candidate runtime smoke v0: implemented. Boundary: local Docker/FastAPI HTTP verified `POST /documents/upload-chunks -> 201` preserves `pdf_no_extractable_text`, `chunk_handoff_no_chunks`, `chunk_count=0`, `page_text_char_counts=[0]`, `empty_page_count=1`, `extracted_page_count=0`, `robust_pdf_extraction=false`, `raw_file_storage=false`, and `parsed_text_storage=false` for a valid uploaded blank PDF; this is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, or product-complete.

External reviewer PDF no-text failure candidate runtime request refresh v0: implemented. Boundary: reviewer-facing request surfaces now point to `docs/review/uploaded-pdf-no-text-failure-candidate-runtime-smoke.md` so a reviewer can inspect `pdf_no_extractable_text`, `chunk_handoff_no_chunks`, `chunk_count=0`, `page_text_char_counts=[0]`, and `robust_pdf_extraction=false` for a valid blank uploaded PDF; this is request infrastructure only, not a live issue body edit, hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, or product-complete.

External reviewer PDF no-text failure candidate runtime issue-body refresh v0: implemented. Boundary: issue #1 now links `docs/review/uploaded-pdf-no-text-failure-candidate-runtime-smoke.md`, the request refresh, and the issue-body refresh record from `Latest Proof To Inspect`; this is an owner-authored issue body edit only, not external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, layout fidelity, or product-complete.

External feedback current-state PDF no-text failure candidate runtime issue verification v0: implemented. Boundary: current issue #1 has the no-text PDF runtime proof, request refresh, and issue-body refresh links, but the only screened comment is owner-authored by `svy04`, `candidate_count=0`, `draft_count=0`, and external reviewer feedback remains pending.

Uploaded PDF no-text ops summary dashboard v0: implemented. Boundary: `/ops/summary` now exposes `chunk_handoff_no_chunks_count` and `pdf_no_text_failure_candidate_count`, while `/ops/dashboard` shows `No-text PDF Handoffs` and `PDF No-text Failure Candidates`; these are metadata-derived from document `profile_json`, not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, automatic failure-case creation, or product-complete.

Uploaded PDF no-text ops summary dashboard runtime smoke v0: implemented. Boundary: local Docker/FastAPI HTTP verified a valid blank PDF upload increments `chunk_handoff_no_chunks_count` and `pdf_no_text_failure_candidate_count` by `1`, and `/ops/dashboard` contains `No-text PDF Handoffs`, `PDF No-text Failure Candidates`, and the metadata-derived boundary; this is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, automatic failure-case creation, or product-complete.

Persisted document failure candidate draft preview v0: implemented. Boundary: `POST /documents/{document_id}/failure-case-draft-preview` turns a persisted document `profile_json.failure_case_candidate` into a preview-only draft with `human_confirmation_required=true`; it does not create `failure_cases`, does not re-upload the file, and does not claim automatic failure-case creation, robust PDF extraction, hosted deployment evidence, external reviewer feedback, or product-complete.

Persisted document failure candidate draft preview runtime smoke v0: implemented. Boundary: local Docker/FastAPI HTTP verified `GET /health -> 200`, `POST /documents/upload-chunks -> 201`, `POST /documents/{document_id}/failure-case-draft-preview -> 200`, and `GET /failure-cases -> 200`; the preview returned `preview_only_not_persisted`, `human_confirmation_required=true`, `pdf_no_extractable_text`, `persisted_document_failure_case_candidate`, and `failure_case_count_delta=0`. This is not automatic failure-case creation, hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, or product-complete.

External reviewer persisted document failure candidate draft runtime request refresh v0: implemented. Boundary: reviewer-facing request surfaces now point to `docs/review/persisted-document-failure-candidate-draft-preview-runtime-smoke.md` so reviewers can inspect `preview_only_not_persisted`, `human_confirmation_required=true`, `pdf_no_extractable_text`, `persisted_document_failure_case_candidate`, and `failure_case_count_delta=0`; this is request infrastructure only, not a live issue body edit, automatic failure-case creation, hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, or product-complete.

External reviewer persisted document failure candidate draft runtime issue-body refresh v0: implemented. Boundary: issue #1 now links `docs/review/persisted-document-failure-candidate-draft-preview-runtime-smoke.md`, the request refresh, and the issue-body refresh record from `Latest Proof To Inspect`; this is an owner-authored issue body edit only, not external reviewer feedback, hosted deployment evidence, automatic failure-case creation, robust PDF extraction, OCR, or product-complete.

External feedback current-state persisted document failure candidate draft runtime issue verification v0: implemented. Boundary: current issue #1 has the persisted document failure candidate draft runtime proof, request refresh, and issue-body refresh links, but the only screened comment is owner-authored by `svy04`, with `candidate_count=0`, `draft_count=0`, and external reviewer feedback still pending.

Persisted document failure candidate manual handoff smoke v0: implemented. Boundary: route-level smoke verifies a persisted document `profile_json.failure_case_candidate` can become a preview-only draft, be human-confirmed by changing `draft.fix_status` from `draft` to `open`, and then be submitted to the existing `POST /failure-cases -> 201`; this is not automatic failure-case creation, not a confirm endpoint, not hosted deployment evidence, not external reviewer feedback, robust PDF extraction, OCR, or product-complete.

Persisted document failure candidate manual handoff runtime smoke v0: implemented. Boundary: local Docker/FastAPI HTTP verified `GET /health -> 200`, `POST /documents/upload-chunks -> 201`, `POST /documents/{document_id}/failure-case-draft-preview -> 200`, `POST /failure-cases -> 201`, and `GET /failure-cases -> 200`; `failure_case_count_delta=1` after human confirmation changed `draft.fix_status` from `draft` to `open`. This is not automatic failure-case creation, not a confirm endpoint, not hosted deployment evidence, not external reviewer feedback, robust PDF extraction, OCR, or product-complete.

External reviewer persisted document failure candidate manual handoff runtime request refresh v0: implemented. Boundary: reviewer-facing request surfaces now point to `docs/review/persisted-document-failure-candidate-manual-handoff-runtime-smoke.md` so reviewers can inspect `POST /failure-cases -> 201`, `failure_case_count_delta=1`, and the human confirmation step from `draft` to `open`; this is request infrastructure only, not a live issue body edit, automatic failure-case creation, a confirm endpoint, hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, or product-complete.

External reviewer persisted document failure candidate manual handoff runtime issue-body refresh v0: implemented. Boundary: issue #1 now links `docs/review/persisted-document-failure-candidate-manual-handoff-runtime-smoke.md`, the request refresh, and the issue-body refresh record from `Latest Proof To Inspect`; this is an owner-authored issue body edit only, not external reviewer feedback, hosted deployment evidence, automatic failure-case creation, a confirm endpoint, robust PDF extraction, OCR, or product-complete.

External feedback current-state persisted document failure candidate manual handoff runtime issue verification v0: implemented. Boundary: current issue #1 has the persisted document failure candidate manual handoff runtime proof, request refresh, and issue-body refresh links, but the only screened comment is owner-authored by `svy04`, with `candidate_count=0`, `draft_count=0`, and external reviewer feedback still pending.

README latest-marker persisted document failure candidate manual handoff current-state refresh v0: implemented. Boundary: README top markers now point to the persisted document failure candidate manual handoff issue-body refresh and current-state issue verification; external reviewer feedback remains pending, and this is not automatic failure-case creation, a confirm endpoint, hosted deployment evidence, robust PDF extraction, or product-complete.

README latest-marker persisted document failure candidate manual handoff current-state remote verification v0: implemented. Boundary: remote GitHub Actions runs `27021345997` (`CI`) and `27021346012` (`External Feedback Screen`) succeeded on head `448f171512a7aaaf71686d04969b402ccf7c1fce`; the screen success is workflow evidence only, not external reviewer feedback, hosted deployment evidence, automatic failure-case creation, a confirm endpoint, robust PDF extraction, or product-complete.

Application-ready persisted document failure candidate manual handoff refresh v0: implemented. Boundary: application-ready review now surfaces the persisted document failure candidate manual handoff runtime proof and pending-feedback current-state proof; this is application-facing documentation only, not automatic failure-case creation, a confirm endpoint, hosted deployment evidence, robust PDF extraction, or product-complete.

Uploaded PDF downstream handoff v0: implemented. Boundary: `POST /documents/upload-chunk-preview`, `POST /documents/upload-chunks`, and `POST /documents/upload-retrieval-preview` reuse PyMuPDF digital text extraction for uploaded PDF bytes; OCR, table extraction, layout fidelity, robust PDF extraction, raw file storage, hosted deployment evidence, and external reviewer feedback are not claimed.

Uploaded PDF downstream handoff runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP evidence shows uploaded digital PDF bytes flow through PyMuPDF extraction into upload chunk preview, explicit upload-to-chunks persistence, listed chunk lookup, and upload retrieval preview; this is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, or raw file storage.

Uploaded PDF downstream handoff application refresh v0: implemented. Boundary: application-facing docs now point to `docs/review/uploaded-pdf-downstream-handoff-runtime-smoke.md` for the local PDF handoff proof; this is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, or raw file storage.

External reviewer PDF downstream handoff request refresh v0: implemented. Boundary: reviewer-facing request surfaces now point to `docs/review/uploaded-pdf-downstream-handoff-runtime-smoke.md`; this is request infrastructure only, not external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, or raw file storage.

External reviewer PDF downstream handoff issue-body refresh v0: implemented. Boundary: live issue #1 now points reviewers to `docs/review/uploaded-pdf-downstream-handoff-runtime-smoke.md` and `docs/review/external-reviewer-pdf-downstream-handoff-request-refresh.md`; this is an owner-authored issue body edit only, not external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, or raw file storage.

External feedback current-state PDF downstream handoff issue verification v0: implemented. Boundary: current issue #1 screen after the PDF downstream handoff issue-body refresh still has `comment_count=1`, `candidate_count=0`, `draft_count=0`, and only a self-authored non-qualifying comment; external reviewer feedback remains pending.

Uploaded PDF retrieval-run provenance v0: implemented. Boundary: PDF-derived upload chunk rows now carry `parser`, `digital_pdf_text_extraction`, and `robust_pdf_extraction` metadata into persisted document retrieval-run candidate provenance; this is route-level proof only, not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Evidence Ledger generation, Noise Gate behavior, or report generation.

Uploaded PDF retrieval-run provenance runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP evidence shows uploaded digital PDF bytes flow through `POST /documents/upload-chunks` into `POST /documents/{document_id}/retrieval-runs` while preserving `candidate_parsers -> pdf-pymupdf`; this is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Evidence Ledger generation, Noise Gate behavior, or report generation.

Uploaded PDF retrieval-run-linked Evidence Ledger provenance v0: implemented. Boundary: retrieval-run-linked Evidence Ledger entries now persist candidate chunk parser/source provenance in `metadata_json`, including `parser -> pdf-pymupdf`, `digital_pdf_text_extraction -> true`, and `robust_pdf_extraction -> false`; this is route-level/schema proof only, not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Noise Gate behavior, or report generation.

Uploaded PDF retrieval-run-linked Evidence Ledger provenance runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP evidence shows uploaded digital PDF bytes flow through `POST /documents/upload-chunks`, `POST /documents/{document_id}/retrieval-runs`, `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`, and `GET /evidence-ledgers?retrieval_run_id=` while preserving `metadata_json.parser -> pdf-pymupdf` on the persisted Evidence Ledger row; this is not hosted deployment evidence, external reviewer feedback, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Noise Gate behavior, or report generation.

External reviewer PDF retrieval-run-linked Evidence Ledger provenance request refresh v0: implemented. Boundary: reviewer-facing request surfaces now point to `docs/review/uploaded-pdf-retrieval-run-linked-evidence-ledger-provenance-runtime-smoke.md`; this is request infrastructure only, not a live public issue body edit, not external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Noise Gate behavior, or report generation.

External reviewer PDF retrieval-run-linked Evidence Ledger provenance issue-body refresh v0: implemented. Boundary: live issue #1 now points reviewers to `docs/review/uploaded-pdf-retrieval-run-linked-evidence-ledger-provenance-runtime-smoke.md` and `docs/review/external-reviewer-pdf-retrieval-run-linked-evidence-ledger-provenance-request-refresh.md`; this is an owner-authored issue body edit only, not external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Noise Gate behavior, or report generation.

External feedback current-state PDF retrieval-run-linked Evidence Ledger provenance issue verification v0: implemented. Boundary: current issue #1 screen after the PDF retrieval-run-linked Evidence Ledger provenance issue-body refresh still has `comment_count=1`, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, and only a self-authored non-qualifying comment; external reviewer feedback remains pending.

External reviewer PDF retrieval-run provenance request refresh v0: implemented. Boundary: reviewer-facing request surfaces now point to `docs/review/uploaded-pdf-retrieval-run-provenance-runtime-smoke.md`; this is request infrastructure only, not a live public issue body edit, not external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Evidence Ledger generation, Noise Gate behavior, or report generation.

External reviewer PDF retrieval-run provenance issue-body refresh v0: implemented. Boundary: live issue #1 now points reviewers to `docs/review/uploaded-pdf-retrieval-run-provenance-runtime-smoke.md` and `docs/review/external-reviewer-pdf-retrieval-run-provenance-request-refresh.md`; this is an owner-authored issue body edit only, not external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, layout fidelity, raw file storage, full parsed text persistence, Evidence Ledger generation, Noise Gate behavior, or report generation.

External feedback current-state PDF retrieval-run provenance issue verification v0: implemented. Boundary: current issue #1 screen after the PDF retrieval-run provenance issue-body refresh still has `comment_count=1`, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, and only a self-authored non-qualifying comment; external reviewer feedback remains pending.

ci node24 actions runtime opt-in v0: implemented. Boundary: `.github/workflows/ci.yml` and `.github/workflows/external-feedback-screen.yml` set `FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: "true"` after the remote run warned that Node.js 20 actions are deprecated; this is workflow runtime compatibility only, not product runtime evidence.

ci node24 actions runtime remote verification v0: implemented. Boundary: remote runs `26870586255` (`CI`) and `26870586219` (`External Feedback Screen`) succeeded on head `c3c6908`; the annotation is still present as a forced Node.js 24 runtime warning, so this is compatibility evidence only, not product runtime evidence.

ci node24 action version refresh v0: implemented. Boundary: workflow action references were refreshed to upstream current refs after the forced Node.js 24 runtime warning remained; this is workflow runtime compatibility only, and the remote annotation result remains unverified until the next push.

ci node24 action version remote verification v0: implemented. Boundary: remote runs `26969000702` (`CI`) and `26969000663` (`External Feedback Screen`) succeeded on head `83fb603`; check-run annotations were empty and no Node.js 20 forced-runtime warning was observed in logs, so this is workflow runtime compatibility evidence only, not product runtime evidence.

testclient dependency warning cleanup v0: implemented. Boundary: API test dependencies now include `httpx2>=2.3.0`, and pytest treats `StarletteDeprecationWarning` as an error so deprecated TestClient fallback warnings cannot quietly pass locally; remote warning result remains unverified until the next push.

testclient dependency warning remote verification v0: implemented. Boundary: remote runs `26969672909` (`CI`) and `26969672911` (`External Feedback Screen`) succeeded on head `29f1afa`; CI check-run annotations were empty and no `StarletteDeprecationWarning` / TestClient fallback warning was observed, but generic `warning` text still appears in unrelated checkout hints and external-feedback JSON fields.


Uploaded raw file download endpoint review v0: implemented. Boundary: source-first review selects a future scan-first `GET /documents/upload-raw-files/{raw_file_id}/download` route that requires the latest clean scan result and keeps authorization / download rate limit explicit; review-only, not endpoint code, not a download endpoint, not malware scanning evidence, and not product-complete.

Guarded raw file download endpoint v0: implemented. Boundary: explicit `GET /documents/upload-raw-files/{raw_file_id}/download` returns raw bytes only when the latest scan result is `completed / clean`; missing scan evidence or latest non-clean result returns `409`; local v0 keeps authorization as no-auth/not-production, so this is not production malware scanning evidence, not hosted deployment evidence, and not product-complete.

Guarded raw file download endpoint runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP proved upload -> no-scan download `409` -> clean scan metadata -> download `200` with raw bytes and nosniff/download headers -> later failed scan metadata -> download `409`; not hosted deployment evidence, not external reviewer feedback, not production malware scanning evidence, and not product-complete.

External reviewer guarded download request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to the guarded raw file download runtime smoke; this is not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not production malware scanning evidence, and not product-complete.

External review issue body guarded download refresh v0: implemented. Boundary: issue #1 now points to the guarded raw file download runtime smoke and its reviewer request refresh; owner-authored issue body edit only, not external reviewer feedback, not hosted deployment evidence, not production malware scanning evidence, not production authorization, and not enforced download rate limiting.

External feedback current-state guarded download issue verification v0: implemented. Boundary: current issue #1 screen after the guarded download issue-body refresh still has `comment_count=1`, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, and only a self-authored non-qualifying comment; external reviewer feedback remains pending.

Uploaded raw file download rate limit review v0: implemented. Boundary: source-first review selects a future local in-memory fixed-window download rate limit for the guarded raw file endpoint; review-only, not endpoint code, not an enforced rate limit, not production authorization, not hosted deployment evidence, and not product-complete.

Uploaded raw file download rate limit local v0: implemented. Boundary: guarded raw file download now has a per-process in-memory fixed-window local rate limit: 5 attempts per 60 seconds per raw_file_id/client-host key, returning `429` with no raw bytes when exceeded; not distributed rate limiting, not production authorization, not hosted deployment evidence, and not product-complete.

Uploaded raw file download rate limit runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP verified `[409, 409, 409, 409, 409] -> 429` for repeated same-file no-scan downloads and `200` for a separate clean download with local rate-limit/no-auth/nosniff headers; not distributed rate limiting, production authorization, hosted deployment evidence, or product-complete.

External reviewer rate-limit request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to the guarded raw file download rate-limit runtime smoke; this is not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not distributed rate limiting, not production authorization, and not product-complete.

External review issue body rate-limit refresh v0: implemented. Boundary: issue #1 now points to the guarded raw file download rate-limit runtime smoke and its reviewer request refresh; owner-authored issue body edit only, not external reviewer feedback, not hosted deployment evidence, not distributed rate limiting, not production authorization, and not endpoint malicious-detection runtime proof.

External feedback current-state rate-limit issue verification v0: implemented. Boundary: current issue #1 screen after the rate-limit issue-body refresh still has `comment_count=1`, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, and only a self-authored non-qualifying comment; external reviewer feedback remains pending.

Uploaded raw file signature validation review v0: implemented. Boundary: source-first review selects a future local magic-prefix allowlist boundary for PDF/CSV/HTML/markdown inputs; review-only, not endpoint code, not an enforced signature validator, not malware scanning evidence, and not production authorization.

Uploaded raw file signature validation local v0: implemented. Boundary: `POST /documents/upload-raw-files` now runs a local magic-prefix allowlist check before persistence, accepts CSV despite spoofed Content-Type metadata, and blocks declared PDF without a `%PDF-` prefix with `415`; not robust file-type detection, malware scanning evidence, production authorization, or product-complete.

Uploaded raw file signature validation runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP verified spoofed CSV upload `201`, declared PDF mismatch `415`, no raw bytes in the blocked response, and no recent persistence of the mismatch hash; not robust file-type detection, malware scanning evidence, production authorization, hosted deployment evidence, or product-complete.

External reviewer signature-validation request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to the raw file signature validation runtime smoke; this is not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not robust file-type detection, not malware scanning evidence, and not production authorization.

External review issue body signature-validation refresh v0: implemented. Boundary: issue #1 now points to the raw file signature validation runtime smoke and its reviewer request refresh; owner-authored issue body edit only, not external reviewer feedback, not hosted deployment evidence, not robust file-type detection, not malware scanning evidence, and not production authorization.

External feedback current-state signature-validation issue verification v0: implemented. Boundary: current issue #1 screen after the signature-validation issue-body refresh still has `comment_count=1`, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, and only a self-authored non-qualifying comment; external reviewer feedback remains pending.

Uploaded raw file extension allowlist review v0: implemented. Boundary: source-first review selects a future local filename extension allowlist for raw uploads, validating after filename decoding and naming double-extension/null-byte bypass cases; review-only, not endpoint code, not an enforced extension validator, not robust file-type detection, not malware scanning evidence, and not production authorization.

Uploaded raw file extension allowlist local v0: implemented. Boundary: `POST /documents/upload-raw-files` now validates filename extensions before raw byte persistence, records `local_v0_extension_allowlist_not_production`, accepts allowed CSV filenames, and blocks `sample.exe.csv` double-extension uploads with `415` and no raw bytes; not robust file-type detection, malware scanning evidence, production authorization, hosted proof, or product-complete.

Uploaded raw file extension allowlist runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP verified allowed CSV upload `201` with extension boundary warnings, `sample.exe.csv` double-extension block `415`, no raw bytes in responses, and no recent persistence of the blocked content hash; not robust file-type detection, malware scanning evidence, production authorization, hosted deployment evidence, or product-complete.

External reviewer extension-allowlist request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to the raw file extension allowlist runtime smoke; this is not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not robust file-type detection, not malware scanning evidence, and not production authorization.

External review issue body extension-allowlist refresh v0: implemented. Boundary: issue #1 now points to the raw file extension allowlist runtime smoke and its reviewer request refresh; owner-authored issue body edit only, not external reviewer feedback, not hosted deployment evidence, not robust file-type detection, not malware scanning evidence, and not production authorization.

External feedback current-state extension-allowlist issue verification v0: implemented. Boundary: current issue #1 screen after the extension-allowlist issue-body refresh still has `comment_count=1`, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, and only a self-authored non-qualifying comment; external reviewer feedback remains pending.

Uploaded raw file download filename safety local v0: implemented. Boundary: guarded raw file downloads now expose `local_v0_content_disposition_filename_safety_not_production`, derive a conservative ASCII attachment filename, cap it at 120 characters, and fall back to `raw-file-<uuid>.bin` when normalization empties the candidate; not production authorization, hosted proof, robust file serving, or product-complete.

Uploaded raw file download filename safety runtime smoke v0: implemented. Boundary: local Docker FastAPI verified a path/encoded-control/overlong CSV filename downloads with `local_v0_content_disposition_filename_safety_not_production`, a 120-character safe attachment filename, no path/dotdot/CRLF/injected-label content, and preserved `.csv`; not production authorization, hosted proof, malware detection proof, or product-complete.

External reviewer filename-safety request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to the raw file download filename safety runtime smoke; this is not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not production authorization, not malware detection proof, and not product-complete.

External review issue body filename-safety refresh v0: implemented. Boundary: issue #1 now points to the raw file download filename safety runtime smoke and its reviewer request refresh; owner-authored issue body edit only, not external reviewer feedback, not hosted deployment evidence, not production authorization, not malware detection proof, and not product-complete.

External feedback current-state filename-safety issue verification v0: implemented. Boundary: current issue #1 screen after the filename-safety issue-body refresh still has `comment_count=1`, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, and only a self-authored non-qualifying comment; external reviewer feedback remains pending.

Uploaded raw file download authorization audit review v0: implemented. Boundary: source-first review selects a future `raw_file_download_events` audit schema before any production authorization claim; review-only, not endpoint code, not schema, not user identity, not hosted deployment evidence, and not product-complete.

Uploaded raw file download audit schema v0: implemented. Boundary: `raw_file_download_events` now records guarded raw file download decisions for missing scan, rate-limited, and allowed paths, with local v0 boundary strings; this is audit persistence only, not production authorization, not user identity, not hosted deployment evidence, and not product-complete.

Uploaded raw file download audit runtime smoke v0: implemented. Boundary: local Docker FastAPI plus PostgreSQL verified missing-scan 409, rate-limited `[409, 409, 409, 409, 409, 429]`, and allowed 200 download decisions are persisted and inspectable through download events; not production authorization, not user identity, not hosted deployment evidence, not malware detection proof, and not product-complete.

External reviewer download-audit request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to the raw file download audit runtime smoke; this is not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not production authorization, not user identity, not malware detection proof, and not product-complete.

External review issue body download-audit refresh v0: implemented. Boundary: issue #1 now points to the raw file download audit runtime smoke and its reviewer request refresh; owner-authored issue body edit only, not external reviewer feedback, not hosted deployment evidence, not production authorization, not user identity, not malware detection proof, and not product-complete.

External feedback current-state download-audit issue verification v0: implemented. Boundary: current issue #1 screen after the download-audit issue-body refresh still has `comment_count=1`, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, and only a self-authored non-qualifying comment; external reviewer feedback remains pending.

Uploaded raw file download authorization gate review v0: implemented. Boundary: source-first review selects a future `raw_file_download_approvals` manual approval schema before any production authorization claim; review-only, not endpoint code, not schema, not user identity, not signed URL support, not RBAC, and not product-complete.

Uploaded raw file download approval schema v0: implemented. Boundary: `raw_file_download_approvals` now exists in the fresh schema and migration 021 as a local manual approval table; download route behavior is unchanged, and this is not endpoint code, not repository code, not production authorization, not user identity, not signed URL support, and not product-complete.

Uploaded raw file download approval schema runtime verification v0: implemented. Boundary: local Docker DB migration runner applied `021_raw_file_download_approvals.sql` and status reached `Applied migrations: 20`, `Pending migrations: 0`; table columns, indexes, and constraints were introspected; not endpoint code, not repository code, not production authorization, not user identity, and not product-complete.

Uploaded raw file download approval repository review v0: implemented. Boundary: review-only selection of `RawFileDownloadApprovalCreate`, `RawFileDownloadApprovalOut`, `create_raw_file_download_approval`, and `list_raw_file_download_approvals`; no repository code, endpoint code, download route behavior, production authorization, user identity, signed URL support, RBAC, or product-complete claim.

Uploaded raw file download approval repository v0: implemented. Boundary: repository-only caller-provided manual approval rows through `RawFileDownloadApprovalCreate`, `RawFileDownloadApprovalOut`, `create_raw_file_download_approval`, and `list_raw_file_download_approvals`; no endpoint code, download route behavior, production authorization, user identity, signed URL support, RBAC, or product-complete claim.

Uploaded raw file download approval endpoint review v0: implemented. Boundary: review-only selection of metadata-only `POST /documents/upload-raw-files/{raw_file_id}/download-approvals` and `GET /documents/upload-raw-files/{raw_file_id}/download-approvals`; no endpoint code, download route behavior, approval enforcement, production authorization, user identity, signed URL support, RBAC, or product-complete claim.

Uploaded raw file download approval endpoint v0: implemented. Boundary: metadata-only create/list endpoints for caller-provided manual approval rows; download route behavior still requires latest clean scan result, and this is not approval enforcement, production authorization, user identity, signed URL support, RBAC, hosted evidence, or product-complete claim.

Uploaded raw file download approval endpoint runtime smoke v0: implemented. Boundary: local Docker FastAPI plus PostgreSQL verified approval metadata create/list over HTTP and confirmed approval metadata did not override the latest clean scan guard; not approval enforcement, production authorization, user identity, signed URL support, hosted evidence, or product-complete claim.

Uploaded raw file download approval gate behavior review v0: implemented. Boundary: source-first review selects `find_active_raw_file_download_approval` as the next helper gate before changing raw download route behavior; not route behavior, approval enforcement, production authorization, user identity, signed URL support, RBAC, hosted evidence, or product-complete claim.

Uploaded raw file download approval helper v0: implemented. Boundary: repository-only `find_active_raw_file_download_approval` returns one approved, unexpired, non-revoked row for a raw file and latest scan result; not route behavior, approval enforcement, production authorization, user identity, signed URL support, RBAC, hosted evidence, or product-complete claim.

Uploaded raw file download approval gate behavior v0: implemented. Boundary: guarded raw downloads now require latest clean scan and active approval; missing/expired approval attempts are blocked and audited, allowed events include `download_approval_id` in metadata_json; not production authorization, user identity, signed URL support, RBAC, hosted evidence, or product-complete claim.

Uploaded raw file download approval gate behavior runtime smoke v0: implemented. Boundary: local Docker FastAPI plus PostgreSQL verified `missing_download_approval`, `revoked_or_expired_download_approval`, and active approval 200 paths after migration 022 aligned the audit event blocked-reason constraint; not production authorization, user identity, signed URL support, RBAC, hosted evidence, or product-complete claim.

External reviewer approval-gate request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to the raw file download approval gate behavior runtime smoke; this is not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not production authorization, not user identity, not signed URL support, and not product-complete.

External review issue body approval-gate refresh v0: implemented. Boundary: issue #1 now points to the approval gate behavior runtime smoke and its reviewer request refresh; owner-authored issue body edit only, not external reviewer feedback, not hosted deployment evidence, not production authorization, not user identity, not signed URL support, and not product-complete.

External feedback current-state approval-gate issue verification v0: implemented. Boundary: current issue #1 screen after the approval-gate issue-body refresh still has `comment_count=1`, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, and only a self-authored non-qualifying comment; external reviewer feedback remains pending.

Uploaded raw file download approval input guard v0: implemented. Boundary: `RawFileDownloadApprovalCreate` now rejects unknown approval statuses and rejects already expired `approved` approvals before they can become active approval metadata, while `RawFileDownloadApprovalOut` remains separate for historical audit rows; this is local v0 API/model input validation, not production authorization, not user identity, not signed URL support, not hosted evidence, and not product-complete.

Uploaded raw file download approval input guard runtime smoke v0: implemented. Boundary: local Docker FastAPI plus PostgreSQL verified valid approval metadata create/list, unknown approval status `422`, and already expired active approval `422`; this is local runtime evidence only, not production authorization, not authenticated user identity, not signed URL support, not hosted evidence, and not product-complete.

External reviewer approval-input guard request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to the raw file download approval input guard runtime smoke; this is not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not production authorization, not authenticated user identity, not signed URL support, and not product-complete.

External review issue body approval-input guard refresh v0: implemented. Boundary: issue #1 now points to the approval input guard runtime smoke and its reviewer request refresh; owner-authored issue body edit only, not external reviewer feedback, not hosted deployment evidence, not production authorization, not authenticated user identity, not signed URL support, and not product-complete.

External feedback current-state approval-input guard issue verification v0: implemented. Boundary: current issue #1 screen after the approval-input guard issue-body refresh still has `comment_count=1`, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, and only a self-authored non-qualifying comment; external reviewer feedback remains pending.

Uploaded raw file download approval audit metadata v0: implemented. Boundary: allowed raw file download audit events now include approval status, expiry, latest scan-result reference, scan-match boolean, approval boundary, identity boundary, and operator label; this is local v0 audit metadata only, not production authorization, not authenticated user identity, not signed URL support, not hosted evidence, and not product-complete.

Uploaded raw file download approval audit metadata runtime smoke v0: implemented. Boundary: local Docker FastAPI plus PostgreSQL verified upload, clean scan metadata, active approval, download `200`, and allowed audit event metadata with approval id/status/expiry/latest-scan-match/identity boundary; this is local runtime evidence only, not production authorization, not authenticated user identity, not signed URL support, not hosted evidence, and not product-complete.

External reviewer approval-audit-metadata request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to the raw file download approval audit metadata runtime smoke; this is not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not production authorization, not authenticated user identity, not signed URL support, and not product-complete.

External review issue body approval-audit-metadata refresh v0: implemented. Boundary: issue #1 now points to the approval audit metadata runtime smoke and its reviewer request refresh; owner-authored issue body edit only, not external reviewer feedback, not hosted deployment evidence, not production authorization, not authenticated user identity, not signed URL support, and not product-complete.

External feedback current-state approval-audit-metadata issue verification v0: implemented. Boundary: current issue #1 screen after the approval-audit-metadata issue-body refresh still has `comment_count=1`, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, and only a self-authored non-qualifying comment; external reviewer feedback remains pending.

Uploaded raw file download readiness preview v0: implemented. Boundary: `GET /documents/upload-raw-files/{raw_file_id}/download-readiness` reports whether latest clean scan, quarantine status, and active local manual approval currently satisfy the guarded download preconditions; it returns no raw bytes, consumes no download rate-limit attempt, and writes no download audit event. This is local v0 preflight only, not production authorization, not authenticated user identity, not signed URL support, not RBAC/ABAC/ReBAC, not hosted evidence, and not product-complete.

Uploaded raw file download readiness runtime smoke v0: implemented. Boundary: local Docker FastAPI plus PostgreSQL verified readiness before scan (`missing_clean_scan`), after clean scan without approval (`missing_download_approval`), and after clean scan plus active approval (`allowed`), while `raw_bytes_returned=false`, `rate_limit_consumed=false`, and `events_after_readiness_count=0`; not production authorization, not authenticated user identity, not signed URL support, not hosted evidence, not external reviewer feedback, and not product-complete.

External reviewer readiness-runtime request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to the raw file download readiness runtime smoke; this is not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not production authorization, not authenticated user identity, not signed URL support, and not product-complete.

External review issue body readiness-runtime refresh v0: implemented. Boundary: issue #1 now points reviewers to the readiness runtime smoke and its reviewer request refresh; owner-authored issue body edit only, not external reviewer feedback, not hosted deployment evidence, not production authorization, not authenticated user identity, not signed URL support, and not product-complete.

External feedback current-state readiness-runtime issue verification v0: implemented. Boundary: current issue #1 screen after the readiness-runtime issue-body refresh still has `comment_count=1`, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, and only a self-authored non-qualifying comment; external reviewer feedback remains pending.

Uploaded raw file guard ops summary v0: implemented. Boundary: `GET /ops/summary` and `GET /ops/dashboard` now surface raw-file guard counts for uploaded raw files, scan results, clean/error scans, download approvals, active approvals, download events, blocked downloads, and allowed downloads; this is local operations metadata only, not download readiness call persistence, production authorization, authenticated user identity, signed URL support, hosted evidence, external reviewer feedback, or product-complete.

Uploaded raw file guard ops summary runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP verified raw upload, blocked missing-scan download, failed scan metadata, clean scan metadata, active approval, allowed download, expected `/ops/summary` counter deltas, and `/ops/dashboard` metric labels; not production authorization, authenticated identity, signed URL support, hosted deployment evidence, external reviewer feedback, or product-complete.

External reviewer raw-file guard ops summary request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to the raw-file guard ops summary runtime smoke; this is not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not production authorization, not authenticated identity, not signed URL support, and not product-complete.

External review issue body raw-file guard ops summary refresh v0: implemented. Boundary: issue #1 now points reviewers to the raw-file guard ops summary runtime smoke and its reviewer request refresh; owner-authored issue body edit only, not external reviewer feedback, not hosted deployment evidence, not production authorization, not authenticated identity, not signed URL support, and not product-complete.

External feedback current-state raw-file guard ops summary issue verification v0: implemented. Boundary: current issue #1 has the raw-file guard ops summary proof/request links, but `comment_count=1`, `candidate_count=0`, `draft_count=0`, and only a self-authored non-qualifying comment; external reviewer feedback remains pending.

External reviewer workflow proof bundle request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to the workflow proof bundle runtime smoke; this is not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, not distributed tracing, not hosted observability, not new lineage storage, and not product-complete.

External review issue body workflow proof bundle refresh v0: implemented. Boundary: issue #1 now points reviewers to the workflow proof bundle runtime smoke and its request refresh; owner-authored issue body edit only, not external reviewer feedback, not hosted deployment evidence, not distributed tracing, not hosted observability, not new lineage storage, and not product-complete.

External feedback current-state workflow proof bundle issue verification v0: implemented. Boundary: current issue #1 has the workflow proof bundle proof/request links, but `comment_count=1`, `screened_comment_count=1`, `candidate_count=0`, `draft_count=0`, and only a self-authored non-qualifying comment; external reviewer feedback remains pending.

Workflow proof bundle dashboard link v0: implemented. Boundary: `GET /ops/dashboard` workflow rows now link to the existing `GET /workflow-runs/{id}/proof-bundle` read model; this is dashboard navigation only, not a new endpoint, schema, migration, lineage storage, distributed tracing, hosted observability, external reviewer feedback, or product-complete claim.

Workflow proof bundle dashboard runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP verified `GET /ops/dashboard` includes the workflow proof bundle link and `GET /workflow-runs/{id}/proof-bundle` returns `200`; this is not new endpoint behavior, schema, migration, lineage storage, distributed tracing, hosted observability, hosted deployment evidence, external reviewer feedback, or product-complete.

Workflow proof bundle markdown export v0: implemented. Boundary: `GET /workflow-runs/{id}/proof-bundle/markdown` renders the existing workflow proof bundle read model as `text/markdown; charset=utf-8`, and `GET /ops/dashboard` exposes a GET-only `proof markdown` link. This is read-only rendering only, not new storage, distributed tracing, hosted observability, semantic retrieval quality evidence, external reviewer feedback, or product-complete.

Workflow proof bundle markdown export runtime smoke v0: implemented. Boundary: local Docker PostgreSQL plus live FastAPI HTTP verified `GET /ops/dashboard -> 200`, dashboard `proof markdown` link discovery, and `GET /workflow-runs/{id}/proof-bundle/markdown -> 200` returning `text/markdown; charset=utf-8`; this is not hosted deployment evidence, external reviewer feedback, distributed tracing, hosted observability, semantic retrieval quality evidence, or product-complete.

External-reader proof path workflow markdown runtime route refresh v0: implemented. Boundary: `docs/review/external-reader-proof-path.md` and the README External Reviewer Fast Path now start first-pass readers with `docs/review/workflow-proof-bundle-markdown-export-runtime-smoke.md`, while preserving workflow checklist dashboard runtime and report markdown inspection paths as predecessor proof. This is reader-route alignment only, not new runtime evidence, not a live issue body edit, not external reviewer feedback, not hosted deployment evidence, and not product-complete.

External-reader proof path workflow markdown runtime route refresh remote verification v0: implemented. Boundary: pushed route-refresh commit `2c5fd10a990887cd6baeb288aa7c83918dc303ba` passed CI run `27055679959` and External Feedback Screen run `27055679968`; this is remote workflow verification only, not the reader-route refresh itself, not external reviewer feedback, not hosted deployment evidence, and not product-complete.

External review issue body workflow markdown runtime route refresh v0: implemented. Boundary: issue #1 now points `Latest Proof To Inspect` to `docs/review/workflow-proof-bundle-markdown-export-runtime-smoke.md`, the workflow markdown route refresh, and its remote verification; this is owner-authored issue routing only, not external reviewer feedback, not hosted deployment evidence, and not product-complete.

External feedback current-state workflow markdown issue verification v0: implemented. Boundary: issue #1 still has only owner-authored non-qualifying feedback after the workflow markdown issue-body refresh, with `candidate_count=0`, `draft_count=0`, `reason=self_authored_comment`, and `status=pending`; this is current-state issue screening only, not external reviewer feedback, hosted deployment evidence, or product-complete.

External feedback current-state workflow markdown issue verification remote verification v0: implemented. Boundary: pushed issue-screen commit `ea58f7ecedb2d0f3a5e839d6ba2c62def3e1bee4` passed CI run `27056276600` and External Feedback Screen run `27056276610`; this is remote workflow verification only, not the current-state issue screen itself, not external reviewer feedback, hosted deployment evidence, or product-complete.

External reviewer workflow proof bundle dashboard runtime request refresh v0: implemented. Boundary: reviewer-facing repository paths now link to `docs/review/workflow-proof-bundle-dashboard-runtime-smoke.md` and `docs/review/external-reviewer-workflow-proof-bundle-dashboard-runtime-request-refresh.md`; this is not a live issue body edit, external reviewer feedback, hosted deployment evidence, distributed tracing, hosted observability, new lineage storage, or product-complete.

External review issue body workflow proof bundle dashboard runtime refresh v0: implemented. Boundary: issue #1 body now points reviewers to `docs/review/workflow-proof-bundle-dashboard-runtime-smoke.md`, `docs/review/external-reviewer-workflow-proof-bundle-dashboard-runtime-request-refresh.md`, and `docs/review/external-review-issue-body-workflow-proof-bundle-dashboard-runtime-refresh.md`; this is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, distributed tracing, hosted observability, new lineage storage, or product-complete.

External feedback current-state workflow proof bundle dashboard runtime issue verification v0: implemented. Boundary: current issue #1 has the dashboard runtime proof, request refresh, and issue-body refresh links, but the only screened comment is owner-authored, `candidate_count=0`, `draft_count=0`, and external reviewer feedback remains pending.

External reviewer shortlist v0: implemented. Boundary: `docs/review/external-reviewer-shortlist.md` gives outside reviewers a 90-second shortlist with a maximum five proof artifacts before the full proof path; this is reviewer navigation only, not external reviewer feedback, hosted deployment evidence, customer validation, Braincrew acceptance, or product-complete.

External review issue body shortlist refresh v0: implemented. Boundary: issue #1 body now starts its Fast Path with `docs/review/external-reviewer-shortlist.md`; this is owner-authored issue routing only, not external reviewer feedback, hosted deployment evidence, customer validation, Braincrew acceptance, or product-complete.

External feedback current-state shortlist issue verification v0: implemented. Boundary: current issue #1 starts its Fast Path with `docs/review/external-reviewer-shortlist.md`, but the only screened comment is owner-authored, `candidate_count=0`, `draft_count=0`, and external reviewer feedback remains pending.

## Planned Agent Workflow

NoiseProof Agent will use five explicit roles before introducing any complex multi-agent abstraction:

1. Ingestion Agent: parse and profile inputs
2. Retrieval Agent: compare chunk strategies and retrieve source-linked evidence
3. Analysis Agent: draft claims from retrieved evidence
4. Critic Agent: block unsupported claims, contradictions, overconfident language, missing limitations, and trading-advice drift
5. Report Agent: generate a claim-bounded report with citations and next data needed

Each planned stage must log its input and output.

Auto Trace behavior records preview endpoint metadata in `agent_runs.trace_json` using the current workflow version. This is not full workflow tracing or distributed observability.

## Evidence Ledger

The Evidence Ledger is the control surface between retrieval and final answer generation. Phase 6 implements a deterministic preview boundary. Phase 12 persists generated ledger entries so operations views can count unsupported and contradicted claims. Phase 202 adds a retrieval-run-linked handoff endpoint that reads a persisted retrieval run's `metadata_json.candidate_chunk_ids`, reloads the referenced `document_chunks`, and stores Evidence Ledger rows with `retrieval_run_id`.

Each ledger entry records:

- claim
- source id
- source type
- source date
- evidence span
- confidence
- limitation
- contradicting source ids
- status

Allowed status values:

```text
supported
weakly_supported
contradicted
unsupported
blocked
```

The system should generate the ledger before generating a final report. Current persistence is v0, and retrieval-run-linked rows can now carry `retrieval_run_id` when created through `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`.

## Noise Gate

The Noise Gate is the reviewer before a final response is allowed through. Phase 7 implements a deterministic preview boundary. Phase 13 persists gate decisions so blocked and revision-needed outputs remain inspectable. Phase 204 adds a retrieval-run-linked handoff endpoint that requires persisted Evidence Ledger rows for the same retrieval run before creating a Noise Gate record.

It checks:

- Does every strong claim have evidence?
- Are there at least two sources for high-confidence claims?
- Is source recency visible?
- Are contradictions surfaced?
- Are quantitative and qualitative signals separated?
- Is the answer drifting into trading advice?
- Are limitations explicit?

The current preview returns `pass`, `needs_revision`, or `blocked`. `POST /noise-gates` stores the decision and checks. It does not generate the final report.

If the gate fails, the system should return:

```text
현재 근거만으로는 결론을 내릴 수 없습니다. 가능한 해석은 다음과 같고, 추가로 확인해야 할 데이터는 다음과 같습니다.
```

## Evaluation

Evaluation is organized around inspectability, not polished demo output.

The Phase 10 evaluation package tracks:

- sample dataset description
- retrieval hit rate
- citation coverage
- missing evidence count
- unsupported claim examples
- contradiction examples
- failure cases and next fixes

See:

- `docs/evaluation/eval-plan.md`
- `docs/evaluation/retrieval-eval-report.md`
- `docs/evaluation/failure-cases.md`

The project does not claim model quality, semantic retrieval quality, or answer quality success.

Semantic retrieval quality report regeneration:

- command: `uv run python -m app.services.semantic_quality_report_command`
- proof: `docs/review/semantic-retrieval-quality-report-regeneration-command.md`
- failure boundary: `docs/review/semantic-retrieval-quality-report-regeneration-failure-boundary.md`
- check mode: `docs/review/semantic-retrieval-quality-report-check-mode.md`
- CI staleness check: `docs/review/semantic-retrieval-quality-report-ci-check.md`

This provides byte-for-byte regeneration and CI staleness detection for the toy semantic retrieval quality report. It is not vector search quality evidence, not a benchmark result, and not a model comparison.

## Failure Cases

Failure cases are first-class artifacts. The planned system will record:

- failed questions
- retrieval misses
- unsupported claims
- contradicted claims
- trading-advice drift
- missing source recency
- parser failures
- root cause and next action

## Local Setup

The current local stack defines a PostgreSQL + pgvector database service and a FastAPI skeleton.

```bash
cp .env.example .env
docker compose up -d db
cd apps/api
uv sync
uv run uvicorn app.main:app --reload
```

Smoke checks:

```bash
curl http://localhost:8000/health
curl http://localhost:8000/ops/summary
curl http://localhost:8000/ops/dashboard
curl -X POST http://localhost:8000/documents/profile \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"markdown\",\"text\":\"# Memo\nDate: 2026-05-28\nSource: https://example.com\nRevenue grew 12%.\"}"
curl -X POST http://localhost:8000/documents/parse-preview \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"markdown\",\"content\":\"# Memo\nDate: 2026-05-28\nSource: https://example.com\nRevenue grew 12%.\"}"
curl -X POST http://localhost:8000/documents/chunk-preview \
  -H "Content-Type: application/json" \
  -d "{\"source_type\":\"markdown\",\"content\":\"# Market\nRevenue grew 12% in 2026.\n\n## Risks\nCosts rose 7%.\",\"max_characters\":80,\"overlap\":10}"
curl -X POST http://localhost:8000/retrieval-runs \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"strategy\":\"heading-aware\",\"sources\":[{\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"content\":\"# Demand\nEnterprise demand grew 12% in 2026.\"}]}"
curl -X POST http://localhost:8000/collection-plans/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Did this company's AI narrative become materially stronger?\"}"
curl -X POST http://localhost:8000/evidence-ledgers/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"retrieval_results\":[{\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"chunk_strategy\":\"heading-aware\",\"chunk_index\":0,\"text\":\"Enterprise demand grew 12% in 2026.\",\"score\":0.75,\"matched_terms\":[\"demand\",\"enterprise\",\"growth\"],\"metadata\":{\"source_date\":\"2026-05-28\"}}]}"
curl -X POST http://localhost:8000/evidence-ledgers \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Should I buy this company?\",\"retrieval_results\":[]}"
curl http://localhost:8000/evidence-ledgers
curl -X POST http://localhost:8000/retrieval-runs/<uuid>/evidence-ledger
curl -X POST http://localhost:8000/retrieval-runs/<uuid>/noise-gate
curl -X POST http://localhost:8000/retrieval-runs/<uuid>/report
curl -X POST http://localhost:8000/noise-gates/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"evidence_entries\":[{\"claim\":\"Enterprise demand grew\",\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"source_date\":\"2026-05-28\",\"evidence_span\":\"Enterprise demand grew 12% in 2026.\",\"confidence\":\"medium\",\"limitation\":\"Supported by one retrieved source.\",\"contradicting_source_ids\":[],\"status\":\"supported\",\"matched_terms\":[\"enterprise\",\"demand\",\"growth\"],\"role\":\"direct_support\"}],\"draft_claims\":[\"Enterprise demand grew, with the current evidence limited to one retrieved source.\"]}"
curl -X POST http://localhost:8000/noise-gates \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Should I buy this company?\",\"evidence_entries\":[{\"claim\":\"Should I buy this company\",\"source_id\":null,\"source_type\":null,\"source_date\":null,\"evidence_span\":\"\",\"confidence\":\"none\",\"limitation\":\"Question drifts into buy/sell or financial-advice intent.\",\"contradicting_source_ids\":[],\"status\":\"blocked\",\"matched_terms\":[],\"role\":\"user_intent_check\"}],\"draft_claims\":[\"Should I buy this company?\"]}"
curl http://localhost:8000/noise-gates
curl -X POST http://localhost:8000/reports/preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"evidence_entries\":[{\"claim\":\"Enterprise demand grew\",\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"source_date\":\"2026-05-28\",\"evidence_span\":\"Enterprise demand grew 12% in 2026.\",\"confidence\":\"medium\",\"limitation\":\"Supported by one retrieved source.\",\"contradicting_source_ids\":[],\"status\":\"supported\",\"matched_terms\":[\"enterprise\",\"demand\",\"growth\"],\"role\":\"direct_support\"}],\"draft_claims\":[\"Enterprise demand grew, with the current evidence limited to one retrieved source.\"]}"
curl -X POST http://localhost:8000/workflow-runs/execute-preview \
  -H "Content-Type: application/json" \
  -d "{\"question\":\"Which segment had enterprise demand growth?\",\"strategy\":\"fixed-window\",\"sources\":[{\"source_id\":\"doc-demand\",\"source_type\":\"markdown\",\"content\":\"Enterprise segment demand growth was 12 percent in 2026.\"}],\"draft_claims\":[\"Enterprise segment demand growth was supported by current retrieved evidence.\"]}"
curl http://localhost:8000/workflow-runs/<uuid>
curl http://localhost:8000/workflow-runs/<uuid>/lineage
curl http://localhost:8000/workflow-runs/<uuid>/proof-bundle
curl http://localhost:8000/agent-runs
```

Reviewer-facing public proof route:

```text
docs/review/external-reviewer-live-proof-route-refresh.md
https://svy04.github.io/proof-artifacts/noiseproof-live-route-verification-2026-06-01/
```

This route helps external reviewers find the latest public proof surface, reviewer brief, and issue #1. It is not external reviewer feedback, not hosted deployment evidence for NoiseProof Agent, and not customer validation.

## Demo Flow

Planned demo flow after implementation:

1. Upload or reference messy PDF, CSV, URL/HTML, and markdown memo inputs.
2. Generate a document profile for each input.
3. Compare fixed-window, heading-aware, and row-aware chunk strategies.
4. Create a Collection Plan Preview for a market-intelligence question.
5. Run retrieval for source-linked candidate chunks.
6. Generate an Evidence Ledger Preview before the answer.
7. Ask the Critic Agent to block unsupported claims and surface contradictions.
8. Generate a claim-bounded report preview with citations and limitations.
9. Show the run log and failure case record.

## What I Would Improve Next

The current next evidence gate remains external reviewer feedback v0.

The project already has a reviewer request packet, intake criteria, reviewer brief, direct link map, root review guide, live issue-body encoding verification, live issue-body root-guide verification, live issue-body link-map verification, issue-template link-map refresh, issue-label verification, owner request comment rejection verification, outreach packet, screening CLI, screening workflow, and remote pending artifact verification. Those artifacts prepare the path, but they do not prove that an outside reviewer inspected the work.

The owner approved continuing implementation while that external-review gate stays pending. That approval is recorded in `docs/review/owner-approved-product-continuation-decision.md`; it is not external reviewer feedback, customer validation, Braincrew acceptance, hosted deployment evidence, or production readiness.

File upload preview v0 through uploaded file retrieval persistence application refresh v0 are now implemented as bounded upload proof steps. The current next evidence gate remains `external reviewer feedback v0`; external reviewer feedback is still pending.

The latest current-state screen after the uploaded-file chunk persistence issue-body refresh is recorded in `docs/review/external-feedback-current-state-chunk-issue-verification.md`. It observes `comment_count: 1`, `candidate_count: 0`, and `draft_count: 0`; the only public comment is owner-authored and does not close `external reviewer feedback v0`.

The explicit upload-to-chunks handoff endpoint is now implemented and recorded in `docs/review/uploaded-file-chunk-persistence-handoff-endpoint.md`: `POST /documents/upload-chunks` creates document metadata plus derived chunk rows while keeping the existing upload chunk preview preview-only. Local runtime evidence and application-facing proof refresh for that endpoint are recorded in `docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md` and `docs/review/uploaded-file-chunk-persistence-handoff-application-refresh.md`.

The document-scoped retrieval persistence endpoint is now implemented and recorded in `docs/review/uploaded-file-retrieval-persistence-endpoint.md`: `POST /documents/{document_id}/retrieval-runs` reads existing `document_chunks`, persists one row in the existing `retrieval_runs` table, and stores `metadata_json.candidate_chunk_ids` without adding embeddings, semantic retrieval, Evidence Ledger generation, or financial advice behavior. Local runtime evidence is recorded in `docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md`, and the application-facing refresh is recorded in `docs/review/uploaded-file-retrieval-persistence-application-refresh.md`.

The retrieval-run-linked Evidence Ledger endpoint is implemented as `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`: it uses an existing persisted `retrieval_runs` row and its `metadata_json.candidate_chunk_ids` to reload `document_chunks`, generate deterministic Evidence Ledger entries, and persist those rows with `retrieval_run_id`. Local Docker runtime evidence is recorded in `docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md`. It does not call an LLM, create embeddings, perform semantic retrieval, generate a Noise Gate or report, or provide financial advice.

The retrieval-run-linked Noise Gate endpoint is implemented as `POST /retrieval-runs/{retrieval_run_id}/noise-gate`: it requires existing Evidence Ledger rows linked to that retrieval run, persists a Noise Gate record, and records `stage_input_manifest.input_evidence_ledger_entry_ids`. Local Docker runtime evidence is recorded in `docs/review/retrieval-run-linked-noise-gate-runtime-smoke.md`. It does not call an LLM, create embeddings, perform semantic retrieval, generate a report, create failure cases, or provide financial advice.

The retrieval-run-linked Report endpoint is implemented as `POST /retrieval-runs/{retrieval_run_id}/report`: it requires existing Evidence Ledger rows and a linked Noise Gate record, persists a Report record, and records `stage_input_manifest.input_evidence_ledger_entry_ids` plus `stage_input_manifest.input_noise_gate_record_id`. Local Docker runtime evidence is recorded in `docs/review/retrieval-run-linked-report-runtime-smoke.md`. It does not call an LLM, create embeddings, perform semantic retrieval, create failure cases, or provide financial advice; when the gate requires revision, the report body remains bounded instead of becoming a free-form answer.

## Braincrew Role Alignment

Primary hiring target:

```text
Braincrew Forward Deployed Engineer
```

Secondary / long-term target:

```text
Braincrew Product Engineer
```

NoiseProof Agent is designed to produce evidence for customer problem definition, RAG/agent workflow design, full-stack service implementation, logging, monitoring, evaluation, deployment readiness, and technical decision documentation.

This repository is the implementation artifact. The portfolio blog is the strategy, explanation, and proof surface.

External reviewer PDF table-candidate downstream runtime request refresh v0: implemented. Boundary: reviewer-facing request surfaces now point to `docs/review/uploaded-pdf-table-candidate-downstream-provenance-runtime-smoke.md`, `docs/review/uploaded-pdf-table-candidate-downstream-provenance-remote-verification.md`, and `docs/review/external-reviewer-pdf-table-candidate-downstream-runtime-request-refresh.md`; observed marker `retrieval_candidate_table_candidate_count -> 1`; this is request infrastructure only, not a live public issue body edit, not external reviewer feedback, not hosted deployment evidence, not robust PDF extraction, not table extraction, and not product-complete.

External review issue body PDF table-candidate downstream runtime refresh v0: implemented. Boundary: issue #1 now points reviewers to `docs/review/uploaded-pdf-table-candidate-downstream-provenance-runtime-smoke.md`, `docs/review/uploaded-pdf-table-candidate-downstream-provenance-remote-verification.md`, `docs/review/external-reviewer-pdf-table-candidate-downstream-runtime-request-refresh.md`, and `docs/review/external-review-issue-body-pdf-table-candidate-downstream-runtime-refresh.md`; this is owner-authored issue body routing only, not external reviewer feedback, hosted deployment evidence, robust PDF extraction, OCR, table extraction, Evidence Ledger generation, Noise Gate behavior, report generation, or product-complete.

External feedback current-state PDF table-candidate downstream runtime issue verification v0: implemented. Boundary: current issue #1 points to the table-candidate downstream runtime proof, remote verification, request refresh, and issue-body refresh while screening still reports `candidate_count=0`, `draft_count=0`, `status=pending`, and `self_authored_comment`; this is not external reviewer feedback, hosted deployment evidence, robust PDF extraction, table extraction, or product-complete.

External feedback current-state PDF table-candidate downstream runtime issue verification remote verification v0: implemented. Boundary: remote GitHub Actions runs `27039725653` (`CI`) and `27039725630` (`External Feedback Screen`) succeeded on head `49eed2ac1013a9043c3865f580c4350bb132a4d7`; this is workflow evidence only, not external reviewer feedback, hosted deployment evidence, customer validation, robust PDF extraction, table extraction, or product-complete.

README current proof route table-candidate refresh v0: implemented. Boundary: the first-screen README proof route now points to `docs/review/uploaded-pdf-table-candidate-downstream-provenance-runtime-smoke.md`, its remote verification, request refresh, issue-body refresh, and current-state issue verification; this is route clarity only, not a new runtime smoke, external reviewer feedback, hosted deployment evidence, robust PDF extraction, table extraction, or product-complete.

README current proof route table-candidate refresh remote verification v0: implemented. Boundary: remote GitHub Actions runs `27040299642` (`CI`) and `27040299666` (`External Feedback Screen`) succeeded on head `94d6743743f18d1d4852defc2ea1da578b7e2654`; this is workflow evidence only, not external reviewer feedback, hosted deployment evidence, robust PDF extraction, table extraction, or product-complete.

README latest remote verification marker table-candidate refresh v0: implemented. Boundary: the first-screen README latest remote verification marker now points to `docs/review/readme-current-proof-route-table-candidate-refresh-remote-verification.md`; this is marker clarity only, not external reviewer feedback, hosted deployment evidence, runtime product proof, robust PDF extraction, table extraction, or product-complete.

Docker environment readiness current-state v0: implemented. Boundary: local Docker `29.4.3`, Compose `v5.1.3`, WSL2 `docker-desktop`, isolated `noiseproof-phase611` PostgreSQL/pgvector on `POSTGRES_PORT=55440`, migration status `Pending migrations: 0`, and live local `GET /health` plus `GET /ops/summary` were verified; this is local environment readiness only, not hosted deployment evidence, production orchestration, external reviewer feedback, live OpenAI provider evidence, or product-complete.

Ops summary semantic retrieval boundary note refresh v0: implemented. Boundary: `/ops/summary` now separates implemented caller-provided vector semantic retrieval preview/run paths from still-unproven embedding generation, hosted semantic retrieval quality evidence, distributed tracing, and free-form final report generation; this is wording accuracy only, not live OpenAI provider evidence, semantic retrieval quality evidence, hosted deployment evidence, external reviewer feedback, or product-complete.

Ops summary semantic retrieval boundary note runtime smoke v0: implemented. Boundary: local Docker PostgreSQL/pgvector plus live FastAPI HTTP verified `GET /ops/summary -> 200` and the corrected caller-provided vector semantic retrieval boundary notes; this is local runtime wording evidence only, not live OpenAI provider evidence, semantic retrieval quality evidence, hosted deployment evidence, external reviewer feedback, or product-complete.

Ops summary semantic retrieval operational counts v0: implemented. Boundary: `/ops/summary` now returns `retrieval_run_count`, `semantic_retrieval_run_count`, `chunk_embedding_count`, and `caller_provided_embedding_count`; route-level tests verify one semantic retrieval run with two caller-provided embedding rows surfaces as operational counts. This is not embedding generation, semantic retrieval quality evidence, live OpenAI provider evidence, hosted deployment evidence, external reviewer feedback, or product-complete.

Ops summary semantic retrieval operational counts runtime smoke v0: implemented. Boundary: local Docker PostgreSQL/pgvector plus live FastAPI HTTP verified one semantic retrieval run and two caller-provided embedding rows surfaced in `/ops/summary` as `semantic_retrieval_run_count -> 1`, `chunk_embedding_count -> 2`, and `caller_provided_embedding_count -> 2`; this is local operational count evidence only, not embedding generation, semantic retrieval quality evidence, live OpenAI provider evidence, hosted deployment evidence, external reviewer feedback, or product-complete.

Ops dashboard semantic retrieval operational counts v0: implemented. Boundary: `/ops/dashboard` now renders `Retrieval Runs Recorded`, `Semantic Retrieval Runs`, `Chunk Embedding Rows`, and `Caller-provided Embeddings` in the summary grid, with a boundary that these are operational counts, not semantic retrieval quality evidence. This is dashboard inspectability only, not embedding generation, hosted deployment evidence, external reviewer feedback, or product-complete.

Ops dashboard semantic retrieval operational counts runtime smoke v0: implemented. Boundary: local Docker PostgreSQL/pgvector plus live FastAPI HTTP verified `GET /ops/dashboard -> 200` and dashboard HTML markers for retrieval runs, semantic retrieval runs, chunk embedding rows, caller-provided embeddings, and the semantic-quality boundary; this is local dashboard visibility evidence only, not embedding generation, semantic retrieval quality evidence, hosted deployment evidence, external reviewer feedback, or product-complete.
