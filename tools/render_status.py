#!/usr/bin/env python3
"""Render Perfect Foundations live status blocks from project-status.toml."""

from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import sys
import tomllib

README_START = "<!-- PERFECT-STATUS:START -->"
README_END = "<!-- PERFECT-STATUS:END -->"
BLUEPRINT_START = "<!-- PERFECT-BLUEPRINT-STATUS:START -->"
BLUEPRINT_END = "<!-- PERFECT-BLUEPRINT-STATUS:END -->"


def pct_bar(percent: int) -> str:
    filled = round(percent / 5)
    filled = max(0, min(20, filled))
    return "█" * filled + "░" * (20 - filled)


def title_case_token(value: str) -> str:
    return value.replace("-", " ").replace("_", " ").title()


def status_label(value: str) -> str:
    labels = {
        "on-track": "On track",
        "at-risk": "At risk",
        "blocked": "Blocked",
        "paused": "Paused",
        "stable": "Stable",
        "not-configured": "Not configured",
        "not-started": "Not started",
        "not-tested": "Not tested",
        "not-published": "Not published",
        "unreleased": "Unreleased",
    }
    return labels.get(value, title_case_token(value))


def require(mapping: dict, *keys: str):
    cur = mapping
    for key in keys:
        if key not in cur:
            raise ValueError(f"missing required status key: {'.'.join(keys)}")
        cur = cur[key]
    return cur


def validate(data: dict) -> None:
    progress = require(data, "progress")
    weights = require(progress, "weights")
    architecture = require(data, "architecture")
    default_grade = require(data, "default_grade")

    if sum(int(v) for v in weights.values()) != 100:
        raise ValueError("progress weights must sum to 100")

    dims = (
        "architecture",
        "core_implementation",
        "extended_capability",
        "verification",
        "distro_ecosystem",
        "qualification",
        "release_readiness",
    )
    for dim in dims:
        value = int(require(progress, f"{dim}_percent"))
        if not 0 <= value <= 100:
            raise ValueError(f"{dim}_percent must be 0..100")

    arch_calc = round(100 * int(architecture["completed_count"]) / int(architecture["total_count"]))
    if arch_calc != int(progress["architecture_percent"]):
        raise ValueError(
            f"architecture_percent={progress['architecture_percent']} but gate counts calculate to {arch_calc}"
        )

    ready_calc = round(100 * int(default_grade["completed_count"]) / int(default_grade["total_count"]))
    if ready_calc != int(progress["default_grade_readiness_percent"]):
        raise ValueError(
            "default_grade_readiness_percent does not match default-grade gate counts"
        )

    overall_calc = round(
        sum(int(progress[f"{dim}_percent"]) * int(weights[dim]) for dim in dims) / 100
    )
    if overall_calc != int(progress["overall_percent"]):
        raise ValueError(
            f"overall_percent={progress['overall_percent']} but weighted dimensions calculate to {overall_calc}"
        )

    updated = dt.date.fromisoformat(require(data, "identity", "last_updated"))
    if updated > dt.date.today():
        raise ValueError("last_updated cannot be in the future")


def ready_state(completed: set[str], token: str, pending_text: str) -> str:
    return "Complete" if token in completed else pending_text


def render_dashboard(data: dict) -> str:
    identity = data["identity"]
    lifecycle = data["lifecycle"]
    progress = data["progress"]
    work = data["work"]
    release = data["release"]
    eng = data["engineering"]
    arch = data["architecture"]
    ready = data["default_grade"]

    q = list(arch.get("pending_design_questions", []))
    q_md = "\n".join(f"- [ ] {item}" for item in q) or "- [ ] No open design questions recorded"
    completed_ready = set(ready.get("completed", []))
    risk_text = work.get("known_design_risks", work.get("risk_register", "See Project Blueprint"))
    if isinstance(risk_text, int):
        risk_text = str(risk_text)
    elif risk_text == "documented-see-project-blueprint":
        risk_text = "Documented in the Project Blueprint"

    rows = [
        ("Overall lifecycle", progress["overall_percent"]),
        ("Architecture", progress["architecture_percent"]),
        ("Core implementation", progress["core_implementation_percent"]),
        ("Extended capability", progress["extended_capability_percent"]),
        ("Verification & hardening", progress["verification_percent"]),
        ("Distro & ecosystem", progress["distro_ecosystem_percent"]),
        ("Qualification", progress["qualification_percent"]),
        ("Release readiness", progress["release_readiness_percent"]),
        ("Default-grade readiness", progress["default_grade_readiness_percent"]),
    ]
    track_rows = "\n".join(
        f"| **{label}** | `{pct_bar(int(value))}` | **{int(value)}%** |" for label, value in rows
    )

    complete_arch = "\n".join(f"- [x] {title_case_token(x)}" for x in arch.get("completed", []))
    pending_arch = "\n".join(f"- [ ] {title_case_token(x)}" for x in arch.get("pending", []))

    dashboard = f"""{README_START}
## Live project status

> **Authoritative source:** [`project-status.toml`](project-status.toml) · Last updated **{identity['last_updated']}** · A status older than 30 days should be treated as stale unless the project is paused or stable. Progress is earned from completed engineering gates, not commits or lines of code.

| Status | Current value |
|---|---|
| **Lifecycle** | **{status_label(lifecycle['stage'])}** |
| **Health** | **{status_label(lifecycle['health'])}** |
| **Current milestone** | **{lifecycle['current_milestone']} — {lifecycle['current_milestone_name']}** |
| **Current focus** | {lifecycle['current_focus']} |
| **Next gate** | **{lifecycle['next_gate']}** |
| **Overall lifecycle progress** | **{progress['overall_percent']}%** |
| **Architecture progress** | **{progress['architecture_percent']}% — {arch['completed_count']} / {arch['total_count']} architecture gates complete** |
| **Core implementation** | **{progress['core_implementation_percent']}%** |
| **Extended capability** | **{progress['extended_capability_percent']}%** |
| **Verification & hardening** | **{progress['verification_percent']}%** |
| **Distro & ecosystem readiness** | **{progress['distro_ecosystem_percent']}%** |
| **Perfect Qualification** | **{progress['qualification_percent']}%** |
| **Release readiness** | **{progress['release_readiness_percent']}%** |
| **Default-grade readiness** | **{progress['default_grade_readiness_percent']}% — {ready['completed_count']} / {ready['total_count']} readiness gates complete** |
| **Blocking issues** | **{work['blocking_issues']}** |
| **Critical blockers** | **{work['critical_blockers']}** |
| **Open design questions** | **{work['open_design_questions']}** |
| **Pending architecture gates** | **{work['pending_architecture_gates']}** |
| **Known design risks** | {risk_text} |
| **CI health** | {status_label(eng['ci_health'])} |
| **Audit status** | {status_label(eng['audit_status'])} |
| **Qualification status** | {status_label(eng['qualification_status'])} |
| **Cargo package** | {status_label(eng['cargo_package'])} |
| **Offline build** | {status_label(eng['offline_build'])} |
| **docs.rs** | {status_label(eng['docs_rs'])} |
| **crates.io** | {status_label(eng['crates_io'])} |
| **`no_std` direction** | {status_label(eng['no_std'])} |
| **Unsafe policy** | {status_label(eng['unsafe_policy'])} |
| **FFI policy** | {status_label(eng['ffi_policy'])} |
| **MSRV** | {release['msrv']} |
| **License** | {release['license']} |
| **Version** | {release['version']} |
| **Target version** | {release['target_version']} |
| **Release state** | {status_label(release['release_status'])} |
| **Last qualified SHA** | {release['last_qualified_sha'] or 'None'} |
| **Last release** | {release['last_release'] or 'None'} |

### Progress by track

| Track | Progress | Percent |
|---|---|---:|
{track_rows}

<details>
<summary><strong>{lifecycle['current_milestone']} gate detail — {arch['completed_count']} complete / {len(arch.get('pending', []))} pending</strong></summary>

### Complete
{complete_arch}

### Pending
{pending_arch}

</details>

<details>
<summary><strong>Current project-specific design questions</strong></summary>

{q_md}

</details>

### Default-grade readiness snapshot

| Readiness area | State |
|---|---|
| Project design dossier | {ready_state(completed_ready, 'project-design-dossier', 'Pending')} |
| Family adoption/release standards linked | {ready_state(completed_ready, 'family-adoption-and-release-standards-linked', 'Pending')} |
| Stable semantic contract | {ready_state(completed_ready, 'stable-semantic-contract', 'Pending architecture closure')} |
| Critical correctness blockers zero | {ready_state(completed_ready, 'critical-correctness-blockers-zero', 'Not yet qualified')} |
| Independent reference qualification | {ready_state(completed_ready, 'independent-reference-qualification', 'Not started')} |
| MSRV / target matrix | {ready_state(completed_ready, 'msrv-and-target-matrix', 'TBD')} |
| Offline packaged build | {ready_state(completed_ready, 'offline-packaged-build', 'Not tested')} |
| Dependency / license / advisory review | {ready_state(completed_ready, 'dependency-license-advisory-review', 'Not started')} |
| No undocumented native/network build behavior | {ready_state(completed_ready, 'no-undocumented-native-network-build-behavior', 'Not yet qualified')} |
| API + semantic SemVer policy | {ready_state(completed_ready, 'api-and-semantic-semver-policy', 'Pending')} |
| Representative performance evidence | {ready_state(completed_ready, 'representative-performance-evidence', 'Not started')} |
| Resource behavior documented | {ready_state(completed_ready, 'resource-behavior-documented', 'Not started')} |
| Fuzz / property / mutation evidence | {ready_state(completed_ready, 'fuzz-property-mutation-evidence', 'Not started')} |
| Unsafe / FFI review | {ready_state(completed_ready, 'unsafe-ffi-review', 'Not started')} |
| docs.rs / crates.io release quality | {ready_state(completed_ready, 'docs-rs-crates-io-release-quality', 'Not published')} |
| Perfect Qualification | {ready_state(completed_ready, 'perfect-qualification', 'Not started')} |
| Serious downstream integration | {ready_state(completed_ready, 'serious-downstream-integration', 'Not started')} |
| Security handling | {ready_state(completed_ready, 'security-handling', 'Not started')} |
| Maintenance / release process | {ready_state(completed_ready, 'maintenance-and-release-process', 'Not established')} |
| Distro packaging note | {ready_state(completed_ready, 'distro-packaging-note', 'Not written')} |

The scoring and synchronization rules are defined in the [Perfect Foundations Status System](https://github.com/Perfect-Foundations/perfect-family/blob/main/docs/STATUS-SYSTEM.md).

{README_END}"""
    return dashboard


def render_blueprint_state(data: dict) -> str:
    identity = data["identity"]
    lifecycle = data["lifecycle"]
    progress = data["progress"]
    work = data["work"]
    arch = data["architecture"]
    ready = data["default_grade"]
    return f"""{BLUEPRINT_START}
## Current project state

| | |
|---|---|
| **Authoritative status** | [`project-status.toml`](../project-status.toml) |
| **Lifecycle** | {status_label(lifecycle['stage'])} |
| **Health** | {status_label(lifecycle['health'])} |
| **Milestone** | {lifecycle['current_milestone']} — {lifecycle['current_milestone_name']} |
| **Current focus** | {lifecycle['current_focus']} |
| **Overall progress** | {progress['overall_percent']}% |
| **Architecture** | {progress['architecture_percent']}% — {arch['completed_count']} / {arch['total_count']} gates |
| **Implementation** | {progress['core_implementation_percent']}% |
| **Verification** | {progress['verification_percent']}% |
| **Distro/ecosystem** | {progress['distro_ecosystem_percent']}% |
| **Qualification** | {progress['qualification_percent']}% |
| **Release readiness** | {progress['release_readiness_percent']}% |
| **Default-grade readiness** | {progress['default_grade_readiness_percent']}% — {ready['completed_count']} / {ready['total_count']} gates |
| **Blocking issues** | {work['blocking_issues']} |
| **Critical blockers** | {work['critical_blockers']} |
| **Open design questions** | {work['open_design_questions']} |
| **Next gate** | {lifecycle['next_gate']} |
| **Last status update** | {identity['last_updated']} |

The README contains the detailed live dashboard. This blueprint defines the design; `project-status.toml` defines the current measured state.

{BLUEPRINT_END}"""


def replace_generated(text: str, start: str, end: str, generated: str, heading: str, insert_before: str | None) -> str:
    marker_pattern = re.compile(re.escape(start) + r"[\s\S]*?" + re.escape(end))
    if marker_pattern.search(text):
        return marker_pattern.sub(generated, text, count=1)

    heading_pattern = re.compile(rf"(?ms)^{re.escape(heading)}\s*.*?(?=^## |\Z)")
    if heading_pattern.search(text):
        return heading_pattern.sub(generated + "\n\n", text, count=1)

    if insert_before and insert_before in text:
        return text.replace(insert_before, generated + "\n\n" + insert_before, 1)

    first_h2 = re.search(r"(?m)^## ", text)
    if first_h2:
        return text[: first_h2.start()] + generated + "\n\n" + text[first_h2.start():]
    return text.rstrip() + "\n\n" + generated + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("repository", nargs="?", default=".")
    args = parser.parse_args()

    root = pathlib.Path(args.repository).resolve()
    status_path = root / "project-status.toml"
    readme_path = root / "README.md"
    blueprint_path = root / "docs" / "PROJECT-BLUEPRINT.md"

    with status_path.open("rb") as fh:
        data = tomllib.load(fh)
    validate(data)

    dashboard = render_dashboard(data)
    blueprint_state = render_blueprint_state(data)

    readme = readme_path.read_text(encoding="utf-8")
    new_readme = replace_generated(
        readme,
        README_START,
        README_END,
        dashboard,
        "## Live project status",
        "## At a glance",
    )
    if new_readme != readme:
        readme_path.write_text(new_readme, encoding="utf-8")

    blueprint = blueprint_path.read_text(encoding="utf-8")
    new_blueprint = replace_generated(
        blueprint,
        BLUEPRINT_START,
        BLUEPRINT_END,
        blueprint_state,
        "## Current project state",
        None,
    )
    if new_blueprint != blueprint:
        blueprint_path.write_text(new_blueprint, encoding="utf-8")

    print(
        f"{data['identity']['project']}: overall={data['progress']['overall_percent']}% "
        f"architecture={data['progress']['architecture_percent']}% "
        f"default-grade={data['progress']['default_grade_readiness_percent']}%"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
