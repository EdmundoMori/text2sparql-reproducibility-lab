# QALD9PLUS_TEST_SEAL_PLAN

**RUN_ID:** `20260722T105246Z` · Status: `TEST_SEAL_PLAN_DEFINED` · seal: **not sealed** (payload NOT_ACQUIRED)

## Objetivo
Sellar el test DBpedia tras T6B para prevenir leakage.

## Permitido en T6B
tamaño · Git blob OID · SHA-256 · JSON parse · conteo registros · inventario de nombres de campos · cobertura EN sin imprimir contenido.

## Prohibido en T6B
imprimir preguntas/SPARQL · ejemplos · prompts · hiperparámetros · few-shot · split dev · consultas · uso en adapter.

Template: `configs/common/acquisition/qald9plus/QALD9PLUS_TEST_SEAL_MANIFEST_TEMPLATE.yaml`
