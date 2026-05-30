# Application-ready Review

Status: Phase 40 review packet.

This is an application-ready review, not a product-complete declaration.

Not product-complete: robust PDF extraction, embeddings, semantic retrieval, distributed tracing, hosted deployment, and external user validation are still unproven.

## Summary

Current judgment: Partial application-ready portfolio artifact.

NoiseProof Agent is strong enough to show a Braincrew-style reviewer the project shape, service boundary, evidence-first workflow, operations surface, persisted Evidence Ledger v0 records, persisted Noise Gate v0 records, persisted Report Preview v0 records, `workflow_trace_id` correlation, direct trace lookup, persisted record filtering, dashboard trace/filter links, agent-run linkage review, parent agent-run lifecycle, child-record `agent_run_id` linkage, dashboard parent/child provenance links, dashboard Evidence Ledger table, evidence-to-gate/report cross-link review, single workflow parent review, WorkflowRun schema, WorkflowRun metadata persistence, WorkflowRun dashboard visibility, WorkflowRun child-link review, deterministic workflow execution preview, child `workflow_run_id` links, workflow-run child inspection, direct evidence-to-gate/report cross-link review, workflow stage input manifests, direct cross-stage link schema review, workflow lineage read model, dashboard lineage links, missing-reference review and test, boundary hardening review, manifest-shape hardening, warning taxonomy review, structured warning codes, warning-code documentation review, warning-code runbook example, warning-code dashboard review, warning-code dashboard surfacing, migration runner review/implementation/runtime verification, fresh DB API smoke evidence, failure-case persistence smoke evidence, agent-run failure linkage smoke evidence, workflow failure linkage smoke evidence, preview endpoint traces, failure records, and technical decision trail.

It is not strong enough to claim production RAG quality or autonomous market intelligence.

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
| migration runner can apply on fresh DB | Pass | `docs/review/migration-runner-fresh-db-verification.md` | local Docker only; not production migration orchestration |
| fresh DB API smoke path works | Pass | `docs/review/fresh-db-api-smoke-verification.md` | local Docker/API smoke only; not hosted deployment evidence |
| failure-case persistence smoke works | Pass | `docs/review/failure-case-persistence-smoke-verification.md` | stores manually submitted failure records; automatic failure detection is not claimed |
| agent-run failure linkage smoke works | Pass | `docs/review/agent-run-failure-linkage-smoke-verification.md` | links manual failure records to failed agent runs; complete workflow failure causality is not claimed |
| workflow failure linkage smoke works | Pass | `docs/review/workflow-failure-linkage-smoke-verification.md` | test-fixture proof only; complete workflow failure causality is not claimed |
| failure-case workflow linkage review exists | Pass | `docs/review/failure-case-workflow-linkage-review.md` | failure cases are not linked to workflow parents yet |

Historical Phase 31.5 boundary: JSON manifest only, not direct FK or join-table lineage. Phase 32 makes that manifest easier to inspect through a derived read model, but it still does not convert the manifest into a relational contract.

## Best External Claim

Use:

```text
NoiseProof Agent is a small, inspectable portfolio service that shows how messy market data can be profiled, retrieved, converted into persisted evidence entries, persisted as gate decisions, stored as claim-bounded report preview records, linked to a deterministic workflow parent with `workflow_run_id` plus `workflow_trace_id` correlation, inspected from the workflow parent detail endpoint, annotated with local stage input manifests for deterministic gate/report stages, projected through a derived workflow lineage read model, reached from dashboard workflow-row links, tested for missing manifest reference surfacing, hardened against malformed manifest id shapes, reviewed for lineage warning taxonomy, given structured lineage warning codes without dropping human-readable warnings, reviewed for warning-code documentation boundaries, documented with a runbook response-shape example, reviewed for bounded dashboard surfacing before UI changes, and surfaced in the plain dashboard as response-level taxonomy only. It does not yet claim direct evidence -> gate -> report foreign-key lineage.
```

Do not use:

```text
NoiseProof Agent is a production-ready RAG system.
NoiseProof Agent predicts markets.
NoiseProof Agent automates trading decisions.
```

## Next Proof-link Pass

If this repo is linked from the portfolio site, link only these claims:

- evidence-first data agent
- not a trading bot
- parser/chunk/retrieval preview boundaries
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

Avoid claims about:

- production deployment
- hosted deployment evidence
- automatic failure detection
- complete workflow failure causality
- external users
- robust PDF extraction
- semantic retrieval
- distributed tracing
- market prediction accuracy
- direct evidence -> gate -> report foreign-key lineage
