# CoT-SPARQL pre-freeze documentary recovery

**RUN_ID:** `20261012T135645Z`
**Mode:** DOCUMENTARY · METADATA_ONLY · ZERO_COST · NO_METHOD_EXECUTION


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
