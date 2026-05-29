from datetime import date, datetime, timezone
from uuid import uuid4

from fastapi.testclient import TestClient

from app.db import get_repository
from app.main import create_app
from app.schemas import AgentRunCreate, DocumentCreate, FailureCaseCreate, OpsSummaryOut


class InMemoryRepository:
    def __init__(self):
        self.documents = []
        self.agent_runs = []
        self.failure_cases = []
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
            workflow_version="phase5.5-collection-plan-preview",
            document_count=len(self.documents),
            agent_run_count=len(self.agent_runs),
            failure_case_count=len(self.failure_cases),
            unsupported_claim_count=0,
            contradiction_count=0,
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
        "workflow_version": "phase5.5-collection-plan-preview",
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
        == "phase5.5-collection-plan-preview"
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
