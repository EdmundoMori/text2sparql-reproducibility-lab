#!/usr/bin/env python3
"""Metadata-only resolver for DBpedia 2016-10 endpoint-equivalent file inventory.

Hard rules:
- allowlisted hosts only
- directory listing GET / small metadata / checksum / DataID only
- HEAD for RDF/compressed candidates (never GET body of .ttl/.nt/.nq/.tql/.bz2/.gz)
- reject payload content types on GET
- record redirects, sizes, etag, last-modified, response SHA-256 of metadata only
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import urljoin, urlparse

ALLOWED_HOSTS = {
    "dbpedia.org",
    "www.dbpedia.org",
    "downloads.dbpedia.org",
    "databus.dbpedia.org",
    "api.github.com",
    "github.com",
    "raw.githubusercontent.com",
    "project-hobbit.eu",
    "sites.google.com",
    "arxiv.org",
    "doi.org",
    "api.crossref.org",
}

PAYLOAD_SUFFIXES = (
    ".ttl",
    ".nt",
    ".nq",
    ".tql",
    ".rdf",
    ".owl",
    ".bz2",
    ".gz",
    ".zip",
    ".tar",
)

METADATA_NAME_HINTS = (
    "checksum",
    "md5",
    "sha1",
    "sha256",
    "dataid",
    "void",
    "license",
    "readme",
    "index",
    ".html",
    ".txt",
    ".json",
    ".ttl.bz2.sha",  # rare
)

PAYLOAD_CONTENT_TYPES = (
    "application/x-bzip2",
    "application/gzip",
    "application/x-gzip",
    "application/octet-stream",
    "text/turtle",
    "application/n-triples",
    "application/n-quads",
)


class HrefParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.hrefs: list[str] = []

    def handle_starttag(self, tag: str, attrs) -> None:
        if tag.lower() != "a":
            return
        for k, v in attrs:
            if k.lower() == "href" and v:
                self.hrefs.append(v)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def host_allowed(url: str) -> bool:
    host = urlparse(url).hostname or ""
    return host in ALLOWED_HOSTS


def is_payload_path(url: str) -> bool:
    path = urlparse(url).path.lower()
    # checksum beside payload is metadata
    if any(x in path for x in ("md5", "sha1", "sha256", "checksum", "dataid")):
        return False
    return path.endswith(PAYLOAD_SUFFIXES)


def looks_metadata_name(name: str) -> bool:
    n = name.lower()
    return any(h in n for h in METADATA_NAME_HINTS) or n.endswith((".html", ".txt", ".json", ".csv"))


class Resolver:
    def __init__(self, out_dir: Path, log_path: Path, max_bytes_meta: int = 2_000_000) -> None:
        self.out_dir = out_dir
        self.log_path = log_path
        self.max_bytes_meta = max_bytes_meta
        self.out_dir.mkdir(parents=True, exist_ok=True)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.log_path.exists():
            self.log_path.write_text("")
        self.entries: list[dict] = []

    def log(self, method: str, url: str, status, nbytes: int, sha: str, note: str = "") -> None:
        line = f"{utc_now()} {method} {url} status={status} bytes={nbytes} sha256={sha} {note}\n"
        with self.log_path.open("a") as f:
            f.write(line)

    def _open(self, req: urllib.request.Request, timeout: int = 60):
        class Guard(urllib.request.HTTPRedirectHandler):
            def redirect_request(self, req, fp, code, msg, headers, newurl):
                if not host_allowed(newurl):
                    raise RuntimeError(f"redirect_denied:{newurl}")
                return urllib.request.HTTPRedirectHandler.redirect_request(
                    self, req, fp, code, msg, headers, newurl
                )

        opener = urllib.request.build_opener(Guard)
        return opener.open(req, timeout=timeout)

    def head(self, url: str, label: str) -> dict:
        if not host_allowed(url):
            raise RuntimeError(f"host_denied:{url}")
        req = urllib.request.Request(
            url,
            method="HEAD",
            headers={"User-Agent": "text2sparql-lab-p23-metadata/0.1"},
        )
        try:
            with self._open(req) as resp:
                status = getattr(resp, "status", 200) or 200
                final = resp.geturl()
                headers = {k.lower(): v for k, v in resp.headers.items()}
                meta = b""
                sha = hashlib.sha256(meta).hexdigest()
                self.log("HEAD", url, status, 0, sha, f"label={label} final={final}")
                return {
                    "url": url,
                    "final_url": final,
                    "status": status,
                    "headers": headers,
                    "content_length": headers.get("content-length"),
                    "content_type": headers.get("content-type"),
                    "etag": headers.get("etag"),
                    "last_modified": headers.get("last-modified"),
                }
        except Exception as e:
            self.log("HEAD", url, "ERR", 0, "n/a", f"label={label} err={e}")
            return {"url": url, "status": "ERR", "error": str(e)}

    def get_metadata(self, url: str, label: str, allow_html: bool = True) -> dict:
        if not host_allowed(url):
            raise RuntimeError(f"host_denied:{url}")
        if is_payload_path(url) and not looks_metadata_name(urlparse(url).path):
            raise RuntimeError(f"payload_get_denied:{url}")
        req = urllib.request.Request(
            url,
            method="GET",
            headers={"User-Agent": "text2sparql-lab-p23-metadata/0.1", "Accept": "*/*"},
        )
        with self._open(req) as resp:
            status = getattr(resp, "status", 200) or 200
            final = resp.geturl()
            if not host_allowed(final):
                raise RuntimeError(f"final_host_denied:{final}")
            ctype = (resp.headers.get("Content-Type") or "").lower()
            if any(p in ctype for p in PAYLOAD_CONTENT_TYPES) and "html" not in ctype and "xml" not in ctype and "json" not in ctype and "text/" not in ctype:
                # hard stop: do not read body
                raise RuntimeError(f"payload_content_type_denied:{ctype}")
            if is_payload_path(final) and not looks_metadata_name(urlparse(final).path):
                raise RuntimeError(f"payload_final_denied:{final}")
            chunks = []
            total = 0
            while True:
                chunk = resp.read(65536)
                if not chunk:
                    break
                total += len(chunk)
                if total > self.max_bytes_meta:
                    raise RuntimeError("metadata_oversized")
                chunks.append(chunk)
            data = b"".join(chunks)
            if not allow_html and b"<html" in data[:200].lower():
                raise RuntimeError("html_not_allowed")
            sha = hashlib.sha256(data).hexdigest()
            out = self.out_dir / f"{label}"
            out.write_bytes(data)
            self.log("GET", url, status, len(data), sha, f"label={label} final={final} ctype={ctype}")
            return {
                "url": url,
                "final_url": final,
                "status": status,
                "path": str(out),
                "bytes": len(data),
                "sha256": sha,
                "content_type": ctype,
                "headers": {k.lower(): v for k, v in resp.headers.items()},
            }

    def list_directory(self, url: str, label: str) -> list[str]:
        meta = self.get_metadata(url, f"{label}.html", allow_html=True)
        text = Path(meta["path"]).read_text(errors="ignore")
        parser = HrefParser()
        parser.feed(text)
        links = []
        for href in parser.hrefs:
            if href.startswith("?") or href.startswith("#") or href in ("../", "./"):
                continue
            full = urljoin(url if url.endswith("/") else url + "/", href)
            if host_allowed(full):
                links.append(full)
        # unique preserve order
        seen = set()
        out = []
        for u in links:
            if u not in seen:
                seen.add(u)
                out.append(u)
        (self.out_dir / f"{label}_links.json").write_text(json.dumps(out, indent=2))
        return out


def classify_file(url: str) -> dict:
    path = urlparse(url).path
    name = path.rsplit("/", 1)[-1]
    serialization = "UNKNOWN"
    compression = "none"
    if name.endswith(".ttl.bz2"):
        serialization, compression = "turtle", "bz2"
    elif name.endswith(".tql.bz2"):
        serialization, compression = "nquads_tql", "bz2"
    elif name.endswith(".nt.bz2"):
        serialization, compression = "ntriples", "bz2"
    elif name.endswith(".ttl"):
        serialization = "turtle"
    elif name.endswith(".tql"):
        serialization = "nquads_tql"
    directory = "/".join(path.strip("/").split("/")[:-1])
    component = "other"
    if "/core/" in path and "/core-i18n/" not in path:
        component = "core"
    elif "/links/" in path:
        component = "links"
    elif "/core-i18n/en/" in path:
        component = "core-i18n-en"
    elif name.lower().startswith(("md5sums", "sha", "checksum")):
        component = "checksum"
    return {
        "filename": name,
        "directory": directory,
        "serialization": serialization,
        "compression": compression,
        "dataset_component": component,
    }


def main(argv: Iterable[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--log", required=True)
    ap.add_argument("--summary", required=True)
    args = ap.parse_args(list(argv) if argv is not None else None)

    out_dir = Path(args.out_dir)
    log = Path(args.log)
    r = Resolver(out_dir, log)

    roots = [
        ("downloads_root", "https://downloads.dbpedia.org/2016-10/"),
        ("core_dir", "https://downloads.dbpedia.org/2016-10/core/"),
        ("links_dir", "https://downloads.dbpedia.org/2016-10/links/"),
        ("core_i18n_en_dir", "https://downloads.dbpedia.org/2016-10/core-i18n/en/"),
        ("archive_page", "https://downloads.dbpedia.org/wiki-archive/downloads-2016-10.html"),
        ("sparql_resources", "https://www.dbpedia.org/resources/sparql/"),
    ]

    inventory = []
    for label, url in roots:
        try:
            if url.endswith(".html") or "resources" in url or "wiki-archive" in url:
                r.get_metadata(url, f"{label}.html")
                continue
            links = r.list_directory(url, label)
            for link in links:
                clf = classify_file(link)
                # HEAD payload candidates; GET only metadata-looking names
                if is_payload_path(link) and not looks_metadata_name(urlparse(link).path):
                    head = r.head(link, f"head_{clf['filename'][:80]}")
                    inventory.append(
                        {
                            "source_url": link,
                            **clf,
                            "remote_size_bytes": head.get("content_length"),
                            "etag": head.get("etag"),
                            "last_modified": head.get("last_modified"),
                            "content_type": head.get("content_type"),
                            "head_status": head.get("status"),
                            "payload_requested": False,
                            "method": "HEAD",
                        }
                    )
                else:
                    # small metadata file GET
                    try:
                        safe = re.sub(r"[^A-Za-z0-9._-]+", "_", clf["filename"])[:120] or "meta"
                        meta = r.get_metadata(link, f"meta_{safe}")
                        inventory.append(
                            {
                                "source_url": link,
                                **clf,
                                "remote_size_bytes": meta.get("bytes"),
                                "etag": meta.get("headers", {}).get("etag"),
                                "last_modified": meta.get("headers", {}).get("last-modified"),
                                "content_type": meta.get("content_type"),
                                "head_status": meta.get("status"),
                                "payload_requested": False,
                                "method": "GET_METADATA",
                                "response_sha256": meta.get("sha256"),
                            }
                        )
                    except Exception as e:
                        inventory.append({"source_url": link, **clf, "error": str(e), "payload_requested": False})
            time.sleep(0.05)
        except Exception as e:
            r.log("GET", url, "ERR", 0, "n/a", f"label={label} err={e}")

    summary = {
        "generated_at": utc_now(),
        "inventory_count": len(inventory),
        "inventory": inventory,
    }
    Path(args.summary).write_text(json.dumps(summary, indent=2))
    print(json.dumps({"inventory_count": len(inventory), "summary": args.summary}, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
