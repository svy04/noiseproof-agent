ALTER TABLE evidence_ledger_entries
  ADD COLUMN IF NOT EXISTS retrieval_run_id UUID REFERENCES retrieval_runs(id) ON DELETE SET NULL;
