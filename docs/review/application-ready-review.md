# Application-ready Review

Status: Phase 82 review packet.

This is an application-ready review, not a product-complete declaration.

Not product-complete: robust PDF extraction, actual embedding model generation remains unproven, semantic retrieval quality, distributed tracing, hosted deployment, and external user validation are still unproven.

README proof-marker archive: `docs/review/readme-proof-marker-archive.md` preserves legacy README proof markers after README scanability cleanup. It is source-level provenance, not product runtime evidence, not hosted deployment evidence, not automatic failure-case creation, and not complete workflow failure causality.

## Summary

Current judgment: Partial application-ready portfolio artifact.

NoiseProof Agent is application-ready as a portfolio evidence packet: it shows a small local service with evidence-first workflow surfaces, operations visibility, persisted proof records, workflow-parent lineage, failure-case persistence, and bounded proof links before any free-form answer is claimed.

Detailed evidence remains in the checklist below and in the external-reader proof path. This summary is intentionally not a product-complete declaration.

Allowed external claim: local, inspectable portfolio evidence exists for the current bounded workflow surfaces.

Forbidden claim: this is not hosted deployment evidence, automatic persistence remains unclaimed, and this is not automatic failure-case creation, not complete workflow failure causality, not production RAG quality, and not autonomous market intelligence.

## Checklist

| Application-ready criterion | Status | Evidence | Boundary |
|---|---|---|---|
| local Docker Compose stack runs | Pass | `docker compose ps` shows healthy `noiseproof-agent-db` | local only |
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
| embedding provider source review exists | Pass | `docs/review/embedding-provider-source-review.md` | source review only; no API call; no dependency; no cost-incurring runtime path; actual embedding model generation remains unproven |
| embedding model provider disabled path exists | Pass | `POST /chunks/embedding-model-preview`, `docs/review/embedding-model-provider-disabled-path.md` | readiness/disabled path only; no provider call; no embedding vector is generated; no persistence; actual embedding model generation remains unproven |
| embedding model provider live-call review exists | Pass | `docs/review/embedding-model-provider-live-call-review.md` | guardrail review only; not implemented runtime behavior; no provider call; actual embedding model generation remains unproven |
| embedding model mocked-provider call exists | Pass | `POST /chunks/embedding-model-preview`, `docs/review/embedding-model-mocked-provider-call.md` | injected mocked provider only; no live OpenAI provider call; no live provider call in CI; no automatic persistence; actual live embedding model generation remains unproven |
| embedding model live-provider implementation review exists | Pass | `docs/review/embedding-model-live-provider-implementation-review.md` | owner-runtime implementation gate only; no live OpenAI provider call, no network call, no API cost, no persistence, and actual live embedding model generation remains unproven |
| embedding model live-provider code review exists | Pass | `docs/review/embedding-model-live-provider-code-review.md` | code insertion review only; no OpenAI dependency, no runtime behavior, no live provider call, no API cost, and actual live embedding model generation remains unproven |
| failure cases are recorded | Pass | failure case endpoint and dashboard | not comprehensive |
| operations dashboard shows runs and failures | Pass | `GET /ops/dashboard` | plain HTML, not polished UI |
| README is understandable without explanation | Pass | `README.md` | should still be reviewed by an external reader |
| architecture and ADRs exist | Pass | `docs/architecture.md`, `docs/adr/*` | ADRs cover initial decisions only |
| evaluation report exists | Pass | `docs/evaluation/*` | not a benchmark |
| Braincrew role map exists | Pass | `docs/application/braincrew-role-map.md` | role fit is an argument, not hiring proof |
| evidence -> gate -> report lineage exists | Partial | `POST /workflow-runs/execute-preview`, `GET /workflow-runs/{id}`, child `workflow_run_id` links, `workflow_trace_id` correlation | direct evidence -> gate -> report foreign-key links are still deferred |
| single workflow parent exists | Pass for deterministic preview | `POST /workflow-runs`, `GET /workflow-runs`, `GET /workflow-runs/{id}`, `POST /workflow-runs/execute-preview`, child `workflow_run_id` links | local deterministic preview only, not autonomous workflow execution |
| direct stage-level input links exist | Partial / derived read model | workflow-created Noise Gate and Report rows include `stage_input_manifest`; `GET /workflow-runs/{id}/lineage` resolves those manifest ids against existing child records; `docs/review/direct-cross-stage-link-schema-review.md` defers schema links | derived read model only, not direct FK or join-table lineage |
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
| uploaded file chunk persistence exists | Pass | `POST /documents/{document_id}/chunks`, `GET /documents/{document_id}/chunks`, `docs/review/uploaded-file-chunk-persistence-runtime-smoke.md`, `docs/review/uploaded-file-chunk-persistence-application-refresh.md` | manual document-scoped chunk text persistence only; no automatic upload-preview-to-chunk persistence; no embeddings; no retrieval persistence |
| uploaded file chunk handoff persistence exists | Pass | `POST /documents/upload-chunks`, `GET /documents/{document_id}/chunks`, `docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md`, `docs/review/uploaded-file-chunk-persistence-handoff-application-refresh.md` | explicit uploaded-file-to-chunks handoff only; no raw uploaded byte storage; no full parsed text persistence; no embeddings; no retrieval persistence |
| uploaded file retrieval persistence exists | Pass | `POST /documents/{document_id}/retrieval-runs`, `GET /retrieval-runs`, `docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md`, `docs/review/uploaded-file-retrieval-persistence-application-refresh.md` | explicit retrieval over persisted `document_chunks` only; no embeddings; no semantic retrieval; no Evidence Ledger generation; not financial advice |
| uploaded raw file quarantine storage exists | Pass | `POST /documents/upload-raw-files`, `GET /documents/upload-raw-files`, `docs/review/uploaded-raw-file-storage-runtime-smoke.md`, `docs/review/uploaded-raw-file-storage-application-refresh.md` | quarantined PostgreSQL BYTEA storage with metadata-only responses; not production malware scanning; not hosted deployment evidence |
| guarded raw file download endpoint runtime smoke exists | Pass | `GET /documents/upload-raw-files/{raw_file_id}/download`, `docs/review/uploaded-raw-file-download-endpoint-runtime-smoke.md`, `docs/review/uploaded-raw-file-download-rate-limit-local.md`, `docs/review/uploaded-raw-file-download-rate-limit-runtime-smoke.md` | latest clean scan required; no-scan and later failed scan return `409`; local v0 in-memory rate limit runtime smoke exists; local v0 no-auth marker; not production authorization, distributed rate limiting, hosted deployment evidence, or production malware scanning evidence |
| retrieval-run-linked Evidence Ledger persistence exists | Pass | `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`, `GET /evidence-ledgers`, `docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md` | deterministic handoff from persisted lexical retrieval runs only; no embeddings; no semantic retrieval; no LLM judgment; no Noise Gate or report generation |
| retrieval-run-linked Noise Gate persistence exists | Pass | `POST /retrieval-runs/{retrieval_run_id}/noise-gate`, `GET /noise-gates`, `docs/review/retrieval-run-linked-noise-gate-runtime-smoke.md` | deterministic handoff after linked Evidence Ledger rows only; pre-ledger `409`; no LLM judgment; no report generation; not financial advice |
| retrieval-run-linked Report persistence exists | Pass | `POST /retrieval-runs/{retrieval_run_id}/report`, `GET /reports`, `docs/review/retrieval-run-linked-report-runtime-smoke.md` | deterministic handoff after linked Evidence Ledger and Noise Gate rows only; pre-gate `409`; records `input_noise_gate_record_id`; no free-form final report generation; not financial advice |
| deterministic local hash embedding preview exists | Pass | `POST /chunks/embedding-preview`, `docs/review/deterministic-text-embedding-preview.md` | preview-only local hash vector; not persisted; not a semantic embedding model; actual embedding model generation remains unproven; not vector search quality evidence |
| caller-provided chunk embedding endpoint exists | Pass | `POST /chunks/{chunk_id}/embeddings`, `GET /chunks/{chunk_id}/embeddings`, `docs/review/embedding-endpoint-runtime-smoke.md` | caller-provided vectors only; no embedding generation; no semantic retrieval; no HNSW/IVFFlat behavior; not vector search quality |
| caller-provided semantic retrieval persistence exists | Pass | `POST /documents/{document_id}/semantic-retrieval-runs`, `GET /retrieval-runs`, `docs/review/semantic-retrieval-persistence-runtime-smoke.md`, `docs/review/semantic-retrieval-persistence-application-refresh.md` | caller-provided vectors over existing embeddings only; semantic retrieval quality remains unproven; no embedding generation; no Evidence Ledger generation from semantic retrieval |
| toy semantic retrieval quality report exists | Pass | `docs/evaluation/semantic-retrieval-quality-report.md`, `docs/review/semantic-retrieval-quality-report-application-refresh.md` | semantic retrieval quality report is toy fixture output; not vector search quality evidence, not a benchmark result, not a model comparison |
| migration runner can apply on fresh DB | Pass | `docs/review/migration-runner-fresh-db-verification.md` | local Docker only; not production migration orchestration |
| fresh DB API smoke path works | Pass | `docs/review/fresh-db-api-smoke-verification.md` | local Docker/API smoke only; not hosted deployment evidence |
| failure-case persistence smoke works | Pass | `docs/review/failure-case-persistence-smoke-verification.md` | stores manually submitted failure records; automatic failure detection is not claimed |
| agent-run failure linkage smoke works | Pass | `docs/review/agent-run-failure-linkage-smoke-verification.md` | links manual failure records to failed agent runs; complete workflow failure causality is not claimed |
| workflow failure linkage smoke works | Pass | `docs/review/workflow-failure-linkage-smoke-verification.md` | test-fixture proof only; complete workflow failure causality is not claimed |
| failure-case workflow linkage review exists | Pass | `docs/review/failure-case-workflow-linkage-review.md` | historical review boundary; manual workflow parent linkage now exists, while automatic failure-case creation remains unclaimed |
| failure-case draft preview exists | Pass | `POST /failure-cases/draft-preview` | returns a suggested payload only; does not persist failure cases automatically |
| failure-case draft preview smoke works | Pass | `docs/review/failure-case-draft-preview-smoke-verification.md` | route-level smoke only; automatic failure-case persistence is not claimed |
| failure-case draft manual handoff smoke works | Pass | `docs/review/failure-case-draft-manual-handoff-smoke-verification.md` | human confirmation boundary remains explicit; not automatic persistence |
| failure-case draft fresh DB handoff smoke works | Pass | `docs/review/failure-case-draft-fresh-db-handoff-smoke-verification.md` | local Docker DB evidence only; not hosted deployment evidence |
| workflow failure-to-draft smoke works | Pass | `docs/review/workflow-failure-to-draft-smoke-verification.md` | route-level smoke only; automatic failure-case creation remains unclaimed |
| failure-case workflow parent linkage fresh DB works | Pass | `docs/review/failure-case-workflow-parent-linkage-fresh-db-verification.md` | local Docker DB evidence only; not hosted deployment evidence; automatic failure-case creation remains unclaimed |
| failure-case workflow parent dashboard link works | Pass | `GET /ops/dashboard` Failure Cases table Workflow Parent column | manual provenance only; not automatic failure-case creation |
| failure-case workflow parent dashboard fresh DB smoke works | Pass | `docs/review/failure-case-workflow-parent-linkage-fresh-db-dashboard-smoke-verification.md` | local Docker DB dashboard evidence only; manual provenance only; not hosted deployment evidence |
| proof index reader path exists | Pass | `docs/review/failure-case-workflow-parent-linkage-proof-index.md` | index-only; no new runtime proof |
| External-reader proof path exists | Pass | `docs/review/external-reader-proof-path.md` | 5-minute path only; not hosted deployment evidence; not automatic failure-case creation; not complete workflow failure causality |
| README proof-marker archive is discoverable from application docs | Pass | `docs/review/readme-proof-marker-archive.md` | source-level provenance only; not product runtime evidence |

Historical Phase 31.5 boundary: JSON manifest only, not direct FK or join-table lineage. Phase 32 makes that manifest easier to inspect through a derived read model, but it still does not convert the manifest into a relational contract.

## Best External Claim

Use:

```text
Short external claim:

NoiseProof Agent is a small, inspectable portfolio service for evidence-first market intelligence: source profiling, parser/chunk/retrieval previews, deterministic local hash embedding preview exists, trace context header propagation exists, uploaded file intake manifest preview/persistence, parsed document metadata persistence, manual chunk persistence, retrieval persistence with `metadata_json.candidate_chunk_ids`, caller-provided chunk embedding runtime proof, caller-provided semantic retrieval persistence runtime proof, retrieval-run-linked Evidence Ledger/Noise Gate/Report persistence with precondition `409`s, persisted proof records, workflow-parent lineage, failure-case records, and manual failure-case workflow-parent provenance.

Detailed phase history remains in `docs/GOAL.md`, `docs/review/external-reader-proof-path.md`, `docs/application/portfolio-index.md`, and phase-specific `docs/review/*` artifacts.

Boundary: this is not product-complete declaration language, not hosted deployment evidence, not automatic failure-case creation, not complete workflow failure causality, and not production RAG quality.
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

For this proof chain, start with the proof index reader path. Its Allowed claim is limited to manual workflow parent provenance being persisted, fresh-DB verified, and surfaced in the plain operations dashboard. Its Forbidden claim keeps automatic failure-case creation, complete workflow failure causality, and hosted production deployment evidence out of bounds.

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
