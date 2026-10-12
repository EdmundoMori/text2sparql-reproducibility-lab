# Training and adaptation fairness contract

**RUN_ID:** `20261012T130607Z`
**Protocol:** `1.0.0-25R3`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_EXECUTION


Regimes: `AR_ZERO_SHOT`, `AR_FEW_SHOT_TRAIN_ONLY`, `AR_SUPERVISED_TRAIN_SPLIT`, `AR_ORACLE_INPUT`,
`AR_DOMAIN_RETRAINED`, `AR_RESOURCE_EQUIVALENT_RETRAIN`, `AR_OTHER_DECLARED`.

Test data is forbidden for training, tuning, validation, demonstration selection and nearest-example
construction. Demonstrations must come from declared train-only data. External corpora, counts, splits and
licenses must be reported. Different regimes may enter L2 when task/test/graph/track/evaluator are common,
but causal claims require stricter L3 controls. Physical batch may change only with compensating gradient
accumulation that preserves effective batch; other deviations get an adaptation flag.
