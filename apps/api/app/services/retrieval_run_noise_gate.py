from uuid import UUID, uuid4

from fastapi import HTTPException

from app.db import Repository
from app.schemas import (
    EvidenceLedgerEntryOut,
    NoiseGatePreviewRequest,
    NoiseGateStoredRecordOut,
)
from app.services.noise_gate import preview_noise_gate
from app.services.run_trace import run_with_trace


def persist_noise_gate_from_retrieval_run(
    retrieval_run_id: UUID,
    repository: Repository,
) -> NoiseGateStoredRecordOut:
    retrieval_run = repository.get_retrieval_run(retrieval_run_id)
    if retrieval_run is None:
        raise HTTPException(status_code=404, detail="Retrieval run not found")

    workflow_trace_id = uuid4()

    def operation(agent_run_id: UUID) -> NoiseGateStoredRecordOut:
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

        evidence_entries = [
            EvidenceLedgerEntryOut(**entry)
            for entry in ledger_entries
        ]
        preview = preview_noise_gate(
            NoiseGatePreviewRequest(
                question=retrieval_run["question"],
                evidence_entries=evidence_entries,
                draft_claims=[],
            )
        )
        preview = preview.model_copy(
            update={
                "warnings": [
                    *preview.warnings,
                    (
                        "Noise Gate record was generated from retrieval_run-linked "
                        "Evidence Ledger rows."
                    ),
                    (
                        "This handoff does not call an LLM, create embeddings, perform "
                        "semantic retrieval, generate a report, or provide financial advice."
                    ),
                ]
            }
        )
        persisted = repository.create_noise_gate_record(
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
                "source_endpoint": (
                    "POST /retrieval-runs/{retrieval_run_id}/evidence-ledger"
                ),
                "persistence_boundary": (
                    "retrieval_run_linked_noise_gate_no_llm_no_embeddings"
                ),
            },
        )
        return NoiseGateStoredRecordOut(**persisted)

    return run_with_trace(
        repository,
        endpoint="POST /retrieval-runs/{retrieval_run_id}/noise-gate",
        user_question=retrieval_run["question"],
        trace_json={
            "retrieval_run_id": str(retrieval_run_id),
            "workflow_trace_id": str(workflow_trace_id),
            "source_table": "evidence_ledger_entries",
            "no_llm": True,
            "no_embeddings": True,
            "no_semantic_retrieval": True,
            "no_report_generation": True,
        },
        operation=operation,
        trace_from_result=lambda result: {
            "decision": result.decision,
            "final_response_allowed": result.final_response_allowed,
            "evidence_entry_count": result.evidence_entry_count,
            "draft_claim_count": result.draft_claim_count,
        },
    )
