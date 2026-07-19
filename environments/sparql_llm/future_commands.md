# Comandos futuros — sparql_llm (NO ejecutar en Prompt 4B)

## CORE_OFFLINE — candidato primer micro-smoke

```bash
# Futuro Prompt 5A (ejemplo documental)
cd /home/edmundo/text2sparql-reproducibility-lab
python3 -m venv environments/sparql_llm/.venv
source environments/sparql_llm/.venv/bin/activate
python -m pip install -U pip
# Instalar desde árbol o PyPI pin documental — elegir en el prompt de install:
#   pip install -e "upstream/sparql_llm"   # editable desde pin local
# o pip install "sparql-llm==?"            # solo si se fija versión publicada verificada
python -c "from sparql_llm import SparqlVoidShapesLoader, validate_sparql_with_void; print('ok')"
# Opcional: pytest tests/test_components.py con filtros offline — solo si no requieren red
```

**Éxito smoke:** import OK + (opcional) validate con `tests/void_uniprot.ttl`.  
**Etiqueta:** `smoke_only` tras documentar comandos/resultados. **No** `reproduced`.

## MCP_OR_AGENT_API (posterior)

```bash
# Tras CORE_OFFLINE estable
pip install -e "upstream/sparql_llm[agent]"   # sintaxis exacta a verificar en install prompt
export OPENROUTER_API_KEY=...                 # valor solo en .env local
# Preferir stdio / import agent path; evitar CLI --http hasta verificar bug
# Si Qdrant: docker run (Compose ABSENT) — un contenedor, un worker
# uvicorn con --workers 1 si se usa API
```

## FULL_CHAT_STACK

Requiere Compose o equivalente `docker run` multi-servicio — **no** smoke mínimo.

## TEXT2SPARQL_VIRTUOSO

**BLOCKED_ON_LOCAL_HOST** — no comandos locales.
