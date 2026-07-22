# GIT_BLOB_AND_SHA256_VERIFICATION_PLAN

**RUN_ID:** `20260722T105246Z` · Prompt 21A · Status: `FUTURE_EXECUTION_CONTRACT_DEFINED` · **NOT_EXECUTED**

## Algoritmos separados

### Git blob OID (SHA-1)
```
SHA-1( b"blob " + decimal_file_size + b"\0" + exact_file_bytes )
```
OIDs esperados en `QALD9PLUS_EN_DBPEDIA_EXACT_FILE_MANIFEST.yaml`.

### SHA-256 local
`SHA-256(exact_file_bytes)` tras descarga · `PUBLISHED_SHA256_NOT_AVAILABLE` en origen · `LOCAL_SHA256_PENDING_ACQUISITION` ahora.

## Reglas T6B
1. Validar bytes antes de cualquier normalización.
2. No modificar line endings.
3. Comprobar tamaño exacto.
4. Comprobar Git blob OID.
5. Calcular SHA-256 local.
6. Registrar ambos algoritmos por separado.
7. Cualquier discrepancia → no PASS.
8. No reemplazar desde mirror.

**No ejecutado en Prompt 21A.**
