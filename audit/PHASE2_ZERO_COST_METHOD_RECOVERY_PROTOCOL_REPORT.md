# PHASE2 — ZERO_COST method recovery protocol (Prompt 25R2)

**RUN_ID:** `20261012T125143Z` · **Protocol:** `1.0.0-25R2` · **Gate:** `ZERO_COST_METHOD_RECOVERY_PROTOCOL_DEFINED_READY_FOR_FAIR_COMPARISON_CONTRACT` · **Cost:** 0.00

## 1. Executive summary

Defines a reusable, effort-parity recovery protocol converting 25R1 blocker maps into evidence-gated recovery dimensions, RG0–RG9, state machine, controlled-variant rules, and prioritized future recovery prompts — **without executing any recovery**.

## 2–4. Input / scope / out of scope

Input gate: `GLOBAL_BLOCKER_RECOVERY_AND_ZERO_COST_RECONCILIATION_COMPLETE_READY_FOR_METHOD_RECOVERY_PROTOCOL`.  
In: protocol/contracts/matrices/cards. Out: execution, training, weights, SPARQL, deploy, adapters, author contact, profile selection.

## 5–15. Policies

ZERO_COST preserved. Recovery dimensions A–D separated. RG0–RG9 locked. State machine locked. Terminal/reopen/effort parity/evidence hierarchy/controlled variants/model-backend replacement/external compute policies defined under `docs/protocols/common/recovery-protocol/20261012T125143Z/` and `configs/common/recovery-protocol/`.

## 16–22. Methods

| Method | Priority tier | Native | ZERO_COST | Controlled |
|---|---|---|---|---|
| sparql_llm | TIER_A | API cost-blocked | local-backend candidate | YES |
| sgpt | TIER_A | ckpt blocked | retrain conditional | resource-equiv |
| rdfconfig_llm | TIER_B | legal/artifact pending | conditional | after Zenodo equiv |
| mkgqagent | TIER_B | LEGAL_BLOCKED | documentary | after LICENSE |
| cot_sparql | TIER_C | documentary pending | documentary | not invented |
| firesparql | TIER_D | domain pending | documentary | not for QALD (R7) |
| tebaqa | TIER_E | HISTORICAL_ONLY | HISTORICAL | optional later |

## 23–28. Priority / DAG / catalog / claims / portfolio

See priority matrix, dependency DAG, future prompt catalog (`RESERVED_NOT_EXECUTED`), claim policy, minimum common portfolio (participants not frozen).

## 29. Fair-comparison handoff

`FAIR_COMPARISON_HANDOFF.md` prepared for 25R3.

## 30–36. Positions

QALD primary · DBpedia target · LC-QuAD HOLD · deploy deferred · G4 NOT_SATISFIED · G5 pending · G6D documented · G6I pending · adapters false · benchmark NOT_CURRENTLY_ELIGIBLE.

## 37–40. Roadmap / next / long-term / conclusion

25R2 COMPLETE · next **Prompt_25R3**. Protocol ≠ recovery demonstrated.
