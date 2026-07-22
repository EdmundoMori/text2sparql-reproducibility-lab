# RDFCONFIG_TRACK_RESOLUTION

**RUN_ID:** `20260722T095602Z` · inspección estática `upstream/rdfconfig_llm/rdf-config/config/`

## Evidencia
Presentes (entre otros): `bgee`, `rhea`, `uniprot`, `uniprot_and_bgee`, y también `dbpedia/` (demo/toy model Book/Game; endpoint localhost). Companion pin separado puede diferir.

## Decisión
### A. rdfconfig_domain_native — IA_DOMAIN_NATIVE
Bgee/Rhea/UniProt (y combinaciones presentes). `CONTRACT_DOMAIN_NATIVE_ONLY`. Fuera del benchmark QALD DBpedia principal.

### B. rdfconfig_schema_common_dbpedia — NEGATIVE
`ADAPTER_NEGATIVE_CONTRACT_DEFINED`. Existe YAML demo `config/dbpedia`, pero **no** constituye schema bundle común QALD/lab-verified.
→ `CONTRACT_BLOCKED_MISSING_ARTIFACT` (common QALD-aligned schema bundle ausente) + LEGAL_NOT_CONFIRMED.
No candidato executable IA_SCHEMA_COMMON.

Asignación ambigua `IA_SCHEMA_COMMON|IA_DOMAIN_NATIVE` → variantes separadas.
