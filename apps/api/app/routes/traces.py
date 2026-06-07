from uuid import UUID

from fastapi import APIRouter, Depends, Request

from app.db import Repository, get_repository
from app.schemas import (
    AgentRunOut,
    EvidenceLedgerStoredEntryOut,
    NoiseGateStoredRecordOut,
    ReportStoredRecordOut,
    TraceLookupOut,
    TraceLookupSummaryOut,
)

router = APIRouter(prefix="/traces", tags=["traces"])


@router.get("/otel-spans/local")
def list_local_otel_spans(request: Request) -> dict:
    recorder = request.app.state.otel_span_recorder
    return recorder.snapshot()


@router.get("/{workflow_trace_id}", response_model=TraceLookupOut)
def lookup_trace_records(
    workflow_trace_id: UUID,
    repository: Repository = Depends(get_repository),
) -> TraceLookupOut:
    records = repository.lookup_trace_records(workflow_trace_id)
    agent_runs = [AgentRunOut(**row) for row in records["agent_runs"]]
    evidence_entries = [
        EvidenceLedgerStoredEntryOut(**row)
        for row in records["evidence_ledger_entries"]
    ]
    noise_gate_records = [
        NoiseGateStoredRecordOut(**row) for row in records["noise_gate_records"]
    ]
    report_records = [
        ReportStoredRecordOut(**row) for row in records["report_records"]
    ]
    return TraceLookupOut(
        workflow_trace_id=workflow_trace_id,
        agent_runs=agent_runs,
        evidence_ledger_entries=evidence_entries,
        noise_gate_records=noise_gate_records,
        report_records=report_records,
        summary=TraceLookupSummaryOut(
            agent_run_count=len(agent_runs),
            evidence_ledger_entry_count=len(evidence_entries),
            noise_gate_record_count=len(noise_gate_records),
            report_record_count=len(report_records),
        ),
    )
