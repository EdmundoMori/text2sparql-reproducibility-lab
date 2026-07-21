# ZERO_COST_NATIVE_AUDIT_REGATE — Prompt 11C

**Fecha:** 2026-07-21  
**SHA inicial 11C:** `60590cc000cc18c76c796ca7a4655c07c658ffda`  
**Prompt 11 artifact commit:** `ee477c9d1d37b86d03593c141cd90577f7f1ba43`  
**Prompt 11 final HEAD:** `a2478b721970444401bd7edae313e1e1aa81926e`

---

## 1. Decisión humana

“elijo coste 0” — `HUMAN_DECISION_VERIFIED` (EDMUNDO MORI ORRILLO, 2026-07-21).  
`MAX_EXTERNAL_MONETARY_COST_USD = 0.00`.

## 2. Alcance

Re-gate documental de métodos activos bajo ZERO_USD. Sin installs, descargas, APIs, Docker execution ni train en 11C.

## 3. Evidencia conservada

CORE_OFFLINE 5B; protocolo 9; prep 10/10B; modelo/cota 11; WAVE_A–C; portafolio baselines.

## 4. Camino online cerrado

`LOCAL_CHAT_API_ONE_QUESTION` → **`NO_GO_ECONOMIC_ZERO_COST_POLICY`**.  
Técnicamente ready; autorización de gasto declined. Prompt 12 chat cancelled/deferred.

## 5. Definición de coste cero

Ver `audit/ZERO_COST_POLICY.md`.

## 6. Métodos activos

`sparql_llm` (smoke_only), `mkgqagent`, `rdfconfig_llm`, `sgpt`, `cot_sparql`, `firesparql` (audit_only). TeBaQA histórico.

## 7. Acciones evaluadas

Z1–Z12 en `ZERO_COST_ACTION_MATRIX.csv`.

## 8. Legalidad

| Método | Gate legal relevante |
|---|---|
| sgpt | internal_execution_allowed (MIT) |
| sparql_llm | allowed; spend declined |
| rdfconfig companion | MIT; generador unresolved |
| mkgqagent / cot / firesparql code | HOLD_LEGAL / blocked execution |

## 9. Factibilidad

Z1 ready (documental). Z3 conditional. Z8 blocked_by_policy. Z11/Z12 blocked.

## 10. Valor científico

Priorizar evidencia incremental hacia ejecución verificable $0 en familia distinta a sparql_llm.

## 11. Equivalencia nativa

Z8 sería native_equivalent_candidate si hubiera presupuesto. Z9/Z10 no nativos. Z1→Z3 = reduced_smoke_only path.

## 12. Nueva cola

`ZERO_COST_NATIVE_REPRODUCTION_QUEUE.csv` — **no** sobrescribe `NATIVE_REPRODUCTION_QUEUE.csv` (Prompt 8 histórico).  
Re-gate interino rdfconfig (`NATIVE_AUDIT_COMPARATIVE_GATE_RERUN_ZERO_USD.md`) superseded por 11C.

## 13. Acción seleccionada

**Z1 SGPT_ENVIRONMENT_DEFINITION** — `GO_NEXT_ZERO_COST`.

Regla lexicográfica: $0 → legal MIT → evidencia env incremental → código/datos presentes → viable local → sin sustitución → aproxima Z2/Z3 → stop conditions → 1–2 prompts a ejecución débil etiquetada → diversidad vs sparql_llm.

## 14. Alternativas aplazadas

Ver §14 de `NEXT_ZERO_COST_EXECUTION_DECISION.md`. Z4 rdfconfig legal = DOCUMENT_ONLY (no GO_NEXT 11C).

## 15. Efecto sobre PE1–PE4

| PE | Estado |
|---|---|
| PE1 | substantially_answered |
| PE2 | partial_evidence; online `deferred_by_zero_cost_policy` |
| PE3 | not_started |
| PE4 | partial_evidence |

## 16. Trabajo restante de Fase 1

Env SGPT; posibles Z2/Z3 etiquetados; cierres legales; política MISSING_*; no adapters; no PE3 aún.

## 17. Riesgos de sesgo

Sesgo offline-only; sesgo anti-API interpretado como fallo técnico; sesgo a train reducido como paper match.

## 18. Objetivo de largo plazo

Secuencia intacta: reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones.

## 19. Conclusión conservadora

Bajo coste cero, el laboratorio **no** ejecuta el smoke online de SPARQL-LLM. La siguiente acción documental es definir entorno SGPT, sin train y sin afirmar Table 4. Fase 1 permanece abierta.
