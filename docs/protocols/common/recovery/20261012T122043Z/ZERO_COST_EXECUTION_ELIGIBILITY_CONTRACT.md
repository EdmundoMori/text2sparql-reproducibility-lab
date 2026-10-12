# ZERO_COST execution eligibility contract

**Policy:** `ZERO_EXTERNAL_MONETARY_COST` · MAX_EXTERNAL_MONETARY_COST_USD = **0.00**

Config: `configs/common/recovery/ZERO_COST_EXECUTION_GATE.yaml`

## Subgates ZC1–ZC8 (mandatory)

ZC1 LICENSE · ZC2 MODEL_WEIGHTS · ZC3 DATASET · ZC4 RUNTIME · ZC5 LLM_BACKEND ·
ZC6 ENDPOINT_AND_EXTERNAL_SERVICES · ZC7 COMPUTE · ZC8 NO_PAID_SERVICE

`ZERO_COST_EXECUTION_ELIGIBLE` iff ZC1–ZC8 are SATISFIED or NOT_APPLICABLE.

Commercial free tiers ≠ SATISFIED automáticamente.
Free trials / promotional credits ≠ SATISFIED.
