from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]


def readme_with_proof_marker_archive() -> str:
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    archive_path = REPO_ROOT / "docs/review/readme-proof-marker-archive.md"
    if archive_path.is_file():
        return readme + "\n" + archive_path.read_text(encoding="utf-8")
    return readme


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
        "docs/review/failure-case-draft-preview-smoke-verification.md",
        "docs/review/failure-case-draft-persistence-handoff-review.md",
        "docs/review/failure-case-draft-manual-handoff-smoke-verification.md",
        "docs/review/failure-case-draft-fresh-db-handoff-review.md",
        "docs/review/failure-case-draft-fresh-db-handoff-smoke-verification.md",
        "docs/review/failure-case-workflow-failure-to-draft-review.md",
        "docs/review/failure-case-workflow-parent-linkage-dashboard-review.md",
        "docs/review/failure-case-workflow-parent-linkage-fresh-db-dashboard-smoke-review.md",
        "docs/review/failure-case-workflow-parent-linkage-fresh-db-dashboard-smoke-verification.md",
        "docs/review/failure-case-workflow-parent-linkage-proof-consolidation-review.md",
        "docs/review/failure-case-workflow-parent-linkage-proof-index.md",
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
    readme = readme_with_proof_marker_archive()
    architecture = (REPO_ROOT / "docs/architecture.md").read_text(encoding="utf-8")

    assert "Phase 32 - Workflow Lineage Read Model v0" in goal
    assert "GET /workflow-runs/{id}/lineage" in goal
    assert "derived read model over existing workflow child records and stage_input_manifest values" in goal
    assert "does not add migrations, columns, join tables" in goal
    assert "Workflow lineage read model v0: implemented" in readme
    assert "GET /workflow-runs/{id}/lineage" in architecture


def test_phase33_docs_mark_dashboard_lineage_links_without_ui_polish_claims():
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
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
    readme = readme_with_proof_marker_archive()
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
    readme = readme_with_proof_marker_archive()
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
    readme = readme_with_proof_marker_archive()
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
    readme = readme_with_proof_marker_archive()
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
    readme = readme_with_proof_marker_archive()
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
    readme = readme_with_proof_marker_archive()
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
    readme = readme_with_proof_marker_archive()
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
    readme = readme_with_proof_marker_archive()
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
    readme = readme_with_proof_marker_archive()

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
    readme = readme_with_proof_marker_archive()

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
    readme = readme_with_proof_marker_archive()
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
    readme = readme_with_proof_marker_archive()

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
    readme = readme_with_proof_marker_archive()

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
    readme = readme_with_proof_marker_archive()
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
    readme = readme_with_proof_marker_archive()

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
    readme = readme_with_proof_marker_archive()

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
    readme = readme_with_proof_marker_archive()
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
    readme = readme_with_proof_marker_archive()

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
    readme = readme_with_proof_marker_archive()
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
    readme = readme_with_proof_marker_archive()

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
    readme = readme_with_proof_marker_archive()
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
    readme = readme_with_proof_marker_archive()

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
    readme = readme_with_proof_marker_archive()
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
    readme = readme_with_proof_marker_archive()

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
    readme = readme_with_proof_marker_archive()
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
    readme = readme_with_proof_marker_archive()
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
    readme = readme_with_proof_marker_archive()

    assert "Failure-case workflow linkage review" in content
    assert "review-only gate" in content
    assert "Do not add workflow_run_id to failure_cases yet" in content
    assert "manual failure record" in content
    assert "failed workflow parent" in content
    assert "no failure-case creation path" in content
    assert "schema remains unchanged" in content
    assert "failure-case workflow linkage review v0" in goal
    assert "Failure-case workflow linkage review v0: implemented" in readme


def test_failure_case_workflow_linkage_application_refresh_surfaces_historical_boundary():
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    role_map = (REPO_ROOT / "docs/application/braincrew-role-map.md").read_text(
        encoding="utf-8"
    )
    review = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Failure-case workflow linkage application refresh v0: implemented" in readme
    assert "failure-case workflow linkage application refresh v0" in goal
    assert "Failure-case workflow linkage review" in portfolio
    assert "docs/review/failure-case-workflow-linkage-review.md" in portfolio
    assert "historical failure-case workflow linkage review" in role_map
    assert "manual workflow parent linkage now exists" in role_map
    assert "failure-case workflow linkage review" in review
    assert "historical review boundary" in review


def test_failure_case_creation_path_review_selects_manual_draft_before_automation():
    content = (REPO_ROOT / "docs/review/failure-case-creation-path-review.md").read_text(
        encoding="utf-8"
    )
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()

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
    readme = readme_with_proof_marker_archive()
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")

    assert "Failure-case draft preview v0: implemented" in readme
    assert "failure-case draft preview v0" in goal
    assert "POST /failure-cases/draft-preview" in readme
    assert "preview_only_not_persisted" in readme
    assert "human_confirmation_required" in readme
    assert "Expected failure-case draft preview smoke check" in runbook
    assert "does not persist a failure case" in runbook


def test_failure_case_draft_preview_application_refresh_surfaces_manual_boundary():
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    role_map = (REPO_ROOT / "docs/application/braincrew-role-map.md").read_text(
        encoding="utf-8"
    )
    review = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Failure-case draft preview application refresh v0: implemented" in readme
    assert "failure-case draft preview application refresh v0" in goal
    assert "Failure-case draft preview" in portfolio
    assert "POST /failure-cases/draft-preview" in portfolio
    assert "human-confirmed draft payload" in role_map
    assert "preview_only_not_persisted" in role_map
    assert "failure-case draft preview exists" in review
    assert "does not persist failure cases automatically" in review


def test_failure_case_draft_preview_smoke_verification_keeps_preview_only_boundary():
    content = (
        REPO_ROOT / "docs/review/failure-case-draft-preview-smoke-verification.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()

    assert "Failure-case draft preview smoke verification" in content
    assert "route-level smoke" in content
    assert "POST /failure-cases/draft-preview" in content
    assert "preview_only_not_persisted" in content
    assert "human_confirmation_required: true" in content
    assert "failure_cases remain unchanged" in content
    assert "not automatic failure detection" in content
    assert "not fresh Docker DB evidence" in content
    assert "failure-case draft preview smoke verification v0" in goal
    assert "Failure-case draft preview smoke verification v0: implemented" in readme


def test_failure_case_draft_preview_smoke_application_refresh_surfaces_smoke_artifact():
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    role_map = (REPO_ROOT / "docs/application/braincrew-role-map.md").read_text(
        encoding="utf-8"
    )
    review = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Failure-case draft preview smoke application refresh v0: implemented" in readme
    assert "failure-case draft preview smoke application refresh v0" in goal
    assert "Failure-case draft preview smoke verification" in portfolio
    assert "docs/review/failure-case-draft-preview-smoke-verification.md" in portfolio
    assert "route-level smoke" in role_map
    assert "not fresh Docker DB evidence" in role_map
    assert "failure-case draft preview smoke" in review
    assert "automatic failure-case persistence is not claimed" in review


def test_failure_case_draft_persistence_handoff_review_defers_automation():
    content = (
        REPO_ROOT / "docs/review/failure-case-draft-persistence-handoff-review.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()

    assert "Failure-case draft persistence handoff review" in content
    assert "review-only gate" in content
    assert "manual handoff smoke" in content
    assert "POST /failure-cases/draft-preview" in content
    assert "POST /failure-cases" in content
    assert "Do not add automatic persistence in this review gate" in content
    assert "Do not add a confirm endpoint in this review gate" in content
    assert "human confirmation boundary" in content
    assert "failure-case draft persistence handoff review v0" in goal
    assert "Failure-case draft persistence handoff review v0: implemented" in readme


def test_failure_case_draft_manual_handoff_smoke_verification_records_existing_path():
    content = (
        REPO_ROOT / "docs/review/failure-case-draft-manual-handoff-smoke-verification.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()

    assert "Failure-case draft manual handoff smoke verification" in content
    assert "route-level smoke" in content
    assert "POST /failure-cases/draft-preview" in content
    assert "POST /failure-cases" in content
    assert "GET /failure-cases" in content
    assert "draft.fix_status: draft" in content
    assert "persisted.fix_status: open" in content
    assert "human confirmation boundary" in content
    assert "not automatic failure-case persistence" in content
    assert "failure-case draft manual handoff smoke verification v0" in goal
    assert "Failure-case draft manual handoff smoke verification v0: implemented" in readme


def test_failure_case_draft_manual_handoff_application_refresh_surfaces_human_step():
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    role_map = (REPO_ROOT / "docs/application/braincrew-role-map.md").read_text(
        encoding="utf-8"
    )
    review = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Failure-case draft manual handoff application refresh v0: implemented" in readme
    assert "failure-case draft manual handoff application refresh v0" in goal
    assert "Failure-case draft manual handoff smoke verification" in portfolio
    assert "docs/review/failure-case-draft-manual-handoff-smoke-verification.md" in portfolio
    assert "draft.fix_status from draft to open" in role_map
    assert "not automatic failure-case persistence" in role_map
    assert "failure-case draft manual handoff smoke" in review
    assert "human confirmation boundary remains explicit" in review


def test_failure_case_draft_fresh_db_handoff_review_selects_runtime_smoke():
    content = (
        REPO_ROOT / "docs/review/failure-case-draft-fresh-db-handoff-review.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()

    assert "Failure-case draft fresh DB handoff review" in content
    assert "review-only gate" in content
    assert "fresh migrated Docker DB" in content
    assert "manual handoff route-level smoke" in content
    assert "Do not add automatic persistence in this review gate" in content
    assert "Do not add a confirm endpoint in this review gate" in content
    assert "failure-case draft fresh-db handoff smoke verification v0" in content
    assert "not hosted deployment evidence" in content
    assert "failure-case draft fresh-db handoff review v0" in goal
    assert "Failure-case draft fresh-db handoff review v0: implemented" in readme


def test_failure_case_draft_fresh_db_handoff_smoke_verification_records_runtime_evidence():
    content = (
        REPO_ROOT / "docs/review/failure-case-draft-fresh-db-handoff-smoke-verification.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()

    assert "Failure-case draft fresh DB handoff smoke verification" in content
    assert "fresh migrated Docker DB" in content
    assert "noiseproof-agent-draft-handoff-smoke" in content
    assert "POST /failure-cases/draft-preview" in content
    assert "POST /failure-cases" in content
    assert "preview_persistence_boundary: preview_only_not_persisted" in content
    assert "draft_fix_status: draft" in content
    assert "persisted_fix_status: open" in content
    assert "ops_failure_case_count: 1" in content
    assert "not hosted deployment evidence" in content
    assert "failure-case draft fresh-db handoff smoke verification v0" in goal
    assert "Failure-case draft fresh-db handoff smoke verification v0: implemented" in readme


def test_failure_case_draft_fresh_db_handoff_application_refresh_surfaces_runtime_proof():
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    role_map = (REPO_ROOT / "docs/application/braincrew-role-map.md").read_text(
        encoding="utf-8"
    )
    review = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Failure-case draft fresh-db handoff application refresh v0: implemented" in readme
    assert "failure-case draft fresh-db handoff application refresh v0" in goal
    assert "Failure-case draft fresh DB handoff smoke verification" in portfolio
    assert "docs/review/failure-case-draft-fresh-db-handoff-smoke-verification.md" in portfolio
    assert "fresh migrated Docker DB handoff proof" in role_map
    assert "not hosted deployment evidence" in role_map
    assert "failure-case draft fresh DB handoff smoke" in review
    assert "automatic persistence remains unclaimed" in review


def test_failure_case_workflow_failure_to_draft_review_selects_preview_input_smoke():
    content = (
        REPO_ROOT / "docs/review/failure-case-workflow-failure-to-draft-review.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()

    assert "Failure-case workflow failure-to-draft review" in content
    assert "review-only gate" in content
    assert "failed workflow parent" in content
    assert "POST /failure-cases/draft-preview" in content
    assert "workflow_run.status = failed" in content
    assert "Do not add automatic failure-case creation in this review gate" in content
    assert "Do not add workflow_run_id to failure_cases in this review gate" in content
    assert "workflow failure-to-draft smoke verification v0" in content
    assert "not complete workflow failure causality" in content
    assert "failure-case workflow failure-to-draft review v0" in goal
    assert "Failure-case workflow failure-to-draft review v0: implemented" in readme


def test_workflow_failure_to_draft_smoke_verification_documents_route_boundary():
    content = (
        REPO_ROOT / "docs/review/workflow-failure-to-draft-smoke-verification.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()

    assert "Workflow failure-to-draft smoke verification" in content
    assert "route-level smoke" in content
    assert "POST /workflow-runs/execute-preview" in content
    assert "POST /failure-cases/draft-preview" in content
    assert "workflow_run.status: failed" in content
    assert "preview_only_not_persisted" in content
    assert "failure_cases remain unchanged" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "workflow failure-to-draft smoke verification v0" in goal
    assert "Workflow failure-to-draft smoke verification v0: implemented" in readme


def test_workflow_failure_to_draft_application_refresh_surfaces_smoke_boundary():
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    role_map = (REPO_ROOT / "docs/application/braincrew-role-map.md").read_text(
        encoding="utf-8"
    )
    review = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Workflow failure-to-draft application refresh v0: implemented" in readme
    assert "workflow failure-to-draft application refresh v0" in goal
    assert "Workflow failure-to-draft smoke verification" in portfolio
    assert "docs/review/workflow-failure-to-draft-smoke-verification.md" in portfolio
    assert "workflow failure-to-draft smoke" in role_map
    assert "not automatic failure-case creation" in role_map
    assert "workflow failure-to-draft smoke" in review
    assert "automatic failure-case creation remains unclaimed" in review


def test_failure_case_workflow_creation_path_decision_defers_automation():
    content = (
        REPO_ROOT / "docs/review/failure-case-workflow-creation-path-decision.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()

    assert "Failure-case workflow creation path decision" in content
    assert "decision-only gate" in content
    assert "automatic failure-case creation remains deferred" in content
    assert "human-confirmed persistence path" in content
    assert "workflow_run_id on failure_cases requires a schema gate" in content
    assert "failure-case workflow creation path decision v0" in goal
    assert "Failure-case workflow creation path decision v0: implemented" in readme


def test_failure_case_workflow_parent_linkage_schema_review_selects_nullable_fk():
    content = (
        REPO_ROOT
        / "docs/review/failure-case-workflow-parent-linkage-schema-review.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()

    assert "Failure-case workflow parent linkage schema review" in content
    assert "review-only gate" in content
    assert "nullable workflow_run_id on failure_cases" in content
    assert "REFERENCES workflow_runs(id) ON DELETE SET NULL" in content
    assert "automatic failure-case creation remains deferred" in content
    assert "no migration is added in this review gate" in content
    assert "failure-case workflow parent linkage schema review v0" in goal
    assert "Failure-case workflow parent linkage schema review v0: implemented" in readme


def test_failure_cases_schema_has_nullable_workflow_parent_link():
    init_schema = (REPO_ROOT / "db/init/001_schema.sql").read_text(encoding="utf-8")
    migration = (
        REPO_ROOT / "db/migrations/011_failure_case_workflow_run_id.sql"
    ).read_text(encoding="utf-8")
    combined = init_schema + "\n" + migration
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()

    assert "workflow_run_id UUID REFERENCES workflow_runs(id) ON DELETE SET NULL" in combined
    assert "ALTER TABLE failure_cases" in migration
    assert "idx_failure_cases_workflow_run_id" in migration
    assert "failure-case workflow parent linkage schema v0" in goal
    assert "Failure-case workflow parent linkage schema v0: implemented" in readme


def test_failure_case_workflow_parent_linkage_smoke_verification_documents_boundary():
    content = (
        REPO_ROOT
        / "docs/review/failure-case-workflow-parent-linkage-smoke-verification.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()

    assert "Failure-case workflow parent linkage smoke verification" in content
    assert "route-level smoke" in content
    assert "POST /workflow-runs" in content
    assert "POST /failure-cases" in content
    assert "workflow_run_id retained" in content
    assert "draft-preview carries workflow_run_id" in content
    assert "not automatic failure-case creation" in content
    assert "not fresh Docker DB evidence" in content
    assert "failure-case workflow parent linkage smoke verification v0" in goal
    assert "Failure-case workflow parent linkage smoke verification v0: implemented" in readme


def test_failure_case_workflow_parent_linkage_fresh_db_verification_documents_runtime_proof():
    content = (
        REPO_ROOT
        / "docs/review/failure-case-workflow-parent-linkage-fresh-db-verification.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()

    assert "Failure-case workflow parent linkage fresh DB verification" in content
    assert "local fresh migrated Docker DB evidence" in content
    assert "applied 011_failure_case_workflow_run_id.sql" in content
    assert "persisted_workflow_run_id_matches: true" in content
    assert "listed_workflow_run_id_matches: true" in content
    assert "ops_failure_case_count: 1" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "failure-case workflow parent linkage fresh-db verification v0" in goal
    assert "Failure-case workflow parent linkage fresh-db verification v0: implemented" in readme


def test_failure_case_workflow_parent_linkage_application_refresh_surfaces_fresh_db_boundary():
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    role_map = (REPO_ROOT / "docs/application/braincrew-role-map.md").read_text(
        encoding="utf-8"
    )
    review = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Failure-case workflow parent linkage application refresh v0: implemented" in readme
    assert "failure-case workflow parent linkage application refresh v0" in goal
    assert "Failure-case workflow parent linkage fresh DB verification" in portfolio
    assert (
        "docs/review/failure-case-workflow-parent-linkage-fresh-db-verification.md"
        in portfolio
    )
    assert "workflow parent linkage fresh DB proof" in role_map
    assert "not hosted deployment evidence" in role_map
    assert "failure-case workflow parent linkage fresh DB" in review
    assert "automatic failure-case creation remains unclaimed" in review


def test_failure_case_workflow_parent_linkage_dashboard_review_defers_rendering_change():
    content = (
        REPO_ROOT
        / "docs/review/failure-case-workflow-parent-linkage-dashboard-review.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()

    assert "Failure-case workflow parent linkage dashboard review" in content
    assert "review-only gate" in content
    assert "Failure Cases table" in content
    assert "workflow_run_id" in content
    assert "Do not add dashboard rendering in this review gate" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "failure-case workflow parent linkage dashboard review v0" in goal
    assert "Failure-case workflow parent linkage dashboard review v0: implemented" in readme


def test_failure_case_workflow_parent_linkage_dashboard_surfacing_docs_keep_manual_boundary():
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")

    assert "failure-case workflow parent linkage dashboard surfacing v0" in goal
    assert "Failure-case workflow parent linkage dashboard surfacing v0: implemented" in readme
    assert "Expected failure-case workflow parent dashboard smoke check" in runbook
    assert "Workflow Parent" in runbook
    assert "manual workflow parent link" in runbook
    assert "not automatic failure-case creation" in runbook


def test_failure_case_workflow_parent_dashboard_application_refresh_surfaces_manual_link_boundary():
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    role_map = (REPO_ROOT / "docs/application/braincrew-role-map.md").read_text(
        encoding="utf-8"
    )
    review = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Failure-case workflow parent linkage dashboard application refresh v0: implemented" in readme
    assert "failure-case workflow parent linkage dashboard application refresh v0" in goal
    assert "Failure-case workflow parent linkage dashboard surfacing" in portfolio
    assert "`GET /ops/dashboard` Failure Cases table Workflow Parent column" in portfolio
    assert "dashboard manual workflow parent link" in role_map
    assert "not automatic failure-case creation" in role_map
    assert "failure-case workflow parent dashboard link" in review
    assert "manual provenance only" in review


def test_failure_case_workflow_parent_fresh_db_dashboard_smoke_review_selects_runtime_html_check():
    content = (
        REPO_ROOT
        / "docs/review/failure-case-workflow-parent-linkage-fresh-db-dashboard-smoke-review.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()

    assert "Failure-case workflow parent linkage fresh DB dashboard smoke review" in content
    assert "review-only gate" in content
    assert "GET /ops/dashboard" in content
    assert "Workflow Parent" in content
    assert "fresh migrated Docker DB" in content
    assert "Do not run the fresh DB smoke in this review gate" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "failure-case workflow parent linkage fresh-db dashboard smoke review v0" in goal
    assert "Failure-case workflow parent linkage fresh-db dashboard smoke review v0: implemented" in readme


def test_failure_case_workflow_parent_fresh_db_dashboard_smoke_verification_documents_runtime_html_proof():
    content = (
        REPO_ROOT
        / "docs/review/failure-case-workflow-parent-linkage-fresh-db-dashboard-smoke-verification.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()

    assert "Failure-case workflow parent linkage fresh DB dashboard smoke verification" in content
    assert "local fresh migrated Docker DB dashboard evidence" in content
    assert "applied 011_failure_case_workflow_run_id.sql" in content
    assert "dashboard_contains_workflow_parent: true" in content
    assert "dashboard_contains_workflow_link: true" in content
    assert "dashboard_contains_manual_boundary: true" in content
    assert "dashboard_contains_not_automatic_creation: true" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "failure-case workflow parent linkage fresh-db dashboard smoke verification v0" in goal
    assert (
        "Failure-case workflow parent linkage fresh-db dashboard smoke verification v0: implemented"
        in readme
    )


def test_failure_case_workflow_parent_fresh_db_dashboard_smoke_application_refresh_surfaces_runtime_boundary():
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    role_map = (REPO_ROOT / "docs/application/braincrew-role-map.md").read_text(
        encoding="utf-8"
    )
    review = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert (
        "Failure-case workflow parent linkage fresh-db dashboard smoke application refresh v0: implemented"
        in readme
    )
    assert "failure-case workflow parent linkage fresh-db dashboard smoke application refresh v0" in goal
    assert "Failure-case workflow parent linkage fresh DB dashboard smoke verification" in portfolio
    assert (
        "docs/review/failure-case-workflow-parent-linkage-fresh-db-dashboard-smoke-verification.md"
        in portfolio
    )
    assert "local fresh migrated Docker DB dashboard evidence" in portfolio
    assert "dashboard_contains_workflow_link: true" in portfolio
    assert "fresh DB dashboard Workflow Parent proof" in role_map
    assert "not hosted deployment evidence" in role_map
    assert "not automatic failure-case creation" in role_map
    assert "not complete workflow failure causality" in role_map
    assert "failure-case workflow parent dashboard fresh DB smoke" in review
    assert "manual provenance only" in review


def test_failure_case_workflow_parent_linkage_proof_consolidation_review_selects_index_gate():
    content = (
        REPO_ROOT
        / "docs/review/failure-case-workflow-parent-linkage-proof-consolidation-review.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()

    assert "Failure-case workflow parent linkage proof consolidation review" in content
    assert "review-only gate" in content
    assert "proof chain is now too distributed" in content
    assert "Do not create a new proof index in this review gate" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "failure-case workflow parent linkage proof index v0" in content
    assert "failure-case workflow parent linkage proof consolidation review v0" in goal
    assert (
        "Failure-case workflow parent linkage proof consolidation review v0: implemented"
        in readme
    )


def test_failure_case_workflow_parent_linkage_proof_index_gives_reader_path_and_boundaries():
    content = (
        REPO_ROOT
        / "docs/review/failure-case-workflow-parent-linkage-proof-index.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()

    assert "Failure-case workflow parent linkage proof index" in content
    assert "reader path" in content
    assert "schema boundary" in content
    assert "manual persistence" in content
    assert "fresh DB persistence" in content
    assert "dashboard surfacing" in content
    assert "fresh DB dashboard proof" in content
    assert "docs/review/failure-case-workflow-parent-linkage-schema-review.md" in content
    assert "docs/review/failure-case-workflow-parent-linkage-fresh-db-verification.md" in content
    assert (
        "docs/review/failure-case-workflow-parent-linkage-fresh-db-dashboard-smoke-verification.md"
        in content
    )
    assert "Allowed claim" in content
    assert "Forbidden claim" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "failure-case workflow parent linkage proof index v0" in goal
    assert "Failure-case workflow parent linkage proof index v0: implemented" in readme


def test_failure_case_workflow_parent_linkage_proof_index_application_refresh_surfaces_reader_path():
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    role_map = (REPO_ROOT / "docs/application/braincrew-role-map.md").read_text(
        encoding="utf-8"
    )
    review = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert (
        "Failure-case workflow parent linkage proof index application refresh v0: implemented"
        in readme
    )
    assert "failure-case workflow parent linkage proof index application refresh v0" in goal
    assert "Failure-case workflow parent linkage proof index" in portfolio
    assert "docs/review/failure-case-workflow-parent-linkage-proof-index.md" in portfolio
    assert "schema boundary -> manual persistence -> fresh DB persistence" in portfolio
    assert "workflow parent proof index" in role_map
    assert "reader path" in role_map
    assert "not automatic failure-case creation" in role_map
    assert "not complete workflow failure causality" in role_map
    assert "proof index reader path" in review
    assert "Allowed claim" in review
    assert "Forbidden claim" in review


def test_failure_case_workflow_parent_linkage_stale_claim_review_identifies_cleanup_gate():
    content = (
        REPO_ROOT
        / "docs/review/failure-case-workflow-parent-linkage-stale-claim-review.md"
    ).read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()

    assert "Failure-case workflow parent linkage stale-claim review" in content
    assert "review-only gate" in content
    assert "stale claim candidates" in content
    assert "failure cases are not linked to workflow parents yet" in content
    assert "workflow_run_id remains deferred" in content
    assert "Do not rewrite application-facing claims in this review gate" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "failure-case workflow parent linkage stale-claim cleanup v0" in content
    assert (
        "failure-case workflow parent linkage proof chain stale-claim review v0"
        in goal
    )
    assert (
        "Failure-case workflow parent linkage proof chain stale-claim review v0: implemented"
        in readme
    )


def test_failure_case_workflow_parent_linkage_stale_claim_cleanup_updates_current_facing_docs():
    cleanup = (
        REPO_ROOT
        / "docs/review/failure-case-workflow-parent-linkage-stale-claim-cleanup.md"
    ).read_text(encoding="utf-8")
    role_map = (REPO_ROOT / "docs/application/braincrew-role-map.md").read_text(
        encoding="utf-8"
    )
    review = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    stale_current_claims = [
        "workflow_run_id on failure_cases remains deferred",
        "failure cases are not linked to workflow parents yet",
        "The failure-case workflow linkage review states that workflow_run_id on failure_cases remains deferred",
    ]
    for claim in stale_current_claims:
        assert claim not in role_map
        assert claim not in review

    assert "Failure-case workflow parent linkage stale-claim cleanup" in cleanup
    assert "application-facing cleanup" in cleanup
    assert "historical review artifacts are preserved" in cleanup
    assert "manual workflow parent linkage now exists" in cleanup
    assert "not automatic failure-case creation" in cleanup
    assert "not complete workflow failure causality" in cleanup
    assert "failure-case workflow parent linkage stale-claim cleanup v0" in goal
    assert (
        "Failure-case workflow parent linkage stale-claim cleanup v0: implemented"
        in readme
    )
    assert "manual workflow parent linkage now exists" in role_map
    assert "automatic failure-case creation remains unclaimed" in role_map
    assert "historical review boundary" in review
    assert "manual workflow parent linkage now exists" in review


def test_external_reader_proof_path_review_selects_compact_reader_gate():
    content = (REPO_ROOT / "docs/review/external-reader-proof-path-review.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "External-reader proof path review" in content
    assert "review-only gate" in content
    assert "reviewer entry path" in content
    assert "README.md" in content
    assert "docs/application/portfolio-index.md" in content
    assert "docs/review/failure-case-workflow-parent-linkage-proof-index.md" in content
    assert "Do not create a new external-reader path in this review gate" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "external-reader proof path index v0" in content
    assert "external-reader proof path review v0" in goal
    assert "External-reader proof path review v0: implemented" in readme


def test_external_reader_proof_path_index_gives_five_minute_path_and_boundaries():
    content = (REPO_ROOT / "docs/review/external-reader-proof-path.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "External-reader Proof Path" in content
    assert "5-minute path" in content
    assert "README.md" in content
    assert "docs/application/portfolio-index.md" in content
    assert "docs/review/failure-case-workflow-parent-linkage-proof-index.md" in content
    assert "docs/review/application-ready-review.md" in content
    assert "docs/application/braincrew-role-map.md" in content
    assert "Allowed claim" in content
    assert "Forbidden claim" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "docs/review/portfolio-site-proof-artifact-route-verification.md" in content
    assert "docs/review/local-browser-screenshot-walkthrough.md" in content
    assert "external reviewer feedback v0" in content
    assert "external-reader proof path index v0" in goal
    assert "External-reader proof path index v0: implemented" in readme


def test_portfolio_external_proof_path_refresh_surfaces_compact_reader_path():
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Portfolio external proof path refresh v0: implemented" in readme
    assert "portfolio external proof path refresh v0" in goal
    assert "External-reader proof path" in portfolio
    assert "docs/review/external-reader-proof-path.md" in portfolio
    assert "5-minute path" in portfolio
    assert "not hosted deployment evidence" in portfolio
    assert "not automatic failure-case creation" in portfolio
    assert "not complete workflow failure causality" in portfolio


def test_external_reader_proof_path_application_refresh_review_selects_application_docs():
    content = (
        REPO_ROOT
        / "docs/review/external-reader-proof-path-application-refresh-review.md"
    ).read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "External-reader proof path application refresh review" in content
    assert "review-only gate" in content
    assert "docs/application/braincrew-role-map.md" in content
    assert "docs/review/application-ready-review.md" in content
    assert "Do not refresh application-facing docs in this review gate" in content
    assert "external-reader proof path application refresh v0" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "external-reader proof path application refresh review v0" in goal
    assert "External-reader proof path application refresh review v0: implemented" in readme


def test_external_reader_proof_path_application_refresh_surfaces_path_in_application_docs():
    role_map = (REPO_ROOT / "docs/application/braincrew-role-map.md").read_text(
        encoding="utf-8"
    )
    review = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "External-reader proof path application refresh v0: implemented" in readme
    assert "external-reader proof path application refresh v0" in goal
    assert "External-reader proof path" in role_map
    assert "docs/review/external-reader-proof-path.md" in role_map
    assert "5-minute path" in role_map
    assert "External-reader proof path" in review
    assert "docs/review/external-reader-proof-path.md" in review
    assert "5-minute path" in review
    assert "not hosted deployment evidence" in role_map
    assert "not automatic failure-case creation" in role_map
    assert "not complete workflow failure causality" in review


def test_readme_external_proof_path_refresh_review_selects_readme_fast_path():
    content = (
        REPO_ROOT / "docs/review/readme-external-proof-path-refresh-review.md"
    ).read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "README external proof path refresh review" in content
    assert "review-only gate" in content
    assert "README.md" in content
    assert "docs/review/external-reader-proof-path.md" in content
    assert "Do not edit README fast path in this review gate" in content
    assert "readme external proof path refresh v0" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "readme external proof path refresh review v0" in goal
    assert "README external proof path refresh review v0: implemented" in readme


def test_readme_external_proof_path_refresh_adds_top_level_fast_path():
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    fast_path_index = readme.index("## External Reviewer Fast Path")
    what_this_is_index = readme.index("## What This Is")

    assert fast_path_index < what_this_is_index
    assert "docs/review/external-reader-proof-path.md" in readme
    assert "5-minute repository-native path" in readme
    assert "not hosted deployment evidence" in readme
    assert "not automatic failure-case creation" in readme
    assert "not complete workflow failure causality" in readme
    assert "readme external proof path refresh v0" in goal
    assert "README external proof path refresh v0: implemented" in readme


def test_readme_phase_history_compression_review_selects_readability_gate():
    content = (
        REPO_ROOT / "docs/review/readme-phase-history-compression-review.md"
    ).read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "README phase-history compression review" in content
    assert "review-only gate" in content
    assert "phase-history paragraph is too long" in content
    assert "Do not compress README in this review gate" in content
    assert "readme phase-history compression v0" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "readme phase-history compression review v0" in goal
    assert "README phase-history compression review v0: implemented" in readme


def test_readme_phase_history_compression_replaces_chronological_wall_with_summary():
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    what_this_is = readme.split("## What This Is", 1)[1].split("## What This Is Not", 1)[0]

    assert "Current implemented capability groups" in what_this_is
    assert "Detailed phase history lives in `docs/GOAL.md`" in what_this_is
    assert "The project started with a documentation-first Day 1 package." not in what_this_is
    assert "Phase 46 verified the runner against the local Docker DB" not in what_this_is
    assert len(what_this_is) < 2500
    assert "readme phase-history compression v0" in goal
    assert "README phase-history compression v0: implemented" in readme


def test_readme_implementation_status_compression_review_selects_scanability_gate():
    content = (
        REPO_ROOT / "docs/review/readme-implementation-status-compression-review.md"
    ).read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "README implementation-status compression review" in content
    assert "review-only gate" in content
    assert "implementation status list is too long" in content
    assert "Do not compress README implementation status in this review gate" in content
    assert "readme implementation-status compression v0" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "readme implementation-status compression review v0" in goal
    assert "README implementation-status compression review v0: implemented" in readme


def test_readme_implementation_status_compression_replaces_top_status_wall():
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    top_status = readme.split("Implementation status:", 1)[1].split(
        "## Implementation Status", 1
    )[0]

    assert "Current status groups" in top_status
    assert "Detailed implementation history remains in the lower detailed Implementation Status section" in top_status
    assert "Failure-case draft fresh-db handoff review v0" not in top_status
    assert "README phase-history compression review v0" not in top_status
    assert len(top_status) < 1800
    assert "readme implementation-status compression v0" in goal
    assert "README implementation-status compression v0: implemented" in readme


def test_readme_detailed_implementation_status_compression_review_selects_lower_section_gate():
    content = (
        REPO_ROOT
        / "docs/review/readme-detailed-implementation-status-compression-review.md"
    ).read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "README detailed implementation-status compression review" in content
    assert "review-only gate" in content
    assert "detailed implementation status section is too long" in content
    assert "Do not compress lower README implementation status in this review gate" in content
    assert "readme detailed implementation-status compression v0" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "readme detailed implementation-status compression review v0" in goal
    assert "README detailed implementation-status compression review v0: implemented" in readme


def test_readme_detailed_implementation_status_compression_replaces_lower_phase_wall():
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    lower_status = readme.split("## Implementation Status", 1)[1].split(
        "Not implemented yet:", 1
    )[0]

    assert "Major implementation milestones" in lower_status
    assert "For exhaustive phase history, use `docs/GOAL.md`" in lower_status
    assert "### Phase 46 - Runtime Migration Runner Verification v0" not in lower_status
    assert "### Phase 101 - README Implementation-status Compression v0" not in lower_status
    assert len(lower_status) < 4500
    assert "readme detailed implementation-status compression v0" in goal
    assert "README detailed implementation-status compression v0: implemented" in readme


def test_readme_proof_marker_archive_review_selects_archive_extraction_gate():
    content = (REPO_ROOT / "docs/review/readme-proof-marker-archive-review.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "README proof-marker archive review" in content
    assert "review-only gate" in content
    assert "hidden README archive is a temporary compatibility bridge" in content
    assert "Do not extract the archive in this review gate" in content
    assert "readme proof-marker archive extraction v0" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "readme proof-marker archive review v0" in goal
    assert "README proof-marker archive review v0: implemented" in readme


def test_readme_proof_marker_archive_extraction_moves_hidden_archive_out_of_readme():
    archive = (REPO_ROOT / "docs/review/readme-proof-marker-archive.md").read_text(
        encoding="utf-8"
    )
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "README detailed implementation status archive moved during Phase 103" not in readme
    assert "README proof-marker archive extraction v0: implemented" in readme
    assert "Legacy README proof markers moved out of README" in archive
    assert "Workflow lineage read model v0: implemented" in archive
    assert "Failure-case workflow parent linkage proof index v0: implemented" in archive
    assert "README detailed implementation-status compression v0: implemented" in archive
    assert "readme proof-marker archive extraction v0" in goal


def test_readme_proof_marker_archive_application_refresh_review_selects_application_docs():
    content = (
        REPO_ROOT
        / "docs/review/readme-proof-marker-archive-application-refresh-review.md"
    ).read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "README proof-marker archive application refresh review" in content
    assert "review-only gate" in content
    assert "application-facing docs do not yet mention the extracted proof-marker archive" in content
    assert "Do not refresh application-facing docs in this review gate" in content
    assert "readme proof-marker archive application refresh v0" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "readme proof-marker archive application refresh review v0" in goal
    assert "README proof-marker archive application refresh review v0: implemented" in readme


def test_readme_proof_marker_archive_application_refresh_surfaces_archive_path():
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    role_map = (REPO_ROOT / "docs/application/braincrew-role-map.md").read_text(
        encoding="utf-8"
    )
    review = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    for content in (portfolio, role_map, review):
        assert "docs/review/readme-proof-marker-archive.md" in content
        assert "source-level provenance" in content
        assert "not product runtime evidence" in content
        assert "not hosted deployment evidence" in content
        assert "not automatic failure-case creation" in content
        assert "not complete workflow failure causality" in content

    assert "README proof-marker archive application refresh v0: implemented" in readme
    assert "readme proof-marker archive application refresh v0" in goal


def test_readme_proof_marker_archive_external_path_review_selects_compact_note():
    review_path = REPO_ROOT / "docs/review/readme-proof-marker-archive-external-path-review.md"
    assert review_path.is_file()
    content = review_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "README proof-marker archive external path review" in content
    assert "review-only gate" in content
    assert "external-reader proof path should stay compact" in content
    assert "Do not update the external-reader proof path in this review gate" in content
    assert "readme proof-marker archive external path refresh v0" in content
    assert "source-level provenance" in content
    assert "not product runtime evidence" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "readme proof-marker archive external path review v0" in goal
    assert "README proof-marker archive external path review v0: implemented" in readme


def test_readme_proof_marker_archive_external_path_refresh_adds_optional_note():
    proof_path = (REPO_ROOT / "docs/review/external-reader-proof-path.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Optional source-level provenance" in proof_path
    assert "docs/review/readme-proof-marker-archive.md" in proof_path
    assert "not product runtime evidence" in proof_path
    assert "not hosted deployment evidence" in proof_path
    assert "not automatic failure-case creation" in proof_path
    assert "not complete workflow failure causality" in proof_path
    assert "README proof-marker archive external path refresh v0: implemented" in readme
    assert "readme proof-marker archive external path refresh v0" in goal


def test_application_current_claim_compression_review_selects_claim_scanability_gate():
    review_path = REPO_ROOT / "docs/review/application-current-claim-compression-review.md"
    assert review_path.is_file()
    content = review_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Application current-claim compression review" in content
    assert "review-only gate" in content
    assert "application-facing current claims are too long" in content
    assert "Do not compress application claims in this review gate" in content
    assert "application current-claim compression v0" in content
    assert "not product-complete declaration" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "application current-claim compression review v0" in goal
    assert "Application current-claim compression review v0: implemented" in readme


def test_application_current_claim_compression_replaces_claim_walls():
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    review = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    portfolio_claim = portfolio.split("## Current Best Claim", 1)[1].split(
        "##", 1
    )[0]
    review_claim = review.split("## Best External Claim", 1)[1].split(
        "Do not use:", 1
    )[0]

    assert "Short current claim:" in portfolio_claim
    assert "Detailed proof history remains in" in portfolio_claim
    assert "Short external claim:" in review_claim
    assert "Detailed phase history remains in" in review_claim
    assert "not product-complete declaration" in review_claim
    assert len(portfolio_claim) < 1800
    assert len(review_claim) < 1400
    assert "README proof-marker archive external path refresh v0" not in portfolio_claim
    assert "Workflow lineage warning code dashboard smoke example" not in review_claim
    assert "Application current-claim compression v0: implemented" in readme
    assert "application current-claim compression v0" in goal


def test_braincrew_role_map_runtime_proof_compression_review_selects_role_map_gate():
    review_path = (
        REPO_ROOT / "docs/review/braincrew-role-map-runtime-proof-compression-review.md"
    )
    assert review_path.is_file()
    content = review_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Braincrew role-map runtime proof compression review" in content
    assert "review-only gate" in content
    assert "Runtime Proof Surfaces section is too long" in content
    assert "Do not compress the Braincrew role map in this review gate" in content
    assert "braincrew role-map runtime proof compression v0" in content
    assert "FDE-first mapping" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "braincrew role-map runtime proof compression review v0" in goal
    assert "Braincrew role-map runtime proof compression review v0: implemented" in readme


def test_braincrew_role_map_runtime_proof_compression_replaces_proof_wall():
    role_map = (REPO_ROOT / "docs/application/braincrew-role-map.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runtime_section = role_map.split("## Runtime Proof Surfaces", 1)[1].split(
        "## DeepDocurator Alignment", 1
    )[0]

    assert "Runtime proof summary:" in runtime_section
    assert "Detailed proof links:" in runtime_section
    assert "The failure-case draft preview can turn workflow failure evidence" not in runtime_section
    assert "The fresh DB dashboard Workflow Parent proof verifies" not in runtime_section
    assert "The workflow parent proof index gives the reader path" not in runtime_section
    assert "not hosted deployment evidence" in runtime_section
    assert "not automatic failure-case creation" in runtime_section
    assert "not complete workflow failure causality" in runtime_section
    assert "not automatic failure detection" in runtime_section
    assert len(runtime_section) < 4200
    assert "Braincrew role-map runtime proof compression v0: implemented" in readme
    assert "braincrew role-map runtime proof compression v0" in goal


def test_application_proof_surface_final_scan_review_selects_final_cleanup_gate():
    review_path = REPO_ROOT / "docs/review/application-proof-surface-final-scan-review.md"
    assert review_path.is_file()
    content = review_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Application proof surface final scan review" in content
    assert "review-only gate" in content
    assert "scan result" in content
    assert "Do not edit proof surfaces in this review gate" in content
    assert "application proof surface final cleanup v0" in content
    assert "no broad product-complete claim" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "application proof surface final scan review v0" in goal
    assert "Application proof surface final scan review v0: implemented" in readme


def test_application_ready_summary_compression_replaces_phase_wall():
    review = (REPO_ROOT / "docs/review/application-ready-review.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    summary = review.split("## Summary", 1)[1].split("## Checklist", 1)[0]

    assert "Current judgment: Partial application-ready portfolio artifact." in summary
    assert "not a product-complete declaration" in summary
    assert "Detailed evidence remains in the checklist below" in summary
    assert "external-reader proof path" in summary
    assert "not hosted deployment evidence" in summary
    assert "not automatic failure-case creation" in summary
    assert "not complete workflow failure causality" in summary
    assert "workflow stage input manifests" not in summary
    assert "failure-case workflow parent dashboard fresh DB smoke" not in summary
    assert len(summary) < 1200
    assert "application-ready summary compression v0" in goal
    assert "Application-ready summary compression v0: implemented" in readme


def test_external_reader_final_proof_path_dry_read_review_selects_next_gate_refresh():
    review_path = (
        REPO_ROOT / "docs/review/external-reader-final-proof-path-dry-read-review.md"
    )
    assert review_path.is_file()
    content = review_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "External-reader final proof-path dry-read review" in content
    assert "review-only gate" in content
    assert "5-minute path remains usable" in content
    assert "stale Next Gate" in content
    assert "Do not edit the external-reader proof path in this review gate" in content
    assert "external-reader proof path next-gate refresh v0" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "external-reader final proof-path dry-read review v0" in goal
    assert "External-reader final proof-path dry-read review v0: implemented" in readme


def test_external_reader_proof_path_next_gate_refresh_replaces_stale_next_gate():
    proof_path = (REPO_ROOT / "docs/review/external-reader-proof-path.md").read_text(
        encoding="utf-8"
    )
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    next_gate = proof_path.split("## Next Gate", 1)[1]

    assert "external reviewer feedback v0" in next_gate
    assert "local browser screenshot walkthrough v0" not in next_gate
    assert "portfolio external proof path refresh v0" not in next_gate
    assert "not hosted deployment evidence" in proof_path
    assert "not automatic failure-case creation" in proof_path
    assert "not complete workflow failure causality" in proof_path
    assert "external-reader proof path next-gate refresh v0" in goal
    assert "External-reader proof path next-gate refresh v0: implemented" in readme


def test_application_package_final_consistency_review_selects_portfolio_handoff():
    review_path = REPO_ROOT / "docs/review/application-package-final-consistency-review.md"
    assert review_path.is_file()
    content = review_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Application package final consistency review" in content
    assert "review-only gate" in content
    assert "no stale Next Gate" in content
    assert "README.md" in content
    assert "external-reader proof path" in content
    assert "portfolio index" in content
    assert "application-ready review" in content
    assert "Braincrew role map" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "portfolio site handoff review v0" in content
    assert "application package final consistency review v0" in goal
    assert "Application package final consistency review v0: implemented" in readme


def test_portfolio_site_handoff_review_selects_noiseproof_artifact_refresh():
    review_path = REPO_ROOT / "docs/review/portfolio-site-handoff-review.md"
    assert review_path.is_file()
    content = review_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")

    assert "Portfolio site handoff review" in content
    assert "review-only gate" in content
    assert "svy04.github.io" in content
    assert "existing NoiseProof proof artifact" in content
    assert "do not edit the portfolio site" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "portfolio site NoiseProof proof artifact refresh v0" in content
    assert "portfolio site handoff review v0" in goal
    assert "Portfolio site handoff review v0: implemented" in readme


def test_portfolio_site_proof_artifact_route_verification_records_live_surface_boundary():
    review_path = REPO_ROOT / "docs/review/portfolio-site-proof-artifact-route-verification.md"
    assert review_path.is_file()
    content = review_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    proof_path = (REPO_ROOT / "docs/review/external-reader-proof-path.md").read_text(
        encoding="utf-8"
    )

    assert "Portfolio Site Proof Artifact Route Verification" in content
    assert "portfolio site proof artifact route verification v0" in content
    assert "https://svy04.github.io/proof-artifacts/noiseproof-agent-phase-ladder-2026-05-30/" in content
    assert "6e8a607" in content
    assert "35319ac" in content
    assert "182 passed, 1 warning" in content
    assert "HasOldTitle" in content
    assert "false" in content
    assert "not hosted deployment evidence" in content
    assert "not automatic failure-case creation" in content
    assert "not complete workflow failure causality" in content
    assert "external reviewer feedback or demo transcript capture v0" in content
    assert "Portfolio site proof artifact route verification v0: implemented" in readme
    assert "portfolio site proof artifact route verification v0" in goal
    assert "docs/review/portfolio-site-proof-artifact-route-verification.md" in portfolio
    assert "docs/review/portfolio-site-proof-artifact-route-verification.md" in proof_path


def test_demo_transcript_capture_records_reader_facing_route_walkthrough_boundary():
    review_path = REPO_ROOT / "docs/review/demo-transcript-capture.md"
    assert review_path.is_file()
    content = review_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    proof_path = (REPO_ROOT / "docs/review/external-reader-proof-path.md").read_text(
        encoding="utf-8"
    )

    assert "Demo Transcript Capture" in content
    assert "demo transcript capture v0" in content
    assert "POST /collection-plans/preview" in content
    assert "POST /workflow-runs/execute-preview" in content
    assert "GET /workflow-runs/{id}/lineage" in content
    assert "GET /ops/dashboard" in content
    assert "deterministic_preview_only" in content
    assert "user_intent_check" in content
    assert "not external reviewer feedback" in content
    assert "not hosted deployment evidence" in content
    assert "not customer validation" in content
    assert "not semantic retrieval" in content
    assert "external reviewer feedback v0" in content
    assert "Demo transcript capture v0: implemented" in readme
    assert "demo transcript capture v0" in goal
    assert "docs/review/demo-transcript-capture.md" in portfolio
    assert "docs/review/demo-transcript-capture.md" in proof_path


def test_local_browser_screenshot_walkthrough_records_visual_dashboard_boundary():
    review_path = REPO_ROOT / "docs/review/local-browser-screenshot-walkthrough.md"
    screenshot_path = REPO_ROOT / "docs/review/media/local-browser-dashboard-walkthrough.png"
    assert review_path.is_file()
    assert screenshot_path.is_file()
    assert screenshot_path.stat().st_size > 10_000

    content = review_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    proof_path = (REPO_ROOT / "docs/review/external-reader-proof-path.md").read_text(
        encoding="utf-8"
    )

    assert "Local Browser Screenshot Walkthrough" in content
    assert "local browser screenshot walkthrough v0" in content
    assert "docs/review/media/local-browser-dashboard-walkthrough.png" in content
    assert "GET /ops/dashboard" in content
    assert "GET /workflow-runs/{id}/lineage" in content
    assert "contains_lineage_link: true" in content
    assert "not hosted deployment evidence" in content
    assert "not customer validation" in content
    assert "not external reviewer feedback" in content
    assert "not production observability" in content
    assert "external reviewer feedback v0" in content
    assert "Local browser screenshot walkthrough v0: implemented" in readme
    assert "local browser screenshot walkthrough v0" in goal
    assert "Local browser screenshot walkthrough" in runbook
    assert "docs/review/media/local-browser-dashboard-walkthrough.png" in runbook
    assert "docs/review/local-browser-screenshot-walkthrough.md" in portfolio
    assert "docs/review/local-browser-screenshot-walkthrough.md" in proof_path


def test_external_review_request_packet_prepares_feedback_without_claiming_it():
    request_path = REPO_ROOT / "docs/review/external-review-request.md"
    issue_template_path = (
        REPO_ROOT / ".github/ISSUE_TEMPLATE/external-review-feedback.md"
    )
    assert request_path.is_file()
    assert issue_template_path.is_file()

    content = request_path.read_text(encoding="utf-8")
    issue_template = issue_template_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    proof_path = (REPO_ROOT / "docs/review/external-reader-proof-path.md").read_text(
        encoding="utf-8"
    )

    assert "External Review Request" in content
    assert "external review request packet v0" in content
    assert "docs/review/external-reader-proof-path.md" in content
    assert "docs/review/local-browser-screenshot-walkthrough.md" in content
    assert "What would make this portfolio stronger?" in content
    assert "What claim feels over-stated?" in content
    assert "What is missing before you would trust this?" in content
    assert "not external reviewer feedback" in content
    assert "not customer validation" in content
    assert "not Braincrew acceptance" in content
    assert "external reviewer feedback v0" in content
    assert "https://github.com/svy04/noiseproof-agent/issues/1" in content
    assert "Reviewer role" in issue_template
    assert "Evidence inspected" in issue_template
    assert "Feedback" in issue_template
    assert "Claim boundary" in issue_template
    assert "External review request packet v0: implemented" in readme
    assert "external review request packet v0" in goal
    assert "external review request packet v0" in runbook
    assert "https://github.com/svy04/noiseproof-agent/issues/1" in goal
    assert "https://github.com/svy04/noiseproof-agent/issues/1" in runbook
    assert "docs/review/external-review-request.md" in portfolio
    assert "docs/review/external-review-request.md" in proof_path
    assert "https://github.com/svy04/noiseproof-agent/issues/1" in portfolio
    assert "https://github.com/svy04/noiseproof-agent/issues/1" in proof_path


def test_external_review_issue_template_link_map_refresh_keeps_template_current():
    refresh_path = REPO_ROOT / "docs/review/external-review-issue-template-link-map-refresh.md"
    issue_template_path = (
        REPO_ROOT / ".github/ISSUE_TEMPLATE/external-review-feedback.md"
    )
    assert refresh_path.is_file()
    assert issue_template_path.is_file()

    content = refresh_path.read_text(encoding="utf-8")
    issue_template = issue_template_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    request = (REPO_ROOT / "docs/review/external-review-request.md").read_text(
        encoding="utf-8"
    )
    issue_body_verification = (
        REPO_ROOT / "docs/review/external-review-issue-body-link-map-verification.md"
    ).read_text(encoding="utf-8")

    link_map_url = (
        "https://github.com/svy04/noiseproof-agent/blob/main/"
        "docs/review/external-reviewer-link-map.md"
    )
    readme_url = "https://github.com/svy04/noiseproof-agent/blob/main/README.md"

    assert "External Review Issue Template Link-map Refresh" in content
    assert "external review issue template link-map refresh v0" in content
    assert link_map_url in content
    assert readme_url in content
    assert "not external reviewer feedback" in content
    assert link_map_url in issue_template
    assert readme_url in issue_template
    assert "https://github.com/svy04/noiseproof-agent/issues/1" in issue_template
    assert "`docs/review/external-reviewer-link-map.md`" not in issue_template
    assert "External review issue template link-map refresh v0: implemented" in readme
    assert "external review issue template link-map refresh v0" in goal
    assert "external review issue template link-map refresh v0" in runbook
    assert "docs/review/external-review-issue-template-link-map-refresh.md" in portfolio
    assert "docs/review/external-review-issue-template-link-map-refresh.md" in request
    assert (
        "docs/review/external-review-issue-template-link-map-refresh.md"
        in issue_body_verification
    )


def test_external_feedback_intake_criteria_blocks_self_authored_proof():
    criteria_path = REPO_ROOT / "docs/review/external-feedback-intake-criteria.md"
    assert criteria_path.is_file()

    content = criteria_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    request = (REPO_ROOT / "docs/review/external-review-request.md").read_text(
        encoding="utf-8"
    )

    assert "External Feedback Intake Criteria" in content
    assert "external feedback intake criteria v0" in content
    assert "https://github.com/svy04/noiseproof-agent/issues/1" in content
    assert "qualifying feedback" in content
    assert "non-qualifying feedback" in content
    assert "reviewer is not the repository owner" in content
    assert "specific artifact inspected" in content
    assert "actionable critique" in content
    assert "self-authored comment" in content
    assert "request for feedback" in content
    assert "empty acknowledgement" in content
    assert "External reviewer feedback remains pending" in content
    assert "not external reviewer feedback" in content
    assert "External feedback intake criteria v0: implemented" in readme
    assert "external feedback intake criteria v0" in goal
    assert "external feedback intake criteria v0" in runbook
    assert "docs/review/external-feedback-intake-criteria.md" in portfolio
    assert "docs/review/external-feedback-intake-criteria.md" in request


def test_external_reviewer_brief_gives_two_minute_path_without_claiming_feedback():
    brief_path = REPO_ROOT / "docs/review/external-reviewer-brief.md"
    assert brief_path.is_file()

    content = brief_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    proof_path = (REPO_ROOT / "docs/review/external-reader-proof-path.md").read_text(
        encoding="utf-8"
    )
    request = (REPO_ROOT / "docs/review/external-review-request.md").read_text(
        encoding="utf-8"
    )

    assert "External Reviewer Brief" in content
    assert "external reviewer brief v0" in content
    assert "2-minute path" in content
    assert "What this currently proves" in content
    assert "What this does not prove" in content
    assert "What I want reviewed" in content
    assert "https://github.com/svy04/noiseproof-agent/issues/1" in content
    assert "docs/review/external-feedback-intake-criteria.md" in content
    assert "not external reviewer feedback" in content
    assert "External reviewer feedback remains pending" in content
    assert "External reviewer brief v0: implemented" in readme
    assert "external reviewer brief v0" in goal
    assert "external reviewer brief v0" in runbook
    assert "docs/review/external-reviewer-brief.md" in portfolio
    assert "docs/review/external-reviewer-brief.md" in proof_path
    assert "docs/review/external-reviewer-brief.md" in request


def test_external_reviewer_live_proof_route_refresh_links_public_artifact_without_claiming_feedback():
    refresh_path = REPO_ROOT / "docs/review/external-reviewer-live-proof-route-refresh.md"
    assert refresh_path.is_file()

    content = refresh_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    proof_path = (REPO_ROOT / "docs/review/external-reader-proof-path.md").read_text(
        encoding="utf-8"
    )
    brief = (REPO_ROOT / "docs/review/external-reviewer-brief.md").read_text(
        encoding="utf-8"
    )

    live_route = (
        "https://svy04.github.io/proof-artifacts/"
        "noiseproof-live-route-verification-2026-06-01/"
    )
    assert "External Reviewer Live Proof Route Refresh" in content
    assert "external reviewer live proof route refresh v0" in content
    assert live_route in content
    assert "39ab5e4" in content
    assert "71c6062" in content
    assert "3dfe5e4" in content
    assert "26720601344" in content
    assert "not external reviewer feedback" in content
    assert "not hosted deployment evidence" in content
    assert "external reviewer feedback v0" in content
    assert "External reviewer live proof route refresh v0: implemented" in readme
    assert "external reviewer live proof route refresh v0" in goal
    assert "external reviewer live proof route refresh v0" in runbook
    assert "docs/review/external-reviewer-live-proof-route-refresh.md" in portfolio
    assert "docs/review/external-reviewer-live-proof-route-refresh.md" in proof_path
    assert live_route in portfolio
    assert live_route in proof_path
    assert live_route in brief


def test_external_reviewer_outreach_packet_prepares_human_request_without_claiming_feedback():
    outreach_path = REPO_ROOT / "docs/review/external-reviewer-outreach-packet.md"
    assert outreach_path.is_file()

    content = outreach_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    proof_path = (REPO_ROOT / "docs/review/external-reader-proof-path.md").read_text(
        encoding="utf-8"
    )
    request = (REPO_ROOT / "docs/review/external-review-request.md").read_text(
        encoding="utf-8"
    )

    assert "External Reviewer Outreach Packet" in content
    assert "external reviewer outreach packet v0" in content
    assert "Copy-paste outreach messages" in content
    assert "FDE / product engineer reviewer" in content
    assert "RAG / data engineer reviewer" in content
    assert "founder / operator reviewer" in content
    assert "https://github.com/svy04/noiseproof-agent/issues/1" in content
    assert "docs/review/external-reviewer-brief.md" in content
    assert "docs/review/external-feedback-intake-criteria.md" in content
    assert "not external reviewer feedback" in content
    assert "external reviewer feedback v0" in content
    assert "External reviewer outreach packet v0: implemented" in readme
    assert "external reviewer outreach packet v0" in goal
    assert "external reviewer outreach packet v0" in runbook
    assert "docs/review/external-reviewer-outreach-packet.md" in portfolio
    assert "docs/review/external-reviewer-outreach-packet.md" in proof_path
    assert "docs/review/external-reviewer-outreach-packet.md" in request


def test_external_feedback_qualification_preview_screens_comments_without_closing_gate():
    preview_path = REPO_ROOT / "docs/review/external-feedback-qualification-preview.md"
    assert preview_path.is_file()

    content = preview_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    criteria = (REPO_ROOT / "docs/review/external-feedback-intake-criteria.md").read_text(
        encoding="utf-8"
    )

    assert "External Feedback Qualification Preview" in content
    assert "external feedback qualification preview v0" in content
    assert "packages/review/external_feedback.py" in content
    assert "candidate_found_manual_review_required" in content
    assert "does not close the gate" in content
    assert "not external reviewer feedback" in content
    assert "external reviewer feedback v0" in content
    assert "External feedback qualification preview v0: implemented" in readme
    assert "external feedback qualification preview v0" in goal
    assert "external feedback qualification preview v0" in runbook
    assert "docs/review/external-feedback-qualification-preview.md" in portfolio
    assert "docs/review/external-feedback-qualification-preview.md" in criteria


def test_external_feedback_screening_cli_documents_real_issue_json_path_without_closing_gate():
    cli_path = REPO_ROOT / "docs/review/external-feedback-screening-cli.md"
    assert cli_path.is_file()

    content = cli_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    preview = (
        REPO_ROOT / "docs/review/external-feedback-qualification-preview.md"
    ).read_text(encoding="utf-8")

    assert "External Feedback Screening CLI" in content
    assert "external feedback screening cli v0" in content
    assert "python -m packages.review.external_feedback_cli" in content
    assert "gh issue view 1 --repo svy04/noiseproof-agent --json comments" in content
    assert "comment_count: 0" in content
    assert "pending" in content
    assert "does not close the gate" in content
    assert "not external reviewer feedback" in content
    assert "External feedback screening CLI v0: implemented" in readme
    assert "external feedback screening cli v0" in goal
    assert "external feedback screening cli v0" in runbook
    assert "docs/review/external-feedback-screening-cli.md" in portfolio
    assert "docs/review/external-feedback-screening-cli.md" in preview


def test_external_feedback_screening_workflow_runs_cli_without_closing_gate():
    workflow_path = REPO_ROOT / ".github/workflows/external-feedback-screen.yml"
    review_path = REPO_ROOT / "docs/review/external-feedback-screening-workflow.md"
    assert workflow_path.is_file()
    assert review_path.is_file()

    workflow = workflow_path.read_text(encoding="utf-8")
    content = review_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    cli_doc = (REPO_ROOT / "docs/review/external-feedback-screening-cli.md").read_text(
        encoding="utf-8"
    )

    assert "External Feedback Screen" in workflow
    assert "workflow_dispatch:" in workflow
    assert "issue_comment:" in workflow
    assert "issues: read" in workflow
    assert "gh issue view 1" in workflow
    assert "python -m packages.review.external_feedback_cli" in workflow
    assert "external-feedback-screen.json" in workflow
    assert "actions/upload-artifact@v4" in workflow
    assert "External Feedback Screening Workflow" in content
    assert "external feedback screening workflow v0" in content
    assert "does not close the gate" in content
    assert "not external reviewer feedback" in content
    assert "external reviewer feedback v0" in content
    assert "External feedback screening workflow v0: implemented" in readme
    assert "external feedback screening workflow v0" in goal
    assert "external feedback screening workflow v0" in runbook
    assert "docs/review/external-feedback-screening-workflow.md" in portfolio
    assert "docs/review/external-feedback-screening-workflow.md" in cli_doc


def test_external_feedback_screening_workflow_uploads_acceptance_draft_without_accepting_feedback():
    workflow_path = REPO_ROOT / ".github/workflows/external-feedback-screen.yml"
    workflow_doc_path = REPO_ROOT / "docs/review/external-feedback-screening-workflow.md"
    draft_cli_doc_path = (
        REPO_ROOT / "docs/review/external-feedback-acceptance-draft-cli.md"
    )
    assert workflow_path.is_file()
    assert workflow_doc_path.is_file()
    assert draft_cli_doc_path.is_file()

    workflow = workflow_path.read_text(encoding="utf-8")
    workflow_doc = workflow_doc_path.read_text(encoding="utf-8")
    draft_cli_doc = draft_cli_doc_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )

    assert "python -m packages.review.external_feedback_acceptance_cli" in workflow
    assert "external-feedback-acceptance-draft.json" in workflow
    assert "name: external-feedback-acceptance-draft" in workflow
    assert "external feedback acceptance draft workflow v0" in workflow_doc
    assert "external-feedback-acceptance-draft.json" in workflow_doc
    assert "does not close the gate" in workflow_doc
    assert "not external reviewer feedback" in workflow_doc
    assert "external-feedback-acceptance-draft.json" in draft_cli_doc
    assert "External feedback acceptance draft workflow v0: implemented" in readme
    assert "external feedback acceptance draft workflow v0" in goal
    assert "external feedback acceptance draft workflow v0" in runbook
    assert "external feedback acceptance draft workflow" in portfolio


def test_external_feedback_screening_workflow_artifact_verification_records_remote_pending_result():
    verification_path = (
        REPO_ROOT / "docs/review/external-feedback-screening-workflow-verification.md"
    )
    assert verification_path.is_file()

    content = verification_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    workflow_doc = (
        REPO_ROOT / "docs/review/external-feedback-screening-workflow.md"
    ).read_text(encoding="utf-8")

    assert "External Feedback Screening Workflow Verification" in content
    assert "external feedback screening workflow verification v0" in content
    assert "26724730074" in content
    assert "external-feedback-screen.json" in content
    assert '"status": "pending"' in content
    assert '"candidate_count": 0' in content
    assert "does not close the gate" in content
    assert "not external reviewer feedback" in content
    assert "External feedback screening workflow verification v0: implemented" in readme
    assert "external feedback screening workflow verification v0" in goal
    assert "external feedback screening workflow verification v0" in runbook
    assert (
        "docs/review/external-feedback-screening-workflow-verification.md"
        in portfolio
    )
    assert (
        "docs/review/external-feedback-screening-workflow-verification.md"
        in workflow_doc
    )


def test_external_feedback_acceptance_draft_workflow_verification_records_remote_pending_result():
    verification_path = (
        REPO_ROOT
        / "docs/review/external-feedback-acceptance-draft-workflow-verification.md"
    )
    assert verification_path.is_file()

    content = verification_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    workflow_doc = (
        REPO_ROOT / "docs/review/external-feedback-screening-workflow.md"
    ).read_text(encoding="utf-8")
    draft_cli_doc = (
        REPO_ROOT / "docs/review/external-feedback-acceptance-draft-cli.md"
    ).read_text(encoding="utf-8")

    assert "External Feedback Acceptance Draft Workflow Verification" in content
    assert "external feedback acceptance draft workflow verification v0" in content
    assert "26727047243" in content
    assert "62a21c2099813570c6475e9547e4609dd046d795" in content
    assert "external-feedback-screen.json" in content
    assert "external-feedback-acceptance-draft.json" in content
    assert '"status": "pending"' in content
    assert '"candidate_count": 0' in content
    assert '"draft_count": 0' in content
    assert "does not close the gate" in content
    assert "not external reviewer feedback" in content
    assert (
        "External feedback acceptance draft workflow verification v0: implemented"
        in readme
    )
    assert "external feedback acceptance draft workflow verification v0" in goal
    assert "external feedback acceptance draft workflow verification v0" in runbook
    assert (
        "docs/review/external-feedback-acceptance-draft-workflow-verification.md"
        in portfolio
    )
    assert (
        "docs/review/external-feedback-acceptance-draft-workflow-verification.md"
        in workflow_doc
    )
    assert (
        "docs/review/external-feedback-acceptance-draft-workflow-verification.md"
        in draft_cli_doc
    )


def test_external_reviewer_link_map_reduces_review_friction_without_claiming_feedback():
    link_map_path = REPO_ROOT / "docs/review/external-reviewer-link-map.md"
    assert link_map_path.is_file()

    content = link_map_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    request = (REPO_ROOT / "docs/review/external-review-request.md").read_text(
        encoding="utf-8"
    )
    brief = (REPO_ROOT / "docs/review/external-reviewer-brief.md").read_text(
        encoding="utf-8"
    )
    outreach = (REPO_ROOT / "docs/review/external-reviewer-outreach-packet.md").read_text(
        encoding="utf-8"
    )

    issue_url = "https://github.com/svy04/noiseproof-agent/issues/1"
    readme_url = "https://github.com/svy04/noiseproof-agent/blob/main/README.md"
    proof_path_url = (
        "https://github.com/svy04/noiseproof-agent/blob/main/"
        "docs/review/external-reader-proof-path.md"
    )
    portfolio_url = (
        "https://github.com/svy04/noiseproof-agent/blob/main/"
        "docs/application/portfolio-index.md"
    )
    brief_url = (
        "https://github.com/svy04/noiseproof-agent/blob/main/"
        "docs/review/external-reviewer-brief.md"
    )

    assert "External Reviewer Link Map" in content
    assert "external reviewer link map v0" in content
    assert issue_url in content
    assert readme_url in content
    assert proof_path_url in content
    assert portfolio_url in content
    assert brief_url in content
    assert "not external reviewer feedback" in content
    assert "external reviewer feedback v0" in content
    assert "External reviewer link map v0: implemented" in readme
    assert "external reviewer link map v0" in goal
    assert "external reviewer link map v0" in runbook
    assert "docs/review/external-reviewer-link-map.md" in portfolio
    assert "docs/review/external-reviewer-link-map.md" in request
    assert "docs/review/external-reviewer-link-map.md" in brief
    assert "docs/review/external-reviewer-link-map.md" in outreach


def test_external_review_issue_body_link_map_verification_records_remote_request_surface():
    verification_path = (
        REPO_ROOT / "docs/review/external-review-issue-body-link-map-verification.md"
    )
    assert verification_path.is_file()

    content = verification_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    request = (REPO_ROOT / "docs/review/external-review-request.md").read_text(
        encoding="utf-8"
    )
    link_map = (REPO_ROOT / "docs/review/external-reviewer-link-map.md").read_text(
        encoding="utf-8"
    )

    assert "External Review Issue Body Link-map Verification" in content
    assert "external review issue body link-map verification v0" in content
    assert "https://github.com/svy04/noiseproof-agent/issues/1" in content
    assert "external-reviewer-link-map.md" in content
    assert "blob/main/README.md" in content
    assert '"comment_count": 0' in content
    assert '"starts_with_request": true' in content
    assert '"has_link_map": true' in content
    assert '"has_direct_readme": true' in content
    assert "not external reviewer feedback" in content
    assert "External review issue body link-map verification v0: implemented" in readme
    assert "external review issue body link-map verification v0" in goal
    assert "external review issue body link-map verification v0" in runbook
    assert "docs/review/external-review-issue-body-link-map-verification.md" in portfolio
    assert "docs/review/external-review-issue-body-link-map-verification.md" in request
    assert "docs/review/external-review-issue-body-link-map-verification.md" in link_map


def test_external_review_issue_label_verification_records_remote_triage_surface():
    verification_path = (
        REPO_ROOT / "docs/review/external-review-issue-label-verification.md"
    )
    assert verification_path.is_file()

    content = verification_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    request = (REPO_ROOT / "docs/review/external-review-request.md").read_text(
        encoding="utf-8"
    )
    body_verification = (
        REPO_ROOT / "docs/review/external-review-issue-body-link-map-verification.md"
    ).read_text(encoding="utf-8")

    assert "External Review Issue Label Verification" in content
    assert "external review issue label verification v0" in content
    assert "https://github.com/svy04/noiseproof-agent/issues/1" in content
    assert '"state": "OPEN"' in content
    assert '"comment_count": 0' in content
    assert '"external-review"' in content
    assert '"feedback"' in content
    assert "not external reviewer feedback" in content
    assert "External review issue label verification v0: implemented" in readme
    assert "external review issue label verification v0" in goal
    assert "external review issue label verification v0" in runbook
    assert "docs/review/external-review-issue-label-verification.md" in portfolio
    assert "docs/review/external-review-issue-label-verification.md" in request
    assert "docs/review/external-review-issue-label-verification.md" in body_verification


def test_external_review_owner_request_comment_verification_records_self_authored_rejection():
    verification_path = (
        REPO_ROOT
        / "docs/review/external-review-owner-request-comment-verification.md"
    )
    assert verification_path.is_file()

    content = verification_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    criteria = (
        REPO_ROOT / "docs/review/external-feedback-intake-criteria.md"
    ).read_text(encoding="utf-8")
    label_verification = (
        REPO_ROOT / "docs/review/external-review-issue-label-verification.md"
    ).read_text(encoding="utf-8")

    assert "External Review Owner Request Comment Verification" in content
    assert "external review owner request comment verification v0" in content
    assert "https://github.com/svy04/noiseproof-agent/issues/1#issuecomment-" in content
    assert '"status": "pending"' in content
    assert '"candidate_count": 0' in content
    assert '"draft_count": 0' in content
    assert "self_authored_comment" in content
    assert "non_qualifying" in content
    assert "not external reviewer feedback" in content
    assert (
        "External review owner request comment verification v0: implemented"
        in readme
    )
    assert "external review owner request comment verification v0" in goal
    assert "external review owner request comment verification v0" in runbook
    assert (
        "docs/review/external-review-owner-request-comment-verification.md"
        in portfolio
    )
    assert (
        "docs/review/external-review-owner-request-comment-verification.md"
        in criteria
    )
    assert (
        "docs/review/external-review-owner-request-comment-verification.md"
        in label_verification
    )


def test_external_review_root_guide_reduces_github_entry_friction_without_claiming_feedback():
    contributing_path = REPO_ROOT / "CONTRIBUTING.md"
    guide_path = REPO_ROOT / "docs/review/external-review-root-guide.md"
    assert contributing_path.is_file()
    assert guide_path.is_file()

    contributing = contributing_path.read_text(encoding="utf-8")
    guide = guide_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    request = (REPO_ROOT / "docs/review/external-review-request.md").read_text(
        encoding="utf-8"
    )
    link_map = (REPO_ROOT / "docs/review/external-reviewer-link-map.md").read_text(
        encoding="utf-8"
    )
    issue_template = (
        REPO_ROOT / ".github/ISSUE_TEMPLATE/external-review-feedback.md"
    ).read_text(encoding="utf-8")

    assert "External Review Guide" in contributing
    assert "https://github.com/svy04/noiseproof-agent/issues/1" in contributing
    assert "docs/review/external-reader-proof-path.md" in contributing
    assert "docs/review/external-feedback-intake-criteria.md" in contributing
    assert "external reviewer feedback v0" in contributing
    assert "not external reviewer feedback" in contributing
    assert "External Review Root Guide" in guide
    assert "external review root guide v0" in guide
    assert "CONTRIBUTING.md" in guide
    assert "not external reviewer feedback" in guide
    assert "External review root guide v0: implemented" in readme
    assert "external review root guide v0" in goal
    assert "external review root guide v0" in runbook
    assert "docs/review/external-review-root-guide.md" in portfolio
    assert "CONTRIBUTING.md" in request
    assert "CONTRIBUTING.md" in link_map
    assert "CONTRIBUTING.md" in issue_template


def test_readme_next_gate_matches_external_feedback_state_without_stale_phase_claim():
    refresh_path = REPO_ROOT / "docs/review/readme-next-gate-stale-claim-refresh.md"
    assert refresh_path.is_file()

    content = refresh_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )

    assert "README Next-gate Stale-claim Refresh" in content
    assert "readme next-gate stale-claim refresh v0" in content
    assert "external reviewer feedback v0" in content
    assert "not external reviewer feedback" in content
    assert "What I Would Improve Next" in readme
    assert "external reviewer feedback v0" in readme
    assert "issue #1" in readme
    assert "External review request packet v0: implemented" in readme
    assert "After Workflow Lineage Warning Code Dashboard Surfacing v0" not in readme
    assert "README next-gate stale-claim refresh v0" in readme
    assert "readme next-gate stale-claim refresh v0" in goal
    assert "readme next-gate stale-claim refresh v0" in runbook
    assert "docs/review/readme-next-gate-stale-claim-refresh.md" in portfolio


def test_external_feedback_acceptance_template_exists_without_claiming_feedback():
    template_path = REPO_ROOT / "docs/review/external-feedback-acceptance-template.md"
    assert template_path.is_file()

    content = template_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    criteria = (REPO_ROOT / "docs/review/external-feedback-intake-criteria.md").read_text(
        encoding="utf-8"
    )

    assert "External Feedback Acceptance Template" in content
    assert "external feedback acceptance template v0" in content
    assert "Reviewer identity" in content
    assert "Inspected evidence" in content
    assert "Accepted critique" in content
    assert "Manual acceptance decision" in content
    assert "not external reviewer feedback" in content
    assert "External feedback acceptance template v0: implemented" in readme
    assert "external feedback acceptance template v0" in goal
    assert "external feedback acceptance template v0" in runbook
    assert "docs/review/external-feedback-acceptance-template.md" in portfolio
    assert "docs/review/external-feedback-acceptance-template.md" in criteria


def test_external_feedback_acceptance_draft_cli_is_documented_without_accepting_feedback():
    draft_cli_path = REPO_ROOT / "docs/review/external-feedback-acceptance-draft-cli.md"
    assert draft_cli_path.is_file()

    content = draft_cli_path.read_text(encoding="utf-8")
    readme = readme_with_proof_marker_archive()
    goal = (REPO_ROOT / "docs/GOAL.md").read_text(encoding="utf-8")
    runbook = (REPO_ROOT / "docs/runbook.md").read_text(encoding="utf-8")
    portfolio = (REPO_ROOT / "docs/application/portfolio-index.md").read_text(
        encoding="utf-8"
    )
    template = (
        REPO_ROOT / "docs/review/external-feedback-acceptance-template.md"
    ).read_text(encoding="utf-8")

    assert "External Feedback Acceptance Draft CLI" in content
    assert "external feedback acceptance draft cli v0" in content
    assert "python -m packages.review.external_feedback_acceptance_cli" in content
    assert "manual_acceptance_required" in content
    assert "does not close the gate" in content
    assert "not external reviewer feedback" in content
    assert "External feedback acceptance draft CLI v0: implemented" in readme
    assert "external feedback acceptance draft cli v0" in goal
    assert "external feedback acceptance draft cli v0" in runbook
    assert "docs/review/external-feedback-acceptance-draft-cli.md" in portfolio
    assert "docs/review/external-feedback-acceptance-draft-cli.md" in template
