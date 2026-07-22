# REPLICATE_AND_SEED_CONTRACT

- Deterministic config: one canonical run + repeatability check when viable.
- Stochastic: ≥3 full runs if cost/auth allow.
- Seeds preregistered before test; never best-seed; never drop failed seed; same evaluable set; report all runs.
- Provider without seed: `NONDETERMINISTIC_UNCONTROLLED_PROVIDER`.

## Statistical (not method) seeds
- `bootstrap_seed`: 2026072201
- `bootstrap_replicates`: 10000

Method seeds: deferred to adapter/config contracts.
