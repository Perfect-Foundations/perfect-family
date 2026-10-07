# Perfect Foundations Live Status System

Perfect Foundations uses one status model across every planned crate so progress can be compared without rewarding commits, lines of code, elapsed time, or subjective estimates.

## Source-of-truth hierarchy

1. **`project-status.toml` in each crate repository** — authoritative machine-readable status.
2. **README Live Project Status** — human-readable summary of the status file.
3. **Project Blueprint current-state section** — architecture-oriented summary linked to the status file.
4. **Perfect Family GitHub Project** — portfolio view synchronized from repository status.

If these disagree, `project-status.toml` is authoritative.

## Progress is gate-based

Progress is earned only by completing defined deliverables.

The overall score is a weighted composition:

| Dimension | Weight |
|---|---:|
| Architecture | 20% |
| Core implementation | 25% |
| Extended capability | 15% |
| Verification & hardening | 15% |
| Distro & ecosystem readiness | 10% |
| Perfect Qualification | 10% |
| Release readiness | 5% |
| **Total** | **100%** |

`overall = Σ(dimension_percent × dimension_weight)`

Percentages are rounded for display; the status file records the underlying gate counts.

## Current initial M0 baseline

The initial architecture dossier establishes 12 of 20 M0 architecture gates:

**Complete**
- purpose and scope documented;
- explicit non-goals documented;
- intended users/use cases documented;
- project blueprint present;
- capability map present;
- candidate core abstractions documented;
- candidate algorithm families documented;
- candidate error model documented;
- independent verification strategy documented;
- benchmark plan documented;
- risk register present;
- adoption/distro/default-grade requirements documented.

**Pending**
- canonical core representation finalized;
- public API draft reviewed;
- feature/dependency plan finalized;
- MSRV finalized;
- supported-target matrix finalized;
- no_std policy finalized;
- unsafe-code policy finalized;
- architecture decision review/ADR closure complete.

Therefore a newly documented-but-unimplemented Perfect crate begins at:

- Architecture: **60%**
- Core implementation: **0%**
- Extended capability: **0%**
- Verification & hardening: **0%**
- Distro & ecosystem readiness: **0%**
- Qualification: **0%**
- Release readiness: **0%**
- Weighted overall: **12%**

This does not mean “12% of the code is written.” It means 12% of the complete lifecycle gate weight has been objectively earned.

## Default-grade readiness

Default-grade readiness is intentionally separate from implementation progress.

A crate can be feature-complete and still be far from suitable as ecosystem infrastructure.

The default-grade checklist covers:
- stable semantic contract;
- critical correctness blockers;
- independent references;
- MSRV/target matrix;
- offline packaged build;
- dependency/license/advisory review;
- no hidden native/network build behavior;
- API + semantic SemVer policy;
- representative performance;
- resource behavior;
- fuzz/property/mutation evidence;
- unsafe/FFI review;
- docs.rs/crates.io quality;
- Perfect Qualification;
- serious downstream integration;
- security handling;
- maintenance/release process;
- distro packaging note;
- reproducible generated data;
- release evidence bundle.

Initial planning repositories have completed only the documentation/standards prerequisites, so the starting readiness score is **10%**.

## Lifecycle states

`reserved → architecture → implementation → hardening → qualification → prerelease → stable → maintenance`

A lifecycle state is not inferred from percentage alone. It changes only when its entry gate is satisfied. Where M1/M3/M5/M6 applies, the [Historical Proven-Reuse Gate](HISTORICAL-REUSE-GATE.md) is part of milestone closure; the review itself earns no percentage.

## Health states

- **on-track** — no known blocker preventing the current milestone.
- **at-risk** — material risk threatens the milestone.
- **blocked** — work cannot proceed without resolving a blocker.
- **paused** — intentionally inactive.
- **stable** — released and maintained.

Pending design decisions are not automatically blockers.

## CI states

- not-configured
- partial
- passing
- failing
- blocked
- not-applicable

A project with no implementation should normally report `not-configured`, not “passing.”

## Staleness

The status record includes `last_updated`.

Once active implementation begins, a status older than 30 days should be treated as **stale** unless the project is explicitly paused or stable.

## Status-update rule

Any change that materially affects one of these must update `project-status.toml` in the same change:

- lifecycle/milestone;
- gate completion;
- blocker count;
- readiness;
- CI state;
- MSRV/target status;
- release status;
- qualification status.

README and GitHub Project summaries should then be synchronized from the status source.

## What does NOT count as progress

No progress is awarded merely for:
- commits;
- lines of code;
- issues closed;
- PR count;
- time spent;
- documentation volume without completing a defined gate;
- benchmark speed without correctness;
- features that are outside the approved scope.

## Status integrity

A 100% value means every gate in that dimension is complete.

**100% overall** is reserved for a released project whose applicable architecture, implementation, extended scope, verification, distro/ecosystem, qualification, and release gates are all complete.

Stable maintenance does not reset the score; regressions or newly discovered release blockers may lower readiness/health until corrected.


## Automatic README synchronization

Every planned crate has:

- `project-status.toml` — authoritative machine-readable state;
- `.github/workflows/live-status.yml` — repository-local trigger;
- the shared reusable workflow in `perfect-family/.github/workflows/status-sync.yml`;
- the shared renderer in `perfect-family/tools/render_status.py`.

When `project-status.toml` changes on the default branch:

1. the repository calls the shared workflow;
2. the renderer parses the TOML with the Python standard library;
3. it validates gate counts, dimension percentages, weights, overall percentage, default-grade percentage, and update date;
4. it regenerates the README live dashboard;
5. it regenerates the Project Blueprint current-state summary;
6. `git diff --check` verifies the generated Markdown;
7. only changed generated documentation is committed back by `github-actions[bot]`.

The visible blocks are bounded by generated-section comments after the first synchronization. Content outside those blocks is not owned by the renderer.

The workflow does not award progress. It only renders values that are already supported by completed gates in the authoritative status file.

### Validation failures

The workflow fails rather than publishing misleading status when:

- progress weights do not total 100;
- a dimension percentage is outside 0–100;
- architecture percentage disagrees with architecture gate counts;
- default-grade readiness disagrees with readiness gate counts;
- weighted overall percentage disagrees with the dimension scores;
- required status keys are missing;
- `last_updated` is in the future.

This turns the progress display into a checked engineering artifact rather than a manually drawn bar.

## Perfect Family Project portfolio fields

The central GitHub Project carries a synchronized management view for every planned crate.

Live-status portfolio fields include:

- Overall Progress
- Architecture Progress
- Implementation Progress
- Verification Progress
- Distro Readiness
- Default-Grade Readiness
- Current Milestone
- Next Gate
- Pending Decisions
- Blocking Issues
- CI Health

These sit beside the existing Domain, Layer, Priority, Phase, Target Version, MSRV, Visibility, Audit Status, Qualification Status, and Release Status fields.

The repository status file remains authoritative if the board and repository ever disagree.

## Current initial family baseline — October 3, 2026

All 40 planned crates currently have:

- an authoritative `project-status.toml`;
- a detailed README live-status dashboard;
- a Project Blueprint current-state summary;
- a GitHub Project status row;
- the live-status synchronization workflow.

The initial common baseline is:

| Measure | Initial value |
|---|---:|
| Lifecycle | Architecture |
| Milestone | M0 — Architecture |
| Overall lifecycle | 12% |
| Architecture | 60% |
| Core implementation | 0% |
| Extended capability | 0% |
| Verification & hardening | 0% |
| Distro & ecosystem | 0% |
| Qualification | 0% |
| Release readiness | 0% |
| Default-grade readiness | 10% |
| Blocking issues | 0 |
| CI health | Not configured |

The common percentages are expected at this moment because every planned crate has completed the same documentation/architecture-dossier gates and none has begun production implementation. They should diverge naturally once individual projects advance.

Perfectπ is deliberately excluded from this rollout until its protected transfer milestone. Its existing repository and development process remain untouched.


## Portfolio synchronization tool

The repository README/blueprint synchronization is automatic through GitHub Actions.

The organization-level Perfect Family Project requires broader Project write permission than an ordinary repository `GITHUB_TOKEN`. For that reason, portfolio synchronization is performed by the authorized maintainer tool:

`tools/sync_project_status.py`

It:

1. reads all organization repositories except the three support repositories;
2. parses each crate's authoritative `project-status.toml`;
3. reads all Project fields and all Project items with explicit pagination limits;
4. creates a crate Project row if one does not exist;
5. synchronizes numeric progress/readiness values;
6. synchronizes milestone, next gate, MSRV, target version, phase, visibility, CI, audit, qualification, and release states;
7. leaves Domain, Layer, and Priority under the Project's architectural/management control.

Run a no-write validation first:

`python tools/sync_project_status.py --dry-run`

Then run without `--dry-run` from an authenticated `gh` session that has permission to edit the Perfect Foundations organization Project.

The tool was dry-run validated against all 40 crate status records on October 3, 2026.
