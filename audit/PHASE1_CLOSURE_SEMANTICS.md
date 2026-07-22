# PHASE1_CLOSURE_SEMANTICS — Prompt 15

**Fecha:** 2026-07-22 · Coste USD 0.00 · documental

## A. `reproduction_status`

Describe el **resultado experimental** (no el grado de auditoría):

| Valor | Significado |
|---|---|
| `smoke_only` | Arranque/import/forward/ruta reducida verificados; **no** reproducción del artículo (`SMOKE_ONLY_NOT_REPRODUCTION`). |
| `blocked` | Ejecución nativa impedida por legal, hardware, política u otra barrera estructural documentada. |
| `not_reproducible` | Con artefactos disponibles no es posible reproducir el protocolo nativo (`NOT_REPRODUCIBLE_WITH_AVAILABLE_ARTIFACTS`). |
| `partially_reproduced` | Subconjunto sustancial del protocolo original con métricas comparables — **no usado en Prompt 15**. |
| `reproduced` | Reproducción nativa del artículo — **no usado en Prompt 15**. |

## B. `native_audit_complete`

Describe si la **auditoría nativa individual** está cerrada:

- artículo, código, datos, métricas y dependencias auditados;
- se intentó ejecutar cuando era legal y proporcional; **o**
- se documentó suficientemente por qué la ejecución no era legal, viable o posible.

Por tanto:

- `native_audit_complete=true` **no** implica reproducción;
- un método `blocked` / `not_reproducible` / `smoke_only` puede tener auditoría completa.

## C. `common_evaluation_protocol_eligibility`

Indica que el método puede considerarse al **diseñar** tracks y contratos de Fase 2.

No implica permiso legal de adapter, runtime disponible, ni benchmark inmediato.

## D. `common_adapter_allowed`

En Prompt 15 permanece **`false`** para todos los métodos (activos e histórico).
