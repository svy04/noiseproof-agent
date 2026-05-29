ALTER TABLE evidence_ledger_entries
  ADD COLUMN IF NOT EXISTS workflow_trace_id UUID NOT NULL DEFAULT gen_random_uuid();

ALTER TABLE noise_gate_records
  ADD COLUMN IF NOT EXISTS workflow_trace_id UUID NOT NULL DEFAULT gen_random_uuid();

ALTER TABLE report_records
  ADD COLUMN IF NOT EXISTS workflow_trace_id UUID NOT NULL DEFAULT gen_random_uuid();
