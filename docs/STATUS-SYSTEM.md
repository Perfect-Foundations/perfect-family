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

A lifecycle state is not inferred from percentage alone. It changes only when its entry gate is satisfied.

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
