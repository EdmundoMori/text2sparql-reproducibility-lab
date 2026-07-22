# SPARQL_EXECUTION_SAFETY_CONTRACT

**RUN_ID:** `20260722T093257Z`

## No autorizados en benchmark v1

SPARQL Update; LOAD; CLEAR; CREATE; DROP; COPY; MOVE; ADD; SERVICE no allowlisted; `file:`; federados no registrados; modificación de grafo.

## Estados

`SAFE_QUERY` · `UNSAFE_QUERY` · `PARSE_INVALID` · `QUERY_FORM_OUT_OF_SCOPE`

Predicción insegura = fallo del método → cero en métricas semánticas. **No validado en Prompt 18.**
