# DEPENDENCY_RESOLUTION_PLAN — SGPT

**Prompt:** 12 — plan documental; **sin** instalación ahora.

---

## A. HECHOS FIJADOS

| Hecho | Valor | Evidencia |
|---|---|---|
| Python declarado | 3.8 | README_REPORTED |
| torch | 1.13.1 | CODE_VERIFIED |
| Repo + pin | `1f6964d1…` | REPOSITORIES.lock |
| Datasets en repo | lcquad2 / qald9 / vquanda | DATA_VERIFIED |
| Licencia | MIT | LEGAL_VERIFIED |

## B. DEPENDENCIAS SIN PIN

transformers; spaCy; en_core_web_sm / lg; NLTK (+ data); numpy; tqdm; tensorboardX; python-Levenshtein; unidecode; optuna-dashboard; Apex (opcional); GPT-2 HF; CUDA wheel; NCCL.

## C. REGLA PARA FIJARLAS EN EL FUTURO (Prompt 12B+)

1. Metadata oficial (PyPI / HF) — fechas coherentes con torch 1.13.1 / Py3.8.  
2. Conservar símbolos de `IMPORT_COMPATIBILITY_REQUIREMENTS.csv`.  
3. Prueba de importación autorizada.  
4. `pip check` + freeze final.  
5. **Nunca** modificar upstream para adaptar el entorno.  
6. No inventar pins en Prompt 12.

## D. STOP CONDITIONS

- Conflicto irresoluble sin tocar upstream.  
- Wheel ausente para Py3.8/torch.  
- Dependencia retirada.  
- Descarga no autorizada.  
- API de pago.  
- Install que exceda recursos.  
- Intento de declarar reproducción / Table 4.
