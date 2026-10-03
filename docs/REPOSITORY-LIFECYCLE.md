# Repository Lifecycle

## Reserved
Repository name exists privately. README records intended scope. No implementation is implied.

## Architecture
Requirements, scope, non-goals, API principles, reuse audit, dependency analysis, references, and verification strategy are developed.

## Implementation
Core code begins only after the architecture is coherent enough to avoid needless rework.

## Hardening
Edge cases, fuzzing, mutation testing, sanitizers, performance, documentation, and target matrices are strengthened.

## Qualification
Crate-specific evidence and cross-family integration are verified, including `perfect-qualification` where applicable.

## Prerelease
Public API is usable but still allowed to change according to documented SemVer expectations.

## Stable
The crate reaches a documented stable contract.

## Maintenance
Compatibility, defects, standards updates, performance, and carefully scoped features continue.

## Visibility

Reserved/planning repositories may remain private. Public visibility is an intentional release decision, not an automatic consequence of repository creation.

## Perfectπ exception

Perfectπ is already public and remains under `DrTomLLC` until it is complete and in service. Transfer to Perfect Foundations happens only after that milestone and after transfer-readiness checks.
