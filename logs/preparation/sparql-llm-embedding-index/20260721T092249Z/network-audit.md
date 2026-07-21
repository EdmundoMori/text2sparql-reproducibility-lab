# Network audit — Prompt 10B

## Allowed
- Download of FastEmbed-resolved artifact for exact id `intfloat/multilingual-e5-large`
  - HF source declared: `qdrant/multilingual-e5-large-onnx` (unreachable offline mode in image; fallback used)
  - URL used: `https://storage.googleapis.com/qdrant-fastembed/fast-multilingual-e5-large.tar.gz`

## Zero
- OpenRouter / OpenAI / LLM inference calls
- POST `/chat`
- MCP tool invocation
- SPARQL endpoint queries (prefix fetch attempted at import under network block → failed closed)
- Alternative embedding models
- init_vectordb full SIB indexing
