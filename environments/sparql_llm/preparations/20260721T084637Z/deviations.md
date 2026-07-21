# Desviaciones — Prompt 10

## Respecto a defaults upstream Settings

- `default_max_try_fix_sparql=0` (upstream default 3) — seguridad para futuro smoke: máximo propuesto 2 LLM calls.
- `default_max_tokens=512` (upstream 16384) — **no enforceado** en rama OpenRouter (`CODE_VERIFIED`).
- `default_number_of_retrieved_docs=3` (upstream 10).
- `auto_init=false` (upstream True).
- Un solo endpoint UniProt + void local; sin homepage_url.
- `docs_collection_name=lab_minimal_uniprot_void` (no `expasy`).

## Respecto a índice nativo / paper

- Documentos ShEx lab sin labels remotos (`labels_queried=false`).
- Máximo 12 clases (subset del VoID).
- Etiqueta `LAB_MINIMAL_INDEX` ≠ índice del artículo ni biodata benchmark.
- `init_vectordb` completo **no** ejecutado.

## No realizados (gate)

- Descarga `intfloat/multilingual-e5-large`.
- `build-index` / `verify-index`.
- Import `agent.main` / preflight FastAPI.
- POST `/chat` / OpenRouter.
