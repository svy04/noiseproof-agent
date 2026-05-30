# Workflow Lineage Read Model Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a derived `GET /workflow-runs/{id}/lineage` read model over existing workflow child records and `stage_input_manifest` values.

**Architecture:** The read model must not add storage. It resolves persisted Evidence Ledger and Noise Gate records referenced by existing manifests and returns missing-reference warnings instead of claiming strict FK lineage.

**Tech Stack:** FastAPI, Pydantic schemas, existing repository child lookup, pytest.

---

### Task 1: Route Test

**Files:**
- Modify: `apps/api/tests/test_routes.py`

- [x] **Step 1: Write the failing route test**

Add a test that creates a deterministic workflow through `POST /workflow-runs/execute-preview`, calls `GET /workflow-runs/{id}/lineage`, and asserts the response is a derived read model with resolved evidence and gate records.

- [x] **Step 2: Verify RED**

Run:

```bash
cd apps/api
uv run pytest tests/test_routes.py::test_workflow_run_lineage_read_model_resolves_manifest_inputs_without_new_storage -q
```

Expected: fail with 404 or missing route.

### Task 2: Minimal Implementation

**Files:**
- Modify: `apps/api/app/schemas.py`
- Modify: `apps/api/app/routes/workflow_runs.py`

- [x] **Step 1: Add schemas**

Add Pydantic output models for gate lineage, report lineage, summary, and full workflow lineage.

- [x] **Step 2: Add route**

Add `GET /workflow-runs/{workflow_run_id}/lineage`. Build it from `repository.get_workflow_run()` and `repository.lookup_workflow_run_records()` only.

- [x] **Step 3: Verify GREEN**

Run the focused route test again. Expected: pass.

### Task 3: Documentation

**Files:**
- Modify: `README.md`
- Modify: `apps/api/README.md`
- Modify: `docs/GOAL.md`
- Modify: `docs/runbook.md`
- Modify: `docs/architecture.md`
- Modify: `docs/application/portfolio-index.md`
- Modify: `docs/review/application-ready-review.md`
- Modify: `docs/review/direct-cross-stage-link-schema-review.md`

- [x] **Step 1: Mark Phase 32 as accepted**

Document `Workflow Lineage Read Model v0` and keep the boundary explicit: no new storage, no join tables, no direct FK lineage.

- [x] **Step 2: Add runbook smoke command**

Document `curl http://localhost:8000/workflow-runs/<uuid>/lineage`.

### Task 4: Verification and Commit

**Files:**
- All modified files above.

- [x] **Step 1: Run full verification**

Run:

```bash
cd apps/api
uv run pytest -q
uv run python -m compileall app ../../packages/ingestion
cd ../..
docker compose config --quiet
git diff --check
```

- [x] **Step 2: Run DB smoke**

Use Docker/Postgres to create a deterministic workflow and call `GET /workflow-runs/{id}/lineage`.

- [ ] **Step 3: Commit and push**

Run:

```bash
git add .
git commit -m "feat: add workflow lineage read model"
git push origin main
```
