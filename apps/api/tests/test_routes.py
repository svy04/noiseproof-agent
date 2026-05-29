from datetime import date, datetime, timezone
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

from app.db import get_repository
from app.main import create_app
from app.schemas import AgentRunCreate, DocumentCreate, FailureCaseCreate, OpsSummaryOut
from app.services.run_trace import run_with_trace


class InMemoryRepository:
    def __init__(self):
        self.documents = []
        self.agent_runs = []
        self.evidence_ledger_entries = []
        self.failure_cases = []
        self.noise_gate_records = []
        self.report_records = []
        self.retrieval_runs = []

    def create_document(self, payload: DocumentCreate) -> dict:
        row = payload.model_dump()
        row["id"] = uuid4()
        row["created_at"] = datetime.now(timezone.utc)
        self.documents.append(row)
        return row

    def list_documents(self):
        return self.documents

    def create_agent_run(self, payload: AgentRunCreate) -> dict:
        row = payload.model_dump()
        row["id"] = uuid4()
        row["started_at"] = datetime.now(timezone.utc)
        row["ended_at"] = None
        self.agent_runs.append(row)
        return row

    def list_agent_runs(self):
        return self.agent_runs

    def create_evidence_ledger_entries(self, question, entries, workflow_trace_id=None):
        workflow_trace_id = workflow_trace_id or uuid4()
        created = []
        for entry in entries:
            row = entry.model_dump()
            row["id"] = uuid4()
            row["question"] = question
            row["run_id"] = None
            row["workflow_trace_id"] = workflow_trace_id
            row["created_at"] = datetime.now(timezone.utc)
            self.evidence_ledger_entries.append(row)
            created.append(row)
        return created

    def list_evidence_ledger_entries(self):
        return self.evidence_ledger_entries

    def create_noise_gate_record(
        self, result, evidence_entry_count, draft_claim_count, workflow_trace_id=None
    ):
        row = result.model_dump()
        row["id"] = uuid4()
        row["workflow_trace_id"] = workflow_trace_id or uuid4()
        row["evidence_entry_count"] = evidence_entry_count
        row["draft_claim_count"] = draft_claim_count
        row["created_at"] = datetime.now(timezone.utc)
        self.noise_gate_records.append(row)
        return row

    def list_noise_gate_records(self):
        return self.noise_gate_records

    def create_report_record(
        self, result, evidence_entry_count, draft_claim_count, workflow_trace_id=None
    ):
        row = result.model_dump()
        row["id"] = uuid4()
        row["workflow_trace_id"] = workflow_trace_id or uuid4()
        row["gate_decision"] = result.gate.decision
        row["claim_count"] = len(result.report.claims) if result.report is not None else 0
        row["evidence_entry_count"] = evidence_entry_count
        row["draft_claim_count"] = draft_claim_count
        row["created_at"] = datetime.now(timezone.utc)
        self.report_records.append(row)
        return row

    def list_report_records(self):
        return self.report_records

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

    def ops_summary(self) -> OpsSummaryOut:
        return OpsSummaryOut(
            status="placeholder",
            workflow_version="phase15-record-linkage",
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


def make_client():
    app = create_app()
    repository = InMemoryRepository()
    app.dependency_overrides[get_repository] = lambda: repository
    return TestClient(app)


def test_health_endpoint():
    client = make_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "noiseproof-agent-api",
            "workflow_version": "phase15-record-linkage",
    }


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
        == "phase15-record-linkage"
    )
    assert client.get("/failure-cases").json()[0]["fix_status"] == "open"


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
    assert "Phase 15" in response.text


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
    assert all(trace["workflow_version"] == "phase15-record-linkage" for trace in traces)
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
        and trace["trace_json"].get("phase") == "phase15-record-linkage"
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
        and trace["trace_json"].get("phase") == "phase15-record-linkage"
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

    def failing_operation():
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
    assert trace["error_message"] == "synthetic preview failure"
    assert trace["trace_json"]["endpoint"] == "POST /reports/preview"
    assert trace["trace_json"]["error_type"] == "ValueError"


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
