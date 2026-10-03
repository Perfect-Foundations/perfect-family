# API and Semantic Stability Policy

Perfect Foundations is intended for long-lived infrastructure use.

## Stability has two dimensions

### Source/API stability
SemVer-visible Rust items: types, traits, functions, modules, feature flags, and implementations that downstream code depends on.

### Semantic stability
Meaning that may remain source-compatible but still break users:
- rounding rules;
- canonical byte encodings;
- error classification;
- default algorithms;
- convergence criteria;
- unit definitions;
- constant-source editions;
- deterministic ordering;
- accepted/rejected input domains.

Perfect projects must treat semantic compatibility as seriously as source compatibility.

## Before 1.0

Pre-1.0 releases may evolve quickly, but:
- changes should still be documented;
- experimental modules/features should be named clearly;
- core representations should not churn casually;
- downstream migration cost should be considered.

## At 1.0

A crate should reach 1.0 only after:
- its scope boundary is stable;
- central representations and invariants are unlikely to be redesigned;
- error semantics are documented;
- feature policy is documented;
- MSRV policy exists;
- supported targets are documented;
- qualification gates applicable to the crate pass.

## Feature stability

Features should be:
- additive whenever practical;
- independent of environment autodetection for semantic behavior;
- documented as stable/experimental/internal;
- named by capability rather than implementation accident.

Default features should remain conservative.

## Deterministic behavior

If a crate promises deterministic output, a release must not silently change that output merely because:
- hash iteration order changed;
- thread scheduling changed;
- a different CPU feature was detected;
- an optimization selected a different approximation.

Intentional semantic-output changes require release notes and, where appropriate, a new mode/version.

## Canonical formats

Canonical wire formats, hashes, evidence identifiers, or persisted mathematical encodings require especially strict compatibility rules. Changes must be explicitly versioned.

## Deprecation

Prefer:
1. add replacement;
2. document migration;
3. deprecate old API;
4. leave a reasonable migration window;
5. remove only in a SemVer-compatible breaking release.

## Stability documentation

Each mature crate should maintain a compatibility section stating:
- current stability level;
- MSRV;
- target support;
- stable/experimental features;
- serialized/wire compatibility policy;
- numerical/semantic compatibility policy.
