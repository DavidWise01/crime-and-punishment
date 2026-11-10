#!/usr/bin/env python3
"""CRP 042 read-only, evidence-carrying archive audit. Standard library only."""
from __future__ import annotations
import datetime as dt
import hashlib
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "kernel" / "registry.json"
OUT = Path(os.environ.get("CRP_AUDIT_OUTPUT", str(ROOT / "dist" / "CRP-042-audit-report.json")))
EXPECTED = 41
FAMILIES = ("book", "film", "crosswalk")

class Links(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.title = ""
        self.in_title = False
    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.in_title = True
        for k, v in attrs:
            if tag in ("a", "script", "link", "img") and k in ("href", "src") and v:
                self.links.append(v)
    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
    def handle_data(self, data):
        if self.in_title:
            self.title += data

def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()

def resolve_href(origin: Path, target: str):
    url = urlsplit(target)
    if url.scheme or url.netloc or target.startswith("#") or target.startswith("mailto:"):
        return None
    if url.path.startswith("/"):
        return None  # absolute site paths can be host-root dependent
    if not url.path:
        return None
    path = (origin.parent / unquote(url.path)).resolve()
    try:
        path.relative_to(ROOT.resolve())
    except ValueError:
        return "EXTERNAL_TRAVERSAL"
    return path

def main():
    report = {
        "schema": "crp.audit.042.v1",
        "timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "repository": "DavidWise01/crime-and-punishment",
        "commit": os.environ.get("GITHUB_SHA", "local-checkout"),
        "observed": {"book": 0, "film": 0, "crosswalk": 0, "passed_files": 0, "blob_mismatches": 0},
        "errors": [],
        "warnings": [],
        "artifact_checks": [],
        "scope": "checkout file existence, Git-blob consistency, HTML title and relative link targets; no GUI or browser playback verification",
    }
    reg = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if reg.get("schema") != "crp.living-kernel.registry.v1":
        report["errors"].append("Registry schema mismatch")
    entries = reg.get("episodes", [])
    if len(entries) != EXPECTED:
        report["errors"].append("Registry count != 41")
    for idx, row in enumerate(entries, start=1):
        n = f"{idx:03d}"
        if row.get("id") != n:
            report["errors"].append(f"Noncanonical index {idx}")
        for kind in FAMILIES:
            entry = row.get(kind, {})
            name = entry.get("path", "")
            source_sha = entry.get("blob_sha", "")
            if not name or not re.fullmatch(
                (r"episodes/" + ("B" if kind == "book" else "F") + n + r"-[^/]+\.html")
                if kind != "crosswalk" else r"witness-crosswalk-" + n + r"\.html", name
            ):
                report["errors"].append(f"Bad {kind} path at {n}: {name}")
                continue
            path = ROOT / name
            record = {"id": n, "kind": kind, "path": name, "status": "error"}
            if not path.is_file():
                report["errors"].append(f"Missing {name}")
                report["artifact_checks"].append(record)
                continue
            data = path.read_bytes()
            report["observed"][kind] += 1
            calculated = git_blob_sha(data)
            record["blob_sha"] = calculated
            record["bytes"] = len(data)
            if calculated != source_sha:
                report["observed"]["blob_mismatches"] += 1
                report["errors"].append(f"Git blob differs for {name}: expected {source_sha}; found {calculated}")
            text = data.decode("utf-8", errors="replace")
            parser = Links()
            parser.feed(text)
            record["title"] = parser.title
            if not parser.title:
                report["warnings"].append(f"No HTML title: {name}")
            if "<canvas" not in text:
                report["warnings"].append(f"No Canvas element: {name}")
            for href in parser.links:
                target = resolve_href(path, href)
                if target == "EXTERNAL_TRAVERSAL":
                    report["warnings"].append(f"Path escapes repository: {name} -> {href}")
                elif isinstance(target, Path) and not target.exists():
                    report["warnings"].append(f"Unresolved relative link: {name} -> {href}")
            if kind == "book" and 15 <= idx <= 41:
                match = re.search(r"<header[^>]*>.*?<span[^>]*>(.*?)</span>", text, re.S)
                if match and ("B" + n) in match.group(1) and re.search(r"PART III\s*/\s*CHAPTER I", match.group(1)):
                    report["warnings"].append(f"Stale inherited chapter header: {name}")
            if kind in ("book", "film") and idx >= 15:
                if not re.search(r"const data=\[\[.*?\]\],book=", text, re.S):
                    report["warnings"].append(f"Nonstandard three-scene script pattern: {name}")
            if kind == "crosswalk" and idx > 1:
                for peer in (row["book"]["path"], row["film"]["path"]):
                    if peer not in text:
                        report["warnings"].append(f"Crosswalk does not link peer: {name} -> {peer}")
            record["status"] = "pass" if calculated == source_sha else "mismatch"
            if record["status"] == "pass":
                report["observed"]["passed_files"] += 1
            report["artifact_checks"].append(record)
    for kind in FAMILIES:
        if report["observed"][kind] != EXPECTED:
            report["errors"].append(f"{kind}: expected {EXPECTED}, got {report['observed'][kind]}")
    report["status"] = "fail" if report["errors"] else ("pass_with_warnings" if report["warnings"] else "pass")
    report["summary"] = {
        "expected_artifacts": 123,
        "observed_artifacts": sum(report["observed"][k] for k in FAMILIES),
        "error_count": len(report["errors"]),
        "warning_count": len(report["warnings"]),
        "browser_playback_verified": False,
        "github_pages_verified": False,
        "source_mirrors_independent": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({**report["summary"], "status": report["status"], "output": str(OUT)}))
    for issue in report["errors"][:30]:
        print("ERROR:", issue)
    for issue in report["warnings"][:30]:
        print("WARN:", issue)
    return 1 if report["errors"] else 0

if __name__ == "__main__":
    sys.exit(main())
