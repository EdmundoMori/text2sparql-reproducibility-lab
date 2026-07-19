# PLAN_SYNC — Estado para optimización del plan de prompts

**Audiencia principal:** ChatGPT (planificador de prompts) y el investigador.  
**Repo GitHub:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab  
**Última actualización:** 2026-07-19 (push completo con `upstream/` vendorizado)  
**Fase lab:** 1 — auditoría / reproducibilidad nativa (clon estático hecho; sin ejecución experimental)

> Instrucción para el planificador: lee este archivo primero. Usa los documentos específicos enlazados para detalle. **No asumas reproducción experimental**: clonar ≠ ejecutar ≠ reproducir un paper. Propón el siguiente prompt adaptado a evidencias, limitaciones de máquina y gates científicos.

---

## 1. Objetivo del laboratorio (recordatorio)

Laboratorio local Text-to-SPARQL: auditar y, cuando sea posible, reproducir métodos publicados; luego evaluarlos bajo protocolo común (QALD-9 Plus EN/DBpedia → LC-QuAD 2.0); a largo plazo, adaptar a KG de descubrimiento de modelos de IA y diseñar un método nuevo con ablaciones.

Documentos rectores del lab (no sustituyen este sync):

| Documento | Ruta |
|---|---|
| Contexto operativo | [`PROJECT_CONTEXT.md`](PROJECT_CONTEXT.md) |
| Protocolo científico | [`RESEARCH_PROTOCOL.md`](RESEARCH_PROTOCOL.md) |
| Perfil de máquina | [`MACHINE_PROFILE.md`](MACHINE_PROFILE.md) |
| Registro de métodos | [`METHOD_REGISTRY.yaml`](METHOD_REGISTRY.yaml) |
| Pins de clones | [`REPOSITORIES.lock.yaml`](REPOSITORIES.lock.yaml) |

---

## 2. Bucle Cursor ↔ ChatGPT

```text
ChatGPT (plan prompts)
    → investigador ejecuta prompt en Cursor
        → Cursor actualiza PLAN_SYNC + docs específicos + push GitHub
            → ChatGPT relee repo y adapta el siguiente prompt
```

Reglas del bucle:

1. Tras cada prompt ejecutado, Cursor actualiza **este** archivo (§3–§7) y, si hace falta, docs específicos.  
2. Cursor registra rutas de docs específicos en [`docs/plan-sync/ARTIFACT_INDEX.md`](docs/plan-sync/ARTIFACT_INDEX.md).  
3. Se hace **commit + push** al repo GitHub (sin `upstream/`, sin secretos, sin datasets/modelos pesados).  
4. ChatGPT debe proponer el **siguiente prompt concreto**, no reescribir todo el plan desde cero salvo bloqueo metodológico.  
5. Respetar `PROJECT_CONTEXT.md` §7: advertencia → solución → continuar ante límites de máquina.

---

## 3. Qué se ha completado (prompts ejecutados)

| # | Prompt / acción | Resultado clave | Docs específicos |
|---|---|---|---|
| 0 | Fundación | `PROJECT_CONTEXT.md`, `RESEARCH_PROTOCOL.md` | mismos |
| 1 | Workspace | Árbol de dirs, Makefile, registries, `.env.example` | [`README.md`](README.md), [`MACHINE_PROFILE.md`](MACHINE_PROFILE.md) |
| 1b | Límites de máquina en contexto | Protocolo advertir→mitigar→continuar | [`docs/decisions/001_machine_limits_warn_and_continue.md`](docs/decisions/001_machine_limits_warn_and_continue.md) |
| 2 | Paper/código/evidencia | 7 candidatos auditados; inclusión decidida | [`audit/PAPER_CODE_MAPPING.md`](audit/PAPER_CODE_MAPPING.md), [`audit/INITIAL_AUDIT_MATRIX.csv`](audit/INITIAL_AUDIT_MATRIX.csv), [`audit/INCLUSION_DECISIONS.md`](audit/INCLUSION_DECISIONS.md), [`audit/RESOURCE_ESTIMATION.md`](audit/RESOURCE_ESTIMATION.md) |
| 2b | Cierre evidencias | Licencias, venue SPARQL-LLM, Table 4 SGPT | [`audit/EVIDENCE_CLOSURE.md`](audit/EVIDENCE_CLOSURE.md), [`audit/LICENSE_MATRIX.csv`](audit/LICENSE_MATRIX.csv), [`audit/RESULT_EVIDENCE_MATRIX.csv`](audit/RESULT_EVIDENCE_MATRIX.csv), [`audit/PUBLICATION_STATUS.csv`](audit/PUBLICATION_STATUS.csv) |
| 3 | Clonado estático | 7 clones; tebaqa excluido; ondas A–D | [`audit/CLONING_REPORT.md`](audit/CLONING_REPORT.md), [`scripts/clone_repositories.sh`](scripts/clone_repositories.sh) |
| Sync | Este mecanismo | `PLAN_SYNC.md` + índice para el planificador | [`docs/plan-sync/ARTIFACT_INDEX.md`](docs/plan-sync/ARTIFACT_INDEX.md), [`docs/plan-sync/NEXT_PROMPT_GUIDANCE.md`](docs/plan-sync/NEXT_PROMPT_GUIDANCE.md) |
| Sync-full | Vendor `upstream/` en GitHub | Árboles de código clonados versionados (~1.2 GiB); `.git` anidados → `.git_local/` local | [`docs/decisions/002_vendor_upstream_on_github.md`](docs/decisions/002_vendor_upstream_on_github.md), `upstream/<method_id>/` |

---

## 4. Hallazgos críticos para adaptar el plan

### 4.1 Máquina (condiciona ejecución)

- Windows + **WSL2** Ubuntu 22.04; RAM WSL ≈ **7.4 GiB**; host ≈ 16 GiB.  
- GPU: RTX 4050 ≈ **6 GiB** VRAM; `nvcc` ausente; Docker OK; **Compose plugin ausente**.  
- Sin Conda/uv; Poetry sí; solo `python3`.  
- Clases útiles: `feasible_using_api`, `feasible_local_gpu` (ligero), `requires_external_gpu`.

→ Preferir prompts de **auditoría estática** y **smoke API (WAVE_A)** antes de train/GPU pesada.

### 4.2 Inclusión de métodos

| Decisión | Métodos |
|---|---|
| INCLUDE_PRIMARY | `sparql_llm`, `mkgqagent`, `sgpt` |
| INCLUDE_CONDITIONAL | `cot_sparql`, `firesparql`, `rdfconfig_llm` |
| HISTORICAL_ONLY (no clonado) | `tebaqa` |

### 4.3 Ondas post-clon

| Wave | Métodos | Implicación para el plan |
|---|---|---|
| WAVE_A | sparql_llm, mkgqagent, rdfconfig_llm | Candidatos a smoke/API siguiente |
| WAVE_B | sgpt | Local condicional (train/eval); no aún |
| WAVE_C | cot_sparql, firesparql | Solo auditoría estática por ahora |
| WAVE_D | tebaqa | Excluido del clon actual |

### 4.4 Bloqueos legales / publicación

- **LICENSE_NOT_CONFIRMED** (clon OK, **no** adaptar/integrar aún): mkgqagent, cot_sparql, firesparql, scott2121 generator.  
- SPARQL-LLM: preprint **Under Review** (arXiv); DOI TWEB **no verificado**.  
- Código público ≠ reutilizable confirmado.

### 4.5 Anomalías de clon

- `firesparql` ~598M (mucho `results/` en Git).  
- `sgpt` ~169 MiB datasets en árbol.  
- Tag mkgqagent tipográfico: `TEXT2SPAQL`.  
- Submódulos: ninguno.

### 4.6 Lo que NO se ha hecho

- Instalación de dependencias / entornos por método.  
- Ejecución de pipelines, entrenamientos, evaluación.  
- Adaptadores comunes.  
- Descarga HF/Docker images.  
- Declarar ningún método como `reproduced`.

---

## 5. Estado de reproducción (protocolo)

Todos los métodos clonados: como máximo `audit_only` / clon estático.  
**Ninguno** en `reproduced` / `partially_reproduced` / `smoke_only` documentado como experimento formal aún.

---

## 6. Recomendación al planificador (siguiente prompt)

Prioridad sugerida (ajustable):

1. **Auditoría estática WAVE_A** en `upstream/` (README, entrypoints, deps, secrets requeridos, riesgo Compose) → ficha por método en `audit/<method_id>/`.  
2. Opcional: **smoke controlado WAVE_A** solo si hay `.env` y presupuesto API; etiquetar explícitamente `smoke_only`, no reproducción.  
3. **No** lanzar train FIRESPARQL/CoT-34B/TeBaQA.  
4. Mantener gate: sin auditoría nativa completa → `common_adapter_allowed: false`.  
5. Para repos `LICENSE_NOT_CONFIRMED`: inspección sí; adapters no.

Detalle operativo: [`docs/plan-sync/NEXT_PROMPT_GUIDANCE.md`](docs/plan-sync/NEXT_PROMPT_GUIDANCE.md).

---

## 7. Índice rápido de artefactos específicos

Ver lista completa y estable en:

→ [`docs/plan-sync/ARTIFACT_INDEX.md`](docs/plan-sync/ARTIFACT_INDEX.md)

---

## 8. Changelog de este archivo

| Fecha | Cambio |
|---|---|
| 2026-07-19 | Creación del mecanismo PLAN_SYNC + primer volcado de estado post-clon |
| 2026-07-19 | Push completo: `upstream/` vendorizado en GitHub (decisión 002); el planificador puede leer código clonado |
