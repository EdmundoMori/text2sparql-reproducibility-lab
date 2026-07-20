# Execution readiness — SGPT (WAVE_B)

**Fecha:** 2026-07-20  
**method_id:** `sgpt`  
**pinned_commit:** `1f6964d1c3bfee50c7dec2c25546f32b4ab94b2b` (`PIN`)  
**reproduction_status (lab):** `audit_only` — **sin cambio** tras esta auditoría estática.

---

## Estados por capacidad

| Capacidad | Estado | Evidencia / bloqueo |
|---|---|---|
| Inventario de datos | **ready** | `DATA_VERIFIED` logs + `DATASET_INVENTORY.csv` |
| `import_or_model` | **unknown / conditional** | sin pip/import en esta pasada; deps + HF `gpt2` |
| `inference_with_checkpoint` | **blocked** | checkpoints `NOT_FOUND` |
| `reduced_training` | **conditional** | posible futuro smoke etiquetado; no Table 4 |
| `native_reproduction` | **not_ready** | VRAM 6 GiB vs 2×12 GB; mismatch splits; métricas anómalas; sin pesos |

---

## Clasificación host

| Dimensión | Veredicto |
|---|---|
| Factibilidad local full | **CONDITIONAL / not_ready** |
| DATA_ONLY | **ready** |
| IMPORT smoke | necesitaría env + network |
| INFERENCE | **blocked** |
| REDUCED_TRAINING_SMOKE | **conditional** futuro |
| NATIVE_REPRODUCTION | **not_ready** |

---

## Próximos pasos recomendados (conservadores)

1. Mantener `reproduction_status = audit_only`.
2. Siguiente ola de trabajo lab: **WAVE_C** auditoría estática (otros métodos), no forzar native SGPT.
3. Si en el futuro se hace smoke SGPT: etiquetar explícitamente **`DATA_ONLY`** o **`REDUCED_TRAINING_SMOKE`** — **nunca** como native reproduction / Table 4 match.
4. No afirmar Answer F1 ni ejecución SPARQL (código no las calcula).

---

## Artefactos de esta pasada

Ver checklist en respuesta del agente y `STATIC_AUDIT.md` §26.
