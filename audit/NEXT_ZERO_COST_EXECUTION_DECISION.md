# NEXT_ZERO_COST_EXECUTION_DECISION — Prompt 11C

**Fecha:** 2026-07-21  
**Política:** `MAX_EXTERNAL_MONETARY_COST_USD = 0.00` (`HUMAN_DECISION_VERIFIED`)  
**Informe:** `audit/ZERO_COST_NATIVE_AUDIT_REGATE.md`  
**Matriz:** `audit/ZERO_COST_ACTION_MATRIX.csv`  
**Cola:** `audit/ZERO_COST_NATIVE_REPRODUCTION_QUEUE.csv`

**Nota:** el re-gate interino que propuso rdfconfig legal como GO_NEXT queda **superseded** por esta decisión formal 11C.

---

## 1. Acción seleccionada

**Z1 — SGPT_ENVIRONMENT_DEFINITION**  
Definición documental de entorno SGPT: dependencias, pins, rutas de datos, límites RAM/VRAM, harness, límites de lo que *no* se hará (sin train, sin Table 4, sin checkpoints inventados).

## 2. Método

`sgpt`

## 3. Clase

**`GO_NEXT_ZERO_COST`**

## 4. Evidencia

| Hecho | Etiqueta |
|---|---|
| MIT confirmada | LEGAL_VERIFIED |
| Static WAVE_B complete; datasets presentes | CODE_VERIFIED / DATA_VERIFIED |
| Checkpoints NOT_FOUND | NOT_FOUND |
| Ready para env definition; reduced train conditional | CODE_VERIFIED (`EXECUTION_READINESS`) |
| Política coste cero | HUMAN_DECISION_VERIFIED |

## 5. Coste monetario externo esperado

**0.00 USD**

## 6. Valor científico

Prepara la única baseline generativa supervisada (`core_baseline_candidate`) para un futuro smoke reducido etiquetado, sin gastar API y sin fingir Table 4. Diversifica respecto a `sparql_llm` ya en `smoke_only` offline.

## 7. Relación con PE1–PE4

- PE1: sin cambio (substantially_answered).  
- PE2: prep de entorno hacia fracción instalable/ejecutable débil futura.  
- PE3: sigue not_started.  
- PE4: aclara deps/recursos/MISSING_CHECKPOINT como barrera.

## 8. Recursos

Solo documentación en el próximo prompt; sin pip/Docker run en 11C. Futuro prompt de env: lectura upstream + posible Dockerfile documental; sin train.

## 9. Descargas futuras posibles

GPT-2 base (gratuita) **solo** si un prompt posterior lo autoriza explícitamente para Z3 — **no** en el próximo prompt de env definition.

## 10. Riesgos

- Deslizar a train o claim Table 4.  
- Ignorar anomalías métricas ya auditadas.  
- Confundir env ready con native reproduction.

## 11. GO criteria (éxito del próximo prompt)

Documento de entorno SGPT con: deps/pins; datos paths; VRAM/RAM notes; qué está blocked (checkpoints); checklist hacia Z2; stop conditions; sin installs forzados si se mantiene documental-only (o installs solo si el prompt futuro lo permite — el título abajo es definición documental).

## 12. NO-GO criteria

No proceder a train; no descargar sin auth; no afirmar PE3; no adapters.

## 13. Stop conditions

Abortar el prompt futuro si se intenta: train, inferencia con checkpoint inventado, Answer F1 inventado, gasto API, modificación upstream.

## 14. Alternativas aplazadas (razón breve)

| ID | Razón |
|---|---|
| Z2 | Después de Z1 |
| Z3 | HOLD_MISSING_MODEL / VRAM / download auth |
| Z4 | DOCUMENT_ONLY; menos camino a ejecución verificable que Z1 |
| Z5 | Ruby ABSENT; companion ≠ generador |
| Z6–Z7 | Documentary / missing code; results≠repro |
| Z8 | NO_GO_ZERO_COST_POLICY |
| Z9 | NOT_SELECTED mutability |
| Z10 | SUBSTITUTION_NOT_NATIVE |
| Z11 | HOLD_LEGAL |
| Z12 | HOLD_HARDWARE (+ legal) |

## 15. Título exacto del próximo prompt

**Prompt 12 — Definición documental de entorno SGPT (ZERO_COST; sin train; sin Table 4)**

## 16. Alcance exacto del próximo prompt

Solo definición de entorno/documentación de readiness SGPT bajo coste cero. **Prohibido:** train, inferencia, descarga no autorizada, OpenRouter, POST `/chat`, adapters, cambio de `reproduction_status`, cierre de Fase 1. **No** ejecutar Z2/Z3 en el mismo prompt salvo que el planificador lo limite explícitamente (recomendación: solo Z1).
