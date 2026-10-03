#!/usr/bin/env python3
"""Synchronize Perfect Family GitHub Project fields from crate project-status.toml files.

Requires an authenticated GitHub CLI session with permission to edit the
Perfect-Foundations organization Project.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tomllib
from dataclasses import dataclass


OWNER = "Perfect-Foundations"
PROJECT_NUMBER = 1
SUPPORT_REPOS = {".github", "perfect-family", "perfect-qualification"}


def run(*args: str, json_output: bool = False, check: bool = True) -> object | str:
    cp = subprocess.run(
        list(args),
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if check and cp.returncode != 0:
        raise RuntimeError(f"command failed: {' '.join(args)}\n{cp.stderr.strip()}")
    if json_output:
        return json.loads(cp.stdout)
    return cp.stdout


def gh(*args: str, json_output: bool = False, check: bool = True):
    return run("gh", *args, json_output=json_output, check=check)


@dataclass
class Field:
    id: str
    name: str
    type: str
    options: dict[str, str]


def load_fields() -> dict[str, Field]:
    raw = gh(
        "project", "field-list", str(PROJECT_NUMBER),
        "--owner", OWNER, "--format", "json",
        json_output=True,
    )
    out: dict[str, Field] = {}
    for item in raw["fields"]:
        opts = {o["name"]: o["id"] for o in item.get("options", [])}
        out[item["name"]] = Field(item["id"], item["name"], item["type"], opts)
    return out


def load_project():
    return gh(
        "project", "view", str(PROJECT_NUMBER),
        "--owner", OWNER, "--format", "json",
        json_output=True,
    )


def load_items():
    raw = gh(
        "project", "item-list", str(PROJECT_NUMBER),
        "--owner", OWNER, "--limit", "100", "--format", "json",
        json_output=True,
    )
    return {item["title"]: item for item in raw["items"]}


def load_repositories():
    repos = gh(
        "api", f"orgs/{OWNER}/repos?per_page=100&type=all",
        json_output=True,
    )
    return [r for r in repos if r["name"] not in SUPPORT_REPOS]


def load_status(repo_full_name: str) -> dict:
    raw = gh(
        "api",
        f"repos/{repo_full_name}/contents/project-status.toml",
        "-H", "Accept: application/vnd.github.raw",
    )
    if isinstance(raw, str):
        return tomllib.loads(raw)
    raise RuntimeError(f"unexpected status response for {repo_full_name}")


def edit_number(project_id: str, item_id: str, field: Field, value: int | float, dry: bool):
    if dry:
        return
    gh(
        "project", "item-edit",
        "--id", item_id,
        "--project-id", project_id,
        "--field-id", field.id,
        "--number", str(value),
    )


def edit_text(project_id: str, item_id: str, field: Field, value: str, dry: bool):
    if dry:
        return
    gh(
        "project", "item-edit",
        "--id", item_id,
        "--project-id", project_id,
        "--field-id", field.id,
        "--text", value,
    )


def edit_select(project_id: str, item_id: str, field: Field, option: str, dry: bool):
    if option not in field.options:
        raise RuntimeError(f"field {field.name!r} has no option {option!r}")
    if dry:
        return
    gh(
        "project", "item-edit",
        "--id", item_id,
        "--project-id", project_id,
        "--field-id", field.id,
        "--single-select-option-id", field.options[option],
    )


def create_item(title: str, body: str, dry: bool) -> dict:
    if dry:
        return {"id": "DRY-RUN", "title": title}
    return gh(
        "project", "item-create", str(PROJECT_NUMBER),
        "--owner", OWNER,
        "--title", title,
        "--body", body,
        "--format", "json",
        json_output=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    project = load_project()
    project_id = project["id"]
    fields = load_fields()
    items = load_items()
    repos = load_repositories()

    required_fields = {
        "Status", "Phase", "Target Version", "MSRV", "Visibility",
        "Audit Status", "Qualification Status", "Release Status",
        "Overall Progress", "Architecture Progress", "Implementation Progress",
        "Verification Progress", "Distro Readiness", "Default-Grade Readiness",
        "Current Milestone", "Next Gate", "Pending Decisions",
        "Blocking Issues", "CI Health",
    }
    missing = required_fields - fields.keys()
    if missing:
        raise RuntimeError(f"Project is missing required fields: {sorted(missing)}")

    count = 0
    for repo in sorted(repos, key=lambda r: r["name"]):
        status = load_status(repo["full_name"])
        title = status["identity"]["project"]
        item = items.get(title)
        body = (
            f"Repository: https://github.com/{repo['full_name']}\n\n"
            f"Authoritative live status: https://github.com/{repo['full_name']}/blob/main/project-status.toml\n\n"
            f"Project Blueprint: https://github.com/{repo['full_name']}/blob/main/docs/PROJECT-BLUEPRINT.md\n\n"
            f"Current: {status['lifecycle']['current_milestone']} — "
            f"{status['lifecycle']['current_milestone_name']} · "
            f"{status['progress']['overall_percent']}% overall · "
            f"{status['progress']['architecture_percent']}% architecture · "
            f"{status['progress']['default_grade_readiness_percent']}% default-grade readiness."
        )
        if item is None:
            item = create_item(title, body, args.dry_run)
            items[title] = item

        item_id = item["id"]
        p = status["progress"]
        w = status["work"]
        lifecycle = status["lifecycle"]
        release = status["release"]
        eng = status["engineering"]

        lifecycle_status = {
            "reserved": "Todo",
            "architecture": "In Progress",
            "implementation": "In Progress",
            "hardening": "In Progress",
            "qualification": "In Progress",
            "prerelease": "In Progress",
            "stable": "Done",
            "maintenance": "Done",
        }[lifecycle["stage"]]
        phase = {
            "reserved": "Planned",
            "architecture": "Architecture",
            "implementation": "Implementation",
            "hardening": "Hardening",
            "qualification": "Qualification",
            "prerelease": "Release",
            "stable": "Release",
            "maintenance": "Maintenance",
        }[lifecycle["stage"]]
        ci = {
            "not-configured": "Not Configured",
            "partial": "Partial",
            "passing": "Passing",
            "failing": "Failing",
            "blocked": "Blocked",
            "not-applicable": "Not Applicable",
        }[eng["ci_health"]]
        audit = {
            "not-started": "Not Started",
            "in-progress": "In Progress",
            "corrections-required": "Corrections Required",
            "passed": "Passed",
        }[eng["audit_status"]]
        qualification = {
            "not-started": "Not Started",
            "in-progress": "In Progress",
            "blocked": "Blocked",
            "passed": "Passed",
        }[eng["qualification_status"]]
        release_status = {
            "unreleased": "Unreleased",
            "prerelease": "Prerelease",
            "release-candidate": "Release Candidate",
            "released": "Released",
        }[release["release_status"]]

        numbers = {
            "Overall Progress": p["overall_percent"],
            "Architecture Progress": p["architecture_percent"],
            "Implementation Progress": p["core_implementation_percent"],
            "Verification Progress": p["verification_percent"],
            "Distro Readiness": p["distro_ecosystem_percent"],
            "Default-Grade Readiness": p["default_grade_readiness_percent"],
            "Pending Decisions": w["pending_architecture_gates"],
            "Blocking Issues": w["blocking_issues"],
        }
        texts = {
            "Current Milestone": f"{lifecycle['current_milestone']} — {lifecycle['current_milestone_name']}",
            "Next Gate": lifecycle["next_gate"],
            "Target Version": release["target_version"],
            "MSRV": release["msrv"],
        }
        selects = {
            "Status": lifecycle_status,
            "Phase": phase,
            "Visibility": "Public" if repo["visibility"] == "public" else "Private",
            "Audit Status": audit,
            "Qualification Status": qualification,
            "Release Status": release_status,
            "CI Health": ci,
        }

        print(
            f"{title}: overall={p['overall_percent']} architecture={p['architecture_percent']} "
            f"default-grade={p['default_grade_readiness_percent']} phase={phase}"
        )
        for field_name, value in numbers.items():
            edit_number(project_id, item_id, fields[field_name], value, args.dry_run)
        for field_name, value in texts.items():
            edit_text(project_id, item_id, fields[field_name], value, args.dry_run)
        for field_name, value in selects.items():
            edit_select(project_id, item_id, fields[field_name], value, args.dry_run)

        count += 1

    print(f"Synchronized {count} crate status rows.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
