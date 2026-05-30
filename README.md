# NoiseProof Agent

A noise-resilient data agent for messy market intelligence.

This project ingests messy documents and market data, evaluates chunking and retrieval strategies, detects contradictory evidence, and generates claim-bounded reports with citations. It is not a trading bot and does not provide buy/sell recommendations.

## What This Is

NoiseProof Agent is a planned RAG/agent service for market intelligence work where the input data is inconsistent, noisy, and difficult to trust.

The project started with a documentation-first Day 1 package. Day 2 added a small service skeleton: FastAPI routes, metadata persistence boundaries, PostgreSQL schema init SQL, and API smoke CI. Phase 2 added messy-data fixtures and Document Profiler v0. Phase 3 added parser adapter stubs for parse-preview boundaries. Phase 4 added a small chunk strategy experiment boundary. Phase 5 added lexical retrieval v0 over chunks and records retrieval runs. Phase 5.5 added a deterministic Collection Plan Preview so a question declares required information roles before evidence work starts. Phase 6 added Evidence Ledger Preview v0 so retrieval candidates can be promoted, weakened, contradicted, or blocked before any final answer exists. Phase 7 added Noise Gate Preview v0 so ledger entries can be blocked, downgraded, or allowed before report generation. Phase 8 added Claim-bounded Report Preview v0 so only gate-passing claims become report-shaped output. Phase 9 added Operations Dashboard v0 so the existing run, retrieval, and failure records are inspectable from the browser. Phase 11 added Auto Trace Recording v0 so preview endpoints leave `agent_runs.trace_json` metadata before the project claims a full agent workflow. Phase 12 added persisted Evidence Ledger records so unsupported and contradiction counts are no longer dashboard placeholders. Phase 13 added persisted Noise Gate records so gate decisions can be inspected after the preview call. Phase 14 added persisted Report Preview records so generated, blocked, and revision-needed report-shaped outputs can be inspected after the preview call. Phase 15 added `workflow_trace_id` linkage across persisted evidence, gate, report records, and their matching `agent_runs.trace_json`. Phase 16 added `GET /traces/{workflow_trace_id}` so a trace id can be inspected directly. Phase 17 added lightweight filters for persisted Evidence Ledger, Noise Gate, and Report record lists. Phase 18 added trace lookup and filter links to the plain operations dashboard. Phase 18.5 reviewed direct `agent_run_id` foreign-key linkage and kept it unimplemented until the run lifecycle is changed. Phase 19 added an agent-run lifecycle so traced operations create a parent run before execution and update that same run after completion or failure. Phase 20 added `agent_run_id` linkage on persisted Evidence Ledger, Noise Gate, and Report records. Phase 21 added parent-run provenance links to persisted gate and report rows in the plain dashboard. Phase 22 added a persisted Evidence Ledger table to the dashboard. Phase 22.5 reviewed evidence-to-gate/report cross-links and deferred them until a single workflow parent exists. Phase 23 reviewed the single workflow parent boundary and chose a future separate `workflow_runs` table over reusing `agent_runs`. Phase 24 added the `workflow_runs` schema and migration without adding workflow execution behavior. Phase 25 added minimal `workflow_runs` create/list metadata persistence without adding orchestration or child `workflow_run_id` links. Phase 26 surfaced workflow-run metadata in the plain operations dashboard while labeling it as metadata-only, not workflow execution. Phase 27 reviewed child `workflow_run_id` links and deferred them until a workflow execution boundary exists. Phase 28 added a deterministic workflow execution preview that creates a parent workflow run and runs retrieval -> evidence -> gate -> report preview steps. Phase 29 added nullable child `workflow_run_id` links for retrieval, evidence, gate, and report records created by that deterministic preview. Phase 30 added `GET /workflow-runs/{id}` so those linked child records can be inspected from the workflow parent. Phase 30.5 reviewed direct evidence -> gate -> report links again and deferred foreign-key claims until downstream stages consume persisted upstream row ids. Phase 31 added `stage_input_manifest` on workflow-created Noise Gate and Report records so persisted upstream ids are visible without claiming direct foreign-key lineage. Phase 31.5 reviewed whether to add direct cross-stage schema links and deferred new FK/join-table storage in favor of a derived lineage read model. Phase 32 added `GET /workflow-runs/{id}/lineage` as that derived read model over existing workflow child records and `stage_input_manifest`, without adding storage, migrations, direct foreign keys, or join tables. Phase 33 added detail and lineage links from workflow rows in the plain operations dashboard, without adding dashboard polish or new lineage storage. Phase 33.5 reviewed missing manifest reference behavior and chose a targeted missing-reference test as the next proof step, without adding runtime behavior. Phase 34 added that targeted missing-reference test and version marker without adding schema or mutation surfaces. Phase 34.5 reviewed manifest-shape, duplicate-reference, and cross-workflow hardening risks before adding any schema. Phase 35 hardened manifest-shape handling so non-list evidence id values no longer get treated as iterable id lists. Phase 35.5 reviewed lineage warning categories before adding structured warning fields. Phase 36 added `warning_codes` to the lineage response while preserving human-readable warnings. Phase 36.5 reviewed how warning codes should be documented before any dashboard or persistence expansion. Phase 37 added a runbook lineage response example showing both `warnings` and `warning_codes`. Phase 37.5 reviewed whether those codes should appear in the plain operations dashboard before adding any dashboard rendering. Phase 38 surfaced the warning-code legend in the plain dashboard as response-level taxonomy only. Phase 38.5 added the runbook smoke example for that dashboard legend. Phase 39 reviewed whether to rename the runtime `workflow_version` after dashboard-only phases. Phase 40 renamed the runtime `workflow_version` to `phase40-lineage-warning-code-dashboard` without changing workflow semantics. Phase 40.5 added explicit runbook smoke checks showing that renamed workflow version on `/health` and `/ops/summary`. Phase 41 reviewed workflow-version naming consistency and identified stale executable schema defaults as the next bounded update. Phase 42 updated fresh schema defaults and added a forward migration for the current workflow-version marker. Phase 42.5 added a runbook smoke example for inspecting those schema defaults. Phase 43 verified the local Docker DB defaults before and after applying migration 010. Phase 44 reviewed migration handling and selected a lightweight SQL migration runner as the next bounded implementation. Phase 45 added that runner as a small `schema_migrations`-backed CLI over existing SQL files. Phase 46 verified the runner against the local Docker DB using status, baseline, and final status checks.

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

- Product definition: documented
- Architecture: documented
- ADRs: documented
- Local database service: configured
- FastAPI health endpoint: implemented
- PostgreSQL schema init: implemented
- Document metadata endpoints: implemented
- Agent run metadata endpoints: implemented
- Failure case endpoints: implemented
- Ops summary placeholder: implemented
- Messy market data fixtures: implemented
- Document Profiler v0: implemented
- Parser adapter stubs: implemented for markdown, CSV, HTML/URL, PDF text-only fallback, and unknown source types
- Chunk strategy experiment v0: implemented for fixed-window, heading-aware, and row-aware strategies
- Retrieval v0: implemented for lexical candidate search over chunk-preview output with source ids
- Collection Plan Preview: implemented for role-based information needs before Evidence Ledger work
- Evidence Ledger Preview: implemented for deterministic claim-level entries over retrieval candidates
- Noise Gate Preview: implemented for deterministic pre-report checks over ledger entries and draft claims
- Claim-bounded Report Preview: implemented for gate-passing ledger entries
- Operations Dashboard v0: implemented as a plain FastAPI HTML view over current metadata records
- Evaluation/Application Package v0: implemented for evaluation planning, failure cases, Braincrew role mapping, cover message, and portfolio index
- Application-ready review: implemented as a partial/pass boundary checklist
- Auto Trace Recording v0: implemented for document profile, parse, chunk, collection plan, evidence ledger, noise gate, and report preview endpoints
- Persisted Evidence Ledger records v0: implemented with `POST /evidence-ledgers`, `GET /evidence-ledgers`, and real ops counts for unsupported and contradicted entries
- Persisted Noise Gate records v0: implemented with `POST /noise-gates`, `GET /noise-gates`, and ops counts for blocked/revision gate decisions
- Persisted Report Preview records v0: implemented with `POST /reports`, `GET /reports`, and ops counts for generated/blocked/revision report-shaped outputs
- Record Linkage v0: implemented with shared `workflow_trace_id` values on persisted evidence, gate, report records, and matching agent-run traces
- Trace-id lookup v0: implemented with `GET /traces/{workflow_trace_id}`
- Persisted record filtering v0: implemented for `GET /evidence-ledgers`, `GET /noise-gates`, and `GET /reports`
- Dashboard trace/filter links v0: implemented in `GET /ops/dashboard`
- Agent-run linkage review v0: implemented as `docs/review/agent-run-linkage-review.md`
- Agent-run lifecycle v0: implemented in `run_with_trace()`
- Persisted child record agent-run linkage v0: implemented for Evidence Ledger, Noise Gate, and Report records
- Dashboard parent/child provenance links v0: implemented for Noise Gate and Report record rows
- Evidence Ledger dashboard table v0: implemented for persisted evidence rows
- Evidence-to-gate/report local cross-links review v0: implemented as a review-only decision artifact
- Single workflow parent review v0: implemented as a review-only decision artifact
- WorkflowRun schema v0: implemented as `workflow_runs` table SQL and migration
- WorkflowRun metadata persistence v0: implemented with `POST /workflow-runs` and `GET /workflow-runs`
- WorkflowRun dashboard table v0: implemented as metadata-only visibility in `GET /ops/dashboard`
- WorkflowRun child-link review v0: implemented as a review-only decision artifact
- Deterministic workflow execution preview v0: implemented with `POST /workflow-runs/execute-preview`
- WorkflowRun child-record links v0: implemented with nullable `workflow_run_id` on retrieval, evidence, gate, and report records
- WorkflowRun child inspection surface v0: implemented with `GET /workflow-runs/{id}`
- Direct evidence-to-gate/report cross-link review v0: implemented as a review-only decision artifact
- Workflow stage input manifest v0: implemented with `stage_input_manifest` on workflow-created Noise Gate and Report records
- Direct cross-stage link schema review v0: implemented as a review-only decision artifact
- Workflow lineage read model v0: implemented with `GET /workflow-runs/{id}/lineage`
- Workflow lineage dashboard links v0: implemented in `GET /ops/dashboard`
- Workflow lineage missing-reference review v0: implemented as `docs/review/workflow-lineage-missing-reference-review.md`
- Workflow lineage missing-reference test v0: implemented for broken `stage_input_manifest` fixtures
- Workflow lineage boundary hardening review v0: implemented as `docs/review/workflow-lineage-boundary-hardening-review.md`
- Workflow lineage manifest-shape hardening v0: implemented for non-list manifest values, duplicate references, and cross-workflow references
- Workflow lineage warning taxonomy review v0: implemented as `docs/review/workflow-lineage-warning-taxonomy-review.md`
- Structured warning taxonomy v0: implemented as `warning_codes` on `GET /workflow-runs/{id}/lineage`
- Workflow lineage warning code documentation review v0: implemented as `docs/review/workflow-lineage-warning-code-documentation-review.md`
- Workflow lineage warning code runbook example v0: implemented in `docs/runbook.md`
- Workflow lineage warning code dashboard review v0: implemented as `docs/review/workflow-lineage-warning-code-dashboard-review.md`
- Workflow lineage warning code dashboard surfacing v0: implemented as a bounded legend in `GET /ops/dashboard`
- Workflow lineage warning code dashboard smoke example v0: implemented in `docs/runbook.md`
- Workflow version naming review v0: implemented as `docs/review/workflow-version-naming-review.md`
- Workflow version naming update v0: implemented as `phase40-lineage-warning-code-dashboard`
- Workflow version naming smoke example v0: implemented in `docs/runbook.md`
- Workflow version naming consistency review v0: implemented as `docs/review/workflow-version-naming-consistency-review.md`
- Schema default workflow version update v0: implemented with fresh init defaults and `db/migrations/010_workflow_version_defaults.sql`
- Schema default workflow version smoke example v0: implemented in `docs/runbook.md`
- Runtime DB schema default verification v0: implemented as `docs/review/runtime-db-schema-default-verification.md`
- Migration runner review v0: implemented as `docs/review/migration-runner-review.md`
- Lightweight SQL migration runner v0: implemented as `python -m app.migration_runner`
- Runtime migration runner verification v0: implemented as `docs/review/runtime-migration-runner-verification.md`
- Migration runner fresh DB verification v0: implemented as `docs/review/migration-runner-fresh-db-verification.md`
- Migration runner runbook cleanup v0: implemented in `docs/runbook.md`
- Fresh DB API smoke verification v0: implemented as `docs/review/fresh-db-api-smoke-verification.md`
- Application evidence index refresh v0: implemented across application-facing docs
- Failure-case persistence smoke verification v0: implemented as `docs/review/failure-case-persistence-smoke-verification.md`
- Failure-case application evidence refresh v0: implemented across application-facing docs
- Web app, file upload parsing, robust PDF extraction, persisted chunks, embeddings, and free-form final report generation: planned, not implemented

## Implementation Status

### Day 1 - Documentation-first package

- Product brief: done
- Architecture: done
- ADRs: done
- Docker Compose database target: done

### Day 2 - Service skeleton

- FastAPI health endpoint: done
- PostgreSQL schema init: done
- Document metadata endpoints: done
- Agent run metadata endpoints: done
- Failure case endpoints: done
- Ops summary placeholder: done
- GitHub Actions API smoke CI: done
- Runbook: done

### Phase 2 - Ingestion fixtures and Document Profiler v0

- Messy market data fixture pack: done
- Reusable profiler package: done
- `POST /documents/profile`: done
- Profile fields for source type, counts, table/url/date/number detection, extraction quality, recommended strategy, and warnings: done

### Phase 3 - Parser adapter stubs

- Parser boundary package: done
- Markdown parser metadata for headings, links, and bullets: done
- CSV parser metadata for rows, columns, headers, and malformed row warnings: done
- HTML/URL text preview and link metadata: done
- PDF text-only fallback with explicit non-claim about robust PDF extraction: done
- Unknown source type structured failure candidate: done
- `POST /documents/parse-preview`: done

### Phase 4 - Chunk strategy experiment v0

- `POST /documents/chunk-preview`: done
- Fixed-window chunking with max-character and overlap controls: done
- Heading-aware chunking with `header_path` metadata: done
- Row-aware chunking with CSV header and row metadata: done
- Strategy comparison metrics for chunk count, character distribution, boundary count, oversized chunks, and estimated tokens: done
- Unknown source types keep parser failure candidates and skip chunking: done

### Phase 5 - Retrieval v0

- `POST /retrieval-runs`: done
- `GET /retrieval-runs`: done
- Lexical candidate search over generated chunks: done
- Source ids returned on each retrieval candidate: done
- Retrieval run records stored in `retrieval_runs`: done
- No-results retrieval case recorded with `status: no_results`: done

### Phase 5.5 - Collection Plan Preview

- `POST /collection-plans/preview`: done
- Question-only input: done
- Required information roles returned before Evidence Ledger work: done
- Buy/sell drift questions include `user_intent_check` and stop conditions: done
- Underspecified, numeric, and source-quality questions expose role-specific warnings: done
- LLM calls, external search, retrieval expansion, Evidence Ledger generation, final reports, dashboard, and DB persistence were not implemented in Phase 5.5

### Phase 6 - Evidence Ledger Preview v0

- `POST /evidence-ledgers/preview`: done
- Retrieval candidates can become claim-level ledger entries: done
- Supported, weakly_supported, contradicted, unsupported, and blocked statuses: done
- Source id, source type, source date, evidence span, confidence, limitation, contradicting source ids, matched terms, and role are returned: done
- No-evidence questions produce a blocked ledger entry: done
- Buy/sell drift questions produce a blocked ledger entry: done
- Contradiction language is surfaced before report generation: done
- LLM calls, external search, Critic / Noise Gate, final reports, dashboard, and Evidence Ledger DB persistence: not implemented

### Phase 7 - Noise Gate Preview v0

- `POST /noise-gates/preview`: done
- Checks whether ledger entries can pass into a future report stage: done
- Blocks unsupported or blocked ledger entries: done
- Blocks buy/sell and financial-advice drift: done
- Requires revision for contradictions, missing source recency, missing limitations, and high-confidence claims with fewer than two source ids: done
- Flags overconfident draft language: done
- Returns decision, checks, blocked claims, downgraded claims, allowed claims, required revisions, fallback message, and warnings: done
- LLM calls, persisted report records, final reports, dashboard UI polish, and answer generation: not implemented

### Phase 8 - Claim-bounded Report Preview v0

- `POST /reports/preview`: done
- Runs Noise Gate before report formatting: done
- Generates report output only when the gate decision is `pass`: done
- Includes summary, claims, source ids, evidence spans, confidence, limitations, contradictions, and next data needed: done
- Returns fallback message and required revisions when the gate is `blocked` or `needs_revision`: done
- LLM calls, persisted report records, and free-form answer generation: not implemented

### Phase 9 - Operations Dashboard v0

- `GET /ops/dashboard`: done
- Browser-readable operations surface for current metadata: done
- Shows summary counts, recent agent runs, failure cases, and retrieval runs: done
- Phase 9 originally kept unsupported claim and contradiction counts as placeholders; Phase 12 connects those counts to persisted Evidence Ledger entries
- Next.js, UI polish, new model behavior, new retrieval behavior, and persisted report records: not implemented

### Phase 10 - Evaluation/Application Package v0

- `docs/evaluation/eval-plan.md`: done
- `docs/evaluation/retrieval-eval-report.md`: done
- `docs/evaluation/failure-cases.md`: done
- `docs/application/braincrew-role-map.md`: done
- `docs/application/cover-message.md`: done
- `docs/application/portfolio-index.md`: done
- `docs/review/application-ready-review.md`: done
- Runtime product behavior, new retrieval behavior, LLM calls, and deployment: not implemented in Phase 10

### Phase 11 - Auto Trace Recording v0

- Preview endpoints auto-create `agent_runs` metadata records: done
- `trace_json` records endpoint, phase, source type, counts, decisions, and report status where available: done
- Failed preview operations are wrapped so a failed trace can be recorded before the exception is re-raised: done
- Full distributed tracing, hosted observability, agent-run-linked gate records, and persisted report records: not implemented

### Phase 12 - Persisted Evidence Ledger Records v0

- `POST /evidence-ledgers`: done
- `GET /evidence-ledgers`: done
- `evidence_ledger_entries` table and migration: done
- unsupported and contradiction counts in `/ops/summary`: done
- unsupported and contradiction counts in `/ops/dashboard`: done
- Retrieval-run-linked ledger persistence, persisted report records, embeddings, and semantic retrieval: not implemented in Phase 12
- Direct agent-run linkage was added later in Phase 20

### Phase 13 - Persisted Noise Gate Records v0

- `POST /noise-gates`: done
- `GET /noise-gates`: done
- `noise_gate_records` table and migration: done
- blocked and needs-revision gate counts in `/ops/summary`: done
- Noise Gate Records section in `/ops/dashboard`: done
- Phase 13 persisted gate records without direct agent-run linkage; that linkage was added later in Phase 20
- LLM calls, embeddings, semantic retrieval, and free-form final report generation: not implemented

### Phase 14 - Persisted Report Preview Records v0

- `POST /reports`: done
- `GET /reports`: done
- `report_records` table and migration: done
- generated, blocked, and needs-revision report counts in `/ops/summary`: done
- Report Records section in `/ops/dashboard`: done
- Phase 14 used deterministic report persistence without direct `agent_run_id`; that linkage was added later in Phase 20
- LLM calls, embeddings, semantic retrieval, and free-form final report generation: not implemented

### Phase 15 - Record Linkage v0

- `workflow_trace_id` on `evidence_ledger_entries`: done
- `workflow_trace_id` on `noise_gate_records`: done
- `workflow_trace_id` on `report_records`: done
- Matching `workflow_trace_id` in `agent_runs.trace_json` for persisted evidence/gate/report endpoints: done
- Phase 15 used `workflow_trace_id` correlation before direct `agent_run_id` child-record linkage was added in Phase 20
- distributed tracing, LLM calls, embeddings, and semantic retrieval: not implemented

### Phase 16 - Trace-id Lookup v0

- `GET /traces/{workflow_trace_id}`: done
- Trace lookup returns matching agent runs, Evidence Ledger entries, Noise Gate records, Report records, and summary counts: done
- It is a local inspectability endpoint, not distributed tracing or hosted observability

### Phase 17 - Persisted Record Filtering v0

- `GET /evidence-ledgers?workflow_trace_id=...`: done
- `GET /evidence-ledgers?status=...`: done
- `GET /noise-gates?workflow_trace_id=...`: done
- `GET /noise-gates?decision=...`: done
- `GET /reports?workflow_trace_id=...`: done
- `GET /reports?status=...`: done
- This is read-only filtering, not a search engine or dashboard polish

### Phase 18 - Dashboard Trace/Filter Links v0

- `GET /ops/dashboard` includes quick links to trace lookup and persisted record filters: done
- Noise Gate records link to `GET /traces/{workflow_trace_id}` and `GET /noise-gates?workflow_trace_id=...`: done
- Report records link to `GET /traces/{workflow_trace_id}` and `GET /reports?workflow_trace_id=...`: done
- Static filter links are exposed for evidence statuses, gate decisions, and report statuses: done
- This is still a plain inspectability surface, not visual dashboard polish

### Phase 18.5 - Agent-run Linkage Review v0

- `docs/review/agent-run-linkage-review.md`: done
- Direct `agent_run_id` foreign-key linkage: reviewed here, implemented later in Phase 20
- At that review gate, the accepted link remained `workflow_trace_id`
- Future implementation should create the agent run first, then persist child records with its id

### Phase 19 - Agent-run Lifecycle v0

- `run_with_trace()` creates a parent `agent_runs` row with `status: running` before executing the operation: done
- the same `agent_runs` row is updated to `completed` or `failed`: done
- failed operations keep one failed parent run instead of creating a separate trace row after failure: done
- `ended_at`, `latency_ms`, `error_message`, and final `trace_json` are updated on the parent run: done
- direct `agent_run_id` foreign-key linkage for persisted Evidence Ledger, Noise Gate, and Report records: added in the following Phase 20 gate

### Phase 20 - Persisted Child Record Agent-run Linkage v0

- `agent_run_id` on persisted Evidence Ledger entries: done
- `agent_run_id` on persisted Noise Gate records: done
- `agent_run_id` on persisted Report records: done
- `db/migrations/006_child_agent_run_ids.sql`: done
- `GET /traces/{workflow_trace_id}` returns child records with the matching parent run id: done
- this is local parent/child linkage, not distributed tracing or hosted observability

### Phase 21 - Dashboard Parent/Child Provenance Links v0

- `GET /ops/dashboard` shows parent run links for persisted Noise Gate rows: done
- `GET /ops/dashboard` shows parent run links for persisted Report rows: done
- Parent run links route through `GET /traces/{workflow_trace_id}`: done
- This is still a plain inspectability surface, not dashboard polish or distributed tracing

### Phase 22 - Evidence Ledger Dashboard Table v0

- `GET /ops/dashboard` shows persisted Evidence Ledger rows: done
- Evidence rows include trace links, parent run links, status filters, claim, evidence span, source, and confidence: done
- This is still a bounded operations view, not dashboard polish or semantic search

### Phase 22.5 - Evidence-to-gate/report Local Cross-links Review v0

- `docs/review/evidence-to-gate-report-cross-links-review.md`: done
- Direct evidence -> gate -> report cross-link columns: deferred
- Future acceptance requires a single workflow parent before cross-stage links are claimed
- This is a review-only gate, not a migration, endpoint, dashboard behavior, or workflow orchestration change

### Phase 23 - Single Workflow Parent Review v0

- `docs/review/single-workflow-parent-review.md`: done
- Reusing `agent_runs` as the workflow parent: rejected
- Future `workflow_runs` table direction: accepted for a later implementation gate
- This is a review-only gate, not a migration, endpoint, dashboard behavior, or workflow orchestration change

### Phase 24 - WorkflowRun Schema v0

- `workflow_runs` table in `db/init/001_schema.sql`: done
- `db/migrations/007_workflow_runs.sql`: done
- Workflow parent status boundary: done
- Workflow execution endpoints, child `workflow_run_id` links, and dashboard behavior: not implemented in this phase

### Phase 25 - WorkflowRun Metadata Persistence v0

- `POST /workflow-runs`: done
- `GET /workflow-runs`: done
- WorkflowRun route, schemas, and repository methods: done
- Workflow orchestration, child `workflow_run_id` links, and dashboard behavior: not implemented in this phase

### Phase 26 - WorkflowRun Dashboard Table v0

- `GET /ops/dashboard` shows workflow-run metadata rows: done
- Dashboard copy labels the table as metadata-only and not workflow execution: done
- Workflow orchestration and child `workflow_run_id` links: not implemented in this phase

### Phase 27 - WorkflowRun Child-link Review v0

- `docs/review/workflow-run-child-link-review.md`: done
- Child `workflow_run_id` columns: deferred until a workflow execution boundary exists
- This is a review-only gate, not a migration, endpoint, dashboard behavior, or orchestration change

### Phase 28 - Deterministic Workflow Execution Preview v0

- `POST /workflow-runs/execute-preview`: done
- Parent `workflow_runs` row is created before deterministic execution and updated after completion or failure: done
- Deterministic retrieval -> evidence -> gate -> report preview sequence: done
- Child records are correlated with `workflow_trace_id`: done
- Child `workflow_run_id` columns were added in Phase 29
- Semantic retrieval, embeddings, LLM calls, external search, and free-form final answer generation: not implemented

### Phase 29 - WorkflowRun Child-record Links v0

- `workflow_run_id` on `retrieval_runs`: done
- `workflow_run_id` on `evidence_ledger_entries`: done
- `workflow_run_id` on `noise_gate_records`: done
- `workflow_run_id` on `report_records`: done
- `db/migrations/008_child_workflow_run_ids.sql`: done
- `POST /workflow-runs/execute-preview` attaches deterministic child records to its parent workflow run: done
- Direct evidence -> gate -> report foreign-key links, autonomous workflow execution, semantic retrieval, embeddings, LLM calls, external search, and free-form final answer generation: not implemented

### Phase 30 - WorkflowRun Child Inspection Surface v0

- `GET /workflow-runs/{id}`: done
- Response returns workflow parent, linked retrieval runs, Evidence Ledger entries, Noise Gate records, Report records, and summary counts: done
- It inspects existing local child links; it does not add direct evidence -> gate -> report foreign-key links or autonomous workflow execution

### Phase 30.5 - Direct Evidence-to-gate/report Cross-link Review v0

- `docs/review/direct-evidence-gate-report-cross-link-review.md`: done
- Direct evidence -> gate -> report foreign-key links: deferred
- Reason: downstream stages still consume evidence-shaped values, not persisted upstream row ids
- Follow-up implemented in Phase 31: Workflow stage input manifest v0

### Phase 31 - Workflow Stage Input Manifest v0

- `stage_input_manifest` on workflow-created Noise Gate records: done
- `stage_input_manifest` on workflow-created Report records: done
- deterministic workflow gate manifest records persisted Evidence Ledger row ids consumed as gate input: done
- deterministic workflow report manifest records persisted Evidence Ledger row ids and Noise Gate record id consumed as report input: done
- Direct evidence -> gate -> report foreign-key links: still not implemented

### Phase 31.5 - Direct Cross-stage Link Schema Review v0

- `docs/review/direct-cross-stage-link-schema-review.md`: done
- Direct evidence -> gate -> report foreign-key links: still deferred
- Join tables: still deferred
- Reason: `stage_input_manifest` proves local deterministic stage input provenance, not strict relational lineage
- Next direction: Workflow lineage read model v0

### Phase 32 - Workflow Lineage Read Model v0

- `GET /workflow-runs/{id}/lineage`: done
- Derived lineage from existing workflow child records and `stage_input_manifest`: done
- Noise Gate input Evidence Ledger ids are resolved back to linked Evidence Ledger records: done
- Report input Evidence Ledger ids and Noise Gate record ids are resolved back to linked records: done
- Missing manifest references are surfaced as warnings and summary counts: done
- New storage, migrations, direct foreign keys, and join tables: not implemented

### Phase 33 - Workflow Lineage Dashboard Links v0

- `GET /ops/dashboard` workflow rows link to `GET /workflow-runs/{id}`: done
- `GET /ops/dashboard` workflow rows link to `GET /workflow-runs/{id}/lineage`: done
- Dashboard copy labels lineage as a derived read model: done
- New storage, migrations, direct foreign keys, join tables, frontend framework, and dashboard polish: not implemented

### Phase 33.5 - Workflow Lineage Missing-reference Review v0

- Missing manifest reference behavior reviewed for `GET /workflow-runs/{id}/lineage`: done
- `docs/review/workflow-lineage-missing-reference-review.md`: done
- Next proof step selected as a targeted missing-reference test fixture: done
- Runtime behavior, migrations, columns, join tables, malformed-manifest mutation endpoint, and repair endpoint: not implemented

### Phase 34 - Workflow Lineage Missing-reference Test v0

- Broken `stage_input_manifest` fixture for `GET /workflow-runs/{id}/lineage`: done
- `missing_reference_count > 0` assertion: done
- missing Evidence Ledger ids and missing Noise Gate id assertions: done
- `phase34-workflow-lineage-missing-reference-test` workflow version marker: done
- Malformed-manifest mutation endpoint, repair endpoint, migrations, columns, and join tables: not implemented

### Phase 34.5 - Workflow Lineage Boundary Hardening Review v0

- `docs/review/workflow-lineage-boundary-hardening-review.md`: done
- Non-list manifest values reviewed as the next hardening risk: done
- Duplicate references and cross-workflow references reviewed: done
- Runtime behavior, migrations, columns, join tables, mutation endpoints, and repair endpoints: not implemented

### Phase 35 - Workflow Lineage Manifest-shape Hardening v0

- Non-list `input_evidence_ledger_entry_ids` values return an empty id list: done
- Invalid manifest shape warning says `input_evidence_ledger_entry_ids must be a list`: done
- Cross-workflow references remain local missing references: done
- Duplicate manifest references preserve order and count: done
- `phase35-workflow-lineage-manifest-shape-hardening` workflow version marker: done
- Migrations, columns, join tables, mutation endpoints, and repair endpoints: not implemented

### Phase 35.5 - Workflow Lineage Warning Taxonomy Review v0

- `docs/review/workflow-lineage-warning-taxonomy-review.md`: done
- Warning categories reviewed: `derived_read_model_boundary`, `missing_manifest_reference`, `invalid_manifest_shape`, `local_workflow_scope`
- Human-readable warning strings remain the current API shape: done
- Warning code fields, migrations, columns, join tables, mutation endpoints, and repair endpoints: not implemented
- Next direction: structured warning taxonomy v0

### Phase 36 - Structured Warning Taxonomy v0

- `GET /workflow-runs/{id}/lineage` returns `warning_codes`: done
- Existing human-readable `warnings` remain available: done
- Codes implemented: `derived_read_model_boundary`, `local_workflow_scope`, `missing_manifest_reference`, `invalid_manifest_shape`
- `phase40-lineage-warning-code-dashboard` workflow version marker: done
- Migrations, columns, join tables, mutation endpoints, repair endpoints, and warning-code persistence: not implemented

### Phase 36.5 - Workflow Lineage Warning Code Documentation Review v0

- `docs/review/workflow-lineage-warning-code-documentation-review.md`: done
- Warning-code meaning table: done
- Human-readable warnings remain canonical for readers: done
- Runtime behavior, migrations, columns, join tables, dashboard rendering, and warning-code persistence: not implemented
- Next direction: workflow lineage warning code runbook example v0

### Phase 37 - Workflow Lineage Warning Code Runbook Example v0

- `docs/runbook.md` shows expected `/workflow-runs/{id}/lineage` response shape: done
- Example includes both `warnings` and `warning_codes`: done
- Example includes `derived_read_model_boundary` and `local_workflow_scope`: done
- Example states warning codes are response-level taxonomy only: done
- Runtime behavior, migrations, columns, join tables, dashboard rendering, and warning-code persistence: not implemented

### Phase 37.5 - Workflow Lineage Warning Code Dashboard Review v0

- `docs/review/workflow-lineage-warning-code-dashboard-review.md`: done
- `GET /ops/dashboard` warning-code surfacing boundary: reviewed
- Dashboard rendering change: deferred to a later bounded gate
- Runtime behavior, migrations, columns, join tables, warning-code persistence, and warning-code enum tables: not implemented

### Phase 38 - Workflow Lineage Warning Code Dashboard Surfacing v0

- Workflow lineage warning code dashboard surfacing v0: implemented
- `GET /ops/dashboard` shows a compact Lineage warning codes legend: done
- Legend includes `derived_read_model_boundary`, `local_workflow_scope`, `missing_manifest_reference`, and `invalid_manifest_shape`: done
- Legend states codes are response-level taxonomy only and not persisted dashboard analytics: done
- Migrations, columns, join tables, warning-code persistence, and warning-code enum tables: not implemented

### Phase 38.5 - Workflow Lineage Warning Code Dashboard Smoke Example v0

- Workflow lineage warning code dashboard smoke example v0: implemented
- `docs/runbook.md` shows the expected `/ops/dashboard` warning-code legend: done
- Runtime behavior, migrations, columns, join tables, and dashboard rendering changes: not implemented

### Phase 39 - Workflow Version Naming Review v0

- `docs/review/workflow-version-naming-review.md`: done
- Current runtime `workflow_version` value reviewed: done
- Runtime rename: deferred to a dedicated update gate
- Runtime behavior, migrations, columns, join tables, trace schema changes, and dashboard rendering changes: not implemented

### Phase 40 - Workflow Version Naming Update v0

- Workflow version naming update v0: implemented
- Runtime `workflow_version` default is `phase40-lineage-warning-code-dashboard`: done
- `AgentRunCreate` and `WorkflowRunCreate` defaults use the same version: done
- README/runbook examples updated: done
- Workflow semantics, storage schema, retrieval, Evidence Ledger, Noise Gate, report, dashboard rendering, LLM, and embedding behavior: not changed

### Phase 40.5 - Workflow Version Naming Smoke Example v0

- Workflow version naming smoke example v0: implemented
- `docs/runbook.md` shows expected `/health` and `/ops/summary` workflow-version smoke checks: done
- Expected `workflow_version` remains `phase40-lineage-warning-code-dashboard`: done
- Workflow semantics, storage schema, retrieval, Evidence Ledger, Noise Gate, report, dashboard rendering, LLM, and embedding behavior: not changed

### Phase 41 - Workflow Version Naming Consistency Review v0

- Workflow version naming consistency review v0: implemented
- `docs/review/workflow-version-naming-consistency-review.md`: done
- Runtime-facing workflow-version surfaces use `phase40-lineage-warning-code-dashboard`: reviewed
- Stale executable schema defaults in `db/init/001_schema.sql` and `db/migrations/007_workflow_runs.sql`: identified
- Schema defaults, migrations, columns, runtime behavior, workflow semantics, dashboard rendering, LLM, and embedding behavior: not changed

### Phase 42 - Schema Default Workflow Version Update v0

- Schema default workflow version update v0: implemented
- Fresh `db/init/001_schema.sql` defaults for `agent_runs.workflow_version` and `workflow_runs.workflow_version` use `phase40-lineage-warning-code-dashboard`: done
- Forward migration `db/migrations/010_workflow_version_defaults.sql`: done
- Historical migration `007_workflow_runs.sql`: not rewritten
- Workflow semantics, storage columns, retrieval, Evidence Ledger, Noise Gate, report, dashboard rendering, LLM, and embedding behavior: not changed

### Phase 42.5 - Schema Default Workflow Version Smoke Example v0

- Schema default workflow version smoke example v0: implemented
- `docs/runbook.md` shows the SQL query for `agent_runs.workflow_version` and `workflow_runs.workflow_version` defaults: done
- Expected default marker is `phase40-lineage-warning-code-dashboard`: done
- Runtime behavior, workflow semantics, migrations, columns, dashboard rendering, LLM, and embedding behavior: not changed

### Phase 43 - Runtime DB Schema Default Verification v0

- Runtime DB schema default verification v0: implemented
- `docs/review/runtime-db-schema-default-verification.md`: done
- Existing Docker volume stale defaults before migration 010: recorded
- Migration 010 applied to the running DB: done
- Post-migration defaults for `agent_runs.workflow_version` and `workflow_runs.workflow_version`: verified as `phase40-lineage-warning-code-dashboard`
- Volume deletion, workflow semantics, columns, dashboard rendering, LLM, and embedding behavior: not changed

### Phase 44 - Migration Runner Review v0

- Migration runner review v0: implemented
- `docs/review/migration-runner-review.md`: done
- Runbook-only `psql` piping: reviewed
- Alembic: reviewed as larger than the current phase needs
- Lightweight SQL migration runner with `schema_migrations`: selected as next bounded implementation
- Migration runner, schema tables, endpoints, dashboard rendering, LLM, and embedding behavior: not changed

### Phase 45 - Lightweight SQL Migration Runner v0

- Lightweight SQL migration runner v0: implemented
- `python -m app.migration_runner --status`: implemented
- `python -m app.migration_runner --baseline`: implemented
- Default apply-pending mode over sorted `db/migrations/*.sql`: implemented
- `schema_migrations` table creation and applied migration metadata: implemented
- Checksum and byte-count drift detection: implemented
- No Alembic dependency, API endpoint, dashboard rendering, LLM, or embedding behavior: added

### Phase 46 - Runtime Migration Runner Verification v0

- Runtime migration runner verification v0: implemented
- Initial `--status`: 0 applied, 9 pending migrations
- `--baseline`: recorded the 9 already-applied local migrations without executing SQL
- Final `--status`: 9 applied, 0 pending migrations
- Production migration orchestration, rollback behavior, API endpoints, dashboard rendering, LLM, and embedding behavior: not added

### Phase 47 - Migration Runner Fresh DB Verification v0

- Migration runner fresh DB verification v0: implemented
- Isolated Compose project `noiseproof-agent-fresh`: verified on `POSTGRES_PORT=55433`
- Initial `--status`: 0 applied, 9 pending migrations
- Default runner apply command: applied all 9 migration files through `010_workflow_version_defaults.sql`
- Final `--status`: 9 applied, 0 pending migrations
- Fresh DB schema defaults for `agent_runs.workflow_version` and `workflow_runs.workflow_version`: verified as `phase40-lineage-warning-code-dashboard`
- Isolated test volume: removed with `docker compose -p noiseproof-agent-fresh down -v`
- Production migration orchestration, rollback behavior, hosted deployment safety, API endpoints, dashboard rendering, LLM, and embedding behavior: not added

### Phase 48 - Migration Runner Runbook Cleanup v0

- Migration runner runbook cleanup v0: implemented
- Default migration path in `docs/runbook.md`: use `python -m app.migration_runner`
- Fresh/reset local DB path: `--status`, apply, `--status`
- Existing already-migrated local DB without `schema_migrations`: `--status`, `--baseline`, `--status`
- Manual SQL piping: documented as a legacy/debug fallback only
- Runtime behavior, migration runner code, schema, API endpoints, dashboard rendering, LLM, and embedding behavior: not changed

### Phase 49 - Fresh DB API Smoke Verification v0

- Fresh DB API smoke verification v0: implemented
- Isolated Compose project `noiseproof-agent-api-smoke`: verified on `POSTGRES_PORT=55435`
- Migration runner on fresh DB: 0 applied / 9 pending -> 9 applied / 0 pending
- Temporary API on port `8018`: verified with `GET /health`, `GET /ops/summary`, `POST /documents`, and `GET /documents`
- Document persistence smoke record: `Sample fresh DB smoke document`
- Isolated test volume: removed with `docker compose -p noiseproof-agent-api-smoke down -v`
- Hosted deployment readiness, production migration orchestration, API expansion, dashboard polish, LLM, and embedding behavior: not added

### Phase 50 - Application Evidence Index Refresh v0

- Application evidence index refresh v0: implemented
- `docs/application/portfolio-index.md`: updated with migration runner and fresh DB API smoke artifacts
- `docs/application/braincrew-role-map.md`: updated with runtime proof surfaces and hosted-deployment boundary
- `docs/review/application-ready-review.md`: updated with local migration/API smoke evidence and overclaim boundaries
- Runtime behavior, schema, API endpoints, migration runner code, dashboard rendering, LLM, and embedding behavior: not changed

### Phase 51 - Failure-case Persistence Smoke Verification v0

- Failure-case persistence smoke verification v0: implemented
- Isolated Compose project `noiseproof-agent-failure-smoke`: verified on `POSTGRES_PORT=55436`
- Migration runner on fresh DB: applied 9 migrations and reached 9 applied / 0 pending
- Temporary API on port `8019`: verified with `GET /health`, `GET /ops/summary`, `POST /failure-cases`, and `GET /failure-cases`
- Failure smoke record: `parser_timeout` with `root_cause: simulated parser timeout`
- Ops summary failure count: 0 before create, 1 after create
- Automatic failure detection, hosted deployment readiness, distributed tracing, LLM, and embedding behavior: not added

### Phase 52 - Failure-case Application Evidence Refresh v0

- Failure-case application evidence refresh v0: implemented
- `docs/application/portfolio-index.md`: updated with the failure-case persistence smoke artifact
- `docs/application/braincrew-role-map.md`: updated with failure-ledger proof surface and automatic-detection boundary
- `docs/review/application-ready-review.md`: updated with failure-case persistence smoke evidence
- Runtime behavior, schema, API endpoints, dashboard rendering, automatic failure detection, LLM, and embedding behavior: not changed

Not implemented yet:

- file upload parsing
- robust PDF extraction
- persisted chunks
- autonomous workflow execution endpoints
- embeddings
- retrieval-run-linked Evidence Ledger records
- full distributed tracing or hosted observability

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

The Evidence Ledger is the control surface between retrieval and final answer generation. Phase 6 implements a deterministic preview boundary. Phase 12 persists generated ledger entries so operations views can count unsupported and contradicted claims.

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

The system should generate the ledger before generating a final report. Current persistence is v0 and does not yet link entries to a retrieval run id.

## Noise Gate

The Noise Gate is the reviewer before a final response is allowed through. Phase 7 implements a deterministic preview boundary. Phase 13 persists gate decisions so blocked and revision-needed outputs remain inspectable.

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

The project does not claim model, semantic retrieval, or answer quality success.

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
curl http://localhost:8000/agent-runs
```

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

After Workflow Lineage Warning Code Dashboard Surfacing v0, the next phase should improve lineage inspectability carefully without overstating the runtime:

- update the runtime workflow-version name only after the review boundary
- keep lineage inspectable without adding new storage, LLM calls, dashboard polish, semantic retrieval, or free-form answer generation
- keep deterministic preview behavior before adding LLM calls or embeddings

It should not start with UI polish, LLM prompt tuning, new retrieval behavior, or broad agent abstractions.

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
