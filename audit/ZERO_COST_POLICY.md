# ZERO_COST_POLICY — Definición operativa

**Fecha:** 2026-07-21  
**Prompt:** 11C  
**Decisión humana:** [`HUMAN_ZERO_COST_DECISION.md`](../docs/protocols/sparql_llm/model-budget-gates/20260721T100618Z/HUMAN_ZERO_COST_DECISION.md)  
**MAX_EXTERNAL_MONETARY_COST_USD:** **0.00**

“Coste cero” = **cero gasto monetario externo autorizado**.  
No implica consumo energético cero ni ausencia de uso de hardware local.

---

## A. PROHIBIDO

- APIs de pago  
- Claves con saldo o facturación  
- Cloud GPU/CPU de pago  
- Suscripciones  
- Pruebas “gratuitas” que requieran método de pago  
- Modelos “free” en OpenRouter como sustitución no fijada  
- Costes asumidos sin autorización explícita del investigador  
- OpenAI / hosted LLMs de pago  
- POST `/chat` sparql_llm bajo presupuesto > 0 no autorizado  

## B. PERMITIDO EN PRINCIPIO (no en Prompt 11C)

Prompt 11C es **solo documental**: no instala, no descarga, no ejecuta.

En prompts futuros, sujeto a gates adicionales:

- CPU/RAM/GPU ya disponibles localmente  
- Docker local  
- Software open source  
- Metadata pública  
- Descargas gratuitas (con autorización explícita cuando el lab lo exija)  
- Modelos públicos gratuitos (p. ej. GPT-2 base) si el gate lo permite  
- Endpoints públicos sin coste monetario  
- Ejecución offline  

## Gates adicionales obligatorios (futuro)

Cualquier uso de la sección B debe pasar además:

1. gate legal;  
2. gate científico;  
3. gate de recursos;  
4. gate de red;  
5. autorización de descarga cuando corresponda.

## No interpretaciones incorrectas

| Incorrecto | Correcto |
|---|---|
| API “free” = reproducibilidad estable | NOT_SELECTED / mutabilidad |
| LLM local = método OpenRouter | SUBSTITUTION_NOT_NATIVE |
| Results versionados = ejecución propia | RESULT_FILE_VERIFIED ≠ EXECUTION_VERIFIED |
| Reduced train = Table 4 | reduced_smoke_only |
| smoke_only = PE3 | no |
| LICENSE_NOT_CONFIRMED = permiso | blocked / HOLD_LEGAL |
