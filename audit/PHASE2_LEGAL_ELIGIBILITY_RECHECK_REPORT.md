# PHASE2_LEGAL_ELIGIBILITY_RECHECK_REPORT — Prompt 20

**RUN_ID:** `20260722T102434Z`  
**Clasificación:** `LAB_POLICY_CLASSIFICATION_BASED_ON_PUBLISHED_EVIDENCE`  
**Coste externo:** `0.00`  
**Gate:** `LEGAL_RECHECK_COMPLETE_PARTIAL_SCOPE_READY_FOR_ACQUISITION_AUTHORIZATION_PACKAGE`

## 1. Resumen ejecutivo
Revalidación documental pin vs HEAD sin descargas ni implementación. SPARQL-LLM y SGPT: MIT en pin → G3C `SATISFIED_EVIDENCE`. mKGQAgent, RDFConfig GitHub, CoT-SPARQL, FIRESPARQL: `LICENSE_ABSENT_AT_PIN` → G3C `NOT_SATISFIED`. QALD-9 Plus: CC BY 4.0 → elegible bajo política del lab para **T6A** (no autorizado). LC-QuAD authors: HOLD. Zenodo RDFConfig separado del GitHub pin. Modelos/servicios CONDITIONAL. Adapters false. Benchmark no elegible.

## 2. Gate de entrada
Prompt 19 gate `ADAPTER_CONTRACTS_DOCUMENTED_READY_FOR_LEGAL_ELIGIBILITY_RECHECK` · acción T5 · HEAD inicial `e209fb4044125516d04ee04d1638ad5b00d448c3`.

## 3. Alcance
Documental ZERO_COST. Metadata GET/HEAD allowlisted. Sin payloads, pesos, archives ZIP, SPARQL, inferencia, stubs, implementación.

## 4. No asesoramiento jurídico
Resultados = clasificación de política del laboratorio sobre evidencia publicada. Un archivo LICENSE no sustituye revisión jurídica profesional cuando proceda. Ver `LEGAL_SCOPE_AND_NON_ADVICE.md`.

## 5. Política del laboratorio
`audit/ZERO_COST_POLICY.md` · `MAX_EXTERNAL_MONETARY_COST_USD=0.00` · sin aceptación automatizada de términos.

## 6. Jerarquía de evidencia
LICENSE/COPYING/NOTICE en artefacto fijado > release metadata > package/model/dataset card > repo metadata > CITATION > README > paper > mirror > inferencia. Inferior no reemplaza superior.

## 7. Modelo por capas
L0–L9 documentado en `LEGAL_COMPONENT_LAYER_MODEL.md`.

## 8. G3 compuesto
Subgates G3C/D/G/M/A/S/O. Compuesto `SATISFIED` solo si todos los requeridos son SATISFIED_EVIDENCE o NOT_APPLICABLE. Ver `G3_COMPOSITE_GATE_SEMANTICS.md`.

## 9. Código SPARQL-LLM
Pin=`3748730…` · LICENSE.txt MIT · hash `ca796c5b…` · pin=HEAD · G3C SATISFIED_EVIDENCE · dependencias compuestas pendientes.

## 10. Código SGPT
Pin=`1f6964d1…` · LICENSE.md MIT · hash `66db862f…` · pin=HEAD · G3C SATISFIED_EVIDENCE · modelos/datasets pendientes.

## 11. Código mKGQAgent
Pin/HEAD sin LICENSE · G3C NOT_SATISFIED · inspección ≠ permiso de integración · implementation candidate=false.

## 12. RDFConfig GitHub/Zenodo/companion
GitHub generator: LICENSE absent → G3C NOT_SATISFIED. Companion dbcls/rdf-config MIT separado (no transferido). Zenodo DOI `10.5281/zenodo.18539214` metadata cc-by-4.0 · `ARCHIVE_CONTENT_EQUIVALENCE_NOT_VERIFIED` · candidato separado pendiente verificación de contenido · sin descarga.

## 13. Código CoT-SPARQL
LICENSE absent · G3C NOT_SATISFIED · blockers runtime/artifact adicionales.

## 14. Código FIRESPARQL
GitHub LICENSE absent · G3C NOT_SATISFIED · HF checkpoint card MIT separado · base Llama terms pending · missing native surfaces.

## 15. TeBaQA histórico
AGPL referencia histórica · `LAB_POLICY_HISTORICAL_ONLY` · no contract activo.

## 16. QALD-9 Plus
LICENSE CC BY 4.0 en pin `8eb038a6…` = HEAD · `LAB_POLICY_ACQUISITION_ELIGIBLE_AFTER_AUTHORIZATION` para QALD9_PLUS_EN_DBPEDIA · attribution manifest obligatorio · payload no adquirido.

## 17. LC-QuAD 2.0
Authors repo LICENSE absent → HOLD. HF `mohnish/lc_quad` card cc-by-3.0 = representación separada, no fuente primaria, no selección de adquisición en Prompt 20.

## 18. Grafos
Inventario endpoints/terms URL · sin inferir licencia de snapshot no identificado · `GRAPH_SNAPSHOT_ACQUISITION_PENDING` · G4 not satisfied · sin consultas SPARQL.

## 19. Modelos
Inventario GPT-2, e5-large, embeddings mKG, CodeLlama, MiniLM, REBEL, spaCy, providers · MODEL_CARD ≠ code license · TERMS_REVIEW_PENDING · sin descarga.

## 20. Checkpoints
FIRESPARQL HF card MIT inventariado · base-model dependency visible · no elimina términos base · sin descarga.

## 21. Artefactos auxiliares
Schema/VoID/Qdrant/FAISS/CoT parquet/rdf-config/prompts/oracle/FIRE results · lineage separado · índice derivado no hereda redistribución de librería MIT.

## 22. Servicios
OpenAI, OpenRouter, Groq, HF Hub, DBpedia, WDQS, ORKG, Falcon, Spotlight, Entity-Fishing, LangChain Hub, SIB · `SERVICE_TERMS_URL_VERIFIED_NOT_INTERPRETED` · paid → BLOCKED_POLICY under ZERO_COST.

## 23. Obligaciones
Attribution/notice matrix · CC BY attribution + indicate changes · MIT notice preservation · sin interpretar cláusulas ambiguas (UNKNOWN).

## 24. Attribution manifests
Templates `ATTRIBUTION_MANIFEST_TEMPLATE.yaml` y `ACQUISITION_LEGAL_MANIFEST_TEMPLATE.yaml` · authorization_id vacío · no auth.

## 25. Contracts
Matriz composite: SPARQL-LLM/SGPT G3C ok + composite conditional · resto G3C not · TeBaQA historical · common_adapter_allowed=false · G6I pending.

## 26. Acquisition eligibility
Elegible (lab policy): QALD9_PLUS_EN_DBPEDIA → T6A package only. Hold: LC-QuAD authors, graphs, models, FIRE checkpoint, CoT. Separate: Zenodo RDFConfig.

## 27. Riesgos
21 riesgos registrados (absent pin, mirror/source, archive/HEAD, base-model, terms drift, etc.).

## 28. G3
G3C satisfied solo SPARQL-LLM/SGPT (+ companion MIT separado; TeBaQA histórico). Composite CONDITIONAL o NOT_SATISFIED. No G3 compuesto SATISFIED para benchmark.

## 29. G4
`G4_RUNTIME_PIN_NOT_SATISFIED` (sin cambio).

## 30. G5
Documentary satisfied · runtime `G5_IMPLEMENTATION_AND_CONFORMANCE_PENDING`.

## 31. G6I
`G6I_IMPLEMENTATION_APPROVAL_PENDING` (sin cambio).

## 32. Adapters
`common_adapter_allowed=false` todos · G6D documented · sin implementación.

## 33. Benchmark
`NOT_CURRENTLY_ELIGIBLE`.

## 34. PE5–PE8
PE5: protocol_metric_adapter_and_legal_contracts_defined_pending_assets_implementation_and_benchmark  
PE6: diagnostic_metric_observability_and_legal_boundaries_defined_pending_execution  
PE7/PE8: not_started · evidencia preparatoria legal; no experimental.

## 35. Gate
`LEGAL_RECHECK_COMPLETE_PARTIAL_SCOPE_READY_FOR_ACQUISITION_AUTHORIZATION_PACKAGE`  
Qualifiers en `LEGAL_ELIGIBILITY_GATE.md`. **No** significa acquisition authorized / implementation allowed / terms accepted / G4–G6I ready / adapter or benchmark ready.

## 36. Siguiente acción
**T6A / Prompt 21A** — paquete documental de autorización QALD-9 Plus EN/DBpedia CC BY 4.0, ZERO_COST, sin descargar. No ejecutado aquí.

## 37. Objetivo de largo plazo
reproducción nativa → evaluación común → caso de estudio → errores → Text-to-SQL → método nuevo → ablaciones. Intacta.

## 38. Conclusión conservadora
Prompt 20 cierra T5 documental con scope parcial listo para **paquete de autorización** (no para descarga). Métodos sin licencia bloqueados. Separaciones source/archive/mirror/model-card respetadas. Coste 0. Upstream intacto.
