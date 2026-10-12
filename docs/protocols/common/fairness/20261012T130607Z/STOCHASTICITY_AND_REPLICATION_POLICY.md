# Stochasticity and replication policy

**RUN_ID:** `20261012T130607Z`
**Protocol:** `1.0.0-25R3`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_EXECUTION


One frozen execution may suffice for deterministic methods. Stochastic inference fixes seeds when supported.
Stochastic training should use three seeds when computationally feasible under ZERO_COST. If repetitions are
not feasible, classify `SINGLE_RUN_RESOURCE_LIMITED` and prohibit variance, significance or stability claims
requiring replication. No seeds are run in Prompt 25R3.
