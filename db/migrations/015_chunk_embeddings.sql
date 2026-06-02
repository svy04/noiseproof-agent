CREATE TABLE IF NOT EXISTS chunk_embeddings (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  chunk_id UUID NOT NULL REFERENCES document_chunks(id) ON DELETE CASCADE,
  embedding_model TEXT NOT NULL,
  embedding_dimension INTEGER NOT NULL CHECK (embedding_dimension > 0),
  embedding_text_hash TEXT NOT NULL,
  embedding_created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  distance_metric TEXT NOT NULL DEFAULT 'cosine' CHECK (
    distance_metric IN ('cosine', 'l2', 'inner_product')
  ),
  embedding_status TEXT NOT NULL DEFAULT 'planned' CHECK (
    embedding_status IN ('planned', 'created', 'stale', 'failed')
  ),
  embedding vector,
  metadata_json JSONB NOT NULL DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE (chunk_id, embedding_model, embedding_text_hash, distance_metric)
);

CREATE INDEX IF NOT EXISTS idx_chunk_embeddings_chunk_id
  ON chunk_embeddings(chunk_id);

CREATE INDEX IF NOT EXISTS idx_chunk_embeddings_model
  ON chunk_embeddings(embedding_model);

CREATE INDEX IF NOT EXISTS idx_chunk_embeddings_status
  ON chunk_embeddings(embedding_status);
