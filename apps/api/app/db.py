from collections.abc import Sequence
from typing import Protocol
from uuid import UUID

import psycopg
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb

from app.schemas import (
    AgentRunCreate,
    DocumentCreate,
    EvidenceLedgerEntryOut,
    FailureCaseCreate,
    NoiseGatePreviewOut,
    OpsSummaryOut,
    ReportPreviewOut,
    RetrievalRunCreate,
    WorkflowRunCreate,
)
from app.settings import Settings, get_settings


class Repository(Protocol):
    def create_document(self, payload: DocumentCreate) -> dict: ...
    def list_documents(self) -> Sequence[dict]: ...
    def create_agent_run(self, payload: AgentRunCreate) -> dict: ...
    def update_agent_run(
        self,
        agent_run_id: UUID,
        *,
        status: str,
        error_message: str | None,
        latency_ms: int,
        trace_json: dict,
    ) -> dict: ...
    def list_agent_runs(self) -> Sequence[dict]: ...
    def create_workflow_run(self, payload: WorkflowRunCreate) -> dict: ...
    def list_workflow_runs(self) -> Sequence[dict]: ...
    def create_evidence_ledger_entries(
        self,
        question: str,
        entries: list[EvidenceLedgerEntryOut],
        workflow_trace_id: UUID,
        agent_run_id: UUID | None = None,
    ) -> Sequence[dict]: ...
    def list_evidence_ledger_entries(
        self,
        workflow_trace_id: UUID | None = None,
        status: str | None = None,
    ) -> Sequence[dict]: ...
    def create_noise_gate_record(
        self,
        result: NoiseGatePreviewOut,
        evidence_entry_count: int,
        draft_claim_count: int,
        workflow_trace_id: UUID,
        agent_run_id: UUID | None = None,
    ) -> dict: ...
    def list_noise_gate_records(
        self,
        workflow_trace_id: UUID | None = None,
        decision: str | None = None,
    ) -> Sequence[dict]: ...
    def create_report_record(
        self,
        result: ReportPreviewOut,
        evidence_entry_count: int,
        draft_claim_count: int,
        workflow_trace_id: UUID,
        agent_run_id: UUID | None = None,
    ) -> dict: ...
    def list_report_records(
        self,
        workflow_trace_id: UUID | None = None,
        status: str | None = None,
    ) -> Sequence[dict]: ...
    def lookup_trace_records(self, workflow_trace_id: UUID) -> dict[str, Sequence[dict]]: ...
    def create_failure_case(self, payload: FailureCaseCreate) -> dict: ...
    def list_failure_cases(self) -> Sequence[dict]: ...
    def create_retrieval_run(self, payload: RetrievalRunCreate) -> dict: ...
    def list_retrieval_runs(self) -> Sequence[dict]: ...
    def ops_summary(self) -> OpsSummaryOut: ...


class PostgresRepository:
    def __init__(self, settings: Settings):
        self._settings = settings

    def _connect(self):
        return psycopg.connect(self._settings.database_url, row_factory=dict_row)

    def create_document(self, payload: DocumentCreate) -> dict:
        with self._connect() as conn:
            row = conn.execute(
                """
                INSERT INTO documents (
                  source_type, source_uri, filename, title, source_date,
                  profile_json, extraction_quality, status
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING *
                """,
                (
                    payload.source_type,
                    payload.source_uri,
                    payload.filename,
                    payload.title,
                    payload.source_date,
                    Jsonb(payload.profile_json),
                    payload.extraction_quality,
                    payload.status,
                ),
            ).fetchone()
            conn.commit()
            return dict(row)

    def list_documents(self) -> Sequence[dict]:
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT * FROM documents ORDER BY created_at DESC, id DESC"
            ).fetchall()
            return [dict(row) for row in rows]

    def create_agent_run(self, payload: AgentRunCreate) -> dict:
        with self._connect() as conn:
            row = conn.execute(
                """
                INSERT INTO agent_runs (
                  user_question, workflow_version, status, error_message,
                  token_cost, latency_ms, trace_json
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING *
                """,
                (
                    payload.user_question,
                    payload.workflow_version,
                    payload.status,
                    payload.error_message,
                    payload.token_cost,
                    payload.latency_ms,
                    Jsonb(payload.trace_json),
                ),
            ).fetchone()
            conn.commit()
            return dict(row)

    def update_agent_run(
        self,
        agent_run_id: UUID,
        *,
        status: str,
        error_message: str | None,
        latency_ms: int,
        trace_json: dict,
    ) -> dict:
        with self._connect() as conn:
            row = conn.execute(
                """
                UPDATE agent_runs
                SET status = %s,
                    error_message = %s,
                    latency_ms = %s,
                    trace_json = %s,
                    ended_at = now()
                WHERE id = %s
                RETURNING *
                """,
                (
                    status,
                    error_message,
                    latency_ms,
                    Jsonb(trace_json),
                    agent_run_id,
                ),
            ).fetchone()
            conn.commit()
            return dict(row)

    def list_agent_runs(self) -> Sequence[dict]:
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT * FROM agent_runs ORDER BY started_at DESC, id DESC"
            ).fetchall()
            return [dict(row) for row in rows]

    def create_workflow_run(self, payload: WorkflowRunCreate) -> dict:
        with self._connect() as conn:
            row = conn.execute(
                """
                INSERT INTO workflow_runs (
                  question, workflow_version, status, trace_json,
                  started_at, ended_at, latency_ms, error_message
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING *
                """,
                (
                    payload.question,
                    payload.workflow_version,
                    payload.status,
                    Jsonb(payload.trace_json),
                    payload.started_at,
                    payload.ended_at,
                    payload.latency_ms,
                    payload.error_message,
                ),
            ).fetchone()
            conn.commit()
            return dict(row)

    def list_workflow_runs(self) -> Sequence[dict]:
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT * FROM workflow_runs ORDER BY created_at DESC, id DESC"
            ).fetchall()
            return [dict(row) for row in rows]

    def create_evidence_ledger_entries(
        self,
        question: str,
        entries: list[EvidenceLedgerEntryOut],
        workflow_trace_id: UUID,
        agent_run_id: UUID | None = None,
    ) -> Sequence[dict]:
        with self._connect() as conn:
            rows = []
            for entry in entries:
                row = conn.execute(
                    """
                    INSERT INTO evidence_ledger_entries (
                      run_id, agent_run_id, workflow_trace_id,
                      question, claim, source_id, source_type, source_date,
                      evidence_span, confidence, limitation,
                      contradicting_source_ids, status, matched_terms, role
                    )
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    RETURNING *
                    """,
                    (
                        agent_run_id,
                        agent_run_id,
                        workflow_trace_id,
                        question,
                        entry.claim,
                        entry.source_id,
                        entry.source_type,
                        entry.source_date,
                        entry.evidence_span,
                        entry.confidence,
                        entry.limitation,
                        Jsonb(entry.contradicting_source_ids),
                        entry.status,
                        Jsonb(entry.matched_terms),
                        entry.role,
                    ),
                ).fetchone()
                rows.append(dict(row))
            conn.commit()
            return rows

    def list_evidence_ledger_entries(
        self,
        workflow_trace_id: UUID | None = None,
        status: str | None = None,
    ) -> Sequence[dict]:
        filters, params = _record_filters(
            workflow_trace_id=workflow_trace_id,
            status=status,
        )
        with self._connect() as conn:
            rows = conn.execute(
                f"""
                SELECT * FROM evidence_ledger_entries
                {filters}
                ORDER BY created_at DESC, id DESC
                """,
                params,
            ).fetchall()
            return [dict(row) for row in rows]

    def create_noise_gate_record(
        self,
        result: NoiseGatePreviewOut,
        evidence_entry_count: int,
        draft_claim_count: int,
        workflow_trace_id: UUID,
        agent_run_id: UUID | None = None,
    ) -> dict:
        with self._connect() as conn:
            row = conn.execute(
                """
                INSERT INTO noise_gate_records (
                  workflow_trace_id, agent_run_id, question, decision, final_response_allowed, checks,
                  blocked_claims, downgraded_claims, allowed_claims,
                  required_revisions, fallback_message, warnings,
                  evidence_entry_count, draft_claim_count
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING *
                """,
                (
                    workflow_trace_id,
                    agent_run_id,
                    result.question,
                    result.decision,
                    result.final_response_allowed,
                    Jsonb([check.model_dump() for check in result.checks]),
                    Jsonb(result.blocked_claims),
                    Jsonb(result.downgraded_claims),
                    Jsonb(result.allowed_claims),
                    Jsonb(result.required_revisions),
                    result.fallback_message,
                    Jsonb(result.warnings),
                    evidence_entry_count,
                    draft_claim_count,
                ),
            ).fetchone()
            conn.commit()
            return dict(row)

    def list_noise_gate_records(
        self,
        workflow_trace_id: UUID | None = None,
        decision: str | None = None,
    ) -> Sequence[dict]:
        filters, params = _record_filters(
            workflow_trace_id=workflow_trace_id,
            decision=decision,
        )
        with self._connect() as conn:
            rows = conn.execute(
                f"""
                SELECT * FROM noise_gate_records
                {filters}
                ORDER BY created_at DESC, id DESC
                """,
                params,
            ).fetchall()
            return [dict(row) for row in rows]

    def create_report_record(
        self,
        result: ReportPreviewOut,
        evidence_entry_count: int,
        draft_claim_count: int,
        workflow_trace_id: UUID,
        agent_run_id: UUID | None = None,
    ) -> dict:
        with self._connect() as conn:
            row = conn.execute(
                """
                INSERT INTO report_records (
                  workflow_trace_id, agent_run_id, question, status, report, gate, gate_decision,
                  fallback_message, required_revisions, warnings,
                  claim_count, evidence_entry_count, draft_claim_count
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING *
                """,
                (
                    workflow_trace_id,
                    agent_run_id,
                    result.question,
                    result.status,
                    Jsonb(result.report.model_dump() if result.report is not None else None),
                    Jsonb(result.gate.model_dump()),
                    result.gate.decision,
                    result.fallback_message,
                    Jsonb(result.required_revisions),
                    Jsonb(result.warnings),
                    len(result.report.claims) if result.report is not None else 0,
                    evidence_entry_count,
                    draft_claim_count,
                ),
            ).fetchone()
            conn.commit()
            return dict(row)

    def list_report_records(
        self,
        workflow_trace_id: UUID | None = None,
        status: str | None = None,
    ) -> Sequence[dict]:
        filters, params = _record_filters(
            workflow_trace_id=workflow_trace_id,
            status=status,
        )
        with self._connect() as conn:
            rows = conn.execute(
                f"""
                SELECT * FROM report_records
                {filters}
                ORDER BY created_at DESC, id DESC
                """,
                params,
            ).fetchall()
            return [dict(row) for row in rows]

    def lookup_trace_records(self, workflow_trace_id: UUID) -> dict[str, Sequence[dict]]:
        with self._connect() as conn:
            agent_runs = conn.execute(
                """
                SELECT * FROM agent_runs
                WHERE trace_json->>'workflow_trace_id' = %s
                ORDER BY started_at DESC, id DESC
                """,
                (str(workflow_trace_id),),
            ).fetchall()
            evidence_entries = conn.execute(
                """
                SELECT * FROM evidence_ledger_entries
                WHERE workflow_trace_id = %s
                ORDER BY created_at DESC, id DESC
                """,
                (workflow_trace_id,),
            ).fetchall()
            noise_gate_records = conn.execute(
                """
                SELECT * FROM noise_gate_records
                WHERE workflow_trace_id = %s
                ORDER BY created_at DESC, id DESC
                """,
                (workflow_trace_id,),
            ).fetchall()
            report_records = conn.execute(
                """
                SELECT * FROM report_records
                WHERE workflow_trace_id = %s
                ORDER BY created_at DESC, id DESC
                """,
                (workflow_trace_id,),
            ).fetchall()
        return {
            "agent_runs": [dict(row) for row in agent_runs],
            "evidence_ledger_entries": [dict(row) for row in evidence_entries],
            "noise_gate_records": [dict(row) for row in noise_gate_records],
            "report_records": [dict(row) for row in report_records],
        }

    def create_failure_case(self, payload: FailureCaseCreate) -> dict:
        with self._connect() as conn:
            row = conn.execute(
                """
                INSERT INTO failure_cases (
                  agent_run_id, failure_type, description, root_cause,
                  fix_status, next_action
                )
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING *
                """,
                (
                    payload.agent_run_id,
                    payload.failure_type,
                    payload.description,
                    payload.root_cause,
                    payload.fix_status,
                    payload.next_action,
                ),
            ).fetchone()
            conn.commit()
            return dict(row)

    def list_failure_cases(self) -> Sequence[dict]:
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT * FROM failure_cases ORDER BY created_at DESC, id DESC"
            ).fetchall()
            return [dict(row) for row in rows]

    def create_retrieval_run(self, payload: RetrievalRunCreate) -> dict:
        with self._connect() as conn:
            row = conn.execute(
                """
                INSERT INTO retrieval_runs (
                  question, strategy, status, latency_ms, result_count,
                  hit_rate, citation_coverage, missing_evidence_count, metadata_json
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING *
                """,
                (
                    payload.question,
                    payload.strategy,
                    payload.status,
                    payload.latency_ms,
                    payload.result_count,
                    payload.hit_rate,
                    payload.citation_coverage,
                    payload.missing_evidence_count,
                    Jsonb(payload.metadata_json),
                ),
            ).fetchone()
            conn.commit()
            return dict(row)

    def list_retrieval_runs(self) -> Sequence[dict]:
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT * FROM retrieval_runs ORDER BY created_at DESC, id DESC"
            ).fetchall()
            return [dict(row) for row in rows]

    def ops_summary(self) -> OpsSummaryOut:
        with self._connect() as conn:
            row = conn.execute(
                """
                SELECT
                  (SELECT count(*) FROM documents) AS document_count,
                  (SELECT count(*) FROM agent_runs) AS agent_run_count,
                  (SELECT count(*) FROM failure_cases) AS failure_case_count,
                  (SELECT count(*) FROM retrieval_runs) AS retrieval_run_count,
                  (SELECT count(*) FROM noise_gate_records) AS noise_gate_record_count,
                  (SELECT count(*) FROM report_records) AS report_record_count,
                  (
                    SELECT count(*)
                    FROM noise_gate_records
                    WHERE decision = 'blocked'
                  ) AS blocked_gate_count,
                  (
                    SELECT count(*)
                    FROM noise_gate_records
                    WHERE decision = 'needs_revision'
                  ) AS revision_gate_count,
                  (
                    SELECT count(*)
                    FROM report_records
                    WHERE status = 'generated'
                  ) AS generated_report_count,
                  (
                    SELECT count(*)
                    FROM report_records
                    WHERE status = 'blocked'
                  ) AS blocked_report_count,
                  (
                    SELECT count(*)
                    FROM report_records
                    WHERE status = 'needs_revision'
                  ) AS revision_report_count,
                  (
                    SELECT count(*)
                    FROM evidence_ledger_entries
                    WHERE status IN ('unsupported', 'blocked')
                  ) AS unsupported_claim_count,
                  (
                    SELECT count(*)
                    FROM evidence_ledger_entries
                    WHERE status = 'contradicted'
                       OR jsonb_array_length(contradicting_source_ids) > 0
                  ) AS contradiction_count,
                  (SELECT avg(latency_ms) FROM agent_runs WHERE latency_ms IS NOT NULL)
                    AS average_latency_ms
                """
            ).fetchone()

        return OpsSummaryOut(
            status="placeholder",
            workflow_version=self._settings.workflow_version,
            document_count=row["document_count"],
            agent_run_count=row["agent_run_count"],
            failure_case_count=row["failure_case_count"],
            noise_gate_record_count=row["noise_gate_record_count"],
            blocked_gate_count=row["blocked_gate_count"],
            revision_gate_count=row["revision_gate_count"],
            report_record_count=row["report_record_count"],
            generated_report_count=row["generated_report_count"],
            blocked_report_count=row["blocked_report_count"],
            revision_report_count=row["revision_report_count"],
            unsupported_claim_count=row["unsupported_claim_count"],
            contradiction_count=row["contradiction_count"],
            average_latency_ms=row["average_latency_ms"],
            notes=[
                f"Retrieval runs recorded: {row['retrieval_run_count']}. Evidence Ledger persisted entries now drive unsupported and contradiction counts.",
                "Embeddings, semantic retrieval, distributed tracing, and final report generation beyond deterministic previews are still not implemented.",
            ],
        )


def get_repository() -> Repository:
    return PostgresRepository(get_settings())


def _record_filters(**criteria: object) -> tuple[str, list[object]]:
    clauses = []
    params = []
    for column, value in criteria.items():
        if value is None:
            continue
        clauses.append(f"{column} = %s")
        params.append(value)
    if not clauses:
        return "", []
    return "WHERE " + " AND ".join(clauses), params
