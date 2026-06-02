# README Proof-marker Archive

Legacy README proof markers moved out of README during Phase 105.

Phase marker: readme proof-marker archive extraction v0.

This file preserves source-level continuity for older README proof markers after the rendered README was compressed for external-reader scanability.

README detailed implementation-status compression v0: implemented
README next-gate stale-claim refresh v0: implemented
External feedback acceptance template v0: implemented
External feedback acceptance draft CLI v0: implemented
External feedback acceptance draft workflow v0: implemented
External feedback acceptance draft workflow verification v0: implemented
External reviewer upload-manifest request refresh v0: implemented
External reviewer upload-manifest issue-body refresh v0: implemented
External reviewer upload-manifest persistence request refresh v0: implemented
External reviewer upload-manifest persistence issue-body refresh v0: implemented
Persisted uploaded file intake schema review v0: implemented
Uploaded file chunk persistence repository review v0: implemented
Uploaded file chunk persistence endpoint review v0: implemented
Uploaded file chunk persistence endpoint v0: implemented
External reviewer chunk persistence request refresh v0: implemented
External reviewer chunk persistence issue-body refresh v0: implemented
External feedback current-state chunk issue verification v0: implemented
Uploaded file chunk persistence handoff review v0: implemented
Uploaded file chunk persistence handoff endpoint v0: implemented
External reviewer chunk handoff request refresh v0: implemented
External reviewer chunk handoff issue-body refresh v0: implemented
External feedback current-state chunk handoff issue verification v0: implemented
Uploaded file chunk persistence handoff application refresh v0: implemented
Uploaded file retrieval persistence review v0: implemented
Uploaded file retrieval persistence endpoint v0: implemented
Uploaded file retrieval persistence runtime smoke v0: implemented
Uploaded file retrieval persistence application refresh v0: implemented
External reviewer retrieval persistence request refresh v0: implemented
External reviewer retrieval persistence issue-body refresh v0: implemented
External feedback current-state retrieval persistence issue verification v0: implemented

README detailed implementation status archive moved during Phase 103.
This hidden source archive preserves earlier README proof markers while the rendered README stays scanable.

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

- Workflow lineage read model v0: implemented
- `GET /workflow-runs/{id}/lineage`: done
- Derived lineage from existing workflow child records and `stage_input_manifest`: done
- Noise Gate input Evidence Ledger ids are resolved back to linked Evidence Ledger records: done
- Report input Evidence Ledger ids and Noise Gate record ids are resolved back to linked records: done
- Missing manifest references are surfaced as warnings and summary counts: done
- New storage, migrations, direct foreign keys, and join tables: not implemented

### Phase 33 - Workflow Lineage Dashboard Links v0

- Workflow lineage dashboard links v0: implemented
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

- Workflow lineage missing-reference test v0: implemented
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

- Workflow lineage manifest-shape hardening v0: implemented
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

- Structured warning taxonomy v0: implemented
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

- Workflow lineage warning code runbook example v0: implemented
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
- `python -m app.migration_runner - -status`: implemented
- `python -m app.migration_runner - -baseline`: implemented
- Default apply-pending mode over sorted `db/migrations/*.sql`: implemented
- `schema_migrations` table creation and applied migration metadata: implemented
- Checksum and byte-count drift detection: implemented
- No Alembic dependency, API endpoint, dashboard rendering, LLM, or embedding behavior: added

### Phase 46 - Runtime Migration Runner Verification v0

- Runtime migration runner verification v0: implemented
- Initial `- -status`: 0 applied, 9 pending migrations
- `- -baseline`: recorded the 9 already-applied local migrations without executing SQL
- Final `- -status`: 9 applied, 0 pending migrations
- Production migration orchestration, rollback behavior, API endpoints, dashboard rendering, LLM, and embedding behavior: not added

### Phase 47 - Migration Runner Fresh DB Verification v0

- Migration runner fresh DB verification v0: implemented
- Isolated Compose project `noiseproof-agent-fresh`: verified on `POSTGRES_PORT=55433`
- Initial `- -status`: 0 applied, 9 pending migrations
- Default runner apply command: applied all 9 migration files through `010_workflow_version_defaults.sql`
- Final `- -status`: 9 applied, 0 pending migrations
- Fresh DB schema defaults for `agent_runs.workflow_version` and `workflow_runs.workflow_version`: verified as `phase40-lineage-warning-code-dashboard`
- Isolated test volume: removed with `docker compose -p noiseproof-agent-fresh down -v`
- Production migration orchestration, rollback behavior, hosted deployment safety, API endpoints, dashboard rendering, LLM, and embedding behavior: not added

### Phase 48 - Migration Runner Runbook Cleanup v0

- Migration runner runbook cleanup v0: implemented
- Default migration path in `docs/runbook.md`: use `python -m app.migration_runner`
- Fresh/reset local DB path: `- -status`, apply, `- -status`
- Existing already-migrated local DB without `schema_migrations`: `- -status`, `- -baseline`, `- -status`
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

### Phase 53 - Agent-run Failure Linkage Smoke Verification v0

- Agent-run failure linkage smoke verification v0: implemented
- Isolated Compose project `noiseproof-agent-failure-link-smoke`: verified on `POSTGRES_PORT=55437`
- Temporary API on port `8020`: verified with `POST /agent-runs`, `POST /failure-cases`, `GET /failure-cases`, `GET /agent-runs`, and `GET /ops/summary`
- Linked failure smoke record: `linked_parser_timeout` with `agent_run_id` pointing at the created failed agent run
- Ops summary counts: `agent_run_count: 1`, `failure_case_count: 1`
- Automatic failure detection, complete workflow failure causality, hosted deployment evidence, LLM, and embedding behavior: not added

### Phase 54 - Agent-run Failure Linkage Application Refresh v0

- Agent-run failure linkage application refresh v0: implemented
- `docs/application/portfolio-index.md`: updated with the linked failure-case proof artifact
- `docs/application/braincrew-role-map.md`: updated with linked failure-case proof and workflow-causality boundary
- `docs/review/application-ready-review.md`: updated with agent-run failure linkage smoke evidence
- Runtime behavior, schema, API endpoints, dashboard rendering, automatic failure detection, complete workflow failure causality, LLM, and embedding behavior: not changed

### Phase 55 - Workflow Failure Provenance Review v0

- Workflow failure provenance review v0: implemented
- `docs/review/workflow-failure-provenance-review.md`: added
- Current claim: operation-level failure linkage for a manual failure record
- Deferred: `workflow_run_id` on `failure_cases`, automatic failure detection, and workflow-level failure causality
- Runtime behavior, schema, API endpoints, dashboard rendering, automatic failure detection, LLM, and embedding behavior: not changed

### Phase 56 - Workflow Failure Linkage Smoke Verification v0

- Workflow failure linkage smoke verification v0: implemented
- `docs/review/workflow-failure-linkage-smoke-verification.md`: added
- Route-level test fixture verifies a failed downstream stage marks the workflow parent as failed
- Current claim: failed workflow parent state is inspectable in the test fixture
- Deferred: fresh Docker DB proof, automatic failure detection, `workflow_run_id` on `failure_cases`, and complete workflow failure causality
- Runtime behavior, schema, API endpoints, dashboard rendering, LLM, and embedding behavior: not changed

### Phase 57 - Workflow Failure Linkage Application Refresh v0

- Workflow failure linkage application refresh v0: implemented
- `docs/application/portfolio-index.md`: updated with workflow failure linkage smoke artifact
- `docs/application/braincrew-role-map.md`: updated with failed workflow parent proof and boundaries
- `docs/review/application-ready-review.md`: updated with workflow failure linkage smoke evidence
- Runtime behavior, schema, API endpoints, dashboard rendering, automatic failure detection, complete workflow failure causality, LLM, and embedding behavior: not changed

### Phase 58 - Failure-case Workflow Linkage Review v0

- Failure-case workflow linkage review v0: implemented
- `docs/review/failure-case-workflow-linkage-review.md`: added
- Current decision: do not add `workflow_run_id` to `failure_cases` yet
- Reason: there is still no failure-case creation path from a failed workflow parent
- Runtime behavior, schema, API endpoints, dashboard rendering, automatic failure detection, complete workflow failure causality, LLM, and embedding behavior: not changed

### Phase 59 - Failure-case Workflow Linkage Application Refresh v0

- Failure-case workflow linkage application refresh v0: implemented
- `docs/application/portfolio-index.md`: updated with failure-case workflow linkage review artifact
- `docs/application/braincrew-role-map.md`: updated with deferred `failure_cases.workflow_run_id` boundary
- `docs/review/application-ready-review.md`: updated with failure-case workflow linkage boundary
- Runtime behavior, schema, API endpoints, dashboard rendering, automatic failure detection, complete workflow failure causality, LLM, and embedding behavior: not changed

### Phase 60 - Failure-case Creation Path Review v0

- Failure-case creation path review v0: implemented
- `docs/review/failure-case-creation-path-review.md`: added
- Current decision: use a manual failure-case draft path before automation
- Deferred: automatic failure-case creation, `workflow_run_id` on `failure_cases`, schema changes, and root-cause automation
- Runtime behavior, schema, API endpoints, dashboard rendering, automatic failure detection, complete workflow failure causality, LLM, and embedding behavior: not changed

### Phase 61 - Failure-case Draft Preview v0

- Failure-case draft preview v0: implemented
- `POST /failure-cases/draft-preview`: returns a suggested failure-case payload
- `persistence_boundary`: `preview_only_not_persisted`
- `human_confirmation_required`: true
- The preview does not persist a failure case or automatically classify production incidents

### Phase 62 - Failure-case Draft Preview Application Refresh v0

- Failure-case draft preview application refresh v0: implemented
- `docs/application/portfolio-index.md`: updated with the draft-preview endpoint as an application-facing artifact
- `docs/application/braincrew-role-map.md`: updated with the human-confirmed draft payload boundary
- `docs/review/application-ready-review.md`: updated with the preview-only, non-persisting boundary
- Runtime behavior, schema, API endpoints, dashboard rendering, automatic failure detection, complete workflow failure causality, LLM, and embedding behavior: not changed

### Phase 63 - Failure-case Draft Preview Smoke Verification v0

- Failure-case draft preview smoke verification v0: implemented
- `docs/review/failure-case-draft-preview-smoke-verification.md`: added
- Verified test path: `tests/test_routes.py::test_failure_case_draft_preview_suggests_manual_payload_without_persistence`
- Observed: `1 passed, 65 deselected, 1 warning`
- Boundary: route-level smoke only; not fresh Docker DB evidence, automatic failure detection, automatic failure-case persistence, or complete workflow failure causality

### Phase 64 - Failure-case Draft Preview Smoke Application Refresh v0

- Failure-case draft preview smoke application refresh v0: implemented
- `docs/application/portfolio-index.md`: updated with the smoke verification artifact
- `docs/application/braincrew-role-map.md`: updated with route-level smoke and non-DB-proof boundaries
- `docs/review/application-ready-review.md`: updated with draft-preview smoke evidence
- Runtime behavior, schema, API endpoints, dashboard rendering, automatic failure detection, complete workflow failure causality, LLM, and embedding behavior: not changed

### Phase 65 - Failure-case Draft Persistence Handoff Review v0

- Failure-case draft persistence handoff review v0: implemented
- `docs/review/failure-case-draft-persistence-handoff-review.md`: added
- Current decision: prove manual handoff from `POST /failure-cases/draft-preview` to existing `POST /failure-cases` before adding automation
- Deferred: automatic persistence, confirm endpoint, `workflow_run_id` on `failure_cases`, and complete workflow failure causality
- Runtime behavior, schema, API endpoints, dashboard rendering, automatic failure detection, complete workflow failure causality, LLM, and embedding behavior: not changed

### Phase 66 - Failure-case Draft Manual Handoff Smoke Verification v0

- Failure-case draft manual handoff smoke verification v0: implemented
- `docs/review/failure-case-draft-manual-handoff-smoke-verification.md`: added
- Verified test path: `tests/test_routes.py::test_failure_case_draft_can_be_manually_handed_to_failure_case_persistence`
- Observed: `1 passed, 66 deselected, 1 warning`
- Boundary: route-level smoke only; not automatic persistence, a confirm endpoint, fresh Docker DB evidence, or complete workflow failure causality

### Phase 67 - Failure-case Draft Manual Handoff Application Refresh v0

- Failure-case draft manual handoff application refresh v0: implemented
- `docs/application/portfolio-index.md`: updated with the manual handoff smoke artifact
- `docs/application/braincrew-role-map.md`: updated with the explicit human edit from `draft` to `open`
- `docs/review/application-ready-review.md`: updated with the manual handoff smoke boundary
- Runtime behavior, schema, API endpoints, dashboard rendering, automatic failure detection, complete workflow failure causality, LLM, and embedding behavior: not changed

### Phase 68 - Failure-case Draft Fresh-db Handoff Review v0

- Failure-case draft fresh-db handoff review v0: implemented
- `docs/review/failure-case-draft-fresh-db-handoff-review.md`: added
- Current decision: run the manual draft-to-persistence handoff against a fresh migrated Docker DB before stronger application claims
- Deferred: automatic persistence, confirm endpoint, `workflow_run_id` on `failure_cases`, and complete workflow failure causality
- Runtime behavior, schema, API endpoints, dashboard rendering, automatic failure detection, complete workflow failure causality, LLM, and embedding behavior: not changed

### Phase 69 - Failure-case Draft Fresh-db Handoff Smoke Verification v0

- Failure-case draft fresh-db handoff smoke verification v0: implemented
- `docs/review/failure-case-draft-fresh-db-handoff-smoke-verification.md`: added
- Fresh DB project: `noiseproof-agent-draft-handoff-smoke`
- Verified path: migration runner -> FastAPI -> draft preview -> human-confirmed `POST /failure-cases` -> `GET /ops/summary`
- Observed: `preview_only_not_persisted`, `draft_fix_status: draft`, `persisted_fix_status: open`, `ops_failure_case_count: 1`
- Boundary: local fresh migrated Docker DB evidence only; not hosted deployment evidence, automatic persistence, a confirm endpoint, or complete workflow failure causality

### Phase 70 - Failure-case Draft Fresh-db Handoff Application Refresh v0

- Failure-case draft fresh-db handoff application refresh v0: implemented
- `docs/application/portfolio-index.md`: updated with the fresh DB handoff smoke artifact
- `docs/application/braincrew-role-map.md`: updated with local runtime proof and hosted-deployment boundary
- `docs/review/application-ready-review.md`: updated with the fresh DB handoff smoke boundary
- Runtime behavior, schema, API endpoints, dashboard rendering, automatic failure detection, complete workflow failure causality, LLM, and embedding behavior: not changed

### Phase 71 - Failure-case Workflow Failure-to-draft Review v0

- Failure-case workflow failure-to-draft review v0: implemented
- `docs/review/failure-case-workflow-failure-to-draft-review.md`: added
- Current decision: prove failed workflow parent -> draft-preview input before any automatic failure-case creation
- Deferred: automatic failure-case creation, automatic persistence, confirm endpoint, `workflow_run_id` on `failure_cases`, and complete workflow failure causality
- Runtime behavior, schema, API endpoints, dashboard rendering, automatic failure detection, complete workflow failure causality, LLM, and embedding behavior: not changed

### Phase 72 - Workflow Failure-to-draft Smoke Verification v0

- Workflow failure-to-draft smoke verification v0: implemented
- `docs/review/workflow-failure-to-draft-smoke-verification.md`: added
- Route-level smoke: failed `POST /workflow-runs/execute-preview` parent -> `POST /failure-cases/draft-preview`
- Observed: `workflow_run.status: failed`, `persistence_boundary: preview_only_not_persisted`, `human_confirmation_required: true`
- Confirmed: failure-case draft preview does not persist a failure case; `failure_cases` remain unchanged
- Boundary: not automatic failure-case creation, not automatic persistence, not fresh Docker DB evidence, and not complete workflow failure causality

### Phase 73 - Workflow Failure-to-draft Application Refresh v0

- Workflow failure-to-draft application refresh v0: implemented
- `docs/application/portfolio-index.md`: updated with workflow failure-to-draft smoke artifact
- `docs/application/braincrew-role-map.md`: updated with route-level smoke and automatic-creation boundary
- `docs/review/application-ready-review.md`: updated with workflow failure-to-draft smoke boundary
- Runtime behavior, schema, API endpoints, dashboard rendering, automatic failure-case creation, automatic persistence, complete workflow failure causality, LLM, and embedding behavior: not changed

### Phase 74 - Failure-case Workflow Creation Path Decision v0

- Failure-case workflow creation path decision v0: implemented
- `docs/review/failure-case-workflow-creation-path-decision.md`: added
- Decision: automatic failure-case creation remains deferred
- Selected direction: human-confirmed persistence path before durable failure records
- Boundary: `workflow_run_id` on `failure_cases` requires a schema gate before implementation

### Phase 75 - Failure-case Workflow Parent Linkage Schema Review v0

- Failure-case workflow parent linkage schema review v0: implemented
- `docs/review/failure-case-workflow-parent-linkage-schema-review.md`: added
- Selected schema direction: nullable `workflow_run_id` on `failure_cases`
- Intended FK: `REFERENCES workflow_runs(id) ON DELETE SET NULL`
- Boundary: no migration is added in this review gate; automatic failure-case creation remains deferred

### Phase 76 - Failure-case Workflow Parent Linkage Schema v0

- Failure-case workflow parent linkage schema v0: implemented
- `failure_cases.workflow_run_id`: added as nullable `UUID REFERENCES workflow_runs(id) ON DELETE SET NULL`
- `db/migrations/011_failure_case_workflow_run_id.sql`: added
- `FailureCaseCreate` / `FailureCaseOut`: now include optional `workflow_run_id`
- `POST /failure-cases`: can manually persist workflow parent linkage
- `POST /failure-cases/draft-preview`: now carries `workflow_run_id` into the suggested draft payload
- Boundary: automatic failure-case creation and complete workflow failure causality remain unclaimed

### Phase 77 - Failure-case Workflow Parent Linkage Smoke Verification v0

- Failure-case workflow parent linkage smoke verification v0: implemented
- `docs/review/failure-case-workflow-parent-linkage-smoke-verification.md`: added
- Route-level smoke: `POST /workflow-runs` -> `POST /failure-cases` -> `GET /failure-cases`
- Observed: workflow parent link is retained in failure-case create/list responses
- Observed: draft-preview carries workflow_run_id into the suggested draft payload
- Boundary: not automatic failure-case creation, not fresh Docker DB evidence, and not complete workflow failure causality

### Phase 78 - Failure-case Workflow Parent Linkage Fresh-db Verification v0

- Failure-case workflow parent linkage fresh-db verification v0: implemented
- `docs/review/failure-case-workflow-parent-linkage-fresh-db-verification.md`: added
- Fresh DB project: `noiseproof-agent-workflow-link-smoke`
- Verified migration runner applied `011_failure_case_workflow_run_id.sql`
- Verified real FastAPI/PostgreSQL path: `POST /workflow-runs` -> `POST /failure-cases` -> `GET /failure-cases` -> `GET /ops/summary`
- Observed: persisted and listed `workflow_run_id` match the workflow parent id; `ops_failure_case_count: 1`
- Boundary: local fresh migrated Docker DB evidence only; not hosted deployment evidence, not automatic failure-case creation, and not complete workflow failure causality

### Phase 79 - Failure-case Workflow Parent Linkage Application Refresh v0

- Failure-case workflow parent linkage application refresh v0: implemented
- `docs/application/portfolio-index.md`: updated with the fresh DB workflow parent linkage artifact
- `docs/application/braincrew-role-map.md`: updated with the workflow parent linkage fresh DB proof and hosted-deployment boundary
- `docs/review/application-ready-review.md`: updated with the failure-case workflow parent linkage fresh DB boundary
- Runtime behavior, schema, API endpoints, dashboard rendering, automatic failure-case creation, automatic persistence, complete workflow failure causality, LLM, and embedding behavior: not changed

### Phase 80 - Failure-case Workflow Parent Linkage Dashboard Review v0

- Failure-case workflow parent linkage dashboard review v0: implemented
- `docs/review/failure-case-workflow-parent-linkage-dashboard-review.md`: added
- Current decision: surface manual `failure_cases.workflow_run_id` in the Failure Cases table as a link to `/workflow-runs/{id}` in the next gate
- Boundary: this review does not add dashboard rendering, automatic failure-case creation, automatic failure detection, or complete workflow failure causality

### Phase 81 - Failure-case Workflow Parent Linkage Dashboard Surfacing v0

- Failure-case workflow parent linkage dashboard surfacing v0: implemented
- `GET /ops/dashboard`: Failure Cases table now shows a Workflow Parent column
- Manual `failure_cases.workflow_run_id` values link to `/workflow-runs/{id}`
- Dashboard copy labels the link as manual workflow parent link provenance, not automatic failure-case creation
- Boundary: no schema, migration, new endpoint, automatic failure-case creation, automatic detection, complete workflow failure causality, LLM, or embedding behavior changed

### Phase 82 - Failure-case Workflow Parent Linkage Dashboard Application Refresh v0

- Failure-case workflow parent linkage dashboard application refresh v0: implemented
- `docs/application/portfolio-index.md`: updated with dashboard Workflow Parent column behavior
- `docs/application/braincrew-role-map.md`: updated with dashboard manual workflow parent link boundary
- `docs/review/application-ready-review.md`: updated with manual provenance-only dashboard link boundary
- Runtime behavior, schema, API endpoints, automatic failure-case creation, automatic detection, complete workflow failure causality, LLM, and embedding behavior: not changed

### Phase 83 - Failure-case Workflow Parent Linkage Fresh-db Dashboard Smoke Review v0

- Failure-case workflow parent linkage fresh-db dashboard smoke review v0: implemented
- `docs/review/failure-case-workflow-parent-linkage-fresh-db-dashboard-smoke-review.md`: added
- Current decision: run a fresh migrated Docker DB smoke for `GET /ops/dashboard` showing the manual Workflow Parent link
- Boundary: this review does not run the smoke, claim hosted deployment evidence, claim automatic failure-case creation, or claim complete workflow failure causality

### Phase 84 - Failure-case Workflow Parent Linkage Fresh-db Dashboard Smoke Verification v0

- Failure-case workflow parent linkage fresh-db dashboard smoke verification v0: implemented
- `docs/review/failure-case-workflow-parent-linkage-fresh-db-dashboard-smoke-verification.md`: added
- Runtime proof: fresh Docker DB, migrations through `011_failure_case_workflow_run_id.sql`, FastAPI on port 8025, manual workflow-linked failure case, and `GET /ops/dashboard` HTML containing the Workflow Parent link
- Boundary: local smoke only; not hosted deployment evidence, not automatic failure-case creation, and not complete workflow failure causality

### Phase 85 - Failure-case Workflow Parent Linkage Fresh-db Dashboard Smoke Application Refresh v0

- Failure-case workflow parent linkage fresh-db dashboard smoke application refresh v0: implemented
- `docs/application/portfolio-index.md`: updated with the fresh DB dashboard Workflow Parent proof
- `docs/application/braincrew-role-map.md`: updated with the fresh DB dashboard Workflow Parent proof and boundaries
- `docs/review/application-ready-review.md`: updated with the application-ready claim boundary
- Boundary: application-facing documentation only; no runtime behavior, schema, dashboard rendering, automatic failure-case creation, or complete workflow failure causality changed

### Phase 86 - Failure-case Workflow Parent Linkage Proof Consolidation Review v0

- Failure-case workflow parent linkage proof consolidation review v0: implemented
- `docs/review/failure-case-workflow-parent-linkage-proof-consolidation-review.md`: added
- Current decision: create a compact proof index next because the workflow-parent/failure-case proof chain is now too distributed for fast review
- Boundary: review-only; no proof index, runtime behavior, schema, dashboard rendering, hosted deployment evidence, automatic failure-case creation, or complete workflow failure causality added

### Phase 87 - Failure-case Workflow Parent Linkage Proof Index v0

- Failure-case workflow parent linkage proof index v0: implemented
- `docs/review/failure-case-workflow-parent-linkage-proof-index.md`: added
- Reader path: schema boundary -> manual persistence -> fresh DB persistence -> dashboard surfacing -> fresh DB dashboard proof -> application-facing boundary
- Boundary: index-only; no runtime behavior, schema, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure-case creation, or complete workflow failure causality added

### Phase 88 - Failure-case Workflow Parent Linkage Proof Index Application Refresh v0

- Failure-case workflow parent linkage proof index application refresh v0: implemented
- `docs/application/portfolio-index.md`: updated with proof index reader path
- `docs/application/braincrew-role-map.md`: updated with proof index reader path
- `docs/review/application-ready-review.md`: updated with Allowed claim / Forbidden claim language for the proof index
- Boundary: application-facing documentation only; no runtime behavior, schema, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure-case creation, or complete workflow failure causality added

### Phase 89 - Failure-case Workflow Parent Linkage Proof Chain Stale-claim Review v0

- Failure-case workflow parent linkage proof chain stale-claim review v0: implemented
- `docs/review/failure-case-workflow-parent-linkage-stale-claim-review.md`: added
- Current decision: clean up stale current-facing language that still says manual workflow parent linkage is deferred
- Boundary: review-only; no runtime behavior, schema, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure-case creation, or complete workflow failure causality added

### Phase 90 - Failure-case Workflow Parent Linkage Stale-claim Cleanup v0

- Failure-case workflow parent linkage stale-claim cleanup v0: implemented
- `docs/review/failure-case-workflow-parent-linkage-stale-claim-cleanup.md`: added
- `docs/application/braincrew-role-map.md`: current-facing wording now says manual workflow parent linkage exists
- `docs/review/application-ready-review.md`: current-facing checklist boundary now treats the older linkage review as historical context
- Boundary: application-facing cleanup only; no runtime behavior, schema, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure-case creation, or complete workflow failure causality added

### Phase 91 - External-reader Proof Path Review v0

- External-reader proof path review v0: implemented
- `docs/review/external-reader-proof-path-review.md`: added
- Current decision: create a compact external-reader proof path next
- Boundary: review-only; no runtime behavior, schema, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure-case creation, or complete workflow failure causality added

### Phase 92 - External-reader Proof Path Index v0

- External-reader proof path index v0: implemented
- `docs/review/external-reader-proof-path.md`: added
- Reader path: README -> portfolio index -> failure-case workflow parent proof index -> application-ready review -> Braincrew role map
- Boundary: index-only; no runtime behavior, schema, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure-case creation, or complete workflow failure causality added

### Phase 93 - Portfolio External Proof Path Refresh v0

- Portfolio external proof path refresh v0: implemented
- `docs/application/portfolio-index.md`: updated with `docs/review/external-reader-proof-path.md` as the 5-minute path
- Boundary: application-facing documentation only; no runtime behavior, schema, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure-case creation, or complete workflow failure causality added

### Phase 94 - External-reader Proof Path Application Refresh Review v0

- External-reader proof path application refresh review v0: implemented
- `docs/review/external-reader-proof-path-application-refresh-review.md`: added
- Current decision: surface `docs/review/external-reader-proof-path.md` in Braincrew role map and application-ready review next
- Boundary: review-only; no runtime behavior, schema, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure-case creation, or complete workflow failure causality added

### Phase 95 - External-reader Proof Path Application Refresh v0

- External-reader proof path application refresh v0: implemented
- `docs/application/braincrew-role-map.md`: updated with `docs/review/external-reader-proof-path.md`
- `docs/review/application-ready-review.md`: updated with the 5-minute path and boundaries
- Boundary: application-facing documentation only; no runtime behavior, schema, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure-case creation, or complete workflow failure causality added

### Phase 96 - README External Proof Path Refresh Review v0

- README external proof path refresh review v0: implemented
- `docs/review/readme-external-proof-path-refresh-review.md`: added
- Current decision: add a short README fast-path block next
- Boundary: review-only; no runtime behavior, schema, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure-case creation, or complete workflow failure causality added

### Phase 97 - README External Proof Path Refresh v0

- README external proof path refresh v0: implemented
- README now links `docs/review/external-reader-proof-path.md` near the top as the 5-minute repository-native path
- Boundary: README documentation only; no runtime behavior, schema, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure-case creation, or complete workflow failure causality added

### Phase 98 - README Phase-history Compression Review v0

- README phase-history compression review v0: implemented
- `docs/review/readme-phase-history-compression-review.md`: added
- Current decision: compress the long README chronological phase paragraph next
- Boundary: review-only; no runtime behavior, schema, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure-case creation, or complete workflow failure causality added

### Phase 99 - README Phase-history Compression v0

- README phase-history compression v0: implemented
- `README.md` now replaces the long chronological wall with current implemented capability groups
- Detailed phase history remains in `docs/GOAL.md`, `docs/application/portfolio-index.md`, and phase-specific `docs/review/*` artifacts
- Boundary: README documentation only; no runtime behavior, schema, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure-case creation, or complete workflow failure causality added

### Phase 100 - README Implementation-status Compression Review v0

- README implementation-status compression review v0: implemented as `docs/review/readme-implementation-status-compression-review.md`
- Current decision: compress the top README implementation status list next
- Boundary: review-only; no runtime behavior, schema, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure-case creation, or complete workflow failure causality added

### Phase 101 - README Implementation-status Compression v0

- README implementation-status compression v0: implemented
- The top `Implementation status:` wall now summarizes current status groups and explicit non-claims
- Detailed implementation history remains in the lower `## Implementation Status` section, `docs/GOAL.md`, and phase-specific `docs/review/*` artifacts
- Boundary: README documentation only; no runtime behavior, schema, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure-case creation, or complete workflow failure causality added

### Phase 102 - README Detailed Implementation-status Compression Review v0

- README detailed implementation-status compression review v0: implemented as `docs/review/readme-detailed-implementation-status-compression-review.md`
- Current decision: compress the lower README implementation status section next
- Boundary: review-only; no runtime behavior, schema, dashboard rendering, smoke execution, hosted deployment evidence, automatic failure-case creation, or complete workflow failure causality added

### Phase 190 - Uploaded File Chunk Persistence Handoff Runtime Smoke v0

- Uploaded file chunk persistence handoff runtime smoke v0: implemented
- `docs/review/uploaded-file-chunk-persistence-handoff-runtime-smoke.md`: added
- Boundary: local runtime smoke evidence only; no hosted deployment evidence, external reviewer feedback, retrieval persistence, embeddings, raw uploaded byte storage, or product-complete claim added

### Phase 191 - External Reviewer Chunk Handoff Request Refresh v0

- External reviewer chunk handoff request refresh v0: implemented
- `docs/review/external-reviewer-chunk-handoff-request-refresh.md`: added
- Boundary: request infrastructure only; no runtime behavior, hosted deployment evidence, external reviewer feedback, or product-complete claim added

### Phase 192 - External Reviewer Chunk Handoff Issue-body Refresh v0

- External reviewer chunk handoff issue-body refresh v0: implemented
- `docs/review/external-review-issue-body-chunk-handoff-refresh.md`: added
- Boundary: owner-authored issue edit only; no external reviewer feedback, hosted deployment evidence, or product-complete claim added

### Phase 193 - External Feedback Current-state Chunk Handoff Issue Verification v0

- External feedback current-state chunk handoff issue verification v0: implemented
- `docs/review/external-feedback-current-state-chunk-handoff-issue-verification.md`: added
- Boundary: current-state screen only; no external reviewer feedback, hosted deployment evidence, customer validation, Braincrew acceptance, or product-complete claim added

### Phase 194 - Uploaded File Chunk Persistence Handoff Application Refresh v0

- Uploaded file chunk persistence handoff application refresh v0: implemented
- `docs/review/uploaded-file-chunk-persistence-handoff-application-refresh.md`: added
- `docs/application/braincrew-role-map.md`: updated with the handoff runtime proof link
- `docs/review/application-ready-review.md`: updated with the explicit upload-to-chunks handoff boundary
- Boundary: documentation-only application packaging; no runtime behavior, hosted deployment evidence, external reviewer feedback, raw uploaded byte storage, retrieval persistence, or product-complete claim added

### Phase 195 - Uploaded File Retrieval Persistence Review v0

- Uploaded file retrieval persistence review v0: implemented
- `docs/review/uploaded-file-retrieval-persistence-review.md`: added
- Selected future endpoint: `POST /documents/{document_id}/retrieval-runs`
- Selected boundary: reuse existing `document_chunks`, existing `retrieval_runs`, and `metadata_json.candidate_chunk_ids` before adding any retrieval-candidates table
- Boundary: review-only; no runtime behavior, schema, endpoint code, embeddings, semantic retrieval, Evidence Ledger generation, financial advice behavior, hosted deployment evidence, external reviewer feedback, or product-complete claim added

### Phase 196 - Uploaded File Retrieval Persistence Endpoint v0

- Uploaded file retrieval persistence endpoint v0: implemented
- `docs/review/uploaded-file-retrieval-persistence-endpoint.md`: added
- `POST /documents/{document_id}/retrieval-runs`: added as document-scoped retrieval persistence endpoint
- `metadata_json.candidate_chunk_ids`: stores selected chunk ids in the existing `retrieval_runs` row
- Boundary: route-level behavior only; no schema, migration, retrieval-candidates table, embeddings, semantic retrieval, Evidence Ledger generation, financial advice behavior, hosted deployment evidence, external reviewer feedback, or product-complete claim added

### Phase 197 - Uploaded File Retrieval Persistence Runtime Smoke v0

- Uploaded file retrieval persistence runtime smoke v0: implemented
- `docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md`: added
- Local Docker DB observed healthy with `Applied migrations: 12` and `Pending migrations: 0`
- Live HTTP observed `POST /documents/upload-chunks -> 201`
- Live HTTP observed `POST /documents/{document_id}/retrieval-runs -> 201`
- Live HTTP observed `GET /retrieval-runs -> 200` with matching `metadata_json.candidate_chunk_ids`
- Boundary: local runtime evidence only; no hosted deployment evidence, external reviewer feedback, customer validation, Braincrew acceptance, Evidence Ledger generation, semantic retrieval, embeddings, financial advice behavior, or product-complete claim added

### Phase 198 - Uploaded File Retrieval Persistence Application Refresh v0

- Uploaded file retrieval persistence application refresh v0: implemented
- `docs/review/uploaded-file-retrieval-persistence-application-refresh.md`: added
- `docs/review/uploaded-file-retrieval-persistence-runtime-smoke.md`: surfaced as the primary runtime proof
- `docs/application/portfolio-index.md`: updated with the application refresh link
- `docs/application/braincrew-role-map.md`: updated with the retrieval persistence runtime proof link
- `docs/review/application-ready-review.md`: updated with the explicit retrieval persistence boundary
- Boundary: documentation-only application packaging; no runtime behavior, hosted deployment evidence, external reviewer feedback, Evidence Ledger generation, semantic retrieval, embeddings, financial advice behavior, or product-complete claim added

### Phase 202 - Retrieval-run-linked Evidence Ledger Endpoint v0

- Retrieval-run-linked Evidence Ledger endpoint v0: implemented
- `docs/review/retrieval-run-linked-evidence-ledger-endpoint.md`: added
- `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger`: added as persisted retrieval-to-evidence handoff endpoint
- `db/migrations/014_evidence_ledger_retrieval_run_id.sql`: added to link Evidence Ledger rows back to persisted retrieval runs
- Boundary: deterministic lexical retrieval-run handoff only; no embeddings, semantic retrieval, LLM judgment, Noise Gate generation, report generation, hosted deployment evidence, external reviewer feedback, financial advice behavior, or product-complete claim added

### Phase 203 - Retrieval-run-linked Evidence Ledger Runtime Smoke v0

- Retrieval-run-linked Evidence Ledger runtime smoke v0: implemented
- `docs/review/retrieval-run-linked-evidence-ledger-runtime-smoke.md`: added
- Local Docker DB observed `Applied migrations: 13` and `Pending migrations: 0`
- Live HTTP observed `POST /retrieval-runs/{retrieval_run_id}/evidence-ledger -> 201`
- Live HTTP observed `GET /evidence-ledgers -> 200` with matching `retrieval_run_id`
- Boundary: local runtime evidence only; no hosted deployment evidence, external reviewer feedback, customer validation, Braincrew acceptance, embeddings, semantic retrieval, LLM judgment, Noise Gate generation, report generation, financial advice behavior, or product-complete claim added
