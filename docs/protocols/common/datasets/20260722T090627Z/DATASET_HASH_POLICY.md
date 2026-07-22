# DATASET_HASH_POLICY

**RUN_ID:** `20260722T090627Z`

| Tipo | Qué garantiza | No garantiza |
|---|---|---|
| repository commit SHA | estado del repo | contenido de un archivo aislado fuera del tree |
| Git tree OID | conjunto de paths | checksum de archivo independiente |
| Git blob OID | contenido del blob en Git | algoritmo SHA-256 de archivo suelto |
| release/archive checksum | archive publicado | n/a (no hay releases aquí) |
| LFS OID | puntero LFS | payload (no usado) |
| HTTP ETag | cache HTTP | integridad de dataset |
| metadata-response SHA-256 | respuesta API/HTML guardada | payload dataset |
| local payload SHA-256 | copia local existente | igualdad con fuente remota sin comparar blobs |

**Reglas Prompt 17:** no etiquetar Git SHA como SHA-256; checksum oficial ausente → `NOT_PUBLISHED_PENDING_CONTROLLED_ACQUISITION`.
