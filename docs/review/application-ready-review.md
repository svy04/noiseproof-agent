# Application-ready Review

Status: Phase 82 review packet.

This is an application-ready review, not a product-complete declaration.

Not product-complete: robust PDF extraction, actual embedding model generation remains unproven, semantic retrieval quality, distributed tracing, hosted deployment, and external user validation are still unproven.

Multi Real-world PDF Parse Observation Matrix: `docs/review/multi-real-world-pdf-parse-observation.md` records three BEA real-world PDF PyMuPDF digital-text parse observations, with `observed_fixture_count -> 3`, `total_page_count -> 95`, `total_text_char_count -> 217555`, `total_table_candidate_count -> 43`, `table_extraction_performed -> false`, `ocr_calls_attempted -> false`, `binary_files_committed -> false`, `raw_extracted_text_committed -> false`, and `can_claim_robust_pdf_extraction -> false`. This is a multi-fixture real-world PDF parse observation matrix only, not robust PDF extraction evidence, not arbitrary market PDF parsing evidence, not OCR evidence, not table extraction evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Multi Real-world PDF Parse Observation Matrix Remote Verification: `docs/review/multi-real-world-pdf-parse-observation-remote-verification.md` records that the Phase 891 gate passed remote CI, including `Check multi real-world PDF parse observation report staleness` and full API smoke tests. This is remote workflow verification only, not the owner-runtime parse observations themselves, not robust PDF extraction evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Real-world PDF Parse Observation: `docs/review/real-world-pdf-parse-observation.md` records one BEA real-world PDF PyMuPDF digital-text parse observation, with `page_count -> 35`, `text_char_count -> 92219`, `table_candidate_count -> 35`, `table_extraction_performed -> false`, `ocr_calls_attempted -> false`, and `can_claim_robust_pdf_extraction -> false`. This is a single real-world PDF parse observation only, not robust PDF extraction evidence, not arbitrary market PDF parsing evidence, not OCR evidence, not table extraction evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Real-world PDF Parse Observation Remote Verification: `docs/review/real-world-pdf-parse-observation-remote-verification.md` records that the Phase 889 gate passed remote CI, including `Check real-world PDF parse observation report staleness` and full API smoke tests. This is remote workflow verification only, not the owner-runtime parse observation itself, not robust PDF extraction evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Owner-approved Real-world PDF Download and Hash: `docs/review/owner-approved-real-world-pdf-download-hash.md` records one BEA real-world PDF download/hash observation and four BLS runtime 403 observations, with `downloaded_fixture_count -> 1`, `blocked_fixture_count -> 4`, `binary_files_committed -> false`, `download_cache_committed -> false`, and `can_claim_robust_pdf_extraction -> false`. This is download/hash metadata only, not robust PDF extraction evidence, not arbitrary market PDF parsing evidence, not OCR evidence, not table extraction evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Owner-approved Real-world PDF Download and Hash Remote Verification: `docs/review/owner-approved-real-world-pdf-download-hash-remote-verification.md` records that the Phase 887 gate passed remote CI, including `Check owner-approved real-world PDF download/hash report staleness` and full API smoke tests. This is remote workflow verification only, not the owner-runtime download/hash observation itself, not robust PDF extraction evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

README Proof-bounded Marketing Surface: `docs/review/readme-proof-bounded-marketing-surface.md` records that the README first screen now separates current proof, non-proof, source-first borrowed patterns, and the 90-second reviewer path. This is README marketing surface only, not product-complete, not robust PDF extraction evidence, not hosted deployment evidence, not external reviewer feedback, and not Braincrew acceptance.

Licensed Real-world PDF Fixture Pack: `docs/review/licensed-real-world-pdf-fixture-pack.md` records a metadata-only candidate pack with `candidate_count -> 4`, `downloaded_candidate_count -> 0`, `binary_files_committed -> false`, and `can_claim_robust_pdf_extraction -> false`. This is candidate metadata only, not robust PDF extraction evidence, not arbitrary market PDF parsing evidence, not OCR evidence, not table extraction evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Licensed Real-world PDF Fixture Pack Remote Verification: `docs/review/licensed-real-world-pdf-fixture-pack-remote-verification.md` records that the Phase 884 candidate pack passed remote CI, including `Check licensed real-world PDF fixture pack report staleness` and full API smoke tests. This is remote workflow verification only, not the candidate pack itself, not a real-world PDF download, not robust PDF extraction evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Multi-fixture OCR Adapter Eval: `docs/review/multi-fixture-ocr-adapter-eval.md` records that the 8-role PDF fixture matrix now includes one sanitized owner-runtime OCR smoke signal, with `owner_runtime_ocr_smoke_count -> 1`, `combined_fixture_signal_count -> 9`, and `can_claim_robust_pdf_extraction -> false`. This is a multi-fixture OCR adapter evaluation surface only, not robust PDF extraction evidence, not arbitrary market PDF OCR evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Multi-fixture OCR Adapter Eval Remote Verification: `docs/review/multi-fixture-ocr-adapter-eval-remote-verification.md` records that the Phase 882 eval passed remote CI, including `Check multi-fixture OCR adapter eval report staleness` and full API smoke tests. This is remote workflow verification only, not the eval gate itself, not robust PDF extraction evidence, not arbitrary market PDF OCR evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Opt-in OCR Adapter Owner-runtime Smoke: `docs/review/opt-in-ocr-adapter-owner-runtime-smoke.md` records one owner-runtime PyMuPDF OCR smoke over the committed synthetic image-only fixture. The validator accepted `expected_spans_found -> true`, `recognized_text -> ocr smoke text`, and `accepted_owner_runtime_smoke -> true` while preserving `can_claim_robust_pdf_extraction -> false`. This is one synthetic fixture OCR smoke only, not robust PDF extraction evidence, not arbitrary market PDF OCR evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Opt-in OCR Adapter Owner-runtime Smoke Remote Verification: `docs/review/opt-in-ocr-adapter-owner-runtime-smoke-remote-verification.md` records that the Phase 880 owner-runtime smoke documentation passed remote CI, including `Check opt-in OCR adapter runtime input discovery missing state` and full API smoke tests. This is remote workflow verification only, not new OCR runtime evidence, not robust PDF extraction evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Latest opt-in OCR adapter runtime smoke harness: `docs/review/opt-in-ocr-adapter-runtime-smoke.md` records an owner-runtime gated PyMuPDF OCR smoke harness and CI missing-input path with `owner_runtime_input_status -> missing_tessdata_prefix`, `opt_in_enabled -> false`, and `ocr_calls_attempted -> false`. This is a harness and missing-input proof only, not OCR evidence, not robust PDF extraction evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Opt-in OCR Adapter Runtime Smoke Remote Verification: `docs/review/opt-in-ocr-adapter-runtime-smoke-remote-verification.md` records that the Phase 878 harness passed remote CI, including the `Check opt-in OCR adapter runtime input discovery missing state` step and full API smoke tests. This is remote workflow verification only, not OCR evidence, not robust PDF extraction evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Latest committed OCR/layout/image binary fixture provenance: `docs/review/committed-ocr-layout-image-binary-fixture-provenance.md` records committed synthetic binary PDFs for the OCR/image/layout/empty-text roles with `committed_fixture_count -> 4`, `parser_observed_fixture_count -> 4`, and `can_claim_robust_pdf_extraction -> false`. This is committed synthetic fixture provenance only, not robust PDF extraction evidence, not OCR evidence, not image/chart interpretation evidence, not layout fidelity evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Committed OCR Layout Image Binary Fixture Provenance Remote Verification: `docs/review/committed-ocr-layout-image-binary-fixture-provenance-remote-verification.md` records that the Phase 876 provenance gate passed remote CI, including the `Check committed OCR layout image binary fixture provenance report staleness` step and full API smoke tests. This is remote workflow verification only, not robust PDF extraction evidence, not OCR evidence, not image/chart interpretation evidence, not layout fidelity evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Latest proof gap registry ops surface: `docs/review/proof-gap-registry-ops-surface.md` records that `GET /ops/summary` and `GET /ops/dashboard` now expose the current unproven claim gaps as a read-only registry. This is current-gap visibility only, not robust PDF extraction evidence, not live embedding generation proof, not semantic retrieval quality evidence, not distributed tracing, not hosted observability, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Latest OCR/layout/image fixture adapter runtime pack: `docs/review/ocr-layout-image-fixture-adapter-runtime-pack.md` records that the four OCR/image/layout/empty-text PDF roles now have executable synthetic adapter-runtime observations with `adapter_runtime_observed_count -> 4` and `can_claim_robust_pdf_extraction -> false`. This is not robust PDF extraction evidence, not OCR evidence, not image/chart interpretation evidence, not layout fidelity evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

OCR Layout Image Fixture Adapter Runtime Pack Remote Verification: `docs/review/ocr-layout-image-fixture-adapter-runtime-pack-remote-verification.md` records that the Phase 874 pack passed remote CI, including the `Check OCR layout image fixture adapter runtime pack report staleness` step and full API smoke tests. This is remote workflow verification only, not robust PDF extraction evidence, not OCR evidence, not image/chart interpretation evidence, not layout fidelity evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Latest missing PDF runtime observation pack: `docs/review/missing-pdf-runtime-observation-pack.md` records that the four previously missing PDF fixture roles now have a bounded pack with `combined_observed_fixture_count -> 8` and `can_claim_robust_pdf_extraction -> false`. This is not robust PDF extraction evidence, not OCR evidence, not image/chart interpretation evidence, not layout fidelity evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Missing PDF Runtime Observation Pack Remote Verification: `docs/review/missing-pdf-runtime-observation-pack-remote-verification.md` records that the Phase 872 pack passed remote CI, including the `Check missing PDF runtime observation pack report staleness` step and full API smoke tests. This is remote workflow verification only, not robust PDF extraction evidence, not OCR evidence, not image/chart interpretation evidence, not layout fidelity evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Latest multi-fixture PDF extraction quality eval: `docs/review/multi-fixture-pdf-extraction-quality-eval.md` records that the PDF quality fixture matrix now keeps all 8 fixture roles visible, with 4 observed fixtures, 4 missing runtime observations, and `can_claim_robust_pdf_extraction -> false`. This is a gap surface only, not robust PDF extraction evidence, not OCR evidence, not layout fidelity evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Multi-fixture PDF Extraction Quality Eval Remote Verification: `docs/review/multi-fixture-pdf-extraction-quality-eval-remote-verification.md` records that the Phase 870 matrix passed remote CI, including the `Check multi-fixture PDF extraction quality report staleness` step and full API smoke tests. This is remote workflow verification only, not robust PDF extraction evidence, not OCR evidence, not layout fidelity evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Latest Live Lexical Qrels Baseline Eval: `docs/review/live-lexical-qrels-baseline-eval.md` records that the current lexical retrieval code path can generate a qrels-evaluable run for the tiny local fixture. It preserves the blocked semantic-quality claim gate with `live_lexical_qrels_baseline_quality_claim_blocked` and keeps `semantic retrieval quality remains unproven` visible. This is a live lexical baseline only, not semantic retrieval quality evidence, not embedding generation, not representative retrieval evaluation, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Latest Live Semantic Qrels Baseline Eval: `docs/review/live-semantic-qrels-baseline-eval.md` records that caller-provided fixture vectors can generate a qrels-evaluable semantic-cosine run for the tiny local fixture. It preserves the blocked semantic-quality claim gate with `live_semantic_qrels_baseline_quality_claim_blocked`, exposes `missing_embedding_chunk_ids -> chunk-missing-source`, and keeps `semantic retrieval quality remains unproven` visible. This is a caller-provided vector baseline only, not semantic retrieval quality evidence, not live embedding generation, not representative retrieval evaluation, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Latest Representative Live Semantic Quality Eval: `docs/review/representative-live-semantic-quality-eval.md` records that the local representative fixture covers all current NoiseProof information roles and the source types `csv`, `html`, `markdown`, `memo`, and `pdf`. It preserves the blocked production semantic-quality claim gate with `representative_live_semantic_quality_claim_blocked` and keeps `semantic retrieval quality remains unproven` visible. This is a local representative fixture with caller-provided vectors only, not production semantic retrieval quality evidence, not live embedding generation, not a public benchmark result, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Latest Live Embedding Domain Qrels Owner-runtime Packet: `docs/review/live-embedding-domain-qrels-owner-runtime-eval-packet.md` records the no-secret/no-call packet, input discovery, and metadata-only validator for a future owner-runtime live embedding-backed domain qrels evaluation. It uses `app.services.live_embedding_domain_qrels_harness`, requires `provider_call_count -> 18` in the accepted report, and keeps `owner_runtime_live_embedding_domain_qrels_eval_v0` pending because current discovery is `missing_openai_api_key`. This is not live embedding generation proof, not production semantic retrieval quality evidence, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Live Embedding Domain Qrels Owner-runtime Packet Remote Verification: `docs/review/live-embedding-domain-qrels-owner-runtime-eval-packet-remote-verification.md` records that head `4bda105f31698521302341ed69e30addae9190b0` passed CI run `27491187230` job `81256509435` and External Feedback Screen run `27491187229` job `81256509371`, including `Check live embedding domain qrels owner-runtime input discovery`. This is remote workflow verification only, not live embedding generation proof, not production semantic retrieval quality evidence, not external reviewer feedback, and not product-complete.

Live Embedding Domain Qrels Owner-runtime Runner: `docs/review/live-embedding-domain-qrels-owner-runtime-runner.md` records the executable owner-runtime command `--run-owner-runtime-eval`, outside-repository output guard, missing-input CI path, and metadata-only report boundary for a future domain qrels eval. This makes the next gate easier to run but is not live embedding generation proof, not production semantic retrieval quality evidence, not external reviewer feedback, and not product-complete.

Live Embedding Domain Qrels Owner-runtime Runner Remote Verification: `docs/review/live-embedding-domain-qrels-owner-runtime-runner-remote-verification.md` records that head `67dec62288b1dc40f57e2a8c1c3a22169b959f39` passed CI run `27491615373` job `81257751009` and External Feedback Screen run `27491615371` job `81257751081`, including `Check live embedding domain qrels owner-runtime runner missing input`. This is remote workflow verification only, not live embedding generation proof, not production semantic retrieval quality evidence, not external reviewer feedback, and not product-complete.

Live semantic qrels baseline eval remote verification: `docs/review/live-semantic-qrels-baseline-eval-remote-verification.md` records that head `ed73aef0b13261ac74ee14c7402d839dc5532797` passed CI run `27490045473` job `81253278484` and External Feedback Screen run `27490045474` job `81253278486`. This is remote workflow verification only, not semantic retrieval quality evidence, not live embedding generation, not representative retrieval evaluation, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Live lexical qrels baseline eval remote verification: `docs/review/live-lexical-qrels-baseline-eval-remote-verification.md` records that head `8a7cc07aac8c4d7c218424a0ecf50381cfea0d3c` passed CI run `27489607815` job `81252099416` and External Feedback Screen run `27489607811` job `81252099394`. This is remote workflow verification only, not semantic retrieval quality evidence, not embedding generation, not representative retrieval evaluation, not hosted deployment evidence, not external reviewer feedback, and not product-complete.

Latest semantic diagnostic alignment: `docs/review/application-ready-semantic-diagnostic-alignment.md` records that this review now points to the semantic retrieval diagnostic matrix proof chain, including `docs/review/semantic-retrieval-quality-diagnostic-matrix.md`, `docs/review/external-reader-proof-path-semantic-retrieval-quality-diagnostic-matrix-route-refresh.md`, `docs/review/external-review-issue-body-semantic-retrieval-quality-diagnostic-matrix-route-refresh.md`, `docs/review/external-feedback-current-state-semantic-retrieval-quality-diagnostic-matrix-issue-verification.md`, and `docs/review/external-feedback-current-state-semantic-retrieval-quality-diagnostic-matrix-issue-verification-remote-verification.md`. This keeps `candidate_count: 0`, `status: pending`, and the boundary that semantic retrieval quality remains unproven visible.

Latest semantic quality claim-gate alignment: `docs/review/application-ready-semantic-quality-claim-gate-alignment.md` records that this review now points to the semantic quality claim-gate proof chain, including `docs/review/semantic-quality-claim-gate.md`, `docs/review/semantic-quality-claim-gate-remote-verification.md`, `docs/review/external-reader-proof-path-semantic-quality-claim-gate-route-refresh.md`, `docs/review/external-reader-proof-path-semantic-quality-claim-gate-route-refresh-remote-verification.md`, `docs/review/external-review-issue-body-semantic-quality-claim-gate-route-refresh.md`, `docs/review/external-review-issue-body-semantic-quality-claim-gate-route-refresh-remote-verification.md`, `docs/review/external-feedback-current-state-semantic-quality-claim-gate-issue-verification.md`, and `docs/review/external-feedback-current-state-semantic-quality-claim-gate-issue-verification-remote-verification.md`. This keeps `status: blocked`, `can_claim_semantic_quality: false`, `semantic_quality_claim_blocked`, `candidate_count: 0`, `status: pending`, and the boundary that semantic retrieval quality remains unproven visible.

Latest semantic quality claim-gate alignment remote verification: `docs/review/application-ready-semantic-quality-claim-gate-alignment-remote-verification.md` records that commit `b481dfebc22332fe5b9520059c04a4ed85d5846a` passed CI run `27081708141` and External Feedback Screen run `27081708142` after the application-ready semantic quality claim-gate alignment was pushed. This is remote workflow verification only, not the application alignment itself, not vector search quality evidence, not embedding generation, not external reviewer feedback, not hosted deployment evidence, and not product-complete.

README proof-marker archive: `docs/review/readme-proof-marker-archive.md` preserves legacy README proof markers after README scanability cleanup. It is source-level provenance, not product runtime evidence, not hosted deployment evidence, not automatic failure-case creation, and not complete workflow failure causality.

## Summary

Current judgment: Partial application-ready portfolio artifact.

NoiseProof Agent is application-ready as a portfolio evidence packet: it shows a small local service with evidence-first workflow surfaces, operations visibility, persisted proof records, workflow-parent lineage, failure-case persistence, and bounded proof links before any free-form answer is claimed.

Detailed evidence remains in the checklist below and in the external-reader proof path. This summary is intentionally not a product-complete declaration.

Allowed external claim: local, inspectable portfolio evidence exists for the current bounded workflow surfaces.

Forbidden claim: this is not hosted deployment evidence, not automatic failure-case creation beyond the local v0 workflow failure path, production/background failure-case automation remains unclaimed, and this is not retry behavior, not root-cause automation, not complete workflow failure causality, not production RAG quality, and not autonomous market intelligence.

## Checklist

| Application-ready criterion | Status | Evidence | Boundary |
|---|---|---|---|
| local Docker Compose stack runs | Pass | `docker compose ps` has local DB evidence; Compose project isolation now creates project-scoped names such as `noiseproof-phase595-db-1` | local only; not hosted deployment evidence |
| Compose project isolation | Pass | `docs/review/compose-project-isolation.md`; `container_name` removed from `docker-compose.yml`; `POSTGRES_PORT=55439 docker compose -p noiseproof-phase595 up -d db` created `noiseproof-phase595-db-1` | local Compose isolation only; not production orchestration, hosted deployment evidence, or Kubernetes readiness |
| PDF, CSV, URL/HTML, markdown memo inputs supported | Partial | parser adapter stubs, JSON text-only PDF fallback, and uploaded PDF text extraction v0 | OCR, table extraction, layout fidelity, and robust PDF extraction are not claimed |
| uploaded PDF downstream handoff runtime proof exists | Pass | `docs/review/uploaded-pdf-downstream-handoff-runtime-smoke.md` | local runtime evidence only; digital PDF text only; not OCR, table extraction, layout fidelity, robust PDF extraction, raw file storage, or hosted deployment evidence |
| uploaded PDF retrieval-run provenance runtime proof exists | Pass | `docs/review/uploaded-pdf-retrieval-run-provenance-runtime-smoke.md` | local runtime evidence only; preserves parser provenance into retrieval-run candidate metadata; not OCR, table extraction, layout fidelity, robust PDF extraction, raw file storage, Evidence Ledger generation, or hosted deployment evidence |
| document profile is generated | Pass | `POST /documents/profile` | direct text payloads only |
| three chunk strategies can be compared | Pass | fixed-window, heading-aware, row-aware | chunks are not persisted |
| retrieval returns source ids | Pass | lexical retrieval v0 plus caller-provided semantic retrieval preview/persistence | semantic retrieval quality remains unproven; actual embedding model generation remains unproven |
| Evidence Ledger can be generated before final answer | Pass | `POST /evidence-ledgers/preview`, `POST /evidence-ledgers` | persisted v0 entries are not yet linked to retrieval run ids |
| unsupported claims are blocked | Pass | Noise Gate, persisted Noise Gate, and Report Preview tests | deterministic checks only |
| contradictions are surfaced | Pass | Evidence Ledger and Noise Gate previews | not a full contradiction engine |
| buy/sell recommendation questions are refused or reframed | Pass | collection, ledger, gate, and report boundaries | not legal or financial advice tooling |
| every agent run leaves a trace | Pass for current preview endpoints | preview endpoints auto-create `agent_runs.trace_json`; retrieval has dedicated `retrieval_runs` | metadata trace only, not distributed tracing or a complete multi-stage workflow trace |
| trace context header propagation exists | Pass | response `traceparent`, `x-noiseproof-trace-source`, `x-noiseproof-trace-boundary`, `docs/review/trace-context-header-propagation.md` | local header propagation only; not distributed tracing, no OpenTelemetry, no hosted observability, no span export |
| trace context header runtime smoke exists | Pass | `docs/review/trace-context-header-runtime-smoke.md` | local uvicorn/curl evidence only; not hosted observability, not distributed tracing, not cross-service trace proof |
| http trace context run metadata exists | Pass | `agent_runs.trace_json.http_traceparent`, `http_trace_source`, `http_trace_context_boundary`, `docs/review/http-trace-context-run-metadata.md` | local run metadata capture only; not distributed tracing, not OpenTelemetry span export, not hosted observability |
| http trace context Docker runtime smoke exists | Pass | `docs/review/http-trace-context-docker-runtime-smoke.md`; Dockerized `POST /collection-plans/preview -> 200`; `GET /agent-runs -> 200` | local Docker runtime evidence only; not hosted deployment evidence, not distributed tracing, not OpenTelemetry span export, not hosted observability |
| local OpenTelemetry span export exists | Pass | `docs/review/local-otel-span-export.md`; `NOISEPROOF_ENABLE_OTEL_SPAN_EXPORT`; `GET /traces/otel-spans/local`; `x-noiseproof-otel-span-export` | local in-memory span export only; not distributed tracing, not hosted observability, not external collector integration, not production monitoring, not cross-service trace proof, not hosted deployment evidence |
| local OpenTelemetry span export Docker runtime smoke exists | Pass | `docs/review/local-otel-span-export-runtime-smoke.md`; `noiseproof-phase851`; `NOISEPROOF_ENABLE_OTEL_SPAN_EXPORT=true`; `x-noiseproof-otel-span-export: local_in_memory_enabled`; `span_export_enabled=true`; `span_count=4` | local Docker/FastAPI runtime evidence only; local in-memory span export only; not distributed tracing, hosted observability, external collector integration, OpenTelemetry Collector deployment, production monitoring, cross-service trace proof, hosted deployment evidence, or product-complete |
| embedding provider source review exists | Pass | `docs/review/embedding-provider-source-review.md` | source review only; no API call; no dependency; no cost-incurring runtime path; actual embedding model generation remains unproven |
| embedding model provider disabled path exists | Pass | `POST /chunks/embedding-model-preview`, `docs/review/embedding-model-provider-disabled-path.md` | readiness/disabled path only; no provider call; no embedding vector is generated; no persistence; actual embedding model generation remains unproven |
| embedding model provider live-call review exists | Pass | `docs/review/embedding-model-provider-live-call-review.md` | guardrail review only; not implemented runtime behavior; no provider call; actual embedding model generation remains unproven |
| embedding model mocked-provider call exists | Pass | `POST /chunks/embedding-model-preview`, `docs/review/embedding-model-mocked-provider-call.md` | injected mocked provider only; no live OpenAI provider call; no live provider call in CI; no automatic persistence; actual live embedding model generation remains unproven |
| embedding model live-provider implementation review exists | Pass | `docs/review/embedding-model-live-provider-implementation-review.md` | owner-runtime implementation gate only; no live OpenAI provider call, no network call, no API cost, no persistence, and actual live embedding model generation remains unproven |
| embedding model live-provider code review exists | Pass | `docs/review/embedding-model-live-provider-code-review.md` | code insertion review only; no OpenAI dependency, no runtime behavior, no live provider call, no API cost, and actual live embedding model generation remains unproven |
| embedding model live-provider dependency review exists | Pass | `docs/review/embedding-model-live-provider-dependency-review.md` | dependency candidate review only; no package installation, no lockfile change, no runtime behavior, no live provider call, and actual live embedding model generation remains unproven |
| embedding model live-provider dependency addition exists | Pass | `apps/api/pyproject.toml`, `apps/api/uv.lock`, `docs/review/embedding-model-live-provider-dependency-addition.md` | dependency metadata only; no app code, no route behavior change, no live provider call, no API cost, and actual live embedding model generation remains unproven |
| embedding model live-provider adapter disabled-code exists | Pass | `apps/api/app/services/openai_embedding_provider.py`, `docs/review/embedding-model-live-provider-adapter-disabled-code.md` | adapter code with fake-client tests only; route remains unwired, no default live provider call, no CI live provider call, and actual live embedding model generation remains unproven |
| embedding model live-provider route wiring review exists | Pass | `docs/review/embedding-model-live-provider-route-wiring-review.md` | route wiring review only; no runtime behavior, no route wiring, no live provider call, no CI live provider call, and actual live embedding model generation remains unproven |
| embedding model live-provider route wiring opt-in-disabled exists | Pass | `apps/api/app/settings.py`, `apps/api/app/services/embedding_model_preview.py`, `docs/review/embedding-model-live-provider-route-wiring-opt-in-disabled.md` | owner-runtime opt-in dependency wiring only; no default live provider call, no CI live provider call, no API cost in tests, and actual live embedding model generation remains unproven |
| embedding model live-provider error boundary exists | Pass | `apps/api/app/services/embedding_model_preview.py`, `apps/api/tests/test_routes.py`, `docs/review/embedding-model-live-provider-error-boundary.md` | provider error metadata only; no live embedding generation proof, no semantic retrieval quality evidence, no hosted evidence, and no external reviewer feedback |
| embedding provider readiness ops surface exists | Pass | `GET /ops/summary`, `GET /ops/dashboard`, `docs/review/embedding-provider-readiness-ops-surface.md` | readiness metadata only; no OpenAI provider call, no secret output, no persistence, no live embedding generation proof, and no external reviewer feedback |
| embedding model live-provider owner-runtime smoke packet exists | Pass | `apps/api/app/services/embedding_model_live_provider_harness.py`, `docs/review/embedding-model-live-provider-owner-runtime-smoke-packet.md` | no-secret/no-call packet only; no live OpenAI provider call, no API cost, no external reviewer feedback, and actual live embedding model generation remains unproven |
| failure cases are recorded | Pass | failure case endpoint and dashboard | not comprehensive |
| operations dashboard shows runs and failures | Pass | `GET /ops/dashboard` | plain HTML, not polished UI |
| README is understandable without explanation | Pass | `README.md` | should still be reviewed by an external reader |
| architecture and ADRs exist | Pass | `docs/architecture.md`, `docs/adr/*` | ADRs cover initial decisions only |
| evaluation report exists | Pass | `docs/evaluation/*` | not a benchmark |
| Braincrew role map exists | Pass | `docs/application/braincrew-role-map.md` | role fit is an argument, not hiring proof |
| evidence -> gate -> report lineage exists | Pass for deterministic workflow preview | `POST /workflow-runs/execute-preview`, `GET /workflow-runs/{id}/lineage`, `direct_stage_links`, `noise_gate_evidence_links`, `report_evidence_links`, `report_noise_gate_links`, `docs/review/workflow-direct-stage-links.md`, `docs/review/workflow-direct-stage-links-runtime-smoke.md`, `docs/review/external-reviewer-workflow-direct-stage-links-runtime-request-refresh.md` | workflow-created records only; standalone gate/report endpoints remain payload-only unless they create explicit links |
| single workflow parent exists | Pass for deterministic preview | `POST /workflow-runs`, `GET /workflow-runs`, `GET /workflow-runs/{id}`, `POST /workflow-runs/execute-preview`, child `workflow_run_id` links | local deterministic preview only, not autonomous workflow execution |
| direct stage-level input links exist | Pass for deterministic workflow preview | workflow-created Noise Gate and Report rows include `stage_input_manifest`; `GET /workflow-runs/{id}/lineage` resolves manifest ids and returns `direct_stage_links`; `db/migrations/023_workflow_stage_links.sql`; `docs/review/workflow-direct-stage-links-runtime-smoke.md`; request refresh: `docs/review/external-reviewer-workflow-direct-stage-links-runtime-request-refresh.md` | workflow-created records only; standalone gate/report endpoints remain payload-only; not distributed tracing |
| workflow stage event log exists | Pass for deterministic workflow preview | `workflow_stage_events`; `db/migrations/024_workflow_stage_events.sql`; `GET /workflow-runs/{id}` and `GET /workflow-runs/{id}/proof-bundle` expose `stage_events` with `workflow_stage_event_count`; `docs/review/workflow-stage-event-log.md`; `docs/review/workflow-stage-event-log-runtime-smoke.md`; request refresh: `docs/review/external-reviewer-workflow-stage-event-log-runtime-request-refresh.md` | local event log only; not distributed tracing, OpenTelemetry, hosted observability, autonomous workflow execution, or product-complete |
| failed workflow stage events are recorded | Pass for deterministic workflow preview failures | `POST /workflow-runs/execute-preview` records the active failed stage in `workflow_stage_events`; `docs/review/workflow-failed-stage-event.md`; `docs/review/workflow-failed-stage-event-runtime-smoke.md`; request refresh: `docs/review/external-reviewer-workflow-failed-stage-event-runtime-request-refresh.md`; `test_workflow_execute_preview_records_failed_stage_event_when_stage_errors` | local failure observability only; the older runtime smoke verifies `retrieval -> completed`, `evidence_ledger -> failed`, and the pre-auto-creation boundary `failure_case_count_delta -> 0`; not retry behavior, root-cause automation, distributed tracing, hosted observability, hosted deployment evidence, or product-complete |
| workflow failure auto failure-case creation exists | Pass for local v0 deterministic workflow preview failures | `docs/review/workflow-failure-auto-failure-case-creation.md`, `docs/review/workflow-failure-auto-failure-case-creation-runtime-smoke.md`, `auto_failure_case_id`, `auto_created_from_workflow_failure_local_v0`, `local_workflow_stage_failure_event_auto_failure_case_local_v0` | local route/runtime behavior only; not retry behavior, root-cause automation, complete workflow failure causality, production background worker behavior, hosted deployment evidence, external reviewer feedback, or product-complete |
| workflow failure auto-created failure case is visible from dashboard | Pass | `docs/review/workflow-failure-auto-created-failure-case-dashboard-runtime-smoke.md`, `GET /ops/dashboard`, `dashboard_contains_auto_created_failure_case_filter -> true`, `dashboard_contains_auto_created_failure_case_id -> true`, `dashboard_contains_review_queue_linked_count -> true` | dashboard read-model proof only; not retry behavior, root-cause automation, complete workflow failure causality, hosted deployment evidence, external reviewer feedback, or product-complete |
| workflow failure auto-created failure-case dashboard proof is reviewer-routed | Pass | `docs/review/workflow-failure-auto-created-failure-case-dashboard-runtime-smoke.md`, `docs/review/external-reviewer-workflow-failure-auto-created-dashboard-runtime-request-refresh.md` | request-surface refresh only; not a live issue body edit, external reviewer feedback, hosted deployment evidence, retry behavior, root-cause automation, complete workflow failure causality, or product-complete |
| workflow failure auto-creation runtime proof is reviewer-routed | Pass | `docs/review/workflow-failure-auto-failure-case-creation-runtime-smoke.md`, `docs/review/external-reviewer-workflow-failure-auto-creation-runtime-request-refresh.md`, `docs/review/external-review-issue-body-workflow-failure-auto-creation-runtime-refresh.md`, `docs/review/external-feedback-current-state-workflow-failure-auto-creation-runtime-issue-verification.md` | reviewer/request routing and current-state verification only; not external reviewer feedback, hosted deployment evidence, retry behavior, root-cause automation, complete workflow failure causality, or product-complete |
| workflow lineage is discoverable from dashboard | Pass | workflow rows in `GET /ops/dashboard` link to `GET /workflow-runs/{id}` and `GET /workflow-runs/{id}/lineage` | plain HTML links only, no dashboard polish |
| workflow proof bundle is discoverable from dashboard | Pass | workflow rows in `GET /ops/dashboard` link to `GET /workflow-runs/{id}/proof-bundle` | navigation only; no new endpoint, storage, distributed tracing, hosted observability, or dashboard polish |
| missing manifest reference behavior is covered by a bounded fixture | Pass | `test_workflow_run_lineage_reports_missing_manifest_references_without_mutation_api` proves `missing_reference_count > 0` without new schema or mutation paths | fixture-level proof, not production corruption recovery |
| manifest-shape risk is hardened | Pass | non-list `input_evidence_ledger_entry_ids` values produce empty ids and a warning; duplicate and cross-workflow behavior is tested | still local read-model hardening, not normalized lineage schema |
| lineage warning categories are reviewed | Pass | `docs/review/workflow-lineage-warning-taxonomy-review.md` names derived boundary, missing reference, invalid shape, and local scope warnings | review-only; no structured warning field yet |
| structured warning codes exist | Pass | `GET /workflow-runs/{id}/lineage` returns `warning_codes` while preserving `warnings` | response-level taxonomy only; no storage or schema persistence |
| warning-code documentation is reviewed | Pass | `docs/review/workflow-lineage-warning-code-documentation-review.md` keeps docs scope bounded | review-only; no dashboard rendering or persistence |
| warning-code response example exists | Pass | `docs/runbook.md` shows `warnings` and `warning_codes` together | example only; not runtime proof |
| warning-code dashboard surfacing is reviewed | Pass | `docs/review/workflow-lineage-warning-code-dashboard-review.md` | review-only; no dashboard rendering yet |
| warning-code dashboard legend exists | Pass | `GET /ops/dashboard` shows Lineage warning codes | response-level taxonomy only; not persisted analytics |
| warning-code dashboard smoke example exists | Pass | `docs/runbook.md` expected dashboard legend | docs-only; not runtime proof |
| workflow-version naming reviewed | Pass | `docs/review/workflow-version-naming-review.md` | review-only; runtime value unchanged |
| workflow-version naming updated | Pass | `phase40-lineage-warning-code-dashboard` in runtime defaults and examples | identifier-only; no workflow semantic change |
| uploaded file intake manifest preview exists | Pass | `POST /documents/upload-intake-manifest-preview`, `docs/review/uploaded-file-intake-manifest-runtime-smoke.md` | preview-only content hash and storage boundary; not raw file storage |
| uploaded file intake manifest persistence exists | Pass | `POST /documents/upload-intake-manifests`, `GET /documents/upload-intake-manifests`, `docs/review/uploaded-file-intake-manifest-persistence-runtime-smoke.md` | manifest metadata only; no raw uploaded bytes; not hosted deployment evidence |
| uploaded file parsed document persistence exists | Pass | `POST /documents/upload-parsed-documents`, `GET /documents`, `docs/review/uploaded-file-parsed-document-persistence-runtime-smoke.md` | metadata/profile row only; no raw uploaded bytes; no parsed text persistence; not robust PDF extraction |
| uploaded file chunk persistence exists | Pass | `POST /documents/{document_id}/chunks`, `GET /documents/{document_id}/chunks`, `docs/review/uploaded-file-chunk-persistence-runtime-smoke.md`, `docs/review/uploaded-file-chunk-persistence-application-refresh.md` | manual document-scoped chunk text persistence only; explicit uploaded-file-to-chunks handoff exists through `POST /documents/upload-chunks`; implicit upload-preview auto-persistence remains intentionally unclaimed; no embeddings; no retrieval persistence |
| uploaded file chunk handoff persistence exists | Pass | `POST /documents/upload-chunks`, `GET /documents/{document_id}/chunks`, `docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md`, `docs/review/uploaded-file-chunk-persistence-handoff-application-refresh.md` | explicit uploaded-file-to-chunks handoff only; no raw uploaded byte storage; no full parsed text persistence; no embeddings; no retrieval persistence |
| uploaded PDF page diagnostics runtime proof exists | Pass | `docs/review/uploaded-pdf-page-diagnostics-runtime-smoke.md` | local runtime evidence only; digital PDF diagnostics only; not OCR, table extraction, layout fidelity, robust PDF extraction, raw file storage, hosted deployment evidence, or external reviewer feedback |
| uploaded PDF table-candidate diagnostics route proof exists | Pass | `docs/review/uploaded-pdf-table-candidate-diagnostics.md`, `POST /documents/upload-preview` | route-level metadata only; uses PyMuPDF `find_tables()` candidate diagnostics; does not extract table contents; not table extraction, OCR, layout fidelity, robust PDF extraction, hosted deployment evidence, external reviewer feedback, or product-complete |
| uploaded PDF table-candidate diagnostics runtime proof exists | Pass | `docs/review/uploaded-pdf-table-candidate-diagnostics-runtime-smoke.md` | local runtime evidence only; preview-only `POST /documents/upload-preview` returned one table candidate and `document_count_delta=0`; not table extraction, table-content extraction, OCR, layout fidelity, robust PDF extraction, hosted deployment evidence, external reviewer feedback, or product-complete |
| uploaded PDF table-candidate downstream provenance runtime proof exists | Pass | `docs/review/uploaded-pdf-table-candidate-downstream-provenance-runtime-smoke.md`, `test_uploaded_pdf_table_candidate_diagnostics_flow_into_chunk_and_retrieval_provenance` | local runtime evidence and route test only; table-candidate metadata reaches document profile, chunk metadata, retrieval metadata, and retrieval candidate metadata; not table extraction, table-content extraction, OCR, layout fidelity, robust PDF extraction, Evidence Ledger generation, hosted deployment evidence, external reviewer feedback, or product-complete |
| uploaded file retrieval persistence exists | Pass | `POST /documents/{document_id}/retrieval-runs`, `GET /retrieval-runs`, `docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md`, `docs/review/uploaded-file-retrieval-persistence-application-refresh.md` | explicit retrieval over persisted `document_chunks` only; no embeddings; no semantic retrieval; no Evidence Ledger generation; not financial advice |
| uploaded raw file quarantine storage exists | Pass | `POST /documents/upload-raw-files`, `GET /documents/upload-raw-files`, `docs/review/uploaded-raw-file-storage-runtime-smoke.md`, `docs/review/uploaded-raw-file-storage-application-refresh.md` | quarantined PostgreSQL BYTEA storage with metadata-only responses; not production malware scanning; not hosted deployment evidence |
| guarded raw file download endpoint runtime smoke exists | Pass | `GET /documents/upload-raw-files/{raw_file_id}/download`, `docs/review/uploaded-raw-file-download-endpoint-runtime-smoke.md`, `docs/review/uploaded-raw-file-download-rate-limit-local.md`, `docs/review/uploaded-raw-file-download-rate-limit-runtime-smoke.md`, `docs/review/raw-file-download-operator-token-guard.md` | latest clean scan required; no-scan and later failed scan return `409`; local v0 in-memory rate limit runtime smoke exists; opt-in operator-token guard uses `local_v0_operator_token_header_not_production`; not production authorization, authenticated user identity, distributed rate limiting, hosted deployment evidence, or production malware scanning evidence |
| retrieval-run-linked Evidence Ledger persistence exists | Pass | `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`, `GET /evidence-ledgers`, `docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md` | deterministic handoff from persisted lexical retrieval runs only; no embeddings; no semantic retrieval; no LLM judgment; no Noise Gate or report generation |
| retrieval-run-linked Noise Gate persistence exists | Pass | `POST /retrieval-runs/{retrieval_run_id}/noise-gate`, `GET /noise-gates`, `docs/review/retrieval-run-linked-noise-gate-runtime-smoke.md` | deterministic handoff after linked Evidence Ledger rows only; pre-ledger `409`; no LLM judgment; no report generation; not financial advice |
| retrieval-run-linked Report persistence exists | Pass | `POST /retrieval-runs/{retrieval_run_id}/report`, `GET /reports`, `docs/review/retrieval-run-linked-report-runtime-smoke.md` | deterministic handoff after linked Evidence Ledger and Noise Gate rows only; pre-gate `409`; records `input_noise_gate_record_id`; no free-form final report generation; not financial advice |
| persisted Report markdown export exists | Pass | `GET /reports/{report_record_id}/markdown`, `docs/review/persisted-report-markdown-export.md` | deterministic read/export of existing persisted Report records only; no new claims, no LLM, no retrieval, no new Evidence Ledger or Report rows, and no free-form reports |
| deterministic local hash embedding preview exists | Pass | `POST /chunks/embedding-preview`, `docs/review/deterministic-text-embedding-preview.md` | preview-only local hash vector; not persisted; not a semantic embedding model; actual embedding model generation remains unproven; not vector search quality evidence |
| caller-provided chunk embedding endpoint exists | Pass | `POST /chunks/{chunk_id}/embeddings`, `GET /chunks/{chunk_id}/embeddings`, `docs/review/embedding-endpoint-runtime-smoke.md` | caller-provided vectors only; no embedding generation; no semantic retrieval; no HNSW/IVFFlat behavior; not vector search quality |
| caller-provided semantic retrieval persistence exists | Pass | `POST /documents/{document_id}/semantic-retrieval-runs`, `GET /retrieval-runs`, `docs/review/semantic-retrieval-persistence-runtime-smoke.md`, `docs/review/semantic-retrieval-persistence-application-refresh.md` | caller-provided vectors over existing embeddings only; semantic retrieval quality remains unproven; no embedding generation; no Evidence Ledger generation from semantic retrieval |
| toy semantic retrieval quality report exists | Pass | `docs/evaluation/semantic-retrieval-quality-report.md`, `docs/review/semantic-retrieval-quality-report-application-refresh.md` | semantic retrieval quality report is toy fixture output; not vector search quality evidence, not a benchmark result, not a model comparison |
| toy semantic retrieval diagnostic matrix exists | Pass | `docs/evaluation/semantic-retrieval-quality-report.md`, `docs/review/semantic-retrieval-quality-diagnostic-matrix.md` | per-query fixture diagnostics only; not vector search quality evidence, not embedding generation, not a benchmark result, not product-complete |
| semantic quality claim gate exists | Pass | `docs/review/semantic-quality-claim-gate.md`; `docs/evaluation/semantic-retrieval-quality-report.md` now renders `## Quality Claim Gate`, `status: blocked`, and `semantic_quality_claim_blocked` | claim blocking only; not vector search quality evidence, not embedding generation, not benchmark evidence, not retrieval tuning, not external reviewer feedback, not hosted deployment evidence |
| semantic quality claim-gate proof chain is application-aligned | Pass | `docs/review/application-ready-semantic-quality-claim-gate-alignment.md`; `docs/review/semantic-quality-claim-gate.md`; `docs/review/semantic-quality-claim-gate-remote-verification.md`; `docs/review/external-reader-proof-path-semantic-quality-claim-gate-route-refresh.md`; `docs/review/external-reader-proof-path-semantic-quality-claim-gate-route-refresh-remote-verification.md`; `docs/review/external-review-issue-body-semantic-quality-claim-gate-route-refresh.md`; `docs/review/external-review-issue-body-semantic-quality-claim-gate-route-refresh-remote-verification.md`; `docs/review/external-feedback-current-state-semantic-quality-claim-gate-issue-verification.md`; `docs/review/external-feedback-current-state-semantic-quality-claim-gate-issue-verification-remote-verification.md` | application review alignment only; semantic retrieval quality remains unproven; `status: blocked`, `can_claim_semantic_quality: false`, `candidate_count: 0`, and `status: pending`; not vector search quality evidence, not embedding generation, not hosted deployment evidence, not external reviewer feedback |
| semantic retrieval diagnostic proof chain is application-aligned | Pass | `docs/review/application-ready-semantic-diagnostic-alignment.md`; `docs/review/external-reader-proof-path-semantic-retrieval-quality-diagnostic-matrix-route-refresh.md`; `docs/review/external-review-issue-body-semantic-retrieval-quality-diagnostic-matrix-route-refresh.md`; `docs/review/external-feedback-current-state-semantic-retrieval-quality-diagnostic-matrix-issue-verification.md`; `docs/review/external-feedback-current-state-semantic-retrieval-quality-diagnostic-matrix-issue-verification-remote-verification.md` | application review alignment only; semantic retrieval quality remains unproven; `candidate_count: 0` and `status: pending`; not vector search quality evidence, not embedding generation, not hosted deployment evidence, not external reviewer feedback |
| migration runner can apply on fresh DB | Pass | `docs/review/migration-runner-fresh-db-verification.md` | local Docker only; not production migration orchestration |
| fresh DB API smoke path works | Pass | `docs/review/fresh-db-api-smoke-verification.md` | local Docker/API smoke only; not hosted deployment evidence |
| failure-case persistence smoke works | Pass | `docs/review/failure-case-persistence-smoke-verification.md` | stores manually submitted failure records; automatic failure detection is not claimed |
| agent-run failure linkage smoke works | Pass | `docs/review/agent-run-failure-linkage-smoke-verification.md` | links manual failure records to failed agent runs; complete workflow failure causality is not claimed |
| workflow failure linkage smoke works | Pass | `docs/review/workflow-failure-linkage-smoke-verification.md` | test-fixture proof only; complete workflow failure causality is not claimed |
| failure-case workflow linkage review exists | Pass | `docs/review/failure-case-workflow-linkage-review.md` | historical review boundary; manual workflow parent linkage now exists; automatic failure-case creation remains unclaimed in that historical review, while local v0 workflow failure auto-creation now exists and production/background failure-case automation remains unclaimed |
| failure-case draft preview exists | Pass | `POST /failure-cases/draft-preview` | returns a suggested payload only; does not persist failure cases automatically |
| failure-case draft preview smoke works | Pass | `docs/review/failure-case-draft-preview-smoke-verification.md` | route-level smoke only; automatic failure-case persistence is not claimed |
| failure-case draft manual handoff smoke works | Pass | `docs/review/failure-case-draft-manual-handoff-smoke-verification.md` | human confirmation boundary remains explicit; not automatic persistence |
| workflow failure-case persistence handoff exists | Pass | `POST /failure-cases/workflow-runs/{workflow_run_id}`, `docs/review/workflow-failure-case-persistence-handoff.md`, `docs/review/workflow-failure-case-persistence-handoff-runtime-smoke.md`, `docs/review/external-reviewer-workflow-failure-case-persistence-runtime-request-refresh.md` | caller-triggered `caller_triggered_workflow_failure_case_persistence`; local runtime smoke observed `queue_status_for_workflow -> failure_case_linked`, completed-workflow `409`, and duplicate `409`; request surface points reviewers to the proof; not hosted deployment evidence, background automation, root-cause automation, or complete workflow failure causality |
| persisted document failure candidate manual handoff runtime works | Pass | `docs/review/persisted-document-failure-candidate-manual-handoff-runtime-smoke.md`, `docs/review/external-feedback-current-state-persisted-document-failure-candidate-manual-handoff-runtime-issue-verification.md` | document-derived failure-case draft/manual handoff only; preview stays `preview_only_not_persisted`, human changes `draft.fix_status` from `draft` to `open`, and `POST /failure-cases -> 201` after confirmation; not automatic failure-case creation, not a confirm endpoint, not hosted deployment evidence, not robust PDF extraction |
| failure-case draft fresh DB handoff smoke works | Pass | `docs/review/failure-case-draft-fresh-db-handoff-smoke-verification.md` | local Docker DB evidence only; automatic persistence remains unclaimed; not hosted deployment evidence |
| workflow failure-to-draft smoke works | Pass | `docs/review/workflow-failure-to-draft-smoke-verification.md` | older route-level smoke only; in that proof, automatic failure-case creation remains unclaimed; local v0 auto-created failure cases are covered by the workflow failure auto failure-case creation runtime smoke |
| failure-case workflow parent linkage fresh DB works | Pass | `docs/review/failure-case-workflow-parent-linkage-fresh-db-verification.md` | local Docker DB evidence only; not hosted deployment evidence; manual parent linkage proof separate from local v0 auto-created failure cases |
| failure-case workflow parent dashboard link works | Pass | `GET /ops/dashboard` Failure Cases table Workflow Parent column | manual and local v0 auto-created provenance only; not retry behavior, root-cause automation, or complete workflow failure causality |
| failure-case workflow parent dashboard fresh DB smoke works | Pass | `docs/review/failure-case-workflow-parent-linkage-fresh-db-dashboard-smoke-verification.md` | local Docker DB dashboard evidence only; manual provenance only; not hosted deployment evidence |
| proof index reader path exists | Pass | `docs/review/failure-case-workflow-parent-linkage-proof-index.md` | index-only; no new runtime proof |
| External-reader proof path exists | Pass | `docs/review/external-reader-proof-path.md` | 5-minute path only; not hosted deployment evidence; not automatic failure-case creation; not complete workflow failure causality |
| README proof-marker archive is discoverable from application docs | Pass | `docs/review/readme-proof-marker-archive.md` | source-level provenance only; not product runtime evidence |
| Evidence Ledger quality risk ops counts are visible | Pass | `GET /ops/summary`, `GET /ops/dashboard`, `docs/review/evidence-quality-risk-ops-surface.md`, `docs/review/evidence-quality-risk-ops-surface-runtime-smoke.md`, `docs/review/evidence-quality-risk-ops-surface-runtime-smoke-remote-verification.md` | persisted-row metadata only; local runtime smoke and remote workflow verification exist; not final truth adjudication, retrieval quality evidence, Evidence Ledger quality evidence, embedding generation, external reviewer feedback, or hosted deployment evidence |
| Evidence Ledger quality risk rows can preview manual failure-case drafts | Pass | `POST /evidence-ledgers/{entry_id}/failure-case-draft-preview`, `docs/review/evidence-quality-risk-failure-case-draft-preview.md`, `docs/review/evidence-quality-risk-failure-case-draft-preview-runtime-smoke.md`, `docs/review/evidence-quality-risk-failure-case-draft-preview-runtime-smoke-remote-verification.md` | preview-only manual handoff; local runtime smoke and remote workflow verification exist; does not persist `failure_cases`; not automatic failure-case creation, final truth adjudication, retrieval quality evidence, Evidence Ledger quality evidence, or product-complete |

Historical Phase 31.5 boundary: JSON manifest only, not direct FK or join-table lineage. Phase 32 makes that manifest easier to inspect through a derived read model, but it still does not convert the manifest into a relational contract.

## Best External Claim

Use:

```text
Short external claim:

NoiseProof Agent is a small, inspectable portfolio service for evidence-first market intelligence: source profiling, parser/chunk/retrieval previews, deterministic local hash embedding preview, trace context headers, upload intake/parsed metadata persistence, manual chunk persistence, retrieval persistence with `metadata_json.candidate_chunk_ids`, caller-provided chunk embedding and semantic retrieval runtime proof, retrieval-run-linked Evidence Ledger/Noise Gate/Report persistence with precondition `409`s, persisted Report markdown export, persisted proof records, workflow-parent lineage, workflow direct stage links v0, failure-case records, document-derived failure-case draft/manual handoff, manual failure-case workflow-parent provenance, and local v0 auto-created workflow failure cases.

Detailed phase history remains in `docs/GOAL.md`, `docs/review/external-reader-proof-path.md`, `docs/application/portfolio-index.md`, and phase-specific `docs/review/*` artifacts.

Boundary: this is not product-complete declaration language, not hosted deployment evidence, not automatic failure-case creation beyond local v0, not production/background failure-case automation, not retry behavior, not root-cause automation, not complete workflow failure causality, and not production RAG quality.
```

Do not use:

```text
NoiseProof Agent is a production-ready RAG system.
NoiseProof Agent predicts markets.
NoiseProof Agent automates trading decisions.
```

## Next Proof-link Pass

If this repo is linked from the portfolio site, link only these claims:

- External-reader proof path: `docs/review/external-reader-proof-path.md`
- evidence-first data agent
- not a trading bot
- parser/chunk/retrieval preview boundaries
- uploaded file intake manifest preview, uploaded file intake manifest persistence, uploaded file parsed document persistence, uploaded file chunk persistence, uploaded file retrieval persistence, deterministic local hash embedding preview, caller-provided chunk embedding endpoint, caller-provided semantic retrieval persistence, retrieval-run-linked Evidence Ledger persistence, and runtime smoke
- retrieval-run-linked Noise Gate persistence and pre-ledger `409` runtime smoke
- retrieval-run-linked Report persistence and pre-gate `409` runtime smoke
- persisted Report markdown export
- Evidence Ledger Preview
- Persisted Evidence Ledger Records v0
- Noise Gate Preview
- Persisted Noise Gate Records v0
- Persisted Report Preview Records v0
- Record Linkage v0 through `workflow_trace_id`
- Trace-id Lookup v0
- Persisted Record Filtering v0
- Dashboard Trace/Filter Links v0
- Agent-run Linkage Review v0
- Agent-run Lifecycle v0
- Persisted Child Record Agent-run Linkage v0
- Deterministic Workflow Execution Preview v0
- WorkflowRun Child-record Links v0
- WorkflowRun Child Inspection Surface v0
- Workflow Stage Input Manifest v0
- Direct Evidence-to-gate/report Cross-link Review v0
- Direct Cross-stage Link Schema Review v0
- Workflow Lineage Read Model v0
- Workflow Proof Bundle Read Model v0
- Workflow Lineage Dashboard Links v0
- Operations Dashboard v0
- evaluation/application package
- Auto Trace Recording v0 for preview endpoint metadata
- Trace context header propagation v0
- Migration Runner Fresh DB Verification v0
- Fresh DB API Smoke Verification v0
- Failure-case Persistence Smoke Verification v0
- Agent-run Failure Linkage Smoke Verification v0
- Workflow Failure Linkage Smoke Verification v0
- Failure-case Workflow Linkage Review v0
- Failure-case Draft Preview v0
- Failure-case Draft Preview Smoke Verification v0
- Failure-case Draft Manual Handoff Smoke Verification v0
- Failure-case Draft Fresh DB Handoff Smoke Verification v0
- Failure-case Workflow Parent Linkage Fresh DB Verification v0
- Failure-case Workflow Parent Linkage Dashboard Surfacing v0
- Failure-case Workflow Parent Linkage Fresh DB Dashboard Smoke Verification v0
- Failure-case Workflow Parent Linkage Proof Index v0

For this proof chain, start with the proof index reader path. Its Allowed claim is limited to manual workflow parent provenance being persisted, fresh-DB verified, and surfaced in the plain operations dashboard. Its Forbidden claim keeps automatic failure-case creation beyond local v0, complete workflow failure causality, and hosted production deployment evidence out of bounds.

Avoid claims about:

- production deployment
- hosted deployment evidence
- automatic failure detection
- complete workflow failure causality
- automatic failure-case persistence
- external users
- robust PDF extraction
- actual embedding model generation and semantic retrieval quality
- distributed tracing
- market prediction accuracy
- direct evidence -> gate -> report foreign-key lineage
## Proof Gap Action Surface

Phase 858 adds `docs/review/proof-gap-action-surface.md`.

Reviewer-facing ops endpoints now include:

```text
GET /ops/proof-gaps
GET /ops/proof-gaps/{gap_id}
```

This surface exposes `acceptable_evidence`, `blocked_claims`, `proof_routes`,
and `recommended_next_gate` for the current proof gaps. It makes unresolved
claims easier to inspect without closing them.

For `semantic_retrieval_quality`, the status remains `unproven`, the blocked
claim remains `semantic retrieval quality is proven`, and the recommended next
gate is `representative_live_semantic_retrieval_quality_eval_v0`.

Boundary: this is `action_surface_only_not_new_proof_or_gap_closure`, not
robust PDF extraction evidence, live embedding generation proof, semantic
retrieval quality evidence, distributed tracing, hosted observability, hosted
deployment evidence, external reviewer feedback, customer validation, Braincrew
acceptance, or product-complete.

## Qrels-backed Semantic Retrieval Quality Eval

Phase 859 adds `docs/review/qrels-backed-semantic-quality-eval.md` and
`docs/evaluation/qrels-backed-semantic-quality-report.md`.

The evaluation uses explicit local qrels and a TREC-style run file:

```text
examples/semantic-retrieval-quality/qrels.txt
examples/semantic-retrieval-quality/semantic-run.txt
```

The report records:

```text
judged_coverage_at_k -> 0.6667
unjudged_retrieved_count_at_k -> 2
qrels_backed_semantic_quality_claim_blocked
```

Application-facing interpretation: NoiseProof can now show a qrels-backed toy
quality-evaluation path, including unjudged retrieved documents and missed
relevant documents. It still cannot claim semantic retrieval quality.

Boundary: this is qrels-backed toy fixture evaluation only, not semantic
retrieval quality evidence, embedding generation, benchmark evidence, model
comparison, live vector search quality evidence, hosted deployment evidence,
external reviewer feedback, customer validation, Braincrew acceptance, or
product-complete.
