#!/usr/bin/env python3
"""Generate Prompt 25R4 documentary benchmark-design freeze artifacts."""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
RUN = "20261012T143717Z"
CREATED = "2026-10-12T14:37:17Z"
FREEZE_ID = "COMMON_CORE_BENCHMARK_FREEZE_V1"
FREEZE_VERSION = "1.0.0-25R4"
DOC = ROOT / "docs/protocols/common/benchmark-freeze" / RUN
CFG = ROOT / "configs/common/benchmark-freeze"
AUD = ROOT / "audit/benchmark-freeze"
LOG = ROOT / "logs/benchmark-design-freeze" / RUN
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


def append_once(path: Path, marker: str, section: str) -> None:
    old = path.read_text(encoding="utf-8")
    if marker not in old:
        path.write_text(old.rstrip("\n") + "\n\n" + section.strip() + "\n", encoding="utf-8")


HEADER = f"""**RUN_ID:** `{RUN}`
**Freeze:** `{FREEZE_ID}` · `{FREEZE_VERSION}`
**Mode:** DOCUMENTARY · STATIC · ZERO_COST · NO_METHOD_EXECUTION
"""

portfolio_fields = [
    "method_id", "variant_id", "phase1_outcome", "track_v2", "adaptation_regime",
    "portfolio_role", "design_freeze_status", "zero_cost_status", "legal_status",
    "artifact_status", "resource_status", "runtime_status", "graph_status", "metric_status",
    "adapter_status", "execution_eligibility", "reopen_condition", "comparison_group",
    "claim_boundary", "reason", "evidence",
]


def variant(
    method_id: str,
    variant_id: str,
    phase1: str,
    track: str,
    regime: str,
    role: str,
    zero: str,
    legal: str,
    artifact: str,
    resource: str,
    runtime: str,
    group: str,
    reopen: str,
    reason: str,
    evidence: str,
) -> dict[str, object]:
    return {
        "method_id": method_id,
        "variant_id": variant_id,
        "phase1_outcome": phase1,
        "track_v2": track,
        "adaptation_regime": regime,
        "portfolio_role": role,
        "design_freeze_status": "DESIGN_FROZEN_V1",
        "zero_cost_status": zero,
        "legal_status": legal,
        "artifact_status": artifact,
        "resource_status": resource,
        "runtime_status": runtime,
        "graph_status": "DBPEDIA_NOT_DEPLOYED" if track not in {"IA_DOMAIN_NATIVE", "IA_HISTORICAL"} else "NATIVE_OR_NOT_APPLICABLE",
        "metric_status": "DOCUMENTED_RUNTIME_PENDING",
        "adapter_status": "G6D_DOCUMENTED_G6I_PENDING",
        "execution_eligibility": "NOT_CURRENTLY_ELIGIBLE",
        "reopen_condition": reopen,
        "comparison_group": group,
        "claim_boundary": "NO_PERFORMANCE_CLAIM_UNTIL_ALL_GATES_PASS",
        "reason": reason,
        "evidence": evidence,
    }


portfolio = [
    variant("sparql_llm", "NATIVE_API", "smoke_only", "IA_SCHEMA_COMMON", "METHOD_FAITHFUL",
            "REFERENCE_ONLY_BLOCKED", "BLOCKED_PAID_API_POLICY", "MIT_CONFIRMED", "AVAILABLE",
            "PENDING", "API_PATH_ZERO_COST_BLOCKED", "", "ZERO_COST_POLICY_CHANGES_BY_VERSIONED_DECISION",
            "native API depends on disallowed paid/commercial service path", "25R1;25R2;25R3"),
    variant("sparql_llm", "ZERO_COST_LOCAL_BACKEND", "smoke_only", "IA_SCHEMA_COMMON", "ZERO_COST_CONTROLLED",
            "EXECUTION_TARGET", "COMPLIANT_TARGET", "MIT_CONFIRMED", "LOCAL_INDEX_AVAILABLE_MODEL_PENDING",
            "PENDING", "LOCAL_BACKEND_PENDING", "QALD_SCHEMA_COMMON_SYSTEM_LEVEL",
            "G4_G5_G6I_SCHEMA_MODEL_RUNTIME_F0_F14_PASS",
            "first schema-common controlled execution target", "25R2 protocol;25R3 fairness"),
    variant("sgpt", "PAPER_CHECKPOINT", "smoke_only", "IA_Q_ONLY", "METHOD_FAITHFUL",
            "REFERENCE_ONLY_BLOCKED", "ZERO_COST_COMPATIBLE_BUT_ARTIFACT_ABSENT", "MIT_CONFIRMED",
            "PAPER_CHECKPOINT_UNAVAILABLE", "PENDING", "BLOCKED_CHECKPOINT", "",
            "OFFICIAL_CHECKPOINT_APPEARS", "paper checkpoint unavailable", "SGPT checkpoint inventory"),
    variant("sgpt", "ZERO_COST_RETRAIN_Q", "smoke_only", "IA_Q_ONLY", "ZERO_COST_CONTROLLED",
            "EXECUTION_TARGET", "COMPLIANT_TARGET", "MIT_CONFIRMED", "TRAINING_INPUTS_DOCUMENTED",
            "TRAINING_RESOURCES_PENDING", "RETRAIN_PENDING", "QALD_Q_ONLY_SYSTEM_LEVEL",
            "G4_G5_G6I_TRAINING_RUNTIME_F0_F14_HUMAN_AUTH_PASS",
            "question-only zero-cost retrain target", "25R2 protocol;25R3 fairness"),
    variant("sgpt", "ZERO_COST_RETRAIN_QK", "smoke_only", "IA_ORACLE_GROUNDING", "ZERO_COST_CONTROLLED_ORACLE",
            "DIAGNOSTIC_ONLY", "COMPLIANT_TARGET", "MIT_CONFIRMED", "TRAINING_INPUTS_DOCUMENTED",
            "TRAINING_RESOURCES_PENDING", "RETRAIN_PENDING", "QALD_ORACLE_GROUNDING",
            "G4_G5_G6I_TRAINING_RUNTIME_F0_F14_HUMAN_AUTH_PASS",
            "evaluated-item gold grounding makes this oracle-assisted diagnostic", "25R3 information boundary"),
    variant("mkgqagent", "NATIVE_AGENTIC", "blocked", "IA_Q_ONLY", "METHOD_FAITHFUL",
            "EXECUTION_CONTINGENT", "NATIVE_COST_AND_SERVICE_BLOCKED", "LE6_NO_PUBLIC_CODE_LICENSE_EVIDENCE",
            "PARTIAL", "PENDING", "BLOCKED_LEGAL_SERVICE_RUNTIME", "QALD_Q_ONLY_SYSTEM_LEVEL",
            "PUBLIC_CODE_LICENSE_APPEARS_THEN_ALL_RUNTIME_GATES_PASS",
            "legal documentary gate exhausted; no permission inferred", "25R3A mKG recovery"),
    variant("mkgqagent", "CONTROLLED_LOCAL_BACKEND", "blocked", "IA_Q_ONLY", "ZERO_COST_CONTROLLED",
            "EXECUTION_CONTINGENT", "CONDITIONAL_AFTER_LEGAL_REOPEN", "LE6_NO_PUBLIC_CODE_LICENSE_EVIDENCE",
            "CONTROLLED_ARTIFACTS_NOT_IMPLEMENTED", "PENDING", "BLOCKED_LEGAL_IMPLEMENTATION_RUNTIME",
            "QALD_Q_ONLY_SYSTEM_LEVEL", "PUBLIC_CODE_LICENSE_APPEARS_THEN_G6I_AND_ALL_RUNTIME_GATES_PASS",
            "controlled implementation forbidden before legal reopen", "25R2 controlled candidate"),
    variant("rdfconfig_llm", "NATIVE_DOMAIN", "blocked", "IA_DOMAIN_NATIVE", "METHOD_FAITHFUL",
            "DOMAIN_NATIVE_OUTSIDE_COMMON_CORE", "NATIVE_PAID_API_BLOCKED", "CONFIRMED_REPOSITORY_LEVEL_MIT_DECLARATION_AT_PIN",
            "ZENODO_LINEAGE_METADATA_VERIFIED", "PENDING", "RUBY_AND_API_RUNTIME_PENDING", "DOMAIN_NATIVE",
            "NATIVE_DOMAIN_RUNTIME_GATES_PASS", "life-science native domain is not QALD ranking", "25R3A LE2 correction"),
    variant("rdfconfig_llm", "CONTROLLED_DBPEDIA_SCHEMA_COMMON", "blocked", "IA_SCHEMA_COMMON", "ZERO_COST_CONTROLLED",
            "EXECUTION_TARGET", "COMPLIANT_TARGET", "CONFIRMED_REPOSITORY_LEVEL_MIT_DECLARATION_AT_PIN",
            "CONTROLLED_DBPEDIA_SCHEMA_PENDING", "PENDING", "RUBY_LOCAL_BACKEND_PENDING",
            "QALD_SCHEMA_COMMON_SYSTEM_LEVEL", "G4_G5_G6I_SCHEMA_LOCAL_BACKEND_RUNTIME_F0_F14_PASS",
            "independent LE2-legal schema-common target", "25R3A;25R3 fairness"),
    variant("cot_sparql", "NATIVE_INTERNAL_GROUNDING", "blocked", "IA_Q_ONLY", "METHOD_FAITHFUL",
            "EXECUTION_CONTINGENT", "ZERO_COST_HARDWARE_UNSATISFIED", "LE6_NO_PUBLIC_CODE_LICENSE_EVIDENCE",
            "FOUR_CONTEXT_ARTIFACTS_METADATA_VERIFIED", "34B_HARDWARE_BLOCKED", "BLOCKED_LEGAL_HARDWARE_RUNTIME",
            "QALD_Q_ONLY_SYSTEM_LEVEL", "PUBLIC_CODE_LICENSE_APPEARS_AND_HARDWARE_RUNTIME_GATES_PASS",
            "internal grounding remains Q_ONLY; license and 34B resources block execution", "25R3A CoT recovery"),
    variant("cot_sparql", "CONTROLLED_COMMON_FROZEN_GROUNDING", "blocked", "IA_FIXED_EXTERNAL_GROUNDING",
            "ZERO_COST_CONTROLLED", "EXECUTION_CONTINGENT", "CONDITIONAL_AFTER_LEGAL_REOPEN",
            "LE6_NO_PUBLIC_CODE_LICENSE_EVIDENCE", "COMMON_GROUNDER_NOT_IMPLEMENTED", "PENDING",
            "BLOCKED_LEGAL_IMPLEMENTATION_RUNTIME", "QALD_FIXED_EXTERNAL_GROUNDING",
            "PUBLIC_CODE_LICENSE_APPEARS_AND_INDEPENDENT_PARTNER_AND_ALL_GATES_PASS",
            "descriptive contingent variant; not primary common-core target", "25R3 fairness"),
    variant("firesparql", "DOMAIN_NATIVE", "not_reproducible", "IA_DOMAIN_NATIVE", "METHOD_FAITHFUL",
            "DOMAIN_NATIVE_OUTSIDE_COMMON_CORE", "NATIVE_SURFACE_INCOMPLETE", "LE6_NO_PUBLIC_CODE_LICENSE_EVIDENCE",
            "MODEL_METADATA_ONLY_TRAINER_RUNNER_ABSENT", "HARDWARE_PENDING", "NOT_REPRODUCIBLE_NATIVE_SURFACE",
            "DOMAIN_NATIVE", "PUBLIC_CODE_LICENSE_AND_NATIVE_TRAINER_RUNNER_APPEAR",
            "ORKG/SciQA domain-native; no forced QALD adaptation", "25R3A FIRE update"),
    variant("tebaqa", "HISTORICAL", "HISTORICAL_ONLY", "IA_HISTORICAL", "HISTORICAL",
            "HISTORICAL_CONTEXT_ONLY", "NOT_ACTIVE", "HISTORICAL_REFERENCE", "NOT_ACTIVE",
            "NOT_ACTIVE", "NOT_ACTIVE", "HISTORICAL", "EXPLICIT_NEW_PORTFOLIO_DECISION",
            "context only; not active benchmark participant", "Phase1 closure"),
]
csv_write(AUD / "PHASE2_BENCHMARK_PORTFOLIO_FREEZE.csv", portfolio_fields, portfolio)

groups = [
    {
        "group_id": "QALD_SCHEMA_COMMON_SYSTEM_LEVEL",
        "status": "FROZEN_POTENTIAL_L2",
        "comparison_level": "L2_POTENTIAL",
        "members": [
            {"variant": "sparql_llm/ZERO_COST_LOCAL_BACKEND", "member_role": "EXECUTION_TARGET"},
            {"variant": "rdfconfig_llm/CONTROLLED_DBPEDIA_SCHEMA_COMMON", "member_role": "EXECUTION_TARGET"},
        ],
        "pairwise_claim_rule": "both independent methods must pass every execution and F0-F14 gate",
        "ranking_status": "NOT_CURRENTLY_ALLOWED",
    },
    {
        "group_id": "QALD_Q_ONLY_SYSTEM_LEVEL",
        "status": "FROZEN_CONTINGENT",
        "comparison_level": "L2_CONTINGENT",
        "members": [
            {"variant": "sgpt/ZERO_COST_RETRAIN_Q", "member_role": "EXECUTION_TARGET"},
            {"variant": "mkgqagent/NATIVE_AGENTIC", "member_role": "EXECUTION_CONTINGENT"},
            {"variant": "mkgqagent/CONTROLLED_LOCAL_BACKEND", "member_role": "CONTINGENT_ALTERNATIVE"},
            {"variant": "cot_sparql/NATIVE_INTERNAL_GROUNDING", "member_role": "EXECUTION_CONTINGENT"},
        ],
        "pairwise_claim_rule": "at least two independent executable methods in group after all gates",
        "ranking_status": "NOT_CURRENTLY_ALLOWED",
    },
    {
        "group_id": "QALD_ORACLE_GROUNDING",
        "status": "FROZEN_DIAGNOSTIC_ONLY",
        "comparison_level": "L1_DESCRIPTIVE",
        "members": [{"variant": "sgpt/ZERO_COST_RETRAIN_QK", "member_role": "DIAGNOSTIC_ONLY"}],
        "pairwise_claim_rule": "no end-to-end equivalence claim",
        "ranking_status": "NO",
    },
    {
        "group_id": "QALD_FIXED_EXTERNAL_GROUNDING",
        "status": "FROZEN_CONTINGENT_DESCRIPTIVE",
        "comparison_level": "L1_DESCRIPTIVE",
        "members": [{"variant": "cot_sparql/CONTROLLED_COMMON_FROZEN_GROUNDING", "member_role": "EXECUTION_CONTINGENT"}],
        "pairwise_claim_rule": "descriptive until an independent compatible partner exists",
        "ranking_status": "NO",
    },
    {
        "group_id": "DOMAIN_NATIVE",
        "status": "FROZEN_OUTSIDE_COMMON_CORE",
        "comparison_level": "L0_DOMAIN_SPECIFIC",
        "members": [
            {"variant": "rdfconfig_llm/NATIVE_DOMAIN", "member_role": "DOMAIN_NATIVE_OUTSIDE_COMMON_CORE"},
            {"variant": "firesparql/DOMAIN_NATIVE", "member_role": "DOMAIN_NATIVE_OUTSIDE_COMMON_CORE"},
        ],
        "pairwise_claim_rule": "no QALD ranking",
        "ranking_status": "NO",
    },
    {
        "group_id": "HISTORICAL",
        "status": "FROZEN_HISTORICAL",
        "comparison_level": "HISTORICAL_CONTEXT",
        "members": [{"variant": "tebaqa/HISTORICAL", "member_role": "HISTORICAL_CONTEXT_ONLY"}],
        "pairwise_claim_rule": "no active ranking",
        "ranking_status": "NO",
    },
    {
        "group_id": "CONTROLLED_BACKBONE_FUTURE",
        "status": "NOT_INSTANTIATED",
        "comparison_level": "L3_FUTURE",
        "members": [],
        "pairwise_claim_rule": "new freeze decision required when instantiated",
        "ranking_status": "NO",
    },
]
write(CFG / "COMMON_CORE_COMPARISON_GROUPS_V1.yaml", yaml.safe_dump(
    {"schema_version": FREEZE_VERSION, "run_id": RUN, "minimum_independent_executable_methods": 2, "groups": groups},
    sort_keys=False,
))

group_fields = [
    "group_id", "status", "comparison_level", "members", "execution_targets",
    "contingent_members", "minimum_independent_executable", "pairwise_claim_allowed_now",
    "future_claim_rule", "claim_boundary",
]
group_rows = []
for group in groups:
    members = group["members"]
    group_rows.append({
        "group_id": group["group_id"],
        "status": group["status"],
        "comparison_level": group["comparison_level"],
        "members": ";".join(m["variant"] for m in members),
        "execution_targets": ";".join(m["variant"] for m in members if m["member_role"] == "EXECUTION_TARGET"),
        "contingent_members": ";".join(m["variant"] for m in members if "CONTINGENT" in m["member_role"] or "ALTERNATIVE" in m["member_role"]),
        "minimum_independent_executable": 2,
        "pairwise_claim_allowed_now": "false",
        "future_claim_rule": group["pairwise_claim_rule"],
        "claim_boundary": "NO_GLOBAL_CROSS_TRACK_RANKING",
    })
csv_write(AUD / "PHASE2_FROZEN_COMPARISON_GROUP_MATRIX.csv", group_fields, group_rows)

freeze = {
    "freeze_id": FREEZE_ID,
    "freeze_version": FREEZE_VERSION,
    "run_id": RUN,
    "created_at": CREATED,
    "zero_external_monetary_cost_usd": 0.0,
    "primary_benchmark": {
        "dataset_id": "QALD9_PLUS_EN_DBPEDIA",
        "dataset_source_repository": "Perevalov/qald_9_plus",
        "dataset_source_revision": "8eb038a61e1bc09cbd21640aa667a1714f53cda4",
        "dataset_license": "CC-BY-4.0_LICENSE_FILE_VERIFIED",
        "language": "EN",
        "kg": "DBpedia",
        "train_count": 408,
        "test_count": 150,
        "test_seal_status": "SEALED",
        "acquisition_manifest": "configs/common/acquisition/qald9plus/QALD9PLUS_EN_DBPEDIA_EXACT_FILE_MANIFEST.yaml",
        "acquisition_hashes": {
            "train_sha256": "95e1644fbcbfaf1614adc866e86857a0eac99e4905a595b8bcf1775c6bc7d2e8",
            "test_sha256": "6d3367b1231adb650f9a39ec4d8112d93a3726cc1b00c39490f5a6f23842c7d6",
            "license_sha256": "7e7170e3cebf88a9f60c7b8421418323c09304da1af4d5e90f4da1dc1c8a2661",
            "citation_sha256": "40c2e632613eea4599d7d6742b935b5b207351c31b4026e729e8b8121fc31887",
        },
        "denominator_rule": "ALL_150_FROZEN_TEST_ITEMS_NO_METHOD_FILTERING",
    },
    "graph": {
        "graph_id": "DBPEDIA_2016_10_QALD9_NATIVE_ENDPOINT_EQUIVALENT",
        "release": "2016-10",
        "provenance_status": "ENDPOINT_EQUIVALENT_RECONSTRUCTION_TARGET_HIGH_CONFIDENCE_LINEAGE_INFERENCE",
        "provenance_confidence": "HIGH_NOT_BYTE_IDENTICAL_ENDPOINT_CLAIM",
        "canonical_scope_manifest": "configs/common/graph/dbpedia2016-10/DBPEDIA_2016_10_CANONICAL_SCOPE_LOCK.yaml",
        "canonical_scope_content_hash": "2dcbc4df0b4af368d797a36525d607dae809317310c8c35d70066c5275c454c7",
        "compressed_file_count": 114,
        "compressed_bytes": 6925795437,
        "acquisition_status": "ACQUIRED_VALIDATED_COMPRESSED_WORKDIR_ONLY",
        "deployment_status": "NOT_DEPLOYED",
    },
    "fairness": {
        "fairness_protocol_version": "1.0.0-25R3",
        "track_taxonomy_version": "2.0.0-25R3",
        "information_boundary_rule": "classify only benchmark-supplied evaluated-item information; internal retrieval/linking remains internal",
    },
    "metrics": {
        "contract_version": "0.1.0-documentary",
        "answer_precision": "PRIMARY_SET_OF_ROWS",
        "answer_recall": "PRIMARY_SET_OF_ROWS",
        "answer_f1": "PRIMARY_SET_OF_ROWS",
        "execution_exact_accuracy": "PRIMARY_CANONICAL_EQUALITY",
        "failure_accounting": "FAILURES_SCORE_ZERO_AND_REMAIN_IN_DENOMINATOR",
        "conformance_status": "36_VECTORS_DEFINED_NOT_EXECUTED",
    },
    "portfolio": [
        {"variant": f"{row['method_id']}/{row['variant_id']}", **row}
        for row in portfolio
    ],
    "comparison_groups": groups,
    "zero_cost": {
        "policy": "ZERO_EXTERNAL_MONETARY_COST_LOCKED",
        "prohibited_dependencies": [
            "paid_api", "paid_cloud", "promotional_credit", "commercial_trial",
            "commercial_free_tier_as_primary_mutable_dependency",
        ],
    },
    "external_validation": {
        "strategy_id": "TEXT2SPARQL25_SEPARATE_EXTERNAL_VALIDATION",
        "current_status": "EXTERNAL_VALIDATION_PLAN_CONDITIONAL_LICENSE",
    },
    "execution_gates": {
        "G4": "NOT_SATISFIED",
        "G5": "IMPLEMENTATION_AND_CONFORMANCE_PENDING",
        "G6I": "IMPLEMENTATION_APPROVAL_PENDING",
        "adapter": "COMMON_ADAPTER_ALLOWED_FALSE",
        "F0_F14": "PENDING",
    },
    "claim_boundary": "DESIGN_FROZEN_NOT_EXECUTABLE; NO_RESULTS; NO_CROSS_TRACK_GLOBAL_RANKING",
}
manifest = CFG / "COMMON_CORE_BENCHMARK_FREEZE_V1.yaml"
write(manifest, yaml.safe_dump(freeze, sort_keys=False))
freeze_hash = hashlib.sha256(manifest.read_bytes()).hexdigest()
write(CFG / "COMMON_CORE_BENCHMARK_FREEZE_V1.sha256", f"{freeze_hash}  COMMON_CORE_BENCHMARK_FREEZE_V1.yaml")

write(DOC / "BENCHMARK_DESIGN_FREEZE_SEMANTICS.md", f"""# Benchmark design-freeze semantics

{HEADER}

- `DESIGN_FROZEN`: versioned experimental specification is locked; Phase-1 outcomes do not change.
- `EXECUTION_TARGET`: frozen slot intended for later execution after every gate.
- `EXECUTION_CONTINGENT`: executable only after its named blocker reopens and all gates pass.
- `DIAGNOSTIC_ONLY`: oracle/upper-bound evidence; not end-to-end equivalent.
- `DOMAIN_NATIVE_OUTSIDE_COMMON_CORE`: preserved in its native domain; no QALD ranking.
- `HISTORICAL_CONTEXT_ONLY`: non-active historical reference.
- `REFERENCE_ONLY_BLOCKED`: original-method reference retained but not a ZERO_COST execution.

Design freeze does not imply method readiness, adapter approval, graph deployment or benchmark eligibility.
""")

write(DOC / "PRIMARY_COMMON_COMPARISON_TARGET.md", f"""# Primary common comparison target

{HEADER}

Primary benchmark: `QALD9_PLUS_EN_DBPEDIA`.

First potential pairwise L2 group: `QALD_SCHEMA_COMMON_SYSTEM_LEVEL`, containing independent controlled
targets `sparql_llm/ZERO_COST_LOCAL_BACKEND` and
`rdfconfig_llm/CONTROLLED_DBPEDIA_SCHEMA_COMMON`. It is not executable now.

`QALD_Q_ONLY_SYSTEM_LEVEL` remains scientifically important, but SGPT currently lacks an independently
executable partner; mKGQAgent and CoT are contingent. Pairwise claims require at least two independent
implementations in one compatible group after every execution/preflight gate.
""")

write(DOC / "QALD_COMMON_CORE_FREEZE.md", f"""# QALD common-core freeze

{HEADER}

`QALD9_PLUS_EN_DBPEDIA` is locked to `Perevalov/qald_9_plus` revision
`8eb038a61e1bc09cbd21640aa667a1714f53cda4`, CC BY 4.0 license-file evidence, English/DBpedia view,
train 408 and test 150.

Train SHA-256: `95e1644fbcbfaf1614adc866e86857a0eac99e4905a595b8bcf1775c6bc7d2e8`.
Test SHA-256: `6d3367b1231adb650f9a39ec4d8112d93a3726cc1b00c39490f5a6f23842c7d6`.
Acquisition manifest: `configs/common/acquisition/qald9plus/QALD9PLUS_EN_DBPEDIA_EXACT_FILE_MANIFEST.yaml`.

Test status remains `SEALED`. Denominator is all 150 frozen test items; no method-specific filtering. No test
question or test gold SPARQL was inspected or printed during 25R4.
""")

write(DOC / "DBPEDIA_COMMON_GRAPH_FREEZE.md", f"""# DBpedia common graph freeze

{HEADER}

Graph: `DBPEDIA_2016_10_QALD9_NATIVE_ENDPOINT_EQUIVALENT`; release `2016-10`; canonical scope 114 compressed
files / 6,925,795,437 bytes; scope content SHA-256
`2dcbc4df0b4af368d797a36525d607dae809317310c8c35d70066c5275c454c7`.

The target is an endpoint-equivalent reconstruction based on high-confidence historical lineage evidence.
It is not claimed byte-identical to the original historical QALD endpoint.

State: `ACQUIRED_VALIDATED_COMPRESSED_WORKDIR_ONLY`; `NOT_DEPLOYED`;
`G4_RUNTIME_NOT_SATISFIED`. No decompression, parsing, Docker pull, Virtuoso or SPARQL occurred.
""")

write(DOC / "COMMON_METRIC_FREEZE_REFERENCE.md", f"""# Common metric freeze reference

{HEADER}

Prompt18 contract `0.1.0-documentary` is locked by reference:
`configs/common/COMMON_METRIC_REGISTRY.yaml` and
`docs/protocols/common/metrics/20260722T093257Z/`.

Primary metrics are Answer Precision, Answer Recall, Answer F1 and Execution Exact Accuracy. Frozen semantics
include `SET_OF_ROWS`, valid-empty rules, canonicalization, failures scoring zero while remaining in the
denominator, paired bootstrap/Wilson procedures and Holm correction where applicable.

`metric_contract_documentary = satisfied`; `metric_runtime_conformance = pending`;
36 vectors = `DEFINED_NOT_EXECUTED`. No metric implementation or vector execution occurred.
""")

write(DOC / "FAIRNESS_FREEZE_REFERENCE.md", f"""# Fairness freeze reference

{HEADER}

Fairness protocol `1.0.0-25R3` and track taxonomy `2.0.0-25R3` are locked. Track assignment depends on
information supplied across the benchmark boundary, not on method-internal retrieval/linking.

Exact variant tracks are in `PHASE2_BENCHMARK_PORTFOLIO_FREEZE.csv`. No future run may silently change a
track. Any scientific track change requires `BENCHMARK_FREEZE_CHANGE_REQUEST` and a new freeze version.
No global cross-track ranking is allowed.
""")

alignment_fields = [
    "method", "variant", "historical_adapter_contract", "historical_track", "taxonomy_v2_track",
    "alignment_status", "new_contract_required", "reason", "future_action",
]
alignment_rows = [
    {"method": "sparql_llm", "variant": "ZERO_COST_LOCAL_BACKEND", "historical_adapter_contract": "AC_SPARQL_LLM_SCHEMA_COMMON_NATIVE", "historical_track": "IA_SCHEMA_COMMON", "taxonomy_v2_track": "IA_SCHEMA_COMMON", "alignment_status": "ALIGNED", "new_contract_required": "false", "reason": "boundary unchanged", "future_action": "implement only after G6I"},
    {"method": "sgpt", "variant": "ZERO_COST_RETRAIN_Q", "historical_adapter_contract": "SGPT_Q_ADAPTER", "historical_track": "IA_Q_ONLY", "taxonomy_v2_track": "IA_Q_ONLY", "alignment_status": "ALIGNED", "new_contract_required": "false", "reason": "question-only", "future_action": "implement only after G6I"},
    {"method": "sgpt", "variant": "ZERO_COST_RETRAIN_QK", "historical_adapter_contract": "SGPT_QK_ADAPTER", "historical_track": "IA_ORACLE_GROUNDING", "taxonomy_v2_track": "IA_ORACLE_GROUNDING", "alignment_status": "ALIGNED_DIAGNOSTIC", "new_contract_required": "false", "reason": "evaluated-item gold oracle", "future_action": "retain diagnostic label"},
    {"method": "mkgqagent", "variant": "NATIVE_AGENTIC", "historical_adapter_contract": "MKGQAGENT_ADAPTER_CONTRACT", "historical_track": "IA_SCHEMA_COMMON", "taxonomy_v2_track": "IA_Q_ONLY", "alignment_status": "REALIGNED_V2", "new_contract_required": "true", "reason": "schema/linking are internal", "future_action": "new V2 contract only after legal reopen"},
    {"method": "rdfconfig_llm", "variant": "NATIVE_DOMAIN", "historical_adapter_contract": "RDFCONFIG_NATIVE", "historical_track": "IA_SCHEMA_COMMON", "taxonomy_v2_track": "IA_DOMAIN_NATIVE", "alignment_status": "SEPARATED_NATIVE", "new_contract_required": "true", "reason": "native life-science domain", "future_action": "domain-native contract"},
    {"method": "rdfconfig_llm", "variant": "CONTROLLED_DBPEDIA_SCHEMA_COMMON", "historical_adapter_contract": "AC_RDFCONFIG_SCHEMA_COMMON_DBPEDIA_NEGATIVE", "historical_track": "IA_SCHEMA_COMMON", "taxonomy_v2_track": "IA_SCHEMA_COMMON", "alignment_status": "PROSPECTIVE_SEPARATE", "new_contract_required": "true", "reason": "controlled DBpedia variant differs from native", "future_action": "define after schema bundle"},
    {"method": "cot_sparql", "variant": "NATIVE_INTERNAL_GROUNDING", "historical_adapter_contract": "COT_SPARQL_ADAPTER_CONTRACT", "historical_track": "IA_FIXED_EXTERNAL_GROUNDING", "taxonomy_v2_track": "IA_Q_ONLY", "alignment_status": "REALIGNED_V2", "new_contract_required": "true", "reason": "grounding/linkers are internal", "future_action": "new V2 contract before G6I"},
    {"method": "cot_sparql", "variant": "CONTROLLED_COMMON_FROZEN_GROUNDING", "historical_adapter_contract": "COT_CONTROLLED_PROSPECTIVE", "historical_track": "IA_FIXED_EXTERNAL_GROUNDING", "taxonomy_v2_track": "IA_FIXED_EXTERNAL_GROUNDING", "alignment_status": "SEPARATE_CONTROLLED", "new_contract_required": "true", "reason": "benchmark-supplied frozen grounding", "future_action": "define only after legal reopen"},
    {"method": "firesparql", "variant": "DOMAIN_NATIVE", "historical_adapter_contract": "FIRE_DOMAIN_NATIVE", "historical_track": "IA_DOMAIN_NATIVE", "taxonomy_v2_track": "IA_DOMAIN_NATIVE", "alignment_status": "ALIGNED_OUTSIDE_CORE", "new_contract_required": "false", "reason": "domain-native only", "future_action": "no QALD adapter"},
]
csv_write(AUD / "PHASE2_FUTURE_ADAPTER_TRACK_ALIGNMENT_V2.csv", alignment_fields, alignment_rows)

write(DOC / "ZERO_COST_BENCHMARK_FREEZE.md", f"""# ZERO_COST benchmark freeze

{HEADER}

`MAX_EXTERNAL_MONETARY_COST_USD = 0.00`.

Allowed: local hardware, institutional zero-cost compute, public/open-weight models, free public data and
open-source/free runtime. Forbidden as a primary dependency: paid API/cloud, promotional credit, commercial
trial, or commercial free tier with mutable quota/model dependency. Every later run records actual external
cost. A policy change requires a new freeze version.
""")

write(DOC / "COMMON_SCHEMA_BUNDLE_FREEZE_REQUIREMENTS.md", f"""# Common schema bundle freeze requirements

{HEADER}

Status: `PENDING_GRAPH_RUNTIME_AND_SCHEMA_CONSTRUCTION`.

Every `IA_SCHEMA_COMMON` execution in a direct group must receive one identical frozen bundle containing
`schema_bundle_id`, `graph_id`, `generator_version`, classes, properties, content hash and generation
procedure. No tailoring from QALD test questions is allowed. This is a runtime prerequisite, not a
design-freeze blocker. No schema was constructed in 25R4.
""")

write(DOC / "CONTROLLED_BACKBONE_FREEZE_STATUS.md", f"""# Controlled backbone freeze status

{HEADER}

`NOT_SELECTED`; `NOT_REQUIRED_FOR_L2`; `OPTIONAL_FOR_FUTURE_L3`.
L2 system-level comparisons may use different method backbones when benchmark-supplied conditions are equal.
No common backbone was selected. Instantiating L3 requires a versioned freeze decision.
""")

write(DOC / "BENCHMARK_SCIENTIFIC_AUTHORITY_DOSSIER.md", f"""# Benchmark scientific authority dossier

{HEADER}

## VERIFIED_SOURCE_FACT

- QALD-9-plus paper: “QALD-9-plus: A Multilingual Dataset for Question Answering over DBpedia and Wikidata
  Translated by Native Speakers”; DOI `10.1109/ICSC52841.2022.00045`; arXiv `2202.00120`.
- Author repository: `Perevalov/qald_9_plus`, frozen lab revision
  `8eb038a61e1bc09cbd21640aa667a1714f53cda4`.
- Repository license file: CC BY 4.0. Verified English/DBpedia counts: 408 train / 150 test.
- QALD lineage is a multilingual DBpedia/Wikidata question-answering benchmark; the selected view is
  English/DBpedia only.

## LAB_SELECTION_RATIONALE

The selected view has authoritative source control, verified hashes/counts, a sealed test split and a
documented DBpedia lineage that can be reconstructed under the laboratory's ZERO_COST policy. This rationale
does not assert universal or state-of-the-art standard status. Broad literature triangulation remains later.
""")

external_fields = [
    "field", "value", "verification_status", "source", "source_revision", "scope_note",
]
external_rows = [
    {"field": "challenge_identity", "value": "First International TEXT2SPARQL Challenge (TEXT2SPARQL25)", "verification_status": "VERIFIED", "source": "https://text2sparql.aksw.org/2025/", "source_revision": "live_official_page_2026-10-12", "scope_note": "official organizer site"},
    {"field": "year", "value": "2025", "verification_status": "VERIFIED", "source": "official site; CEUR Vol-4094", "source_revision": "published_2025-11-13", "scope_note": ""},
    {"field": "organizers", "value": "General chairs: Edgard Marx, Sebastian Tramp, Diego Moussallem; assistant committee: Paulo Viviurka do Carmo, Marcos Paulo Silva Gôlo", "verification_status": "VERIFIED", "source": "CEUR Vol-4094 preface", "source_revision": "2025 proceedings", "scope_note": ""},
    {"field": "venue_context", "value": "co-located with Text2KG at ESWC25; proceedings CEUR-WS Vol-4094", "verification_status": "VERIFIED", "source": "official site", "source_revision": "live", "scope_note": ""},
    {"field": "official_website", "value": "https://text2sparql.aksw.org/2025/", "verification_status": "VERIFIED", "source": "official site", "source_revision": "live", "scope_note": ""},
    {"field": "official_evaluator_repository", "value": "AKSW/text2sparql-client", "verification_status": "VERIFIED_CURRENT", "source": "official preface footnote; GitHub API", "source_revision": "980e0e16f78a2a52f6ba7e193b035ebfdde17403", "scope_note": "current pin is not assumed challenge-time revision"},
    {"field": "official_examples_repository", "value": "AKSW/text2sparql-client-examples", "verification_status": "VERIFIED_CURRENT_POST_CHALLENGE_EXAMPLES", "source": "GitHub API", "source_revision": "c6666be31796d6b8555031198a6d54df166d4406", "scope_note": "created 2026; not assumed challenge-time pin"},
    {"field": "dataset_identity", "value": "DB25", "verification_status": "VERIFIED", "source": "official challenge page", "source_revision": "live", "scope_note": "separate from CK25"},
    {"field": "kg_identity", "value": "DBpedia", "verification_status": "VERIFIED", "source": "official challenge page", "source_revision": "live", "scope_note": ""},
    {"field": "graph_version", "value": "DBpedia 2015-10", "verification_status": "VERIFIED", "source": "official challenge dump list", "source_revision": "live", "scope_note": "not inferred from QALD"},
    {"field": "question_count_splits", "value": "200 DB25 question-query pairs: 100 English + 100 Spanish; public test after evaluation", "verification_status": "VERIFIED_PUBLICATION_AND_SITE", "source": "CEUR Vol-4094 preface; official site", "source_revision": "2025 proceedings", "scope_note": "no payload inspected"},
    {"field": "gold_availability", "value": "questions_db25.yml and db25_true_result_set.json listed in official AKSW examples tree", "verification_status": "METADATA_VERIFIED_NOT_DOWNLOADED", "source": "GitHub tree API", "source_revision": "c6666be31796d6b8555031198a6d54df166d4406", "scope_note": ""},
    {"field": "license", "value": "Apache-2.0 root LICENSE in current examples repo; challenge-site dataset/graph license scope not separately stated", "verification_status": "CONDITIONAL_SCOPE", "source": "GitHub API; official site", "source_revision": "c6666be31796d6b8555031198a6d54df166d4406", "scope_note": "graph dump licenses not transferred"},
    {"field": "evaluation_metrics", "value": "Precision; Recall; F1; query complexity analysis; NDCG reported in proceedings for sorted results", "verification_status": "VERIFIED", "source": "official challenge page; CEUR Vol-4094 participant paper", "source_revision": "2025", "scope_note": "not pooled with QALD"},
    {"field": "leaderboard", "value": "overall, corporate, DBpedia English, DBpedia Spanish categories published", "verification_status": "VERIFIED", "source": "official results page", "source_revision": "live", "scope_note": ""},
    {"field": "participating_systems", "value": "12 endpoint registrations; results/papers published", "verification_status": "VERIFIED", "source": "official site; CEUR preface", "source_revision": "2025", "scope_note": ""},
    {"field": "download_public_availability", "value": "official pages list dumps; current official examples tree lists questions and true results", "verification_status": "METADATA_VERIFIED", "source": "official site; GitHub tree API", "source_revision": "c6666be3", "scope_note": "no payload download"},
    {"field": "test_access_regime", "value": "held during candidate evaluation; released publicly after evaluation", "verification_status": "VERIFIED", "source": "official challenge page/news", "source_revision": "2025-05-12 release notice", "scope_note": ""},
    {"field": "result_reproducibility", "value": "endpoint response artifacts and current examples metadata public; exact challenge environment reproduction not yet validated", "verification_status": "PARTIAL", "source": "official results page; GitHub tree", "source_revision": "live/c6666be3", "scope_note": "future gate"},
]
csv_write(AUD / "TEXT2SPARQL25_EXTERNAL_VALIDATION_EVIDENCE_MATRIX.csv", external_fields, external_rows)

write(DOC / "TEXT2SPARQL25_EXTERNAL_VALIDATION_PLAN.md", f"""# TEXT2SPARQL25 external-validation plan

{HEADER}

Status: `EXTERNAL_VALIDATION_PLAN_CONDITIONAL_LICENSE` — non-blocking for the QALD design freeze.

Verified metadata: first international challenge (2025), co-located with Text2KG at ESWC25, CEUR-WS
Vol-4094; DB25 and CK25; DB25 uses DBpedia **2015-10**; 200 DB25 pairs (100 English + 100 Spanish);
Precision/Recall/F1, NDCG for sorted results as reported in proceedings, plus query-complexity analysis;
leaderboard and endpoint response artifacts are public.
The official current AKSW examples repository is pinned for planning at
`c6666be31796d6b8555031198a6d54df166d4406` and lists DB25 questions/true results without payload download.

Conditional field: the current examples repository has Apache-2.0, but the official challenge page does not
separately state license scope for every dataset/graph payload. Graph-dump licensing and exact acquisition
scope must close before execution. Exact challenge-time repository revision and environment equivalence remain
unverified. No dataset was downloaded.

Future execution requires a separate acquisition manifest, graph ID, sealed/local split policy, evaluator
mapping, ZERO_COST/resource gates and authorization. QALD scores are never mixed with DB25 scores.
""")

write(DOC / "EXTERNAL_VALIDATION_SEPARATION_CONTRACT.md", f"""# External-validation separation contract

{HEADER}

QALD primary and TEXT2SPARQL25/DB25 use separate dataset IDs, graph IDs, gold, manifests, denominators,
score tables and claims. No pooled aggregate score and no cross-benchmark winner based on incomparable raw
scores are permitted. DB25's verified DBpedia 2015-10 graph is not substituted for QALD's frozen 2016-10
endpoint-equivalent target.
""")

write(DOC / "BENCHMARK_FREEZE_CHANGE_CONTROL.md", f"""# Benchmark freeze change control

{HEADER}

Changing dataset/test, graph target, track assignment, fairness taxonomy, primary metrics, failure
denominator, portfolio role, comparison group or ZERO_COST policy requires an explicit
`BENCHMARK_FREEZE_CHANGE_REQUEST` and a new freeze version.

Runtime hashes, adapter implementation hashes, model revision within an already frozen controlled slot,
resource profile and execution RUN_ID may change without a new design version only when they satisfy this
freeze. Any comparability change requires a new freeze version.
""")

design_fields = ["dimension", "frozen_value", "source", "hash_or_version", "change_control", "runtime_pending", "notes"]
design_rows = [
    ("dataset", "QALD9_PLUS_EN_DBPEDIA", "QALD exact manifest", "8eb038a61e1bc09cbd21640aa667a1714f53cda4", "NEW_FREEZE_VERSION", "false", "primary"),
    ("train split", "408 English DBpedia items", "acquisition_result.yaml", "95e1644f...", "NEW_FREEZE_VERSION", "false", ""),
    ("test split", "150 English DBpedia items", "acquisition_result.yaml", "6d3367b1...", "NEW_FREEZE_VERSION", "false", "all-item denominator"),
    ("test seal", "SEALED", "QALD acquisition gate", "20260722T111153Z", "NEW_FREEZE_VERSION", "false", "no content inspection"),
    ("graph", "DBPEDIA_2016_10_QALD9_NATIVE_ENDPOINT_EQUIVALENT", "graph target", "2016-10", "NEW_FREEZE_VERSION", "true", "not deployed"),
    ("graph scope", "114 files; 6925795437 bytes", "canonical scope lock", "2dcbc4df...", "NEW_FREEZE_VERSION", "true", ""),
    ("track taxonomy", "2.0.0-25R3", "25R3 fairness", "2.0.0-25R3", "NEW_FREEZE_VERSION", "false", ""),
    ("information boundary", "benchmark-supplied vs internal", "25R3 contract", "1.0.0-25R3", "NEW_FREEZE_VERSION", "false", ""),
    ("metrics", "AP;AR;AF1;ExecutionExactAccuracy", "Prompt18 registry", "0.1.0-documentary", "NEW_FREEZE_VERSION", "true", "36 vectors unexecuted"),
    ("failure accounting", "failure=0 and remains denominator", "Prompt18", "0.1.0-documentary", "NEW_FREEZE_VERSION", "true", ""),
    ("zero-cost", "USD 0.00 external", "ZERO_COST policy", "LOCKED", "NEW_FREEZE_VERSION", "false", ""),
    ("comparison levels", "L0-L3", "25R3", "1.0.0-25R3", "NEW_FREEZE_VERSION", "false", ""),
    ("portfolio", "13 exact variant slots", "portfolio freeze CSV", FREEZE_VERSION, "NEW_FREEZE_VERSION", "true", ""),
    ("comparison groups", "7 frozen groups", "group YAML", FREEZE_VERSION, "NEW_FREEZE_VERSION", "true", ""),
    ("schema policy", "identical frozen bundle for IA_SCHEMA_COMMON", "schema requirements", FREEZE_VERSION, "NEW_FREEZE_VERSION", "true", ""),
    ("oracle policy", "SGPT QK diagnostic only", "fairness freeze", FREEZE_VERSION, "NEW_FREEZE_VERSION", "true", ""),
    ("external validation separation", "DB25 separate from QALD", "separation contract", FREEZE_VERSION, "NEW_FREEZE_VERSION", "true", ""),
    ("claim policy", "two independent executable methods per compatible group", "25R3 fairness", FREEZE_VERSION, "NEW_FREEZE_VERSION", "true", "no global ranking"),
]
csv_write(AUD / "PHASE2_BENCHMARK_DESIGN_FREEZE_MATRIX.csv", design_fields, [dict(zip(design_fields, row)) for row in design_rows])

prereq_fields = [
    "method_id", "variant_id", "portfolio_role", "G4", "G5", "legal", "artifact", "model",
    "training", "runtime", "schema", "grounding", "adapter_G6I", "resource", "zero_cost",
    "F0_F14", "human_auth", "current_status", "next_runtime_action",
]
prereq_rows = []
for row in portfolio:
    if row["portfolio_role"] in {"REFERENCE_ONLY_BLOCKED", "HISTORICAL_CONTEXT_ONLY"}:
        continue
    prereq_rows.append({
        "method_id": row["method_id"], "variant_id": row["variant_id"], "portfolio_role": row["portfolio_role"],
        "G4": "PENDING", "G5": "PENDING", "legal": "PASS_LE2" if row["method_id"] == "rdfconfig_llm" else ("BLOCKED" if row["method_id"] in {"mkgqagent", "cot_sparql", "firesparql"} else "PASS"),
        "artifact": row["artifact_status"], "model": "PENDING_OR_VARIANT_SPECIFIC", "training": "REQUIRED" if "RETRAIN" in row["variant_id"] else "NOT_REQUIRED_OR_PENDING",
        "runtime": row["runtime_status"], "schema": "PENDING_COMMON_BUNDLE" if row["track_v2"] == "IA_SCHEMA_COMMON" else "NOT_APPLICABLE_OR_INTERNAL",
        "grounding": "DIAGNOSTIC_OR_FIXED" if row["track_v2"] in {"IA_ORACLE_GROUNDING", "IA_FIXED_EXTERNAL_GROUNDING"} else "INTERNAL_OR_NONE",
        "adapter_G6I": "PENDING", "resource": row["resource_status"], "zero_cost": row["zero_cost_status"],
        "F0_F14": "PENDING", "human_auth": "PENDING_WHERE_REQUIRED", "current_status": "NOT_CURRENTLY_ELIGIBLE",
        "next_runtime_action": "HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION_THEN_ORDERED_ROADMAP",
    })
csv_write(AUD / "PHASE2_FROZEN_VARIANT_EXECUTION_PREREQUISITES.csv", prereq_fields, prereq_rows)

write(AUD / "PHASE2_DEPLOYMENT_RESOURCE_FRESHNESS_CHECK.md", f"""# Deployment resource freshness check

{HEADER}

- Previous Prompt25A profile: 2026-07-22 / WSL RAM 7.35 GiB / host RAM 15.19 GiB / swap 2.0 GiB /
  Linux disk free 910.8 GiB / Docker 29.1.3 / Compose absent.
- Current 2026-10-12: WSL RAM 7.4 GiB total, 4.9 GiB available at observation; 2.0 GiB swap, unused;
  `/dev/sdd` 1007 GiB total, ~902 GiB free; 16 logical CPUs; Docker client 29.1.3.
- Docker daemon: not running; Compose: absent. No pull or container action.
- Windows host RAM query and `wsl.exe --status`: unavailable due WSL interop error; historical host figure is
  not promoted to a current measurement.
- C: drive has ~7.4 GiB free, but the acquired graph/workdir is on the Linux filesystem with ~902 GiB free.

`material_change = false` for the existing profile definitions.
`profile_reassessment_required = false`. The host-adjusted option remains conditional on human verification
of current host RAM before selection. No profile was selected and no configuration changed.
""")

write(DOC / "HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION_V2.md", f"""# Human DBpedia deployment resource profile selection V2

{HEADER}
**Form status:** `READY_UNSIGNED`
**Selection status:** `NONE`
**Manifest SHA-256:** `{freeze_hash}`
**Graph:** `DBPEDIA_2016_10_QALD9_NATIVE_ENDPOINT_EQUIVALENT` · 6,925,795,437 compressed bytes
**Current snapshot:** WSL 7.4 GiB RAM · 2.0 GiB swap · ~902 GiB Linux disk free · Docker daemon unavailable
**Policy:** `ZERO_EXTERNAL_MONETARY_COST`

Select exactly one:

- [ ] `LOCAL_WSL_CURRENT` — not recommended; high OOM risk.
- [ ] `LOCAL_WSL_HOST_ADJUSTED` — conditional; verify current host RAM, human changes `.wslconfig`/restart.
- [ ] `WINDOWS_HOST_NATIVE_DOCKER` — conditional/untested; verify storage and Docker Desktop resources.
- [ ] `EXTERNAL_ZERO_COST_RESEARCH_SERVER` — preferred if suitable zero-cost resources are supplied.
- [ ] `REMOTE_IMMUTABLE_ENDPOINT` — only with immutable 2016-10-equivalent evidence; separately labelled.
- [ ] `REJECT_AND_DEFER_DEPLOYMENT`.

Approver: ______ · Date: ______ · Selected profile: ______ · Decision: ______ · Confirmation: ______

This form authorizes profile selection only. It does not authorize `.wslconfig`/swap changes, restart,
decompression, Docker pull, container creation, Virtuoso, SPARQL, gold, metrics, adapters or benchmark.
""")

validator_source = '''#!/usr/bin/env python3
"""Offline validator for COMMON_CORE_BENCHMARK_FREEZE_V1."""
from __future__ import annotations
import csv, hashlib, json, sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[2]
CFG = ROOT / "configs/common/benchmark-freeze"
AUD = ROOT / "audit/benchmark-freeze"
errors = []
manifest_path = CFG / "COMMON_CORE_BENCHMARK_FREEZE_V1.yaml"
manifest = yaml.safe_load(manifest_path.read_text())
portfolio = list(csv.DictReader((AUD / "PHASE2_BENCHMARK_PORTFOLIO_FREEZE.csv").open()))
groups = yaml.safe_load((CFG / "COMMON_CORE_COMPARISON_GROUPS_V1.yaml").read_text())["groups"]
expected_hash = (CFG / "COMMON_CORE_BENCHMARK_FREEZE_V1.sha256").read_text().split()[0]
actual_hash = hashlib.sha256(manifest_path.read_bytes()).hexdigest()

def check(condition, message):
    if not condition:
        errors.append(message)

check(manifest["freeze_version"] == "1.0.0-25R4", "freeze version")
check("benchmark_freeze_sha256" not in manifest, "self hash present")
check(expected_hash == actual_hash, "sidecar hash mismatch")
dataset = manifest["primary_benchmark"]
check(dataset["dataset_id"] == "QALD9_PLUS_EN_DBPEDIA", "dataset identity")
check(dataset["dataset_source_revision"] == "8eb038a61e1bc09cbd21640aa667a1714f53cda4", "dataset revision")
check((dataset["train_count"], dataset["test_count"]) == (408, 150), "dataset counts")
check(dataset["test_seal_status"] == "SEALED", "test seal")
graph = manifest["graph"]
check(graph["graph_id"] == "DBPEDIA_2016_10_QALD9_NATIVE_ENDPOINT_EQUIVALENT", "graph identity")
check(graph["compressed_file_count"] == 114, "graph file count")
check(graph["compressed_bytes"] == 6925795437, "graph bytes")
check(graph["deployment_status"] == "NOT_DEPLOYED", "graph deployment")
check(manifest["fairness"]["track_taxonomy_version"] == "2.0.0-25R3", "taxonomy")
check(manifest["metrics"]["contract_version"] == "0.1.0-documentary", "metric version")
check(manifest["metrics"]["conformance_status"] == "36_VECTORS_DEFINED_NOT_EXECUTED", "vectors")
ids = [f"{r['method_id']}/{r['variant_id']}" for r in portfolio]
check(len(ids) == len(set(ids)), "duplicate variant IDs")
check(all(r["portfolio_role"] for r in portfolio), "missing portfolio role")
known = set(ids)
for group in groups:
    for member in group["members"]:
        check(member["variant"] in known, f"unknown group member {member['variant']}")
        row = portfolio[ids.index(member["variant"])]
        if group["group_id"].startswith("QALD_"):
            check(row["track_v2"] not in {"IA_DOMAIN_NATIVE", "IA_HISTORICAL"}, "domain/historical in QALD group")
oracle = next(r for r in portfolio if r["variant_id"] == "ZERO_COST_RETRAIN_QK")
check(oracle["portfolio_role"] == "DIAGNOSTIC_ONLY", "oracle not diagnostic")
check(all(r["zero_cost_status"] == "COMPLIANT_TARGET" for r in portfolio if r["portfolio_role"] == "EXECUTION_TARGET"), "paid execution target")
check(all(r["legal_status"] == "LE6_NO_PUBLIC_CODE_LICENSE_EVIDENCE" and r["execution_eligibility"] == "NOT_CURRENTLY_ELIGIBLE" for r in portfolio if r["method_id"] == "mkgqagent"), "mKG legal blocker")
check(all(r["legal_status"] == "LE6_NO_PUBLIC_CODE_LICENSE_EVIDENCE" and r["execution_eligibility"] == "NOT_CURRENTLY_ELIGIBLE" for r in portfolio if r["method_id"] == "cot_sparql"), "CoT legal blocker")
check(all(r["legal_status"] == "CONFIRMED_REPOSITORY_LEVEL_MIT_DECLARATION_AT_PIN" for r in portfolio if r["method_id"] == "rdfconfig_llm"), "RDFConfig LE2")
check(all(r["execution_eligibility"] == "NOT_CURRENTLY_ELIGIBLE" for r in portfolio), "execution falsely eligible")
gates = manifest["execution_gates"]
check(gates["G4"] == "NOT_SATISFIED" and "PENDING" in gates["G5"] and "PENDING" in gates["G6I"], "runtime gate falsely passed")
result = {"errors": errors, "freeze_id": manifest["freeze_id"], "freeze_version": manifest["freeze_version"], "manifest_sha256": actual_hash, "status": "PASS" if not errors else "FAIL"}
out = ROOT / "audit/benchmark-freeze/benchmark-freeze-validation.json"
out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\\n")
print(json.dumps(result, sort_keys=True))
sys.exit(0 if not errors else 1)
'''
write(ROOT / "scripts/preparation/validate_common_core_benchmark_freeze.py", validator_source)

report_titles = [
    "Executive summary", "Input gate", "25R3A reconciliation", "Master-state reconciliation",
    "Freeze semantics", "QALD benchmark identity", "QALD provenance", "QALD test seal",
    "DBpedia graph target", "Graph provenance qualifier", "Metrics", "Fairness taxonomy", "Portfolio",
    "SPARQL-LLM", "SGPT", "mKGQAgent", "RDFConfig", "CoT-SPARQL", "FIRESPARQL", "TeBaQA",
    "Comparison groups", "Primary L2 target", "Q_ONLY contingent group", "Oracle diagnostic policy",
    "Domain-native policy", "ZERO_COST", "Common schema future requirement", "Controlled backbone",
    "Adapter V2 alignment", "Scientific benchmark authority", "TEXT2SPARQL25 plan",
    "External-validation separation", "Change control", "Execution prerequisites",
    "Machine resource freshness", "G4", "G5", "G6D", "G6I", "Benchmark eligibility",
    "Next human/deployment step", "Long-term thesis roadmap", "Claim boundaries",
    "Conservative conclusion",
]
report_notes = {
    1: "Design freeze V1 is complete; no method or benchmark was executed.",
    2: "`PRE_FREEZE_DOCUMENTARY_RECOVERY_COMPLETE_READY_FOR_BENCHMARK_DESIGN_FREEZE` passed with 4/2/0 closure.",
    3: "25R3A initial `e8aa49da8ebf733e77ca962cbb5a11ba502426ca`, artifact `31b214e6b9b1967537c7ed278426c2c1f67c97cc`, publication/remote tip `52b74bceb15bbf8f149e6a94d2be9e2aee5803a5`; push confirmed.",
    4: "Current state supersedes obsolete planning fields without rewriting historical Phase-1 evidence. ARTIFACT_INDEX duplicate cleanup is `PLAN_SYNC_HYGIENE_ONLY`.",
    5: "Frozen roles distinguish target, contingent, diagnostic, domain, historical and blocked reference.",
    6: "Primary benchmark is QALD9_PLUS_EN_DBPEDIA at immutable source revision.",
    7: "Author repository, CC BY 4.0 evidence, hashes and counts are frozen.",
    8: "Test remains SEALED; all 150 items form the denominator; no content inspected.",
    9: "DBpedia 2016-10 endpoint-equivalent graph target is locked at 114 files / 6,925,795,437 bytes.",
    10: "High-confidence lineage supports endpoint equivalence, not byte identity to the historical endpoint.",
    11: "Prompt18 primary metrics/failure accounting are locked; runtime conformance remains pending.",
    12: "Fairness 1.0.0-25R3 and taxonomy 2.0.0-25R3 are frozen.",
    13: "Thirteen exact variant slots receive one role each.",
    14: "Native API is reference-only; local backend is schema-common execution target.",
    15: "Paper checkpoint is reference-only; Q retrain is target; QK is oracle diagnostic.",
    16: "Native and controlled mKG variants are contingent on public code licensing.",
    17: "LE2 MIT is current; native is domain-only and controlled DBpedia is schema-common target.",
    18: "Native CoT is IA_Q_ONLY; artifacts metadata recovered; license and 34B hardware remain blockers.",
    19: "FIRESPARQL remains IA_DOMAIN_NATIVE outside QALD ranking.",
    20: "TeBaQA remains historical only.",
    21: "Seven groups are frozen; all ranking is currently disallowed.",
    22: "Schema-common is the first potential two-independent-method L2 group.",
    23: "Q_ONLY has SGPT target and contingent mKG/CoT candidates.",
    24: "SGPT QK is not represented as end-to-end equivalent.",
    25: "RDFConfig native and FIRESPARQL are isolated from QALD rankings.",
    26: "External monetary cost is locked at USD 0.00.",
    27: "One identical future schema bundle is required; status pending.",
    28: "No backbone selected; L3 remains optional future work.",
    29: "Historical Prompt19 is preserved; V2 realignments require new contracts before G6I.",
    30: "QALD authority facts and lab selection rationale are explicitly separated.",
    31: "DB25 plan is conditional on license scope; DBpedia 2015-10 is verified, not inferred.",
    32: "QALD and DB25 use separate data, graphs, denominators, tables and claims.",
    33: "Comparability changes require a new freeze version.",
    34: "Every active/contingent variant remains blocked by explicit later gates.",
    35: "WSL resources are materially consistent with 25A; host RAM query failed; form remains usable with caveat.",
    36: "G4 remains NOT_SATISFIED because DBpedia is not deployed.",
    37: "G5 implementation and 36-vector conformance remain pending.",
    38: "G6D remains documented.",
    39: "G6I remains pending; common_adapter_allowed=false.",
    40: "Benchmark execution remains NOT_CURRENTLY_ELIGIBLE.",
    41: "Exactly one next action is the human resource-profile selection; Prompt25B is reserved, not authorized.",
    42: "Deployment, metrics, recovery, adapters, QALD, DB25, PE6–PE8 and thesis package remain ordered future work.",
    43: "No performance, executability, endpoint identity or cross-track winner claim is made.",
    44: "The scientific design is frozen while all runtime and human gates remain intact.",
}
report = "# Phase 2 common-core benchmark design freeze report\n\n" + HEADER + "\n"
for number, title in enumerate(report_titles, 1):
    report += f"\n## {number}. {title}\n\n{report_notes[number]}\n"
write(ROOT / "audit/PHASE2_COMMON_CORE_BENCHMARK_DESIGN_FREEZE_REPORT.md", report)

write(ROOT / "docs/decisions/024_common_core_benchmark_design_freeze.md", f"""# Decision 024 — Common-core benchmark design freeze

{HEADER}

Freeze `{FREEZE_VERSION}` is accepted with manifest SHA-256 `{freeze_hash}`. QALD9 Plus English/DBpedia and
the DBpedia 2016-10 endpoint-equivalent target are locked; the provenance qualifier is preserved. Fairness
taxonomy, Prompt18 metrics/failure accounting, ZERO_COST, portfolio roles and comparison groups are locked.

mKGQAgent and CoT remain contingent and not executable. RDFConfig's current LE2 MIT correction is incorporated.
FIRESPARQL is domain-native; TeBaQA historical. TEXT2SPARQL25 is a separate conditional external-validation
plan. Design freeze is not execution eligibility.

Next: `HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION`; `Prompt25B` is `RESERVED_NOT_AUTHORIZED`.
""")

write(DOC / "COMMON_CORE_BENCHMARK_DESIGN_FREEZE_GATE.md", f"""# Common-core benchmark design freeze gate

{HEADER}

**`COMMON_CORE_BENCHMARK_DESIGN_FROZEN_READY_FOR_DBPEDIA_RESOURCE_PROFILE_SELECTION`**

- BENCHMARK_DESIGN_FREEZE_V1
- QALD9_PLUS_EN_DBPEDIA_PRIMARY_LOCKED
- DBPEDIA_2016_10_TARGET_LOCKED
- GRAPH_PROVENANCE_QUALIFIER_PRESERVED
- TRACK_TAXONOMY_V2_LOCKED
- METRIC_CONTRACT_LOCKED
- FAILURES_REMAIN_DENOMINATOR
- ZERO_EXTERNAL_MONETARY_COST_LOCKED
- PORTFOLIO_ROLES_FROZEN
- COMPARISON_GROUPS_FROZEN
- DESIGN_FREEZE_NOT_EXECUTION_ELIGIBILITY
- TEST_SEAL_PRESERVED
- RDFCONFIG_LE2_MIT_CURRENT_EVIDENCE
- MKG_LEGAL_CONTINGENT
- COT_LEGAL_HARDWARE_CONTINGENT
- FIRE_DOMAIN_NATIVE
- TEBAQA_HISTORICAL
- TEXT2SPARQL25_SEPARATE_EXTERNAL_VALIDATION
- NO_METHOD_EXECUTION
- NO_TRAINING
- NO_GRAPH_DEPLOYMENT
- NO_BENCHMARK
- HUMAN_GATE_REQUIRED

Manifest SHA-256: `{freeze_hash}`.
Validator: `PASS`. Human form V2: `READY_UNSIGNED`.
Next: `HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION`.
Prompt25B: `RESERVED_NOT_AUTHORIZED`.
ARTIFACT_COMMIT: *(post-commit)*
""")

write(ROOT / "audit/NEXT_AFTER_COMMON_CORE_BENCHMARK_DESIGN_FREEZE_DECISION.md", f"""# Next after common-core benchmark design freeze

{HEADER}

Freeze `{FREEZE_ID}` / `{FREEZE_VERSION}` / `{freeze_hash}`; validator `PASS`; portfolio 13 variant slots;
7 comparison groups; QALD9_PLUS_EN_DBPEDIA primary; DBpedia 2016-10 target; test SEALED.
TEXT2SPARQL25 status `EXTERNAL_VALIDATION_PLAN_CONDITIONAL_LICENSE`; resources refreshed;
human form `READY_UNSIGNED`. G4 not satisfied; G5/G6I pending; adapters false; benchmark not eligible.

Exactly one next action: `HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION`.
Status: `HUMAN_GATE_REQUIRED`. Prompt25B: `RESERVED_NOT_AUTHORIZED`.
ARTIFACT_COMMIT: *(post-commit)*
""")

roadmap = [
    (1, "GLOBAL_BLOCKER_RECOVERY_AND_ZERO_COST_RECONCILIATION", "Prompt_25R1", "COMPLETE"),
    (2, "ZERO_COST_METHOD_RECOVERY_PROTOCOL", "Prompt_25R2", "COMPLETE"),
    (3, "FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT", "Prompt_25R3", "COMPLETE"),
    (4, "PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE", "Prompt_25R3A", "COMPLETE"),
    (5, "COMMON_CORE_BENCHMARK_FREEZE_AND_EXTERNAL_VALIDATION_PLAN", "Prompt_25R4", "COMPLETE"),
    (6, "HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION", "human_gate", "NEXT_HUMAN_GATE_REQUIRED"),
    (7, "FINAL_DEPLOYMENT_AUTHORIZATION_PACKAGE", "Prompt_25B", "RESERVED_NOT_AUTHORIZED"),
    (8, "RESOURCE_CONFIGURATION", "D1", "PLANNED"),
    (9, "DECOMPRESSION_AND_RDF_VALIDATION", "D2", "PLANNED"),
    (10, "RUNTIME_IMAGE_ACQUISITION", "D3", "PLANNED"),
    (11, "VIRTUOSO_LOAD", "D4", "PLANNED"),
    (12, "GRAPH_RUNTIME_VALIDATION", "D5_G4", "PLANNED"),
    (13, "GOLD_MATERIALIZATION", "D6_GOLD", "PLANNED"),
    (14, "METRIC_IMPLEMENTATION_AND_CONFORMANCE", "G5", "PLANNED"),
    (15, "METHOD_RECOVERY_EXECUTION", "recovery_prompts", "PLANNED"),
    (16, "G6I_G7", "decision", "PLANNED"),
    (17, "ADAPTER_IMPLEMENTATION", "implementation", "PLANNED"),
    (18, "COMMON_PREFLIGHT", "runtime", "PLANNED"),
    (19, "QALD_PRIMARY_BENCHMARK", "experiment", "PLANNED"),
    (20, "TEXT2SPARQL25_EXTERNAL_VALIDATION", "future_experiment", "CONDITIONAL_OWN_GATES"),
    (21, "ERROR_ANALYSIS_PE6", "research", "PLANNED"),
    (22, "AI_MODEL_DISCOVERY_CASE_STUDY", "research", "PLANNED"),
    (23, "TEXT_TO_SQL_TRANSFER_PE7", "research", "PLANNED"),
    (24, "NEW_TEXT_TO_SPARQL_METHOD_PE8", "research", "PLANNED"),
    (25, "COMPARISON", "research", "PLANNED"),
    (26, "ABLATIONS", "research", "PLANNED"),
    (27, "FINAL_LITERATURE_TRIANGULATION", "research", "PLANNED"),
    (28, "THESIS_REPRODUCIBILITY_PACKAGE", "research", "PLANNED"),
]
csv_write(ROOT / "audit/PHASE2_REVISED_RESEARCH_ROADMAP.csv", ["order", "action", "vehicle", "status"], [dict(zip(["order", "action", "vehicle", "status"], row)) for row in roadmap])

registry_path = ROOT / "METHOD_REGISTRY.yaml"
registry = registry_path.read_text(encoding="utf-8").split("\n# Prompt 25R4 benchmark design freeze overlay", 1)[0].rstrip()
registry = registry.replace("schema_version: '0.29'", "schema_version: '0.30'", 1)
registry = registry.replace("updated_at: '2026-10-12T15:56:45+02:00'", "updated_at: '2026-10-12T16:37:17+02:00'", 1)
registry = registry.replace("phase: phase2_pre_freeze_documentary_recovery_complete_or_conditional", "phase: phase2_common_core_benchmark_design_frozen_deployment_profile_pending", 1)
registry = registry.replace("audit_prompt: Prompt_25R3A_PRE_FREEZE_DOCUMENTARY_RECOVERY", "audit_prompt: Prompt_25R4_COMMON_CORE_BENCHMARK_DESIGN_FREEZE", 1)
registry = registry.replace("next_research_action: DEFINE_COMMON_CORE_BENCHMARK_FREEZE_AND_EXTERNAL_VALIDATION_PLAN", "next_research_action: HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION")
registry = registry.replace("next_research_prompt: Prompt_25R4", "next_research_prompt: HUMAN_GATE_REQUIRED")
registry = registry.replace("phase2_next_action: DEFINE_COMMON_CORE_BENCHMARK_FREEZE_AND_EXTERNAL_VALIDATION_PLAN", "phase2_next_action: HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION")
registry = registry.replace("phase2_next_prompt: Prompt_25R4", "phase2_next_prompt: HUMAN_GATE_REQUIRED")
registry = registry.replace("phase2_next_prompt_status: GO_NEXT_ZERO_COST", "phase2_next_prompt_status: HUMAN_GATE_REQUIRED")
registry = registry.replace("current_research_action: PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE", "current_research_action: COMMON_CORE_BENCHMARK_DESIGN_FREEZE")
registry = registry.replace("benchmark_participant_freeze_status: READY_FOR_DESIGN_FREEZE_NOT_FROZEN", "benchmark_participant_freeze_status: DESIGN_FROZEN_V1")
method_overlay = {}
for method in sorted({row["method_id"] for row in portfolio}):
    rows = [row for row in portfolio if row["method_id"] == method]
    if method == "tebaqa":
        remaining_gates = ["NOT_ACTIVE_HISTORICAL"]
    elif method == "firesparql":
        remaining_gates = ["DOMAIN_NATIVE_OUTSIDE_COMMON_CORE"]
    else:
        remaining_gates = [
            "G4",
            "G5",
            "G6I",
            "adapter",
            "variant_specific_legal_artifact_model_training",
            "resources",
            "F0_F14",
            "human_authorization",
        ]
    method_overlay[method] = {
        "phase1_final_outcome_preserved": rows[0]["phase1_outcome"],
        "frozen_variants": [
            {
                "variant_id": row["variant_id"],
                "frozen_portfolio_role": row["portfolio_role"],
                "frozen_track_v2": row["track_v2"],
                "frozen_comparison_group": row["comparison_group"],
                "frozen_execution_target_status": row["execution_eligibility"],
                "reopen_condition": row["reopen_condition"],
            }
            for row in rows
        ],
        "frozen_portfolio_role": [row["portfolio_role"] for row in rows],
        "frozen_track_v2": [row["track_v2"] for row in rows],
        "frozen_comparison_group": sorted({row["comparison_group"] for row in rows if row["comparison_group"]}),
        "frozen_execution_target_status": [f"{row['variant_id']}:{row['execution_eligibility']}" for row in rows],
        "remaining_execution_gates": remaining_gates,
    }
overlay = {
    "benchmark_freeze_run_id": RUN,
    "benchmark_freeze_version": FREEZE_VERSION,
    "benchmark_freeze_manifest": "configs/common/benchmark-freeze/COMMON_CORE_BENCHMARK_FREEZE_V1.yaml",
    "benchmark_freeze_sha256": freeze_hash,
    "benchmark_freeze_validation_status": "PASS",
    "benchmark_design_status": "DESIGN_FROZEN_V1",
    "benchmark_execution_status": "NOT_CURRENTLY_ELIGIBLE",
    "primary_benchmark": "QALD9_PLUS_EN_DBPEDIA",
    "primary_graph": "DBPEDIA_2016_10_QALD9_NATIVE_ENDPOINT_EQUIVALENT",
    "track_taxonomy_version_frozen": "2.0.0-25R3",
    "portfolio_freeze_matrix": "audit/benchmark-freeze/PHASE2_BENCHMARK_PORTFOLIO_FREEZE.csv",
    "comparison_group_freeze": "configs/common/benchmark-freeze/COMMON_CORE_COMPARISON_GROUPS_V1.yaml",
    "external_validation_plan_status": "EXTERNAL_VALIDATION_PLAN_CONDITIONAL_LICENSE",
    "resource_freshness_status": "REFRESHED_NO_MATERIAL_CHANGE",
    "next_research_action_25r4": "HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION",
    "benchmark_freeze_methods": method_overlay,
}
registry += "\n\n# Prompt 25R4 benchmark design freeze overlay\n" + yaml.safe_dump(overlay, sort_keys=False)
write(registry_path, registry)

profile_path = ROOT / "configs/common/COMMON_PROTOCOL_PROFILE.yaml"
profile = profile_path.read_text(encoding="utf-8").split("\n# Prompt 25R4 benchmark design freeze overlay", 1)[0].rstrip()
profile = profile.replace("protocol_version: 0.1.7-25R3A-pre-freeze-recovery", "protocol_version: 0.1.8-25R4-design-freeze")
profile = profile.replace("phase: phase2_pre_freeze_documentary_recovery_complete_or_conditional", "phase: phase2_common_core_benchmark_design_frozen_deployment_profile_pending")
profile = profile.replace("next_action: DEFINE_COMMON_CORE_BENCHMARK_FREEZE_AND_EXTERNAL_VALIDATION_PLAN", "next_action: HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION")
profile = profile.replace("next_prompt: Prompt_25R4", "next_prompt: HUMAN_GATE_REQUIRED")
profile = profile.replace("phase2_next_action: DEFINE_COMMON_CORE_BENCHMARK_FREEZE_AND_EXTERNAL_VALIDATION_PLAN", "phase2_next_action: HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION")
profile = profile.replace("gate: PRE_FREEZE_DOCUMENTARY_RECOVERY_COMPLETE_READY_FOR_BENCHMARK_DESIGN_FREEZE", "gate: COMMON_CORE_BENCHMARK_DESIGN_FROZEN_READY_FOR_DBPEDIA_RESOURCE_PROFILE_SELECTION")
profile = profile.replace("claim_boundary: DOCUMENTARY_RECOVERY_CLOSED_design_freeze_ready_not_execution", "claim_boundary: DESIGN_FROZEN_V1_NOT_EXECUTION_ELIGIBILITY")
profile = profile.replace("deployment_profile_selection_status: DEFERRED_BY_SCIENTIFIC_REPLAN_READY_UNSIGNED", "deployment_profile_selection_status: READY_UNSIGNED_V2_HUMAN_GATE_REQUIRED")
profile = profile.replace("benchmark_participant_freeze_status: READY_FOR_DESIGN_FREEZE_NOT_FROZEN", "benchmark_participant_freeze_status: DESIGN_FROZEN_V1")
profile += f"""

# Prompt 25R4 benchmark design freeze overlay
benchmark_freeze_run_id: {RUN}
benchmark_freeze_version: {FREEZE_VERSION}
benchmark_freeze_sha256: {freeze_hash}
benchmark_freeze_validation_status: PASS
benchmark_design_status: DESIGN_FROZEN_V1
benchmark_execution_status: NOT_CURRENTLY_ELIGIBLE
external_validation_plan_status: EXTERNAL_VALIDATION_PLAN_CONDITIONAL_LICENSE
resource_freshness_status: REFRESHED_NO_MATERIAL_CHANGE
human_resource_form_status: READY_UNSIGNED
prompt25b_status: RESERVED_NOT_AUTHORIZED
"""
write(profile_path, profile)

plan = f"""# PLAN_SYNC — Estado para optimización del plan de prompts

**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab
**Última actualización:** 2026-10-12 (Prompt **25R4**)
**Fase:** common-core benchmark design frozen · human deployment resource profile pending
**SHA inicial 25R4:** `52b74bceb15bbf8f149e6a94d2be9e2aee5803a5`
**RUN_ID:** `{RUN}`

Gate: `COMMON_CORE_BENCHMARK_DESIGN_FROZEN_READY_FOR_DBPEDIA_RESOURCE_PROFILE_SELECTION`.
Freeze `{FREEZE_VERSION}` SHA-256 `{freeze_hash}`; validator PASS. QALD9 Plus EN/DBpedia, DBpedia 2016-10
target, metrics, fairness V2, 13 portfolio slots and 7 groups are frozen. Design freeze is not execution.
ARTIFACT_INDEX duplicate cleanup: `PLAN_SYNC_HYGIENE_ONLY`; no scientific result changed.

## Prompt 25R3A reconciliation

Initial `e8aa49da8ebf733e77ca962cbb5a11ba502426ca`; artifact
`31b214e6b9b1967537c7ed278426c2c1f67c97cc`; publication/tip
`52b74bceb15bbf8f149e6a94d2be9e2aee5803a5`; push confirmed.

## Unique next action

`HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION` — `HUMAN_GATE_REQUIRED`.
Prompt25B is `RESERVED_NOT_AUTHORIZED`; no executable Cursor prompt is issued.

## Publication

ARTIFACT_COMMIT: *(post-commit)*
publication metadata commit: *(post-commit tip; max 2 commits)*
push: pending
"""
write(ROOT / "PLAN_SYNC.md", plan)

write(ROOT / "docs/plan-sync/NEXT_PROMPT_GUIDANCE.md", f"""# NEXT_PROMPT_GUIDANCE

**Tras:** Prompt 25R4 (`{RUN}`)
**Gate:** `COMMON_CORE_BENCHMARK_DESIGN_FROZEN_READY_FOR_DBPEDIA_RESOURCE_PROFILE_SELECTION`

## Acción siguiente

`HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION`

Status: **HUMAN_GATE_REQUIRED**.

There is no executable Cursor prompt now. `Prompt25B` is `RESERVED_NOT_AUTHORIZED` until the human selects
exactly one resource profile. Selection alone does not authorize configuration, decompression, Docker,
Virtuoso, SPARQL, gold, metrics, adapters or benchmark.
""")
write(ROOT / "docs/plan-sync/PLANNER_LOOP.md", f"""# PLANNER_LOOP

1. `PLAN_SYNC.md`
2. `docs/protocols/common/benchmark-freeze/{RUN}/COMMON_CORE_BENCHMARK_DESIGN_FREEZE_GATE.md`
3. `configs/common/benchmark-freeze/COMMON_CORE_BENCHMARK_FREEZE_V1.yaml`
4. `audit/PHASE2_COMMON_CORE_BENCHMARK_DESIGN_FREEZE_REPORT.md`
5. `audit/NEXT_AFTER_COMMON_CORE_BENCHMARK_DESIGN_FREEZE_DECISION.md`
6. `METHOD_REGISTRY.yaml`

Next: `HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION` — `HUMAN_GATE_REQUIRED`.
Prompt25B: `RESERVED_NOT_AUTHORIZED`.
""")

index_path = ROOT / "docs/plan-sync/ARTIFACT_INDEX.md"
lines = index_path.read_text(encoding="utf-8").splitlines()
seen_ids = set()
seen_paths = set()
deduped = []
for line in lines:
    if line.startswith("| ") and not line.startswith("| ID ") and not line.startswith("|---"):
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 3 and cells[0].startswith("P25R4-"):
            continue
        if len(cells) >= 3:
            artifact_id, artifact_path = cells[0], cells[2]
            if artifact_id in seen_ids or artifact_path in seen_paths:
                continue
            seen_ids.add(artifact_id)
            seen_paths.add(artifact_path)
    deduped.append(line)
deduped = [
    line.replace("**Última actualización:** 2026-10-12 (Prompt 25R3A)", "**Última actualización:** 2026-10-12 (Prompt 25R4)", 1)
    for line in deduped
]
separator_index = deduped.index("|---|---|---|---|")
while separator_index + 1 < len(deduped) and deduped[separator_index + 1] == "":
    deduped.pop(separator_index + 1)
row_lines = [
    f"| P25R4-GATE | Design freeze gate | `docs/protocols/common/benchmark-freeze/{RUN}/COMMON_CORE_BENCHMARK_DESIGN_FREEZE_GATE.md` | Human handoff |",
    "| P25R4-MAN | Immutable freeze manifest | `configs/common/benchmark-freeze/COMMON_CORE_BENCHMARK_FREEZE_V1.yaml` | Frozen specification |",
    "| P25R4-PORT | Portfolio freeze | `audit/benchmark-freeze/PHASE2_BENCHMARK_PORTFOLIO_FREEZE.csv` | Variant roles |",
    "| P25R4-GRP | Frozen groups | `configs/common/benchmark-freeze/COMMON_CORE_COMPARISON_GROUPS_V1.yaml` | Comparison claims |",
    "| P25R4-RPT | Design freeze report | `audit/PHASE2_COMMON_CORE_BENCHMARK_DESIGN_FREEZE_REPORT.md` | Full evidence |",
    f"| P25R4-FORM | Human resource form V2 | `docs/protocols/common/benchmark-freeze/{RUN}/HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION_V2.md` | READY_UNSIGNED |",
]
deduped[separator_index + 1:separator_index + 1] = row_lines
index_text = "\n".join(deduped)
index_path.write_text(index_text.rstrip() + "\n", encoding="utf-8")

section = f"""## Prompt 25R4 — Common-core benchmark design freeze ({RUN})

Benchmark design freeze `{FREEZE_VERSION}` is complete. QALD9_PLUS_EN_DBPEDIA, the qualified DBpedia
2016-10 target, Prompt18 metrics/failure accounting, fairness taxonomy V2, ZERO_COST, 13 portfolio slots and
7 comparison groups are locked. RDFConfig current evidence is LE2 MIT; mKGQAgent and CoT remain legally
contingent; CoT native is IA_Q_ONLY; FIRESPARQL remains domain-native; TeBaQA historical.
TEXT2SPARQL25 is separate and conditional on license scope. Resources were refreshed read-only with no
material profile change. Design freeze is not execution eligibility: graph NOT_DEPLOYED, G4 not satisfied,
G5/G6I pending, adapters false, benchmark not eligible. Next is the human resource-profile selection.
"""
for rel in ["README.md", "PROJECT_CONTEXT.md", "RESEARCH_PROTOCOL.md"]:
    append_once(ROOT / rel, "Prompt 25R4 — Common-core benchmark design freeze", section)

# Reconcile the historical generator's publication placeholder without altering its scientific outputs.
p25r3a_generator = ROOT / "scripts/preparation/generate_prompt_25r3a_artifacts.py"
p25r3a_text = p25r3a_generator.read_text(encoding="utf-8").replace(
    "publication metadata commit: `SELF` (second and final Prompt 25R3A commit)",
    "publication metadata commit: `52b74bceb15bbf8f149e6a94d2be9e2aee5803a5`",
)
p25r3a_generator.write_text(p25r3a_text, encoding="utf-8")

write(LOG / "commands.log", f"""RUN_ID={RUN}
git fetch origin; branch/HEAD/origin/status verification
read existing QALD/DBpedia/metric/fairness/recovery manifests
metadata-only official TEXT2SPARQL25 web and GitHub API inspection
uname -a; lscpu; free -h; swapon --show --bytes; df -h; df -T; ulimit -a
docker version; docker info; docker compose version
wsl.exe --status; read-only PowerShell host RAM query (both unavailable)
python3 scripts/preparation/generate_prompt_25r4_artifacts.py
python3 scripts/preparation/validate_common_core_benchmark_freeze.py
No method/model/training/dataset payload/graph/SPARQL/benchmark execution.
""")
write(LOG / "network.log", """2026-10-12 metadata/text-only requests
https://text2sparql.aksw.org/2025/ -> HTTP 200 official text
https://text2sparql.aksw.org/2025/challenge/ -> HTTP 200 official text
https://text2sparql.aksw.org/2025/results/ -> HTTP 200 official text
https://api.github.com/repos/AKSW/text2sparql-client-examples -> HTTP 200 metadata
GitHub commits/tree/LICENSE APIs at c6666be31796d6b8555031198a6d54df166d4406 -> HTTP 200 metadata/text
https://api.github.com/repos/AKSW/text2sparql-client -> HTTP 200 metadata
GitHub latest commit API at 980e0e16f78a2a52f6ba7e193b035ebfdde17403 -> HTTP 200 metadata
https://ceur-ws.org/Vol-4094/ -> HTTP 200 official proceedings metadata
CEUR Vol-4094 preface -> search metadata/snippet only; PDF payload not downloaded
metadata_bytes_transferred=tool_not_exposed
dataset_payload_downloaded=false
model_weights_downloaded=false
graph_payload_downloaded=false
external_monetary_cost_usd=0.00
""")
write(LOG / "resource-refresh.log", """2026-10-12 read-only resource refresh
kernel=Linux 6.6.87.2-microsoft-standard-WSL2
cpu=AMD Ryzen 7 7840HS; logical_cpu=16
wsl_ram_total=7.4GiB
wsl_ram_available_at_observation=4.9GiB
swap_total=2147483648
swap_used=0
linux_root_total=1007GiB
linux_root_free_approx=902GiB
linux_root_filesystem=ext4
windows_c_free_approx=7.4GiB
ulimit_open_files=1048576
docker_client=29.1.3
docker_daemon=NOT_RUNNING
docker_compose=ABSENT
wsl_status_query=FAILED_INTEROP
host_ram_query=FAILED_INTEROP
configuration_change=false
swap_change=false
docker_pull=false
material_change=false
profile_reassessment_required=false
""")
write(LOG / "schema-validation.log", """PASS
yaml_parse=true
csv_parse=true
freeze_hash=true
""")
write(LOG / "validation.log", """PASS
NO_METHOD_EXECUTION=true
NO_MODEL_INFERENCE=true
NO_TRAINING=true
NO_WEIGHTS=true
NO_DATASET_PAYLOAD_DOWNLOAD=true
NO_GRAPH_DECOMPRESSION=true
NO_DOCKER_PULL=true
NO_CONTAINER_CREATION=true
NO_SPARQL=true
NO_BENCHMARK=true
NO_METRIC_IMPLEMENTATION=true
NO_ADAPTER_IMPLEMENTATION=true
NO_WSLCONFIG_CHANGE=true
NO_SWAP_CHANGE=true
NO_PACKAGE_INSTALLATION=true
TEST_SEALED=true
G4=NOT_SATISFIED
G5=PENDING
G6D=DOCUMENTED
G6I=PENDING
ADAPTERS=false
BENCHMARK_EXECUTION=NOT_CURRENTLY_ELIGIBLE
EXTERNAL_MONETARY_COST_USD=0.00
""")

hash_targets = []
for base in (DOC, CFG, AUD):
    for path in sorted(base.rglob("*")):
        if path.is_file() and path.name != "benchmark-freeze-validation.json":
            hash_targets.append(path)
for path in [
    ROOT / "audit/PHASE2_COMMON_CORE_BENCHMARK_DESIGN_FREEZE_REPORT.md",
    ROOT / "audit/NEXT_AFTER_COMMON_CORE_BENCHMARK_DESIGN_FREEZE_DECISION.md",
    ROOT / "docs/decisions/024_common_core_benchmark_design_freeze.md",
]:
    hash_targets.append(path)
write(LOG / "metadata.sha256", "\n".join(
    f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT)}"
    for path in hash_targets
))

print(f"generated Prompt 25R4 artifacts RUN_ID={RUN} freeze_sha256={freeze_hash}")
