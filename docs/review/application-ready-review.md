# Application-ready Review

Status: Phase 82 review packet.

This is an application-ready review, not a product-complete declaration.

Not product-complete: robust PDF extraction, embeddings, semantic retrieval, distributed tracing, hosted deployment, and external user validation are still unproven.

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
| PDF, CSV, URL/HTML, markdown memo inputs supported | Partial | parser adapter stubs and text-only PDF fallback | robust PDF extraction is not claimed |
| document profile is generated | Pass | `POST /documents/profile` | direct text payloads only |
| three chunk strategies can be compared | Pass | fixed-window, heading-aware, row-aware | chunks are not persisted |
| retrieval returns source ids | Pass | lexical retrieval v0 | semantic retrieval is not implemented |
| Evidence Ledger can be generated before final answer | Pass | `POST /evidence-ledgers/preview`, `POST /evidence-ledgers` | persisted v0 entries are not yet linked to retrieval run ids |
| unsupported claims are blocked | Pass | Noise Gate, persisted Noise Gate, and Report Preview tests | deterministic checks only |
| contradictions are surfaced | Pass | Evidence Ledger and Noise Gate previews | not a full contradiction engine |
| buy/sell recommendation questions are refused or reframed | Pass | collection, ledger, gate, and report boundaries | not legal or financial advice tooling |
| every agent run leaves a trace | Pass for current preview endpoints | preview endpoints auto-create `agent_runs.trace_json`; retrieval has dedicated `retrieval_runs` | metadata trace only, not distributed tracing or a complete multi-stage workflow trace |
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

NoiseProof Agent is a small, inspectable portfolio service that demonstrates evidence-first workflow surfaces for messy market intelligence: source profiling, parser/chunk/retrieval previews, uploaded file intake manifest preview and uploaded file intake manifest persistence with content hash plus no-raw-storage boundary, persisted evidence/gate/report records, workflow-parent lineage, failure-case records, and manual failure-case workflow-parent provenance.

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
- uploaded file intake manifest preview, uploaded file intake manifest persistence, and runtime smoke
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
- Workflow Lineage Dashboard Links v0
- Operations Dashboard v0
- evaluation/application package
- Auto Trace Recording v0 for preview endpoint metadata
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
- semantic retrieval
- distributed tracing
- market prediction accuracy
- direct evidence -> gate -> report foreign-key lineage
