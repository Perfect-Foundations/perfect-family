# Perfect Foundations Agent Instructions

This file is the authoritative repository instruction file for coding/research agents. Follow it before making changes.

## Non-negotiable truth rules

1. **Inspect live state before acting.** Never guess repository state. Read the current branch/SHA, origin state, worktree status, relevant CI, open PR/issues, and the governing family documents.
2. **Evidence before claims.** Never claim a build, test, CI job, file, commit, PR, qualification, package, target, release, or completion succeeded unless a tool result proves it. Apply the family [Claim Assurance Standard](docs/CLAIM-ASSURANCE-STANDARD.md): verification scope is exact, unknown stays unknown, and unavailable/indeterminate checks are not passing.
3. **Keep lifecycle states distinct.** Implemented != Verified != Qualified != Released. Do not collapse these states in prose or status.
4. **No progress inflation.** Progress is gate/evidence based. Commits, code volume, docs, elapsed time, or effort do not earn progress by themselves.
5. **Preserve concurrent work.** If a worktree is dirty or origin changed, inspect and reconcile. Never discard unknown changes, force-push, reset, or overwrite concurrent work.
6. **Do not promise background work.** Complete the current safe action now or report the concrete blocker.

## Sources of truth

Authority order:
1. this repository's architecture/policy documents;
2. each crate's `project-status.toml` for that crate's lifecycle/readiness state;
3. `perfect-qualification` for cross-family qualification evidence;
4. live `DrTomLLC/perfect-pi` for Perfectπ technical authority.

Do not invent a single family-wide percentage unless an authoritative family status model explicitly defines one.

## Perfectπ

Perfectπ is read-only from Perfect Foundations work. Never edit, commit, refactor, fix, merge into, or open corrective PRs against `DrTomLLC/perfect-pi` unless the user explicitly changes that rule. Reuse/generalize its proven techniques where appropriate, preserving provenance.

## Engineering doctrine

- Correctness -> explicit semantics -> mathematical rigor -> proven reuse -> family coherence -> reproducibility -> robustness -> minimal dependencies -> portability -> maintainability -> performance -> convenience.
- Reuse before reinvention. Inspect Perfectπ, existing Perfect crates, mature Rust crates, authoritative references, and the [Proven Reuse Register](docs/PROVEN-REUSE-REGISTER.md) before significant implementation. Preserve exact source/revision provenance when adapting work.
- Benchmark before optimization. Do not choose an algorithm, backend, cache, workspace, threshold, or unsafe path because it merely sounds faster.
- Numerical semantics are API semantics. Exactness, rounding, overflow, underflow, truncation, uncertainty, domain errors, and determinism must be explicit.
- Prefer Pure Rust, minimal dependencies, deterministic APIs, and `no_std` where practical.
- Unsafe/FFI/native code requires necessity, isolation, documentation, tests, and explicit review.
- Do not create duplicate shared primitives. Give each primitive one intentional owner in the family DAG.

## Required workflow

Before substantial work:
- fetch/prune origin and record repo, branch, HEAD, origin HEAD, and `git status`;
- read the relevant Blueprint, requirements, ADRs, traceability, status, CI, issues/PRs, dependency map, and build order;
- inspect reusable lower-layer/reference work;
- identify the actual requirement/root cause before editing.

Before commit/push:
- run the applicable CI-equivalent format/build/test/lint/doc/target matrix;
- run `git diff --check`;
- review for semantic/API/dependency/scope drift;
- update durable evidence/status only for gates actually earned;
- re-fetch origin and reconcile concurrent changes.

After work, report: repo/branch/SHA, changed files, reused work, commands/evidence, failures, blockers, readiness, and next action.

## Text/file integrity

Preserve repository encoding and line endings. Use explicit UTF-8 or byte-preserving edits for Markdown/TOML. On Windows, do not round-trip Unicode project files through text commands that can silently mojibake punctuation.

## Anti-drift rule

When a lower-level source of truth conflicts with a summary, fix the summary; do not reinterpret the requirement to match implementation. If a material decision changes, record it through the project's requirement/ADR/traceability process.
