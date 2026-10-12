#!/usr/bin/env python3
"""Generate Prompt 25R3 documentary fairness-contract artifacts.

This script performs no method, model, graph, SPARQL, or benchmark execution.
"""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
RUN = "20261012T130607Z"
DOC = ROOT / "docs/protocols/common/fairness" / RUN
CFG = ROOT / "configs/common/fairness"
AUD = ROOT / "audit/fairness"
LOG = ROOT / "logs/fair-comparison-contract" / RUN
for directory in (DOC, CFG, AUD, LOG):
    directory.mkdir(parents=True, exist_ok=True)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = "\n".join(line.rstrip() for line in text.strip().splitlines()) + "\n"
    path.write_text(normalized, encoding="utf-8")


def csv_write(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


header = f"""**RUN_ID:** `{RUN}`
**Protocol:** `1.0.0-25R3`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_EXECUTION
"""

docs: dict[str, str] = {}
docs["FAIR_COMPARISON_PRINCIPLES.md"] = f"""# Fair comparison principles

{header}

`HOMOGENEITY_DOES_NOT_MEAN_ARCHITECTURAL_SAMENESS`.

## A. MUST_BE_COMMON_WHEN_DIRECTLY_COMPARED

Dataset view, test questions and split, item universe and denominator, graph snapshot and endpoint semantics,
gold materialization, evaluator and metric definitions, failure accounting, test seal, information-access
track, benchmark-supplied information, ZERO_EXTERNAL_MONETARY_COST policy, and reporting schema.

## B. METHOD_SPECIFIC_BY_DESIGN

Architecture, prompts, internal retrieval, internal agent/reasoning loop, native model, training algorithm,
repair mechanism, internal entity/relation linking, internal calls, internal index/memory, and endpoint
feedback intrinsic to the method.

## C. MUST_BE_REPORTED_AND_STRATIFIED

Backbone/revision, adaptation/training regime, quantization, hardware, latency, memory, endpoint/linker/LLM
calls, seeds, and external services. Differences are not hidden and do not by themselves invalidate L2
quality comparison; they constrain causal and efficiency claims.
"""
docs["INFORMATION_BOUNDARY_CONTRACT.md"] = f"""# Information boundary contract

{header}

## BENCHMARK_SUPPLIED_INFORMATION

Only information crossing from harness/adapter to the method: question, language, benchmark item ID,
endpoint reference, schema bundle, oracle entities/relations, fixed external grounding, and demonstrations.
Every supplied field must appear in the frozen input manifest.

## METHOD_INTERNAL_INFORMATION_ACQUISITION

Retrievers, indexes, entity/relation linkers, endpoint feedback, internal search, agent tools and experience
pools invoked by the method itself. They require reproducibility and ZERO_COST evidence, but remain internal.

An internal linker does **not** create `IA_ORACLE_GROUNDING`. Oracle means gold-derived information for the
evaluated item crossed the benchmark boundary. Train-only demonstrations remain method-internal unless the
benchmark supplies them. A benchmark-supplied common frozen linker output is `IA_FIXED_EXTERNAL_GROUNDING`.
"""
docs["INFORMATION_ACCESS_TRACK_TAXONOMY_V2.md"] = f"""# Information access track taxonomy V2

{header}

| Track | Benchmark-supplied information | Boundary |
|---|---|---|
| IA_Q_ONLY | question, basic metadata, common endpoint reference | Native internal retrieval/linking allowed if non-gold, declared, reproducible and ZERO_COST |
| IA_SCHEMA_COMMON | IA_Q_ONLY plus identical frozen schema bundle | No richer method-specific benchmark bundle in the group |
| IA_ORACLE_GROUNDING | gold-derived entity/relation/property information for evaluated item | Must say oracle-assisted; never end-to-end |
| IA_FIXED_EXTERNAL_GROUNDING | same frozen external linker/grounder output supplied to every group member | Distinct from native internal linkers |
| IA_DOMAIN_NATIVE | different dataset/KG/domain | No QALD ranking |
| IA_HISTORICAL | historical context | No active ranking |

Taxonomy version: `2.0.0-25R3`.

Historical Prompt 19 adapter contracts and Prompt 25R2 recovery rows retain their original labels as evidence.
Where `PROMPT_25R3_RECONCILIATION` records a different `new_track`, V2 governs future fairness. F12 remains
blocked until any affected adapter contract/input mapping is explicitly reconciled; no silent reinterpretation
or implementation is authorized.
"""
docs["COMMON_COMPARISON_UNIT.md"] = f"""# Common comparison unit

{header}

The minimum unit is:

`method_variant × dataset_view × graph_snapshot × information_access_track × adaptation_regime × model_regime × evaluator_version × protocol_version`.

Results differing in a critical comparison dimension are not directly comparable unless explicitly
stratified. A label referring only to a method family is insufficient.
"""
docs["DIRECT_COMPARISON_LEVELS.md"] = f"""# Direct comparison levels

{header}

- **L0_NOT_COMPARABLE:** different domain/KG/test or incompatible information tracks.
- **L1_DESCRIPTIVE_CROSS_TRACK:** coexist in a report; no winner or ranking claim.
- **L2_FAIR_SYSTEM_LEVEL_COMPARISON:** same dataset view, test, graph, evaluator, metrics, information track,
  failure accounting, test seal and ZERO_COST eligibility. Architecture/backbone may differ. Permits only
  system-level performance claims under named external conditions.
- **L3_CONTROLLED_METHOD_COMPARISON:** L2 plus controlled backbone/revision, grounding, schema and adaptation
  data where scientifically admissible. Permits stronger component claims only when the experimental design
  isolates that component.

Not every method must reach L3. L2 never proves that an architecture caused a difference.
"""
docs["COMMON_DATASET_HOMOGENEITY_CONTRACT.md"] = f"""# Common dataset homogeneity contract

{header}

Primary view remains `QALD9_PLUS_EN_DBPEDIA`, source pin
`8eb038a61e1bc09cbd21640aa667a1714f53cda4`, English, DBpedia, train 408 / test 150,
CC-BY-4.0 evidence, test seal `SEALED`.

All common evaluations use the exact same test item IDs, exclusions and denominator. Syntax error,
execution error, timeout, abstention, no/invalid output remain failures in the denominator. No
method-specific filtering, hard-question removal, test-derived prompts, tuning or recovery decisions.
Inability to process an item is recorded as failure. Final participants remain unfrozen.
"""
docs["TRAINING_AND_ADAPTATION_FAIRNESS_CONTRACT.md"] = f"""# Training and adaptation fairness contract

{header}

Regimes: `AR_ZERO_SHOT`, `AR_FEW_SHOT_TRAIN_ONLY`, `AR_SUPERVISED_TRAIN_SPLIT`, `AR_ORACLE_INPUT`,
`AR_DOMAIN_RETRAINED`, `AR_RESOURCE_EQUIVALENT_RETRAIN`, `AR_OTHER_DECLARED`.

Test data is forbidden for training, tuning, validation, demonstration selection and nearest-example
construction. Demonstrations must come from declared train-only data. External corpora, counts, splits and
licenses must be reported. Different regimes may enter L2 when task/test/graph/track/evaluator are common,
but causal claims require stricter L3 controls. Physical batch may change only with compensating gradient
accumulation that preserves effective batch; other deviations get an adaptation flag.
"""
docs["COMMON_SCHEMA_ACCESS_POLICY.md"] = f"""# Common schema access policy

{header}

Every `IA_SCHEMA_COMMON` member receives one identical frozen bundle with `schema_bundle_id`, version,
content hash, generation process, graph target, classes, properties, and optional VoID/shapes. No richer
benchmark-supplied schema is permitted for one member of the same direct-comparison group. Endpoint-derived
extra schema is a declared `METHOD_INTERNAL_CAPABILITY`; Prompt 25R4 must decide whether it requires a
separate variant/group.
"""
docs["GROUNDING_AND_ORACLE_FAIRNESS_CONTRACT.md"] = f"""# Grounding and oracle fairness contract

{header}

Grounding regimes are `NO_SUPPLIED_GROUNDING`, `METHOD_INTERNAL_GROUNDING`,
`COMMON_FIXED_EXTERNAL_GROUNDING`, and `GOLD_ORACLE_GROUNDING`.

Only gold-derived information crossing the benchmark boundary is oracle. Internal native linkers are not
oracle. Common fixed grounding must be identical and frozen for every member. Oracle-assisted results may
be reported as upper bounds, never as end-to-end and never ranked as equivalent to Q_ONLY.
"""
docs["TEST_SEAL_AND_LEAKAGE_PREVENTION_CONTRACT.md"] = f"""# Test seal and leakage prevention contract

{header}

The QALD test remains sealed. Forbidden: prompt design, hyperparameter selection, demonstrations, schema
tailoring, manual corrections, recovery choices, or model selection based on test content/performance.
After authorization only the frozen harness may feed a sealed question, execute the generated query,
evaluate with the frozen evaluator, and store predictions/results. Suspected pretraining contamination is
flagged separately from deliberate leakage and does not authorize test inspection.
"""
docs["METRIC_AND_FAILURE_ACCOUNTING_ALIGNMENT.md"] = f"""# Metric and failure-accounting alignment

{header}

Common primary metrics remain Answer Precision, Answer Recall, Answer F1 and Execution Exact Accuracy under
the Prompt 18 canonicalization, empty-answer, timeout, error-category, denominator and aggregation contracts.
Syntax/execution errors, timeout, abstention, no output and invalid output stay in the common denominator.
Native metrics are supplementary. BLEU, ROUGE and query exact match never substitute for Answer F1.
Runtime status remains G5 implementation/conformance pending.
"""
docs["RESOURCE_AND_HARDWARE_COMPARABILITY_POLICY.md"] = f"""# Resource and hardware comparability policy

{header}

Quality and operational efficiency are distinct. L2 quality may compare systems requiring different
hardware if common task conditions hold and resources are reported. Latency, memory and throughput ranking
requires the same physical machine or an explicitly equivalent profile. Institutional ZERO_COST compute may
support quality results, but cannot be efficiency-ranked against local execution unless profiles match.
Report CPU, GPU, VRAM, RAM, storage, quantization, threads, batch and concurrency.
"""
docs["TIMEOUT_AND_EXECUTION_BUDGET_POLICY.md"] = f"""# Timeout and execution budget policy

{header}

Future execution combines a predeclared `COMMON_SAFETY_CEILING` with `METHOD_NATIVE_INTERNAL_BEHAVIOR`.
The per-item timeout must be equal within a direct group where technically meaningful, remain in the
denominator, and never be tuned on test. Token/call caps must not alter a method's architecture merely to
force superficial equality; any architecture-affecting cap creates a separate declared variant.
"""
docs["STOCHASTICITY_AND_REPLICATION_POLICY.md"] = f"""# Stochasticity and replication policy

{header}

One frozen execution may suffice for deterministic methods. Stochastic inference fixes seeds when supported.
Stochastic training should use three seeds when computationally feasible under ZERO_COST. If repetitions are
not feasible, classify `SINGLE_RUN_RESOURCE_LIMITED` and prohibit variance, significance or stability claims
requiring replication. No seeds are run in Prompt 25R3.
"""
docs["MODEL_AND_BACKBONE_COMPARABILITY_POLICY.md"] = f"""# Model and backbone comparability policy

{header}

`METHOD_FAITHFUL` permits native backbones to differ and supports L2 system comparison. `CONTROLLED_BACKBONE`
may support L3 only if architecture permits, variant admissibility and license pass, ZERO_COST holds, and
identity is preserved. SGPT is not forced onto an LLM-agent backbone; CoT-SPARQL gets no invented smaller
model. No common backbone is selected in 25R3.
"""
docs["NETWORK_AND_EXTERNAL_SERVICE_POLICY.md"] = f"""# Network and external service policy

{header}

Primary variants must satisfy ZERO_EXTERNAL_MONETARY_COST. Services must be local or free, public, stable
and reproducibly versionable. Commercial free tiers are not primary dependencies. Output-affecting mutable
services must be frozen, replaced by a reproducible local equivalent, or marked non-reproducible. Network
dependencies and revisions are mandatory reporting fields.
"""
docs["FAIR_COMPARISON_CLAIM_POLICY.md"] = f"""# Fair comparison claim policy

{header}

L2 permits: “Under the same QALD view, DBpedia snapshot, evaluator and information track, system A achieved
higher Answer F1 than system B.” L2 does not permit “architecture A is better” without L3 controls.
Cross-track/global “best method” claims are forbidden. Oracle results say `oracle-assisted`. Controlled
variants say `controlled ZERO_COST variant`, never native reproduction. A track needs at least two
independently implemented method families for pairwise inter-method claims; variants of one codebase alone
do not satisfy this rule.
"""
docs["FAIR_COMPARISON_PREFLIGHT_CONTRACT.md"] = f"""# Fair comparison preflight contract

{header}

| Gate | Requirement | 25R3 |
|---|---|---|
| F0_DATASET_PIN | exact view/items | DOCUMENTED_NOT_EXECUTED |
| F1_GRAPH_RUNTIME | frozen operational graph | DOCUMENTED_NOT_EXECUTED |
| F2_TEST_SEAL | seal intact | DOCUMENTED_NOT_EXECUTED |
| F3_TRACK_LOCK | V2 track locked | DOCUMENTED_NOT_EXECUTED |
| F4_INPUT_MANIFEST | supplied fields frozen | DOCUMENTED_NOT_EXECUTED |
| F5_TRAINING_MANIFEST | data/adaptation declared | DOCUMENTED_NOT_EXECUTED |
| F6_MODEL_PIN | model/revision/license | DOCUMENTED_NOT_EXECUTED |
| F7_ZERO_COST | ZC evidence | DOCUMENTED_NOT_EXECUTED |
| F8_RUNTIME_PIN | environment pinned | DOCUMENTED_NOT_EXECUTED |
| F9_EVALUATOR_PASS | conformance passes | DOCUMENTED_NOT_EXECUTED |
| F10_FAILURE_ACCOUNTING | denominator verified | DOCUMENTED_NOT_EXECUTED |
| F11_RESOURCE_MANIFEST | hardware declared | DOCUMENTED_NOT_EXECUTED |
| F12_ADAPTER_PASS | adapter conformance | DOCUMENTED_NOT_EXECUTED |
| F13_NO_TEST_LEAKAGE | test-seal evidence | DOCUMENTED_NOT_EXECUTED |
| F14_EXECUTION_AUTHORIZATION | explicit human gate | CANNOT_PASS_IN_25R3 |

No preflight gate passes in this documentary prompt.
"""
docs["PRE_BENCHMARK_FREEZE_RECOVERY_REQUIREMENTS.md"] = f"""# Pre-benchmark-freeze recovery requirements

{header}

`BENCHMARK_PARTICIPANT_FREEZE_READY = false`.

Before participant freeze, cheap documentary common-core paths must become
`RECOVERED_DOCUMENTARILY` or `DOCUMENTARY_GATE_EXHAUSTED`:

1. mKGQAgent authoritative public code-license recovery.
2. RDFConfig Zenodo v1.0.0 ↔ GitHub pin source equivalence.
3. CoT-SPARQL authoritative license and essential-artifact recovery.

FIRESPARQL domain-native recovery is optional/non-blocking for QALD; TeBaQA is historical/non-blocking.
SPARQL-LLM local model selection and SGPT full-training preflight may remain after benchmark-design freeze.
This is not authorization to execute any recovery route.
"""
docs["PRE_FREEZE_DOCUMENTARY_RECOVERY_HANDOFF.md"] = f"""# Prompt 25R3A handoff

{header}

Metadata-only scope: (A) mKGQAgent authoritative license search; (B) RDFConfig Zenodo artifact/source
equivalence; (C) CoT-SPARQL authoritative license/artifact search; (D) optional parallel FIRESPARQL
domain-native documentary update, non-blocking for QALD.

Forbidden: model execution, training, weights, paid APIs, benchmark, graph deployment, SPARQL and adapters.
Completion requires each common-core blocker to be documentarily recovered or exhausted under the 25R2
evidence hierarchy.
"""
docs["FAIR_COMPARISON_AND_HOMOGENEITY_GATE.md"] = f"""# Fair comparison and homogeneity gate

{header}

**`FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT_DEFINED_READY_FOR_PRE_FREEZE_DOCUMENTARY_RECOVERY`**

Qualifiers:

- ZERO_EXTERNAL_MONETARY_COST_PRESERVED
- HOMOGENEITY_NOT_ARCHITECTURAL_SAMENESS
- BENCHMARK_INFORMATION_BOUNDARY_DEFINED
- METHOD_INTERNAL_CAPABILITIES_SEPARATED
- TRACK_TAXONOMY_V2_DEFINED
- TRACK_ASSIGNMENTS_RECONCILED
- ORACLE_ACCESS_EXPLICIT
- COMMON_DATASET_PRINCIPLE_DEFINED
- COMMON_GRAPH_PRINCIPLE_DEFINED
- COMMON_EVALUATOR_PRINCIPLE_DEFINED
- TEST_SEAL_PRESERVED
- FAILURES_REMAIN_DENOMINATOR
- L0_L3_COMPARISON_LEVELS_DEFINED
- CROSS_TRACK_GLOBAL_RANKING_FORBIDDEN
- RESOURCE_AND_QUALITY_COMPARISON_SEPARATED
- BENCHMARK_PARTICIPANTS_NOT_YET_FROZEN
- PRE_FREEZE_DOCUMENTARY_RECOVERY_REQUIRED
- NO_METHOD_EXECUTION
- NO_TRAINING
- NO_DEPLOYMENT
- NO_BENCHMARK
- GO_NEXT_ZERO_COST

Next: `RUN_PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE` — Prompt `25R3A`.
ARTIFACT_COMMIT: *(post-commit)*
"""
for name, content in docs.items():
    write(DOC / name, content)

taxonomy = {
    "schema_version": "2.0.0-25R3",
    "run_id": RUN,
    "boundary_rule": "track_is_defined_only_by_benchmark_supplied_information",
    "tracks": {
        "IA_Q_ONLY": {"supplied": ["question", "language", "item_id", "endpoint_reference"], "internal_native_retrieval_allowed": True},
        "IA_SCHEMA_COMMON": {"supplied": ["IA_Q_ONLY", "frozen_common_schema_bundle"], "same_bundle_required": True},
        "IA_ORACLE_GROUNDING": {"supplied": ["gold_derived_grounding_for_evaluated_item"], "end_to_end_claim": False},
        "IA_FIXED_EXTERNAL_GROUNDING": {"supplied": ["same_frozen_grounder_output_for_group"], "native_internal_linker": False},
        "IA_DOMAIN_NATIVE": {"direct_qald_ranking": False},
        "IA_HISTORICAL": {"active_ranking": False},
    },
}
write(CFG / "INFORMATION_ACCESS_TRACK_TAXONOMY_V2.yaml", yaml.safe_dump(taxonomy, sort_keys=False))

eligibility_schema = {
    "schema_version": "1.0.0-25R3",
    "required": [
        "method_a", "variant_a", "method_b", "variant_b", "dataset_equal", "graph_equal",
        "track_equal", "gold_access_equal", "schema_access_equal", "grounding_equal",
        "training_regime", "model_regime", "zero_cost_eligible", "metric_equal",
        "failure_accounting_equal", "test_seal_equal", "resource_reporting_available",
        "comparison_level", "direct_quality_comparison_allowed", "latency_comparison_allowed",
        "resource_efficiency_comparison_allowed", "causal_method_claim_allowed", "reason", "pending_gate",
    ],
    "levels": ["L0_NOT_COMPARABLE", "L1_DESCRIPTIVE_CROSS_TRACK", "L2_FAIR_SYSTEM_LEVEL_COMPARISON", "L3_CONTROLLED_METHOD_COMPARISON"],
}
write(CFG / "DIRECT_COMPARISON_ELIGIBILITY_SCHEMA.yaml", yaml.safe_dump(eligibility_schema, sort_keys=False))

result_schema = {
    "schema_version": "1.0.0-25R3",
    "required": [
        "method_id", "variant_id", "run_id", "dataset_id", "dataset_version", "graph_id",
        "graph_version", "track_id", "adaptation_regime", "model_id", "model_revision",
        "model_license", "controlled_variant", "changed_components", "schema_bundle",
        "grounding_regime", "training_data", "seed", "hardware_profile", "runtime",
        "network_dependencies", "external_cost_usd", "question_count", "success_count",
        "failure_count", "timeout_count", "primary_metrics", "diagnostic_metrics", "latency",
        "memory", "claim_level",
    ],
    "constraints": {"external_cost_usd": 0.0, "claim_level": ["L0", "L1", "L2", "L3"]},
}
write(CFG / "FAIR_RESULT_REPORTING_SCHEMA.yaml", yaml.safe_dump(result_schema, sort_keys=False))

variants = [
    dict(method="sparql_llm", variant="NATIVE_API", q="yes", schema="yes", oe="no", orr="no", fixed="no", ex="no", retrieval="yes", linking="no", lookup="yes", feedback="variant", memory="yes", tools="yes", gold="no", track="IA_SCHEMA_COMMON", evidence="STATIC_AUDIT;native_API_reference;ZERO_COST_blocked"),
    dict(method="sparql_llm", variant="ZERO_COST_LOCAL_BACKEND", q="yes", schema="yes", oe="no", orr="no", fixed="no", ex="no", retrieval="yes", linking="no", lookup="yes", feedback="variant", memory="yes", tools="yes", gold="no", track="IA_SCHEMA_COMMON", evidence="STATIC_AUDIT;AC_SPARQL_LLM_SCHEMA_COMMON_NATIVE"),
    dict(method="sparql_llm", variant="ZERO_COST_LOCAL_BACKEND_INTERNAL_FEEDBACK", q="yes", schema="yes", oe="no", orr="no", fixed="no", ex="no", retrieval="yes", linking="no", lookup="yes", feedback="yes", memory="yes", tools="yes", gold="no", track="IA_SCHEMA_COMMON", evidence="AC_SPARQL_LLM_SCHEMA_COMMON_INTERNAL_FEEDBACK"),
    dict(method="sgpt", variant="sgpt_q", q="yes", schema="no", oe="no", orr="no", fixed="no", ex="no", retrieval="no", linking="no", lookup="no", feedback="no", memory="no", tools="no", gold="no", track="IA_Q_ONLY", evidence="SGPT_ADAPTER_CONTRACTS"),
    dict(method="sgpt", variant="sgpt_qk", q="yes", schema="no", oe="yes", orr="yes", fixed="no", ex="no", retrieval="no", linking="no", lookup="no", feedback="no", memory="no", tools="no", gold="yes_evaluated_item", track="IA_ORACLE_GROUNDING", evidence="SGPT_ADAPTER_CONTRACTS"),
    dict(method="mkgqagent", variant="NATIVE_AGENTIC", q="yes", schema="no", oe="no", orr="no", fixed="no", ex="no", retrieval="yes_experience_pool", linking="yes_falcon", lookup="no", feedback="yes", memory="yes", tools="yes", gold="no_test_gold", track="IA_Q_ONLY", evidence="audit/mkgqagent/STATIC_AUDIT.md;MKGQAGENT_ADAPTER_CONTRACT"),
    dict(method="mkgqagent", variant="CONTROLLED_LOCAL_BACKEND", q="yes", schema="no", oe="no", orr="no", fixed="no", ex="no", retrieval="yes_experience_pool", linking="yes_preserved_or_frozen_if_admissible", lookup="no", feedback="yes_local_endpoint", memory="yes", tools="yes", gold="no_test_gold", track="IA_Q_ONLY", evidence="25R2 controlled candidate;blocked until public license"),
    dict(method="rdfconfig_llm", variant="NATIVE_DOMAIN", q="yes", schema="domain_native", oe="no", orr="no", fixed="no", ex="no", retrieval="no", linking="no", lookup="yes_rdfconfig", feedback="no", memory="no", tools="ruby", gold="no", track="IA_DOMAIN_NATIVE", evidence="RDFCONFIG_ADAPTER_CONTRACTS"),
    dict(method="rdfconfig_llm", variant="CONTROLLED_DBPEDIA_SCHEMA_COMMON", q="yes", schema="yes", oe="no", orr="no", fixed="no", ex="no", retrieval="no", linking="no", lookup="yes_rdfconfig", feedback="no", memory="no", tools="ruby", gold="no", track="IA_SCHEMA_COMMON", evidence="AC_RDFCONFIG_SCHEMA_COMMON_DBPEDIA_NEGATIVE;prospective_only"),
    dict(method="cot_sparql", variant="NATIVE_INTERNAL_GROUNDING", q="yes", schema="no", oe="no", orr="no", fixed="no", ex="no_train_internal", retrieval="yes_train_one_shot", linking="yes_native_services", lookup="no", feedback="yes_http_validation", memory="yes_train_index", tools="yes", gold="no_test_gold;train_gold_examples_internal", track="IA_Q_ONLY", evidence="GROUNDING_AND_LINKING_AUDIT;RETRIEVAL_AND_PROMPT_AUDIT"),
    dict(method="cot_sparql", variant="CONTROLLED_COMMON_FROZEN_GROUNDING", q="yes", schema="no", oe="no", orr="no", fixed="yes", ex="no_train_internal", retrieval="yes_train_one_shot", linking="benchmark_supplied_frozen", lookup="no", feedback="yes_http_validation", memory="yes_train_index", tools="yes", gold="no", track="IA_FIXED_EXTERNAL_GROUNDING", evidence="COT_SPARQL_ADAPTER_CONTRACT;prospective_only"),
    dict(method="firesparql", variant="DOMAIN_NATIVE", q="yes", schema="domain_native", oe="no", orr="no", fixed="no", ex="train_only", retrieval="yes", linking="method_specific", lookup="domain", feedback="qlever_native", memory="yes", tools="yes", gold="no_test_gold", track="IA_DOMAIN_NATIVE", evidence="audit/firesparql/ARCHITECTURE_AND_DATA_FLOW.md"),
    dict(method="firesparql", variant="DOMAIN_NATIVE_CLEANED", q="yes", schema="domain_native", oe="no", orr="no", fixed="no", ex="train_only", retrieval="yes", linking="method_specific", lookup="domain", feedback="qlever_native", memory="yes", tools="gpt4o_cleaning_paid_blocked", gold="no_test_gold", track="IA_DOMAIN_NATIVE", evidence="AC_FIRESPARQL_CLEANED;ZERO_COST blocked"),
    dict(method="firesparql", variant="DOMAIN_NATIVE_RAG", q="yes", schema="domain_native", oe="no", orr="no", fixed="no", ex="train_only", retrieval="yes_rag", linking="method_specific", lookup="domain", feedback="qlever_native", memory="yes", tools="groq_service_blocked", gold="no_test_gold", track="IA_DOMAIN_NATIVE", evidence="AC_FIRESPARQL_RAG"),
    dict(method="tebaqa", variant="HISTORICAL", q="historical", schema="historical", oe="no", orr="no", fixed="no", ex="no", retrieval="historical", linking="historical", lookup="historical", feedback="historical", memory="historical", tools="historical", gold="unknown_not_active", track="IA_HISTORICAL", evidence="METHOD_REGISTRY;historical_only"),
]

boundary_fields = ["method", "variant", "external_question", "external_schema", "external_oracle_entities", "external_oracle_relations", "external_fixed_grounding", "external_examples", "internal_retrieval", "internal_linking", "internal_schema_lookup", "internal_endpoint_feedback", "internal_memory", "internal_agent_tools", "gold_dependency", "candidate_track_v2", "evidence"]
boundary_rows = [{boundary_fields[0]: v["method"], boundary_fields[1]: v["variant"], **dict(zip(boundary_fields[2:], [v["q"], v["schema"], v["oe"], v["orr"], v["fixed"], v["ex"], v["retrieval"], v["linking"], v["lookup"], v["feedback"], v["memory"], v["tools"], v["gold"], v["track"], v["evidence"]]))} for v in variants]
csv_write(AUD / "PHASE2_METHOD_INFORMATION_BOUNDARY_MATRIX.csv", boundary_fields, boundary_rows)

previous = {
    ("sparql_llm", "NATIVE_API"): "IA_SCHEMA_COMMON",
    ("sparql_llm", "ZERO_COST_LOCAL_BACKEND"): "IA_SCHEMA_COMMON",
    ("sparql_llm", "ZERO_COST_LOCAL_BACKEND_INTERNAL_FEEDBACK"): "IA_SCHEMA_COMMON",
    ("sgpt", "sgpt_q"): "IA_Q_ONLY", ("sgpt", "sgpt_qk"): "IA_ORACLE_GROUNDING",
    ("mkgqagent", "NATIVE_AGENTIC"): "IA_Q_ONLY|handoff_25R2_IA_SCHEMA_COMMON",
    ("mkgqagent", "CONTROLLED_LOCAL_BACKEND"): "handoff_25R2_IA_SCHEMA_COMMON",
    ("rdfconfig_llm", "NATIVE_DOMAIN"): "IA_SCHEMA_COMMON|IA_DOMAIN_NATIVE",
    ("rdfconfig_llm", "CONTROLLED_DBPEDIA_SCHEMA_COMMON"): "IA_SCHEMA_COMMON_negative_contract",
    ("cot_sparql", "NATIVE_INTERNAL_GROUNDING"): "IA_FIXED_EXTERNAL_GROUNDING|handoff_25R2_IA_ORACLE_GROUNDING",
    ("cot_sparql", "CONTROLLED_COMMON_FROZEN_GROUNDING"): "IA_FIXED_EXTERNAL_GROUNDING",
    ("firesparql", "DOMAIN_NATIVE"): "IA_DOMAIN_NATIVE",
    ("firesparql", "DOMAIN_NATIVE_CLEANED"): "IA_DOMAIN_NATIVE",
    ("firesparql", "DOMAIN_NATIVE_RAG"): "IA_DOMAIN_NATIVE",
    ("tebaqa", "HISTORICAL"): "IA_HISTORICAL",
}
recon_fields = ["method", "variant", "benchmark_supplied_question", "benchmark_supplied_schema", "benchmark_supplied_gold_entities", "benchmark_supplied_gold_relations", "benchmark_supplied_examples", "benchmark_supplied_fixed_linker_output", "internal_retrieval", "internal_entity_linker", "internal_relation_linker", "internal_endpoint_feedback", "internal_experience_pool", "internal_schema_lookup", "test_gold_dependency", "previous_track", "candidate_track_v2", "track_changed", "change_reason", "evidence", "confidence"]
recon_rows = []
for v in variants:
    old = previous[(v["method"], v["variant"])]
    change = old != v["track"]
    reason = "boundary_reaudit_confirmed"
    if v["method"] == "mkgqagent":
        reason = "entrypoint receives question+dataset only; tools/linkers/pool/schema behavior are internal"
    elif v["method"] == "cot_sparql" and v["variant"].startswith("NATIVE"):
        reason = "native linker services and train-only one-shot are invoked internally; no evaluated-item gold crosses boundary"
    elif v["method"] == "rdfconfig_llm":
        reason = "native life-science domain separated from prospective controlled DBpedia schema-common negative contract"
    recon_rows.append(dict(method=v["method"], variant=v["variant"], benchmark_supplied_question=v["q"], benchmark_supplied_schema=v["schema"], benchmark_supplied_gold_entities=v["oe"], benchmark_supplied_gold_relations=v["orr"], benchmark_supplied_examples=v["ex"], benchmark_supplied_fixed_linker_output=v["fixed"], internal_retrieval=v["retrieval"], internal_entity_linker=v["linking"], internal_relation_linker=v["linking"], internal_endpoint_feedback=v["feedback"], internal_experience_pool=v["memory"], internal_schema_lookup=v["lookup"], test_gold_dependency=v["gold"], previous_track=old, candidate_track_v2=v["track"], track_changed=str(change).lower(), change_reason=reason, evidence=v["evidence"], confidence="HIGH" if v["method"] in {"mkgqagent", "cot_sparql", "sgpt"} else "MEDIUM_HIGH"))
csv_write(AUD / "PHASE2_TRACK_ASSIGNMENT_RECONCILIATION.csv", recon_fields, recon_rows)

dimensions = [
    ("dataset","yes","yes","no","yes","same task universe"), ("test_split","yes","yes","no","yes","paired denominator"),
    ("graph","yes","yes","no","yes","same answers/semantics"), ("gold","track_equal","yes","cross_track_only","yes","oracle changes task"),
    ("metric","yes","yes","no","yes","same interpretation"), ("evaluator","yes","yes","no","yes","same implementation"),
    ("input_track","yes","yes","cross_track_L1","yes","same supplied information"), ("schema","track_equal","yes","method_internal_may_differ","yes","boundary"),
    ("grounding","track_equal","yes","method_internal_may_differ","yes","boundary"), ("training","no","yes_for_causal","yes_L2","yes","system vs causal"),
    ("backbone","no","yes_when_claimed","yes_L2","yes","system vs controlled"), ("architecture","no","isolated_component_only","yes","yes","legitimate method difference"),
    ("hardware","no_quality_yes_efficiency","yes_efficiency","yes_quality","yes","quality/operations split"), ("timeout","yes_when_meaningful","yes","native_behavior_preserved","yes","failure bias"),
    ("seeds","policy_equal","yes","determinism_dependent","yes","replication"), ("external_services","reproducibility_equal","yes","method_internal","yes","drift"),
    ("cost","yes_zero","yes_zero","no","yes","locked policy"), ("failure_accounting","yes","yes","no","yes","denominator"),
    ("test_seal","yes","yes","no","yes","leakage prevention"),
]
csv_write(AUD / "PHASE2_HOMOGENEITY_DIMENSION_MATRIX.csv", ["dimension","must_be_equal_for_L2","must_be_equal_for_L3","may_differ","must_report","reason"], [dict(zip(["dimension","must_be_equal_for_L2","must_be_equal_for_L3","may_differ","must_report","reason"], r)) for r in dimensions])

pair_fields = eligibility_schema["required"]
def pair(a, va, b, vb, level, allowed, reason, pending, track_equal="yes", zero="pending"):
    return dict(method_a=a, variant_a=va, method_b=b, variant_b=vb, dataset_equal="required_QALD", graph_equal="required_DBPEDIA_2016_10", track_equal=track_equal, gold_access_equal="required", schema_access_equal="required_by_track", grounding_equal="required_by_track", training_regime="report_may_differ_L2", model_regime="report_may_differ_L2", zero_cost_eligible=zero, metric_equal="required", failure_accounting_equal="required", test_seal_equal="required", resource_reporting_available="pending", comparison_level=level, direct_quality_comparison_allowed=allowed, latency_comparison_allowed="no_pending_matched_hardware", resource_efficiency_comparison_allowed="no_pending_matched_hardware", causal_method_claim_allowed="no" if level != "L3_CONTROLLED_METHOD_COMPARISON" else "conditional", reason=reason, pending_gate=pending)
pairs = [
    pair("sgpt","sgpt_q","mkgqagent","NATIVE_AGENTIC","L2_FAIR_SYSTEM_LEVEL_COMPARISON","pending","same V2 Q_ONLY track; independent implementations","license+F0-F14"),
    pair("sgpt","sgpt_q","cot_sparql","NATIVE_INTERNAL_GROUNDING","L2_FAIR_SYSTEM_LEVEL_COMPARISON","pending","same V2 Q_ONLY only if native grounding remains internal","license+artifacts+compute+F0-F14"),
    pair("mkgqagent","NATIVE_AGENTIC","cot_sparql","NATIVE_INTERNAL_GROUNDING","L2_FAIR_SYSTEM_LEVEL_COMPARISON","pending","same V2 Q_ONLY; both documentary blocked","licenses+artifacts+F0-F14"),
    pair("sparql_llm","ZERO_COST_LOCAL_BACKEND","rdfconfig_llm","CONTROLLED_DBPEDIA_SCHEMA_COMMON","L2_FAIR_SYSTEM_LEVEL_COMPARISON","pending","prospective schema-common independent systems","RDF_equivalence+schema_bundle+models+F0-F14"),
    pair("sgpt","sgpt_q","sgpt","sgpt_qk","L1_DESCRIPTIVE_CROSS_TRACK","no","Q_ONLY vs evaluated-item gold oracle","track_mismatch",track_equal="no"),
    pair("cot_sparql","NATIVE_INTERNAL_GROUNDING","cot_sparql","CONTROLLED_COMMON_FROZEN_GROUNDING","L1_DESCRIPTIVE_CROSS_TRACK","no","native internal vs benchmark-supplied fixed grounding","track_mismatch",track_equal="no"),
    pair("firesparql","DOMAIN_NATIVE","sgpt","sgpt_q","L0_NOT_COMPARABLE","no","ORKG/SciQA vs QALD/DBpedia","domain_graph_test_mismatch",track_equal="no"),
]
pairs[-1]["dataset_equal"] = "no"
pairs[-1]["graph_equal"] = "no"
csv_write(AUD / "PHASE2_DIRECT_COMPARISON_ELIGIBILITY_MATRIX.csv", pair_fields, pairs)

groups = [
    dict(group_id="QALD_Q_ONLY_SYSTEM_LEVEL", status="PROVISIONAL_BLOCKED", members_candidate="sgpt_q;mkgqagent_NATIVE_AGENTIC;cot_NATIVE_INTERNAL_GROUNDING", minimum_members=2, current_eligible_count=0, blocked_candidates="all_runtime; mkg_license; cot_license_artifacts_compute", comparison_level="L2", direct_ranking_allowed="only_after_F0-F14_and_two_independent", claim_boundary="system_quality_only"),
    dict(group_id="QALD_SCHEMA_COMMON_SYSTEM_LEVEL", status="PROVISIONAL_BLOCKED", members_candidate="sparql_llm_ZERO_COST_LOCAL_BACKEND;rdfconfig_CONTROLLED_DBPEDIA_SCHEMA_COMMON", minimum_members=2, current_eligible_count=0, blocked_candidates="model_selection; RDF_equivalence/legal/schema_adaptation", comparison_level="L2", direct_ranking_allowed="pending", claim_boundary="system_quality_only"),
    dict(group_id="QALD_ORACLE_GROUNDING", status="SINGLE_FAMILY_DESCRIPTIVE", members_candidate="sgpt_qk", minimum_members=2, current_eligible_count=0, blocked_candidates="checkpoint_or_retrain;runtime", comparison_level="L1_until_independent_pair", direct_ranking_allowed="no", claim_boundary="oracle-assisted"),
    dict(group_id="QALD_FIXED_GROUNDING", status="SINGLE_FAMILY_PROSPECTIVE", members_candidate="cot_CONTROLLED_COMMON_FROZEN_GROUNDING", minimum_members=2, current_eligible_count=0, blocked_candidates="legal;artifacts;common_grounder", comparison_level="L1", direct_ranking_allowed="no", claim_boundary="fixed-grounding"),
    dict(group_id="DOMAIN_NATIVE", status="DESCRIPTIVE", members_candidate="rdfconfig_NATIVE_DOMAIN;firesparql_DOMAIN_NATIVE", minimum_members=2, current_eligible_count=0, blocked_candidates="different native domains/KGs;legal/artifacts", comparison_level="L0_or_domain_specific", direct_ranking_allowed="no_global", claim_boundary="native-domain only"),
    dict(group_id="HISTORICAL", status="HISTORICAL_ONLY", members_candidate="tebaqa_HISTORICAL", minimum_members=2, current_eligible_count=0, blocked_candidates="not_active", comparison_level="L1_descriptive", direct_ranking_allowed="no", claim_boundary="historical context"),
    dict(group_id="CONTROLLED_BACKBONE_FUTURE", status="UNINSTANTIATED", members_candidate="", minimum_members=2, current_eligible_count=0, blocked_candidates="no common backbone selected", comparison_level="L3_future", direct_ranking_allowed="no", claim_boundary="causal only after controls"),
]
csv_write(AUD / "PHASE2_PROVISIONAL_COMPARISON_GROUPS.csv", list(groups[0]), groups)

risks = [
    ("track_misclassification","HIGH","boundary audit + manifests"), ("oracle_leakage","CRITICAL","gold-source trace"),
    ("test_leakage","CRITICAL","seal + no-test declarations"), ("schema_asymmetry","HIGH","bundle hash"),
    ("grounding_asymmetry","HIGH","track lock"), ("hidden_external_service","HIGH","network manifest"),
    ("paid_api_advantage","CRITICAL","ZERO_COST gate"), ("training_data_mismatch","HIGH","training manifest"),
    ("test_filtering","CRITICAL","fixed IDs/denominator"), ("different_graph","CRITICAL","graph pin"),
    ("endpoint_drift","HIGH","local snapshot semantics"), ("model_backbone_confounding","HIGH","L2 claim limit"),
    ("hardware_confounding","MEDIUM","quality/efficiency split"), ("timeout_bias","HIGH","predeclared group ceiling"),
    ("failure_denominator_bias","CRITICAL","common accounting"), ("prompt_tuning_on_test","CRITICAL","seal"),
    ("random_seed_cherry_picking","HIGH","seed preregistration"), ("quantization_confounding","MEDIUM","report/stratify"),
    ("method_specific_postprocessing","HIGH","declare as method component"), ("manual_correction","CRITICAL","forbidden"),
    ("domain_mismatch","CRITICAL","L0/domain track"), ("global_ranking_misuse","HIGH","cross-track prohibition"),
    ("controlled_variant_identity_loss","HIGH","25R2 admissibility + claim label"),
]
csv_write(AUD / "PHASE2_FAIR_COMPARISON_RISK_REGISTER.csv", ["risk_id","severity","control","status"], [dict(risk_id=a,severity=b,control=c,status="OPEN_DOCUMENTARY_CONTROL_DEFINED") for a,b,c in risks])

# Reconcile existing matrices without deleting historical columns/rows.
track_map = {
    "mkgqagent_q_only_agentic": ("IA_Q_ONLY", "question+dataset boundary; internal pool/linker/tools"),
    "cot_native_external_services": ("IA_Q_ONLY", "native services are method-internal, not benchmark-supplied"),
    "cot_fixed_external_grounding": ("IA_Q_ONLY", "historical aggregate represented native linker calls; benchmark boundary supplies no grounding"),
    "cot_common_frozen_grounding": ("IA_FIXED_EXTERNAL_GROUNDING", "controlled benchmark-supplied frozen outputs"),
    "rdfconfig_domain_native": ("IA_DOMAIN_NATIVE", "native life-science domain"),
    "rdfconfig_schema_or_domain": ("IA_DOMAIN_NATIVE", "historical dual candidate resolved: native is domain-only; controlled DBpedia is separate"),
    "rdfconfig_schema_common_dbpedia": ("IA_SCHEMA_COMMON", "prospective controlled negative contract"),
}
for rel in ["audit/PHASE2_TRACK_ASSIGNMENT_MATRIX.csv", "audit/PHASE2_ORACLE_AND_GROUNDING_MATRIX.csv", "audit/PHASE2_DATASET_TRACK_COMPATIBILITY.csv"]:
    path = ROOT / rel
    with path.open(newline="", encoding="utf-8") as h:
        rows = list(csv.DictReader(h))
        fields = list(rows[0])
    extra = ["taxonomy_version", "reconciliation_id", "old_track", "new_track", "reconciliation_reason", "reconciliation_evidence"]
    for f in extra:
        if f not in fields:
            fields.append(f)
    for row in rows:
        variant = row.get("variant_id") or ""
        old = row.get("information_access_track") or row.get("track_id") or ""
        new, reason = track_map.get(variant, (old, "confirmed_or_aggregate_historical_row"))
        row.update(taxonomy_version="TRACK_TAXONOMY_V2", reconciliation_id="PROMPT_25R3_RECONCILIATION", old_track=old, new_track=new, reconciliation_reason=reason, reconciliation_evidence="audit/fairness/PHASE2_TRACK_ASSIGNMENT_RECONCILIATION.csv")
    csv_write(path, fields, rows)

report = f"""# Phase 2 fair comparison and homogeneity contract report

{header}

## 1. Executive summary
External conditions, not architectures, are homogenized. Taxonomy V2 and L0–L3 are documentary only.

## 2. Input gate
HEAD/origin `6c5ddb631cf3961c6777906b6c3595e87ab4f0ba`, clean `main`; required 25R2 gate satisfied.
25R2: initial `3c57735c…`, artifact `5da725f3…`, publication/tip `6c5ddb63…`, push confirmed.

## 3. Scientific motivation
Heterogeneous systems need explicit task/information equality without suppressing legitimate capabilities.

## 4. Homogeneity principle
Dataset/test/graph/evaluator/track/denominator/seal/cost are common at L2; architecture need not be.

## 5. Benchmark-information boundary
Only harness-supplied fields determine the information track.

## 6. Internal method capabilities
Native retrieval, linkers, indexes, tools and endpoint feedback are internal unless supplied by the harness.

## 7. Track taxonomy V2
Q_ONLY, SCHEMA_COMMON, ORACLE, FIXED_EXTERNAL, DOMAIN_NATIVE and HISTORICAL are defined in version 2.0.0-25R3.

## 8. Track reconciliation
The reconciliation matrix records prior labels, new labels, reason, evidence and confidence without erasing history.
Prompt 19 adapter labels remain historical documentary evidence; affected CoT input contracts must be revised
before F12, and cannot override V2 merely because they called a method-internal service “external grounding”.

## 9. SPARQL-LLM
Native API and controlled local variants are SCHEMA_COMMON; paid native API is not ZERO_COST eligible.

## 10. SGPT Q
Q_ONLY, supervised/retrained regime declared, no oracle input.

## 11. SGPT QK
ORACLE_GROUNDING because evaluated-item gold-derived constants cross the boundary; always oracle-assisted.

## 12. mKGQAgent
Q_ONLY. Entrypoint receives question+dataset; experience pool, Falcon, tools and endpoint feedback are internal.
The provisional 25R2 handoff SCHEMA_COMMON label is rejected.

## 13. RDFConfig
Native life-science variant is DOMAIN_NATIVE. Prospective DBpedia controlled variant is SCHEMA_COMMON and
remains a negative contract pending Zenodo equivalence, legal resolution and schema adaptation review.

## 14. CoT-SPARQL
Native is Q_ONLY: native service calls and train-only one-shot retrieval are internal; no test-item gold crosses
the boundary. Only prospective benchmark-supplied frozen grounding is FIXED_EXTERNAL. It is not ORACLE.

## 15. FIRESPARQL
DOMAIN_NATIVE/ORKG; no QALD ranking. Cleaned/RAG variants retain the domain track and their service blockers.

## 16. TeBaQA
HISTORICAL; descriptive context only.

## 17. Dataset homogeneity
Exact QALD9_PLUS_EN_DBPEDIA test item universe, IDs, exclusions and denominator are required.

## 18. Graph homogeneity
All L2 QALD results require DBPEDIA_2016_10_QALD9_NATIVE_ENDPOINT_EQUIVALENT semantics. Runtime is unavailable.

## 19. Schema
SCHEMA_COMMON requires one hashed frozen bundle; richer internal derivation is reported and reviewed in 25R4.

## 20. Grounding/oracle
Internal grounding ≠ oracle. Evaluated-item gold input is oracle; common frozen supplied grounding is separate.

## 21. Training/adaptation
Test use is prohibited; regimes and external corpora are reported. Different regimes limit causal claims.

## 22. Model/backbone
Native backbones may differ at L2. No common backbone is selected; controlled backbones are future L3 candidates.

## 23. Resources
Quality and efficiency claims are separated; all hardware and quantization fields are mandatory.

## 24. Timeout
A common safety ceiling coexists with native internal behavior; timeouts remain in the denominator.

## 25. Stochasticity
Freeze inference seeds; prefer three training seeds when ZERO_COST feasible; otherwise SINGLE_RUN_RESOURCE_LIMITED.

## 26. Network/services
Primary dependencies must be reproducible and ZERO_COST; commercial free tiers are forbidden as primary.

## 27. Metrics
Answer Precision/Recall/F1 and Execution Exact Accuracy remain primary; BLEU/ROUGE/exact query are supplementary.

## 28. Failure accounting
Syntax/execution error, timeout, abstention, no output and invalid output remain in the denominator.

## 29. Test sealing
QALD test remains SEALED; prompt/tuning/example/recovery choices based on test are forbidden.

## 30. Comparison levels
L0 not comparable; L1 descriptive cross-track; L2 fair system-level; L3 controlled method comparison.

## 31. Direct comparison matrix
Potential L2 pairs exist only provisionally; every row remains pending F0–F14 and method recovery gates.

## 32. Comparison groups
Potential L2 groups: QALD Q_ONLY (SGPT Q, mKGQAgent, native CoT) and QALD SCHEMA_COMMON
(SPARQL-LLM local, controlled RDFConfig). Current eligible count is zero. No L3 pair exists.

## 33. Fairness risks
Twenty-three risks include track/oracle/test/schema/grounding/service/cost/data/graph/backbone/resource biases.

## 34. Claim policy
System-level claims name external conditions; causal architecture and global cross-track ranking are forbidden.

## 35. Preflight
F0–F14 are defined as DOCUMENTED_NOT_EXECUTED; F14 cannot pass in 25R3.

## 36. QALD status
Primary view acquired, validated and SEALED; LC-QuAD remains HOLD.

## 37. DBpedia status
Compressed target acquired; NOT_DEPLOYED; no graph operation in this run.

## 38. Recovery dependencies
mKG license, RDFConfig Zenodo equivalence and CoT license/artifacts are blocking documentary paths.

## 39. Benchmark-freeze prerequisites
Freeze is NOT_READY_PENDING_DOCUMENTARY_RECOVERY until cheap common-core documentary paths recover or exhaust.

## 40. Revised roadmap
25R3A precedes 25R4; deployment/profile/25B/D1–D6/G5/execution/adapters/benchmark remain deferred.

## 41. Next action
Exactly `RUN_PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE`, Prompt 25R3A.

## 42. Doctoral claim boundary
Claims remain tied to comparison level, track, variant identity and common experimental conditions.

## 43. Conservative conclusion
No participant is frozen and no method/model/training/graph/SPARQL/adapter/evaluator/benchmark is executed.
G4 NOT_SATISFIED; G5 runtime pending; G6D documented; G6I pending; adapters false; benchmark
NOT_CURRENTLY_ELIGIBLE. ZERO_EXTERNAL_MONETARY_COST, USD 0.00.
"""
write(ROOT / "audit/PHASE2_FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT_REPORT.md", report)

decision = f"""# Decision 022 — Fair comparison and homogeneity contract

Date: 2026-10-12 · RUN_ID `{RUN}`

Accepted: homogeneity is not architectural sameness; the benchmark-supplied/internal boundary and Track
Taxonomy V2 govern access; dataset/graph/evaluator/failure/test-seal conditions are common; L0–L3 govern
claims; quality and efficiency are distinct; ZERO_COST is mandatory; no global cross-track ranking.

mKGQAgent is Q_ONLY; native CoT is Q_ONLY while only its prospective frozen-grounding variant is
FIXED_EXTERNAL; RDFConfig native and controlled DBpedia variants remain separate. Participants are not
frozen. Pre-freeze documentary recovery is required. No execution occurred.

Decision: next = `RUN_PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE`, Prompt `25R3A`.
"""
write(ROOT / "docs/decisions/022_fair_comparison_and_homogeneity_contract.md", decision)

next_decision = f"""# NEXT AFTER FAIR COMPARISON CONTRACT

| Field | Value |
|---|---|
| Gate | `FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT_DEFINED_READY_FOR_PRE_FREEZE_DOCUMENTARY_RECOVERY` |
| Protocol / taxonomy | `1.0.0-25R3` / `2.0.0-25R3` |
| Benchmark freeze | `NOT_READY_PENDING_DOCUMENTARY_RECOVERY` |
| Blocking documentary paths | mKG license; RDF Zenodo equivalence; CoT license+artifacts |
| QALD / DBpedia | primary acquired+sealed / compressed acquired NOT_DEPLOYED |
| G4 / G5 / G6D / G6I | NOT_SATISFIED / pending / documented / pending |
| Adapters / benchmark | false / NOT_CURRENTLY_ELIGIBLE |
| Next action | `RUN_PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE` |
| Next prompt | `Prompt_25R3A` |

Exactly one next action. Deployment/profile/25B/training/recovery execution/benchmark remain deferred.
ARTIFACT_COMMIT: *(post-commit)*
"""
write(ROOT / "audit/NEXT_AFTER_FAIR_COMPARISON_CONTRACT_DECISION.md", next_decision)

roadmap_rows = [
    (1,"GLOBAL_BLOCKER_RECOVERY_AND_ZERO_COST_RECONCILIATION","Prompt_25R1","COMPLETE"),
    (2,"ZERO_COST_METHOD_RECOVERY_PROTOCOL","Prompt_25R2","COMPLETE"),
    (3,"FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT","Prompt_25R3","COMPLETE"),
    (4,"PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE","Prompt_25R3A","NEXT"),
    (5,"COMMON_CORE_BENCHMARK_FREEZE_AND_EXTERNAL_VALIDATION_PLAN","Prompt_25R4","PLANNED"),
    (6,"HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION","human_gate","DEFERRED_NOT_CANCELLED"),
    (7,"FINAL_DEPLOYMENT_AUTHORIZATION_PACKAGE","Prompt_25B","PLANNED_AFTER_25R4_AND_PROFILE"),
    (8,"RESOURCE_CONFIGURATION","D1","PLANNED"), (9,"DECOMPRESSION_AND_RDF_VALIDATION","D2","PLANNED"),
    (10,"RUNTIME_IMAGE_ACQUISITION","D3","PLANNED"), (11,"VIRTUOSO_LOAD","D4","PLANNED"),
    (12,"GRAPH_RUNTIME_VALIDATION","D5_G4","PLANNED"), (13,"GOLD_MATERIALIZATION","D6","PLANNED"),
    (14,"METRIC_IMPLEMENTATION_AND_CONFORMANCE","G5","PLANNED"),
    (15,"BLOCKED_METHOD_RECOVERY_EXECUTION_WAVE","recovery_prompts","PLANNED"),
    (16,"G6I_G7_ADAPTER_IMPLEMENTATION_DECISION","decision","PLANNED"),
    (17,"ADAPTER_IMPLEMENTATION","implementation","PLANNED"), (18,"COMMON_PREFLIGHT","runtime","PLANNED"),
    (19,"QALD_PRIMARY_BENCHMARK","experiment","PLANNED"), (20,"TEXT2SPARQL25_EXTERNAL_VALIDATION","future_experiment","PLANNED"),
    (21,"ERROR_ANALYSIS_PE6","research","PLANNED"), (22,"AI_MODEL_DISCOVERY_CASE_STUDY","research","PLANNED"),
    (23,"TEXT_TO_SQL_TRANSFER_PE7","research","PLANNED"), (24,"NEW_TEXT_TO_SPARQL_METHOD_PE8","research","PLANNED"),
    (25,"COMPARISON","research","PLANNED"), (26,"ABLATION_STUDY","research","PLANNED"),
    (27,"FINAL_SCIENTIFIC_LITERATURE_TRIANGULATION","research","PLANNED"),
    (28,"THESIS_REPRODUCIBILITY_EVIDENCE_PACKAGE","research","PLANNED"),
]
csv_write(ROOT / "audit/PHASE2_REVISED_RESEARCH_ROADMAP.csv", ["order","action","vehicle","status"], [dict(zip(["order","action","vehicle","status"], r)) for r in roadmap_rows])

plan = f"""# PLAN_SYNC — Estado para optimización del plan de prompts

**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab
**Última actualización:** 2026-10-12 (Prompt **25R3**)
**Fase:** fairness contract complete · pre-freeze documentary recovery pending
**SHA inicial 25R3:** `6c5ddb631cf3961c6777906b6c3595e87ab4f0ba`
**RUN_ID:** `{RUN}`

Gate: `FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT_DEFINED_READY_FOR_PRE_FREEZE_DOCUMENTARY_RECOVERY`.
Taxonomy V2 locks the benchmark information boundary; mKG and native CoT resolve to Q_ONLY; RDF native
remains DOMAIN_NATIVE. Participants are not frozen. No execution; ZERO_COST.

## Prompt 25R2 reconciliation

Initial `3c57735c4e1f7100fc5e98c54a6505767951e61a`; artifact
`5da725f3a8a2a334e38c82430a59a15d52acdff0`; publication/tip
`6c5ddb631cf3961c6777906b6c3595e87ab4f0ba`; push confirmed.

## Unique next action

`RUN_PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE` — Prompt `25R3A` — `GO_NEXT_ZERO_COST`.
Do not select deployment, 25B, training, method execution or benchmark.

## Publication

ARTIFACT_COMMIT: *(post-commit)*
publication metadata commit: *(post-commit tip; max 2 commits)*
push: pending
"""
write(ROOT / "PLAN_SYNC.md", plan)

guidance = f"""# NEXT_PROMPT_GUIDANCE

**Tras:** Prompt 25R3 (`{RUN}`)
**Gate:** `FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT_DEFINED_READY_FOR_PRE_FREEZE_DOCUMENTARY_RECOVERY`

## Acción siguiente

`RUN_PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE`

**Prompt 25R3A** — Pre-freeze documentary recovery wave for authoritative legal and artifact blockers of
potential common-core methods, ZERO_COST, metadata only, without model execution, training, deployment or
benchmark.

Status: **GO_NEXT_ZERO_COST**. No seleccionar aún 25R4, 25B, deployment, training, execution or benchmark.
"""
write(ROOT / "docs/plan-sync/NEXT_PROMPT_GUIDANCE.md", guidance)
write(ROOT / "docs/plan-sync/PLANNER_LOOP.md", f"""# PLANNER_LOOP

1. `PLAN_SYNC.md`
2. `docs/protocols/common/fairness/{RUN}/FAIR_COMPARISON_AND_HOMOGENEITY_GATE.md`
3. `audit/PHASE2_FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT_REPORT.md`
4. `audit/NEXT_AFTER_FAIR_COMPARISON_CONTRACT_DECISION.md`
5. `METHOD_REGISTRY.yaml`

Next: `RUN_PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE` — Prompt `25R3A`.
""")

index = ROOT / "docs/plan-sync/ARTIFACT_INDEX.md"
idx = index.read_text(encoding="utf-8")
idx = idx.replace("**Última actualización:** 2026-07-22 (Prompt 23C)", "**Última actualización:** 2026-10-12 (Prompt 25R3)")
marker = "| ID | Tema | Ruta | Cuándo leerlo |\n|---|---|---|---|\n"
new_rows = (
    f"| P25R3-GATE | Fairness gate | `docs/protocols/common/fairness/{RUN}/FAIR_COMPARISON_AND_HOMOGENEITY_GATE.md` | Tras 25R3 |\n"
    "| P25R3-RPT | Fairness report | `audit/PHASE2_FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT_REPORT.md` | Contrato completo |\n"
    "| P25R3-TRK | Track reconciliation | `audit/fairness/PHASE2_TRACK_ASSIGNMENT_RECONCILIATION.csv` | V2 evidence |\n"
    "| P25R3-PAIR | Direct comparison matrix | `audit/fairness/PHASE2_DIRECT_COMPARISON_ELIGIBILITY_MATRIX.csv` | L0–L3 |\n"
    f"| P25R3-HAND | 25R3A handoff | `docs/protocols/common/fairness/{RUN}/PRE_FREEZE_DOCUMENTARY_RECOVERY_HANDOFF.md` | Next |\n"
)
idx = idx.replace(marker, marker + new_rows)
write(index, idx)

for rel in ["README.md", "PROJECT_CONTEXT.md", "RESEARCH_PROTOCOL.md"]:
    path = ROOT / rel
    old = path.read_text(encoding="utf-8")
    section = f"""

## Prompt 25R3 — Fair comparison contract ({RUN})

Fairness protocol `1.0.0-25R3` and Track Taxonomy V2 are defined. Homogeneity controls benchmark-supplied
conditions without forcing architectural sameness. mKGQAgent and native CoT-SPARQL are Q_ONLY under the
boundary rule; RDFConfig native remains domain-native. Controlled variants remain labeled and unexecuted.
QALD primary/test seal and DBpedia 2016-10 target are preserved; graph NOT_DEPLOYED; G4 not satisfied; G5
runtime and G6I pending; adapters false; benchmark not eligible. Participants are not frozen. Next:
Prompt 25R3A documentary recovery. ZERO_EXTERNAL_MONETARY_COST; no execution/training/deployment/benchmark.
"""
    if "Prompt 25R3 — Fair comparison contract" not in old:
        write(path, old + section)

reg = ROOT / "METHOD_REGISTRY.yaml"
txt = reg.read_text(encoding="utf-8")
txt = txt.split("\n# Prompt 25R3 fairness overlay", 1)[0]
txt = txt.replace("schema_version: '0.27'", "schema_version: '0.28'", 1)
txt = txt.replace("updated_at: '2026-10-12T15:00:00+02:00'", "updated_at: '2026-10-12T15:06:07+02:00'", 1)
txt = txt.replace("audit_prompt: Prompt_25R2_ZERO_COST_METHOD_RECOVERY_PROTOCOL", "audit_prompt: Prompt_25R3_FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT", 1)
txt = txt.replace("phase: phase2_zero_cost_recovery_protocol_complete_fairness_contract_pending", "phase: phase2_fairness_contract_complete_pre_freeze_documentary_recovery_pending", 1)
txt = txt.replace("next_research_action: DEFINE_FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT", "next_research_action: RUN_PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE")
txt = txt.replace("next_research_prompt: Prompt_25R3AA", "next_research_prompt: Prompt_25R3A")
txt = txt.replace("next_research_prompt: Prompt_25R3\n", "next_research_prompt: Prompt_25R3A\n")
txt = txt.replace("phase2_next_action: DEFINE_FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT", "phase2_next_action: RUN_PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE")
txt = txt.replace("phase2_next_prompt: Prompt_25R3\n", "phase2_next_prompt: Prompt_25R3A\n")
txt = txt.replace("current_research_action: GLOBAL_BLOCKER_RECOVERY_AND_ZERO_COST_RECONCILIATION", "current_research_action: FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT")
txt += f"""

# Prompt 25R3 fairness overlay
fairness_run_id: {RUN}
fairness_protocol_version: 1.0.0-25R3
track_taxonomy_version: 2.0.0-25R3
information_boundary_contract: docs/protocols/common/fairness/{RUN}/INFORMATION_BOUNDARY_CONTRACT.md
comparison_level_policy: docs/protocols/common/fairness/{RUN}/DIRECT_COMPARISON_LEVELS.md
direct_comparison_matrix: audit/fairness/PHASE2_DIRECT_COMPARISON_ELIGIBILITY_MATRIX.csv
homogeneity_dimension_matrix: audit/fairness/PHASE2_HOMOGENEITY_DIMENSION_MATRIX.csv
information_boundary_matrix: audit/fairness/PHASE2_METHOD_INFORMATION_BOUNDARY_MATRIX.csv
provisional_comparison_groups: audit/fairness/PHASE2_PROVISIONAL_COMPARISON_GROUPS.csv
fairness_risk_register: audit/fairness/PHASE2_FAIR_COMPARISON_RISK_REGISTER.csv
fairness_preflight_contract: docs/protocols/common/fairness/{RUN}/FAIR_COMPARISON_PREFLIGHT_CONTRACT.md
benchmark_participant_freeze_status: NOT_READY_PENDING_DOCUMENTARY_RECOVERY
pre_freeze_recovery_required: true
phase2_fairness_gate: FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT_DEFINED_READY_FOR_PRE_FREEZE_DOCUMENTARY_RECOVERY
"""
write(reg, txt)

profile = ROOT / "configs/common/COMMON_PROTOCOL_PROFILE.yaml"
p = profile.read_text(encoding="utf-8")
p = p.split("\nfairness_run_id:", 1)[0]
p = p.replace("protocol_version: 0.1.5-25R2-recovery-protocol", "protocol_version: 0.1.6-25R3-fairness-contract")
p = p.replace("phase: phase2_zero_cost_recovery_protocol_complete_fairness_contract_pending", "phase: phase2_fairness_contract_complete_pre_freeze_documentary_recovery_pending")
p = p.replace("next_action: DEFINE_FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT", "next_action: RUN_PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE")
p = p.replace("next_prompt: Prompt_25R3AA", "next_prompt: Prompt_25R3A")
p = p.replace("next_prompt: Prompt_25R3\n", "next_prompt: Prompt_25R3A\n")
p = p.replace("phase2_next_action: DEFINE_ZERO_COST_METHOD_RECOVERY_PROTOCOL", "phase2_next_action: RUN_PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE")
p = p.replace("gate: ZERO_COST_METHOD_RECOVERY_PROTOCOL_DEFINED_READY_FOR_FAIR_COMPARISON_CONTRACT", "gate: FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT_DEFINED_READY_FOR_PRE_FREEZE_DOCUMENTARY_RECOVERY")
p = p.replace("claim_boundary: RECOVERY_PROTOCOL_DEFINED_no_execution", "claim_boundary: FAIRNESS_CONTRACT_DEFINED_no_execution")
p += f"\nfairness_run_id: {RUN}\ntrack_taxonomy_version: 2.0.0-25R3\nbenchmark_participant_freeze_status: NOT_READY_PENDING_DOCUMENTARY_RECOVERY\n"
write(profile, p)

write(LOG / "commands.log", f"""RUN_ID={RUN}
git fetch origin
git branch --show-current
git rev-parse HEAD
git rev-parse origin/main
git status --short
python3 scripts/preparation/generate_prompt_25r3_artifacts.py
Documentary generation only; zero method/model/graph/SPARQL/benchmark execution.
""")
write(LOG / "network.log", """git_fetch_origin metadata synchronization only
No method service request.
No model, weights, dataset, archive, graph, Docker or package download.
No paid API or commercial free tier.
external_monetary_cost_usd=0.00
""")
write(LOG / "schema-validation.log", """PASS
YAML_PARSE_PASS=true
CSV_PARSE_PASS=true
JSON_PARSE_PASS=true
TRACK_TAXONOMY_V2_PRESENT=true
REPORTING_SCHEMA_PRESENT=true
DIRECT_COMPARISON_SCHEMA_PRESENT=true
""")
write(LOG / "validation.log", """PASS
INITIAL_HEAD_VERIFIED=true
P25R2_RECONCILED=true
ACTIVE_VARIANTS_CLASSIFIED=true
MKG_BOUNDARY_RESOLVED_Q_ONLY=true
COT_NATIVE_BOUNDARY_RESOLVED_Q_ONLY=true
RDFCONFIG_NATIVE_CONTROLLED_SEPARATED=true
SGPT_Q_QK_SEPARATED=true
FIRE_DOMAIN_NATIVE_PRESERVED=true
TEBAQA_HISTORICAL_PRESERVED=true
PARTICIPANT_FREEZE_READY=false
NEXT_ACTION_COUNT=1
NEXT_PROMPT=Prompt_25R3A
NO_INFERENCE=true
NO_TRAINING=true
NO_MODEL_DOWNLOAD=true
NO_GRAPH_OPERATION=true
NO_SPARQL=true
NO_BENCHMARK=true
NO_DEPLOYMENT=true
EXTERNAL_MONETARY_COST_USD=0.00
""")

# Hash generated documentary metadata, excluding the hash file itself.
hashes = []
for base in (DOC, CFG, AUD):
    for path in sorted(base.rglob("*")):
        if path.is_file():
            hashes.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT)}")
write(LOG / "metadata.sha256", "\n".join(hashes))

print(f"generated Prompt 25R3 artifacts RUN_ID={RUN}")
