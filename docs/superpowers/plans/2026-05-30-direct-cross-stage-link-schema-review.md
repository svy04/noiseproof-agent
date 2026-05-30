# Direct Cross-stage Link Schema Review Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Add a Phase 31.5 review-only gate that decides whether Phase 31's stage input manifests justify direct cross-stage schema links.

**Architecture:** This gate adds no runtime behavior, migrations, or endpoints. It creates a review artifact, updates continuation/source-of-truth docs, and adds tests that keep the boundary explicit.

**Tech Stack:** Markdown documentation, pytest doc checks, existing FastAPI project verification commands.

---

### Task 1: Add Review Test

**Files:**
- Modify: `apps/api/tests/test_docs.py`
- Create later: `docs/review/direct-cross-stage-link-schema-review.md`

- [x] **Step 1: Write the failing test**

Add a test that reads `docs/review/direct-cross-stage-link-schema-review.md` and asserts the review is a review-only gate, references Phase 31, mentions `stage_input_manifest`, defers direct foreign-key links and join tables, and points to `Workflow lineage read model v0`.

- [x] **Step 2: Run the test to verify it fails**

Run:

```bash
cd apps/api
uv run pytest tests/test_docs.py::test_direct_cross_stage_link_schema_review_defers_schema_and_points_to_read_model -q
```

Expected result: fail because `docs/review/direct-cross-stage-link-schema-review.md` does not exist.

### Task 2: Add Review Artifact

**Files:**
- Create: `docs/review/direct-cross-stage-link-schema-review.md`

- [x] **Step 1: Create the review document**

The document must state:

- Phase 31 added local `stage_input_manifest` values.
- The manifest is enough for local deterministic stage input provenance.
- The manifest is not enough for strict relational lineage.
- Direct evidence -> gate -> report foreign-key links are not added in this review gate.
- Join tables are not added in this review gate.
- The next safer implementation is a derived workflow lineage read model.

- [x] **Step 2: Run the focused doc test**

Run:

```bash
cd apps/api
uv run pytest tests/test_docs.py::test_direct_cross_stage_link_schema_review_defers_schema_and_points_to_read_model -q
```

Expected result: pass.

### Task 3: Update Source-of-truth Docs

**Files:**
- Modify: `docs/GOAL.md`
- Modify: `README.md`
- Modify: `docs/runbook.md`
- Modify: `docs/architecture.md`
- Modify: `docs/application/portfolio-index.md`
- Modify: `docs/review/application-ready-review.md`

- [x] **Step 1: Mark Phase 31.5 as accepted**

Update accepted state and phase ladder to include `Direct Cross-stage Link Schema Review v0`.

- [x] **Step 2: Preserve boundaries**

State that the review did not add migrations, endpoints, foreign-key links, join tables, LLM calls, embeddings, or dashboard polish.

- [x] **Step 3: Set next gate**

Set the next recommended implementation gate to `Workflow lineage read model v0`.

### Task 4: Verify and Commit

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

Expected result: all commands exit 0. Known CRLF warnings from git are acceptable when exit code remains 0.

- [ ] **Step 2: Commit and push**

Run:

```bash
git add apps/api/tests/test_docs.py docs README.md
git commit -m "docs: review direct cross-stage link schema"
git push origin main
gh run list --repo svy04/noiseproof-agent --branch main --limit 6 --json databaseId,headSha,status,conclusion,displayTitle,workflowName,createdAt
```

Expected result: pushed commit has a successful CI run.
