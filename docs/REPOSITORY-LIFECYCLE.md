# Repository Lifecycle

## Reserved
Repository name exists privately. README records intended scope. No implementation is implied.

## Architecture
Requirements, scope, non-goals, API principles, reuse audit, dependency analysis, references, and verification strategy are developed.

## Implementation
Core code begins only after the architecture is coherent enough to avoid needless rework. Before M1 closes, the project completes the applicable historical-reuse review defined by the family [Historical Proven-Reuse Gate](HISTORICAL-REUSE-GATE.md).

## Hardening
Edge cases, fuzzing, mutation testing, sanitizers, performance, documentation, and target matrices are strengthened. M5 hardening explicitly converts applicable LMES/Perfectπ historical defect classes into destination-specific regression/adversarial evidence or records a technical NOT_APPLICABLE disposition.

## Qualification
Crate-specific evidence and cross-family integration are verified, including `perfect-qualification` where applicable. M6 cannot newly close until M1/M3/M5 historical-reuse dispositions are revision-bound, independently re-verified where adapted, and free of unresolved release-blocking deferrals.

## Prerelease / private release candidate
Public API is usable but still allowed to change according to documented SemVer
expectations. Implemented Rust crates should already be crates.io-package-ready
here while retaining `publish = false`; license/publication/public-visibility
decisions may remain deferred until explicit open-release authorization.

## Stable
The crate reaches a documented stable contract. Stable private-candidate status
does not itself imply crates.io publication or public repository visibility.

## Maintenance
Compatibility, defects, standards updates, performance, and carefully scoped features continue.

## Visibility

Reserved/planning repositories may remain private. Public visibility is an intentional release decision, not an automatic consequence of repository creation.

## Perfectπ exception

Perfectπ is already public and remains under `DrTomLLC` until it is complete and in service. Transfer to Perfect Foundations happens only after that milestone and after transfer-readiness checks.
