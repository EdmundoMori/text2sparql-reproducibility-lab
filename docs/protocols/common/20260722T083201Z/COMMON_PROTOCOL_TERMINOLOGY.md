# COMMON_PROTOCOL_TERMINOLOGY

**RUN_ID:** `20260722T083201Z` · **Prompt 16** · PROTOCOL_FRAMEWORK_ONLY · Coste 0.00

## Definiciones

| Término | Definición |
|---|---|
| common evaluation | Evaluación bajo contratos/tracks/datasets/métricas comunes del lab (Fase 2+). Distinta de reproducción nativa. |
| native evaluation | Ejecución/auditoría del método en su protocolo del artículo (Fase 1). |
| benchmark | Ejecución autorizada del protocolo común. **No** ejecutado en Prompt 16. |
| dataset | Colección versionada de ítems. Pins: DATASET_PIN_PENDING. |
| graph snapshot | Dump inmutable del KG. Estado: GRAPH_SNAPSHOT_PENDING. |
| endpoint | Servicio SPARQL asociado a snapshot o contrato de drift. |
| method | Sistema Text-to-SPARQL (`method_id`). |
| method variant | Configuración comparable distinta (p. ej. sgpt_q vs sgpt_qk). |
| adapter | Capa fuera de upstream CommonInput→CommonOutput. Deshabilitado (common_adapter_allowed=false). |
| information-access track | Eje principal de fairness: qué información recibe el método. |
| execution-style tag | Etiqueta arquitectónica. No crea fairness track por sí sola. |
| adaptation regime | Cómo se adapta (zero-shot, supervised, oracle input, …). |
| model-control regime | Backbone nativo vs controlado del lab. |
| oracle input | Entidades/relaciones/schema gold suministrados. |
| external grounding | Salidas de linker externo común y congelado. |
| evaluable item | Ítem del conjunto pre-declarado con status. |
| dataset defect | Defecto dataset/gold/grafo → exclusión global. |
| abstention | Método no responde; permanece en denominador. |
| method failure | Timeout, query inválida, error ejecución, sin output. |
| system failure | Fallo infraestructura (outage) no imputable automáticamente. |
| comparable run | Cumple COMPARABILITY_RULES. |
| descriptive cross-track result | Entre tracks distintos: DESCRIPTIVE_CROSS_TRACK_ONLY. |

## Regla

Una arquitectura distinta no crea automáticamente un track distinto. El track principal representa la información que el método recibe.
