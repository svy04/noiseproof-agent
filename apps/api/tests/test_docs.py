from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]


def test_phase10_evaluation_and_application_artifacts_exist():
    required_files = [
        "docs/evaluation/eval-plan.md",
        "docs/evaluation/retrieval-eval-report.md",
        "docs/evaluation/failure-cases.md",
        "docs/application/braincrew-role-map.md",
        "docs/application/cover-message.md",
        "docs/application/portfolio-index.md",
        "docs/review/application-ready-review.md",
        "docs/review/agent-run-linkage-review.md",
        "docs/review/evidence-to-gate-report-cross-links-review.md",
        "docs/review/direct-evidence-gate-report-cross-link-review.md",
        "docs/review/direct-cross-stage-link-schema-review.md",
        "docs/review/single-workflow-parent-review.md",
        "docs/review/workflow-run-child-link-review.md",
        "docs/review/workflow-lineage-missing-reference-review.md",
        "docs/review/workflow-lineage-boundary-hardening-review.md",
        "docs/review/workflow-lineage-warning-taxonomy-review.md",
        "docs/review/workflow-lineage-warning-code-documentation-review.md",
        "docs/review/workflow-lineage-warning-code-dashboard-review.md",
        "docs/review/workflow-version-naming-review.md",
        "docs/review/workflow-version-naming-consistency-review.md",
        "docs/review/runtime-db-schema-default-verification.md",
        "docs/review/migration-runner-review.md",
        "docs/review/runtime-migration-runner-verification.md",
        "docs/review/migration-runner-fresh-db-verification.md",
        "docs/review/fresh-db-api-smoke-verification.md",
        "docs/review/failure-case-persistence-smoke-verification.md",
        "docs/review/agent-run-failure-linkage-smoke-verification.md",
        "docs/review/workflow-failure-provenance-review.md",
        "docs/review/workflow-failure-linkage-smoke-verification.md",
        "docs/review/failure-case-workflow-linkage-review.md",
        "docs/review/failure-case-creation-path-review.md",
    ]

    for file_path in required_files:
        assert (REPO_ROOT / file_path).is_file(), f"Missing {file_path}"


def test_braincrew_role_map_keeps_fde_first_and_bounds_claims():
    content = (REPO_ROOT / "docs/application/braincrew-role-map.md").read_text(encoding="utf-8")

    assert "Forward Deployed Engineer" in content
    assert "Product Engineer" in content
    assert "FDE-first" in content
    assert "not a trading bot" in content
    assert "Unproven" in content


def test_evaluation_docs_include_examples_and_unproven_boundaries():
    eval_plan = (REPO_ROOT / "docs/evaluation/eval-plan.md").read_text(encoding="utf-8")
    retrieval_report = (REPO_ROOT / "docs/evaluation/retrieval-eval-report.md").read_text(encoding="utf-8")
    failure_cases = (REPO_ROOT / "docs/evaluation/failure-cases.md").read_text(encoding="utf-8")

    assert "sample dataset" in eval_plan
    assert "unsupported claim" in eval_plan
    assert "Not yet measured" in retrieval_report
    assert "lexical retrieval" in retrieval_report
    assert "runtime_verification" in failure_cases
    assert "No LLM" in failure_cases


def test_application_ready_review_marks_partial_boundaries():
    content = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(encoding="utf-8")

    assert "application-ready review" in content
    assert "Partial" in content
    assert "Not product-complete" in content
    assert "every agent run leaves a trace" in content


def test_agent_run_linkage_review_keeps_fk_boundary_explicit():
    content = (REPO_ROOT / "docs/review/agent-run-linkage-review.md").read_text(encoding="utf-8")

    assert "agent_run_id" in content
    assert "workflow_trace_id" in content
    assert "Do not add the foreign key in this review gate" in content
    assert "create the agent run first" in content
    assert "false sense of provenance" in content


def test_evidence_to_gate_report_cross_links_review_keeps_boundary_explicit():
    content = (REPO_ROOT / "docs/review/evidence-to-gate-report-cross-links-review.md").read_text(encoding="utf-8")

    assert "Evidence-to-gate/report local cross-links review" in content
    assert "review-only gate" in content
    assert "Do not add cross-link columns in this review gate" in content
    assert "workflow_trace_id" in content
    assert "agent_run_id" in content
    assert "false sense of causal lineage" in content
    assert "single workflow parent" in content


def test_single_workflow_parent_review_keeps_orchestration_boundary_explicit():
    content = (REPO_ROOT / "docs/review/single-workflow-parent-review.md").read_text(encoding="utf-8")

    assert "Single workflow parent review" in content
    assert "review-only gate" in content
    assert "Do not reuse agent_runs as the workflow parent" in content
    assert "workflow_runs" in content
    assert "one endpoint invocation" in content
    assert "evidence -> gate -> report" in content
    assert "false sense of orchestration" in content


def test_workflow_runs_schema_exists_with_nullable_child_links():
    init_schema = (REPO_ROOT / "db/init/001_schema.sql").read_text(encoding="utf-8")
    migration = (REPO_ROOT / "db/migrations/007_workflow_runs.sql").read_text(encoding="utf-8")
    child_link_migration = (REPO_ROOT / "db/migrations/008_child_workflow_run_ids.sql").read_text(
        encoding="utf-8"
    )
    manifest_migration = (REPO_ROOT / "db/migrations/009_stage_input_manifest.sql").read_text(
        encoding="utf-8"
    )
    combined = init_schema + "\n" + migration + "\n" + child_link_migration + "\n" + manifest_migration

    assert "CREATE TABLE IF NOT EXISTS workflow_runs" in combined
    assert "question TEXT NOT NULL" in combined
    assert "workflow_version TEXT NOT NULL" in combined
    assert "status TEXT NOT NULL" in combined
    assert "trace_json JSONB NOT NULL DEFAULT '{}'::jsonb" in combined
    assert "status IN (" in combined
    assert "'created'" in combined
    assert "'running'" in combined
    assert "'completed'" in combined
    assert "'failed'" in combined
    assert "'blocked'" in combined
    assert "'needs_revision'" in combined
    for table_name in [
        "retrieval_runs",
        "evidence_ledger_entries",
        "noise_gate_records",
        "report_records",
    ]:
        assert f"ALTER TABLE {table_name}" in child_link_migration
    assert combined.count("workflow_run_id UUID REFERENCES workflow_runs(id) ON DELETE SET NULL") >= 4
    assert combined.count("stage_input_manifest JSONB NOT NULL DEFAULT '{}'::jsonb") >= 4


def test_workflow_run_child_link_review_defers_schema_until_orchestration_boundary():
    content = (REPO_ROOT / "docs/review/workflow-run-child-link-review.md").read_text(encoding="utf-8")

    assert "WorkflowRun child-link review" in content
    assert "review-only gate" in content
    assert "Do not add child workflow_run_id columns in this review gate" in content
    assert "workflow_runs" in content
    assert "agent_run_id" in content
    assert "evidence -> gate -> report" in content
    assert "false sense of workflow causality" in content


def test_direct_evidence_gate_report_cross_link_review_requires_runtime_order_before_fk_claims():
    content = (REPO_ROOT / "docs/review/direct-evidence-gate-report-cross-link-review.md").read_text(
        encoding="utf-8"
    )

    assert "Direct evidence-to-gate/report cross-link review" in content
    assert "review-only gate" in content
    assert "Do not add direct evidence -> gate -> report foreign-key links in this review gate" in content
    assert "GET /workflow-runs/{id}" in content
    assert "workflow_run_id" in content
    assert "evidence -> gate -> report" in content
    assert "execution order" in content
    assert "false sense of stage-level causality" in content
    assert "Follow-up status after Phase 31" in content
    assert "stage_input_manifest" in content


def test_phase31_goal_and_application_review_document_manifest_boundary():
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    review = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(encoding="utf-8")

    assert "Phase 31 - Workflow Stage Input Manifest v0" in goal
    assert "stage_input_manifest JSONB on noise_gate_records" in goal
    assert "stage_input_manifest JSONB on report_records" in goal
    assert "Direct cross-stage link schema review v0" in goal
    assert "Workflow Stage Input Manifest v0" in review
    assert "JSON manifest only, not direct FK or join-table lineage" in review


def test_direct_cross_stage_link_schema_review_defers_schema_and_points_to_read_model():
    content = (REPO_ROOT / "docs/review/direct-cross-stage-link-schema-review.md").read_text(
        encoding="utf-8"
    )

    assert "Direct cross-stage link schema review" in content
    assert "review-only gate" in content
    assert "Phase 31" in content
    assert "stage_input_manifest" in content
    assert "Do not add direct evidence -> gate -> report foreign-key links yet" in content
    assert "Do not add join tables yet" in content
    assert "JSON manifest is enough for local deterministic stage input provenance" in content
    assert "not enough for strict relational lineage" in content
    assert "Workflow lineage read model v0" in content


def test_phase32_docs_mark_lineage_read_model_without_storage_claims():
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    architecture = (REPO_ROOT / "docs/architecture.md").read_text(encoding="utf-8")

    assert "Phase 32 - Workflow Lineage Read Model v0" in goal
    assert "GET /workflow-runs/{id}/lineage" in goal
    assert "derived read model over existing workflow child records and stage_input_manifest values" in goal
    assert "does not add migrations, columns, join tables" in goal
    assert "Workflow lineage read model v0: implemented" in readme
    assert "GET /workflow-runs/{id}/lineage" in architecture


def test_phase33_docs_mark_dashboard_lineage_links_without_ui_polish_claims():
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")

    assert "Phase 33 - Workflow Lineage Dashboard Links v0" in goal
    assert "Workflow lineage dashboard links v0: implemented" in readme
    assert "detail and lineage links from workflow rows" in goal
    assert "no dashboard polish" in goal
    assert "curl http://localhost:8000/ops/dashboard" in runbook
    assert "workflow lineage links" in runbook


def test_workflow_lineage_missing_reference_review_keeps_runtime_scope_bounded():
    content = (REPO_ROOT / "docs/review/workflow-lineage-missing-reference-review.md").read_text(
        encoding="utf-8"
    )
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Workflow lineage missing-reference review" in content
    assert "review-only gate" in content
    assert "GET /workflow-runs/{id}/lineage" in content
    assert "missing_reference_count" in content
    assert "One or more stage_input_manifest references could not be resolved" in content
    assert "no migrations" in content
    assert "no columns" in content
    assert "no join tables" in content
    assert "do not add runtime mutation path" in content
    assert "targeted missing-reference test" in content
    assert "Phase 33.5 - Workflow Lineage Missing-reference Review v0" in goal
    assert "docs/review/workflow-lineage-missing-reference-review.md" in goal
    assert "Workflow lineage missing-reference test v0" in goal


def test_phase34_docs_mark_missing_reference_test_without_schema_expansion():
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")

    assert "Phase 34 - Workflow Lineage Missing-reference Test v0" in goal
    assert "Workflow lineage missing-reference test v0: implemented" in readme
    assert "missing_reference_count > 0" in goal
    assert "no malformed-manifest mutation endpoint" in goal
    assert "no migrations, columns, or join tables" in goal
    assert "missing-reference fixture" in runbook


def test_workflow_lineage_boundary_hardening_review_identifies_manifest_shape_risk():
    content = (REPO_ROOT / "docs/review/workflow-lineage-boundary-hardening-review.md").read_text(
        encoding="utf-8"
    )
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Workflow lineage boundary hardening review" in content
    assert "review-only gate" in content
    assert "input_evidence_ledger_entry_ids" in content
    assert "non-list manifest values" in content
    assert "string values must not be treated as iterable evidence id lists" in content
    assert "duplicate references" in content
    assert "cross-workflow references" in content
    assert "no migrations" in content
    assert "no columns" in content
    assert "no join tables" in content
    assert "Workflow lineage manifest-shape hardening v0" in content
    assert "Phase 34.5 - Workflow Lineage Boundary Hardening Review v0" in goal
    assert "Workflow lineage manifest-shape hardening v0" in goal


def test_phase35_docs_mark_manifest_shape_hardening_without_schema_expansion():
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")

    assert "Phase 35 - Workflow Lineage Manifest-shape Hardening v0" in goal
    assert "Workflow lineage manifest-shape hardening v0: implemented" in readme
    assert "input_evidence_ledger_entry_ids must be a list" in goal
    assert "cross-workflow references remain local missing references" in goal
    assert "duplicate manifest references preserve order and count" in goal
    assert "no migrations, columns, or join tables" in goal
    assert "phase35-workflow-lineage-manifest-shape-hardening" in readme


def test_workflow_lineage_warning_taxonomy_review_keeps_warning_scope_bounded():
    content = (REPO_ROOT / "docs/review/workflow-lineage-warning-taxonomy-review.md").read_text(
        encoding="utf-8"
    )
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Workflow lineage warning taxonomy review" in content
    assert "review-only gate" in content
    assert "derived_read_model_boundary" in content
    assert "missing_manifest_reference" in content
    assert "invalid_manifest_shape" in content
    assert "local_workflow_scope" in content
    assert "warning strings remain human-readable" in content
    assert "Do not add warning code fields in this review gate" in content
    assert "no migrations" in content
    assert "no columns" in content
    assert "no join tables" in content
    assert "structured warning taxonomy v0" in content
    assert "Workflow lineage warning taxonomy review v0" in goal
    assert "structured warning taxonomy v0" in goal


def test_phase36_docs_mark_structured_warning_taxonomy_without_storage_expansion():
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    architecture = (REPO_ROOT / "docs/architecture.md").read_text(encoding="utf-8")

    assert "Phase 36 - Structured Warning Taxonomy v0" in goal
    assert "warning_codes" in goal
    assert "derived_read_model_boundary" in goal
    assert "missing_manifest_reference" in goal
    assert "invalid_manifest_shape" in goal
    assert "local_workflow_scope" in goal
    assert "no migrations, columns, or join tables" in goal
    assert "Structured warning taxonomy v0: implemented" in readme
    assert "warning_codes" in architecture


def test_workflow_lineage_warning_code_documentation_review_keeps_docs_scope_bounded():
    content = (
        REPO_ROOT / "docs/review/workflow-lineage-warning-code-documentation-review.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Workflow lineage warning code documentation review" in content
    assert "review-only gate" in content
    assert "warning_codes" in content
    assert "human-readable warnings remain canonical for readers" in content
    assert "derived_read_model_boundary" in content
    assert "missing_manifest_reference" in content
    assert "invalid_manifest_shape" in content
    assert "local_workflow_scope" in content
    assert "Do not add runtime behavior in this review gate" in content
    assert "no migrations" in content
    assert "no columns" in content
    assert "no join tables" in content
    assert "workflow lineage warning code runbook example v0" in content
    assert "Workflow lineage warning code documentation review v0" in goal
    assert "workflow lineage warning code runbook example v0" in goal


def test_phase37_runbook_documents_lineage_warning_code_response_shape():
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")

    assert "Phase 37 - Workflow Lineage Warning Code Runbook Example v0" in goal
    assert "Workflow lineage warning code runbook example v0: implemented" in readme
    assert "Expected `/workflow-runs/{id}/lineage` response shape" in runbook
    assert '"warnings": [' in runbook
    assert '"warning_codes": [' in runbook
    assert '"derived_read_model_boundary"' in runbook
    assert '"local_workflow_scope"' in runbook
    assert "response-level taxonomy only" in runbook
    assert "no migrations, columns, or join tables" in goal


def test_workflow_lineage_warning_code_dashboard_review_keeps_ui_scope_bounded():
    content = (
        REPO_ROOT / "docs/review/workflow-lineage-warning-code-dashboard-review.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Workflow lineage warning code dashboard review" in content
    assert "review-only gate" in content
    assert "GET /ops/dashboard" in content
    assert "warning_codes" in content
    assert "derived_read_model_boundary" in content
    assert "local_workflow_scope" in content
    assert "Do not add dashboard rendering in this review gate" in content
    assert "no migrations" in content
    assert "no columns" in content
    assert "no join tables" in content
    assert "workflow lineage warning code dashboard surfacing v0" in content
    assert "Workflow lineage warning code dashboard review v0" in goal
    assert "workflow lineage warning code dashboard surfacing v0" in goal


def test_phase38_docs_mark_warning_code_dashboard_surfacing_without_storage_expansion():
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    architecture = (REPO_ROOT / "docs/architecture.md").read_text(encoding="utf-8")

    assert "Phase 38 - Workflow Lineage Warning Code Dashboard Surfacing v0" in goal
    assert "Lineage warning codes" in goal
    assert "derived_read_model_boundary" in goal
    assert "local_workflow_scope" in goal
    assert "missing_manifest_reference" in goal
    assert "invalid_manifest_shape" in goal
    assert "no migrations, columns, or join tables" in goal
    assert "Workflow lineage warning code dashboard surfacing v0: implemented" in readme
    assert "Lineage warning codes" in runbook
    assert "not persisted dashboard analytics" in runbook
    assert "warning-code dashboard surfacing" in architecture


def test_phase38_5_docs_add_dashboard_warning_code_smoke_example():
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")

    assert "Phase 38.5 - Workflow Lineage Warning Code Dashboard Smoke Example v0" in goal
    assert "Expected `/ops/dashboard` warning-code legend" in runbook
    assert "Lineage warning codes:" in runbook
    assert "`derived_read_model_boundary`" in runbook
    assert "`local_workflow_scope`" in runbook
    assert "`missing_manifest_reference`" in runbook
    assert "`invalid_manifest_shape`" in runbook
    assert "not persisted dashboard analytics" in runbook
    assert "Workflow lineage warning code dashboard smoke example v0: implemented" in readme


def test_workflow_version_naming_review_keeps_runtime_scope_bounded():
    content = (REPO_ROOT / "docs/review/workflow-version-naming-review.md").read_text(
        encoding="utf-8"
    )
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Workflow version naming review" in content
    assert "review-only gate" in content
    assert "workflow_version" in content
    assert "phase36-structured-warning-taxonomy" in content
    assert "dashboard-only phases" in content
    assert "Do not rename workflow_version in this review gate" in content
    assert "no runtime behavior" in content
    assert "workflow version naming update v0" in content
    assert "Phase 39 - Workflow Version Naming Review v0" in goal
    assert "workflow version naming update v0" in goal


def test_phase40_docs_mark_workflow_version_naming_update_without_behavior_expansion():
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    architecture = (REPO_ROOT / "docs/architecture.md").read_text(encoding="utf-8")

    assert "Phase 40 - Workflow Version Naming Update v0" in goal
    assert "phase40-lineage-warning-code-dashboard" in goal
    assert "phase40-lineage-warning-code-dashboard" in runbook
    assert "Workflow version naming update v0: implemented" in readme
    assert "no workflow semantics" in goal
    assert "Workflow Version Naming Update v0 exists" in architecture


def test_phase40_5_docs_add_workflow_version_smoke_example():
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")

    assert "Phase 40.5 - Workflow Version Naming Smoke Example v0" in goal
    assert "workflow version naming smoke example v0" in goal
    assert "Workflow version naming smoke example v0: implemented" in readme
    assert "Expected workflow-version smoke checks" in runbook
    assert "curl http://localhost:8000/health" in runbook
    assert "curl http://localhost:8000/ops/summary" in runbook
    assert '"workflow_version": "phase40-lineage-warning-code-dashboard"' in runbook
    assert "no workflow semantics changed" in runbook


def test_workflow_version_naming_consistency_review_identifies_schema_default_drift():
    content = (
        REPO_ROOT / "docs/review/workflow-version-naming-consistency-review.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

    assert "Workflow version naming consistency review" in content
    assert "review-only gate" in content
    assert "phase40-lineage-warning-code-dashboard" in content
    assert "db/init/001_schema.sql" in content
    assert "db/migrations/007_workflow_runs.sql" in content
    assert "stale schema defaults" in content
    assert "Do not change schema defaults in this review gate" in content
    assert "schema default workflow version update v0" in content
    assert "Phase 41 - Workflow Version Naming Consistency Review v0" in goal
    assert "schema default workflow version update v0" in goal
    assert "Workflow version naming consistency review v0: implemented" in readme


def test_phase42_schema_default_workflow_version_update_uses_forward_migration():
    init_schema = (REPO_ROOT / "db/init/001_schema.sql").read_text(encoding="utf-8")
    migration_path = REPO_ROOT / "db/migrations/010_workflow_version_defaults.sql"
    migration = migration_path.read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

    assert migration_path.is_file()
    assert init_schema.count("DEFAULT 'phase40-lineage-warning-code-dashboard'") >= 2
    assert "ALTER TABLE agent_runs" in migration
    assert "ALTER COLUMN workflow_version SET DEFAULT 'phase40-lineage-warning-code-dashboard'" in migration
    assert "ALTER TABLE workflow_runs" in migration
    assert "Do not rewrite historical migration 007" in goal
    assert "Phase 42 - Schema Default Workflow Version Update v0" in goal
    assert "Schema default workflow version update v0: implemented" in readme


def test_phase42_5_docs_add_schema_default_workflow_version_smoke_example():
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")

    assert "Phase 42.5 - Schema Default Workflow Version Smoke Example v0" in goal
    assert "Schema default workflow version smoke example v0: implemented" in readme
    assert "Expected schema-default workflow-version smoke checks" in runbook
    assert "SELECT table_name, column_default" in runbook
    assert "agent_runs.workflow_version" in runbook
    assert "workflow_runs.workflow_version" in runbook
    assert "phase40-lineage-warning-code-dashboard" in runbook
    assert "schema defaults only" in runbook


def test_runtime_db_schema_default_verification_records_before_and_after_defaults():
    content = (REPO_ROOT / "docs/review/runtime-db-schema-default-verification.md").read_text(
        encoding="utf-8"
    )
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

    assert "Runtime DB schema default verification" in content
    assert "Docker runtime verification performed" in content
    assert "Initial observed defaults before applying migration 010" in content
    assert "phase5.5-collection-plan-preview" in content
    assert "phase24-workflow-run-schema" in content
    assert "Observed defaults after applying migration 010" in content
    assert "phase40-lineage-warning-code-dashboard" in content
    assert "No volume deletion was performed" in content
    assert "Phase 43 - Runtime DB Schema Default Verification v0" in goal
    assert "Runtime DB schema default verification v0: implemented" in readme


def test_migration_runner_review_selects_lightweight_sql_runner_next():
    content = (REPO_ROOT / "docs/review/migration-runner-review.md").read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

    assert "Migration runner review" in content
    assert "review-only gate" in content
    assert "runbook-only psql piping" in content
    assert "Alembic" in content
    assert "lightweight SQL migration runner" in content
    assert "schema_migrations" in content
    assert "Do not implement the runner in this review gate" in content
    assert "lightweight SQL migration runner v0" in content
    assert "Phase 44 - Migration Runner Review v0" in goal
    assert "Migration runner review v0: implemented" in readme


def test_phase45_docs_mark_lightweight_sql_migration_runner_boundary():
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")

    assert "Phase 45 - Lightweight SQL Migration Runner v0" in goal
    assert "Lightweight SQL migration runner v0: implemented" in readme
    assert "python -m app.migration_runner --status" in runbook
    assert "python -m app.migration_runner --baseline" in runbook
    assert "schema_migrations" in runbook
    assert "not a production migration platform" in runbook
    assert "No Alembic dependency" in goal


def test_runtime_migration_runner_verification_records_status_baseline_status():
    content = (REPO_ROOT / "docs/review/runtime-migration-runner-verification.md").read_text(
        encoding="utf-8"
    )
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

    assert "Runtime migration runner verification" in content
    assert "Docker runtime verification performed" in content
    assert "Initial runner status before baseline" in content
    assert "Applied migrations: 0" in content
    assert "Pending migrations: 9" in content
    assert "Runner baseline result" in content
    assert "baselined 010_workflow_version_defaults.sql" in content
    assert "Final runner status after baseline" in content
    assert "Applied migrations: 9" in content
    assert "Pending migrations: 0" in content
    assert "Phase 46 - Runtime Migration Runner Verification v0" in goal
    assert "Runtime migration runner verification v0: implemented" in readme


def test_migration_runner_fresh_db_verification_records_apply_path():
    content = (REPO_ROOT / "docs/review/migration-runner-fresh-db-verification.md").read_text(
        encoding="utf-8"
    )
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

    assert "Migration runner fresh DB verification" in content
    assert "isolated Compose project" in content
    assert "noiseproof-agent-fresh" in content
    assert "Initial runner status" in content
    assert "Applied migrations: 0" in content
    assert "Pending migrations: 9" in content
    assert "Runner apply result" in content
    assert "applied 010_workflow_version_defaults.sql" in content
    assert "Final runner status" in content
    assert "Applied migrations: 9" in content
    assert "Pending migrations: 0" in content
    assert "phase40-lineage-warning-code-dashboard" in content
    assert "test volume was removed" in content
    assert "Phase 47 - Migration Runner Fresh DB Verification v0" in goal
    assert "Migration runner fresh DB verification v0: implemented" in readme


def test_migration_runner_runbook_cleanup_makes_runner_first_and_manual_fallback():
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")

    assert "Phase 48 - Migration Runner Runbook Cleanup v0" in goal
    assert "Migration runner runbook cleanup v0: implemented" in readme
    assert "Default path: use the migration runner" in runbook
    assert "Do not use `--baseline` on a fresh DB" in runbook
    assert "manual SQL piping is a legacy/debug fallback" in runbook
    assert "Fresh or reset local DB" in runbook
    assert "Existing already-migrated local DB without schema_migrations rows" in runbook
    assert "Manual fallback" in runbook


def test_fresh_db_api_smoke_verification_records_service_path():
    content = (REPO_ROOT / "docs/review/fresh-db-api-smoke-verification.md").read_text(
        encoding="utf-8"
    )
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

    assert "Fresh DB API smoke verification" in content
    assert "noiseproof-agent-api-smoke" in content
    assert "POSTGRES_PORT=55435" in content
    assert "uv run python -m app.migration_runner" in content
    assert "uv run uvicorn app.main:app" in content
    assert "GET /health" in content
    assert "GET /ops/summary" in content
    assert "POST /documents" in content
    assert "GET /documents" in content
    assert "status_code: 200" in content
    assert "Sample fresh DB smoke document" in content
    assert "isolated test volume was removed" in content
    assert "Phase 49 - Fresh DB API Smoke Verification v0" in goal
    assert "Fresh DB API smoke verification v0: implemented" in readme


def test_application_evidence_index_refresh_surfaces_runtime_artifacts_without_overclaiming():
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(encoding="utf-8")
    role_map = (REPO_ROOT / "docs/application/braincrew-role-map.md").read_text(encoding="utf-8")
    review = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(encoding="utf-8")

    assert "Phase 50 - Application Evidence Index Refresh v0" in goal
    assert "Application evidence index refresh v0: implemented" in readme
    assert "Fresh DB API smoke verification" in portfolio
    assert "docs/review/fresh-db-api-smoke-verification.md" in portfolio
    assert "Migration runner fresh DB verification" in portfolio
    assert "docs/review/migration-runner-fresh-db-verification.md" in portfolio
    assert "fresh migrated Docker DB" in role_map
    assert "migration runner" in role_map
    assert "fresh DB API smoke" in review
    assert "not hosted deployment evidence" in review


def test_failure_case_persistence_smoke_verification_records_failure_ledger_path():
    content = (
        REPO_ROOT / "docs/review/failure-case-persistence-smoke-verification.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

    assert "Failure-case persistence smoke verification" in content
    assert "noiseproof-agent-failure-smoke" in content
    assert "POSTGRES_PORT=55436" in content
    assert "POST /failure-cases" in content
    assert "GET /failure-cases" in content
    assert "status_code: 201" in content
    assert "status_code: 200" in content
    assert "parser_timeout" in content
    assert "simulated parser timeout" in content
    assert "isolated test volume was removed" in content
    assert "Phase 51 - Failure-case Persistence Smoke Verification v0" in goal
    assert "Failure-case persistence smoke verification v0: implemented" in readme


def test_failure_case_application_evidence_refresh_surfaces_failure_smoke_without_detection_claims():
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(encoding="utf-8")
    role_map = (REPO_ROOT / "docs/application/braincrew-role-map.md").read_text(encoding="utf-8")
    review = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(encoding="utf-8")

    assert "Phase 52 - Failure-case Application Evidence Refresh v0" in goal
    assert "Failure-case application evidence refresh v0: implemented" in readme
    assert "Failure-case persistence smoke verification" in portfolio
    assert "docs/review/failure-case-persistence-smoke-verification.md" in portfolio
    assert "failure-case persistence smoke" in role_map
    assert "not automatic failure detection" in role_map
    assert "failure-case persistence smoke" in review
    assert "automatic failure detection is not claimed" in review


def test_agent_run_failure_linkage_smoke_verification_records_fk_path():
    content = (
        REPO_ROOT / "docs/review/agent-run-failure-linkage-smoke-verification.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

    assert "Agent-run failure linkage smoke verification" in content
    assert "noiseproof-agent-failure-link-smoke" in content
    assert "POSTGRES_PORT=55437" in content
    assert "POST /agent-runs" in content
    assert "POST /failure-cases" in content
    assert "GET /failure-cases" in content
    assert "agent_run_id" in content
    assert "linked_parser_timeout" in content
    assert "status_code: 201" in content
    assert "status_code: 200" in content
    assert "isolated test volume was removed" in content
    assert "Phase 53 - Agent-run Failure Linkage Smoke Verification v0" in goal
    assert "Agent-run failure linkage smoke verification v0: implemented" in readme


def test_agent_run_failure_linkage_application_refresh_surfaces_linked_failure_without_causality_claims():
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(encoding="utf-8")
    role_map = (REPO_ROOT / "docs/application/braincrew-role-map.md").read_text(encoding="utf-8")
    review = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(encoding="utf-8")

    assert "Phase 54 - Agent-run Failure Linkage Application Refresh v0" in goal
    assert "Agent-run failure linkage application refresh v0: implemented" in readme
    assert "Agent-run failure linkage smoke verification" in portfolio
    assert "docs/review/agent-run-failure-linkage-smoke-verification.md" in portfolio
    assert "linked failure-case proof" in role_map
    assert "not complete workflow failure causality" in role_map
    assert "agent-run failure linkage smoke" in review
    assert "complete workflow failure causality is not claimed" in review


def test_workflow_failure_provenance_review_defers_schema_until_causality_is_real():
    content = (REPO_ROOT / "docs/review/workflow-failure-provenance-review.md").read_text(
        encoding="utf-8"
    )
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

    assert "Workflow failure provenance review" in content
    assert "review-only gate" in content
    assert "operation-level failure linkage" in content
    assert "workflow-level failure causality" in content
    assert "Do not add workflow_run_id to failure_cases in this review gate" in content
    assert "Do not add automatic failure detection in this review gate" in content
    assert "manual failure record" in content
    assert "false sense of workflow failure causality" in content
    assert "workflow failure linkage smoke verification v0" in content
    assert "Phase 55 - Workflow Failure Provenance Review v0" in goal
    assert "Workflow failure provenance review v0: implemented" in readme


def test_workflow_failure_linkage_smoke_verification_stays_test_fixture_bounded():
    content = (REPO_ROOT / "docs/review/workflow-failure-linkage-smoke-verification.md").read_text(
        encoding="utf-8"
    )
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")

    assert "Workflow failure linkage smoke verification" in content
    assert "test-fixture smoke" in content
    assert "workflow_run.status = failed" in content
    assert "failure_cases remain unchanged" in content
    assert "no workflow_run_id on failure_cases" in content
    assert "not automatic failure detection" in content
    assert "not fresh Docker DB evidence" in content
    assert "Phase 56 - Workflow Failure Linkage Smoke Verification v0" in goal
    assert "Workflow failure linkage smoke verification v0: implemented" in readme
    assert "Phase 56 verifies the workflow failure path with a test fixture" in runbook


def test_workflow_failure_linkage_application_refresh_surfaces_workflow_failure_smoke():
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    role_map = (REPO_ROOT / "docs/application/braincrew-role-map.md").read_text(
        encoding="utf-8"
    )
    review = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(
        encoding="utf-8"
    )
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Workflow failure linkage application refresh v0: implemented" in readme
    assert "workflow failure linkage application refresh v0" in goal
    assert "Workflow failure linkage smoke verification" in portfolio
    assert "docs/review/workflow-failure-linkage-smoke-verification.md" in portfolio
    assert "failed workflow parent proof" in role_map
    assert "not automatic failure detection" in role_map
    assert "not fresh Docker DB evidence" in role_map
    assert "workflow failure linkage smoke" in review
    assert "complete workflow failure causality is not claimed" in review


def test_failure_case_workflow_linkage_review_defers_schema_until_creation_path_exists():
    content = (REPO_ROOT / "docs/review/failure-case-workflow-linkage-review.md").read_text(
        encoding="utf-8"
    )
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

    assert "Failure-case workflow linkage review" in content
    assert "review-only gate" in content
    assert "Do not add workflow_run_id to failure_cases yet" in content
    assert "manual failure record" in content
    assert "failed workflow parent" in content
    assert "no failure-case creation path" in content
    assert "schema remains unchanged" in content
    assert "failure-case workflow linkage review v0" in goal
    assert "Failure-case workflow linkage review v0: implemented" in readme


def test_failure_case_workflow_linkage_application_refresh_surfaces_deferred_schema_boundary():
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    role_map = (REPO_ROOT / "docs/application/braincrew-role-map.md").read_text(
        encoding="utf-8"
    )
    review = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(
        encoding="utf-8"
    )
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Failure-case workflow linkage application refresh v0: implemented" in readme
    assert "failure-case workflow linkage application refresh v0" in goal
    assert "Failure-case workflow linkage review" in portfolio
    assert "docs/review/failure-case-workflow-linkage-review.md" in portfolio
    assert "workflow_run_id on failure_cases remains deferred" in role_map
    assert "no failure-case creation path from failed workflow parents" in role_map
    assert "failure-case workflow linkage review" in review
    assert "failure cases are not linked to workflow parents yet" in review


def test_failure_case_creation_path_review_selects_manual_draft_before_automation():
    content = (REPO_ROOT / "docs/review/failure-case-creation-path-review.md").read_text(
        encoding="utf-8"
    )
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")

    assert "Failure-case creation path review" in content
    assert "review-only gate" in content
    assert "manual failure-case draft" in content
    assert "do not automatically create failure_cases from workflow failures" in content
    assert "human confirmation boundary" in content
    assert "no new API endpoint" in content
    assert "schema remains unchanged" in content
    assert "failure-case creation path review v0" in goal
    assert "Failure-case creation path review v0: implemented" in readme


def test_failure_case_draft_preview_docs_keep_persistence_boundary_visible():
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")

    assert "Failure-case draft preview v0: implemented" in readme
    assert "failure-case draft preview v0" in goal
    assert "POST /failure-cases/draft-preview" in readme
    assert "preview_only_not_persisted" in readme
    assert "human_confirmation_required" in readme
    assert "Expected failure-case draft preview smoke check" in runbook
    assert "does not persist a failure case" in runbook
