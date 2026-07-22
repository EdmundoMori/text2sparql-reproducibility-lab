# STATISTICAL_ANALYSIS_CONTRACT

**Status:** `STATISTICAL_CONTRACT_DEFINED`

Comparisons only within: same dataset view · graph · track · compatible adaptation · model-control · evaluable set.

## A. Per-method intervals
Answer F1 macro: paired/item bootstrap CI 95%. Exact / validity rates: Wilson CI 95%. Latency: median/percentile bootstrap when applicable.

## B. Paired
Answer F1: paired bootstrap of difference. Binary: exact McNemar. Effect size: mean paired difference, risk difference, matched OR when defined.

## C. Multiple comparisons
Holm correction; family = dataset × track × model-control × metric family.

## D. Stochastic runs
≥3 seeds: distribution + mean-per-seed + two-stage bootstrap (or documented equivalent). Single stochastic run: `SINGLE_STOCHASTIC_RUN_VARIANCE_NOT_ESTIMATED`.

## E. Restrictions
No cross-track tests; no superiority by point estimate alone; report N and discordant pairs; corrected+uncorrected p; significance ≠ practical effect; no unregistered post-hoc as confirmatory.
