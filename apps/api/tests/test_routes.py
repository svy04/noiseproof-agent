from datetime import date, datetime, timezone
from hashlib import sha256
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

from app.db import get_repository
from app.main import create_app
from app.schemas import AgentRunCreate, DocumentCreate, FailureCaseCreate, OpsSummaryOut
from app.services.run_trace import run_with_trace

WORKFLOW_VERSION = "phase40-lineage-warning-code-dashboard"


class InMemoryRepository:
    def __init__(self):
        self.documents = []
        self.document_chunks = []
        self.agent_runs = []
        self.evidence_ledger_entries = []
        self.failure_cases = []
        self.noise_gate_records = []
        self.report_records = []
        self.retrieval_runs = []
        self.workflow_runs = []
        self.uploaded_file_intake_manifests = []
        self.uploaded_raw_files = []
        self.chunk_embeddings = []

    def create_document(self, payload: DocumentCreate) -> dict:
        row = payload.model_dump()
        row["id"] = uuid4()
        row["created_at"] = datetime.now(timezone.utc)
        self.documents.append(row)
        return row

    def list_documents(self):
        return self.documents

    def create_document_chunk(self, payload) -> dict:
        row = payload.model_dump()
        row["id"] = uuid4()
        row["created_at"] = datetime.now(timezone.utc)
        self.document_chunks.append(row)
        return row

    def list_document_chunks(self, document_id, limit=20):
        rows = [
            row
            for row in self.document_chunks
            if str(row["document_id"]) == str(document_id)
        ]
        return rows[:limit]

    def create_chunk_embedding(self, payload) -> dict:
        row = payload.model_dump()
        row["id"] = uuid4()
        row["embedding_created_at"] = datetime.now(timezone.utc)
        row["created_at"] = datetime.now(timezone.utc)
        self.chunk_embeddings.append(row)
        return row

    def list_chunk_embeddings(
        self,
        chunk_id=None,
        embedding_model=None,
        embedding_status=None,
        limit=20,
    ):
        rows = self.chunk_embeddings
        if chunk_id is not None:
            rows = [row for row in rows if str(row["chunk_id"]) == str(chunk_id)]
        if embedding_model is not None:
            rows = [row for row in rows if row["embedding_model"] == embedding_model]
        if embedding_status is not None:
            rows = [row for row in rows if row["embedding_status"] == embedding_status]
        return rows[:limit]

    def preview_semantic_retrieval_candidates(
        self,
        *,
        document_id,
        query_embedding,
        embedding_model,
        embedding_dimension,
        limit=5,
    ):
        rows = []
        for chunk in self.document_chunks:
            if str(chunk["document_id"]) != str(document_id):
                continue
            for embedding in self.chunk_embeddings:
                if str(embedding["chunk_id"]) != str(chunk["id"]):
                    continue
                if embedding["embedding_model"] != embedding_model:
                    continue
                if embedding["embedding_dimension"] != embedding_dimension:
                    continue
                if embedding["distance_metric"] != "cosine":
                    continue
                if embedding["embedding_status"] != "created":
                    continue
                if embedding.get("embedding") is None:
                    continue
                rows.append(
                    {
                        "chunk_id": chunk["id"],
                        "embedding_id": embedding["id"],
                        "document_id": chunk["document_id"],
                        "source_type": chunk["source_type"],
                        "chunk_strategy": chunk["chunk_strategy"],
                        "chunk_index": chunk["chunk_index"],
                        "chunk_text": chunk["chunk_text"],
                        "chunk_metadata_json": chunk.get("metadata_json") or {},
                        "embedding_model": embedding["embedding_model"],
                        "embedding_dimension": embedding["embedding_dimension"],
                        "distance_metric": embedding["distance_metric"],
                        "embedding_metadata_json": embedding.get("metadata_json") or {},
                        "distance": _cosine_distance(
                            query_embedding,
                            embedding["embedding"],
                        ),
                    }
                )
        return sorted(rows, key=lambda row: (row["distance"], row["chunk_index"]))[:limit]

    def create_uploaded_file_intake_manifest(self, payload) -> dict:
        row = payload.model_dump()
        row["id"] = uuid4()
        row["created_at"] = datetime.now(timezone.utc)
        self.uploaded_file_intake_manifests.append(row)
        return row

    def list_uploaded_file_intake_manifests(self, limit=20):
        return self.uploaded_file_intake_manifests[:limit]

    def create_uploaded_raw_file(self, payload) -> dict:
        row = payload.model_dump()
        row["id"] = uuid4()
        row["created_at"] = datetime.now(timezone.utc)
        self.uploaded_raw_files.append(row)
        return row

    def list_uploaded_raw_files(self, limit=20):
        return self.uploaded_raw_files[:limit]

    def create_agent_run(self, payload: AgentRunCreate) -> dict:
        row = payload.model_dump()
        row["id"] = uuid4()
        row["started_at"] = datetime.now(timezone.utc)
        row["ended_at"] = None
        self.agent_runs.append(row)
        return row

    def update_agent_run(
        self,
        agent_run_id,
        *,
        status,
        error_message,
        latency_ms,
        trace_json,
    ):
        for row in self.agent_runs:
            if row["id"] == agent_run_id:
                row["status"] = status
                row["error_message"] = error_message
                row["latency_ms"] = latency_ms
                row["trace_json"] = trace_json
                row["ended_at"] = datetime.now(timezone.utc)
                return row
        raise KeyError(f"Unknown agent run id: {agent_run_id}")

    def list_agent_runs(self):
        return self.agent_runs

    def create_evidence_ledger_entries(
        self,
        question,
        entries,
        workflow_trace_id=None,
        agent_run_id=None,
        workflow_run_id=None,
        retrieval_run_id=None,
    ):
        workflow_trace_id = workflow_trace_id or uuid4()
        created = []
        for entry in entries:
            row = entry.model_dump()
            row["id"] = uuid4()
            row["question"] = question
            row["run_id"] = agent_run_id
            row["workflow_trace_id"] = workflow_trace_id
            row["agent_run_id"] = agent_run_id
            row["workflow_run_id"] = workflow_run_id
            row["retrieval_run_id"] = retrieval_run_id
            row["created_at"] = datetime.now(timezone.utc)
            self.evidence_ledger_entries.append(row)
            created.append(row)
        return created

    def list_evidence_ledger_entries(
        self,
        workflow_trace_id=None,
        status=None,
        retrieval_run_id=None,
    ):
        rows = self.evidence_ledger_entries
        if workflow_trace_id is not None:
            rows = [
                row for row in rows if str(row["workflow_trace_id"]) == str(workflow_trace_id)
            ]
        if status is not None:
            rows = [row for row in rows if row["status"] == status]
        if retrieval_run_id is not None:
            rows = [
                row for row in rows if str(row.get("retrieval_run_id")) == str(retrieval_run_id)
            ]
        return rows

    def create_noise_gate_record(
        self,
        result,
        evidence_entry_count,
        draft_claim_count,
        workflow_trace_id=None,
        agent_run_id=None,
        workflow_run_id=None,
        stage_input_manifest=None,
    ):
        row = result.model_dump()
        row["id"] = uuid4()
        row["workflow_trace_id"] = workflow_trace_id or uuid4()
        row["agent_run_id"] = agent_run_id
        row["workflow_run_id"] = workflow_run_id
        row["stage_input_manifest"] = stage_input_manifest or {}
        row["evidence_entry_count"] = evidence_entry_count
        row["draft_claim_count"] = draft_claim_count
        row["created_at"] = datetime.now(timezone.utc)
        self.noise_gate_records.append(row)
        return row

    def list_noise_gate_records(self, workflow_trace_id=None, decision=None):
        rows = self.noise_gate_records
        if workflow_trace_id is not None:
            rows = [
                row for row in rows if str(row["workflow_trace_id"]) == str(workflow_trace_id)
            ]
        if decision is not None:
            rows = [row for row in rows if row["decision"] == decision]
        return rows

    def create_report_record(
        self,
        result,
        evidence_entry_count,
        draft_claim_count,
        workflow_trace_id=None,
        agent_run_id=None,
        workflow_run_id=None,
        stage_input_manifest=None,
    ):
        row = result.model_dump()
        row["id"] = uuid4()
        row["workflow_trace_id"] = workflow_trace_id or uuid4()
        row["agent_run_id"] = agent_run_id
        row["workflow_run_id"] = workflow_run_id
        row["stage_input_manifest"] = stage_input_manifest or {}
        row["gate_decision"] = result.gate.decision
        row["claim_count"] = len(result.report.claims) if result.report is not None else 0
        row["evidence_entry_count"] = evidence_entry_count
        row["draft_claim_count"] = draft_claim_count
        row["created_at"] = datetime.now(timezone.utc)
        self.report_records.append(row)
        return row

    def list_report_records(self, workflow_trace_id=None, status=None):
        rows = self.report_records
        if workflow_trace_id is not None:
            rows = [
                row for row in rows if str(row["workflow_trace_id"]) == str(workflow_trace_id)
            ]
        if status is not None:
            rows = [row for row in rows if row["status"] == status]
        return rows

    def lookup_trace_records(self, workflow_trace_id):
        trace_id = str(workflow_trace_id)
        return {
            "agent_runs": [
                row
                for row in self.agent_runs
                if row["trace_json"].get("workflow_trace_id") == trace_id
            ],
            "evidence_ledger_entries": [
                row
                for row in self.evidence_ledger_entries
                if str(row["workflow_trace_id"]) == trace_id
            ],
            "noise_gate_records": [
                row
                for row in self.noise_gate_records
                if str(row["workflow_trace_id"]) == trace_id
            ],
            "report_records": [
                row
                for row in self.report_records
                if str(row["workflow_trace_id"]) == trace_id
            ],
        }

    def create_failure_case(self, payload: FailureCaseCreate) -> dict:
        row = payload.model_dump()
        row["id"] = uuid4()
        row["created_at"] = datetime.now(timezone.utc)
        self.failure_cases.append(row)
        return row

    def list_failure_cases(self):
        return self.failure_cases

    def create_retrieval_run(self, payload) -> dict:
        row = payload.model_dump()
        row["id"] = uuid4()
        row["created_at"] = datetime.now(timezone.utc)
        self.retrieval_runs.append(row)
        return row

    def list_retrieval_runs(self):
        return self.retrieval_runs

    def get_retrieval_run(self, retrieval_run_id):
        for row in self.retrieval_runs:
            if str(row["id"]) == str(retrieval_run_id):
                return row
        return None

    def create_workflow_run(self, payload) -> dict:
        row = payload.model_dump()
        row["id"] = uuid4()
        row["created_at"] = datetime.now(timezone.utc)
        row["started_at"] = None
        row["ended_at"] = None
        self.workflow_runs.append(row)
        return row

    def list_workflow_runs(self):
        return self.workflow_runs

    def get_workflow_run(self, workflow_run_id):
        for row in self.workflow_runs:
            if str(row["id"]) == str(workflow_run_id):
                return row
        return None

    def lookup_workflow_run_records(self, workflow_run_id):
        workflow_id = str(workflow_run_id)
        return {
            "retrieval_runs": [
                row for row in self.retrieval_runs if str(row.get("workflow_run_id")) == workflow_id
            ],
            "evidence_ledger_entries": [
                row
                for row in self.evidence_ledger_entries
                if str(row.get("workflow_run_id")) == workflow_id
            ],
            "noise_gate_records": [
                row for row in self.noise_gate_records if str(row.get("workflow_run_id")) == workflow_id
            ],
            "report_records": [
                row for row in self.report_records if str(row.get("workflow_run_id")) == workflow_id
            ],
        }

    def update_workflow_run(
        self,
        workflow_run_id,
        *,
        status,
        error_message,
        latency_ms,
        trace_json,
    ):
        for row in self.workflow_runs:
            if row["id"] == workflow_run_id:
                row["status"] = status
                row["error_message"] = error_message
                row["latency_ms"] = latency_ms
                row["trace_json"] = trace_json
                row["ended_at"] = datetime.now(timezone.utc)
                return row
        raise KeyError(f"Unknown workflow run id: {workflow_run_id}")

    def ops_summary(self) -> OpsSummaryOut:
        return OpsSummaryOut(
            status="placeholder",
            workflow_version=WORKFLOW_VERSION,
            document_count=len(self.documents),
            agent_run_count=len(self.agent_runs),
            failure_case_count=len(self.failure_cases),
            noise_gate_record_count=len(self.noise_gate_records),
            blocked_gate_count=sum(
                row["decision"] == "blocked" for row in self.noise_gate_records
            ),
            revision_gate_count=sum(
                row["decision"] == "needs_revision" for row in self.noise_gate_records
            ),
            report_record_count=len(self.report_records),
            generated_report_count=sum(
                row["status"] == "generated" for row in self.report_records
            ),
            blocked_report_count=sum(
                row["status"] == "blocked" for row in self.report_records
            ),
            revision_report_count=sum(
                row["status"] == "needs_revision" for row in self.report_records
            ),
            unsupported_claim_count=sum(
                row["status"] in {"unsupported", "blocked"}
                for row in self.evidence_ledger_entries
            ),
            contradiction_count=sum(
                row["status"] == "contradicted" or bool(row["contradicting_source_ids"])
                for row in self.evidence_ledger_entries
            ),
            average_latency_ms=None,
            notes=["test repository"],
        )


class EvidencePersistenceFailureRepository(InMemoryRepository):
    def create_evidence_ledger_entries(
        self,
        question,
        entries,
        workflow_trace_id=None,
        agent_run_id=None,
        workflow_run_id=None,
        retrieval_run_id=None,
    ):
        raise RuntimeError("simulated evidence persistence failure")


def make_client():
    app = create_app()
    repository = InMemoryRepository()
    app.dependency_overrides[get_repository] = lambda: repository
    return TestClient(app)


def _cosine_distance(left, right):
    left_norm = sum(value * value for value in left) ** 0.5
    right_norm = sum(value * value for value in right) ** 0.5
    denominator = left_norm * right_norm
    if denominator == 0:
        return 1.0
    similarity = sum(left_value * right_value for left_value, right_value in zip(left, right))
    return 1.0 - similarity / denominator


def test_health_endpoint():
    client = make_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "noiseproof-agent-api",
            "workflow_version": WORKFLOW_VERSION,
    }


def test_runtime_workflow_version_names_dashboard_warning_code_surface():
    client = make_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["workflow_version"] == "phase40-lineage-warning-code-dashboard"


def test_document_metadata_roundtrip():
    client = make_client()

    payload = {
        "source_type": "pdf",
        "source_uri": "sample://market-report-001.pdf",
        "title": "Sample market report",
        "source_date": "2026-05-28",
        "extraction_quality": "unknown",
        "status": "registered",
    }

    created = client.post("/documents", json=payload)
    listed = client.get("/documents")

    assert created.status_code == 201
    assert created.json()["source_type"] == "pdf"
    assert created.json()["source_date"] == date(2026, 5, 28).isoformat()
    assert listed.status_code == 200
    assert len(listed.json()) == 1


def test_agent_run_and_failure_case_roundtrip():
    client = make_client()

    run = client.post(
        "/agent-runs",
        json={
            "user_question": "Which sources conflict on demand growth?",
            "latency_ms": 123,
        },
    )
    failure = client.post(
        "/failure-cases",
        json={
            "failure_type": "unsupported_claim",
            "description": "Draft stated demand growth without source evidence.",
            "next_action": "Require source id before report generation.",
        },
    )

    assert run.status_code == 201
    assert failure.status_code == 201
    assert (
        client.get("/agent-runs").json()[0]["workflow_version"]
        == WORKFLOW_VERSION
    )
    assert client.get("/failure-cases").json()[0]["fix_status"] == "open"


def test_failure_case_can_retain_manual_workflow_parent_link():
    client = make_client()
    workflow_run = client.post(
        "/workflow-runs",
        json={
            "question": "Which workflow failure should be reviewed?",
            "status": "failed",
            "error_message": "simulated evidence persistence failure",
        },
    )
    workflow_run_id = workflow_run.json()["id"]

    failure = client.post(
        "/failure-cases",
        json={
            "workflow_run_id": workflow_run_id,
            "failure_type": "workflow_stage_error",
            "description": "Workflow evidence persistence failed after retrieval.",
            "root_cause": "RuntimeError: simulated evidence persistence failure",
            "fix_status": "open",
            "next_action": "Inspect failed workflow parent before retry.",
        },
    )
    listed = client.get("/failure-cases")

    assert workflow_run.status_code == 201
    assert failure.status_code == 201
    assert failure.json()["workflow_run_id"] == workflow_run_id
    assert listed.status_code == 200
    assert listed.json()[0]["workflow_run_id"] == workflow_run_id


def test_failure_case_draft_preview_suggests_manual_payload_without_persistence():
    client = make_client()
    workflow_run_id = str(uuid4())

    response = client.post(
        "/failure-cases/draft-preview",
        json={
            "workflow_run_id": workflow_run_id,
            "question": "Which segment had enterprise demand growth?",
            "workflow_status": "failed",
            "error_message": "simulated evidence persistence failure",
            "trace_json": {
                "stage": "workflow_execute_preview",
                "error_type": "RuntimeError",
            },
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload["persistence_boundary"] == "preview_only_not_persisted"
    assert payload["human_confirmation_required"] is True
    assert payload["source_summary"] == {
        "workflow_run_id": workflow_run_id,
        "workflow_status": "failed",
        "stage": "workflow_execute_preview",
        "error_type": "RuntimeError",
    }
    assert payload["draft"]["agent_run_id"] is None
    assert payload["draft"]["workflow_run_id"] == workflow_run_id
    assert payload["draft"]["failure_type"] == "workflow_stage_error"
    assert "workflow_execute_preview" in payload["draft"]["description"]
    assert payload["draft"]["root_cause"] == "RuntimeError: simulated evidence persistence failure"
    assert payload["draft"]["fix_status"] == "draft"
    assert "Review the failed workflow stage" in payload["draft"]["next_action"]
    assert any("does not create failure_cases" in warning for warning in payload["warnings"])
    assert any("human confirmation" in warning for warning in payload["warnings"])
    assert client.get("/failure-cases").json() == []


def test_failure_case_draft_can_be_manually_handed_to_failure_case_persistence():
    client = make_client()

    preview = client.post(
        "/failure-cases/draft-preview",
        json={
            "workflow_run_id": str(uuid4()),
            "question": "Which segment had enterprise demand growth?",
            "workflow_status": "failed",
            "error_message": "simulated evidence persistence failure",
            "trace_json": {
                "stage": "workflow_execute_preview",
                "error_type": "RuntimeError",
            },
        },
    )

    assert preview.status_code == 200
    preview_payload = preview.json()
    draft = preview_payload["draft"]
    assert preview_payload["persistence_boundary"] == "preview_only_not_persisted"
    assert preview_payload["human_confirmation_required"] is True
    assert draft["fix_status"] == "draft"
    assert client.get("/failure-cases").json() == []

    human_confirmed_payload = {**draft, "fix_status": "open"}
    persisted = client.post("/failure-cases", json=human_confirmed_payload)
    listed = client.get("/failure-cases")

    assert persisted.status_code == 201
    assert persisted.json()["failure_type"] == "workflow_stage_error"
    assert persisted.json()["fix_status"] == "open"
    assert persisted.json()["root_cause"] == draft["root_cause"]
    assert listed.status_code == 200
    assert len(listed.json()) == 1


def test_document_chunk_persistence_endpoint_roundtrip_explicit_document_scope():
    client = make_client()
    document = client.post(
        "/documents",
        json={"source_type": "markdown", "title": "Uploaded report"},
    ).json()
    document_id = document["id"]

    payload = {
        "source_type": "markdown",
        "source_uri": "upload://sample.md",
        "filename": "sample.md",
        "chunk_strategy": "fixed-window",
        "chunk_index": 0,
        "chunk_text": "Revenue increased in Q1.",
        "character_start": 0,
        "character_end": 24,
        "metadata_json": {"strategy": "fixed-window"},
    }

    created = client.post(f"/documents/{document_id}/chunks", json=payload)
    listed = client.get(f"/documents/{document_id}/chunks")

    assert created.status_code == 201
    created_json = created.json()
    assert created_json["document_id"] == document_id
    assert created_json["chunk_text"] == "Revenue increased in Q1."
    assert created_json["persistence_boundary"] == "chunk_text_only_no_raw_file_storage"
    assert listed.status_code == 200
    assert len(listed.json()) == 1
    assert listed.json()[0]["id"] == created_json["id"]


def test_chunk_embedding_endpoint_persists_caller_provided_vector_only():
    client = make_client()
    chunk_id = str(uuid4())

    response = client.post(
        f"/chunks/{chunk_id}/embeddings",
        json={
            "embedding_model": "local-test-model",
            "embedding_dimension": 3,
            "embedding_text_hash": "sha256:chunk-text",
            "distance_metric": "cosine",
            "embedding_status": "created",
            "embedding": [0.1, 0.2, 0.3],
            "metadata_json": {"embedding_source": "caller_provided_vector"},
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["chunk_id"] == chunk_id
    assert body["embedding_model"] == "local-test-model"
    assert body["embedding_dimension"] == 3
    assert body["embedding"] == [0.1, 0.2, 0.3]
    assert body["metadata_json"]["embedding_source"] == "caller_provided_vector"
    assert body["metadata_json"]["persistence_boundary"] == (
        "caller_provided_embedding_only_no_generation"
    )

    list_response = client.get(
        f"/chunks/{chunk_id}/embeddings",
        params={
            "embedding_model": "local-test-model",
            "embedding_status": "created",
        },
    )

    assert list_response.status_code == 200
    rows = list_response.json()
    assert len(rows) == 1
    assert rows[0]["chunk_id"] == chunk_id
    assert rows[0]["metadata_json"]["embedding_source"] == "caller_provided_vector"


def test_chunk_embedding_endpoint_rejects_generated_embedding_claims():
    client = make_client()
    chunk_id = str(uuid4())

    response = client.post(
        f"/chunks/{chunk_id}/embeddings",
        json={
            "embedding_model": "local-test-model",
            "embedding_dimension": 3,
            "embedding_text_hash": "sha256:chunk-text",
            "distance_metric": "cosine",
            "embedding_status": "created",
            "embedding": [0.1, 0.2, 0.3],
            "metadata_json": {"embedding_source": "generated_by_model"},
        },
    )

    assert response.status_code == 400
    assert "caller-provided vector" in response.json()["detail"]


def test_semantic_retrieval_preview_ranks_caller_provided_vectors_without_persistence():
    client = make_client()
    document = client.post(
        "/documents",
        json={
            "source_type": "markdown",
            "source_uri": "upload://semantic.md",
            "filename": "semantic.md",
            "title": "Semantic retrieval preview fixture",
        },
    ).json()
    demand_chunk = client.post(
        f"/documents/{document['id']}/chunks",
        json={
            "source_type": "markdown",
            "source_uri": "upload://semantic.md",
            "filename": "semantic.md",
            "chunk_strategy": "fixed-window",
            "chunk_index": 0,
            "chunk_text": "Enterprise demand growth reached 12% in 2026.",
            "metadata_json": {"header_path": ["Demand"]},
        },
    ).json()
    noise_chunk = client.post(
        f"/documents/{document['id']}/chunks",
        json={
            "source_type": "markdown",
            "source_uri": "upload://semantic.md",
            "filename": "semantic.md",
            "chunk_strategy": "fixed-window",
            "chunk_index": 1,
            "chunk_text": "Weather noise was unrelated to the market question.",
            "metadata_json": {"header_path": ["Noise"]},
        },
    ).json()
    missing_chunk = client.post(
        f"/documents/{document['id']}/chunks",
        json={
            "source_type": "markdown",
            "source_uri": "upload://semantic.md",
            "filename": "semantic.md",
            "chunk_strategy": "fixed-window",
            "chunk_index": 2,
            "chunk_text": "Supply chain data has no embedding yet.",
            "metadata_json": {"header_path": ["Missing"]},
        },
    ).json()
    client.post(
        f"/chunks/{demand_chunk['id']}/embeddings",
        json={
            "embedding_model": "local-test-model",
            "embedding_dimension": 2,
            "embedding_text_hash": "sha256:demand",
            "distance_metric": "cosine",
            "embedding_status": "created",
            "embedding": [1.0, 0.0],
            "metadata_json": {"embedding_source": "caller_provided_vector"},
        },
    )
    client.post(
        f"/chunks/{noise_chunk['id']}/embeddings",
        json={
            "embedding_model": "local-test-model",
            "embedding_dimension": 2,
            "embedding_text_hash": "sha256:noise",
            "distance_metric": "cosine",
            "embedding_status": "created",
            "embedding": [0.0, 1.0],
            "metadata_json": {"embedding_source": "caller_provided_vector"},
        },
    )

    response = client.post(
        f"/documents/{document['id']}/semantic-retrieval-preview",
        json={
            "question": "Which chunk is closest to demand growth?",
            "query_embedding": [1.0, 0.0],
            "embedding_model": "local-test-model",
            "embedding_dimension": 2,
            "limit": 2,
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["retrieval_mode"] == "semantic_preview"
    assert body["persistence_boundary"] == "preview_only_not_persisted"
    assert body["ranking_boundary"] == "exact_cosine_caller_provided_query_vector"
    assert [candidate["chunk_id"] for candidate in body["candidates"]] == [
        demand_chunk["id"],
        noise_chunk["id"],
    ]
    assert body["candidates"][0]["distance"] <= body["candidates"][1]["distance"]
    assert body["candidates"][0]["metadata"]["embedding_table"] == "chunk_embeddings"
    assert body["metadata_json"]["candidate_chunk_ids"] == [
        demand_chunk["id"],
        noise_chunk["id"],
    ]
    assert missing_chunk["id"] in body["missing_embedding_chunk_ids"]
    assert any("does not generate embeddings" in warning for warning in body["warnings"])
    assert any("does not persist retrieval_runs" in warning for warning in body["warnings"])
    assert client.get("/retrieval-runs").json() == []


def test_semantic_retrieval_preview_rejects_query_dimension_mismatch():
    client = make_client()
    document = client.post(
        "/documents",
        json={
            "source_type": "markdown",
            "source_uri": "upload://semantic.md",
            "filename": "semantic.md",
            "title": "Semantic retrieval preview fixture",
        },
    ).json()

    response = client.post(
        f"/documents/{document['id']}/semantic-retrieval-preview",
        json={
            "question": "bad vector",
            "query_embedding": [1.0],
            "embedding_model": "local-test-model",
            "embedding_dimension": 2,
        },
    )

    assert response.status_code == 400
    assert "query_embedding length must match embedding_dimension" in response.json()[
        "detail"
    ]


def test_semantic_retrieval_run_persists_candidates_without_evidence_ledger():
    client = make_client()
    document, demand_chunk, noise_chunk, missing_chunk = _create_semantic_fixture(client)

    response = client.post(
        f"/documents/{document['id']}/semantic-retrieval-runs",
        json={
            "question": "Which chunk is closest to demand growth?",
            "query_embedding": [1.0, 0.0],
            "embedding_model": "local-test-model",
            "embedding_dimension": 2,
            "limit": 2,
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["question"] == "Which chunk is closest to demand growth?"
    assert body["strategy"] == "semantic-cosine"
    assert body["status"] == "completed"
    assert body["result_count"] == 2
    assert body["citation_coverage"] == 1.0
    assert body["missing_evidence_count"] == 0
    assert body["metadata_json"]["source_table"] == "document_chunks"
    assert body["metadata_json"]["embedding_table"] == "chunk_embeddings"
    assert body["metadata_json"]["retrieval_mode"] == "semantic_persisted"
    assert body["metadata_json"]["preview_source"] == "semantic_preview_runtime_smoke"
    assert body["metadata_json"]["candidate_chunk_ids"] == [
        demand_chunk["id"],
        noise_chunk["id"],
    ]
    assert len(body["metadata_json"]["candidate_embedding_ids"]) == 2
    assert missing_chunk["id"] in body["metadata_json"]["missing_embedding_chunk_ids"]
    assert body["metadata_json"]["query_vector_source"] == "caller_provided_vector"
    assert body["metadata_json"]["ranking_boundary"] == (
        "exact_cosine_caller_provided_query_vector"
    )
    assert body["metadata_json"]["persistence_boundary"] == (
        "semantic_retrieval_run_only_no_evidence_ledger"
    )
    assert body["metadata_json"]["no_embedding_generation"] is True
    assert body["metadata_json"]["no_evidence_ledger_generation"] is True
    assert body["metadata_json"]["not_financial_advice"] is True
    assert [result["source_id"] for result in body["results"]] == [
        demand_chunk["id"],
        noise_chunk["id"],
    ]
    assert body["results"][0]["source_type"] == "markdown"
    assert body["results"][0]["score"] >= body["results"][1]["score"]
    assert body["results"][0]["matched_terms"] == []
    assert body["results"][0]["metadata"]["embedding_table"] == "chunk_embeddings"
    assert any("does not generate embeddings" in warning for warning in body["warnings"])
    assert any("does not generate Evidence Ledger" in warning for warning in body["warnings"])

    listed = client.get("/retrieval-runs")
    assert listed.status_code == 200
    stored = listed.json()[0]
    assert stored["id"] == body["id"]
    assert stored["metadata_json"]["retrieval_mode"] == "semantic_persisted"
    assert stored["metadata_json"]["candidate_chunk_ids"] == [
        demand_chunk["id"],
        noise_chunk["id"],
    ]
    assert client.get("/evidence-ledgers").json() == []


def test_semantic_retrieval_run_rejects_query_dimension_mismatch_without_persistence():
    client = make_client()
    document, *_ = _create_semantic_fixture(client)

    response = client.post(
        f"/documents/{document['id']}/semantic-retrieval-runs",
        json={
            "question": "bad vector",
            "query_embedding": [1.0],
            "embedding_model": "local-test-model",
            "embedding_dimension": 2,
            "limit": 2,
        },
    )

    assert response.status_code == 400
    assert "query_embedding length must match embedding_dimension" in response.json()[
        "detail"
    ]
    assert client.get("/retrieval-runs").json() == []


def _create_semantic_fixture(client):
    document = client.post(
        "/documents",
        json={
            "source_type": "markdown",
            "source_uri": "upload://semantic.md",
            "filename": "semantic.md",
            "title": "Semantic retrieval persistence fixture",
        },
    ).json()
    demand_chunk = client.post(
        f"/documents/{document['id']}/chunks",
        json={
            "source_type": "markdown",
            "source_uri": "upload://semantic.md",
            "filename": "semantic.md",
            "chunk_strategy": "fixed-window",
            "chunk_index": 0,
            "chunk_text": "Enterprise demand growth reached 12% in 2026.",
            "metadata_json": {"header_path": ["Demand"]},
        },
    ).json()
    noise_chunk = client.post(
        f"/documents/{document['id']}/chunks",
        json={
            "source_type": "markdown",
            "source_uri": "upload://semantic.md",
            "filename": "semantic.md",
            "chunk_strategy": "fixed-window",
            "chunk_index": 1,
            "chunk_text": "Weather noise was unrelated to the market question.",
            "metadata_json": {"header_path": ["Noise"]},
        },
    ).json()
    missing_chunk = client.post(
        f"/documents/{document['id']}/chunks",
        json={
            "source_type": "markdown",
            "source_uri": "upload://semantic.md",
            "filename": "semantic.md",
            "chunk_strategy": "fixed-window",
            "chunk_index": 2,
            "chunk_text": "Supply chain data has no embedding yet.",
            "metadata_json": {"header_path": ["Missing"]},
        },
    ).json()
    client.post(
        f"/chunks/{demand_chunk['id']}/embeddings",
        json={
            "embedding_model": "local-test-model",
            "embedding_dimension": 2,
            "embedding_text_hash": "sha256:demand",
            "distance_metric": "cosine",
            "embedding_status": "created",
            "embedding": [1.0, 0.0],
            "metadata_json": {"embedding_source": "caller_provided_vector"},
        },
    )
    client.post(
        f"/chunks/{noise_chunk['id']}/embeddings",
        json={
            "embedding_model": "local-test-model",
            "embedding_dimension": 2,
            "embedding_text_hash": "sha256:noise",
            "distance_metric": "cosine",
            "embedding_status": "created",
            "embedding": [0.0, 1.0],
            "metadata_json": {"embedding_source": "caller_provided_vector"},
        },
    )
    return document, demand_chunk, noise_chunk, missing_chunk


def test_upload_chunk_preview_does_not_auto_persist_document_chunks():
    client = make_client()
    document = client.post(
        "/documents",
        json={"source_type": "markdown", "title": "Uploaded report"},
    ).json()
    document_id = document["id"]

    preview = client.post(
        "/documents/upload-chunk-preview",
        files={
            "file": (
                "sample.md",
                b"# Revenue\nRevenue increased in Q1.",
                "text/markdown",
            )
        },
        data={"source_type": "markdown", "strategy": "fixed-window"},
    )
    listed = client.get(f"/documents/{document_id}/chunks")

    assert preview.status_code == 200
    assert listed.status_code == 200
    assert listed.json() == []


def test_document_upload_intake_manifest_preview_hashes_file_without_persistence():
    client = make_client()
    content = b"# Market note\nEnterprise demand growth was 12 percent in 2026.\n"

    response = client.post(
        "/documents/upload-intake-manifest-preview",
        data={"source_type": "markdown"},
        files={"file": ("sample-note.md", content, "text/markdown")},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["filename"] == "sample-note.md"
    assert body["content_type"] == "text/markdown"
    assert body["byte_count"] == len(content)
    assert body["content_sha256"] == sha256(content).hexdigest()
    assert body["source_type"] == "markdown"
    assert body["parser"] == "markdown"
    assert body["storage_decision"] == "do_not_persist_raw_upload_yet"
    assert body["replayable"] is False
    assert body["persistence_boundary"] == "preview_only_not_persisted"
    assert body["manifest"]["source_uri"] == "upload://sample-note.md"
    assert body["manifest"]["profile"]["extraction_quality"] in {"medium", "high"}
    assert body["manifest"]["future_persistence_candidate"] == "uploaded_file_intake"
    assert any("does not create documents" in warning for warning in body["warnings"])
    assert client.get("/documents").json() == []


def test_document_upload_intake_manifest_persists_manifest_metadata_without_raw_file_storage():
    client = make_client()
    content = b"# Market note\nEnterprise demand growth was 12 percent in 2026.\n"

    response = client.post(
        "/documents/upload-intake-manifests",
        data={"source_type": "markdown"},
        files={"file": ("sample-note.md", content, "text/markdown")},
    )

    assert response.status_code == 201
    body = response.json()
    assert body["filename"] == "sample-note.md"
    assert body["content_type"] == "text/markdown"
    assert body["size_bytes"] == len(content)
    assert body["content_sha256"] == sha256(content).hexdigest()
    assert body["source_type"] == "markdown"
    assert body["parser"] == "markdown"
    assert body["storage_decision"] == "do_not_persist_raw_upload_yet"
    assert body["replayable"] is False
    assert body["persistence_boundary"] == "manifest_only_no_raw_file_storage"
    assert body["profile_json"]["extraction_quality"] in {"medium", "high"}
    assert any(
        "does not create documents" in warning for warning in body["warnings_json"]
    )
    assert client.get("/documents").json() == []


def test_document_upload_raw_file_persists_quarantined_bytes_without_filename_storage_key():
    client = make_client()
    content = b"ticker,revenue\nALPHA,120\n"
    expected_hash = sha256(content).hexdigest()

    response = client.post(
        "/documents/upload-raw-files",
        files={"file": ("../../evil.csv", content, "text/csv")},
        data={"source_type": "csv"},
    )

    assert response.status_code == 201
    body = response.json()
    assert body["content_sha256"] == expected_hash
    assert body["filename"] == "../../evil.csv"
    assert body["source_type"] == "csv"
    assert body["content_type"] == "text/csv"
    assert body["size_bytes"] == len(content)
    assert body["raw_file_storage"] is True
    assert body["storage_backend"] == "postgres_bytea"
    assert body["quarantine_status"] == "stored_quarantined"
    assert body["persistence_boundary"] == "raw_upload_quarantine_db_bytea_no_download_endpoint"
    assert body["storage_key"] != "../../evil.csv"
    assert ".." not in body["storage_key"]
    assert "/" not in body["storage_key"]
    assert "\\" not in body["storage_key"]
    assert "evil.csv" not in body["storage_key"]
    assert "raw_bytes" not in body
    assert any("not used as a storage key" in warning for warning in body["warnings_json"])

    listed = client.get("/documents/upload-raw-files")
    assert listed.status_code == 200
    listed_body = listed.json()
    assert listed_body[0]["id"] == body["id"]
    assert listed_body[0]["content_sha256"] == expected_hash
    assert "raw_bytes" not in listed_body[0]


def test_document_upload_raw_file_rejects_oversized_file_without_persistence():
    client = make_client()

    response = client.post(
        "/documents/upload-raw-files",
        files={"file": ("large.bin", b"x" * 1_000_001, "application/octet-stream")},
        data={"source_type": "binary"},
    )

    assert response.status_code == 413
    assert "exceeds max_raw_upload_bytes" in response.json()["detail"]
    assert client.get("/documents/upload-raw-files").json() == []


def test_list_document_upload_intake_manifests_returns_recent_manifest_metadata():
    client = make_client()
    first_content = b"# First\nDemand grew 12 percent.\n"
    second_content = b"# Second\nDemand fell 4 percent.\n"

    first = client.post(
        "/documents/upload-intake-manifests",
        data={"source_type": "markdown"},
        files={"file": ("first.md", first_content, "text/markdown")},
    )
    second = client.post(
        "/documents/upload-intake-manifests",
        data={"source_type": "markdown"},
        files={"file": ("second.md", second_content, "text/markdown")},
    )

    listed = client.get("/documents/upload-intake-manifests")

    assert first.status_code == 201
    assert second.status_code == 201
    assert listed.status_code == 200
    body = listed.json()
    assert [item["filename"] for item in body] == ["first.md", "second.md"]
    assert body[0]["content_sha256"] == sha256(first_content).hexdigest()
    assert body[1]["content_sha256"] == sha256(second_content).hexdigest()
    assert all(item["persistence_boundary"] == "manifest_only_no_raw_file_storage" for item in body)
    assert client.get("/documents").json() == []


def test_document_upload_parsed_document_persists_profile_without_raw_file_storage():
    client = make_client()
    content = b"# Market note\nEnterprise demand growth was 12 percent in 2026.\n"

    response = client.post(
        "/documents/upload-parsed-documents",
        data={"source_type": "markdown", "title": "Uploaded market note"},
        files={"file": ("sample-note.md", content, "text/markdown")},
    )

    assert response.status_code == 201
    body = response.json()
    profile_json = body["profile_json"]

    assert body["filename"] == "sample-note.md"
    assert body["source_uri"] == "upload://sample-note.md"
    assert body["source_type"] == "markdown"
    assert body["title"] == "Uploaded market note"
    assert body["status"] == "parsed_metadata_only"
    assert body["extraction_quality"] in {"medium", "high"}
    assert profile_json["persistence_boundary"] == (
        "document_metadata_and_profile_only_no_raw_file_storage"
    )
    assert profile_json["raw_file_storage"] is False
    assert profile_json["parsed_text_storage"] is False
    assert profile_json["parser"] == "markdown"
    assert profile_json["profile"]["recommended_strategy"]
    assert profile_json["upload"]["byte_count"] == len(content)
    assert any("metadata/profile only" in warning for warning in profile_json["parse_warnings"])
    assert not any("does not create documents" in warning for warning in profile_json["parse_warnings"])
    assert "Enterprise demand growth" not in str(profile_json)
    assert len(client.get("/documents").json()) == 1


def test_document_upload_preview_parses_markdown_without_persistence():
    client = make_client()
    content = b"# Demand note\nEnterprise demand grew 12% in 2026.\n"

    response = client.post(
        "/documents/upload-preview",
        data={"source_type": "markdown"},
        files={"file": ("sample-note.md", content, "text/markdown")},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["persistence_boundary"] == "preview_only_not_persisted"
    assert body["filename"] == "sample-note.md"
    assert body["content_type"] == "text/markdown"
    assert body["byte_count"] == len(content)
    assert body["source_type"] == "markdown"
    assert body["parser"] == "markdown"
    assert "Enterprise demand grew" in body["text"]
    assert body["profile"]["has_numbers"] is True
    assert any("does not create documents" in warning for warning in body["warnings"])
    assert client.get("/documents").json() == []


def test_document_upload_preview_surfaces_unknown_binary_boundary():
    client = make_client()

    response = client.post(
        "/documents/upload-preview",
        files={"file": ("sample.bin", b"\xff\xfe\x00\x01", "application/octet-stream")},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["persistence_boundary"] == "preview_only_not_persisted"
    assert body["filename"] == "sample.bin"
    assert body["content_type"] == "application/octet-stream"
    assert body["source_type"] == "unknown"
    assert body["parser"] == "unknown"
    assert body["failure_case_candidate"]["failure_type"] == "unknown_source_type"
    assert any("could not infer a supported source_type" in warning for warning in body["warnings"])
    assert any("does not claim robust PDF extraction" in warning for warning in body["warnings"])


def test_document_upload_chunk_preview_compares_uploaded_csv_without_persistence():
    client = make_client()
    content = b"date,segment,growth\n2026-05-28,enterprise,12\n2026-05-29,consumer,-3\n"

    response = client.post(
        "/documents/upload-chunk-preview",
        data={"source_type": "csv", "max_characters": "80", "overlap": "0"},
        files={"file": ("sample-market.csv", content, "text/csv")},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["persistence_boundary"] == "preview_only_not_persisted"
    assert body["filename"] == "sample-market.csv"
    assert body["content_type"] == "text/csv"
    assert body["byte_count"] == len(content)
    assert body["source_type"] == "csv"
    assert body["parser"] == "csv"
    strategy_names = {strategy["strategy"] for strategy in body["strategies"]}
    assert {"fixed-window", "row-aware"}.issubset(strategy_names)
    assert body["profile"]["has_tables"] is True
    assert any("does not create documents" in warning for warning in body["parse_warnings"])
    assert client.get("/documents").json() == []


def test_document_upload_chunks_persists_document_and_chunks_without_raw_file_storage():
    client = make_client()
    content = (
        b"# Market note\n"
        b"Enterprise demand growth was 12 percent in 2026.\n"
        b"Consumer demand declined.\n"
    )

    response = client.post(
        "/documents/upload-chunks",
        data={
            "source_type": "markdown",
            "title": "Uploaded market note",
            "strategy": "fixed-window",
            "max_characters": "80",
            "overlap": "0",
        },
        files={"file": ("sample-note.md", content, "text/markdown")},
    )

    assert response.status_code == 201
    body = response.json()
    document = body["document"]
    chunks = body["chunks"]

    assert body["filename"] == "sample-note.md"
    assert body["content_type"] == "text/markdown"
    assert body["byte_count"] == len(content)
    assert body["source_type"] == "markdown"
    assert body["chunk_strategy"] == "fixed-window"
    assert body["chunk_count"] == len(chunks)
    assert body["persistence_boundary"] == "chunk_text_only_no_raw_file_storage"
    assert body["handoff_boundary"] == "explicit_upload_to_chunks_no_raw_file_storage"
    assert body["raw_file_storage"] is False
    assert body["parsed_text_storage"] is False
    assert any("does not store raw uploaded bytes" in warning for warning in body["warnings"])

    assert document["source_type"] == "markdown"
    assert document["filename"] == "sample-note.md"
    assert document["source_uri"] == "upload://sample-note.md"
    assert document["title"] == "Uploaded market note"
    assert document["status"] == "chunked_metadata_only"
    assert document["profile_json"]["persistence_boundary"] == (
        "document_metadata_and_chunks_only_no_raw_file_storage"
    )
    assert document["profile_json"]["raw_file_storage"] is False
    assert document["profile_json"]["parsed_text_storage"] is False
    assert document["profile_json"]["chunk_count"] == len(chunks)
    assert "Enterprise demand growth" not in str(document["profile_json"])

    assert len(chunks) >= 1
    assert all(chunk["document_id"] == document["id"] for chunk in chunks)
    assert all(chunk["source_type"] == "markdown" for chunk in chunks)
    assert all(chunk["filename"] == "sample-note.md" for chunk in chunks)
    assert all(chunk["chunk_strategy"] == "fixed-window" for chunk in chunks)
    assert all(
        chunk["persistence_boundary"] == "chunk_text_only_no_raw_file_storage"
        for chunk in chunks
    )
    assert any("Enterprise demand growth" in chunk["chunk_text"] for chunk in chunks)

    listed_documents = client.get("/documents").json()
    listed_chunks = client.get(f"/documents/{document['id']}/chunks").json()
    assert len(listed_documents) == 1
    assert listed_chunks == chunks


def test_document_upload_retrieval_preview_searches_uploaded_markdown_without_persistence():
    client = make_client()
    content = b"# Market note\nEnterprise demand growth was 12 percent in 2026.\nConsumer demand declined.\n"

    response = client.post(
        "/documents/upload-retrieval-preview",
        data={
            "question": "Which source mentions enterprise demand growth?",
            "source_type": "markdown",
            "strategy": "fixed-window",
            "top_k": "3",
            "max_characters": "120",
            "overlap": "0",
        },
        files={"file": ("sample-note.md", content, "text/markdown")},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["persistence_boundary"] == "preview_only_not_persisted"
    assert body["filename"] == "sample-note.md"
    assert body["content_type"] == "text/markdown"
    assert body["byte_count"] == len(content)
    assert body["source_type"] == "markdown"
    assert body["question"] == "Which source mentions enterprise demand growth?"
    assert body["status"] == "completed"
    assert body["result_count"] >= 1
    assert body["results"][0]["source_id"] == "upload://sample-note.md"
    assert "enterprise" in body["results"][0]["matched_terms"]
    assert any("does not create retrieval_runs" in warning for warning in body["warnings"])
    assert client.get("/retrieval-runs").json() == []


def test_document_upload_retrieval_preview_keeps_buy_sell_boundary():
    client = make_client()

    response = client.post(
        "/documents/upload-retrieval-preview",
        data={
            "question": "Should I buy this stock?",
            "source_type": "markdown",
        },
        files={
            "file": (
                "earnings-note.md",
                b"Revenue grew 12 percent after earnings.",
                "text/markdown",
            )
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["persistence_boundary"] == "preview_only_not_persisted"
    assert body["trading_advice_boundary"] == "question_contains_trading_advice_drift"
    assert body["status"] == "blocked"
    assert body["results"] == []
    assert any("buy/sell" in warning for warning in body["warnings"])
    assert client.get("/retrieval-runs").json() == []


def test_document_upload_evidence_preview_builds_ledger_without_persistence():
    client = make_client()
    content = b"# Market note\nEnterprise demand growth was 12 percent in 2026.\n"

    response = client.post(
        "/documents/upload-evidence-preview",
        data={
            "question": "Which source supports enterprise demand growth?",
            "source_type": "markdown",
            "strategy": "fixed-window",
            "top_k": "3",
            "max_characters": "120",
            "overlap": "0",
        },
        files={"file": ("sample-note.md", content, "text/markdown")},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["persistence_boundary"] == "preview_only_not_persisted"
    assert body["filename"] == "sample-note.md"
    assert body["retrieval"]["result_count"] >= 1
    assert body["evidence"]["summary"]["supported_count"] >= 1
    assert body["evidence"]["entries"][0]["source_id"] == "upload://sample-note.md"
    assert "enterprise demand growth" in body["evidence"]["entries"][0]["claim"].lower()
    assert any("does not create Evidence Ledger entries" in warning for warning in body["warnings"])
    assert client.get("/retrieval-runs").json() == []
    assert client.get("/evidence-ledgers").json() == []


def test_document_upload_evidence_preview_blocks_trading_drift_before_ledger():
    client = make_client()

    response = client.post(
        "/documents/upload-evidence-preview",
        data={"question": "Should I sell this stock?", "source_type": "markdown"},
        files={
            "file": (
                "earnings-note.md",
                b"Revenue declined after earnings.",
                "text/markdown",
            )
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["persistence_boundary"] == "preview_only_not_persisted"
    assert body["status"] == "blocked"
    assert body["retrieval"]["status"] == "blocked"
    assert body["evidence"]["summary"]["blocked_count"] == 1
    assert body["evidence"]["entries"][0]["status"] == "blocked"
    assert any("buy/sell" in warning for warning in body["warnings"])
    assert client.get("/evidence-ledgers").json() == []


def test_document_upload_noise_gate_preview_checks_uploaded_evidence_without_persistence():
    client = make_client()
    content = b"# Market note\nEnterprise demand growth was 12 percent in 2026.\n"

    response = client.post(
        "/documents/upload-noise-gate-preview",
        data={
            "question": "Which source supports enterprise demand growth?",
            "source_type": "markdown",
            "strategy": "fixed-window",
            "top_k": "3",
            "max_characters": "120",
            "overlap": "0",
        },
        files={"file": ("sample-note.md", content, "text/markdown")},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["persistence_boundary"] == "preview_only_not_persisted"
    assert body["filename"] == "sample-note.md"
    assert body["retrieval"]["result_count"] >= 1
    assert body["evidence"]["summary"]["supported_count"] >= 1
    assert body["gate"]["decision"] in {"pass", "needs_revision"}
    assert any(check["name"] == "limitations_explicit" for check in body["gate"]["checks"])
    assert any("does not create Noise Gate records" in warning for warning in body["warnings"])
    assert client.get("/retrieval-runs").json() == []
    assert client.get("/evidence-ledgers").json() == []
    assert client.get("/noise-gates").json() == []
    assert client.get("/reports").json() == []


def test_document_upload_noise_gate_preview_blocks_trading_drift_without_persistence():
    client = make_client()

    response = client.post(
        "/documents/upload-noise-gate-preview",
        data={"question": "Should I sell this stock?", "source_type": "markdown"},
        files={
            "file": (
                "earnings-note.md",
                b"Revenue declined after earnings.",
                "text/markdown",
            )
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["persistence_boundary"] == "preview_only_not_persisted"
    assert body["status"] == "blocked"
    assert body["retrieval"]["status"] == "blocked"
    assert body["evidence"]["summary"]["blocked_count"] == 1
    assert body["gate"]["decision"] == "blocked"
    assert "trading_advice_drift" in [check["name"] for check in body["gate"]["checks"]]
    assert any("buy/sell" in warning for warning in body["warnings"])
    assert client.get("/noise-gates").json() == []


def test_document_upload_report_preview_formats_uploaded_gate_output_without_persistence():
    client = make_client()
    content = b"# Market note\nEnterprise demand growth was 12 percent in 2026.\n"

    response = client.post(
        "/documents/upload-report-preview",
        data={
            "question": "Which source supports enterprise demand growth?",
            "source_type": "markdown",
            "strategy": "fixed-window",
            "top_k": "3",
            "max_characters": "120",
            "overlap": "0",
        },
        files={"file": ("sample-note.md", content, "text/markdown")},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["persistence_boundary"] == "preview_only_not_persisted"
    assert body["filename"] == "sample-note.md"
    assert body["retrieval"]["result_count"] >= 1
    assert body["evidence"]["summary"]["supported_count"] >= 1
    assert body["report"]["status"] in {"generated", "needs_revision"}
    assert body["report"]["gate"]["decision"] in {"pass", "needs_revision"}
    assert any("does not create report records" in warning for warning in body["warnings"])
    assert client.get("/retrieval-runs").json() == []
    assert client.get("/evidence-ledgers").json() == []
    assert client.get("/noise-gates").json() == []
    assert client.get("/reports").json() == []


def test_document_upload_report_preview_blocks_trading_drift_without_persistence():
    client = make_client()

    response = client.post(
        "/documents/upload-report-preview",
        data={"question": "Should I sell this stock?", "source_type": "markdown"},
        files={
            "file": (
                "earnings-note.md",
                b"Revenue declined after earnings.",
                "text/markdown",
            )
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["persistence_boundary"] == "preview_only_not_persisted"
    assert body["status"] == "blocked"
    assert body["retrieval"]["status"] == "blocked"
    assert body["evidence"]["summary"]["blocked_count"] == 1
    assert body["report"]["status"] == "blocked"
    assert body["report"]["report"] is None
    assert body["report"]["gate"]["decision"] == "blocked"
    assert any("buy/sell" in warning for warning in body["warnings"])
    assert client.get("/reports").json() == []


def test_document_upload_failure_case_draft_preview_suggests_draft_without_persistence():
    client = make_client()
    content = b"# Market note\nEnterprise demand growth was 12 percent in 2026.\n"

    response = client.post(
        "/documents/upload-failure-case-draft-preview",
        data={
            "question": "Which source supports enterprise demand growth?",
            "source_type": "markdown",
            "strategy": "fixed-window",
            "top_k": "3",
            "max_characters": "120",
            "overlap": "0",
        },
        files={"file": ("sample-note.md", content, "text/markdown")},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["persistence_boundary"] == "preview_only_not_persisted"
    assert body["report"]["status"] in {"generated", "needs_revision"}
    assert body["draft_preview"]["persistence_boundary"] == "preview_only_not_persisted"
    assert body["draft_preview"]["human_confirmation_required"] is True
    assert body["draft_preview"]["draft"]["fix_status"] == "draft"
    assert "uploaded_file_report_preview" in body["draft_preview"]["source_summary"]["stage"]
    assert any("does not create failure_cases" in warning for warning in body["warnings"])
    assert client.get("/failure-cases").json() == []
    assert client.get("/reports").json() == []


def test_document_upload_failure_case_draft_preview_keeps_trading_boundary():
    client = make_client()

    response = client.post(
        "/documents/upload-failure-case-draft-preview",
        data={"question": "Should I sell this stock?", "source_type": "markdown"},
        files={
            "file": (
                "earnings-note.md",
                b"Revenue declined after earnings.",
                "text/markdown",
            )
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "blocked"
    assert body["report"]["status"] == "blocked"
    assert body["draft_preview"]["draft"]["failure_type"] == "workflow_stage_error"
    assert "blocked" in body["draft_preview"]["draft"]["description"]
    assert any("buy/sell" in warning for warning in body["warnings"])
    assert client.get("/failure-cases").json() == []


def test_document_upload_failure_case_draft_can_be_manually_persisted_without_automation():
    client = make_client()

    draft_response = client.post(
        "/documents/upload-failure-case-draft-preview",
        data={"question": "Should I sell this stock?", "source_type": "markdown"},
        files={
            "file": (
                "earnings-note.md",
                b"Revenue declined after earnings.",
                "text/markdown",
            )
        },
    )
    draft_body = draft_response.json()

    assert draft_response.status_code == 200
    assert client.get("/failure-cases").json() == []

    manual_response = client.post(
        "/failure-cases",
        json=draft_body["draft_preview"]["draft"],
    )

    assert manual_response.status_code == 201
    persisted = manual_response.json()
    assert persisted["failure_type"] == "workflow_stage_error"
    assert persisted["fix_status"] == "draft"
    assert "Should I sell this stock?" in persisted["description"]
    listed = client.get("/failure-cases").json()
    assert len(listed) == 1
    assert listed[0]["id"] == persisted["id"]


def test_workflow_run_metadata_roundtrip_without_orchestration():
    client = make_client()

    created = client.post(
        "/workflow-runs",
        json={
            "question": "Which sources disagree about memory demand?",
            "status": "created",
            "trace_json": {"phase": "metadata-only"},
        },
    )
    listed = client.get("/workflow-runs")

    assert created.status_code == 201
    assert created.json()["question"] == "Which sources disagree about memory demand?"
    assert created.json()["workflow_version"] == WORKFLOW_VERSION
    assert created.json()["status"] == "created"
    assert created.json()["trace_json"] == {"phase": "metadata-only"}
    assert created.json()["started_at"] is None
    assert listed.status_code == 200
    assert len(listed.json()) == 1
    assert listed.json()[0]["id"] == created.json()["id"]


def test_ops_dashboard_surfaces_workflow_runs_as_metadata_only():
    client = make_client()

    client.post(
        "/workflow-runs",
        json={
            "question": "Which sources disagree about memory demand?",
            "trace_json": {"phase": "metadata-only"},
        },
    )

    dashboard = client.get("/ops/dashboard")

    assert dashboard.status_code == 200
    assert "Workflow Runs" in dashboard.text
    assert "metadata-only" in dashboard.text
    assert "Which sources disagree about memory demand?" in dashboard.text
    assert "deterministic execution-preview parents" in dashboard.text


def test_workflow_run_execute_preview_links_child_records_to_workflow_parent():
    client = make_client()

    response = client.post(
        "/workflow-runs/execute-preview",
        json={
            "question": "Which segment had enterprise demand growth?",
            "strategy": "fixed-window",
            "sources": [
                {
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "content": "Enterprise segment demand growth was 12 percent in 2026.",
                }
            ],
            "draft_claims": [
                "Enterprise segment demand growth was supported by current retrieved evidence."
            ],
        },
    )

    assert response.status_code == 201
    payload = response.json()
    workflow_run_id = payload["workflow_run"]["id"]
    assert payload["execution_boundary"] == "deterministic_preview_only"
    assert payload["workflow_run"]["status"] == "completed"
    assert payload["workflow_run"]["workflow_version"] == WORKFLOW_VERSION
    assert payload["workflow_run"]["trace_json"]["stage"] == "workflow_execute_preview"
    assert payload["retrieval"]["workflow_run_id"] == workflow_run_id
    assert payload["retrieval"]["result_count"] >= 1
    assert payload["evidence"]["stored_entry_count"] >= 1
    assert payload["gate"]["decision"] in {"pass", "needs_revision", "blocked"}
    assert payload["report"]["status"] in {"generated", "needs_revision", "blocked"}
    assert payload["workflow_trace_id"] == payload["evidence"]["entries"][0]["workflow_trace_id"]
    assert payload["workflow_trace_id"] == payload["gate"]["workflow_trace_id"]
    assert payload["workflow_trace_id"] == payload["report"]["workflow_trace_id"]
    assert payload["evidence"]["entries"][0]["workflow_run_id"] == workflow_run_id
    assert payload["gate"]["workflow_run_id"] == workflow_run_id
    assert payload["report"]["workflow_run_id"] == workflow_run_id
    evidence_entry_ids = [entry["id"] for entry in payload["evidence"]["entries"]]
    assert payload["gate"]["stage_input_manifest"] == {
        "input_evidence_ledger_entry_ids": evidence_entry_ids,
        "input_noise_gate_record_id": None,
        "source": "workflow_execution_preview",
    }
    assert payload["report"]["stage_input_manifest"] == {
        "input_evidence_ledger_entry_ids": evidence_entry_ids,
        "input_noise_gate_record_id": payload["gate"]["id"],
        "source": "workflow_execution_preview",
    }
    assert any("child records are attached to workflow_run_id" in warning for warning in payload["warnings"])


def test_workflow_execute_preview_marks_parent_failed_when_stage_errors():
    app = create_app()
    repository = EvidencePersistenceFailureRepository()
    app.dependency_overrides[get_repository] = lambda: repository
    client = TestClient(app, raise_server_exceptions=False)

    response = client.post(
        "/workflow-runs/execute-preview",
        json={
            "question": "Which segment had enterprise demand growth?",
            "strategy": "fixed-window",
            "sources": [
                {
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "content": "Enterprise segment demand growth was 12 percent in 2026.",
                }
            ],
        },
    )

    assert response.status_code == 500
    assert len(repository.workflow_runs) == 1
    workflow_run = repository.workflow_runs[0]
    assert workflow_run["status"] == "failed"
    assert workflow_run["error_message"] == "simulated evidence persistence failure"
    assert workflow_run["latency_ms"] >= 0
    assert workflow_run["ended_at"] is not None
    assert workflow_run["trace_json"]["stage"] == "workflow_execute_preview"
    assert workflow_run["trace_json"]["error_type"] == "RuntimeError"
    assert len(repository.retrieval_runs) == 1
    assert repository.retrieval_runs[0]["workflow_run_id"] == workflow_run["id"]
    assert repository.failure_cases == []


def test_failed_workflow_parent_can_feed_failure_case_draft_preview_without_persistence():
    app = create_app()
    repository = EvidencePersistenceFailureRepository()
    app.dependency_overrides[get_repository] = lambda: repository
    client = TestClient(app, raise_server_exceptions=False)

    execution = client.post(
        "/workflow-runs/execute-preview",
        json={
            "question": "Which segment had enterprise demand growth?",
            "strategy": "fixed-window",
            "sources": [
                {
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "content": "Enterprise segment demand growth was 12 percent in 2026.",
                }
            ],
        },
    )

    assert execution.status_code == 500
    assert len(repository.workflow_runs) == 1
    workflow_run = repository.workflow_runs[0]
    assert workflow_run["status"] == "failed"
    assert repository.failure_cases == []

    preview = client.post(
        "/failure-cases/draft-preview",
        json={
            "workflow_run_id": str(workflow_run["id"]),
            "question": workflow_run["question"],
            "workflow_status": workflow_run["status"],
            "error_message": workflow_run["error_message"],
            "trace_json": workflow_run["trace_json"],
        },
    )

    assert preview.status_code == 200
    payload = preview.json()
    assert payload["persistence_boundary"] == "preview_only_not_persisted"
    assert payload["human_confirmation_required"] is True
    assert payload["source_summary"] == {
        "workflow_run_id": str(workflow_run["id"]),
        "workflow_status": "failed",
        "stage": "workflow_execute_preview",
        "error_type": "RuntimeError",
    }
    assert payload["draft"]["failure_type"] == "workflow_stage_error"
    assert payload["draft"]["root_cause"] == "RuntimeError: simulated evidence persistence failure"
    assert payload["draft"]["fix_status"] == "draft"
    assert any("does not create failure_cases" in warning for warning in payload["warnings"])
    assert repository.failure_cases == []
    assert client.get("/failure-cases").json() == []


def test_workflow_run_detail_returns_child_records_linked_to_workflow_parent():
    client = make_client()
    execution = client.post(
        "/workflow-runs/execute-preview",
        json={
            "question": "Which segment had enterprise demand growth?",
            "strategy": "fixed-window",
            "sources": [
                {
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "content": "Enterprise segment demand growth was 12 percent in 2026.",
                }
            ],
        },
    ).json()
    workflow_run_id = execution["workflow_run"]["id"]

    response = client.get(f"/workflow-runs/{workflow_run_id}")

    assert response.status_code == 200
    payload = response.json()
    assert payload["workflow_run"]["id"] == workflow_run_id
    assert payload["summary"] == {
        "retrieval_run_count": 1,
        "evidence_ledger_entry_count": 1,
        "noise_gate_record_count": 1,
        "report_record_count": 1,
    }
    assert payload["retrieval_runs"][0]["workflow_run_id"] == workflow_run_id
    assert payload["evidence_ledger_entries"][0]["workflow_run_id"] == workflow_run_id
    assert payload["noise_gate_records"][0]["workflow_run_id"] == workflow_run_id
    assert payload["report_records"][0]["workflow_run_id"] == workflow_run_id
    evidence_entry_ids = [entry["id"] for entry in payload["evidence_ledger_entries"]]
    assert payload["noise_gate_records"][0]["stage_input_manifest"][
        "input_evidence_ledger_entry_ids"
    ] == evidence_entry_ids
    assert payload["report_records"][0]["stage_input_manifest"][
        "input_noise_gate_record_id"
    ] == payload["noise_gate_records"][0]["id"]


def test_workflow_run_lineage_read_model_resolves_manifest_inputs_without_new_storage():
    client = make_client()
    execution = client.post(
        "/workflow-runs/execute-preview",
        json={
            "question": "Which segment had enterprise demand growth?",
            "strategy": "fixed-window",
            "sources": [
                {
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "content": "Enterprise segment demand growth was 12 percent in 2026.",
                }
            ],
        },
    ).json()
    workflow_run_id = execution["workflow_run"]["id"]

    response = client.get(f"/workflow-runs/{workflow_run_id}/lineage")

    assert response.status_code == 200
    payload = response.json()
    evidence_entry_ids = [entry["id"] for entry in payload["evidence_ledger_entries"]]
    gate_id = payload["noise_gate_lineage"][0]["record"]["id"]
    assert payload["workflow_run"]["id"] == workflow_run_id
    assert payload["lineage_boundary"] == "derived_read_model_only"
    assert payload["summary"] == {
        "evidence_ledger_entry_count": 1,
        "noise_gate_record_count": 1,
        "report_record_count": 1,
        "gate_input_evidence_reference_count": 1,
        "report_input_evidence_reference_count": 1,
        "report_input_gate_reference_count": 1,
        "missing_reference_count": 0,
    }
    assert payload["noise_gate_lineage"][0]["input_evidence_entry_ids"] == evidence_entry_ids
    assert payload["noise_gate_lineage"][0]["input_evidence_entries"][0]["id"] == evidence_entry_ids[0]
    assert payload["noise_gate_lineage"][0]["missing_evidence_entry_ids"] == []
    assert payload["report_lineage"][0]["input_evidence_entry_ids"] == evidence_entry_ids
    assert payload["report_lineage"][0]["input_evidence_entries"][0]["id"] == evidence_entry_ids[0]
    assert payload["report_lineage"][0]["input_noise_gate_record_id"] == gate_id
    assert payload["report_lineage"][0]["input_noise_gate_record"]["id"] == gate_id
    assert payload["report_lineage"][0]["missing_evidence_entry_ids"] == []
    assert payload["report_lineage"][0]["missing_noise_gate_record_id"] is None
    assert any("derived read model" in warning for warning in payload["warnings"])
    assert payload["warning_codes"] == [
        "derived_read_model_boundary",
        "local_workflow_scope",
    ]


def test_workflow_run_lineage_reports_missing_manifest_references_without_mutation_api():
    client = make_client()
    repository = client.app.dependency_overrides[get_repository]()
    execution = client.post(
        "/workflow-runs/execute-preview",
        json={
            "question": "Which segment had enterprise demand growth?",
            "strategy": "fixed-window",
            "sources": [
                {
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "content": "Enterprise segment demand growth was 12 percent in 2026.",
                }
            ],
        },
    ).json()
    workflow_run_id = execution["workflow_run"]["id"]
    missing_evidence_id = str(uuid4())
    missing_gate_id = str(uuid4())
    repository.noise_gate_records[0]["stage_input_manifest"] = {
        "input_evidence_ledger_entry_ids": [missing_evidence_id],
    }
    repository.report_records[0]["stage_input_manifest"] = {
        "input_evidence_ledger_entry_ids": [missing_evidence_id],
        "input_noise_gate_record_id": missing_gate_id,
    }

    response = client.get(f"/workflow-runs/{workflow_run_id}/lineage")

    assert response.status_code == 200
    payload = response.json()
    assert payload["lineage_boundary"] == "derived_read_model_only"
    assert payload["summary"]["missing_reference_count"] == 3
    assert payload["summary"]["evidence_ledger_entry_count"] == 1
    assert payload["summary"]["gate_input_evidence_reference_count"] == 1
    assert payload["summary"]["report_input_evidence_reference_count"] == 1
    assert payload["summary"]["report_input_gate_reference_count"] == 1
    assert payload["noise_gate_lineage"][0]["input_evidence_entries"] == []
    assert payload["noise_gate_lineage"][0]["missing_evidence_entry_ids"] == [
        missing_evidence_id
    ]
    assert payload["report_lineage"][0]["input_evidence_entries"] == []
    assert payload["report_lineage"][0]["input_noise_gate_record"] is None
    assert payload["report_lineage"][0]["missing_evidence_entry_ids"] == [missing_evidence_id]
    assert payload["report_lineage"][0]["missing_noise_gate_record_id"] == missing_gate_id
    assert any("could not be resolved" in warning for warning in payload["warnings"])
    assert "missing_manifest_reference" in payload["warning_codes"]


def test_workflow_run_lineage_ignores_non_list_manifest_evidence_ids():
    client = make_client()
    repository = client.app.dependency_overrides[get_repository]()
    execution = client.post(
        "/workflow-runs/execute-preview",
        json={
            "question": "Which segment had enterprise demand growth?",
            "strategy": "fixed-window",
            "sources": [
                {
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "content": "Enterprise segment demand growth was 12 percent in 2026.",
                }
            ],
        },
    ).json()
    workflow_run_id = execution["workflow_run"]["id"]
    evidence_entry_id = repository.evidence_ledger_entries[0]["id"]
    gate_id = repository.noise_gate_records[0]["id"]
    repository.noise_gate_records[0]["stage_input_manifest"] = {
        "input_evidence_ledger_entry_ids": str(evidence_entry_id),
    }
    repository.report_records[0]["stage_input_manifest"] = {
        "input_evidence_ledger_entry_ids": str(evidence_entry_id),
        "input_noise_gate_record_id": str(gate_id),
    }

    response = client.get(f"/workflow-runs/{workflow_run_id}/lineage")

    assert response.status_code == 200
    payload = response.json()
    assert payload["summary"]["gate_input_evidence_reference_count"] == 0
    assert payload["summary"]["report_input_evidence_reference_count"] == 0
    assert payload["summary"]["report_input_gate_reference_count"] == 1
    assert payload["summary"]["missing_reference_count"] == 0
    assert payload["noise_gate_lineage"][0]["input_evidence_entry_ids"] == []
    assert payload["noise_gate_lineage"][0]["missing_evidence_entry_ids"] == []
    assert payload["report_lineage"][0]["input_evidence_entry_ids"] == []
    assert payload["report_lineage"][0]["missing_evidence_entry_ids"] == []
    assert payload["report_lineage"][0]["input_noise_gate_record_id"] == str(gate_id)
    assert payload["report_lineage"][0]["missing_noise_gate_record_id"] is None
    assert any(
        "input_evidence_ledger_entry_ids must be a list" in warning
        for warning in payload["warnings"]
    )
    assert "invalid_manifest_shape" in payload["warning_codes"]


def test_workflow_run_lineage_keeps_cross_workflow_manifest_references_local():
    client = make_client()
    repository = client.app.dependency_overrides[get_repository]()
    first = client.post(
        "/workflow-runs/execute-preview",
        json={
            "question": "Which segment had enterprise demand growth?",
            "strategy": "fixed-window",
            "sources": [
                {
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "content": "Enterprise segment demand growth was 12 percent in 2026.",
                }
            ],
        },
    ).json()
    second = client.post(
        "/workflow-runs/execute-preview",
        json={
            "question": "Which segment had customer budget growth?",
            "strategy": "fixed-window",
            "sources": [
                {
                    "source_id": "doc-budget",
                    "source_type": "markdown",
                    "content": "Customer budget growth was 9 percent in 2026.",
                }
            ],
        },
    ).json()
    first_workflow_id = first["workflow_run"]["id"]
    second_workflow_id = second["workflow_run"]["id"]
    first_evidence_id = next(
        row["id"]
        for row in repository.evidence_ledger_entries
        if str(row["workflow_run_id"]) == first_workflow_id
    )
    second_gate = next(
        row
        for row in repository.noise_gate_records
        if str(row["workflow_run_id"]) == second_workflow_id
    )
    second_gate["stage_input_manifest"] = {
        "input_evidence_ledger_entry_ids": [str(first_evidence_id)],
    }

    response = client.get(f"/workflow-runs/{second_workflow_id}/lineage")

    assert response.status_code == 200
    payload = response.json()
    assert payload["workflow_run"]["id"] == second_workflow_id
    assert payload["summary"]["evidence_ledger_entry_count"] == 1
    assert payload["summary"]["gate_input_evidence_reference_count"] == 1
    assert payload["summary"]["missing_reference_count"] == 1
    assert payload["noise_gate_lineage"][0]["input_evidence_entries"] == []
    assert payload["noise_gate_lineage"][0]["missing_evidence_entry_ids"] == [
        str(first_evidence_id)
    ]
    assert any("could not be resolved" in warning for warning in payload["warnings"])
    assert "local_workflow_scope" in payload["warning_codes"]


def test_workflow_run_lineage_preserves_duplicate_manifest_reference_counts():
    client = make_client()
    repository = client.app.dependency_overrides[get_repository]()
    execution = client.post(
        "/workflow-runs/execute-preview",
        json={
            "question": "Which segment had enterprise demand growth?",
            "strategy": "fixed-window",
            "sources": [
                {
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "content": "Enterprise segment demand growth was 12 percent in 2026.",
                }
            ],
        },
    ).json()
    workflow_run_id = execution["workflow_run"]["id"]
    evidence_entry_id = str(repository.evidence_ledger_entries[0]["id"])
    repository.noise_gate_records[0]["stage_input_manifest"] = {
        "input_evidence_ledger_entry_ids": [evidence_entry_id, evidence_entry_id],
    }

    response = client.get(f"/workflow-runs/{workflow_run_id}/lineage")

    assert response.status_code == 200
    payload = response.json()
    assert payload["summary"]["gate_input_evidence_reference_count"] == 2
    assert payload["noise_gate_lineage"][0]["input_evidence_entry_ids"] == [
        evidence_entry_id,
        evidence_entry_id,
    ]
    assert [
        entry["id"] for entry in payload["noise_gate_lineage"][0]["input_evidence_entries"]
    ] == [evidence_entry_id, evidence_entry_id]


def test_ops_dashboard_links_workflow_runs_to_detail_and_lineage_views():
    client = make_client()
    execution = client.post(
        "/workflow-runs/execute-preview",
        json={
            "question": "Which segment had enterprise demand growth?",
            "strategy": "fixed-window",
            "sources": [
                {
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "content": "Enterprise segment demand growth was 12 percent in 2026.",
                }
            ],
        },
    )
    workflow_run_id = execution.json()["workflow_run"]["id"]

    dashboard = client.get("/ops/dashboard")

    assert dashboard.status_code == 200
    assert f'href="/workflow-runs/{workflow_run_id}">detail</a>' in dashboard.text
    assert f'href="/workflow-runs/{workflow_run_id}/lineage">lineage</a>' in dashboard.text
    assert "derived lineage read model" in dashboard.text


def test_ops_dashboard_surfaces_lineage_warning_code_legend_without_persistence_claims():
    client = make_client()

    client.post(
        "/workflow-runs",
        json={
            "question": "Which sources disagree about memory demand?",
            "trace_json": {"phase": "metadata-only"},
        },
    )

    dashboard = client.get("/ops/dashboard")

    assert dashboard.status_code == 200
    assert "Lineage warning codes" in dashboard.text
    assert "derived_read_model_boundary" in dashboard.text
    assert "local_workflow_scope" in dashboard.text
    assert "missing_manifest_reference" in dashboard.text
    assert "invalid_manifest_shape" in dashboard.text
    assert "response-level taxonomy only" in dashboard.text
    assert "not persisted dashboard analytics" in dashboard.text


def test_ops_summary_placeholder_counts_registered_records():
    client = make_client()

    client.post("/documents", json={"source_type": "memo", "title": "Market memo"})
    client.post("/agent-runs", json={"user_question": "What happened?"})
    client.post(
        "/failure-cases",
        json={"failure_type": "retrieval_failure", "description": "No source ids found."},
    )

    response = client.get("/ops/summary")

    assert response.status_code == 200
    assert response.json()["status"] == "placeholder"
    assert response.json()["document_count"] == 1
    assert response.json()["agent_run_count"] == 1
    assert response.json()["failure_case_count"] == 1
    assert response.json()["unsupported_claim_count"] == 0
    assert response.json()["contradiction_count"] == 0


def test_ops_dashboard_surfaces_runs_failures_and_retrievals():
    client = make_client()

    client.post(
        "/agent-runs",
        json={
            "user_question": "Which sources conflict on demand growth?",
            "status": "failed",
            "latency_ms": 321,
        },
    )
    client.post(
        "/failure-cases",
        json={
            "failure_type": "retrieval_failure",
            "description": "No source ids found for the question.",
            "next_action": "Add a source quality check before report generation.",
        },
    )
    client.post(
        "/retrieval-runs",
        json={
            "question": "semiconductor backlog",
            "strategy": "fixed-window",
            "sources": [
                {
                    "source_id": "doc-unrelated",
                    "source_type": "markdown",
                    "content": "# Weather\nRainfall was heavy in Seoul.",
                }
            ],
        },
    )

    response = client.get("/ops/dashboard")

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    assert "Operations Dashboard v0" in response.text
    assert "Recent Agent Runs" in response.text
    assert "Which sources conflict on demand growth?" in response.text
    assert "Failure Cases" in response.text
    assert "retrieval_failure" in response.text
    assert "Retrieval Runs" in response.text
    assert "semiconductor backlog" in response.text
    assert "Phase 35" in response.text


def test_ops_dashboard_links_failure_cases_to_manual_workflow_parent():
    client = make_client()
    workflow_run = client.post(
        "/workflow-runs",
        json={
            "question": "Which failed workflow should be reviewed?",
            "status": "failed",
            "workflow_version": WORKFLOW_VERSION,
        },
    )
    workflow_run_id = workflow_run.json()["id"]
    client.post(
        "/failure-cases",
        json={
            "workflow_run_id": workflow_run_id,
            "failure_type": "workflow_stage_error",
            "description": "Evidence persistence failed after retrieval.",
            "fix_status": "open",
            "next_action": "Inspect the workflow parent before retry.",
        },
    )

    response = client.get("/ops/dashboard")

    assert response.status_code == 200
    assert "Workflow Parent" in response.text
    assert (
        f'href="/workflow-runs/{workflow_run_id}">{workflow_run_id}</a>'
        in response.text
    )
    assert "manual workflow parent link" in response.text
    assert "not automatic failure-case creation" in response.text


def test_core_preview_endpoints_auto_record_agent_run_traces():
    client = make_client()

    client.post(
        "/collection-plans/preview",
        json={"question": "Did enterprise AI demand become stronger?"},
    )
    client.post(
        "/evidence-ledgers/preview",
        json={
            "question": "Which segment had enterprise demand growth?",
            "retrieval_results": [
                {
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "chunk_strategy": "heading-aware",
                    "chunk_index": 0,
                    "text": "Enterprise demand grew 12% in 2026.",
                    "score": 0.75,
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "metadata": {"source_date": "2026-05-28"},
                }
            ],
        },
    )
    client.post(
        "/noise-gates/preview",
        json={
            "question": "Which segment had enterprise demand growth?",
            "evidence_entries": [
                {
                    "claim": "Enterprise demand grew",
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "source_date": "2026-05-28",
                    "evidence_span": "Enterprise demand grew 12% in 2026.",
                    "confidence": "medium",
                    "limitation": "Supported by one retrieved source.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "role": "direct_support",
                }
            ],
        },
    )
    client.post(
        "/reports/preview",
        json={
            "question": "Which segment had enterprise demand growth?",
            "evidence_entries": [
                {
                    "claim": "Enterprise demand grew",
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "source_date": "2026-05-28",
                    "evidence_span": "Enterprise demand grew 12% in 2026.",
                    "confidence": "medium",
                    "limitation": "Supported by one retrieved source.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "role": "direct_support",
                }
            ],
            "draft_claims": [
                "Enterprise demand grew, with the current evidence limited to one retrieved source."
            ],
        },
    )

    traces = client.get("/agent-runs").json()
    endpoints = {trace["trace_json"]["endpoint"] for trace in traces}
    assert {
        "POST /collection-plans/preview",
        "POST /evidence-ledgers/preview",
        "POST /noise-gates/preview",
        "POST /reports/preview",
    }.issubset(endpoints)
    assert all(trace["workflow_version"] == WORKFLOW_VERSION for trace in traces)
    assert any(trace["trace_json"].get("decision") == "pass" for trace in traces)
    assert any(trace["trace_json"].get("report_status") == "generated" for trace in traces)


def test_evidence_ledger_entries_can_be_persisted_and_listed():
    client = make_client()

    response = client.post(
        "/evidence-ledgers",
        json={
            "question": "Which segment had enterprise demand growth?",
            "retrieval_results": [
                {
                    "source_id": "doc-support",
                    "source_type": "markdown",
                    "chunk_strategy": "heading-aware",
                    "chunk_index": 0,
                    "text": "Enterprise demand grew 12% in 2026.",
                    "score": 0.75,
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "metadata": {"source_date": "2026-05-28"},
                },
                {
                    "source_id": "doc-contradiction",
                    "source_type": "markdown",
                    "chunk_strategy": "heading-aware",
                    "chunk_index": 1,
                    "text": "Enterprise demand declined in the same period.",
                    "score": 0.72,
                    "matched_terms": ["enterprise", "demand"],
                    "metadata": {"source_date": "2026-05-29"},
                },
            ],
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["stored_entry_count"] == 2
    assert {entry["status"] for entry in body["entries"]} == {"supported", "contradicted"}
    assert body["entries"][0]["id"]

    entries = client.get("/evidence-ledgers").json()
    assert len(entries) == 2
    assert {entry["question"] for entry in entries} == {
        "Which segment had enterprise demand growth?"
    }

    traces = client.get("/agent-runs").json()
    assert any(
        trace["trace_json"].get("endpoint") == "POST /evidence-ledgers"
        and trace["trace_json"].get("stored_entry_count") == 2
        for trace in traces
    )


def test_ops_summary_counts_persisted_evidence_ledger_boundaries():
    client = make_client()

    client.post(
        "/evidence-ledgers",
        json={
            "question": "Should I buy this company?",
            "retrieval_results": [],
        },
    )
    client.post(
        "/evidence-ledgers",
        json={
            "question": "Which segment had enterprise demand growth?",
            "retrieval_results": [
                {
                    "source_id": "doc-contradiction",
                    "source_type": "markdown",
                    "chunk_strategy": "heading-aware",
                    "chunk_index": 0,
                    "text": "Enterprise demand declined in 2026.",
                    "score": 0.72,
                    "matched_terms": ["enterprise", "demand"],
                    "metadata": {"source_date": "2026-05-29"},
                }
            ],
        },
    )

    summary = client.get("/ops/summary").json()
    assert summary["unsupported_claim_count"] == 1
    assert summary["contradiction_count"] == 1


def test_noise_gate_records_can_be_persisted_and_listed():
    client = make_client()

    response = client.post(
        "/noise-gates",
        json={
            "question": "Which segment had enterprise demand growth?",
            "evidence_entries": [
                {
                    "claim": "Enterprise demand grew",
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "source_date": "2026-05-28",
                    "evidence_span": "Enterprise demand grew 12% in 2026.",
                    "confidence": "medium",
                    "limitation": "Supported by one retrieved source.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "role": "direct_support",
                }
            ],
            "draft_claims": [
                "Enterprise demand grew, with the current evidence limited to one retrieved source."
            ],
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["id"]
    assert body["decision"] == "pass"
    assert body["final_response_allowed"] is True
    assert body["evidence_entry_count"] == 1
    assert body["draft_claim_count"] == 1

    listed = client.get("/noise-gates").json()
    assert len(listed) == 1
    assert listed[0]["decision"] == "pass"

    traces = client.get("/agent-runs").json()
    assert any(
        trace["trace_json"].get("endpoint") == "POST /noise-gates"
        and trace["trace_json"].get("decision") == "pass"
        and trace["trace_json"].get("phase") == WORKFLOW_VERSION
        for trace in traces
    )


def test_ops_summary_and_dashboard_surface_persisted_noise_gate_records():
    client = make_client()

    client.post(
        "/noise-gates",
        json={
            "question": "Should I buy this company?",
            "evidence_entries": [
                {
                    "claim": "Should I buy this company",
                    "source_id": None,
                    "source_type": None,
                    "source_date": None,
                    "evidence_span": "",
                    "confidence": "none",
                    "limitation": "Question drifts into buy/sell or financial-advice intent.",
                    "contradicting_source_ids": [],
                    "status": "blocked",
                    "matched_terms": [],
                    "role": "user_intent_check",
                }
            ],
            "draft_claims": ["Should I buy this company?"],
        },
    )
    client.post(
        "/noise-gates",
        json={
            "question": "Which segment had enterprise demand growth?",
            "evidence_entries": [
                {
                    "claim": "Enterprise demand grew",
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "source_date": None,
                    "evidence_span": "Enterprise demand grew 12% in 2026.",
                    "confidence": "medium",
                    "limitation": "Supported by one retrieved source.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "role": "direct_support",
                }
            ],
        },
    )

    summary = client.get("/ops/summary").json()
    assert summary["noise_gate_record_count"] == 2
    assert summary["blocked_gate_count"] == 1
    assert summary["revision_gate_count"] == 1

    dashboard = client.get("/ops/dashboard")
    assert "Noise Gate Records" in dashboard.text
    assert "Should I buy this company?" in dashboard.text
    assert "needs_revision" in dashboard.text


def test_report_records_can_be_persisted_and_listed():
    client = make_client()

    response = client.post(
        "/reports",
        json={
            "question": "Which segment had enterprise demand growth?",
            "evidence_entries": [
                {
                    "claim": "Enterprise demand grew",
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "source_date": "2026-05-28",
                    "evidence_span": "Enterprise demand grew 12% in 2026.",
                    "confidence": "medium",
                    "limitation": "Supported by one retrieved source.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "role": "direct_support",
                }
            ],
            "draft_claims": [
                "Enterprise demand grew, with the current evidence limited to one retrieved source."
            ],
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["id"]
    assert body["status"] == "generated"
    assert body["gate_decision"] == "pass"
    assert body["claim_count"] == 1
    assert body["evidence_entry_count"] == 1
    assert body["draft_claim_count"] == 1
    assert body["report"]["claims"][0]["claim"] == "Enterprise demand grew"

    listed = client.get("/reports").json()
    assert len(listed) == 1
    assert listed[0]["status"] == "generated"

    traces = client.get("/agent-runs").json()
    assert any(
        trace["trace_json"].get("endpoint") == "POST /reports"
        and trace["trace_json"].get("report_status") == "generated"
        and trace["trace_json"].get("phase") == WORKFLOW_VERSION
        for trace in traces
    )


def test_ops_summary_and_dashboard_surface_persisted_report_records():
    client = make_client()

    client.post(
        "/reports",
        json={
            "question": "Which segment had enterprise demand growth?",
            "evidence_entries": [
                {
                    "claim": "Enterprise demand grew",
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "source_date": "2026-05-28",
                    "evidence_span": "Enterprise demand grew 12% in 2026.",
                    "confidence": "medium",
                    "limitation": "Supported by one retrieved source.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "role": "direct_support",
                }
            ],
        },
    )
    client.post(
        "/reports",
        json={
            "question": "Should I buy this company?",
            "evidence_entries": [
                {
                    "claim": "Should I buy this company?",
                    "source_id": None,
                    "source_type": None,
                    "source_date": None,
                    "evidence_span": "",
                    "confidence": "none",
                    "limitation": "Question drifts into buy/sell or financial-advice intent.",
                    "contradicting_source_ids": [],
                    "status": "blocked",
                    "matched_terms": [],
                    "role": "user_intent_check",
                }
            ],
            "draft_claims": ["This proves you should buy this company."],
        },
    )

    summary = client.get("/ops/summary").json()
    assert summary["report_record_count"] == 2
    assert summary["generated_report_count"] == 1
    assert summary["blocked_report_count"] == 1
    assert summary["revision_report_count"] == 0

    dashboard = client.get("/ops/dashboard")
    assert "Report Records" in dashboard.text
    assert "Which segment had enterprise demand growth?" in dashboard.text
    assert "Should I buy this company?" in dashboard.text
    assert "generated" in dashboard.text
    assert "blocked" in dashboard.text


def test_persisted_records_share_workflow_trace_id_with_agent_run_trace():
    client = make_client()

    ledger_response = client.post(
        "/evidence-ledgers",
        json={
            "question": "Which segment had enterprise demand growth?",
            "retrieval_results": [
                {
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "chunk_strategy": "heading-aware",
                    "chunk_index": 0,
                    "text": "Enterprise demand grew 12% in 2026.",
                    "score": 0.75,
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "metadata": {"source_date": "2026-05-28"},
                }
            ],
        },
    )
    ledger_trace_id = ledger_response.json()["entries"][0]["workflow_trace_id"]

    gate_response = client.post(
        "/noise-gates",
        json={
            "question": "Which segment had enterprise demand growth?",
            "evidence_entries": [
                {
                    "claim": "Enterprise demand grew",
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "source_date": "2026-05-28",
                    "evidence_span": "Enterprise demand grew 12% in 2026.",
                    "confidence": "medium",
                    "limitation": "Supported by one retrieved source.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "role": "direct_support",
                }
            ],
        },
    )
    gate_trace_id = gate_response.json()["workflow_trace_id"]

    report_response = client.post(
        "/reports",
        json={
            "question": "Which segment had enterprise demand growth?",
            "evidence_entries": [
                {
                    "claim": "Enterprise demand grew",
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "source_date": "2026-05-28",
                    "evidence_span": "Enterprise demand grew 12% in 2026.",
                    "confidence": "medium",
                    "limitation": "Supported by one retrieved source.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "role": "direct_support",
                }
            ],
        },
    )
    report_trace_id = report_response.json()["workflow_trace_id"]

    traces = client.get("/agent-runs").json()
    trace_by_endpoint = {
        trace["trace_json"]["endpoint"]: trace["trace_json"]["workflow_trace_id"]
        for trace in traces
        if "workflow_trace_id" in trace["trace_json"]
    }

    assert trace_by_endpoint["POST /evidence-ledgers"] == ledger_trace_id
    assert trace_by_endpoint["POST /noise-gates"] == gate_trace_id
    assert trace_by_endpoint["POST /reports"] == report_trace_id
    assert len({ledger_trace_id, gate_trace_id, report_trace_id}) == 3


def test_trace_lookup_surfaces_records_for_workflow_trace_id():
    client = make_client()

    report_response = client.post(
        "/reports",
        json={
            "question": "Which segment had enterprise demand growth?",
            "evidence_entries": [
                {
                    "claim": "Enterprise demand grew",
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "source_date": "2026-05-28",
                    "evidence_span": "Enterprise demand grew 12% in 2026.",
                    "confidence": "medium",
                    "limitation": "Supported by one retrieved source.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "role": "direct_support",
                }
            ],
        },
    )
    trace_id = report_response.json()["workflow_trace_id"]

    lookup = client.get(f"/traces/{trace_id}")

    assert lookup.status_code == 200
    body = lookup.json()
    assert body["workflow_trace_id"] == trace_id
    assert body["summary"] == {
        "agent_run_count": 1,
        "evidence_ledger_entry_count": 0,
        "noise_gate_record_count": 0,
        "report_record_count": 1,
    }
    assert body["agent_runs"][0]["trace_json"]["endpoint"] == "POST /reports"
    assert body["report_records"][0]["question"] == "Which segment had enterprise demand growth?"


def test_persisted_child_records_store_parent_agent_run_id():
    client = make_client()

    ledger_response = client.post(
        "/evidence-ledgers",
        json={
            "question": "Which segment had enterprise demand growth?",
            "retrieval_results": [
                {
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "chunk_strategy": "heading-aware",
                    "chunk_index": 0,
                    "text": "Enterprise demand grew 12% in 2026.",
                    "score": 0.75,
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "metadata": {"source_date": "2026-05-28"},
                }
            ],
        },
    )
    gate_response = client.post(
        "/noise-gates",
        json={
            "question": "Which segment had enterprise demand growth?",
            "evidence_entries": [
                {
                    "claim": "Enterprise demand grew",
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "source_date": "2026-05-28",
                    "evidence_span": "Enterprise demand grew 12% in 2026.",
                    "confidence": "medium",
                    "limitation": "Supported by one retrieved source.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "role": "direct_support",
                }
            ],
        },
    )
    report_response = client.post(
        "/reports",
        json={
            "question": "Which segment had enterprise demand growth?",
            "evidence_entries": [
                {
                    "claim": "Enterprise demand grew",
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "source_date": "2026-05-28",
                    "evidence_span": "Enterprise demand grew 12% in 2026.",
                    "confidence": "medium",
                    "limitation": "Supported by one retrieved source.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "role": "direct_support",
                }
            ],
        },
    )

    for trace_id, record_key in [
        (ledger_response.json()["entries"][0]["workflow_trace_id"], "evidence_ledger_entries"),
        (gate_response.json()["workflow_trace_id"], "noise_gate_records"),
        (report_response.json()["workflow_trace_id"], "report_records"),
    ]:
        trace = client.get(f"/traces/{trace_id}").json()
        parent_run_id = trace["agent_runs"][0]["id"]
        child_record = trace[record_key][0]
        assert child_record["agent_run_id"] == parent_run_id


def test_persisted_record_lists_can_filter_by_trace_id_and_status():
    client = make_client()

    ledger_response = client.post(
        "/evidence-ledgers",
        json={
            "question": "Which segment had enterprise demand growth?",
            "retrieval_results": [
                {
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "chunk_strategy": "heading-aware",
                    "chunk_index": 0,
                    "text": "Enterprise demand grew 12% in 2026.",
                    "score": 0.75,
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "metadata": {"source_date": "2026-05-28"},
                }
            ],
        },
    )
    ledger_trace_id = ledger_response.json()["entries"][0]["workflow_trace_id"]

    client.post(
        "/noise-gates",
        json={
            "question": "Should I buy this company?",
            "evidence_entries": [
                {
                    "claim": "Should I buy this company?",
                    "source_id": None,
                    "source_type": None,
                    "source_date": None,
                    "evidence_span": "",
                    "confidence": "none",
                    "limitation": "Question drifts into buy/sell or financial-advice intent.",
                    "contradicting_source_ids": [],
                    "status": "blocked",
                    "matched_terms": [],
                    "role": "user_intent_check",
                }
            ],
            "draft_claims": ["This proves you should buy this company."],
        },
    )
    pass_gate = client.post(
        "/noise-gates",
        json={
            "question": "Which segment had enterprise demand growth?",
            "evidence_entries": [
                {
                    "claim": "Enterprise demand grew",
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "source_date": "2026-05-28",
                    "evidence_span": "Enterprise demand grew 12% in 2026.",
                    "confidence": "medium",
                    "limitation": "Supported by one retrieved source.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "role": "direct_support",
                }
            ],
        },
    )
    gate_trace_id = pass_gate.json()["workflow_trace_id"]

    client.post(
        "/reports",
        json={
            "question": "Should I buy this company?",
            "evidence_entries": [
                {
                    "claim": "Should I buy this company?",
                    "source_id": None,
                    "source_type": None,
                    "source_date": None,
                    "evidence_span": "",
                    "confidence": "none",
                    "limitation": "Question drifts into buy/sell or financial-advice intent.",
                    "contradicting_source_ids": [],
                    "status": "blocked",
                    "matched_terms": [],
                    "role": "user_intent_check",
                }
            ],
            "draft_claims": ["This proves you should buy this company."],
        },
    )
    generated_report = client.post(
        "/reports",
        json={
            "question": "Which segment had enterprise demand growth?",
            "evidence_entries": [
                {
                    "claim": "Enterprise demand grew",
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "source_date": "2026-05-28",
                    "evidence_span": "Enterprise demand grew 12% in 2026.",
                    "confidence": "medium",
                    "limitation": "Supported by one retrieved source.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "role": "direct_support",
                }
            ],
        },
    )
    report_trace_id = generated_report.json()["workflow_trace_id"]

    ledger_by_trace = client.get(f"/evidence-ledgers?workflow_trace_id={ledger_trace_id}")
    gates_by_decision = client.get("/noise-gates?decision=pass")
    gates_by_trace = client.get(f"/noise-gates?workflow_trace_id={gate_trace_id}")
    reports_by_status = client.get("/reports?status=generated")
    reports_by_trace = client.get(f"/reports?workflow_trace_id={report_trace_id}")

    assert [entry["workflow_trace_id"] for entry in ledger_by_trace.json()] == [
        ledger_trace_id
    ]
    assert [record["decision"] for record in gates_by_decision.json()] == ["pass"]
    assert [record["workflow_trace_id"] for record in gates_by_trace.json()] == [
        gate_trace_id
    ]
    assert [record["status"] for record in reports_by_status.json()] == ["generated"]
    assert [record["workflow_trace_id"] for record in reports_by_trace.json()] == [
        report_trace_id
    ]


def test_ops_dashboard_links_to_trace_lookup_and_record_filters():
    client = make_client()

    gate_response = client.post(
        "/noise-gates",
        json={
            "question": "Which segment had enterprise demand growth?",
            "evidence_entries": [
                {
                    "claim": "Enterprise demand grew",
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "source_date": "2026-05-28",
                    "evidence_span": "Enterprise demand grew 12% in 2026.",
                    "confidence": "medium",
                    "limitation": "Supported by one retrieved source.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "role": "direct_support",
                }
            ],
        },
    )
    report_response = client.post(
        "/reports",
        json={
            "question": "Which segment had enterprise demand growth?",
            "evidence_entries": [
                {
                    "claim": "Enterprise demand grew",
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "source_date": "2026-05-28",
                    "evidence_span": "Enterprise demand grew 12% in 2026.",
                    "confidence": "medium",
                    "limitation": "Supported by one retrieved source.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "role": "direct_support",
                }
            ],
        },
    )
    gate_trace_id = gate_response.json()["workflow_trace_id"]
    report_trace_id = report_response.json()["workflow_trace_id"]
    gate_agent_run_id = gate_response.json()["agent_run_id"]
    report_agent_run_id = report_response.json()["agent_run_id"]

    dashboard = client.get("/ops/dashboard")

    assert "Trace & Filter Links" in dashboard.text
    assert "Parent Run" in dashboard.text
    assert f'href="/traces/{gate_trace_id}"' in dashboard.text
    assert f'href="/traces/{report_trace_id}"' in dashboard.text
    assert f'href="/traces/{gate_trace_id}">{gate_agent_run_id}</a>' in dashboard.text
    assert f'href="/traces/{report_trace_id}">{report_agent_run_id}</a>' in dashboard.text
    assert f'href="/noise-gates?workflow_trace_id={gate_trace_id}"' in dashboard.text
    assert f'href="/reports?workflow_trace_id={report_trace_id}"' in dashboard.text
    assert 'href="/evidence-ledgers?status=unsupported"' in dashboard.text
    assert 'href="/noise-gates?decision=needs_revision"' in dashboard.text
    assert 'href="/reports?status=generated"' in dashboard.text


def test_ops_dashboard_surfaces_evidence_ledger_records_with_parent_links():
    client = make_client()

    response = client.post(
        "/evidence-ledgers",
        json={
            "question": "Which segment had enterprise demand growth?",
            "retrieval_results": [
                {
                    "source_id": "doc-support",
                    "source_type": "markdown",
                    "chunk_strategy": "heading-aware",
                    "chunk_index": 0,
                    "text": "Enterprise demand grew 12% in 2026.",
                    "score": 0.75,
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "metadata": {"source_date": "2026-05-28"},
                }
            ],
        },
    )
    body = response.json()
    trace_id = body["entries"][0]["workflow_trace_id"]
    agent_run_id = body["entries"][0]["agent_run_id"]

    dashboard = client.get("/ops/dashboard")

    assert "Evidence Ledger Records" in dashboard.text
    assert "Enterprise demand grew" in dashboard.text
    assert f'href="/traces/{trace_id}">{agent_run_id}</a>' in dashboard.text
    assert f'href="/evidence-ledgers?workflow_trace_id={trace_id}"' in dashboard.text
    assert 'href="/evidence-ledgers?status=supported"' in dashboard.text


def test_document_preview_endpoints_auto_record_agent_run_traces():
    client = make_client()

    client.post(
        "/documents/profile",
        json={"source_type": "markdown", "text": "# Memo\nRevenue grew 12%."},
    )
    client.post(
        "/documents/parse-preview",
        json={"source_type": "markdown", "content": "# Memo\nRevenue grew 12%."},
    )
    client.post(
        "/documents/chunk-preview",
        json={"source_type": "markdown", "content": "# Memo\nRevenue grew 12%."},
    )

    traces = client.get("/agent-runs").json()
    endpoints = {trace["trace_json"]["endpoint"] for trace in traces}
    assert {
        "POST /documents/profile",
        "POST /documents/parse-preview",
        "POST /documents/chunk-preview",
    }.issubset(endpoints)
    assert any(trace["trace_json"]["source_type"] == "markdown" for trace in traces)


def test_run_trace_records_failed_preview_operations():
    repository = InMemoryRepository()

    def failing_operation(_agent_run_id):
        raise ValueError("synthetic preview failure")

    with pytest.raises(ValueError):
        run_with_trace(
            repository,
            endpoint="POST /reports/preview",
            user_question="failed preview?",
            trace_json={"evidence_entry_count": 0},
            operation=failing_operation,
        )

    trace = repository.list_agent_runs()[0]
    assert trace["status"] == "failed"
    assert trace["ended_at"] is not None
    assert trace["error_message"] == "synthetic preview failure"
    assert trace["trace_json"]["endpoint"] == "POST /reports/preview"
    assert trace["trace_json"]["error_type"] == "ValueError"


def test_run_trace_creates_parent_run_before_operation_and_updates_it():
    repository = InMemoryRepository()
    observed_parent_ids = []

    def operation(agent_run_id):
        rows = repository.list_agent_runs()
        assert len(rows) == 1
        assert rows[0]["id"] == agent_run_id
        assert rows[0]["status"] == "running"
        assert rows[0]["ended_at"] is None
        observed_parent_ids.append(agent_run_id)
        return {"stored_entry_count": 1}

    result = run_with_trace(
        repository,
        endpoint="POST /evidence-ledgers",
        user_question="Which segment had enterprise demand growth?",
        trace_json={"workflow_trace_id": str(uuid4())},
        operation=operation,
        trace_from_result=lambda value: {
            "stored_entry_count": value["stored_entry_count"]
        },
    )

    rows = repository.list_agent_runs()
    assert result == {"stored_entry_count": 1}
    assert len(rows) == 1
    assert rows[0]["id"] == observed_parent_ids[0]
    assert rows[0]["status"] == "completed"
    assert rows[0]["ended_at"] is not None
    assert rows[0]["latency_ms"] is not None
    assert rows[0]["trace_json"]["endpoint"] == "POST /evidence-ledgers"
    assert rows[0]["trace_json"]["stored_entry_count"] == 1


def test_document_profile_endpoint_detects_fixture_signals():
    client = make_client()

    payload = {
        "source_type": "markdown",
        "text": "# Memo\nDate: 2026-05-28\nSource: https://example.com\nRevenue grew 12%.",
    }

    response = client.post("/documents/profile", json=payload)

    assert response.status_code == 200
    body = response.json()
    assert body["source_type"] == "markdown"
    assert body["character_count"] == len(payload["text"])
    assert body["line_count"] == 4
    assert body["approximate_token_count"] > 0
    assert body["has_urls"] is True
    assert body["has_dates"] is True
    assert body["has_numbers"] is True
    assert body["recommended_strategy"] == "heading-aware"
    assert body["extraction_quality"] in {"high", "medium"}


def test_document_profile_endpoint_recommends_row_aware_for_csv():
    client = make_client()

    response = client.post(
        "/documents/profile",
        json={
            "source_type": "csv",
            "text": "date,segment,growth\n2026-05-28,enterprise,12%\n",
        },
    )

    assert response.status_code == 200
    assert response.json()["has_tables"] is True
    assert response.json()["recommended_strategy"] == "row-aware"


def test_parse_preview_markdown_returns_heading_metadata_and_profile():
    client = make_client()

    response = client.post(
        "/documents/parse-preview",
        json={
            "source_type": "markdown",
            "content": "# Market memo\n\n- Demand grew 12% on 2026-05-28.\n- Source: https://example.com",
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["source_type"] == "markdown"
    assert body["parser"] == "markdown"
    assert body["metadata"]["heading_count"] == 1
    assert body["metadata"]["bullet_count"] == 2
    assert body["profile"]["recommended_strategy"] == "heading-aware"
    assert body["profile"]["has_dates"] is True
    assert body["profile"]["has_numbers"] is True


def test_parse_preview_csv_returns_row_and_column_metadata():
    client = make_client()

    response = client.post(
        "/documents/parse-preview",
        json={
            "source_type": "csv",
            "content": "date,segment,growth\n2026-05-28,enterprise,12%\n",
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["parser"] == "csv"
    assert body["metadata"]["row_count"] == 2
    assert body["metadata"]["column_count"] == 3
    assert body["metadata"]["headers"] == ["date", "segment", "growth"]
    assert body["profile"]["recommended_strategy"] == "row-aware"


def test_parse_preview_html_strips_tags_and_reports_links():
    client = make_client()

    response = client.post(
        "/documents/parse-preview",
        json={
            "source_type": "html",
            "content": "<html><body><h1>Market update</h1><p>Revenue grew 9%.</p><a href='https://example.com/report'>report</a></body></html>",
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["parser"] == "html"
    assert "<h1>" not in body["text"]
    assert "Market update" in body["text"]
    assert body["metadata"]["heading_count"] == 1
    assert body["metadata"]["link_count"] == 1
    assert body["metadata"]["links"] == ["https://example.com/report"]


def test_parse_preview_pdf_is_text_only_fallback_without_robust_claim():
    client = make_client()

    response = client.post(
        "/documents/parse-preview",
        json={
            "source_type": "pdf",
            "content": "Extracted PDF text preview. Revenue grew 9% in 2026.",
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["parser"] == "pdf-text-fallback"
    assert body["metadata"]["robust_pdf_extraction"] is False
    assert body["metadata"]["text_only_fallback"] is True
    assert any("robust PDF extraction is not claimed" in warning for warning in body["warnings"])
    assert body["failure_case_candidate"] is None


def test_parse_preview_unknown_source_type_returns_structured_failure_candidate():
    client = make_client()

    response = client.post(
        "/documents/parse-preview",
        json={"source_type": "spreadsheet-binary", "content": "opaque bytes"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["parser"] == "unknown"
    assert body["warnings"]
    assert body["failure_case_candidate"]["failure_type"] == "unknown_source_type"
    assert body["profile"]["extraction_quality"] == "empty"


def test_parse_preview_bad_csv_exposes_failure_case_candidate():
    client = make_client()

    response = client.post(
        "/documents/parse-preview",
        json={"source_type": "csv", "content": "date,segment,growth\n2026-05-28,enterprise\n"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["metadata"]["inconsistent_row_count"] == 1
    assert body["failure_case_candidate"]["failure_type"] == "csv_inconsistent_rows"


def test_chunk_preview_compares_three_strategies_for_markdown():
    client = make_client()

    response = client.post(
        "/documents/chunk-preview",
        json={
            "source_type": "markdown",
            "content": "# Market\nRevenue grew 12% in 2026.\n\n## Risks\nCosts rose 7%.\n\n## Sources\nSource: https://example.com/report",
            "max_characters": 80,
            "overlap": 10,
        },
    )

    assert response.status_code == 200
    body = response.json()
    strategy_names = {strategy["strategy"] for strategy in body["strategies"]}
    assert strategy_names == {"fixed-window", "heading-aware", "row-aware"}
    assert body["parser"] == "markdown"
    assert body["profile"]["recommended_strategy"] == "heading-aware"

    heading_strategy = next(
        strategy for strategy in body["strategies"] if strategy["strategy"] == "heading-aware"
    )
    assert heading_strategy["metrics"]["chunk_count"] >= 2
    assert heading_strategy["metrics"]["oversized_chunk_count"] == 0
    assert any(chunk["metadata"].get("header_path") == "Market/Risks" for chunk in heading_strategy["chunks"])

    fixed_strategy = next(
        strategy for strategy in body["strategies"] if strategy["strategy"] == "fixed-window"
    )
    assert all(chunk["character_count"] <= 80 for chunk in fixed_strategy["chunks"])


def test_chunk_preview_csv_row_aware_preserves_header_and_row_metadata():
    client = make_client()

    response = client.post(
        "/documents/chunk-preview",
        json={
            "source_type": "csv",
            "content": "date,segment,growth\n2026-05-28,enterprise,12%\n2026-05-29,smb,7%\n",
            "max_characters": 60,
        },
    )

    assert response.status_code == 200
    body = response.json()
    row_strategy = next(
        strategy for strategy in body["strategies"] if strategy["strategy"] == "row-aware"
    )
    assert row_strategy["metrics"]["chunk_count"] == 2
    assert row_strategy["metrics"]["source_line_count"] == 3
    assert row_strategy["chunks"][0]["metadata"]["headers"] == ["date", "segment", "growth"]
    assert row_strategy["chunks"][0]["metadata"]["row_start"] == 1
    assert "date,segment,growth" in row_strategy["chunks"][0]["text"]


def test_chunk_preview_unknown_source_type_keeps_parse_failure_candidate():
    client = make_client()

    response = client.post(
        "/documents/chunk-preview",
        json={"source_type": "spreadsheet-binary", "content": "opaque bytes"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["parser"] == "unknown"
    assert body["failure_case_candidate"]["failure_type"] == "unknown_source_type"
    assert body["strategies"] == []


def test_retrieval_run_returns_ranked_chunk_candidates_with_source_ids():
    client = make_client()

    response = client.post(
        "/retrieval-runs",
        json={
            "question": "Which segment had enterprise demand growth?",
            "strategy": "heading-aware",
            "top_k": 2,
            "sources": [
                {
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "content": "# Demand\nEnterprise demand grew 12% in 2026.\n\n## Risks\nCosts rose 7%.",
                },
                {
                    "source_id": "doc-noise",
                    "source_type": "markdown",
                    "content": "# Weather\nRainfall was heavy in Seoul.",
                },
            ],
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["question"] == "Which segment had enterprise demand growth?"
    assert body["strategy"] == "heading-aware"
    assert body["result_count"] == 1
    assert body["missing_evidence_count"] == 0
    assert body["results"][0]["source_id"] == "doc-demand"
    assert body["results"][0]["chunk_strategy"] == "heading-aware"
    assert body["results"][0]["score"] > 0
    assert {"enterprise", "demand", "growth"}.issubset(set(body["results"][0]["matched_terms"]))
    assert "Enterprise demand grew" in body["results"][0]["text"]

    listed = client.get("/retrieval-runs")
    assert listed.status_code == 200
    assert listed.json()[0]["id"] == body["id"]
    assert listed.json()[0]["result_count"] == 1
    assert "results" not in listed.json()[0]


def test_retrieval_run_records_no_results_case():
    client = make_client()

    response = client.post(
        "/retrieval-runs",
        json={
            "question": "semiconductor backlog",
            "strategy": "fixed-window",
            "sources": [
                {
                    "source_id": "doc-unrelated",
                    "source_type": "markdown",
                    "content": "# Weather\nRainfall was heavy in Seoul.",
                }
            ],
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["results"] == []
    assert body["result_count"] == 0
    assert body["missing_evidence_count"] == 1
    assert body["status"] == "no_results"

    listed = client.get("/retrieval-runs")
    assert listed.status_code == 200
    assert listed.json()[0]["status"] == "no_results"
    assert listed.json()[0]["missing_evidence_count"] == 1


def test_document_retrieval_run_persists_candidates_from_existing_chunks():
    client = make_client()

    document = client.post(
        "/documents",
        json={
            "source_type": "markdown",
            "source_uri": "upload://sample.md",
            "filename": "sample.md",
            "title": "Sample market note",
        },
    ).json()
    demand_chunk = client.post(
        f"/documents/{document['id']}/chunks",
        json={
            "source_type": "markdown",
            "source_uri": "upload://sample.md",
            "filename": "sample.md",
            "chunk_strategy": "fixed-window",
            "chunk_index": 0,
            "chunk_text": "Enterprise demand growth reached 12% in 2026.",
            "metadata_json": {"header_path": ["Demand"]},
        },
    ).json()
    client.post(
        f"/documents/{document['id']}/chunks",
        json={
            "source_type": "markdown",
            "source_uri": "upload://sample.md",
            "filename": "sample.md",
            "chunk_strategy": "fixed-window",
            "chunk_index": 1,
            "chunk_text": "Weather noise was unrelated to the market question.",
            "metadata_json": {"header_path": ["Noise"]},
        },
    )

    response = client.post(
        f"/documents/{document['id']}/retrieval-runs",
        json={
            "question": "Which chunk supports enterprise demand growth?",
            "strategy": "fixed-window",
            "top_k": 2,
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["question"] == "Which chunk supports enterprise demand growth?"
    assert body["strategy"] == "fixed-window"
    assert body["status"] == "completed"
    assert body["result_count"] == 1
    assert body["missing_evidence_count"] == 0
    assert body["metadata_json"]["source_table"] == "document_chunks"
    assert body["metadata_json"]["document_id"] == document["id"]
    assert body["metadata_json"]["candidate_chunk_ids"] == [demand_chunk["id"]]
    assert body["metadata_json"]["source_count"] == 2
    assert body["metadata_json"]["top_k"] == 2
    assert body["results"][0]["source_id"] == demand_chunk["id"]
    assert body["results"][0]["metadata"]["chunk_id"] == demand_chunk["id"]
    assert body["results"][0]["metadata"]["document_id"] == document["id"]
    assert body["results"][0]["metadata"]["source_table"] == "document_chunks"
    assert "Enterprise demand growth" in body["results"][0]["text"]
    assert {
        "enterprise",
        "demand",
        "growth",
    }.issubset(set(body["results"][0]["matched_terms"]))
    assert any("existing document_chunks" in warning for warning in body["warnings"])
    assert any("not financial advice" in warning for warning in body["warnings"])

    listed = client.get("/retrieval-runs")
    assert listed.status_code == 200
    stored = listed.json()[0]
    assert stored["id"] == body["id"]
    assert stored["metadata_json"]["source_table"] == "document_chunks"
    assert stored["metadata_json"]["candidate_chunk_ids"] == [demand_chunk["id"]]
    assert stored["metadata_json"]["persistence_boundary"] == (
        "document_chunk_retrieval_run_only_no_evidence_ledger"
    )


def test_document_retrieval_run_records_no_results_when_document_has_no_chunks():
    client = make_client()

    document = client.post(
        "/documents",
        json={
            "source_type": "markdown",
            "source_uri": "upload://empty.md",
            "filename": "empty.md",
            "title": "Empty note",
        },
    ).json()

    response = client.post(
        f"/documents/{document['id']}/retrieval-runs",
        json={
            "question": "enterprise demand growth",
            "strategy": "fixed-window",
            "top_k": 3,
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["status"] == "no_results"
    assert body["results"] == []
    assert body["result_count"] == 0
    assert body["missing_evidence_count"] == 1
    assert body["metadata_json"]["source_table"] == "document_chunks"
    assert body["metadata_json"]["document_id"] == document["id"]
    assert body["metadata_json"]["candidate_chunk_ids"] == []
    assert body["metadata_json"]["source_count"] == 0
    assert any("No persisted document_chunks" in warning for warning in body["warnings"])

    listed = client.get("/retrieval-runs")
    assert listed.status_code == 200
    assert listed.json()[0]["status"] == "no_results"
    assert listed.json()[0]["metadata_json"]["candidate_chunk_ids"] == []


def test_retrieval_run_can_generate_persisted_evidence_ledger_from_candidate_chunks():
    client = make_client()

    document = client.post(
        "/documents",
        json={
            "source_type": "markdown",
            "source_uri": "upload://sample.md",
            "filename": "sample.md",
            "title": "Sample market note",
        },
    ).json()
    demand_chunk = client.post(
        f"/documents/{document['id']}/chunks",
        json={
            "source_type": "markdown",
            "source_uri": "upload://sample.md",
            "filename": "sample.md",
            "chunk_strategy": "fixed-window",
            "chunk_index": 0,
            "chunk_text": "Enterprise demand growth reached 12% in 2026.",
            "metadata_json": {"header_path": ["Demand"]},
        },
    ).json()
    client.post(
        f"/documents/{document['id']}/chunks",
        json={
            "source_type": "markdown",
            "source_uri": "upload://sample.md",
            "filename": "sample.md",
            "chunk_strategy": "fixed-window",
            "chunk_index": 1,
            "chunk_text": "Weather noise was unrelated to the market question.",
            "metadata_json": {"header_path": ["Noise"]},
        },
    )
    retrieval_run = client.post(
        f"/documents/{document['id']}/retrieval-runs",
        json={
            "question": "Which chunk supports enterprise demand growth?",
            "strategy": "fixed-window",
            "top_k": 2,
        },
    ).json()

    response = client.post(f"/retrieval-runs/{retrieval_run['id']}/evidence-ledger")

    assert response.status_code == 201
    body = response.json()
    assert body["question"] == retrieval_run["question"]
    assert body["stored_entry_count"] == 1
    assert body["summary"]["supported_count"] == 1
    assert body["entries"][0]["retrieval_run_id"] == retrieval_run["id"]
    assert body["entries"][0]["source_id"] == demand_chunk["id"]
    assert body["entries"][0]["status"] == "supported"
    assert "Enterprise demand growth" in body["entries"][0]["evidence_span"]
    assert any("persisted retrieval_run" in warning for warning in body["warnings"])
    assert any("no LLM" in warning for warning in body["warnings"])

    listed = client.get("/evidence-ledgers")
    assert listed.status_code == 200
    assert listed.json()[0]["retrieval_run_id"] == retrieval_run["id"]


def test_retrieval_run_can_generate_persisted_noise_gate_from_linked_ledger_entries():
    client = make_client()

    document = client.post(
        "/documents",
        json={
            "source_type": "markdown",
            "source_uri": "upload://sample.md",
            "filename": "sample.md",
            "title": "Sample market note",
        },
    ).json()
    client.post(
        f"/documents/{document['id']}/chunks",
        json={
            "source_type": "markdown",
            "source_uri": "upload://sample.md",
            "filename": "sample.md",
            "chunk_strategy": "fixed-window",
            "chunk_index": 0,
            "chunk_text": "Enterprise demand growth reached 12% in 2026.",
            "metadata_json": {"header_path": ["Demand"]},
        },
    )
    retrieval_run = client.post(
        f"/documents/{document['id']}/retrieval-runs",
        json={
            "question": "Which chunk supports enterprise demand growth?",
            "strategy": "fixed-window",
            "top_k": 1,
        },
    ).json()
    ledger = client.post(f"/retrieval-runs/{retrieval_run['id']}/evidence-ledger").json()

    response = client.post(f"/retrieval-runs/{retrieval_run['id']}/noise-gate")

    assert response.status_code == 201
    body = response.json()
    assert body["question"] == retrieval_run["question"]
    assert body["decision"] in {"pass", "needs_revision"}
    assert body["evidence_entry_count"] == ledger["stored_entry_count"]
    assert body["draft_claim_count"] == 0
    assert body["stage_input_manifest"]["retrieval_run_id"] == retrieval_run["id"]
    assert body["stage_input_manifest"]["input_evidence_ledger_entry_ids"] == [
        ledger["entries"][0]["id"]
    ]
    assert any("retrieval_run-linked Evidence Ledger" in warning for warning in body["warnings"])
    assert any("does not call an LLM" in warning for warning in body["warnings"])

    listed = client.get("/noise-gates")
    assert listed.status_code == 200
    assert listed.json()[0]["stage_input_manifest"]["retrieval_run_id"] == retrieval_run["id"]


def test_retrieval_run_noise_gate_requires_linked_ledger_entries_first():
    client = make_client()

    document = client.post(
        "/documents",
        json={
            "source_type": "markdown",
            "source_uri": "upload://sample.md",
            "filename": "sample.md",
            "title": "Sample market note",
        },
    ).json()
    client.post(
        f"/documents/{document['id']}/chunks",
        json={
            "source_type": "markdown",
            "source_uri": "upload://sample.md",
            "filename": "sample.md",
            "chunk_strategy": "fixed-window",
            "chunk_index": 0,
            "chunk_text": "Enterprise demand growth reached 12% in 2026.",
            "metadata_json": {"header_path": ["Demand"]},
        },
    )
    retrieval_run = client.post(
        f"/documents/{document['id']}/retrieval-runs",
        json={
            "question": "Which chunk supports enterprise demand growth?",
            "strategy": "fixed-window",
            "top_k": 1,
        },
    ).json()

    response = client.post(f"/retrieval-runs/{retrieval_run['id']}/noise-gate")

    assert response.status_code == 409
    assert "Run POST /retrieval-runs/{retrieval_run_id}/evidence-ledger first" in response.json()[
        "detail"
    ]
    assert client.get("/noise-gates").json() == []


def test_retrieval_run_can_generate_persisted_report_from_linked_gate_and_ledger():
    client = make_client()

    document = client.post(
        "/documents",
        json={
            "source_type": "markdown",
            "source_uri": "upload://sample.md",
            "filename": "sample.md",
            "title": "Sample market note",
        },
    ).json()
    client.post(
        f"/documents/{document['id']}/chunks",
        json={
            "source_type": "markdown",
            "source_uri": "upload://sample.md",
            "filename": "sample.md",
            "chunk_strategy": "fixed-window",
            "chunk_index": 0,
            "chunk_text": "Enterprise demand growth reached 12% in 2026.",
            "metadata_json": {"header_path": ["Demand"]},
        },
    )
    retrieval_run = client.post(
        f"/documents/{document['id']}/retrieval-runs",
        json={
            "question": "Which chunk supports enterprise demand growth?",
            "strategy": "fixed-window",
            "top_k": 1,
        },
    ).json()
    ledger = client.post(f"/retrieval-runs/{retrieval_run['id']}/evidence-ledger").json()
    gate = client.post(f"/retrieval-runs/{retrieval_run['id']}/noise-gate").json()

    response = client.post(f"/retrieval-runs/{retrieval_run['id']}/report")

    assert response.status_code == 201
    body = response.json()
    assert body["question"] == retrieval_run["question"]
    assert body["status"] in {"generated", "needs_revision", "blocked"}
    assert body["evidence_entry_count"] == ledger["stored_entry_count"]
    assert body["draft_claim_count"] == 0
    assert body["stage_input_manifest"]["retrieval_run_id"] == retrieval_run["id"]
    assert body["stage_input_manifest"]["input_evidence_ledger_entry_ids"] == [
        ledger["entries"][0]["id"]
    ]
    assert body["stage_input_manifest"]["input_noise_gate_record_id"] == gate["id"]
    assert any("retrieval_run-linked Noise Gate" in warning for warning in body["warnings"])
    assert any("does not call an LLM" in warning for warning in body["warnings"])

    listed = client.get("/reports")
    assert listed.status_code == 200
    assert listed.json()[0]["stage_input_manifest"]["retrieval_run_id"] == retrieval_run["id"]


def test_retrieval_run_report_requires_linked_noise_gate_first():
    client = make_client()

    document = client.post(
        "/documents",
        json={
            "source_type": "markdown",
            "source_uri": "upload://sample.md",
            "filename": "sample.md",
            "title": "Sample market note",
        },
    ).json()
    client.post(
        f"/documents/{document['id']}/chunks",
        json={
            "source_type": "markdown",
            "source_uri": "upload://sample.md",
            "filename": "sample.md",
            "chunk_strategy": "fixed-window",
            "chunk_index": 0,
            "chunk_text": "Enterprise demand growth reached 12% in 2026.",
            "metadata_json": {"header_path": ["Demand"]},
        },
    )
    retrieval_run = client.post(
        f"/documents/{document['id']}/retrieval-runs",
        json={
            "question": "Which chunk supports enterprise demand growth?",
            "strategy": "fixed-window",
            "top_k": 1,
        },
    ).json()
    client.post(f"/retrieval-runs/{retrieval_run['id']}/evidence-ledger")

    response = client.post(f"/retrieval-runs/{retrieval_run['id']}/report")

    assert response.status_code == 409
    assert "Run POST /retrieval-runs/{retrieval_run_id}/noise-gate first" in response.json()[
        "detail"
    ]
    assert client.get("/reports").json() == []


def test_collection_plan_preview_for_general_market_question():
    client = make_client()

    response = client.post(
        "/collection-plans/preview",
        json={"question": "Did this company's AI narrative become materially stronger?"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["question"] == "Did this company's AI narrative become materially stronger?"
    assert "AI narrative" in body["information_need"]
    assert body["possible_claims"]
    assert {
        "direct_support",
        "contradiction",
        "timeline_anchor",
        "missing_data_signal",
    }.issubset(set(body["required_roles"]))
    assert "company_statement" in body["source_types_to_check"]
    assert any("not judge truth" in warning for warning in body["warnings"])


def test_collection_plan_preview_for_underspecified_question():
    client = make_client()

    response = client.post("/collection-plans/preview", json={"question": "Tell me about AI"})

    assert response.status_code == 200
    body = response.json()
    assert "definition_anchor" in body["required_roles"]
    assert "scope_boundary" in body["required_roles"]
    assert "missing_data_signal" in body["required_roles"]
    assert any("underspecified" in warning for warning in body["warnings"])
    assert any("question is underspecified" in condition for condition in body["stop_conditions"])


def test_collection_plan_preview_blocks_buy_sell_drift():
    client = make_client()

    response = client.post(
        "/collection-plans/preview",
        json={"question": "Should I buy Tesla stock after the AI announcement?"},
    )

    assert response.status_code == 200
    body = response.json()
    assert "user_intent_check" in body["required_roles"]
    assert any("buy/sell" in condition for condition in body["stop_conditions"])
    assert any("trading advice" in risk for risk in body["known_risks"])
    assert any("does not provide buy/sell recommendations" in warning for warning in body["warnings"])


def test_collection_plan_preview_for_question_requiring_numbers():
    client = make_client()

    response = client.post(
        "/collection-plans/preview",
        json={"question": "Did revenue grow by 20% in 2026?"},
    )

    assert response.status_code == 200
    body = response.json()
    assert "quantitative_anchor" in body["required_roles"]
    assert "timeline_anchor" in body["required_roles"]
    assert "financial_report" in body["source_types_to_check"]
    assert "At least one quantitative anchor" in body["minimum_evidence_needed"]


def test_collection_plan_preview_for_source_quality_question():
    client = make_client()

    response = client.post(
        "/collection-plans/preview",
        json={"question": "Is this anonymous rumor about enterprise demand reliable?"},
    )

    assert response.status_code == 200
    body = response.json()
    assert "source_quality_check" in body["required_roles"]
    assert "contradiction" in body["required_roles"]
    assert any("source quality" in risk for risk in body["known_risks"])
    assert any("source quality cannot be checked" in condition for condition in body["stop_conditions"])


def test_evidence_ledger_preview_promotes_retrieval_candidate_to_supported_entry():
    client = make_client()

    response = client.post(
        "/evidence-ledgers/preview",
        json={
            "question": "Which segment had enterprise demand growth?",
            "retrieval_results": [
                {
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "chunk_strategy": "heading-aware",
                    "chunk_index": 0,
                    "text": "Enterprise demand grew 12% in 2026.",
                    "score": 0.75,
                    "matched_terms": ["demand", "enterprise", "growth"],
                    "metadata": {"source_date": "2026-05-28"},
                }
            ],
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["question"] == "Which segment had enterprise demand growth?"
    assert body["summary"]["supported_count"] == 1
    assert body["summary"]["blocked_count"] == 0
    assert body["entries"][0]["status"] == "supported"
    assert body["entries"][0]["source_id"] == "doc-demand"
    assert body["entries"][0]["source_date"] == "2026-05-28"
    assert "Enterprise demand grew" in body["entries"][0]["evidence_span"]
    assert "lexical retrieval candidate" in body["entries"][0]["limitation"]
    assert any("does not judge final truth" in warning for warning in body["warnings"])


def test_evidence_ledger_preview_blocks_when_retrieval_has_no_evidence():
    client = make_client()

    response = client.post(
        "/evidence-ledgers/preview",
        json={
            "question": "Was semiconductor backlog reduced?",
            "retrieval_results": [],
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["summary"]["blocked_count"] == 1
    assert body["summary"]["supported_count"] == 0
    assert body["entries"][0]["status"] == "blocked"
    assert body["entries"][0]["source_id"] is None
    assert "No retrieval candidates" in body["entries"][0]["limitation"]


def test_evidence_ledger_preview_surfaces_contradicting_sources():
    client = make_client()

    response = client.post(
        "/evidence-ledgers/preview",
        json={
            "question": "Did enterprise demand grow?",
            "retrieval_results": [
                {
                    "source_id": "doc-support",
                    "source_type": "markdown",
                    "chunk_strategy": "fixed-window",
                    "chunk_index": 0,
                    "text": "Enterprise demand grew 12% this quarter.",
                    "score": 0.8,
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "metadata": {},
                },
                {
                    "source_id": "doc-contradiction",
                    "source_type": "markdown",
                    "chunk_strategy": "fixed-window",
                    "chunk_index": 0,
                    "text": "Enterprise demand declined and no growth was observed this quarter.",
                    "score": 0.8,
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "metadata": {},
                },
            ],
        },
    )

    assert response.status_code == 200
    body = response.json()
    statuses = {entry["source_id"]: entry["status"] for entry in body["entries"]}
    assert statuses["doc-support"] == "supported"
    assert statuses["doc-contradiction"] == "contradicted"
    support_entry = next(entry for entry in body["entries"] if entry["source_id"] == "doc-support")
    contradiction_entry = next(
        entry for entry in body["entries"] if entry["source_id"] == "doc-contradiction"
    )
    assert support_entry["contradicting_source_ids"] == ["doc-contradiction"]
    assert contradiction_entry["contradicting_source_ids"] == ["doc-support"]
    assert body["summary"]["contradicted_count"] == 1


def test_evidence_ledger_preview_blocks_buy_sell_drift():
    client = make_client()

    response = client.post(
        "/evidence-ledgers/preview",
        json={
            "question": "Should I buy this stock after earnings?",
            "retrieval_results": [
                {
                    "source_id": "doc-earnings",
                    "source_type": "markdown",
                    "chunk_strategy": "fixed-window",
                    "chunk_index": 0,
                    "text": "Revenue grew 12% after earnings.",
                    "score": 0.7,
                    "matched_terms": ["earnings", "growth"],
                    "metadata": {},
                }
            ],
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["summary"]["blocked_count"] == 1
    assert body["entries"][0]["status"] == "blocked"
    assert body["entries"][0]["source_id"] is None
    assert "buy/sell" in body["entries"][0]["limitation"]
    assert any("financial advice" in warning for warning in body["warnings"])


def test_noise_gate_preview_allows_supported_bounded_ledger_entry():
    client = make_client()

    response = client.post(
        "/noise-gates/preview",
        json={
            "question": "Which segment had enterprise demand growth?",
            "evidence_entries": [
                {
                    "claim": "Enterprise demand grew",
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "source_date": "2026-05-28",
                    "evidence_span": "Enterprise demand grew 12% in 2026.",
                    "confidence": "medium",
                    "limitation": "Supported by a lexical retrieval candidate; not yet validated externally.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "role": "direct_support",
                }
            ],
            "draft_claims": [
                "Enterprise demand grew, with the current evidence limited to one retrieved source."
            ],
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["decision"] == "pass"
    assert body["final_response_allowed"] is True
    assert body["blocked_claims"] == []
    assert any(check["name"] == "every_strong_claim_has_evidence" for check in body["checks"])
    assert any("does not generate a report" in warning for warning in body["warnings"])


def test_noise_gate_preview_blocks_unsupported_entries():
    client = make_client()

    response = client.post(
        "/noise-gates/preview",
        json={
            "question": "Was backlog reduced?",
            "evidence_entries": [
                {
                    "claim": "Backlog was reduced",
                    "source_id": None,
                    "source_type": None,
                    "source_date": None,
                    "evidence_span": "",
                    "confidence": "none",
                    "limitation": "No retrieval candidates were provided.",
                    "contradicting_source_ids": [],
                    "status": "blocked",
                    "matched_terms": [],
                    "role": "missing_data_signal",
                }
            ],
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["decision"] == "blocked"
    assert body["final_response_allowed"] is False
    assert body["fallback_message"].startswith("현재 근거만으로는 결론을 내릴 수 없습니다")
    assert body["blocked_claims"] == ["Backlog was reduced"]
    assert any(check["name"] == "unsupported_claim_blocking" for check in body["checks"])


def test_noise_gate_preview_requires_revision_for_contradictions_and_missing_recency():
    client = make_client()

    response = client.post(
        "/noise-gates/preview",
        json={
            "question": "Did enterprise demand grow?",
            "evidence_entries": [
                {
                    "claim": "Enterprise demand grew",
                    "source_id": "doc-support",
                    "source_type": "markdown",
                    "source_date": None,
                    "evidence_span": "Enterprise demand grew 12% this quarter.",
                    "confidence": "medium",
                    "limitation": "Supported by one retrieved source.",
                    "contradicting_source_ids": ["doc-contradiction"],
                    "status": "supported",
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "role": "direct_support",
                },
                {
                    "claim": "Enterprise demand grew",
                    "source_id": "doc-contradiction",
                    "source_type": "markdown",
                    "source_date": None,
                    "evidence_span": "Enterprise demand declined and no growth was observed.",
                    "confidence": "low",
                    "limitation": "Candidate contains contradiction language.",
                    "contradicting_source_ids": ["doc-support"],
                    "status": "contradicted",
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "role": "contradiction",
                },
            ],
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["decision"] == "needs_revision"
    assert body["final_response_allowed"] is False
    assert "Enterprise demand grew" in body["downgraded_claims"]
    assert any(check["name"] == "contradictions_are_surfaced" for check in body["checks"])
    assert any(check["name"] == "source_recency_visible" for check in body["checks"])


def test_noise_gate_preview_blocks_trading_advice_and_overconfident_draft():
    client = make_client()

    response = client.post(
        "/noise-gates/preview",
        json={
            "question": "Should I buy this stock after earnings?",
            "evidence_entries": [
                {
                    "claim": "Revenue grew after earnings",
                    "source_id": "doc-earnings",
                    "source_type": "markdown",
                    "source_date": "2026-05-28",
                    "evidence_span": "Revenue grew 12% after earnings.",
                    "confidence": "medium",
                    "limitation": "Supported by one retrieved source.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["revenue", "earnings"],
                    "role": "direct_support",
                }
            ],
            "draft_claims": ["This proves you should buy the stock."],
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["decision"] == "blocked"
    assert body["final_response_allowed"] is False
    assert any(check["name"] == "trading_advice_drift" for check in body["checks"])
    assert any(check["name"] == "overconfident_language" for check in body["checks"])
    assert any("buy/sell" in revision for revision in body["required_revisions"])


def test_noise_gate_preview_requires_two_sources_for_high_confidence():
    client = make_client()

    response = client.post(
        "/noise-gates/preview",
        json={
            "question": "Did revenue grow by 20% in 2026?",
            "evidence_entries": [
                {
                    "claim": "Revenue grew by 20%",
                    "source_id": "doc-revenue",
                    "source_type": "markdown",
                    "source_date": "2026-05-28",
                    "evidence_span": "Revenue grew by 20% in 2026.",
                    "confidence": "high",
                    "limitation": "Supported by one retrieved source.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["revenue", "growth", "20"],
                    "role": "quantitative_anchor",
                }
            ],
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["decision"] == "needs_revision"
    assert body["final_response_allowed"] is False
    assert body["downgraded_claims"] == ["Revenue grew by 20%"]
    assert any(check["name"] == "high_confidence_has_two_sources" for check in body["checks"])


def test_report_preview_generates_claim_bounded_report_after_passing_gate():
    client = make_client()

    response = client.post(
        "/reports/preview",
        json={
            "question": "Which segment had enterprise demand growth?",
            "evidence_entries": [
                {
                    "claim": "Enterprise demand grew",
                    "source_id": "doc-demand",
                    "source_type": "markdown",
                    "source_date": "2026-05-28",
                    "evidence_span": "Enterprise demand grew 12% in 2026.",
                    "confidence": "medium",
                    "limitation": "Supported by one retrieved source.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "role": "direct_support",
                }
            ],
            "draft_claims": [
                "Enterprise demand grew, with the current evidence limited to one retrieved source."
            ],
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "generated"
    assert body["gate"]["decision"] == "pass"
    assert body["fallback_message"] is None
    assert body["report"]["summary"] == "1 claim(s) can be stated with current evidence boundaries."
    assert body["report"]["claims"][0]["claim"] == "Enterprise demand grew"
    assert body["report"]["claims"][0]["source_ids"] == ["doc-demand"]
    assert body["report"]["claims"][0]["evidence_spans"] == ["Enterprise demand grew 12% in 2026."]
    assert body["report"]["claims"][0]["limitations"] == ["Supported by one retrieved source."]
    assert body["report"]["next_data_needed"]
    assert any("does not use an LLM" in warning for warning in body["warnings"])


def test_report_preview_uses_supported_ledger_claims_without_draft_claims():
    client = make_client()

    response = client.post(
        "/reports/preview",
        json={
            "question": "What evidence supports enterprise AI demand growth?",
            "evidence_entries": [
                {
                    "claim": "Enterprise AI demand grew in 2026.",
                    "source_id": "doc-demand-1",
                    "source_type": "html",
                    "source_date": "2026-05-01",
                    "evidence_span": "Survey data reported enterprise AI adoption demand growth.",
                    "confidence": "medium",
                    "limitation": "Survey source; needs independent confirmation.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["enterprise", "AI", "demand", "growth"],
                    "role": "direct_support",
                },
                {
                    "claim": "Enterprise AI demand grew in 2026.",
                    "source_id": "doc-demand-2",
                    "source_type": "csv",
                    "source_date": "2026-05-03",
                    "evidence_span": "Pipeline data showed an increase in enterprise AI inquiries.",
                    "confidence": "medium",
                    "limitation": "Pipeline metric may include duplicated inquiries.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["enterprise", "AI", "inquiries"],
                    "role": "direct_support",
                },
            ],
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "generated"
    assert body["gate"]["decision"] == "pass"
    assert body["report"]["summary"] == "1 claim(s) can be stated with current evidence boundaries."
    assert body["report"]["claims"][0]["claim"] == "Enterprise AI demand grew in 2026."
    assert body["report"]["claims"][0]["source_ids"] == ["doc-demand-1", "doc-demand-2"]


def test_report_preview_returns_fallback_when_noise_gate_blocks():
    client = make_client()

    response = client.post(
        "/reports/preview",
        json={
            "question": "Should I buy this stock after earnings?",
            "evidence_entries": [
                {
                    "claim": "Revenue grew after earnings",
                    "source_id": "doc-earnings",
                    "source_type": "markdown",
                    "source_date": "2026-05-28",
                    "evidence_span": "Revenue grew 12% after earnings.",
                    "confidence": "medium",
                    "limitation": "Supported by one retrieved source.",
                    "contradicting_source_ids": [],
                    "status": "supported",
                    "matched_terms": ["revenue", "earnings"],
                    "role": "direct_support",
                }
            ],
            "draft_claims": ["This proves you should buy the stock."],
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "blocked"
    assert body["report"] is None
    assert body["gate"]["decision"] == "blocked"
    assert body["fallback_message"].startswith("현재 근거만으로는 결론을 내릴 수 없습니다")
    assert any("buy/sell" in revision for revision in body["required_revisions"])


def test_report_preview_requires_revision_when_gate_needs_revision():
    client = make_client()

    response = client.post(
        "/reports/preview",
        json={
            "question": "Did enterprise demand grow?",
            "evidence_entries": [
                {
                    "claim": "Enterprise demand grew",
                    "source_id": "doc-support",
                    "source_type": "markdown",
                    "source_date": None,
                    "evidence_span": "Enterprise demand grew 12% this quarter.",
                    "confidence": "medium",
                    "limitation": "Supported by one retrieved source.",
                    "contradicting_source_ids": ["doc-contradiction"],
                    "status": "supported",
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "role": "direct_support",
                },
                {
                    "claim": "Enterprise demand grew",
                    "source_id": "doc-contradiction",
                    "source_type": "markdown",
                    "source_date": None,
                    "evidence_span": "Enterprise demand declined and no growth was observed.",
                    "confidence": "low",
                    "limitation": "Candidate contains contradiction language.",
                    "contradicting_source_ids": ["doc-support"],
                    "status": "contradicted",
                    "matched_terms": ["enterprise", "demand", "growth"],
                    "role": "contradiction",
                },
            ],
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "needs_revision"
    assert body["report"] is None
    assert body["gate"]["decision"] == "needs_revision"
    assert "Enterprise demand grew" in body["gate"]["downgraded_claims"]
    assert body["required_revisions"]
