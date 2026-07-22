# INCLUSION_DECISIONS

**Fecha:** 2026-07-18  
**Protocolo:** `RESEARCH_PROTOCOL.md` §6  
**Clases usadas:** `INCLUDE_PRIMARY` | `INCLUDE_CONDITIONAL` | `HISTORICAL_ONLY` | `EXCLUDE_NOT_REPRODUCIBLE` | `PENDING_EVIDENCE`

Ningún método se clasifica como reproducido: solo se decide inclusión para estudio/auditoría nativa posterior. **No se clonó código.**

---

## Criterios aplicados (recordatorio)

Inclusión requiere evidencia de: (1) NL→SPARQL explícito, (2) artículo, (3) código público, (4) evaluación documentada, (5) estudiabilidad.  
La reproducibilidad local se verifica después; aquí solo se clasifica elegibilidad y prioridad.

---

## Decisiones

### sparql_llm → `INCLUDE_PRIMARY`

- Cumple los cinco criterios con evidencia primaria (arXiv + repo MIT activo + F1 TEXT2SPARQL).  
- Genera SPARQL explícitas; evaluación y código claros.  
- Condiciones operativas (API LLM, Docker Compose) se gestionan en reproducción nativa, no degradan la inclusión primaria.

### mkgqagent → `INCLUDE_PRIMARY`

- Paper CEUR/arXiv + repo oficial + Macro F1 documentado + victoria TEXT2SPARQL 2025.  
- SPARQL explícita vía API del challenge.  
- **Condición documentada (no baja a CONDITIONAL):** licencia SPDX **UNKNOWN** — verificar antes de redistribuir artefactos; no impide estudio interno.

### cot_sparql → `INCLUDE_CONDITIONAL`

- Paper DOI + código + métricas fuertes en QALD/LC-QuAD.  
- Condiciones: licencia UNKNOWN; dependencia de LLM local grande (CodeLlama-34B GPTQ) frente a VRAM local ≈6 GB; entorno Conda documentado (Conda ausente en host → venv/pip).  
- Incluir para auditoría nativa con degradación posible a `feasible_using_api` o modelo más pequeño **solo si se documenta** (sin cambiar método y LLM a la vez en comparaciones controladas posteriores).

### firesparql → `INCLUDE_CONDITIONAL`

- Paper DOI + código + modelo HF + SciQA/ORKG.  
- Condiciones: KG académico (ORKG) ≠ DBpedia del protocolo común; instructions de requirements incompletas (“Coming soon”); licencia código UNKNOWN; train paper en H100.  
- Incluir para reproducción nativa SciQA; adaptación común a QALD-9 Plus queda condicionada a auditoría nativa completa.

### rdfconfig_llm → `INCLUDE_CONDITIONAL`

- Paper Bioinformatics DOI + código Zenodo/GitHub + rdf-config MIT + métricas Jaccard.  
- Condiciones: dominio life-science (UniProt/Rhea/Bgee), no DBpedia; requiere API + Ruby rdf-config; LICENSE file del generator ausente pese a claim MIT en README.  
- Incluir para nativa; común DBpedia solo tras adaptar schemas (fase posterior, fuera de upstream).

### sgpt → `INCLUDE_PRIMARY`

- Paper IEEE Access + repo MIT + train/eval documentados + GPT-2 local (sin API).  
- Buena baseline generativa reproducible en GPU modesta (paper: 2×12 GB).  
- Exactitud numérica de Table 4 queda UNKNOWN hasta re-extracción; no afecta inclusión.

### tebaqa → `HISTORICAL_ONLY`

- Paper DOI + código AGPL + evaluación GERBIL/QALD.  
- Template-based (no LLM); última actividad 2023; infra pesada (ES + multi-JVM) poco alineada con el eje LLM del lab.  
- Se conserva como baseline histórica documentada; **no** se prioriza para evaluación común LLM hasta que haya capacidad explícita. No es `EXCLUDE_NOT_REPRODUCIBLE` (código y paper existen).

---

## No usados en este lote

| Clase | Métodos |
|---|---|
| `EXCLUDE_NOT_REPRODUCIBLE` | — |
| `PENDING_EVIDENCE` | — |

---

## Gate hacia evaluación común

| method_id | `common_adapter_allowed` ahora | Motivo |
|---|---|---|
| todos | `false` | Auditoría nativa (clon+ejecución) aún no hecha |

---

## Advertencia de máquina (afinado)

**ADVERTENCIA [RAM/GPU/Compose]:** varios `INCLUDE_*` exigirán API o degradación en este host (WSL ≈7.4 GiB RAM; RTX 4050 ≈6 GB; sin Docker Compose).  
**SOLUCIÓN:** priorizar `mkgqagent` / `rdfconfig_llm` / `sparql_llm` vía API; `sgpt` local; diferir train FIRESPARQL y TeBaQA completo.  
**CONTINÚO:** registro y documentación listos; clonación solo cuando se solicite.

---

## Prompt 15 — Phase 1 final gate (añadido; no reescribe historia)

**Fecha cierre Fase 1:** 2026-07-22  
**Gate:** `PHASE1_CLOSED_READY_FOR_COMMON_EVALUATION_PROTOCOL_DEFINITION`  
**Qualifier:** `RESIDUAL_METHOD_BLOCKERS_PRESERVED`  
**phase1_status:** `closed` · **phase2_status:** `protocol_definition_pending`  
**Adapters:** `common_adapter_allowed=false` (todos)  
**Distribución (6 activos):** smoke_only×2 (sparql_llm, sgpt); blocked×3 (mkgqagent, rdfconfig_llm, cot_sparql); not_reproducible×1 (firesparql)  
**TeBaQA:** `HISTORICAL_ONLY` (fuera del denominador)  
**PE1:** substantially_answered · **PE2:** partial_evidence · **PE3:** not_started (`no_comparable_original_metric_run_available`) · **PE4:** substantially_answered_for_current_portfolio  
**Fase 2:** aún **no** ejecutada — solo elegibilidad documental; siguiente Prompt 16 (definición protocolo común), sin adapters ni benchmarks.  
**Informe:** `audit/PHASE1_FINAL_NATIVE_AUDIT_REPORT.md` · Decisión: `docs/decisions/006_phase1_native_audit_closure_and_phase2_transition.md`
