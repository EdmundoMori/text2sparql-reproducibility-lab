#!/usr/bin/env bash
# clone_repositories.sh — clona upstream para auditoría estática.
# No instala dependencias. No entrena. No modifica archivos dentro de clones.
# Uso: desde la raíz del lab: bash scripts/clone_repositories.sh

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

MANIFEST="${CLONE_MANIFEST:-$ROOT/configs/clone_manifest.yaml}"
LOG_DIR="$ROOT/logs/cloning"
LICENSE_DIR="$ROOT/licenses"
LOCK_FILE="$ROOT/REPOSITORIES.lock.yaml"
STAMP="$(date -Iseconds)"
RUN_LOG="$LOG_DIR/clone_run_${STAMP//[:]/}.log"
SUMMARY_TSV="$LOG_DIR/clone_summary_${STAMP//[:]/}.tsv"

mkdir -p "$LOG_DIR" "$LICENSE_DIR"

export GIT_LFS_SKIP_SMUDGE="${GIT_LFS_SKIP_SMUDGE:-1}"
export GIT_TERMINAL_PROMPT=0

log() { echo "[$(date -Iseconds)] $*" | tee -a "$RUN_LOG"; }
fail() { log "ERROR: $*"; echo "ERROR: $*" >&2; return 1; }

# --- YAML manifest parser (Python) ---
parse_manifest() {
  python3 - "$MANIFEST" <<'PY'
import sys, re
from pathlib import Path
text = Path(sys.argv[1]).read_text(encoding="utf-8")
# Minimal YAML list parser for our flat keys under repositories:
entries = []
cur = None
for line in text.splitlines():
    if line.strip().startswith("- method_id:"):
        if cur:
            entries.append(cur)
        cur = {"method_id": line.split(":", 1)[1].strip()}
        continue
    if cur is None:
        continue
    m = re.match(r"^\s+([a-z_]+):\s*(.*)$", line)
    if not m:
        continue
    k, v = m.group(1), m.group(2).strip().strip('"').strip("'")
    cur[k] = v
if cur:
    entries.append(cur)
for e in entries:
    exp = (e.get("expected_commit") or "").strip()
    if not exp or exp in {"", "null", "None", '""'}:
        exp = "NONE"
    # Use RS=unit separator friendly CSV-like with explicit NONE sentinel
    print("|".join([
        e.get("method_id", ""),
        e.get("role", "primary"),
        e.get("url", ""),
        e.get("local_path", ""),
        e.get("default_branch", "main"),
        exp,
        e.get("inclusion_decision", ""),
        e.get("license_status", ""),
        e.get("license_spdx", "UNKNOWN"),
        e.get("wave", ""),
    ]))
PY
}

copy_license_refs() {
  local method_id="$1" local_path="$2" license_status="$3" license_spdx="$4"
  # One license folder per clone path (avoids collisions when a method has companions)
  local dest_name
  dest_name="$(basename "$local_path")"
  local dest="$LICENSE_DIR/${dest_name}"
  mkdir -p "$dest"
  local note="$dest/LICENSE_STATUS.txt"
  {
    echo "method_id: $method_id"
    echo "local_path: $local_path"
    echo "license_status: $license_status"
    echo "license_spdx: $license_spdx"
    echo "recorded_at: $(date -Iseconds)"
    echo "source_inspection: static copy of LICENSE* if present; else LICENSE_NOT_CONFIRMED note"
  } >"$note"

  local found=0
  for cand in LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING COPYING.md; do
    if [[ -f "$local_path/$cand" ]]; then
      cp -a "$local_path/$cand" "$dest/$cand"
      found=1
      log "License file copied: $local_path/$cand -> $dest/$cand"
    fi
  done
  if [[ "$found" -eq 0 ]]; then
    echo "NO_LICENSE_FILE_IN_REPO" >"$dest/NO_LICENSE_FILE"
    if [[ "$license_status" == "LICENSE_NOT_CONFIRMED" ]]; then
      cat >"$dest/README_LICENSE.md" <<EOF
# License: LICENSE_NOT_CONFIRMED

Repository cloned for **static inspection only**.

- Do **not** copy, modify, or integrate into adapters yet.
- Public code ≠ confirmed reusable rights.
- See audit/LICENSE_MATRIX.csv and audit/EVIDENCE_CLOSURE.md.
EOF
    fi
  fi
}

collect_git_metadata() {
  local local_path="$1"
  (
    cd "$local_path"
    echo "=== remote ==="
    git remote -v
    echo "=== branch ==="
    git rev-parse --abbrev-ref HEAD
    echo "=== commit ==="
    git rev-parse HEAD
    echo "=== commit date ==="
    git show -s --format=%cI HEAD
    echo "=== subject ==="
    git show -s --format=%s HEAD
    echo "=== tags pointing at HEAD ==="
    git tag --points-at HEAD || true
    echo "=== all tags (names) ==="
    git tag -l || true
    echo "=== submodule status ==="
    git submodule status --recursive || true
    echo "=== lfs (if any) ==="
    git lfs ls-files 2>/dev/null | head -n 50 || echo "git-lfs unavailable or no LFS files listed"
    echo "=== du -sh . ==="
    du -sh . 2>/dev/null || true
    echo "=== du -sh .git ==="
    du -sh .git 2>/dev/null || true
  )
}

estimate_sizes() {
  local local_path="$1"
  python3 - "$local_path" <<'PY'
import os, sys
from pathlib import Path
root = Path(sys.argv[1])
# Heuristic buckets (bytes)
code_ext = {".py",".java",".rb",".ts",".tsx",".js",".jsx",".go",".rs",".c",".cc",".cpp",".h",".hpp",".scala",".kt",".sh",".bash",".yml",".yaml",".toml",".cfg",".ini",".md",".adoc",".txt",".json",".sparql",".rq",".ttl",".nt",".rdf",".owl",".xml",".html",".css",".ipynb",".gradle",".properties",".dockerfile"}
model_pat = (".pt",".pth",".bin",".ckpt",".safetensors",".onnx",".gguf",".h5",".pkl",".joblib",".msgpack")
data_dir_hints = ("dataset", "datasets", "data", "questions", "experiment_datasets", "results", "embeddings", "indexes", "index")
docker_hints = ("Dockerfile", "compose.yml", "compose.yaml", "docker-compose")

code=model=data=docker_meta=other=0
n_files=0
for dirpath, dirnames, filenames in os.walk(root):
    # skip .git contents for source estimate but count separately outside
    parts = Path(dirpath).parts
    if ".git" in parts:
        continue
    rel = str(Path(dirpath).relative_to(root)).lower()
    for fn in filenames:
        n_files += 1
        p = Path(dirpath) / fn
        try:
            sz = p.stat().st_size
        except OSError:
            continue
        name = fn.lower()
        suf = p.suffix.lower()
        if any(name == h.lower() or name.startswith("docker-compose") or name.startswith("compose.") for h in docker_hints) or "dockerfile" in name:
            docker_meta += sz
            continue
        if suf in model_pat or "checkpoint" in name or "weights" in name:
            model += sz
            continue
        if any(h in rel.split(os.sep) for h in data_dir_hints) or suf in {".parquet",".arrow",".csv",".tsv",".faiss"}:
            # large result dumps count as data-ish
            data += sz
            continue
        if suf in code_ext or name in {"makefile","gemfile","rakefile","license","licence"}:
            code += sz
            continue
        other += sz

def mb(x): return round(x/1024/1024, 2)
print(f"n_files_no_git={n_files}")
print(f"source_code_est_mib={mb(code)}")
print(f"models_est_mib={mb(model)}")
print(f"datasets_results_est_mib={mb(data)}")
print(f"docker_metadata_est_mib={mb(docker_meta)}")
print(f"other_est_mib={mb(other)}")
print(f"source_code_est_bytes={code}")
print(f"models_est_bytes={model}")
print(f"datasets_results_est_bytes={data}")
print(f"docker_metadata_est_bytes={docker_meta}")
print(f"other_est_bytes={other}")
PY
}

clone_one() {
  local method_id="$1" role="$2" url="$3" local_path="$4" branch="$5" expected="$6"
  local inclusion="$7" license_status="$8" license_spdx="$9" wave="${10}"

  local entry_log="$LOG_DIR/${method_id}_${role}.log"
  log "---- BEGIN $method_id ($role) -> $local_path ----"
  {
    echo "method_id=$method_id"
    echo "role=$role"
    echo "url=$url"
    echo "local_path=$local_path"
    echo "branch=$branch"
    echo "expected_commit=${expected:-<none>}"
    echo "GIT_LFS_SKIP_SMUDGE=$GIT_LFS_SKIP_SMUDGE"
    echo "started=$(date -Iseconds)"
  } | tee -a "$entry_log" >>"$RUN_LOG"

  if [[ -e "$local_path" ]] && [[ ! -d "$local_path/.git" ]]; then
    fail "Path exists but is not a git repo: $local_path"
    return 1
  fi

  if [[ -d "$local_path/.git" ]]; then
    log "Repository already exists: $local_path"
    local current
    current="$(git -C "$local_path" rev-parse HEAD)"
    echo "existing_HEAD=$current" | tee -a "$entry_log"
    if [[ -n "$expected" && "$expected" != "NONE" ]]; then
      if [[ "$current" != "$expected" ]]; then
        fail "Commit mismatch for $local_path: expected=$expected actual=$current — refusing to overwrite"
        return 1
      fi
      log "Commit matches expected: $expected"
    else
      log "No expected_commit pin (NONE); keeping existing clone at $current"
    fi
    # dirty worktree check
    if [[ -n "$(git -C "$local_path" status --porcelain)" ]]; then
      fail "Working tree dirty in $local_path — refusing to proceed"
      return 1
    fi
  else
    mkdir -p "$(dirname "$local_path")"
    log "Cloning $url -> $local_path (branch=$branch, recurse-submodules, LFS smudge skipped)"
    # Do not use --depth: need full history tags optionally; still skip LFS blobs
    if ! git clone --recurse-submodules -b "$branch" "$url" "$local_path" >>"$entry_log" 2>&1; then
      # retry without forcing branch name if remote default differs
      log "Clone with -b $branch failed; retrying without -b"
      rm -rf "$local_path"
      if ! git clone --recurse-submodules "$url" "$local_path" >>"$entry_log" 2>&1; then
        fail "Clone failed for $url"
        return 1
      fi
    fi
    if [[ -n "$expected" && "$expected" != "NONE" ]]; then
      local got
      got="$(git -C "$local_path" rev-parse HEAD)"
      if [[ "$got" != "$expected" ]]; then
        fail "Fresh clone HEAD $got != expected $expected — not auto-checking out another commit"
        return 1
      fi
    else
      log "Fresh clone pinned at HEAD $(git -C "$local_path" rev-parse HEAD) (no prior expected_commit)"
    fi
  fi

  # Ensure submodules initialized (no LFS smudge)
  git -C "$local_path" submodule update --init --recursive >>"$entry_log" 2>&1 || log "WARN: submodule update returned non-zero (may have no submodules)"

  collect_git_metadata "$local_path" | tee -a "$entry_log" >>"$RUN_LOG"
  estimate_sizes "$local_path" | tee -a "$entry_log" >>"$RUN_LOG"
  copy_license_refs "$method_id" "$local_path" "$license_status" "$license_spdx"

  local sha branch_now cdate tags_at_head
  sha="$(git -C "$local_path" rev-parse HEAD)"
  branch_now="$(git -C "$local_path" rev-parse --abbrev-ref HEAD)"
  cdate="$(git -C "$local_path" show -s --format=%cI HEAD)"
  tags_at_head="$(git -C "$local_path" tag --points-at HEAD | tr '\n' ',' | sed 's/,$//')"
  local du_total
  du_total="$(du -sh "$local_path" 2>/dev/null | awk '{print $1}')"

  printf '%s\n' \
    "$method_id	$role	$url	$local_path	$branch_now	$sha	$cdate	${tags_at_head:-none}	$license_status	$license_spdx	$wave	$du_total	ok" \
    >>"$SUMMARY_TSV"

  # Append lock fragment file for later assembly
  local frag="$LOG_DIR/lock_fragment_${method_id}_${role}.yml"
  cat >"$frag" <<EOF
  - method_id: ${method_id}
    role: ${role}
    repo_url: ${url}
    local_path: ${local_path}
    branch: ${branch_now}
    commit_sha: ${sha}
    commit_date: ${cdate}
    tags_at_head: ${tags_at_head:-[]}
    inclusion_decision: ${inclusion}
    license_status: ${license_status}
    license_spdx: ${license_spdx}
    wave: ${wave}
    submodule_status: see logs/cloning/${method_id}_${role}.log
    cloned_at: $(date -Iseconds)
    clone_command: "GIT_LFS_SKIP_SMUDGE=1 git clone --recurse-submodules -b ${branch} ${url} ${local_path}"
    git_lfs_skip_smudge: true
    size_on_disk: ${du_total}
EOF
  log "---- END $method_id ($role) OK sha=$sha size=$du_total ----"
  return 0
}

main() {
  log "ROOT=$ROOT"
  log "MANIFEST=$MANIFEST"
  log "GIT_LFS_SKIP_SMUDGE=$GIT_LFS_SKIP_SMUDGE"
  echo -e "method_id\trole\turl\tlocal_path\tbranch\tcommit_sha\tcommit_date\ttags\tlicense_status\tlicense_spdx\twave\tsize\tstatus" >"$SUMMARY_TSV"

  local failures=0
  while IFS='|' read -r method_id role url local_path branch expected inclusion license_status license_spdx wave; do
    [[ -z "$method_id" ]] && continue
    if ! clone_one "$method_id" "$role" "$url" "$local_path" "$branch" "$expected" "$inclusion" "$license_status" "$license_spdx" "$wave"; then
      failures=$((failures + 1))
      printf '%s\n' "$method_id	$role	$url	$local_path	$branch	UNKNOWN	UNKNOWN	none	$license_status	$license_spdx	$wave	UNKNOWN	failed" >>"$SUMMARY_TSV"
    fi
  done < <(parse_manifest)

  # Assemble REPOSITORIES.lock.yaml
  {
    echo "# REPOSITORIES.lock.yaml — generado por scripts/clone_repositories.sh"
    echo "# No modificar upstream/. Pins exactos de clones."
    echo "schema_version: \"0.2\""
    echo "updated_at: \"$(date -Iseconds)\""
    echo "policy:"
    echo "  clone_root: upstream"
    echo "  modify_upstream: false"
    echo "  git_lfs_skip_smudge: true"
    echo "  no_auto_checkout_without_evidence: true"
    echo "repositories:"
    cat "$LOG_DIR"/lock_fragment_*.yml 2>/dev/null || true
  } >"$LOCK_FILE"

  log "Lock written: $LOCK_FILE"
  log "Summary TSV: $SUMMARY_TSV"
  log "Failures: $failures"
  if [[ "$failures" -gt 0 ]]; then
    exit 1
  fi
}

main "$@"
