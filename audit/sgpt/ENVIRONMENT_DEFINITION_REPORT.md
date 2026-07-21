# ENVIRONMENT_DEFINITION_REPORT — SGPT Prompt 12

**Fecha:** 2026-07-21  
**Pin:** `1f6964d1c3bfee50c7dec2c25546f32b4ab94b2b`  
**Licencia:** MIT  
**SHA inicial:** `d7b199c9caf8035e88eedf717ab7926dcc2d7a11`  
**Coste externo:** **0.00**  
**Install/download/train/infer:** **0**

---

## 1. Objetivo

Definir documentalmente un entorno SGPT trazable para decidir un futuro preflight Z2 gratuito.

## 2. Alcance

Solo documentación + AST. Sin pip/Docker/imports runtime.

## 3. Política coste cero

`MAX_EXTERNAL_MONETARY_COST_USD=0.00`; OpenRouter/POST `/chat` NO-GO.

## 4. Identificación del método

`sgpt` — generative GPT-2 SPARQL; `audit_only`; checkpoints ausentes.

## 5. Entorno declarado

Python 3.8; torch 1.13.1; transformers unpinned; Conda README; epochs 40 README vs 70 params.json.

## 6. Inventario de dependencias

AST: 13 `.py`, 152 filas import; third-party tops: apex, nltk, numpy, spacy, tensorboardX, torch, tqdm, transformers.  
requirements: 8 pkgs; implícitos numpy/tqdm; declared-unused: Levenshtein, unidecode, optuna-dashboard.

## 7. Dependencias implícitas

numpy, tqdm, Apex (condicional), spaCy models, GPT-2, CUDA/NCCL, TensorBoard path.

## 8. Compatibilidad

Símbolos Transformers listados; pins = **UNKNOWN** (no inventados).

## 9. Perfiles

A NATIVE_DECLARED; B Z2 CPU; C Z3 reduced (blocked).

## 10. Datos

Contrato + split drift LC-QuAD2 5969 vs ~6046; QALD9 ID reuse.

## 11. Modelos

GPT-2 base = pretrained público; no descargado.

## 12. Checkpoints

SGPT trained **NOT_FOUND**; runs/outputs **NOT_FOUND**.

## 13. Métricas

Léxicas only; anomalías double-update / F1 no persistido / div0.

## 14. Escrituras

Solo workdir/logs lab; upstream read-only.

## 15. Red y descargas

Prompt 12: ninguna. Futuras requieren autorización.

## 16. Recursos

WSL 7.4 GiB RAM; 6 GiB VRAM; paper 2×12 GB.

## 17. Riesgos

Drift transformers; spaCy sm vs lg; OOM Z3; confusión GPT-2≠checkpoint.

## 18. Z2

Especificado; no ejecutado.

## 19. Z3

Blocked pending Z2 + download auth.

## 20. Table 4

**not_ready** — no afirmar.

## 21. Readiness

Matriz CSV; gate condicional.

## 22. Gate

**`CONDITIONAL_DEPENDENCY_RESOLUTION`**

## 23. Siguiente acción

Prompt **12B** — pins documentales vía metadata oficial, sin install.

## 24. PE1–PE4

PE1 ok; PE2 partial (env doc); PE3 not_started; PE4 barriers refined.

## 25. Conclusión

Entorno **documentado, no resuelto**. Coste 0. SGPT sigue `audit_only`. No train/Table 4.


---

## Prompt 13A/13B closure (añadido; no reescribe auditoría histórica)

- **Z1:** `COMPLETE_DOCUMENTED`
- **Z2:** `COMPLETE_Z2_CORE_PREFLIGHT` (`RUN_ID=20260721T114919Z`)
- Autorización 13A: `AUTHORIZED_AND_CONSUMED_13A`
- Freeze SHA-256: `916d4b76a980ed1b558eb3bb26122f5e6dca9e02ffaeb5ee8e553f7cd66e71a5`
- Matriz evidencia: `audit/sgpt/Z2_EVIDENCE_MATRIX.csv`
- Cierre: `audit/sgpt/ZERO_COST_Z1_Z2_CLOSURE.md`
- Informe 13B: `audit/sgpt/Z2_CLOSURE_AND_POST_Z2_REGATE_REPORT.md`
- Gate: `Z2_ENV_READY_PREFLIGHT_PASS`
- Siguiente: Prompt **14A** (protocolo Z3 documental; sin GPT-2; sin train)
- Conservado: `audit_only`; `native_audit_complete=false`; `common_adapter_allowed=false`; PE3 `not_started`
