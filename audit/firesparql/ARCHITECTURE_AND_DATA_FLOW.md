# ARCHITECTURE_AND_DATA_FLOW — firesparql

**Fecha:** 2026-07-20  
**pinned_commit:** `48d6f168e4c1dd3dc467553aef370299911d4e76` (`PIN`)

---

## Resumen arquitectónico

FIRESPARQL es un **pipeline multi-etapa** SciQA/ORKG: (opcional) preparación one-shot o RAG → generación causal LLaMA (vanilla / one-shot / FT / RAG) → **limpieza LLM (gpt-4o)** → ejecución SPARQL (**runner ausente en repo**) → métricas BLEU/ROUGE + exact match de **conjuntos de resultados** + acumulación multi-round (“RelaxedEM”).

El **fine-tuning LoRA** ocurre **fuera** de este repositorio (evidencia LLaMa-Factory); aquí solo hay datos instruction-format + scripts de inferencia sobre `merge_models/` o HF.

---

## Diagrama Mermaid

```mermaid
flowchart TB
  subgraph data [Datos en repo]
    TQ[sciqa test_questions 513]
    TR[sciqa train 1795]
    FTJ[sciqa_training_data4ft.json]
    PROP[orkg-property.json 9062]
    MS[most_similar_questions.csv]
  end

  subgraph external [Externos / ausentes]
    LMF[LLaMa-Factory training NOT_IN_REPO]
    MM[merge_models ABSENT]
    HF[HF Sherry791 ft4sciqa]
    GROQ[Groq deepseek-r1]
    OAI[OpenAI gpt-4o]
    EP[ORKG endpoint CODE_NOT_FOUND runner]
  end

  TR --> MS
  TR --> FTJ
  FTJ -.-> LMF
  LMF -.-> MM
  LMF -.-> HF

  TQ --> ZS[generate_sparql_cuda/mps ZERO_SHOT]
  MS --> OS[generate_sparql_one_shot_cuda]
  MM --> FT[generate_* FINE_TUNED]
  HF --> FT
  PROP --> RAGCTX[generate_context_rag]
  GROQ --> RAGCTX
  RAGCTX --> RAGG[generate_sparql_rag_*]
  TQ --> RAGG

  ZS --> S1[step1_generated_text]
  OS --> S1
  FT --> S1
  RAGG --> S1

  S1 --> CLN[sparql-cleaning-llm gpt-4o]
  OAI --> CLN
  CLN --> S2[step2_clean_sparql]

  S2 --> EP
  EP --> S3[step3_*_against_orkg summaries]
  S3 --> EM[exact_match.py]
  EM --> S4[step4 success_ids]
  S4 --> ACC[accumulate_exact_match union]
  S2 --> BR[bleu_rouge.py vs gold query]
```

---

## Flujo por familia experimental

| Familia | Entrada modelo | Prompt | Contexto extra |
|---|---|---|---|
| `vanilla` | base Instruct | ORKG zero-shot hardcoded | no |
| `one_shot` | base Instruct | ejemplo gold `train_query` | `most_similar_questions.csv` |
| `ft` | merged LoRA / HF ft | mismo zero-shot ORKG | no |
| `vanilla_rag` / `ft_rag` | base o ft | prompt2 + contexto RAG | `context_from_rag/` |

---

## Observables I/O

- **Entrada NL:** CSV `id,question,query` (test).  
- **Salida step1:** `{id}.txt` con Question + Generated SPARQL.  
- **Salida step2:** SPARQL “cleaned”.  
- **Salida step3:** `sparql_summary.csv` (siempre casi); `sparql_results.csv` **parcial** (23 configs).  
- **Salida step4:** listas de IDs con EM=1.  

Detalle matrices: `PIPELINE_COMPONENT_MATRIX.csv`, `MODEL_CONFIGURATION_MATRIX.csv`.
