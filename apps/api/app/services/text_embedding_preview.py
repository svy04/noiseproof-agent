from __future__ import annotations

import hashlib
import math
import re

from fastapi import HTTPException

from app.schemas import TextEmbeddingPreviewOut, TextEmbeddingPreviewRequest

LOCAL_HASH_EMBEDDING_MODEL = "local-hash-embedding-preview-v0"
_TOKEN_RE = re.compile(r"[a-z0-9]+")


def preview_text_embedding(
    payload: TextEmbeddingPreviewRequest,
) -> TextEmbeddingPreviewOut:
    if payload.embedding_model != LOCAL_HASH_EMBEDDING_MODEL:
        raise HTTPException(
            status_code=400,
            detail=(
                "Only local-hash-embedding-preview-v0 is supported for deterministic "
                "preview generation."
            ),
        )
    if payload.distance_metric != "cosine":
        raise HTTPException(
            status_code=400,
            detail="Only cosine distance is supported for local hash preview embeddings.",
        )

    tokens = _TOKEN_RE.findall(payload.text.lower())
    if not tokens:
        raise HTTPException(
            status_code=400,
            detail="text must contain at least one token for embedding preview.",
        )

    vector = [0.0 for _ in range(payload.embedding_dimension)]
    for token in tokens:
        digest = hashlib.sha256(token.encode("utf-8")).digest()
        index = int.from_bytes(digest[:8], "big") % payload.embedding_dimension
        sign = 1.0 if digest[8] % 2 == 0 else -1.0
        vector[index] += sign

    norm = math.sqrt(sum(value * value for value in vector))
    if norm:
        vector = [round(value / norm, 6) for value in vector]

    text_hash = "sha256:" + hashlib.sha256(payload.text.encode("utf-8")).hexdigest()
    return TextEmbeddingPreviewOut(
        embedding_model=LOCAL_HASH_EMBEDDING_MODEL,
        embedding_dimension=payload.embedding_dimension,
        embedding_text_hash=text_hash,
        distance_metric="cosine",
        embedding_status="preview_generated",
        embedding=vector,
        metadata_json={
            "embedding_source": "deterministic_local_hash_embedding_preview",
            "generation_boundary": "local_hash_preview_not_semantic_model",
            "persistence_boundary": "preview_only_not_persisted",
            "quality_boundary": "not_semantic_quality_evidence",
            "tokenization_boundary": "regex_lowercase_alnum_tokens",
            "token_count": len(tokens),
            "external_model_used": False,
            "llm_used": False,
        },
        warnings=[
            "This is a deterministic local hash preview, not a semantic embedding model.",
            "No external model, no LLM, no semantic quality claim, and no vector search quality claim.",
            "The preview vector is not persisted and does not modify chunk_embeddings.",
        ],
    )
