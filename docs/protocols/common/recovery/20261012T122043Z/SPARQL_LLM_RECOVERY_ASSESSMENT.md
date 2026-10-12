# SPARQL-LLM recovery assessment

**phase1:** smoke_only · MIT · offline smoke PASS · needs_api true historically for full chat.

## Findings (static)

- Repo supports Ollama / init_chat_model / llama.cpp references (local scan hits).
- Embedding cache lab-complete (`intfloat/multilingual-e5-large`).
- Graph runtime still G4 NOT_SATISFIED (common).

## Variants

| Variant | Status |
|---|---|
| SPARQL_LLM_NATIVE_API_VARIANT | ZERO_COST method-faithful **NOT_ELIGIBLE** (paid/commercial API path) |
| SPARQL_LLM_ZERO_COST_LOCAL_BACKEND_VARIANT | **CANDIDATE** controlled variant (local backend; architecture RAG/retrieval/validation preserved if only backend swapped) |

## Recoverability

- native_faithful ZERO_COST: R3/R8 mixture → native paid API path not ZERO_COST; classify **ZERO_COST_METHOD_FAITHFUL_NOT_FEASIBLE** for original API backend
- common_benchmark: **R3** via controlled local backend after graph+adapters
- Blockers: B_COST, B_SERVICE, B_GRAPH(runtime), B_POLICY
