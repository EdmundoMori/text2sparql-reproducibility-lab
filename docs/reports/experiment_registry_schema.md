# Esquema de EXPERIMENT_REGISTRY.jsonl

Archivo append-only. Cada línea es un objeto JSON.  
Estado actual: **archivo vacío** (ningún experimento ejecutado).

## Campos previstos (referencia; no ejecutados aún)

```json
{
  "experiment_id": "string",
  "timestamp": "ISO-8601",
  "method_id": "string",
  "phase": "native|common",
  "reproduction_status": "see RESEARCH_PROTOCOL.md §5",
  "commit_sha": "string|null",
  "command": "string",
  "metrics_kind": "original|common|diagnostic|none",
  "metrics": {},
  "artifacts": [],
  "notes": "string"
}
```

No añadir líneas sintéticas. Solo registrar ejecuciones reales.
