# GRAPH_AND_ENDPOINT_POLICY

**RUN_ID:** `20260722T083201Z` · GRAPH_SNAPSHOT_PENDING

## Preferencia

1. snapshot/dump inmutable;
2. endpoint reproducible asociado al snapshot;
3. endpoint remoto solo con captura de drift.

## Registrar en runs futuros

graph_id; graph_version; endpoint URL; fecha/hora; software endpoint; límites; timeout; result limit; default/named graphs; fingerprint/checksum snapshot; retries; query timeout; availability window.

## Antes de cualquier benchmark futuro

- ejecutar gold queries sobre el mismo grafo;
- identificar gold inválidas;
- distinguir dataset defect vs error del método;
- no usar respuestas históricas de otro grafo sin etiquetar drift.

Estado actual: **GRAPH_SNAPSHOT_PENDING**.
