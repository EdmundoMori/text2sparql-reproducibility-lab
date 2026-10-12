# mKGQAgent recovery assessment

**phase1:** blocked · LICENSE ABSENT at pin and current HEAD (GH license API 404 reconfirmed 25R1).

## Static

- ChatOpenAI + base_url hits exist → local OpenAI-compatible backend **possible in principle**
- LangChain Hub + Falcon + hardcoded DBpedia endpoint dependencies
- Experience pool offline build script absent historically

## Variants

| Variant | Status |
|---|---|
| MKGQAGENT_NATIVE_API_VARIANT | blocked B_LEGAL + B_COST |
| MKGQAGENT_ZERO_COST_CONTROLLED_VARIANT | **conditional candidate** only **after** public LICENSE; would replace API+endpoint with local LLM + local DBpedia + frozen prompts |

## Recoverability

- native: **R4** (license) then R3
- common_benchmark: **R4** then R3
- adapter eligibility remains **false** while LICENSE absent
- Blockers: B_LEGAL (primary), B_COST, B_SERVICE, B_ARTIFACT, B_GRAPH, B_REPRODUCIBILITY
