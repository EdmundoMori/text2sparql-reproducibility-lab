# Virtuoso runtime and loader decision

**RUN_ID:** `20260722T162241Z` · Tags: `VIRTUOSO_RUNTIME_VERSION_DOCUMENTED` · `VIRTUOSO_IMAGE_DIGEST_VERIFIED` · `CONTAINER_ARCH_AMD64_VERIFIED`

## Selected metadata pin (not pulled)

| Field | Value |
|---|---|
| Image | `openlink/virtuoso-opensource-7:7.2.17-r25-g6eb68b6-ubuntu` |
| Index digest | `sha256:2a9914b95f8a52927a73947c87ec2727f78f87d38e41c38c379efb121f9cbed1` |
| linux/amd64 manifest digest | `sha256:748863fd9026fac41667dac484e5044c6c34e95c75bce3bf26c9225fe7684eb6` |
| Source | https://github.com/openlink/virtuoso-opensource · release `v7.2.17` |
| License | GitHub API `NOASSERTION` — verify before load |
| Status | `PINNED_METADATA_ONLY` |

Rejected: `latest`, floating `7`/`7.2`, tenforce as primary.

No `docker pull`. Loader details confirmed at D3/D4.
Matrix: `audit/PHASE2_VIRTUOSO_RUNTIME_CANDIDATE_MATRIX.csv`
