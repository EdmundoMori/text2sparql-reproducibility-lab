# Z3_AUTHORIZATION_LEDGER — SGPT Z3

**Fecha:** 2026-07-22 · Prompt 14D · Coste acumulado externo: **USD 0.00**

No se inventan firmas. Todas las entradas siguientes están **consumidas** y **no reutilizables**.

---

## 1. Prompt 14B — P1 descarga + P2A model load

| Campo | Valor |
|---|---|
| Alcance | Descarga GPT-2 revision fijada; build imagen Z3; preflight load offline |
| Aprobador | EDMUNDO MORI ORRILLO |
| Fecha | 2026-07-21 |
| Resultado | `Z3_P2A_MODEL_LOAD_PREFLIGHT_PASS` |
| Estado | `AUTHORIZED_AND_CONSUMED_14B_P1_P2A` |
| Reutilizable | **no** |
| Coste | 0.00 |
| No autorizado | train, backward, optimizer, Table 4, P2B/14C |

Artefacto: `environments/sgpt/builds/20260721T135432Z/`

---

## 2. Prompt 14B2 — P2B no-grad forward

| Campo | Valor |
|---|---|
| Alcance | Exactamente un forward `torch.no_grad()` sobre canario |
| Aprobador | EDMUNDO MORI ORRILLO |
| Fecha | 2026-07-21 |
| Resultado | `Z3_P2B_NOGRAD_FORWARD_PASS` |
| Estado | `AUTHORIZED_AND_CONSUMED_14B2_P2B` |
| Reutilizable | **no** (no cubre 14C) |
| Coste | 0.00 |
| No autorizado | backward, train, downloads, rebuild, 14C |

Artefacto: `environments/sgpt/builds/20260721T163853Z/`

---

## 3. Prompt 14C — attempt 1 (one-step train)

| Campo | Valor |
|---|---|
| Alcance | Un optimizer.step / 1 época / canario 1/1/1 |
| Aprobador | EDMUNDO MORI ORRILLO |
| Fecha | 2026-07-21 (auth) / run `20260721T183611Z` |
| Resultado bruto | `Z3_OTHER_FAILED` (scheduler count) |
| Estado | `AUTHORIZED_AND_CONSUMED_14C_ATTEMPT1` |
| Reutilizable | **no** |
| Coste | 0.00 |
| No autorizado | reintento automático, Table 4, PE3 |

Artefacto: `environments/sgpt/builds/20260721T183611Z/`

---

## 4. Prompt 14C — attempt 2 (reautorización humana)

| Campo | Valor |
|---|---|
| Alcance | Igual que attempt 1; **nueva** auth humana tras FAIL |
| Aprobador | EDMUNDO MORI ORRILLO |
| Fecha | 2026-07-21 (texto) / ejecución 2026-07-22 `20260722T072146Z` |
| Resultado bruto | `Z3_OTHER_FAILED` (optimizer hook=0) |
| Interpretación operativa | `Z3_ONE_STEP_REDUCED_TRAINING_PASS` + qualifier indirecto |
| Estado | `AUTHORIZED_AND_CONSUMED_14C_ATTEMPT2` |
| Reutilizable | **no** |
| Coste | 0.00 |
| No autorizado | tercer intento, Table 4, re-train por instrumentación |

Artefacto: `environments/sgpt/builds/20260722T072146Z/`

---

## Resumen

| Auth | Consumida | Cubierta |
|---|---|---|
| 14B P1/P2A | sí | load |
| 14B2 P2B | sí | 1 forward |
| 14C att.1 | sí | train intento 1 |
| 14C att.2 | sí | train intento 2 |

**No existe autorización vigente** para nuevo train, download, Docker rebuild ni instrumentación repetida.
