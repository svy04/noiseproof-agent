from collections.abc import Sequence
from typing import Protocol

import psycopg
from psycopg.rows import dict_row
from psycopg.types.json import Jsonb

from app.schemas import (
    AgentRunCreate,
    DocumentCreate,
    FailureCaseCreate,
    OpsSummaryOut,
    RetrievalRunCreate,
)
from app.settings import Settings, get_settings


class Repository(Protocol):
    def create_document(self, payload: DocumentCreate) -> dict: ...
    def list_documents(self) -> Sequence[dict]: ...
    def create_agent_run(self, payload: AgentRunCreate) -> dict: ...
    def list_agent_runs(self) -> Sequence[dict]: ...
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

    def list_agent_runs(self) -> Sequence[dict]:
        with self._connect() as conn:
            rows = conn.execute(
                "SELECT * FROM agent_runs ORDER BY started_at DESC, id DESC"
            ).fetchall()
            return [dict(row) for row in rows]

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
            unsupported_claim_count=0,
            contradiction_count=0,
            average_latency_ms=row["average_latency_ms"],
            notes=[
                f"Retrieval runs recorded: {row['retrieval_run_count']}. Phase 7 adds Noise Gate Preview only; no final report or dashboard implementation yet.",
                "Unsupported claim and contradiction counts remain placeholders until persisted Evidence Ledger entries exist.",
            ],
        )


def get_repository() -> Repository:
    return PostgresRepository(get_settings())
