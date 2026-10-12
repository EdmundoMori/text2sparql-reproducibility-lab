# Fair comparison handoff (→ Prompt 25R3)

**RUN_ID:** `20261012T125143Z`

| Method | Variants | Changed components (prospective) | Info access | Train | Schema | Oracle | Services | Model regime | Direct-compare risk |
|---|---|---|---|---|---|---|---|---|---|
| sparql_llm | NATIVE_API / ZERO_COST_LOCAL_BACKEND | backend only | IA_SCHEMA_COMMON | no | yes | no | API→local | external→local_open | MEDIUM |
| sgpt | PAPER_CKPT / RETRAIN | batch/accum only if equiv | IA_Q_ONLY | yes | no | no | n/a | local_train | LOW |
| mkgqagent | NATIVE / CONTROLLED_LOCAL | backend+endpoint+freeze prompts | IA_SCHEMA_COMMON | no | yes | no | OpenAI/Falcon/hub | local after LICENSE | HIGH |
| rdfconfig_llm | NATIVE / LOCAL | backend; schema adapt later | IA_SCHEMA_COMMON | no | yes | no | OpenAI | local after legal | MEDIUM |
| cot_sparql | NATIVE_34B | none invented | IA_ORACLE_GROUNDING | no | no | yes | linkers | 34B | HIGH |
| firesparql | DOMAIN_NATIVE | must not force QALD | IA_DOMAIN_NATIVE | yes | yes | no | QLever | FT | CRITICAL (R7) |
| tebaqa | HISTORICAL | optional later | IA_HISTORICAL | no | yes | no | legacy | n/a | HIGH |

No final fairness decision in 25R2. Provisional tracks preserved from 25R1.
