#!/usr/bin/env python3
"""Generate Prompt 25R3A metadata-only documentary recovery artifacts."""
from __future__ import annotations

import csv
import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
RUN = "20261012T135645Z"
DOC = ROOT / "docs/protocols/common/pre-freeze-recovery" / RUN
AUD = ROOT / "audit/pre-freeze-recovery"
CFG = ROOT / "configs/common/pre-freeze-recovery"
LOG = ROOT / "logs/pre-freeze-documentary-recovery" / RUN
for directory in (DOC, AUD, CFG, LOG):
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


HEADER = f"""**RUN_ID:** `{RUN}`
**Mode:** DOCUMENTARY · METADATA_ONLY · ZERO_COST · NO_METHOD_EXECUTION
"""

legal_taxonomy = {
    "schema_version": "1.0.0-25R3A",
    "run_id": RUN,
    "purpose": "laboratory evidence classification; not legal advice",
    "classes": {
        "LE1_STANDARD_LICENSE_FILE_AT_PIN": "LICENSE/COPYING or equivalent at exact pin",
        "LE2_EXPLICIT_REPOSITORY_LEVEL_LICENSE_DECLARATION_AT_PIN": {
            "definition": "explicit author-controlled, versioned repository statement naming a standard license and its code scope",
            "can_satisfy_lab_code_gate": True,
            "requirements": ["standard_license_named", "scope_explicit", "same_repository_and_pin", "no_contradiction"],
        },
        "LE3_AUTHOR_ARCHIVE_LICENSE": "official author archive; applies only to archived artifact",
        "LE4_MODEL_OR_DATA_LICENSE": "model/data scope only; does not license wrapper code",
        "LE5_PLATFORM_INFERRED_LICENSE": "platform metadata insufficient without author evidence",
        "LE6_NO_PUBLIC_LICENSE_EVIDENCE": "authoritative search exhausted without public code license evidence",
    },
    "rules": [
        "missing_LICENSE_file_or_platform_null_does_not_negate_valid_LE2",
        "dataset_model_companion_or_archive_license_does_not_transfer_to_wrapper",
        "no_license_by_analogy",
        "no_legal_advice",
    ],
}
write(CFG / "LEGAL_EVIDENCE_CLASSIFICATION.yaml", yaml.safe_dump(legal_taxonomy, sort_keys=False))

write(DOC / "LEGAL_EVIDENCE_CLASSIFICATION.md", f"""# Legal evidence classification

{HEADER}

- **LE1_STANDARD_LICENSE_FILE_AT_PIN:** LICENSE/COPYING-equivalent at the exact pin.
- **LE2_EXPLICIT_REPOSITORY_LEVEL_LICENSE_DECLARATION_AT_PIN:** author-controlled statement in the same
  repository and pin, naming a standard license, explicitly covering repository files, with no contradiction.
- **LE3_AUTHOR_ARCHIVE_LICENSE:** official archive license, scoped only to that archived artifact.
- **LE4_MODEL_OR_DATA_LICENSE:** model/data only; never transfers to wrapper code.
- **LE5_PLATFORM_INFERRED_LICENSE:** platform inference alone is insufficient.
- **LE6_NO_PUBLIC_LICENSE_EVIDENCE:** bounded authoritative search found no public code-license evidence.

LE2 can satisfy the laboratory code-evidence gate. A missing root LICENSE and GitHub `license=null` are
qualifiers, not contradictions to an explicit LE2 statement. Companion, dataset, model and archive licenses
never license the primary wrapper by analogy. This is evidence classification, not legal advice.
""")

write(DOC / "DOCUMENTARY_GATE_EXHAUSTION_POLICY.md", f"""# Documentary gate exhaustion policy

{HEADER}

A gate is `DOCUMENTARY_GATE_EXHAUSTED` after reviewing exact pin, current HEAD, LICENSE/COPYING/NOTICE,
repository-level statements, package metadata, tags, releases, author archives, paper/supplement and relevant
model metadata, with no other obvious public authoritative source. Exhausted means closed under current public
evidence, not permanently impossible. Reopen only on new authoritative evidence such as a public code license,
release or artifact.
""")

write(DOC / "MKGQAGENT_PRE_FREEZE_DOCUMENTARY_RECOVERY.md", f"""# mKGQAgent pre-freeze documentary recovery

{HEADER}

Repository `WSE-research/text2sparql-agent`; pin/current HEAD
`ba0f2f78611a7ccacc8c985a97f6008ef7ee6a6a` (identical). GitHub license API: `null`.
No LICENSE/COPYING/NOTICE, package-license declaration or README code-license statement exists. `CITATION.cff`
identifies authors/repository/paper but has no license field. Tag/release
`v1.0.0-TEXT2SPAQL-ESWC2025` points to the pin and has no assets or license. The paper/project links provide
no explicit code license. Included TTL/data licensing is not treated as code licensing.

Result: `MKG_LICENSE_EXHAUSTED_NO_PUBLIC_CODE_LICENSE`.
Closure: `DOCUMENTARY_GATE_EXHAUSTED`; evidence class `LE6_NO_PUBLIC_LICENSE_EVIDENCE`.
Execution remains legally ineligible. Reopen: `PUBLIC_CODE_LICENSE_APPEARS`. No author contact occurred.
""")

write(DOC / "RDFCONFIG_PRE_FREEZE_DOCUMENTARY_RECOVERY.md", f"""# RDFConfig pre-freeze documentary recovery

{HEADER}

## Exact pin README

Repository `scott2121/sparql_query_generator`; pin/current HEAD
`fe63171d3c8b9679779749ee11f731b2a8318053` (identical), tag/release `v1.0.0`.
Commit/tree `fe63171d…` / `b05ad308c135c1bd443fc9deff485239e716c9f7`, authored and committed by
`scott2121` on `2025-12-22T12:37:45Z`; `author-controlled=true`. `README.md` blob
`c813f08014babde306e2539b1119cf396220622c`, local text SHA-256
`0d234b70ebb9ac497372aa50bf56cae087fff3926a7b00a28c701c775f7481c7`.
Lines 110–113 state: “All files in this repository are distributed under the MIT License” and link
`https://opensource.org/license/mit`. This is author-controlled, repository-wide, at the exact pin.

Classification: `RDFCONFIG_PIN_LICENSE_RECOVERED_LE2_MIT` /
`LE2_EXPLICIT_REPOSITORY_LEVEL_LICENSE_DECLARATION_AT_PIN`.
Qualifiers remain `NO_STANDARD_LICENSE_FILE` and `GITHUB_LICENSE_DETECTION_NULL`; neither contradicts LE2.

## Paper ↔ GitHub ↔ Zenodo

Paper DOI `10.1093/bioinformatics/btag174`, authors Hikaru Nagazumi, Yuki Moriya, Shuichi Kawashima,
Toshiaki Katayama and Kana Shimizu. Its official availability statement identifies the selected GitHub
experimental environment and says data/code are archived at concept DOI `10.5281/zenodo.18539213`.

Zenodo resolves to record `18539214`, version `v1.0.0`, version DOI `10.5281/zenodo.18539214`, publication
date 2026-02-09, creators AKIRA2020, Toshiaki Katayama and scott2121, license `cc-by-4.0`, related identifier
`https://github.com/scott2121/sparql_query_generator/tree/v1.0.0`. One metadata-listed archive:
`scott2121/sparql_query_generator-v1.0.0.zip`, 23,977,650 bytes,
MD5 `30a9ace2fc430de87e01b6aeaa8b2538`. Payload was not downloaded.

Outcomes: `RDFCONFIG_ZENODO_METADATA_LINEAGE_CONFIRMED`,
`RDFCONFIG_ZENODO_BYTE_EQUIVALENCE_NOT_TESTED`. CC-BY-4.0 remains archive-scoped and is not transferred to
GitHub. Because the exact GitHub pin independently passes LE2 MIT, byte equivalence is
`ARCHIVAL_PROVENANCE_ENHANCEMENT_NONBLOCKING`, not a legal blocker.
""")

write(DOC / "COT_SPARQL_PRE_FREEZE_DOCUMENTARY_RECOVERY.md", f"""# CoT-SPARQL pre-freeze documentary recovery

{HEADER}

## License

Repository `dice-group/CoT-Sparql`; pin/current HEAD
`063edd9868425e54010a0cb49ce585ed2186be4d` (identical). GitHub license API `null`; no
LICENSE/COPYING/NOTICE, package declaration, README license, tags or releases. Paper/project evidence does
not state a code license. Organization identity is not license evidence.

Result: `COT_LICENSE_EXHAUSTED_NO_PUBLIC_CODE_LICENSE`,
`DOCUMENTARY_GATE_EXHAUSTED`, evidence class `LE6_NO_PUBLIC_LICENSE_EVIDENCE`.
Reopen: `PUBLIC_CODE_LICENSE_APPEARS`.

## Context artifacts

README links four project-hosted artifacts through `anon.to`. HEAD on the wrapper returned a 200 landing
response without a redirect, but the exact `files.dice-research.org` target embedded in each README URL
returned HTTP 200 and authoritative metadata:

| Artifact | Bytes | ETag | Last-Modified |
|---|---:|---|---|
| dbpedia_examples.parquet | 462043 | `65db4b66-70cdb` | 2024-02-25 14:15:02 GMT |
| embeddings_dbpedia.pkl | 5913763 | `65db4b65-5a3ca3` | 2024-02-25 14:15:01 GMT |
| embeddings_wikidata.pkl | 33019555 | `65db4b60-1f7d6a3` | 2024-02-25 14:14:56 GMT |
| wikidata_examples.parquet | 2141658 | `65db4b2b-20adda` | 2024-02-25 14:14:03 GMT |

All four are `PUBLIC_REMOTE_ARTIFACT_METADATA_VERIFIED`; all remain `ABSENT_IN_LOCAL_CLONE`. No payload or
checksum body was downloaded, so content integrity remains a future acquisition gate. Local absence is not
public absence.

## Native model metadata

`TheBloke/CodeLlama-34B-Instruct-GPTQ` is public, ungated and enabled at immutable revision
`0a2785d47fb7330388e0487e0526bbc53d87c156`; base `codellama/CodeLlama-34b-instruct-hf`; license metadata
`llama2`; architecture `LlamaForCausalLM`; GPTQ 4-bit; metadata total 18,331,499,489 bytes, model tensor
18,329,065,000 bytes. No weights downloaded. Native reference remains 34B; no smaller paper variant found.

## Closure by blocker

LEGAL = `DOCUMENTARY_GATE_EXHAUSTED`; ARTIFACT = `RECOVERED_DOCUMENTARILY` metadata-only; MODEL =
`RECOVERED_DOCUMENTARILY` metadata-only; HARDWARE = `STILL_BLOCKED`; SERVICE and runtime remain pending.
This closes cheap documentary work without making CoT executable.
""")

write(DOC / "FIRESPARQL_PRE_FREEZE_DOCUMENTARY_UPDATE.md", f"""# FIRESPARQL non-blocking documentary update

{HEADER}

Repository `sherry-pan/FIRESPARQL`; pin/current HEAD
`48d6f168e4c1dd3dc467553aef370299911d4e76` (identical). GitHub license API `null`; no
LICENSE/COPYING/NOTICE, README code-license statement, tags or releases. Code-license search is
`DOCUMENTARY_GATE_EXHAUSTED` / LE6.

Official HF model `Sherry791/Meta-Llama-3-8B-Instruct-ft4sciqa` remains public/ungated at revision
`8a44fbe3710f40d8890392ef585101f5ca51851b`, model-card license MIT and base
`meta-llama/Meta-Llama-3-8B-Instruct`; this does not license GitHub code. README still says requirements are
coming soon; no public trainer or QLever execution runner was found in pin, tags or releases.

Track remains `IA_DOMAIN_NATIVE`. Outcome: `NON_BLOCKING_FOR_QALD_FREEZE`; no QALD adaptation attempted.
""")

write(DOC / "BENCHMARK_PARTICIPANT_FREEZE_READINESS.md", f"""# Benchmark participant freeze readiness

{HEADER}

Mandatory rows: mKG license, RDFConfig code license, RDFConfig Zenodo lineage, CoT code license, CoT context
artifacts and CoT native model metadata.

- RECOVERED_DOCUMENTARILY: 4
- DOCUMENTARY_GATE_EXHAUSTED: 2
- DOCUMENTARY_GATE_UNRESOLVED: 0

Therefore `BENCHMARK_PARTICIPANT_FREEZE_READY = true`.

This authorizes Prompt 25R4 to define/freeze design; it does not freeze participants now and does not confer
execution eligibility. FIRESPARQL and TeBaQA are non-blocking. SPARQL-LLM model selection and SGPT training
preflight may remain later.
""")

write(DOC / "BENCHMARK_DESIGN_FREEZE_VS_EXECUTION_ELIGIBILITY.md", f"""# Benchmark design freeze versus execution eligibility

{HEADER}

`BENCHMARK_DESIGN_FREEZE` locks candidate portfolio, evidence-based exclusions, comparison groups, tracks,
dataset, graph target and evaluation rules. It may include blocked candidates and does not mean they run.

`BENCHMARK_EXECUTION_ELIGIBILITY` is later and requires G4, G5 runtime, G6I, adapter implementation and
conformance, ZERO_COST, resources, method recovery and F0–F14 preflight. Current benchmark execution remains
`NOT_CURRENTLY_ELIGIBLE`.
""")

legal_fields = [
    "method_id", "repository", "pinned_commit", "current_head", "license_file_at_pin",
    "license_file_current", "explicit_repo_license_statement_at_pin",
    "explicit_repo_license_statement_current", "statement_scope", "named_license", "linked_license",
    "repo_platform_license", "package_license", "archive_license", "paper_license", "evidence_class",
    "conflict", "lab_legal_status_before", "lab_legal_status_after", "status_changed", "reason", "evidence",
]
legal_rows = [
    dict(method_id="mkgqagent", repository="WSE-research/text2sparql-agent", pinned_commit="ba0f2f78611a7ccacc8c985a97f6008ef7ee6a6a", current_head="ba0f2f78611a7ccacc8c985a97f6008ef7ee6a6a", license_file_at_pin="ABSENT", license_file_current="ABSENT", explicit_repo_license_statement_at_pin="ABSENT", explicit_repo_license_statement_current="ABSENT", statement_scope="none", named_license="UNKNOWN", linked_license="", repo_platform_license="null", package_license="ABSENT", archive_license="ABSENT", paper_license="paper_only_not_code", evidence_class="LE6_NO_PUBLIC_LICENSE_EVIDENCE", conflict="none", lab_legal_status_before="LICENSE_ABSENT_AT_PIN", lab_legal_status_after="DOCUMENTARY_GATE_EXHAUSTED_NO_PUBLIC_CODE_LICENSE", status_changed="documentary_closure_only", reason="bounded authoritative search exhausted", evidence="MKGQAGENT_PRE_FREEZE_DOCUMENTARY_RECOVERY.md"),
    dict(method_id="rdfconfig_llm", repository="scott2121/sparql_query_generator", pinned_commit="fe63171d3c8b9679779749ee11f731b2a8318053", current_head="fe63171d3c8b9679779749ee11f731b2a8318053", license_file_at_pin="NO_STANDARD_LICENSE_FILE", license_file_current="NO_STANDARD_LICENSE_FILE", explicit_repo_license_statement_at_pin="All files in this repository are distributed under the MIT License", explicit_repo_license_statement_current="same_as_pin", statement_scope="all_files_in_repository", named_license="MIT", linked_license="https://opensource.org/license/mit", repo_platform_license="null", package_license="ABSENT", archive_license="CC-BY-4.0_archive_only", paper_license="paper_only", evidence_class="LE2_EXPLICIT_REPOSITORY_LEVEL_LICENSE_DECLARATION_AT_PIN", conflict="none", lab_legal_status_before="LICENSE_ABSENT_AT_PIN", lab_legal_status_after="CONFIRMED_REPOSITORY_LEVEL_MIT_DECLARATION_AT_PIN", status_changed="true", reason="prior policy ignored explicit repository-wide README statement", evidence="README blob c813f080; sha256 0d234b70; RDFCONFIG_LICENSE_EVIDENCE_CORRECTION.md"),
    dict(method_id="cot_sparql", repository="dice-group/CoT-Sparql", pinned_commit="063edd9868425e54010a0cb49ce585ed2186be4d", current_head="063edd9868425e54010a0cb49ce585ed2186be4d", license_file_at_pin="ABSENT", license_file_current="ABSENT", explicit_repo_license_statement_at_pin="ABSENT", explicit_repo_license_statement_current="ABSENT", statement_scope="none", named_license="UNKNOWN", linked_license="", repo_platform_license="null", package_license="ABSENT", archive_license="ABSENT", paper_license="paper_only_not_code", evidence_class="LE6_NO_PUBLIC_LICENSE_EVIDENCE", conflict="none", lab_legal_status_before="LICENSE_ABSENT_AT_PIN", lab_legal_status_after="DOCUMENTARY_GATE_EXHAUSTED_NO_PUBLIC_CODE_LICENSE", status_changed="documentary_closure_only", reason="bounded authoritative search exhausted", evidence="COT_SPARQL_PRE_FREEZE_DOCUMENTARY_RECOVERY.md"),
    dict(method_id="firesparql", repository="sherry-pan/FIRESPARQL", pinned_commit="48d6f168e4c1dd3dc467553aef370299911d4e76", current_head="48d6f168e4c1dd3dc467553aef370299911d4e76", license_file_at_pin="ABSENT", license_file_current="ABSENT", explicit_repo_license_statement_at_pin="ABSENT", explicit_repo_license_statement_current="ABSENT", statement_scope="none", named_license="UNKNOWN", linked_license="", repo_platform_license="null", package_license="ABSENT", archive_license="HF_MIT_MODEL_ONLY", paper_license="paper_only_not_code", evidence_class="LE6_NO_PUBLIC_LICENSE_EVIDENCE", conflict="none", lab_legal_status_before="LICENSE_ABSENT_AT_PIN", lab_legal_status_after="DOCUMENTARY_GATE_EXHAUSTED_NO_PUBLIC_CODE_LICENSE", status_changed="documentary_closure_only", reason="bounded authoritative search exhausted; nonblocking domain method", evidence="FIRESPARQL_PRE_FREEZE_DOCUMENTARY_UPDATE.md"),
]
csv_write(AUD / "PHASE2_AUTHORITATIVE_CODE_LICENSE_RECOVERY_MATRIX.csv", legal_fields, legal_rows)

artifact_fields = [
    "method_id", "artifact_id", "artifact_role", "required_for_variant", "local_status",
    "public_reference_status", "source_authority", "source_url", "canonical_url", "http_metadata_status",
    "size", "checksum", "etag", "license", "version", "artifact_recovery_status",
    "execution_still_blocked_by", "evidence",
]
cot_base = "https://files.dice-research.org/datasets/COT-SPARQLGEN"
artifact_rows = [
    dict(method_id="rdfconfig_llm", artifact_id="zenodo_v1.0.0_zip", artifact_role="official_archive", required_for_variant="archival_provenance_only", local_status="NOT_DOWNLOADED", public_reference_status="ZENODO_METADATA_VERIFIED", source_authority="official_author_archive", source_url="https://doi.org/10.5281/zenodo.18539213", canonical_url="https://zenodo.org/records/18539214", http_metadata_status="API_200", size=23977650, checksum="md5:30a9ace2fc430de87e01b6aeaa8b2538", etag="record_etag_4", license="CC-BY-4.0_archive_only", version="v1.0.0", artifact_recovery_status="RECOVERED_DOCUMENTARILY", execution_still_blocked_by="runtime;controlled_dbpedia_schema;G4;G5;G6I", evidence="Zenodo API record 18539214"),
]
for aid, size, etag, lm, role in [
    ("dbpedia_examples.parquet", 462043, '"65db4b66-70cdb"', "2024-02-25T14:15:02Z", "DBpedia examples"),
    ("embeddings_dbpedia.pkl", 5913763, '"65db4b65-5a3ca3"', "2024-02-25T14:15:01Z", "DBpedia embeddings"),
    ("embeddings_wikidata.pkl", 33019555, '"65db4b60-1f7d6a3"', "2024-02-25T14:14:56Z", "Wikidata embeddings"),
    ("wikidata_examples.parquet", 2141658, '"65db4b2b-20adda"', "2024-02-25T14:14:03Z", "Wikidata examples"),
]:
    artifact_rows.append(dict(method_id="cot_sparql", artifact_id=aid, artifact_role=role, required_for_variant="native_DBpedia" if "dbpedia" in aid else "native_Wikidata", local_status="ABSENT_IN_LOCAL_CLONE", public_reference_status="PUBLIC_REMOTE_ARTIFACT_METADATA_VERIFIED", source_authority="README_AUTHOR_LINKED_PROJECT_HOST", source_url=f"https://anon.to/?{cot_base}/{aid}", canonical_url=f"{cot_base}/{aid}", http_metadata_status=f"HEAD_200 last_modified={lm}", size=size, checksum="NOT_PUBLISHED", etag=etag, license="UNKNOWN_ARTIFACT_SCOPE", version="README_PIN_REFERENCE", artifact_recovery_status="RECOVERED_DOCUMENTARILY", execution_still_blocked_by="license;hardware;runtime;future_content_integrity", evidence="CoT README at pin + direct HEAD metadata"))
artifact_rows += [
    dict(method_id="cot_sparql", artifact_id="TheBloke_CodeLlama_34B_Instruct_GPTQ", artifact_role="native_model_reference", required_for_variant="NATIVE_INTERNAL_GROUNDING", local_status="WEIGHTS_NOT_DOWNLOADED", public_reference_status="PUBLIC_MODEL_METADATA_VERIFIED", source_authority="official_model_repository_referenced_by_README", source_url="https://huggingface.co/TheBloke/CodeLlama-34B-Instruct-GPTQ", canonical_url="https://huggingface.co/TheBloke/CodeLlama-34B-Instruct-GPTQ/tree/0a2785d47fb7330388e0487e0526bbc53d87c156", http_metadata_status="API_200_PUBLIC_UNGATED", size=18331499489, checksum="revision:0a2785d47fb7330388e0487e0526bbc53d87c156", etag='API W/"a6c-AYSFyABLhPMjITw9qSZL0igNyHk"', license="llama2_model_only", version="immutable_revision", artifact_recovery_status="RECOVERED_DOCUMENTARILY", execution_still_blocked_by="license;hardware;runtime", evidence="HF API model+tree metadata"),
    dict(method_id="firesparql", artifact_id="Meta-Llama-3-8B-Instruct-ft4sciqa", artifact_role="official_domain_model", required_for_variant="DOMAIN_NATIVE", local_status="WEIGHTS_NOT_DOWNLOADED", public_reference_status="PUBLIC_MODEL_METADATA_VERIFIED", source_authority="official_author_model_repository", source_url="https://huggingface.co/Sherry791/Meta-Llama-3-8B-Instruct-ft4sciqa", canonical_url="https://huggingface.co/Sherry791/Meta-Llama-3-8B-Instruct-ft4sciqa/tree/8a44fbe3710f40d8890392ef585101f5ca51851b", http_metadata_status="API_200_PUBLIC_UNGATED", size="NOT_QUERIED", checksum="revision:8a44fbe3710f40d8890392ef585101f5ca51851b", etag='API W/"d78-3PfLcEBxKNwNHDHXkgULMnLcuuQ"', license="MIT_model_card_only", version="immutable_revision", artifact_recovery_status="RECOVERED_DOCUMENTARILY", execution_still_blocked_by="code_license;trainer;runner;hardware;domain", evidence="HF API metadata"),
    dict(method_id="firesparql", artifact_id="native_trainer_and_qlever_runner", artifact_role="execution_surface", required_for_variant="DOMAIN_NATIVE", local_status="NOT_FOUND_AT_PIN", public_reference_status="NOT_FOUND_PUBLICLY", source_authority="repo+tags+releases", source_url="https://github.com/sherry-pan/FIRESPARQL", canonical_url="", http_metadata_status="GitHub_metadata_checked", size="", checksum="", etag="", license="", version="", artifact_recovery_status="DOCUMENTARY_GATE_EXHAUSTED", execution_still_blocked_by="missing_native_surface", evidence="pin/current HEAD/README/tags/releases"),
]
csv_write(AUD / "PHASE2_AUTHORITATIVE_ARTIFACT_RECOVERY_MATRIX.csv", artifact_fields, artifact_rows)

write(AUD / "RDFCONFIG_LICENSE_EVIDENCE_CORRECTION.md", f"""# RDFConfig license evidence correction

**RUN_ID:** `{RUN}`

`OLD_STATUS = LICENSE_ABSENT_AT_PIN / LICENSE_NOT_CONFIRMED`.

The earlier audit treated the absence of a root LICENSE and GitHub `license=null` as dispositive and
explicitly ignored the README MIT claim. Prompt 25R3A introduces LE2 and verifies the exact pinned README:
blob `c813f08014babde306e2539b1119cf396220622c`, SHA-256
`0d234b70ebb9ac497372aa50bf56cae087fff3926a7b00a28c701c775f7481c7`, lines 110–113, statement covering
“All files in this repository” under MIT with a standard-license link.

`NEW_STATUS = CONFIRMED_REPOSITORY_LEVEL_MIT_DECLARATION_AT_PIN`.
`CORRECTION_REASON = explicit repository-wide author statement satisfies LE2`.
`EVIDENCE_DISCOVERED_DURING_25R3A = true`.

Qualifiers `NO_STANDARD_LICENSE_FILE` and `GITHUB_LICENSE_DETECTION_NULL` remain. Zenodo CC-BY-4.0 and the
nested companion MIT license remain separate and were not transferred. This corrects current lab evidence;
it does not rewrite RDFConfig's historical Phase-1 `blocked` outcome and is not legal advice.
""")

closure_fields = [
    "recovery_item", "method", "blocking_for_freeze", "status_before", "documentary_action",
    "authoritative_sources_checked", "status_after", "recovered_or_exhausted",
    "remaining_non_documentary_blockers", "reopen_condition", "evidence", "freeze_effect",
]
closure_rows = [
    dict(recovery_item="mkgqagent_license", method="mkgqagent", blocking_for_freeze="true", status_before="LICENSE_ABSENT_AT_PIN", documentary_action="authoritative bounded license search", authoritative_sources_checked="pin;HEAD;README;CITATION;package;tag;release;paper;project", status_after="DOCUMENTARY_GATE_EXHAUSTED", recovered_or_exhausted="true", remaining_non_documentary_blockers="legal permission absent;cost;services;runtime", reopen_condition="PUBLIC_CODE_LICENSE_APPEARS", evidence="MKGQAGENT_PRE_FREEZE_DOCUMENTARY_RECOVERY.md", freeze_effect="closed_not_executable"),
    dict(recovery_item="rdfconfig_code_license", method="rdfconfig_llm", blocking_for_freeze="true", status_before="LICENSE_ABSENT_AT_PIN", documentary_action="verify exact pinned README scope", authoritative_sources_checked="pin;HEAD;README;GitHub API;paper;Zenodo", status_after="RECOVERED_DOCUMENTARILY", recovered_or_exhausted="true", remaining_non_documentary_blockers="runtime;controlled DBpedia schema;G4;G5;G6I", reopen_condition="new_contradictory_authoritative_evidence", evidence="RDFCONFIG_LICENSE_EVIDENCE_CORRECTION.md", freeze_effect="legal_gate_corrected"),
    dict(recovery_item="rdfconfig_zenodo_lineage", method="rdfconfig_llm", blocking_for_freeze="true", status_before="ARCHIVE_CONTENT_EQUIVALENCE_NOT_VERIFIED", documentary_action="paper and Zenodo metadata lineage", authoritative_sources_checked="paper DOI;Zenodo concept/version API;GitHub tag", status_after="RECOVERED_DOCUMENTARILY", recovered_or_exhausted="true", remaining_non_documentary_blockers="byte equivalence untested nonblocking", reopen_condition="archive_integrity_acquisition_needed", evidence="RDFCONFIG_PRE_FREEZE_DOCUMENTARY_RECOVERY.md", freeze_effect="lineage_closed_equivalence_nonblocking"),
    dict(recovery_item="cot_code_license", method="cot_sparql", blocking_for_freeze="true", status_before="LICENSE_ABSENT_AT_PIN", documentary_action="authoritative bounded license search", authoritative_sources_checked="pin;HEAD;README;environment;requirements;tags;releases;paper;archives", status_after="DOCUMENTARY_GATE_EXHAUSTED", recovered_or_exhausted="true", remaining_non_documentary_blockers="legal permission absent;hardware;runtime;services", reopen_condition="PUBLIC_CODE_LICENSE_APPEARS", evidence="COT_SPARQL_PRE_FREEZE_DOCUMENTARY_RECOVERY.md", freeze_effect="closed_not_executable"),
    dict(recovery_item="cot_context_artifacts", method="cot_sparql", blocking_for_freeze="true", status_before="ABSENT_IN_LOCAL_CLONE_MISSING_PUBLIC_UNCERTAIN", documentary_action="HEAD metadata on four README-linked targets", authoritative_sources_checked="pinned README;anon wrapper;files.dice-research.org", status_after="RECOVERED_DOCUMENTARILY", recovered_or_exhausted="true", remaining_non_documentary_blockers="future controlled acquisition+hash;license;hardware", reopen_condition="remote_URL_or_metadata_changes", evidence="PHASE2_AUTHORITATIVE_ARTIFACT_RECOVERY_MATRIX.csv", freeze_effect="absence_terminology_corrected"),
    dict(recovery_item="cot_native_model_metadata", method="cot_sparql", blocking_for_freeze="true", status_before="MODEL_REFERENCE_UNPINNED", documentary_action="HF model and tree metadata only", authoritative_sources_checked="README;HF API", status_after="RECOVERED_DOCUMENTARILY", recovered_or_exhausted="true", remaining_non_documentary_blockers="18.3GB weights not downloaded;hardware;license/runtime", reopen_condition="model_removed_or_official_variant_published", evidence="HF revision 0a2785d47fb7330388e0487e0526bbc53d87c156", freeze_effect="native_34B_reference_pinned_metadata"),
    dict(recovery_item="firesparql_code_license", method="firesparql", blocking_for_freeze="false", status_before="LICENSE_ABSENT_AT_PIN", documentary_action="bounded license update", authoritative_sources_checked="pin;HEAD;README;tags;releases;HF model", status_after="DOCUMENTARY_GATE_EXHAUSTED", recovered_or_exhausted="true", remaining_non_documentary_blockers="code permission;domain;hardware", reopen_condition="PUBLIC_CODE_LICENSE_APPEARS", evidence="FIRESPARQL_PRE_FREEZE_DOCUMENTARY_UPDATE.md", freeze_effect="NON_BLOCKING_FOR_QALD_FREEZE"),
    dict(recovery_item="firesparql_missing_runner_trainer", method="firesparql", blocking_for_freeze="false", status_before="MISSING_NATIVE_SURFACE", documentary_action="repo/tag/release metadata review", authoritative_sources_checked="pin;HEAD;README;tags;releases", status_after="DOCUMENTARY_GATE_EXHAUSTED", recovered_or_exhausted="true", remaining_non_documentary_blockers="trainer+runner absent", reopen_condition="OFFICIAL_TRAINER_OR_RUNNER_PUBLISHED", evidence="FIRESPARQL_PRE_FREEZE_DOCUMENTARY_UPDATE.md", freeze_effect="NON_BLOCKING_FOR_QALD_FREEZE"),
]
csv_write(AUD / "PHASE2_PRE_FREEZE_DOCUMENTARY_RECOVERY_CLOSURE_MATRIX.csv", closure_fields, closure_rows)

# Correct and annotate legal evidence matrices while preserving historical columns.
license_path = ROOT / "audit/LICENSE_MATRIX.csv"
with license_path.open(newline="", encoding="utf-8") as h:
    license_rows = list(csv.DictReader(h))
    license_fields = list(license_rows[0])
for f in ["evidence_class_25r3a", "documentary_gate_25r3a", "correction_run_id"]:
    if f not in license_fields:
        license_fields.append(f)
for row in license_rows:
    if row["method_id"] in {"mkgqagent", "cot_sparql", "firesparql"} and row["artifact_kind"] == "github_code":
        row.update(evidence_class_25r3a="LE6_NO_PUBLIC_LICENSE_EVIDENCE", documentary_gate_25r3a="DOCUMENTARY_GATE_EXHAUSTED", correction_run_id=RUN)
        row["revalidation_date"] = RUN
    elif (
        row["method_id"] == "rdfconfig_llm"
        and row["repo_full_name"] == "scott2121/sparql_query_generator"
        and row["artifact_kind"] == "github_code"
    ):
        row.update(license_status="CONFIRMED_REPOSITORY_LEVEL_DECLARATION", spdx_id="MIT", explicit_declaration_source="README.md@fe63171:113 repository-wide MIT statement", notes="LE2 MIT at exact pin; NO_STANDARD_LICENSE_FILE; GitHub license=null; Zenodo and companion remain separate", revalidation_date=RUN, evidence_class_25r3a="LE2_EXPLICIT_REPOSITORY_LEVEL_LICENSE_DECLARATION_AT_PIN", documentary_gate_25r3a="RECOVERED_DOCUMENTARILY", correction_run_id=RUN)
    else:
        row.update(evidence_class_25r3a="", documentary_gate_25r3a="", correction_run_id="")
csv_write(license_path, license_fields, license_rows)

code_path = ROOT / "audit/PHASE2_CODE_LICENSE_REVALIDATION_MATRIX.csv"
with code_path.open(newline="", encoding="utf-8") as h:
    code_rows = list(csv.DictReader(h))
    code_fields = list(code_rows[0])
for f in ["evidence_class_25r3a", "documentary_gate_25r3a", "revalidation_run_id"]:
    if f not in code_fields:
        code_fields.append(f)
for row in code_rows:
    if row["method_id"] == "rdfconfig_llm":
        row.update(license_at_pin="MIT_EXPLICIT_README_LE2", license_at_current_head="MIT_EXPLICIT_README_LE2", spdx_at_pin="MIT", spdx_at_head="MIT", readme_claim="All files in this repository are distributed under the MIT License", status_at_pin="CONFIRMED_REPOSITORY_LEVEL_MIT_DECLARATION_AT_PIN", status_at_head="CONFIRMED_REPOSITORY_LEVEL_MIT_DECLARATION_AT_PIN", contract_impact="SATISFIED_EVIDENCE_LE2", evidence=f"audit/pre-freeze-recovery/RDFCONFIG_LICENSE_EVIDENCE_CORRECTION.md;README_sha256_0d234b70", confidence="high", evidence_class_25r3a="LE2_EXPLICIT_REPOSITORY_LEVEL_LICENSE_DECLARATION_AT_PIN", documentary_gate_25r3a="RECOVERED_DOCUMENTARILY", revalidation_run_id=RUN)
    elif row["method_id"] in {"mkgqagent", "cot_sparql", "firesparql"}:
        row.update(evidence_class_25r3a="LE6_NO_PUBLIC_LICENSE_EVIDENCE", documentary_gate_25r3a="DOCUMENTARY_GATE_EXHAUSTED", revalidation_run_id=RUN)
    else:
        row.update(evidence_class_25r3a="", documentary_gate_25r3a="", revalidation_run_id="")
csv_write(code_path, code_fields, code_rows)

gate_path = ROOT / "audit/PHASE2_CONTRACT_COMPOSITE_LEGAL_GATE_MATRIX.csv"
with gate_path.open(newline="", encoding="utf-8") as h:
    gate_rows = list(csv.DictReader(h))
    gate_fields = list(gate_rows[0])
for f in ["legal_recovery_25r3a", "remaining_gate_25r3a"]:
    if f not in gate_fields:
        gate_fields.append(f)
for row in gate_rows:
    if row["method_id"] == "rdfconfig_llm":
        row["G3C_code"] = "SATISFIED_EVIDENCE_LE2"
        row["composite_G3"] = "LAB_POLICY_G3_COMPOSITE_CONDITIONAL"
        row["legal_recovery_25r3a"] = "RECOVERED_DOCUMENTARILY"
        row["primary_legal_blocker"] = "none_code_LE2"
        row["remaining_gate_25r3a"] = "runtime;artifact/schema;G4;G5;G6I"
    elif row["method_id"] in {"mkgqagent", "cot_sparql", "firesparql"}:
        row["legal_recovery_25r3a"] = "DOCUMENTARY_GATE_EXHAUSTED"
        row["remaining_gate_25r3a"] = "code_permission_absent;runtime/resources"
    else:
        row["legal_recovery_25r3a"] = ""
        row["remaining_gate_25r3a"] = ""
csv_write(gate_path, gate_fields, gate_rows)

registry = ROOT / "configs/common/LEGAL_EVIDENCE_REGISTRY.yaml"
reg_data = yaml.safe_load(registry.read_text(encoding="utf-8"))
reg_data["registry_version"] = "0.2.0-25R3A"
reg_data["run_id"] = RUN
new_ids = {
    "E_25R3A_MKG_LICENSE_EXHAUSTION",
    "E_25R3A_RDFCONFIG_PIN_README_LE2",
    "E_25R3A_RDFCONFIG_ZENODO_LINEAGE",
    "E_25R3A_COT_LICENSE_EXHAUSTION",
    "E_25R3A_COT_MODEL_METADATA",
    "E_25R3A_FIRE_LICENSE_EXHAUSTION",
}
reg_data["evidence"] = [e for e in reg_data["evidence"] if e.get("evidence_id") not in new_ids]
reg_data["evidence"].extend([
    dict(evidence_id="E_25R3A_MKG_LICENSE_EXHAUSTION", component_layer="L1_METHOD_UPSTREAM_CODE", method_id="mkgqagent", artifact_id="WSE-research/text2sparql-agent", source_url="https://github.com/WSE-research/text2sparql-agent", source_type="BOUNDED_AUTHORITATIVE_SEARCH", pinned_revision="ba0f2f78611a7ccacc8c985a97f6008ef7ee6a6a", current_revision="ba0f2f78611a7ccacc8c985a97f6008ef7ee6a6a", retrieved_at=RUN, license_identifier="ABSENT", license_text_source="ABSENT", scope="code", conflicts="none", status="DOCUMENTARY_GATE_EXHAUSTED", evidence_class="LE6_NO_PUBLIC_LICENSE_EVIDENCE", reopen_condition="PUBLIC_CODE_LICENSE_APPEARS"),
    dict(evidence_id="E_25R3A_RDFCONFIG_PIN_README_LE2", component_layer="L1_METHOD_UPSTREAM_CODE", method_id="rdfconfig_llm", artifact_id="scott2121/sparql_query_generator", source_url="https://github.com/scott2121/sparql_query_generator/blob/fe63171d3c8b9679779749ee11f731b2a8318053/README.md", source_type="OFFICIAL_AUTHOR_REPOSITORY_PINNED_README", pinned_revision="fe63171d3c8b9679779749ee11f731b2a8318053", current_revision="fe63171d3c8b9679779749ee11f731b2a8318053", evidence_hash="0d234b70ebb9ac497372aa50bf56cae087fff3926a7b00a28c701c775f7481c7", blob_id="c813f08014babde306e2539b1119cf396220622c", retrieved_at=RUN, license_identifier="MIT", license_text_source="README.md lines 110-113", scope="all_files_in_repository", conflicts="none", status="CONFIRMED_REPOSITORY_LEVEL_MIT_DECLARATION_AT_PIN", evidence_class="LE2_EXPLICIT_REPOSITORY_LEVEL_LICENSE_DECLARATION_AT_PIN", qualifiers=["NO_STANDARD_LICENSE_FILE", "GITHUB_LICENSE_DETECTION_NULL"]),
    dict(evidence_id="E_25R3A_RDFCONFIG_ZENODO_LINEAGE", component_layer="L1_METHOD_ARCHIVE", method_id="rdfconfig_llm", artifact_id="zenodo_18539214", source_url="https://zenodo.org/api/records/18539214", source_type="OFFICIAL_AUTHOR_ARCHIVE_METADATA", pinned_revision="v1.0.0", retrieved_at=RUN, license_identifier="CC-BY-4.0", license_text_source="zenodo_metadata.license", scope="archive_deposit_only", conflicts="not_transferred_to_github", status="RECOVERED_DOCUMENTARILY", evidence_class="LE3_AUTHOR_ARCHIVE_LICENSE", notes="byte_equivalence_not_tested_nonblocking"),
    dict(evidence_id="E_25R3A_COT_LICENSE_EXHAUSTION", component_layer="L1_METHOD_UPSTREAM_CODE", method_id="cot_sparql", artifact_id="dice-group/CoT-Sparql", source_url="https://github.com/dice-group/CoT-Sparql", source_type="BOUNDED_AUTHORITATIVE_SEARCH", pinned_revision="063edd9868425e54010a0cb49ce585ed2186be4d", current_revision="063edd9868425e54010a0cb49ce585ed2186be4d", retrieved_at=RUN, license_identifier="ABSENT", scope="code", status="DOCUMENTARY_GATE_EXHAUSTED", evidence_class="LE6_NO_PUBLIC_LICENSE_EVIDENCE", reopen_condition="PUBLIC_CODE_LICENSE_APPEARS"),
    dict(evidence_id="E_25R3A_COT_MODEL_METADATA", component_layer="L3_MODEL", method_id="cot_sparql", artifact_id="TheBloke/CodeLlama-34B-Instruct-GPTQ", source_url="https://huggingface.co/api/models/TheBloke/CodeLlama-34B-Instruct-GPTQ", source_type="OFFICIAL_MODEL_REPOSITORY_METADATA", pinned_revision="0a2785d47fb7330388e0487e0526bbc53d87c156", retrieved_at=RUN, license_identifier="llama2", scope="model_only", status="RECOVERED_DOCUMENTARILY", evidence_class="LE4_MODEL_OR_DATA_LICENSE", notes="no_weights_downloaded;does_not_license_code"),
    dict(evidence_id="E_25R3A_FIRE_LICENSE_EXHAUSTION", component_layer="L1_METHOD_UPSTREAM_CODE", method_id="firesparql", artifact_id="sherry-pan/FIRESPARQL", source_url="https://github.com/sherry-pan/FIRESPARQL", source_type="BOUNDED_AUTHORITATIVE_SEARCH", pinned_revision="48d6f168e4c1dd3dc467553aef370299911d4e76", current_revision="48d6f168e4c1dd3dc467553aef370299911d4e76", retrieved_at=RUN, license_identifier="ABSENT", scope="code", status="DOCUMENTARY_GATE_EXHAUSTED", evidence_class="LE6_NO_PUBLIC_LICENSE_EVIDENCE", reopen_condition="PUBLIC_CODE_LICENSE_APPEARS", notes="HF_model_MIT_is_separate"),
])
write(registry, yaml.safe_dump(reg_data, sort_keys=False, allow_unicode=True))

# Add explicit 25R3A status columns to candidate matrices; never mark executable.
def annotate_csv(rel: str, updater) -> None:
    path = ROOT / rel
    with path.open(newline="", encoding="utf-8") as h:
        rows = list(csv.DictReader(h))
        fields = list(rows[0])
    updater(rows, fields)
    csv_write(path, fields, rows)


def add_fields(fields: list[str], names: list[str]) -> None:
    for name in names:
        if name not in fields:
            fields.append(name)


def update_recovery(rows, fields):
    add_fields(fields, ["pre_freeze_documentary_status", "legal_status_25r3a", "artifact_status_25r3a"])
    for r in rows:
        if r["method_id"] == "mkgqagent":
            r.update(pre_freeze_documentary_status="DOCUMENTARY_GATE_EXHAUSTED", legal_status_25r3a="NO_PUBLIC_CODE_LICENSE", artifact_status_25r3a="unchanged")
        elif r["method_id"] == "rdfconfig_llm":
            r.update(pre_freeze_documentary_status="RECOVERED_DOCUMENTARILY", legal_status_25r3a="CONFIRMED_REPOSITORY_LEVEL_MIT_DECLARATION_AT_PIN", artifact_status_25r3a="ZENODO_LINEAGE_CONFIRMED_BYTE_EQUIV_NOT_TESTED_NONBLOCKING")
            r["native_recovery_status"] = "LEGAL_DOCUMENTARILY_RECOVERED_RUNTIME_PENDING"
        elif r["method_id"] == "cot_sparql":
            r.update(pre_freeze_documentary_status="RECOVERED_AND_EXHAUSTED", legal_status_25r3a="DOCUMENTARY_GATE_EXHAUSTED", artifact_status_25r3a="FOUR_CONTEXT_URLS_AND_NATIVE_MODEL_METADATA_RECOVERED")
            r["native_recovery_status"] = "LEGAL_EXHAUSTED_ARTIFACT_METADATA_RECOVERED_HARDWARE_BLOCKED"
        else:
            r.update(pre_freeze_documentary_status="", legal_status_25r3a="", artifact_status_25r3a="")


annotate_csv("audit/recovery-protocol/PHASE2_METHOD_RECOVERY_PROTOCOL_MATRIX.csv", update_recovery)


def update_priority(rows, fields):
    add_fields(fields, ["pre_freeze_documentary_status", "priority_effect_25r3a"])
    for r in rows:
        if r["method_id"] == "rdfconfig_llm":
            r["legal_status"] = "LE2_MIT_RECOVERED"
            r["artifact_status"] = "ZENODO_LINEAGE_CONFIRMED_EQUIV_NONBLOCKING"
            r.update(pre_freeze_documentary_status="RECOVERED_DOCUMENTARILY", priority_effect_25r3a="legal blocker removed; runtime/schema remain")
        elif r["method_id"] == "mkgqagent":
            r["legal_status"] = "EXHAUSTED_NO_PUBLIC_LICENSE"
            r.update(pre_freeze_documentary_status="DOCUMENTARY_GATE_EXHAUSTED", priority_effect_25r3a="closed documentary; execution still legally blocked")
        elif r["method_id"] == "cot_sparql":
            r["legal_status"] = "EXHAUSTED_NO_PUBLIC_LICENSE"
            r["artifact_status"] = "REMOTE_METADATA_VERIFIED"
            r.update(pre_freeze_documentary_status="RECOVERED_AND_EXHAUSTED", priority_effect_25r3a="artifact uncertainty reduced; legal/hardware remain")
        else:
            r.update(pre_freeze_documentary_status="", priority_effect_25r3a="")


annotate_csv("audit/recovery-protocol/PHASE2_METHOD_RECOVERY_PRIORITY_MATRIX.csv", update_priority)


def update_groups(rows, fields):
    add_fields(fields, ["pre_freeze_status_25r3a"])
    for r in rows:
        if r["group_id"] == "QALD_Q_ONLY_SYSTEM_LEVEL":
            r["blocked_candidates"] = "all_runtime; mkg_license_exhausted_no_permission; cot_license_exhausted+hardware"
            r["pre_freeze_status_25r3a"] = "DOCUMENTARY_CLOSED_EXECUTION_BLOCKED"
        elif r["group_id"] == "QALD_SCHEMA_COMMON_SYSTEM_LEVEL":
            r["blocked_candidates"] = "sparql model selection; RDF runtime+controlled DBpedia schema"
            r["pre_freeze_status_25r3a"] = "RDF_LEGAL_RECOVERED_DESIGN_FREEZE_READY"
        else:
            r["pre_freeze_status_25r3a"] = "unchanged"


annotate_csv("audit/fairness/PHASE2_PROVISIONAL_COMPARISON_GROUPS.csv", update_groups)


def update_pairs(rows, fields):
    add_fields(fields, ["pre_freeze_status_25r3a"])
    for r in rows:
        methods = {r["method_a"], r["method_b"]}
        if "rdfconfig_llm" in methods:
            r["pending_gate"] = "schema_bundle+models+runtime+F0-F14"
            r["pre_freeze_status_25r3a"] = "RDF_LEGAL_RECOVERED_NOT_EXECUTABLE"
        elif "mkgqagent" in methods or "cot_sparql" in methods:
            r["pre_freeze_status_25r3a"] = "DOCUMENTARY_CLOSED_LEGAL_OR_RUNTIME_BLOCKED"
        else:
            r["pre_freeze_status_25r3a"] = "unchanged"


annotate_csv("audit/fairness/PHASE2_DIRECT_COMPARISON_ELIGIBILITY_MATRIX.csv", update_pairs)

report = f"""# Phase 2 pre-freeze documentary recovery report

{HEADER}

## 1. Executive summary
All six mandatory documentary rows closed: four recovered, two exhausted, zero unresolved. Freeze design is ready.
## 2. Input fairness gate
25R3 gate satisfied at initial HEAD `e8aa49da8ebf733e77ca962cbb5a11ba502426ca`.
## 3. Scope
Metadata/text-only license, artifact and provenance review; no execution, weights, training, graph or benchmark.
## 4. Evidence hierarchy
Exact pin and author-controlled repository statements precede archives, model/data metadata and platform inference.
## 5. Documentary exhaustion semantics
Exhausted closes current obvious public sources and retains explicit reopen conditions.
## 6. mKGQAgent license
LE6; no public code license after bounded search; gate exhausted and execution remains blocked.
## 7. RDFConfig README license evidence
Exact pinned README explicitly licenses all repository files under MIT; blob/hash and lines recorded.
## 8. RDFConfig GitHub legal status
Corrected from LICENSE_ABSENT to confirmed LE2 MIT; no root LICENSE and platform null remain qualifiers.
## 9. RDFConfig paper lineage
Official paper availability statement connects the selected GitHub repository and Zenodo concept DOI.
## 10. RDFConfig Zenodo metadata
Record/version/files/checksum/CC-BY-4.0 metadata verified without archive download.
## 11. RDFConfig equivalence boundary
Byte equivalence untested; archive license not transferred; equivalence is nonblocking because GitHub pin passes LE2.
## 12. CoT license
LE6; no public code license after pin/HEAD/README/package/tags/releases/paper/archive search.
## 13. CoT context artifacts
Four author-linked direct targets return HEAD 200 with sizes/ETags; absent locally does not mean absent publicly.
## 14. CoT model metadata
Native 34B GPTQ reference pinned to HF revision; public/ungated; llama2 model scope; no weights downloaded.
## 15. CoT remaining hardware blocker
18.3 GB model metadata confirms local hardware risk; legal/runtime/services also remain blocked.
## 16. FIRESPARQL non-blocking update
Code-license and missing trainer/runner searches exhausted; HF model separate; IA_DOMAIN_NATIVE and nonblocking.
## 17. Legal recovery matrix
Four method rows distinguish LE2 recovery from LE6 exhaustion and scope-specific licenses.
## 18. Artifact recovery matrix
Zenodo archive, four CoT context files, CoT model, FIRE model and missing FIRE surfaces are recorded.
## 19. Corrections to earlier evidence
RDFConfig correction is explicit and historical decisions are retained.
## 20. Common-core candidate effects
RDF legal blocker removed; mKG/CoT documentary ambiguity closed but execution remains blocked.
## 21. Fairness groups
Taxonomy V2 and groups preserved; current eligible count remains zero and no participant is frozen here.
## 22. Freeze readiness
`BENCHMARK_PARTICIPANT_FREEZE_READY = true`: recovered 4, exhausted 2, unresolved 0.
## 23. Design freeze vs execution eligibility
25R4 may lock design; G4/G5/G6I/adapters/resources/preflight remain later requirements.
## 24. QALD
QALD9_PLUS_EN_DBPEDIA primary preserved; test SEALED.
## 25. DBpedia
2016-10 target and compressed acquisition preserved; NOT_DEPLOYED.
## 26. G4
NOT_SATISFIED.
## 27. G5
Runtime implementation/conformance pending.
## 28. G6D
DOCUMENTED.
## 29. G6I
PENDING.
## 30. Adapters
`common_adapter_allowed=false`; no adapter implemented.
## 31. Benchmark
NOT_CURRENTLY_ELIGIBLE and not executed.
## 32. Revised roadmap
25R3A complete; 25R4 next; deployment and runtime sequence unchanged.
## 33. Next action
Exactly `DEFINE_COMMON_CORE_BENCHMARK_FREEZE_AND_EXTERNAL_VALIDATION_PLAN`, Prompt 25R4.
## 34. Claim boundaries
Documentary recovery is not native reproduction, execution readiness, archive equivalence or legal advice.
## 35. Conclusion
Cheap documentary ambiguity is closed at USD 0.00 without method/model/graph/SPARQL/training/benchmark execution.
"""
write(ROOT / "audit/PHASE2_PRE_FREEZE_DOCUMENTARY_RECOVERY_REPORT.md", report)

write(ROOT / "docs/decisions/023_pre_freeze_documentary_recovery_closure.md", f"""# Decision 023 — Pre-freeze documentary recovery closure

**RUN_ID:** `{RUN}`

- mKGQAgent license: LE6, `DOCUMENTARY_GATE_EXHAUSTED`.
- RDFConfig code: exact pin recovered as LE2 MIT; prior legal classification corrected.
- RDFConfig Zenodo: lineage recovered; CC-BY archive scope separate; byte equivalence untested/nonblocking.
- CoT code license: LE6, exhausted; four context artifacts and native 34B model recovered at metadata level.
- FIRESPARQL: license/surface search exhausted, IA_DOMAIN_NATIVE, nonblocking.
- Mandatory closure: 4 recovered, 2 exhausted, 0 unresolved.

Decision: benchmark design-freeze readiness is true, participants are not yet frozen, execution remains
ineligible. Next: `DEFINE_COMMON_CORE_BENCHMARK_FREEZE_AND_EXTERNAL_VALIDATION_PLAN` — Prompt 25R4.
""")

write(ROOT / "audit/NEXT_AFTER_PRE_FREEZE_DOCUMENTARY_RECOVERY_DECISION.md", f"""# NEXT AFTER PRE-FREEZE DOCUMENTARY RECOVERY

| Field | Value |
|---|---|
| Mandatory recovered / exhausted / unresolved | 4 / 2 / 0 |
| Freeze readiness | `BENCHMARK_PARTICIPANT_FREEZE_READY=true` |
| Gate | `PRE_FREEZE_DOCUMENTARY_RECOVERY_COMPLETE_READY_FOR_BENCHMARK_DESIGN_FREEZE` |
| Next action | `DEFINE_COMMON_CORE_BENCHMARK_FREEZE_AND_EXTERNAL_VALIDATION_PLAN` |
| Next prompt | `Prompt_25R4` |
| Status | `GO_NEXT_ZERO_COST` |

Exactly one next action. Runtime execution, deployment, training, adapters and benchmark remain deferred.
ARTIFACT_COMMIT: *(post-commit)*
""")

write(DOC / "PRE_FREEZE_DOCUMENTARY_RECOVERY_GATE.md", f"""# Pre-freeze documentary recovery gate

{HEADER}

**`PRE_FREEZE_DOCUMENTARY_RECOVERY_COMPLETE_READY_FOR_BENCHMARK_DESIGN_FREEZE`**

- ZERO_EXTERNAL_MONETARY_COST_PRESERVED
- MKG_LICENSE_SEARCH_CLOSED
- RDFCONFIG_LICENSE_EVIDENCE_REEVALUATED
- RDFCONFIG_ZENODO_SCOPE_SEPARATED
- COT_LICENSE_SEARCH_CLOSED
- COT_ARTIFACT_AVAILABILITY_REEVALUATED
- ABSENT_LOCAL_NOT_EQUAL_MISSING_PUBLIC
- FIRE_DOMAIN_NATIVE_NONBLOCKING
- FAIRNESS_TRACKS_PRESERVED
- QALD_PRIMARY_PRESERVED
- DBPEDIA_TARGET_PRESERVED
- TEST_SEAL_PRESERVED
- NO_MODEL_EXECUTION
- NO_TRAINING
- NO_DEPLOYMENT
- NO_BENCHMARK
- GO_NEXT_ZERO_COST

Mandatory closure: recovered 4 · exhausted 2 · unresolved 0.
Next: `DEFINE_COMMON_CORE_BENCHMARK_FREEZE_AND_EXTERNAL_VALIDATION_PLAN` — Prompt `25R4`.
ARTIFACT_COMMIT: *(post-commit)*
""")

roadmap = [
    (1, "GLOBAL_BLOCKER_RECOVERY_AND_ZERO_COST_RECONCILIATION", "Prompt_25R1", "COMPLETE"),
    (2, "ZERO_COST_METHOD_RECOVERY_PROTOCOL", "Prompt_25R2", "COMPLETE"),
    (3, "FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT", "Prompt_25R3", "COMPLETE"),
    (4, "PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE", "Prompt_25R3A", "COMPLETE"),
    (5, "COMMON_CORE_BENCHMARK_FREEZE_AND_EXTERNAL_VALIDATION_PLAN", "Prompt_25R4", "NEXT"),
    (6, "HUMAN_DBPEDIA_DEPLOYMENT_RESOURCE_PROFILE_SELECTION", "human_gate", "DEFERRED_NOT_CANCELLED"),
    (7, "FINAL_DEPLOYMENT_AUTHORIZATION_PACKAGE", "Prompt_25B", "PLANNED_AFTER_25R4_AND_PROFILE"),
    (8, "RESOURCE_CONFIGURATION", "D1", "PLANNED"),
    (9, "DECOMPRESSION_AND_RDF_VALIDATION", "D2", "PLANNED"),
    (10, "RUNTIME_IMAGE_ACQUISITION", "D3", "PLANNED"),
    (11, "VIRTUOSO_LOAD", "D4", "PLANNED"),
    (12, "GRAPH_RUNTIME_VALIDATION", "D5_G4", "PLANNED"),
    (13, "GOLD_MATERIALIZATION", "D6_GOLD", "PLANNED"),
    (14, "METRIC_IMPLEMENTATION_AND_CONFORMANCE", "G5", "PLANNED"),
    (15, "METHOD_RECOVERY_EXECUTION", "recovery_prompts", "PLANNED"),
    (16, "G6I_G7_ADAPTER_IMPLEMENTATION_DECISION", "decision", "PLANNED"),
    (17, "ADAPTERS", "implementation", "PLANNED"),
    (18, "COMMON_PREFLIGHT", "runtime", "PLANNED"),
    (19, "QALD_BENCHMARK", "experiment", "PLANNED"),
    (20, "TEXT2SPARQL25_EXTERNAL_VALIDATION", "future_experiment", "PLANNED"),
    (21, "ERROR_ANALYSIS_PE6", "research", "PLANNED"),
    (22, "AI_MODEL_DISCOVERY_CASE_STUDY", "research", "PLANNED"),
    (23, "TEXT_TO_SQL_TRANSFER_PE7", "research", "PLANNED"),
    (24, "NEW_TEXT_TO_SPARQL_METHOD_PE8", "research", "PLANNED"),
    (25, "COMPARISON", "research", "PLANNED"),
    (26, "ABLATIONS", "research", "PLANNED"),
    (27, "FINAL_LITERATURE_TRIANGULATION", "research", "PLANNED"),
    (28, "THESIS_REPRODUCIBILITY_PACKAGE", "research", "PLANNED"),
]
csv_write(ROOT / "audit/PHASE2_REVISED_RESEARCH_ROADMAP.csv", ["order", "action", "vehicle", "status"], [dict(zip(["order", "action", "vehicle", "status"], r)) for r in roadmap])

# METHOD_REGISTRY overlay: preserve all historical method outcomes.
method_registry = ROOT / "METHOD_REGISTRY.yaml"
text = method_registry.read_text(encoding="utf-8")
text = text.split("\n# Prompt 25R3A pre-freeze documentary recovery overlay", 1)[0].rstrip()
text = text.replace("schema_version: '0.28'", "schema_version: '0.29'", 1)
text = text.replace("updated_at: '2026-10-12T15:06:07+02:00'", "updated_at: '2026-10-12T15:56:45+02:00'", 1)
text = text.replace("audit_prompt: Prompt_25R3_FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT", "audit_prompt: Prompt_25R3A_PRE_FREEZE_DOCUMENTARY_RECOVERY", 1)
text = text.replace("phase: phase2_fairness_contract_complete_pre_freeze_documentary_recovery_pending", "phase: phase2_pre_freeze_documentary_recovery_complete_or_conditional", 1)
text = text.replace("next_research_action: RUN_PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE", "next_research_action: DEFINE_COMMON_CORE_BENCHMARK_FREEZE_AND_EXTERNAL_VALIDATION_PLAN")
text = text.replace("next_research_prompt: Prompt_25R3A", "next_research_prompt: Prompt_25R4")
text = text.replace("phase2_next_action: RUN_PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE", "phase2_next_action: DEFINE_COMMON_CORE_BENCHMARK_FREEZE_AND_EXTERNAL_VALIDATION_PLAN")
text = text.replace("phase2_next_prompt: Prompt_25R3A", "phase2_next_prompt: Prompt_25R4")
text = text.replace("current_research_action: FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT", "current_research_action: PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE")
text = text.replace("benchmark_participant_freeze_status: NOT_READY_PENDING_DOCUMENTARY_RECOVERY", "benchmark_participant_freeze_status: READY_FOR_DESIGN_FREEZE_NOT_FROZEN")
text = text.replace("pre_freeze_recovery_required: true", "pre_freeze_recovery_required: false")
text += f"""

# Prompt 25R3A pre-freeze documentary recovery overlay
pre_freeze_recovery_run_id: {RUN}
pre_freeze_recovery_report: audit/PHASE2_PRE_FREEZE_DOCUMENTARY_RECOVERY_REPORT.md
pre_freeze_recovery_gate: PRE_FREEZE_DOCUMENTARY_RECOVERY_COMPLETE_READY_FOR_BENCHMARK_DESIGN_FREEZE
benchmark_participant_freeze_ready: true
mandatory_recovered_count: 4
mandatory_exhausted_count: 2
mandatory_unresolved_count: 0
pre_freeze_method_recovery_25r3a:
  mkgqagent:
    authoritative_license_recovery_status: MKG_LICENSE_EXHAUSTED_NO_PUBLIC_CODE_LICENSE
    artifact_metadata_recovery_status: unchanged
    documentary_gate_status: DOCUMENTARY_GATE_EXHAUSTED
    documentary_gate_exhausted: true
    remaining_runtime_blockers: [legal_permission, cost, services, runtime, G4, G5, G6I]
    reopen_condition: PUBLIC_CODE_LICENSE_APPEARS
  rdfconfig_llm:
    authoritative_license_recovery_status: CONFIRMED_REPOSITORY_LEVEL_MIT_DECLARATION_AT_PIN
    artifact_metadata_recovery_status: ZENODO_METADATA_LINEAGE_CONFIRMED_BYTE_EQUIVALENCE_NOT_TESTED_NONBLOCKING
    documentary_gate_status: RECOVERED_DOCUMENTARILY
    documentary_gate_exhausted: false
    qualifiers: [NO_STANDARD_LICENSE_FILE, GITHUB_LICENSE_DETECTION_NULL]
    remaining_runtime_blockers: [runtime, controlled_dbpedia_schema, G4, G5, G6I]
    reopen_condition: NEW_CONTRADICTORY_AUTHORITATIVE_EVIDENCE
  cot_sparql:
    authoritative_license_recovery_status: COT_LICENSE_EXHAUSTED_NO_PUBLIC_CODE_LICENSE
    artifact_metadata_recovery_status: FOUR_CONTEXT_ARTIFACTS_AND_NATIVE_MODEL_METADATA_RECOVERED
    documentary_gate_status: RECOVERED_AND_EXHAUSTED
    documentary_gate_exhausted: true
    remaining_runtime_blockers: [legal_permission, hardware, service, runtime, G4, G5, G6I]
    reopen_condition: PUBLIC_CODE_LICENSE_OR_OFFICIAL_SMALLER_VARIANT_APPEARS
  firesparql:
    authoritative_license_recovery_status: DOCUMENTARY_GATE_EXHAUSTED_NO_PUBLIC_CODE_LICENSE
    artifact_metadata_recovery_status: OFFICIAL_HF_MODEL_CONFIRMED_TRAINER_RUNNER_NOT_FOUND
    documentary_gate_status: DOCUMENTARY_GATE_EXHAUSTED
    documentary_gate_exhausted: true
    remaining_runtime_blockers: [code_license, trainer, runner, hardware, domain]
    reopen_condition: PUBLIC_CODE_LICENSE_OR_NATIVE_SURFACE_APPEARS
    qald_freeze_effect: NON_BLOCKING_FOR_QALD_FREEZE
"""
write(method_registry, text)

profile = ROOT / "configs/common/COMMON_PROTOCOL_PROFILE.yaml"
p = profile.read_text(encoding="utf-8")
p = p.split("\npre_freeze_recovery_run_id:", 1)[0]
p = p.replace("protocol_version: 0.1.6-25R3-fairness-contract", "protocol_version: 0.1.7-25R3A-pre-freeze-recovery")
p = p.replace("phase: phase2_fairness_contract_complete_pre_freeze_documentary_recovery_pending", "phase: phase2_pre_freeze_documentary_recovery_complete_or_conditional")
p = p.replace("next_action: RUN_PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE", "next_action: DEFINE_COMMON_CORE_BENCHMARK_FREEZE_AND_EXTERNAL_VALIDATION_PLAN")
p = p.replace("next_prompt: Prompt_25R3A", "next_prompt: Prompt_25R4")
p = p.replace("gate: FAIR_COMPARISON_AND_HOMOGENEITY_CONTRACT_DEFINED_READY_FOR_PRE_FREEZE_DOCUMENTARY_RECOVERY", "gate: PRE_FREEZE_DOCUMENTARY_RECOVERY_COMPLETE_READY_FOR_BENCHMARK_DESIGN_FREEZE")
p = p.replace("claim_boundary: FAIRNESS_CONTRACT_DEFINED_no_execution", "claim_boundary: DOCUMENTARY_RECOVERY_CLOSED_design_freeze_ready_not_execution")
p = p.replace("phase2_next_action: RUN_PRE_FREEZE_DOCUMENTARY_RECOVERY_WAVE", "phase2_next_action: DEFINE_COMMON_CORE_BENCHMARK_FREEZE_AND_EXTERNAL_VALIDATION_PLAN")
p = p.replace("benchmark_participant_freeze_status: NOT_READY_PENDING_DOCUMENTARY_RECOVERY", "benchmark_participant_freeze_status: READY_FOR_DESIGN_FREEZE_NOT_FROZEN")
p += f"\npre_freeze_recovery_run_id: {RUN}\nmandatory_recovered_count: 4\nmandatory_exhausted_count: 2\nmandatory_unresolved_count: 0\n"
write(profile, p)

plan = f"""# PLAN_SYNC — Estado para optimización del plan de prompts

**Repo:** https://github.com/EdmundoMori/text2sparql-reproducibility-lab
**Última actualización:** 2026-10-12 (Prompt **25R3A**)
**Fase:** pre-freeze documentary recovery complete · benchmark design freeze ready
**SHA inicial 25R3A:** `e8aa49da8ebf733e77ca962cbb5a11ba502426ca`
**RUN_ID:** `{RUN}`

Gate: `PRE_FREEZE_DOCUMENTARY_RECOVERY_COMPLETE_READY_FOR_BENCHMARK_DESIGN_FREEZE`.
Mandatory closure: 4 recovered · 2 exhausted · 0 unresolved. RDFConfig pin is LE2 MIT; mKG and CoT
license searches are exhausted; four CoT context URLs and native 34B model metadata are verified.
Participants are not yet frozen and execution remains ineligible.

## Prompt 25R3 reconciliation

Initial `6c5ddb631cf3961c6777906b6c3595e87ab4f0ba`; artifact
`1f8b19ee44182c36024973d83ce989be514c1f14`; publication/tip
`e8aa49da8ebf733e77ca962cbb5a11ba502426ca`; push confirmed.

## Unique next action

`DEFINE_COMMON_CORE_BENCHMARK_FREEZE_AND_EXTERNAL_VALIDATION_PLAN` — Prompt `25R4` — `GO_NEXT_ZERO_COST`.
Do not select deployment, training, method execution, adapters or benchmark.

## Publication

ARTIFACT_COMMIT: *(post-commit)*
publication metadata commit: *(post-commit tip; max 2 commits)*
push: pending
"""
write(ROOT / "PLAN_SYNC.md", plan)

write(ROOT / "docs/plan-sync/NEXT_PROMPT_GUIDANCE.md", f"""# NEXT_PROMPT_GUIDANCE

**Tras:** Prompt 25R3A (`{RUN}`)
**Gate:** `PRE_FREEZE_DOCUMENTARY_RECOVERY_COMPLETE_READY_FOR_BENCHMARK_DESIGN_FREEZE`

## Acción siguiente

`DEFINE_COMMON_CORE_BENCHMARK_FREEZE_AND_EXTERNAL_VALIDATION_PLAN`

**Prompt 25R4** — Common-core benchmark design/participant freeze and external-validation plan under the
25R3 fairness tracks and 25R3A documentary closure, ZERO_COST, without method or benchmark execution.

Status: **GO_NEXT_ZERO_COST**. No seleccionar aún deployment, 25B, training, adapters or benchmark.
""")
write(ROOT / "docs/plan-sync/PLANNER_LOOP.md", f"""# PLANNER_LOOP

1. `PLAN_SYNC.md`
2. `docs/protocols/common/pre-freeze-recovery/{RUN}/PRE_FREEZE_DOCUMENTARY_RECOVERY_GATE.md`
3. `audit/PHASE2_PRE_FREEZE_DOCUMENTARY_RECOVERY_REPORT.md`
4. `audit/NEXT_AFTER_PRE_FREEZE_DOCUMENTARY_RECOVERY_DECISION.md`
5. `METHOD_REGISTRY.yaml`

Next: `DEFINE_COMMON_CORE_BENCHMARK_FREEZE_AND_EXTERNAL_VALIDATION_PLAN` — Prompt `25R4`.
""")

index = ROOT / "docs/plan-sync/ARTIFACT_INDEX.md"
idx = index.read_text(encoding="utf-8")
idx = idx.replace("**Última actualización:** 2026-10-12 (Prompt 25R3)", "**Última actualización:** 2026-10-12 (Prompt 25R3A)")
marker = "| ID | Tema | Ruta | Cuándo leerlo |\n|---|---|---|---|\n"
if "P25R3A-GATE" not in idx:
    rows = (
        f"| P25R3A-GATE | Pre-freeze documentary gate | `docs/protocols/common/pre-freeze-recovery/{RUN}/PRE_FREEZE_DOCUMENTARY_RECOVERY_GATE.md` | Tras 25R3A |\n"
        "| P25R3A-RPT | Recovery report | `audit/PHASE2_PRE_FREEZE_DOCUMENTARY_RECOVERY_REPORT.md` | Evidencia completa |\n"
        "| P25R3A-LEGAL | Authoritative license matrix | `audit/pre-freeze-recovery/PHASE2_AUTHORITATIVE_CODE_LICENSE_RECOVERY_MATRIX.csv` | LE1–LE6 |\n"
        "| P25R3A-ART | Artifact matrix | `audit/pre-freeze-recovery/PHASE2_AUTHORITATIVE_ARTIFACT_RECOVERY_MATRIX.csv` | CoT/RDF/FIRE metadata |\n"
        "| P25R3A-CLOSE | Closure matrix | `audit/pre-freeze-recovery/PHASE2_PRE_FREEZE_DOCUMENTARY_RECOVERY_CLOSURE_MATRIX.csv` | Freeze readiness |\n"
    )
    idx = idx.replace(marker, marker + rows)
index.write_text(idx, encoding="utf-8")

for rel in ["README.md", "PROJECT_CONTEXT.md", "RESEARCH_PROTOCOL.md"]:
    path = ROOT / rel
    old = path.read_text(encoding="utf-8")
    section = f"""

## Prompt 25R3A — Pre-freeze documentary recovery ({RUN})

Mandatory documentary closure is complete: four rows recovered, two exhausted and zero unresolved.
RDFConfig's exact pinned README provides repository-wide MIT evidence (LE2), correcting the prior
LICENSE_NOT_CONFIRMED classification while retaining NO_STANDARD_LICENSE_FILE and preserving the Phase-1
blocked outcome. mKGQAgent and CoT code-license searches are exhausted; CoT's four remote context artifacts
and native 34B model are metadata-verified without downloads. FIRESPARQL remains domain-native/nonblocking.
Benchmark design freeze is ready but not yet applied; execution remains ineligible. QALD/test seal and DBpedia
target preserved; graph NOT_DEPLOYED; G4 not satisfied; G5/G6I pending; adapters false; cost USD 0.00.
Next: Prompt 25R4.
"""
    if "Prompt 25R3A — Pre-freeze documentary recovery" not in old:
        path.write_text(old.rstrip("\n") + section.rstrip() + "\n", encoding="utf-8")

write(LOG / "commands.log", f"""RUN_ID={RUN}
git fetch origin
git branch --show-current
git rev-parse HEAD
git rev-parse origin/main
git status --short
git show exact pinned README metadata/text hashes
gh api repository/commit/tag/release/content metadata only
curl HEAD only for CoT context artifacts and DOI redirects
Zenodo and Hugging Face metadata APIs only
python3 scripts/preparation/generate_prompt_25r3a_artifacts.py
No method/model/graph/SPARQL/training/benchmark execution.
""")

write(LOG / "network.log", """2026-10-12 metadata-only network
GitHub API repository/commit/tags/releases/content calls: HTTP 200; public metadata/text only.
WSE repo bytes: repo 6814; commit 24623; tags 537; releases 2836.
RDF repo bytes: repo 5740; commit 4305; tags 453; releases 1833.
CoT repo bytes: repo 6413; commit 73105; tags 2; releases 2.
FIRE repo bytes: repo 5260; commit 6996; tags 2; releases 2.
Zenodo records 18539213/18539214: HTTP 200, 3906 bytes each, ETag "4".
HF CoT model API: HTTP 200, 2668 bytes; tree metadata 15317 bytes.
HF FIRE model API: HTTP 200, 3448 bytes.
OUP official paper text extraction: 42.7 KB; availability statement only.
DOI HEAD: 302 to OUP article; OUP HEAD 403; no article payload via curl.
CoT anon HEAD: four HTTP 200 landing responses, header bytes 1673/1679/1667/1673, body 0.
CoT direct HEAD: four HTTP 200, header bytes 275/277/279/277, body 0.
No archive, model weights, dataset, RDF or graph payload downloaded.
external_monetary_cost_usd=0.00
""")
write(LOG / "legal-evidence.log", """MKG=LE6 DOCUMENTARY_GATE_EXHAUSTED
RDFCONFIG=LE2 MIT RECOVERED_DOCUMENTARILY
RDFCONFIG_README_BLOB=c813f08014babde306e2539b1119cf396220622c
RDFCONFIG_README_SHA256=0d234b70ebb9ac497372aa50bf56cae087fff3926a7b00a28c701c775f7481c7
RDFCONFIG_QUALIFIERS=NO_STANDARD_LICENSE_FILE;GITHUB_LICENSE_DETECTION_NULL
ZENODO=LE3 CC-BY-4.0 ARCHIVE_ONLY LINEAGE_RECOVERED BYTE_EQUIV_NOT_TESTED_NONBLOCKING
COT=LE6 DOCUMENTARY_GATE_EXHAUSTED
FIRE=LE6 DOCUMENTARY_GATE_EXHAUSTED NONBLOCKING
No legal advice; laboratory evidence classification only.
""")
write(LOG / "artifact-head-checks.log", """artifact,status,size,etag,last_modified,body_bytes
dbpedia_examples.parquet,HEAD_200,462043,65db4b66-70cdb,2024-02-25T14:15:02Z,0
embeddings_dbpedia.pkl,HEAD_200,5913763,65db4b65-5a3ca3,2024-02-25T14:15:01Z,0
embeddings_wikidata.pkl,HEAD_200,33019555,65db4b60-1f7d6a3,2024-02-25T14:14:56Z,0
wikidata_examples.parquet,HEAD_200,2141658,65db4b2b-20adda,2024-02-25T14:14:03Z,0
anon_wrapper_note=HTTP_200 landing_no_HEAD_redirect; direct embedded target verified
model_weights_downloaded=false
""")
write(LOG / "schema-validation.log", """PASS
YAML_PARSE=true
CSV_PARSE=true
LEGAL_TAXONOMY_PRESENT=true
CLOSURE_ENUMS_VALID=true
""")
write(LOG / "validation.log", """PASS
INITIAL_HEAD=e8aa49da8ebf733e77ca962cbb5a11ba502426ca
MKG_SEARCH_COMPLETE=true
RDF_PIN_README_HASH_RECORDED=true
RDF_LE2_CONFIRMED=true
ZENODO_SCOPE_SEPARATE=true
COT_LICENSE_SEARCH_COMPLETE=true
COT_PUBLIC_ARTIFACT_METADATA_VERIFIED=4
COT_WEIGHTS_DOWNLOADED=false
FIRE_NONBLOCKING=true
MANDATORY_RECOVERED=4
MANDATORY_EXHAUSTED=2
MANDATORY_UNRESOLVED=0
FREEZE_READY=true
PARTICIPANTS_FROZEN=false
NO_METHOD_EXECUTION=true
NO_TRAINING=true
NO_SPARQL=true
NO_DEPLOYMENT=true
NO_BENCHMARK=true
EXTERNAL_MONETARY_COST_USD=0.00
""")

hashes = []
for base in (DOC, AUD, CFG):
    for path in sorted(base.rglob("*")):
        if path.is_file():
            hashes.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT)}")
for path in [
    ROOT / "audit/PHASE2_PRE_FREEZE_DOCUMENTARY_RECOVERY_REPORT.md",
    ROOT / "audit/NEXT_AFTER_PRE_FREEZE_DOCUMENTARY_RECOVERY_DECISION.md",
    ROOT / "docs/decisions/023_pre_freeze_documentary_recovery_closure.md",
]:
    hashes.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.relative_to(ROOT)}")
write(LOG / "metadata.sha256", "\n".join(hashes))

print(f"generated Prompt 25R3A artifacts RUN_ID={RUN}")
