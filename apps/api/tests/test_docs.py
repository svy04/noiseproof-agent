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
