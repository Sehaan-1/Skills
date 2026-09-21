#!/usr/bin/env python3
"""
fetch_package_facts.py — pull live maintenance/license facts from package registries.

Usage:
    python fetch_package_facts.py <ecosystem>:<package> [<ecosystem>:<package> ...]

Supported ecosystems:
    pypi      pypi:stripe
    npm       npm:express  or  npm:@stripe/stripe-js
    crates    crates:rdkafka
    rubygems  rubygems:stripe
    nuget     nuget:AWSSDK.S3
    maven     maven:org.apache.kafka:kafka-clients     (group:artifact)
    go        go:github.com/aws/aws-sdk-go-v2          (module path)

Prints one JSON report to stdout. Each package record includes (where the
registry provides it): latest version, release date, days since release, a
coarse maintenance signal, license, repository URL, and download counts.
A package that can't be resolved never aborts the run; it comes back with
"found": false and an error message, so partial results are still useful.

Standard library only — no pip installs needed.
"""

import gzip
import io
import json
import re
import socket
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone

USER_AGENT = "sdk-advisor-skill/1.0 (fetch_package_facts; registry metadata lookup)"
TIMEOUT = 15

ECOSYSTEMS = ("pypi", "npm", "crates", "rubygems", "nuget", "maven", "go")


def http_get(url, retries=1):
    """GET a URL, transparently gunzipping if the response is gzip-encoded.
    Retries once on transient TLS/connection resets, which flaky proxies cause."""
    last_err = None
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(
                url, headers={"User-Agent": USER_AGENT, "Accept": "*/*", "Accept-Encoding": "gzip"}
            )
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                raw = resp.read()
            if raw[:2] == b"\x1f\x8b":
                raw = gzip.decompress(raw)
            return raw
        except (urllib.error.URLError, socket.timeout, TimeoutError, ConnectionError, OSError) as e:
            last_err = e
            if attempt < retries:
                import time

                time.sleep(1.5)
    raise last_err


def parse_dt(value):
    """Parse an ISO-ish date/datetime string into an aware UTC datetime, or None."""
    if not value:
        return None
    value = str(value).strip()
    try:
        if value.endswith("Z"):
            value = value[:-1] + "+00:00"
        dt = datetime.fromisoformat(value)
    except ValueError:
        m = re.match(r"^(\d{4}-\d{2}-\d{2})", value)
        if not m:
            return None
        dt = datetime.strptime(m.group(1), "%Y-%m-%d")
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def days_since(dt):
    if dt is None:
        return None
    return max(0, (datetime.now(timezone.utc) - dt).days)


def maintenance_signal(days):
    """Coarse maintenance hint from release recency. The skill interprets it;
    a stale release doesn't prove abandonment, and vice versa."""
    if days is None:
        return "unknown"
    if days <= 182:
        return "active"     # release within ~6 months
    if days <= 400:
        return "slowing"    # 6–13 months
    return "stale"          # >~13 months without a release


def normalize_license(lic):
    """Registries encode licenses inconsistently (string, dict, list). Flatten to a string."""
    if lic is None:
        return None
    if isinstance(lic, dict):
        return lic.get("type") or lic.get("name") or None
    if isinstance(lic, list):
        return " OR ".join(str(x) for x in lic) if lic else None
    s = str(lic).strip()
    if len(s) > 160:  # PyPI free-text license fields can be the whole legal text
        s = s[:157] + "..."
    return s or None


def make_record(ecosystem, package, **fields):
    rec = {
        "package": package,
        "ecosystem": ecosystem,
        "found": True,
        "latest_version": None,
        "latest_release_date": None,
        "days_since_latest_release": None,
        "maintenance_signal": "unknown",
        "license": None,
        "repository": None,
        "homepage": None,
        "downloads": None,
        "downloads_period": None,
    }
    rec.update(fields)
    dt = parse_dt(rec.get("latest_release_date"))
    rec["latest_release_date"] = dt.date().isoformat() if dt else None
    d = days_since(dt)
    rec["days_since_latest_release"] = d
    rec["maintenance_signal"] = maintenance_signal(d)
    return rec


def err_record(ecosystem, package, message):
    return {
        "package": package,
        "ecosystem": ecosystem,
        "found": False,
        "error": message,
    }


# ---------------------------------------------------------------- ecosystems


# Map PyPI trove classifiers to SPDX-ish identifiers when metadata lacks a license field.
CLASSIFIER_LICENSE_MAP = {
    "MIT License": "MIT",
    "Apache Software License": "Apache-2.0",
    "BSD License": "BSD-3-Clause",
    "ISC License (ISCL)": "ISC",
    "Mozilla Public License 2.0 (MPL 2.0)": "MPL-2.0",
    "GNU General Public License v2 (GPLv2)": "GPL-2.0",
    "GNU General Public License v3 (GPLv3)": "GPL-3.0",
    "GNU Lesser General Public License v2 (LGPLv2)": "LGPL-2.1",
    "GNU Lesser General Public License v3 (LGPLv3)": "LGPL-3.0",
    "GNU Affero General Public License v3": "AGPL-3.0",
    "The Unlicense (Unlicense)": "Unlicense",
    "zlib/libpng License": "Zlib",
}


def pypi_license_from_classifiers(classifiers):
    hits = [
        c.split(" :: ")[-1]
        for c in classifiers or []
        if c.startswith("License :: OSI Approved ::")
    ]
    if not hits:
        return None
    mapped = [CLASSIFIER_LICENSE_MAP.get(h, h) for h in hits]
    return " OR ".join(dict.fromkeys(mapped))


def find_url(urls, wanted_keys, hosts=("github.com", "gitlab.com", "bitbucket.org")):
    """Case-insensitive lookup of project_urls, falling back to a host match."""
    lower = {str(k).lower(): v for k, v in (urls or {}).items() if v}
    for key in wanted_keys:
        if key in lower:
            return lower[key]
    for value in lower.values():
        if any(h in str(value) for h in hosts):
            return value
    return None


def fetch_pypi(package):
    data = json.loads(http_get(f"https://pypi.org/pypi/{urllib.parse.quote(package)}/json"))
    info = data.get("info", {})
    version = info.get("version")
    release_date = None
    files = data.get("releases", {}).get(version) or data.get("urls") or []
    if files:
        release_date = files[0].get("upload_time_iso_8601") or files[0].get("upload_time")
    urls = info.get("project_urls") or {}
    license_ = (
        info.get("license_expression")
        or normalize_license(info.get("license"))
        or pypi_license_from_classifiers(info.get("classifiers"))
    )
    return make_record(
        "pypi",
        package,
        latest_version=version,
        latest_release_date=release_date,
        license=license_,
        repository=find_url(urls, ("source", "repository", "code", "github")),
        homepage=info.get("home_page") or find_url(urls, ("homepage", "home")),
    )


def fetch_npm(package):
    name = urllib.parse.quote(package, safe="@")
    data = json.loads(http_get(f"https://registry.npmjs.org/{name}"))
    latest = (data.get("dist-tags") or {}).get("latest")
    release_date = (data.get("time") or {}).get(latest)
    repo = data.get("repository")
    if isinstance(repo, dict):
        repo = repo.get("url")
    downloads = None
    try:
        dl = json.loads(
            http_get(f"https://api.npmjs.org/downloads/point/last-week/{name}")
        )
        downloads = dl.get("downloads")
    except Exception:
        pass
    return make_record(
        "npm",
        package,
        latest_version=latest,
        latest_release_date=release_date,
        license=normalize_license(data.get("license")),
        repository=repo,
        homepage=data.get("homepage"),
        downloads=downloads,
        downloads_period="last-week",
    )


def fetch_crates(package):
    data = json.loads(http_get(f"https://crates.io/api/v1/crates/{urllib.parse.quote(package)}"))
    crate = data.get("crate", {})
    version = crate.get("max_stable_version") or crate.get("newest_version")
    release_date = crate.get("updated_at")
    # The version endpoint gives the exact publish date for the chosen version.
    if version:
        try:
            vdata = json.loads(
                http_get(
                    f"https://crates.io/api/v1/crates/{urllib.parse.quote(package)}/{version}"
                )
            )
            release_date = (vdata.get("version") or {}).get("created_at") or release_date
        except Exception:
            pass
    return make_record(
        "crates",
        package,
        latest_version=version,
        latest_release_date=release_date,
        license=crate.get("license"),
        repository=crate.get("repository"),
        homepage=crate.get("homepage"),
        downloads=crate.get("downloads"),
        downloads_period="all-time",
    )


def fetch_rubygems(package):
    data = json.loads(
        http_get(f"https://rubygems.org/api/v1/gems/{urllib.parse.quote(package)}.json")
    )
    return make_record(
        "rubygems",
        package,
        latest_version=data.get("version"),
        latest_release_date=data.get("version_created_at"),
        license=normalize_license(data.get("licenses")),
        repository=data.get("source_code_uri"),
        homepage=data.get("homepage_uri"),
        downloads=data.get("downloads"),
        downloads_period="all-time",
    )


def _version_key(v):
    parts = []
    for chunk in re.split(r"[.\-+]", str(v)):
        parts.append((0, int(chunk), "") if chunk.isdigit() else (1, 0, chunk))
    return parts


def fetch_nuget(package):
    lower = package.lower()
    index = json.loads(
        http_get(f"https://api.nuget.org/v3/registration5-gz-semver2/{lower}/index.json")
    )
    pages = index.get("items", [])
    leaves = []
    for page in pages:
        if "items" in page:
            leaves.extend(page["items"])
        elif page.get("@id"):  # paged registration — fetch the page itself
            try:
                leaves.extend(json.loads(http_get(page["@id"])).get("items", []))
            except Exception:
                pass
    stable = []
    for leaf in leaves:
        entry = leaf.get("catalogEntry", {})
        ver = entry.get("version")
        if ver and "-" not in ver:
            stable.append((ver, entry))
    if not stable:
        return err_record("nuget", package, "package found but no stable versions listed")
    stable.sort(key=lambda kv: _version_key(kv[0]))
    version, entry = stable[-1]
    return make_record(
        "nuget",
        package,
        latest_version=version,
        latest_release_date=entry.get("published"),
        license=entry.get("licenseExpression") or entry.get("licenseUrl"),
        repository=None,
        homepage=None,
    )


def fetch_maven(package):
    if ":" not in package:
        return err_record("maven", package, "maven needs group:artifact, e.g. maven:com.stripe:stripe-java")
    group, artifact = package.split(":", 1)
    q = urllib.parse.quote(f'g:"{group}" AND a:"{artifact}"')
    data = json.loads(
        http_get(f"https://search.maven.org/solrsearch/select?q={q}&rows=1&wt=json")
    )
    docs = data.get("response", {}).get("docs", [])
    if not docs:
        return err_record("maven", package, "not found on Maven Central search")
    doc = docs[0]
    version = doc.get("latestVersion")
    ts = doc.get("timestamp")
    release_date = (
        datetime.fromtimestamp(ts / 1000, tz=timezone.utc).isoformat() if ts else None
    )
    license_name = None
    try:
        pom_url = (
            "https://repo1.maven.org/maven2/"
            f"{group.replace('.', '/')}/{artifact}/{version}/{artifact}-{version}.pom"
        )
        pom = http_get(pom_url).decode("utf-8", errors="replace")
        m = re.search(r"<license>\s*<name>\s*(.*?)\s*</name>", pom, re.DOTALL)
        if m:
            license_name = m.group(1)
    except Exception:
        pass
    return make_record(
        "maven",
        package,
        latest_version=version,
        latest_release_date=release_date,
        license=license_name,
        repository=doc.get("scm") if isinstance(doc.get("scm"), str) else None,
        homepage=None,
    )


def _go_case_encode(module):
    """Go module proxy escapes uppercase letters as '!' + lowercase."""
    return "".join(("!" + ch.lower()) if ch.isupper() else ch for ch in module)


def fetch_go(package):
    data = json.loads(
        http_get(f"https://proxy.golang.org/{_go_case_encode(package)}/@latest")
    )
    return make_record(
        "go",
        package,
        latest_version=data.get("Version"),
        latest_release_date=data.get("Time"),
        license=None,  # the Go proxy doesn't serve license data
        repository="https://" + package,
        homepage=None,
    )


FETCHERS = {
    "pypi": fetch_pypi,
    "npm": fetch_npm,
    "crates": fetch_crates,
    "rubygems": fetch_rubygems,
    "nuget": fetch_nuget,
    "maven": fetch_maven,
    "go": fetch_go,
}


def fetch_one(spec):
    if ":" not in spec:
        return err_record("?", spec, f"bad spec '{spec}' — expected ecosystem:package")
    ecosystem, package = spec.split(":", 1)
    ecosystem = ecosystem.strip().lower()
    package = package.strip()
    if ecosystem not in FETCHERS:
        return err_record(ecosystem, package, f"unsupported ecosystem '{ecosystem}' (one of {', '.join(ECOSYSTEMS)})")
    try:
        return FETCHERS[ecosystem](package)
    except urllib.error.HTTPError as e:
        return err_record(ecosystem, package, f"HTTP {e.code} from {ecosystem} registry")
    except urllib.error.URLError as e:
        return err_record(ecosystem, package, f"network error: {getattr(e, 'reason', e)}")
    except (socket.timeout, TimeoutError):
        return err_record(ecosystem, package, "request timed out")
    except Exception as e:  # noqa: BLE001 — partial results beat crashing the whole run
        return err_record(ecosystem, package, f"{type(e).__name__}: {e}")


def main():
    specs = [a for a in sys.argv[1:] if a not in ("-h", "--help")]
    if not specs or len(sys.argv[1:]) != len(specs):
        sys.stderr.write(__doc__ + "\n")
        if not specs:
            sys.exit(2)
    report = {
        "fetched_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "packages": [fetch_one(s) for s in specs],
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
