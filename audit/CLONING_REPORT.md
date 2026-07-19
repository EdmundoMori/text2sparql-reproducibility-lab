# CLONING_REPORT

**Fecha:** 2026-07-18T21:00:15+02:00  
**Script:** `scripts/clone_repositories.sh`  
**Manifest:** `configs/clone_manifest.yaml`  
**Logs:** `logs/cloning/`  
**Lock:** `REPOSITORIES.lock.yaml`  
**Política:** `GIT_LFS_SKIP_SMUDGE=1`; sin instalaciones; sin entrenamientos; sin modificar `upstream/`.  
**Alcance:** solo `INCLUDE_PRIMARY` + `INCLUDE_CONDITIONAL`. **`tebaqa` no clonado** (`HISTORICAL_ONLY`).

Clonar ≠ decidir ejecución local. Auditoría estática únicamente.

---

## 1. Repositorios clonados (7 paths / 6 method_ids)

| method_id | role | local_path | URL | branch | commit SHA | commit date | tags@HEAD | license | disk | wave |
|---|---|---|---|---|---|---|---|---|---|---|
| sparql_llm | primary | `upstream/sparql_llm` | sib-swiss/sparql-llm | main | `3748730e3bd2df2595280b918269fdaadb9fc0c3` | 2026-05-19T19:43:52+03:00 | none | MIT | 139M | WAVE_A |
| mkgqagent | primary | `upstream/mkgqagent` | WSE-research/text2sparql-agent | main | `ba0f2f78611a7ccacc8c985a97f6008ef7ee6a6a` | 2026-07-07T10:23:01+02:00 | `v1.0.0-TEXT2SPAQL-ESWC2025` | LICENSE_NOT_CONFIRMED | 6.0M | WAVE_A |
| rdfconfig_llm | primary | `upstream/rdfconfig_llm` | scott2121/sparql_query_generator | main | `fe63171d3c8b9679779749ee11f731b2a8318053` | 2025-12-22T21:37:45+09:00 | `v1.0.0` | LICENSE_NOT_CONFIRMED | 62M | WAVE_A |
| rdfconfig_llm | companion | `upstream/rdfconfig_llm_rdf-config` | dbcls/rdf-config | master | `cccc581c16f0b24865030bc5459475a9d0fcbd5f` | 2026-07-15T10:59:50+09:00 | none | MIT | 126M | WAVE_A |
| sgpt | primary | `upstream/sgpt` | rashad101/SGPT-SPARQL-query-generation | main | `1f6964d1c3bfee50c7dec2c25546f32b4ab94b2b` | 2024-09-15T11:21:37+02:00 | none | MIT | 218M | WAVE_B |
| cot_sparql | primary | `upstream/cot_sparql` | dice-group/CoT-Sparql | main | `063edd9868425e54010a0cb49ce585ed2186be4d` | 2024-06-03T15:26:39+02:00 | none | LICENSE_NOT_CONFIRMED | 64M | WAVE_C |
| firesparql | primary | `upstream/firesparql` | sherry-pan/FIRESPARQL | main | `48d6f168e4c1dd3dc467553aef370299911d4e76` | 2025-05-28T12:00:49+02:00 | none | LICENSE_NOT_CONFIRMED | 598M | WAVE_C |

**Fallidos:** ninguno (tras corrección del parser `expected_commit`; primer intento falló por bug de campos, no por red).

---

## 2. No clonados

| method_id | Motivo |
|---|---|
| tebaqa | `HISTORICAL_ONLY` — fuera del alcance de este clon. Clasificación de onda: **WAVE_D_EXCLUDED** (para esta fase de clonado). |

---

## 3. Submódulos

Ningún repositorio clonado tiene `.gitmodules` ni submódulos activos (`git submodule status` vacío en todos).  
`git clone --recurse-submodules` ejecutado igualmente; sin efecto.

---

## 4. Tamaños (heurística post-clon; no es inventario de artefactos externos)

Estimaciones por extensión/ruta sobre el working tree **sin** `.git` (MiB). No se descargaron HF/Docker/LFS smudge.

| path | disk total | source_code_est | models_est | datasets/results_est | docker_meta_est | other_est | n_files |
|---|---|---:|---:|---:|---:|---:|---:|
| sparql_llm | 139M | 3.79 | 0.0 | 87.75 | 0.01 | 1.02 | 132 |
| mkgqagent | 6.0M | 0.06 | 0.06 | 2.73 | 0.0 | 0.56 | 32 |
| rdfconfig_llm | 62M | 2.16 | 0.0 | 1.65 | 0.0 | 30.55 | 1287 |
| rdfconfig_llm_rdf-config | 126M | 10.06 | 0.0 | 14.5 | 0.0 | 32.07 | 906 |
| sgpt | 218M | 0.11 | 0.0 | 168.88 | 0.0 | 0.03 | 46 |
| cot_sparql | 64M | 0.1 | 0.0 | 49.85 | 0.0 | 0.46 | 22 |
| firesparql | 598M | 0.55 | 0.0 | **309.48** | 0.0 | 2.35 | 71954 |

**Modelos HF / imágenes Docker / checkpoints externos:** no descargados. Tamaño estimado externo:

| Artefacto externo | Estimación | Nota |
|---|---|---|
| FIRESPARQL HF LLaMA-3-8B LoRA | UNKNOWN (no descargado; orden GiB típico) | Solo referencia en README/HF |
| sparql_llm / mkgqagent / rdfconfig LLMs API | 0 local | API |
| sgpt GPT-2 weights | UNKNOWN si se entrenan; **0 en repo** como `.pt` | Hay que entrenar para pesos |
| Docker images | 0 descargadas | Compose/Dockerfile presentes en algunos repos |

---

## 5. Ondas (post-clon, verificadas)

| Wave | method_id | Verificación |
|---|---|---|
| **WAVE_A_API_OR_LIGHTWEIGHT** | sparql_llm, mkgqagent, rdfconfig_llm (+ companion) | Confirmado: API/LLM remoto o tooling ligero; aptos para smoke futuro vía API |
| **WAVE_B_LOCAL_CONDITIONAL** | sgpt | Confirmado: train/eval local GPT-2; datasets en árbol (~169 MiB) |
| **WAVE_C_STATIC_AUDIT_ONLY** | cot_sparql, firesparql | Confirmado para esta fase: GPU/requirements/licencia o peso de `results/` desaconsejan ejecución inmediata |
| **WAVE_D_EXCLUDED** | tebaqa | No clonado (`HISTORICAL_ONLY`) |

---

## 6. Anomalías

1. **Bug del script (corregido):** el primer run interpretó `inclusion_decision` como `expected_commit` (campos vacíos). Corregido con sentinel `NONE` / separador `|`. Clones ya existentes se revalidaron sin re-descarga.  
2. **firesparql ~598M / 71k archivos:** el árbol Git incluye `results/` y datasets procesados (≈309 MiB heurística). `GIT_LFS_SKIP_SMUDGE=1` no evita blobs Git normales (0 archivos LFS listados).  
3. **sgpt ~169 MiB en `data/`:** datasets procesados vienen en el clone (no LFS).  
4. **Tag tipográfico mkgqagent:** `v1.0.0-TEXT2SPAQL-ESWC2025` (falta una R en SPARQL).  
5. **LICENSE_NOT_CONFIRMED** en mkgqagent, cot_sparql, firesparql, rdfconfig_llm (generator): clonados solo para inspección; **no** integrar en adaptadores.  
6. **rdfconfig_llm** clona dos paths: primary + companion oficial `dbcls/rdf-config`.  
7. Working trees **limpios** (sin modificaciones locales).

---

## 7. Licencias en `licenses/`

| Carpeta | Contenido |
|---|---|
| `licenses/sparql_llm/` | `LICENSE.txt` (MIT) |
| `licenses/sgpt/` | `LICENSE.md` (MIT) |
| `licenses/rdfconfig_llm_rdf-config/` | `LICENSE` (MIT) |
| `licenses/mkgqagent/`, `cot_sparql/`, `firesparql/`, `rdfconfig_llm/` | `NO_LICENSE_FILE` + `README_LICENSE.md` (`LICENSE_NOT_CONFIRMED`) |

---

## 8. Detención

**Fin de fase de clonado.** No se instalaron dependencias, no se entrenó, no se bajaron modelos HF ni imágenes Docker. Siguiente paso (cuando se solicite): auditoría estática / smoke solo WAVE_A según protocolo.
