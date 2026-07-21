# Autorización de descarga — Prompt 10B

**Aprobador:** EDMUNDO MORI ORRILLO  
**Fecha:** 2026-07-21  
**Modelo autorizado:** `intfloat/multilingual-e5-large` (exacto)  
**FastEmbed esperado:** 0.8.0 (imagen agent)

## Alcance autorizado

- Descargar únicamente el artefacto que FastEmbed 0.8.0 resuelva para ese identificador exacto.
- Almacenar caché en directorio aislado gitignored (`workdir/.../embedding_cache`).
- Registrar origen, revisión/archivos, tamaños y checksums.
- Construir `LAB_MINIMAL_INDEX` con los 12 documentos de Prompt 10.
- Preflight FastAPI sin POST `/chat`.

## No autorizado

- Embeddings alternativos; OpenRouter/OpenAI/LLM; MCP; SPARQL; benchmarks;
  modificar upstream; versionar caché o índice en Git.

## Abort conditions

- Procedencia indeterminable; descarga de otro modelo; espacio insuficiente.
