# METRIC_PREFLIGHT_BOUNDARY — SGPT

**Fuente:** `utils/metrics.py`, `eval.py`, `audit/sgpt/METRICS_AUDIT.md`

## Implementadas (léxicas)

BLEU; SP-BLEU; unigram P/R; SP P/R; diversity; METEOR; ROUGE; F1/SP-F1 **impresos**.

## Ausentes

- Answer F1  
- Ejecución SPARQL  

## Anomalías (`CODE_VERIFIED`)

- Double `metric.update` por ejemplo  
- F1/SP-F1 no persistidos en `result`  
- Riesgo división por cero si P+R=0  
- Clases BLEU/SPBLEU idénticas  
- Test unitario de métricas ≠ evaluación del modelo end-to-end  

## Z2

Solo fixtures sintéticos. **No** recalcular resultados del paper / Table 4.
