from uuid import UUID, uuid4

from fastapi import HTTPException

from app.db import Repository
from app.schemas import (
    EvidenceLedgerEntryOut,
    ReportPreviewRequest,
    ReportStoredRecordOut,
)
from app.services.report_preview import preview_report
from app.services.retrieval_run_source_provenance import (
    source_provenance_from_ledger_entries,
    source_provenance_warnings,
)
from app.services.run_trace import run_with_trace


def persist_report_from_retrieval_run(
    retrieval_run_id: UUID,
    repository: Repository,
) -> ReportStoredRecordOut:
    retrieval_run = repository.get_retrieval_run(retrieval_run_id)
    if retrieval_run is None:
        raise HTTPException(status_code=404, detail="Retrieval run not found")

    workflow_trace_id = uuid4()

    def operation(agent_run_id: UUID) -> ReportStoredRecordOut:
        ledger_entries = list(
            repository.list_evidence_ledger_entries(retrieval_run_id=retrieval_run_id)
        )
        if not ledger_entries:
            raise HTTPException(
                status_code=409,
                detail=(
                    "No Evidence Ledger entries are linked to this retrieval run. "
                    "Run POST /retrieval-runs/{retrieval_run_id}/evidence-ledger first."
                ),
            )

        gate = _latest_gate_for_retrieval_run(retrieval_run_id, repository)
        if gate is None:
            raise HTTPException(
                status_code=409,
                detail=(
                    "No Noise Gate record is linked to this retrieval run. "
                    "Run POST /retrieval-runs/{retrieval_run_id}/noise-gate first."
                ),
            )

        evidence_entries = [
            EvidenceLedgerEntryOut(**entry)
            for entry in ledger_entries
        ]
        source_provenance = source_provenance_from_ledger_entries(ledger_entries)
        preview = preview_report(
            ReportPreviewRequest(
                question=retrieval_run["question"],
                evidence_entries=evidence_entries,
                draft_claims=[],
            )
        )
        preview = preview.model_copy(
            update={
                "warnings": [
                    *preview.warnings,
                    *source_provenance_warnings(source_provenance),
                    (
                        "Report record was generated from retrieval_run-linked "
                        "Noise Gate and Evidence Ledger rows."
                    ),
                    (
                        "This handoff does not call an LLM, create embeddings, perform "
                        "semantic retrieval, create failure cases, or provide financial advice."
                    ),
                ]
            }
        )
        persisted = repository.create_report_record(
            preview,
            evidence_entry_count=len(evidence_entries),
            draft_claim_count=0,
            workflow_trace_id=workflow_trace_id,
            agent_run_id=agent_run_id,
            workflow_run_id=retrieval_run.get("workflow_run_id"),
            stage_input_manifest={
                "retrieval_run_id": str(retrieval_run_id),
                "input_evidence_ledger_entry_ids": [
                    str(entry["id"]) for entry in ledger_entries
                ],
                "input_noise_gate_record_id": str(gate["id"]),
                "source_endpoint": (
                    "POST /retrieval-runs/{retrieval_run_id}/noise-gate"
                ),
                "persistence_boundary": (
                    "retrieval_run_linked_report_no_llm_no_embeddings"
                ),
                **source_provenance,
            },
        )
        return ReportStoredRecordOut(**persisted)

    return run_with_trace(
        repository,
        endpoint="POST /retrieval-runs/{retrieval_run_id}/report",
        user_question=retrieval_run["question"],
        trace_json={
            "retrieval_run_id": str(retrieval_run_id),
            "workflow_trace_id": str(workflow_trace_id),
            "source_table": "noise_gate_records",
            "no_llm": True,
            "no_embeddings": True,
            "no_semantic_retrieval": True,
            "no_failure_case_creation": True,
            "source_retrieval_mode": None,
            "source_query_vector_source": None,
            "source_is_semantic_retrieval_run": None,
            "source_retrieval_persistence_boundary": None,
            "handoff_performs_semantic_retrieval": False,
        },
        operation=operation,
        trace_from_result=lambda result: {
            "report_status": result.status,
            "gate_decision": result.gate_decision,
            "claim_count": result.claim_count,
            "evidence_entry_count": result.evidence_entry_count,
            "draft_claim_count": result.draft_claim_count,
            **(result.stage_input_manifest or {}),
        },
    )


def _latest_gate_for_retrieval_run(
    retrieval_run_id: UUID,
    repository: Repository,
) -> dict | None:
    matches = [
        row
        for row in repository.list_noise_gate_records()
        if str((row.get("stage_input_manifest") or {}).get("retrieval_run_id"))
        == str(retrieval_run_id)
    ]
    if not matches:
        return None
    return max(matches, key=lambda row: row["created_at"])
