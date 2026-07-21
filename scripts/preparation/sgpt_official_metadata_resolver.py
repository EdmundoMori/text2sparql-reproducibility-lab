#!/usr/bin/env python3
"""Official metadata resolver for SGPT pin resolution (Prompt 12B).

Stdlib only. Allowlisted hosts. No package install. No wheel/image/model download.
"""
from __future__ import annotations

import hashlib
import json
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from email.parser import Parser
from pathlib import Path

ALLOWED_HOSTS = {
    "pypi.org",
    "files.pythonhosted.org",  # only if needed for METADATA via JSON redirect info — prefer JSON API
    "download.pytorch.org",
    "auth.docker.io",
    "registry-1.docker.io",
    "api.github.com",
    "raw.githubusercontent.com",
    "huggingface.co",
}

USER_AGENT = "text2sparql-reproducibility-lab/sgpt-pin-resolution-12B (+https://github.com/EdmundoMori/text2sparql-reproducibility-lab)"
TIMEOUT = 30


def _host_ok(url: str) -> str:
    host = urllib.parse.urlparse(url).hostname or ""
    if host not in ALLOWED_HOSTS:
        raise RuntimeError(f"host_not_allowlisted:{host}:{url}")
    return host


def fetch(url: str, dest_raw: Path, network_log: Path, classification: str, method: str = "GET") -> tuple[int, bytes]:
    _host_ok(url)
    req = urllib.request.Request(
        url,
        method=method,
        headers={"User-Agent": USER_AGENT, "Accept": "*/*"},
    )
    # GitHub API may need Accept
    if "api.github.com" in url:
        req.add_header("Accept", "application/vnd.github+json")
    ctx = ssl.create_default_context()
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
            status = resp.status
            data = resp.read() if method == "GET" else b""
            # for HEAD, some servers return body empty
            if method == "HEAD":
                data = b""
    except urllib.error.HTTPError as e:
        status = e.code
        data = e.read() if method == "GET" else b""
        # still log
        sha = hashlib.sha256(data).hexdigest() if data else ""
        size = len(data)
        dest_raw.parent.mkdir(parents=True, exist_ok=True)
        if data:
            dest_raw.write_bytes(data)
        with network_log.open("a", encoding="utf-8") as fh:
            fh.write(
                f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\t{method}\t{status}\t{size}\t{sha}\t{classification}\t{_host_ok(url)}\t{url}\tnon_binary_metadata_or_source\n"
            )
        raise
    sha = hashlib.sha256(data).hexdigest() if data else ""
    size = len(data)
    dest_raw.parent.mkdir(parents=True, exist_ok=True)
    if data:
        dest_raw.write_bytes(data)
    with network_log.open("a", encoding="utf-8") as fh:
        fh.write(
            f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\t{method}\t{status}\t{size}\t{sha}\t{classification}\t{_host_ok(url)}\t{url}\tnon_binary_metadata_or_source\n"
        )
    return status, data


def pypi_project(name: str, raw_dir: Path, network_log: Path) -> dict:
    url = f"https://pypi.org/pypi/{name}/json"
    status, data = fetch(url, raw_dir / f"pypi_{name}.json", network_log, "pypi_project_json")
    return json.loads(data.decode("utf-8"))


def pypi_release(name: str, version: str, raw_dir: Path, network_log: Path) -> dict:
    url = f"https://pypi.org/pypi/{name}/{version}/json"
    status, data = fetch(url, raw_dir / f"pypi_{name}_{version}.json", network_log, "pypi_release_json")
    return json.loads(data.decode("utf-8"))


def github_commits(owner: str, repo: str, path: str, raw_dir: Path, network_log: Path) -> list:
    url = f"https://api.github.com/repos/{owner}/{repo}/commits?path={urllib.parse.quote(path)}&per_page=5"
    safe = path.replace("/", "_")
    status, data = fetch(url, raw_dir / f"gh_commits_{owner}_{repo}_{safe}.json", network_log, "github_commits")
    return json.loads(data.decode("utf-8"))


def github_raw(owner: str, repo: str, ref: str, path: str, raw_dir: Path, network_log: Path) -> str:
    url = f"https://raw.githubusercontent.com/{owner}/{repo}/{ref}/{path}"
    safe = f"{owner}_{repo}_{ref}_{path}".replace("/", "_")
    status, data = fetch(url, raw_dir / f"raw_{safe}", network_log, "github_raw_source")
    return data.decode("utf-8", errors="replace")


def docker_token(repo: str, raw_dir: Path, network_log: Path) -> str:
    url = (
        "https://auth.docker.io/token?service=registry.docker.io"
        f"&scope=repository:{repo}:pull"
    )
    status, data = fetch(url, raw_dir / "docker_token.json", network_log, "docker_auth_token")
    return json.loads(data.decode())["token"]


def docker_manifest(repo: str, reference: str, token: str, raw_dir: Path, network_log: Path, accept: str) -> tuple[dict, dict]:
    url = f"https://registry-1.docker.io/v2/{repo}/manifests/{reference}"
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Authorization": f"Bearer {token}",
            "Accept": accept,
        },
    )
    _host_ok(url)
    ctx = ssl.create_default_context()
    with urllib.request.urlopen(req, timeout=TIMEOUT, context=ctx) as resp:
        status = resp.status
        data = resp.read()
        headers = {k.lower(): v for k, v in resp.headers.items()}
    sha = hashlib.sha256(data).hexdigest()
    dest = raw_dir / f"docker_manifest_{reference.replace(':','_').replace('/','_')}.json"
    dest.write_bytes(data)
    with network_log.open("a", encoding="utf-8") as fh:
        fh.write(
            f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\tGET\t{status}\t{len(data)}\t{sha}\tdocker_manifest\tregistry-1.docker.io\t{url}\tnon_binary_metadata_or_source\n"
        )
    return json.loads(data.decode()), headers


def pytorch_cpu_index(raw_dir: Path, network_log: Path) -> str:
    # simple index listing for cu117/cpu — use cpu index
    url = "https://download.pytorch.org/whl/cpu/torch/"
    try:
        status, data = fetch(url, raw_dir / "pytorch_cpu_torch_index.html", network_log, "pytorch_wheel_index")
        return data.decode("utf-8", errors="replace")
    except Exception as e:
        return f"ERROR:{e}"


def hf_gpt2(raw_dir: Path, network_log: Path) -> dict:
    url = "https://huggingface.co/api/models/gpt2"
    status, data = fetch(url, raw_dir / "hf_gpt2.json", network_log, "hf_model_metadata")
    return json.loads(data.decode())


def check_symbols_in_transformers_tag(tag: str, raw_dir: Path, network_log: Path) -> dict:
    """Static source inspection of huggingface/transformers at tag."""
    results = {}
    # __init__.py exports
    try:
        init_src = github_raw("huggingface", "transformers", tag, "src/transformers/__init__.py", raw_dir, network_log)
    except Exception as e:
        return {"error": str(e), "tag": tag}

    symbols_top = [
        "AdamW",
        "AutoConfig",
        "AutoTokenizer",
        "PreTrainedModel",
        "PreTrainedTokenizer",
        "get_linear_schedule_with_warmup",
    ]
    for s in symbols_top:
        # export patterns
        present = (
            f'"{s}"' in init_src
            or f"'{s}'" in init_src
            or re.search(rf"\b{s}\b", init_src) is not None
        )
        results[s] = {"present_in_init": bool(present)}

    # activations
    try:
        act = github_raw("huggingface", "transformers", tag, "src/transformers/activations.py", raw_dir, network_log)
        results["ACT2FN"] = {"present": "ACT2FN" in act}
    except Exception as e:
        results["ACT2FN"] = {"error": str(e)}

    # modeling_utils
    try:
        mu = github_raw("huggingface", "transformers", tag, "src/transformers/modeling_utils.py", raw_dir, network_log)
        results["Conv1D"] = {"present": "class Conv1D" in mu or "Conv1D =" in mu}
        results["find_pruneable_heads_and_indices"] = {"present": "def find_pruneable_heads_and_indices" in mu}
        results["prune_conv1d_layer"] = {"present": "def prune_conv1d_layer" in mu}
        results["from_pretrained"] = {"present": "def from_pretrained" in mu}
        results["save_pretrained"] = {"present": "def save_pretrained" in mu}
    except Exception as e:
        results["modeling_utils"] = {"error": str(e)}

    # gpt2
    gpt2_paths = [
        "src/transformers/models/gpt2/modeling_gpt2.py",
        "src/transformers/models/gpt2/__init__.py",
    ]
    gpt2_ok = False
    for p in gpt2_paths:
        try:
            src = github_raw("huggingface", "transformers", tag, p, raw_dir, network_log)
            if "GPT2PreTrainedModel" in src:
                gpt2_ok = True
                results["GPT2PreTrainedModel"] = {"present": True, "file": p}
                break
        except Exception:
            continue
    if not gpt2_ok:
        results["GPT2PreTrainedModel"] = {"present": False}

    # AdamW might be in optimization.py only and re-exported
    if not results.get("AdamW", {}).get("present_in_init"):
        try:
            opt = github_raw("huggingface", "transformers", tag, "src/transformers/optimization.py", raw_dir, network_log)
            results["AdamW"]["present_in_optimization"] = "class AdamW" in opt or "AdamW =" in opt
        except Exception as e:
            results["AdamW"]["optimization_error"] = str(e)

    all_ok = True
    required = [
        ("AdamW", lambda r: r.get("AdamW", {}).get("present_in_init") or r.get("AdamW", {}).get("present_in_optimization")),
        ("AutoConfig", lambda r: r.get("AutoConfig", {}).get("present_in_init")),
        ("AutoTokenizer", lambda r: r.get("AutoTokenizer", {}).get("present_in_init")),
        ("PreTrainedModel", lambda r: r.get("PreTrainedModel", {}).get("present_in_init")),
        ("PreTrainedTokenizer", lambda r: r.get("PreTrainedTokenizer", {}).get("present_in_init")),
        ("get_linear_schedule_with_warmup", lambda r: r.get("get_linear_schedule_with_warmup", {}).get("present_in_init")),
        ("ACT2FN", lambda r: r.get("ACT2FN", {}).get("present")),
        ("Conv1D", lambda r: r.get("Conv1D", {}).get("present")),
        ("find_pruneable_heads_and_indices", lambda r: r.get("find_pruneable_heads_and_indices", {}).get("present")),
        ("prune_conv1d_layer", lambda r: r.get("prune_conv1d_layer", {}).get("present")),
        ("GPT2PreTrainedModel", lambda r: r.get("GPT2PreTrainedModel", {}).get("present")),
        ("from_pretrained", lambda r: r.get("from_pretrained", {}).get("present")),
        ("save_pretrained", lambda r: r.get("save_pretrained", {}).get("present")),
    ]
    summary = {}
    for name, fn in required:
        ok = bool(fn(results))
        summary[name] = ok
        all_ok = all_ok and ok
    results["_summary"] = summary
    results["_all_required_present"] = all_ok
    results["tag"] = tag
    return results


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: sgpt_official_metadata_resolver.py <RUN_ID>", file=sys.stderr)
        return 2
    run_id = sys.argv[1]
    repo = Path(__file__).resolve().parents[2]
    raw_dir = repo / "workdir" / "metadata" / "sgpt-pin-resolution" / run_id / "raw"
    out_dir = repo / "workdir" / "metadata" / "sgpt-pin-resolution" / run_id / "normalized"
    log_dir = repo / "logs" / "environment-pin-resolution-sgpt" / run_id
    raw_dir.mkdir(parents=True, exist_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)
    log_dir.mkdir(parents=True, exist_ok=True)
    network_log = log_dir / "network.log"
    network_log.write_text(
        "timestamp_utc\tmethod\tstatus\tsize\tsha256\tclassification\thost\turl\tnote\n",
        encoding="utf-8",
    )

    summary = {"run_id": run_id, "errors": [], "packages": {}, "docker": {}, "transformers_checks": {}, "gpt2": {}, "pytorch_index_snippet": None}

    # PyPI packages
    for name in [
        "torch",
        "transformers",
        "numpy",
        "tqdm",
        "spacy",
        "nltk",
        "tensorboardX",
        "python-Levenshtein",
        "Unidecode",
        "optuna-dashboard",
        "pip",
        "setuptools",
        "wheel",
    ]:
        try:
            proj = pypi_project(name, raw_dir, network_log)
            info = proj.get("info", {})
            summary["packages"][name] = {
                "latest": info.get("version"),
                "requires_python": info.get("requires_python"),
                "release_count": len(proj.get("releases", {})),
                "yanked": info.get("yanked"),
            }
            # save compact version list with upload times
            versions = []
            for ver, files in proj.get("releases", {}).items():
                if not files:
                    continue
                upload = files[0].get("upload_time_iso_8601") or files[0].get("upload_time")
                versions.append({"version": ver, "upload_time": upload, "n_files": len(files)})
            versions.sort(key=lambda x: x["upload_time"] or "")
            (out_dir / f"{name}_versions.json").write_text(json.dumps(versions, indent=2) + "\n", encoding="utf-8")
        except Exception as e:
            summary["errors"].append(f"pypi:{name}:{e}")

    # torch 1.13.1 release detail
    try:
        trel = pypi_release("torch", "1.13.1", raw_dir, network_log)
        wheels = []
        for f in trel.get("urls", []):
            wheels.append(
                {
                    "filename": f.get("filename"),
                    "packagetype": f.get("packagetype"),
                    "python_version": f.get("python_version"),
                    "size": f.get("size"),
                    "digests": f.get("digests"),
                    "url": f.get("url"),
                    "yanked": f.get("yanked"),
                }
            )
        summary["torch_1_13_1"] = {
            "requires_python": trel.get("info", {}).get("requires_python"),
            "requires_dist": trel.get("info", {}).get("requires_dist"),
            "files": wheels,
        }
        (out_dir / "torch_1_13_1_files.json").write_text(json.dumps(wheels, indent=2) + "\n", encoding="utf-8")
    except Exception as e:
        summary["errors"].append(f"torch_release:{e}")

    # pytorch CPU index
    idx = pytorch_cpu_index(raw_dir, network_log)
    summary["pytorch_index_has_1_13_1"] = "1.13.1" in idx
    # extract matching wheel names
    matches = sorted(set(re.findall(r"torch-1\.13\.1[^\s\"'<>]*cp38[^\s\"'<>]*", idx)))
    summary["pytorch_cpu_cp38_matches"] = matches[:50]
    (out_dir / "pytorch_cpu_cp38_matches.json").write_text(json.dumps(matches, indent=2) + "\n", encoding="utf-8")

    # Docker python 3.8 tags — use GitHub docker-library/python for versions, then digest via registry
    try:
        # list tags via registry
        token = docker_token("library/python", raw_dir, network_log)
        # get specific tags of interest
        for tag in ["3.8", "3.8-slim-bookworm", "3.8-slim-bullseye", "3.8.20-slim-bookworm", "3.8.20-bullseye", "3.8.19-slim-bookworm"]:
            try:
                accept = "application/vnd.docker.distribution.manifest.list.v2+json,application/vnd.oci.image.index.v1+json,application/vnd.docker.distribution.manifest.v2+json"
                manifest, headers = docker_manifest("library/python", tag, token, raw_dir, network_log, accept)
                digest = headers.get("docker-content-digest") or headers.get("Docker-Content-Digest")
                amd64 = None
                if "manifests" in manifest:
                    for m in manifest["manifests"]:
                        plat = m.get("platform", {})
                        if plat.get("architecture") == "amd64" and plat.get("os") == "linux":
                            amd64 = m.get("digest")
                            break
                summary["docker"][tag] = {
                    "list_digest": digest,
                    "amd64_digest": amd64,
                    "schemaVersion": manifest.get("schemaVersion"),
                    "mediaType": manifest.get("mediaType"),
                    "n_manifests": len(manifest.get("manifests", [])),
                }
            except Exception as e:
                summary["docker"][tag] = {"error": str(e)}
    except Exception as e:
        summary["errors"].append(f"docker:{e}")

    # Temporal anchor via GitHub API on SGPT repo
    sgpt_files = ["requirements.txt", "train.py", "eval.py", "scripts/model.py", "utils/metrics.py", "README.md"]
    summary["sgpt_history"] = {}
    for path in sgpt_files:
        try:
            commits = github_commits("rashad101", "SGPT-SPARQL-query-generation", path, raw_dir, network_log)
            entries = []
            for c in commits:
                entries.append(
                    {
                        "sha": c.get("sha"),
                        "date": (c.get("commit") or {}).get("committer", {}).get("date")
                        or (c.get("commit") or {}).get("author", {}).get("date"),
                        "message": ((c.get("commit") or {}).get("message") or "")[:120],
                    }
                )
            summary["sgpt_history"][path] = entries
        except Exception as e:
            summary["sgpt_history"][path] = {"error": str(e)}

    # Transformers candidates — historically around 2022-12 torch 1.13.1
    # Prefer versions that still export AdamW at top-level and keep Conv1D APIs
    candidates = ["4.25.1", "4.26.1", "4.27.4", "4.28.1", "4.29.2", "4.30.2", "4.21.3", "4.24.0"]
    for ver in candidates:
        # pypi release info
        try:
            rel = pypi_release("transformers", ver, raw_dir, network_log)
            summary.setdefault("transformers_releases", {})[ver] = {
                "requires_python": rel.get("info", {}).get("requires_python"),
                "requires_dist": rel.get("info", {}).get("requires_dist"),
                "upload_time": (rel.get("urls") or [{}])[0].get("upload_time_iso_8601"),
            }
        except Exception as e:
            summary.setdefault("transformers_releases", {})[ver] = {"error": str(e)}
        # symbol check on tag v{ver}
        tag = f"v{ver}"
        try:
            summary["transformers_checks"][ver] = check_symbols_in_transformers_tag(tag, raw_dir, network_log)
        except Exception as e:
            summary["transformers_checks"][ver] = {"error": str(e)}

    # spaCy releases sample + models metadata via pypi en-core-web-sm
    for model in ["en-core-web-sm", "en-core-web-lg"]:
        try:
            proj = pypi_project(model, raw_dir, network_log)
            versions = list(proj.get("releases", {}).keys())[-15:]
            summary.setdefault("spacy_models", {})[model] = {
                "latest": proj.get("info", {}).get("version"),
                "sample_versions_tail": versions,
                "requires_python": proj.get("info", {}).get("requires_python"),
            }
        except Exception as e:
            summary.setdefault("spacy_models", {})[model] = {"error": str(e)}

    # NLTK release for a candidate
    for ver in ["3.7", "3.8", "3.8.1"]:
        try:
            rel = pypi_release("nltk", ver, raw_dir, network_log)
            summary.setdefault("nltk_releases", {})[ver] = {
                "requires_python": rel.get("info", {}).get("requires_python"),
                "upload_time": (rel.get("urls") or [{}])[0].get("upload_time_iso_8601"),
            }
        except Exception as e:
            summary.setdefault("nltk_releases", {})[ver] = {"error": str(e)}

    # inspect nltk meteor signature at tag
    try:
        met = github_raw("nltk", "nltk", "3.8.1", "nltk/translate/meteor_score.py", raw_dir, network_log)
        summary["nltk_meteor_signature_snip"] = "\n".join(
            [ln for ln in met.splitlines() if "def single_meteor_score" in ln or "def meteor_score" in ln][:5]
        )
    except Exception as e:
        summary["nltk_meteor_error"] = str(e)

    # GPT-2 metadata
    try:
        summary["gpt2"] = hf_gpt2(raw_dir, network_log)
    except Exception as e:
        summary["errors"].append(f"gpt2:{e}")

    # direct deps version probes around 2022-2023
    for name, vers in {
        "numpy": ["1.23.5", "1.24.4"],
        "tqdm": ["4.64.1", "4.65.0"],
        "spacy": ["3.4.4", "3.5.3"],
        "tensorboardX": ["2.5.1", "2.6"],
        "python-Levenshtein": ["0.20.9"],
        "Unidecode": ["1.3.6"],
    }.items():
        for ver in vers:
            try:
                rel = pypi_release(name, ver, raw_dir, network_log)
                summary.setdefault("direct_probe", {}).setdefault(name, {})[ver] = {
                    "requires_python": rel.get("info", {}).get("requires_python"),
                    "requires_dist": rel.get("info", {}).get("requires_dist"),
                    "upload_time": (rel.get("urls") or [{}])[0].get("upload_time_iso_8601"),
                    "wheels": [
                        {
                            "filename": f.get("filename"),
                            "python_version": f.get("python_version"),
                            "size": f.get("size"),
                            "sha256": (f.get("digests") or {}).get("sha256"),
                        }
                        for f in rel.get("urls", [])
                        if f.get("packagetype") == "bdist_wheel"
                    ],
                }
            except Exception as e:
                summary.setdefault("direct_probe", {}).setdefault(name, {})[ver] = {"error": str(e)}

    out = out_dir / "resolver_summary.json"
    # gpt2 can be huge — trim
    if isinstance(summary.get("gpt2"), dict):
        g = summary["gpt2"]
        summary["gpt2"] = {
            "id": g.get("id") or g.get("modelId"),
            "sha": g.get("sha"),
            "pipeline_tag": g.get("pipeline_tag"),
            "library_name": g.get("library_name"),
            "siblings": [
                {"rfilename": s.get("rfilename"), "size": s.get("size")}
                for s in (g.get("siblings") or [])[:30]
            ],
            "cardData_license": (g.get("cardData") or {}).get("license"),
            "tags": (g.get("tags") or [])[:20],
        }
    out.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"run_id": run_id, "summary_path": str(out), "errors": summary["errors"], "docker_tags": list(summary.get("docker", {})), "tf_ok": {k: v.get("_all_required_present") for k, v in summary.get("transformers_checks", {}).items()}}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
