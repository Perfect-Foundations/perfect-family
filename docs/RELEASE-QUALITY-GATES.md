# Release Quality Gates

Perfect Foundations releases should be evidence-driven.

## Gate R0 — Architecture ready
- purpose and boundaries documented;
- core representations selected;
- dependency/reuse audit complete;
- verification strategy defined;
- unresolved questions classified as blocking/non-blocking.

## Gate R1 — Implementation ready
- core contract implemented;
- public errors documented;
- no normal production path relies on panic;
- unsafe code inventory exists;
- feature/dependency model established.

## Gate R2 — Correctness ready
- unit/property tests pass;
- independent reference tests exist where possible;
- edge/pathological cases covered;
- fuzzing plan active for parsers/stateful/high-risk code;
- numerical accuracy evidence available where relevant.

## Gate R3 — Portability ready
- MSRV passes;
- stable Rust passes;
- supported targets pass;
- no_std passes where claimed;
- offline build passes;
- packaged crate builds from its own tarball.

## Gate R4 — Supply-chain ready
- dependency licenses reviewed;
- advisories reviewed;
- build scripts reviewed;
- foreign/native dependencies documented;
- source/data provenance recorded.

## Gate R5 — Performance/resource excellence ready
- representative benchmarks recorded;
- strongest relevant competitor/reference baselines identified;
- no known catastrophic regressions;
- algorithmic scaling documented where material;
- memory/allocation/stack behavior documented where material;
- executable/code/data footprint measured where material;
- embedded/constrained-target resource evidence retained where claimed;
- comparisons use equivalent semantic/precision contracts;
- known material disadvantages are either corrected, justified by a stronger contract/tradeoff, or explicitly deferred with impact recorded;
- custom algorithms/representations are considered where they can materially improve the result;
- benchmark methodology distinguishes stable enforceable regression metrics from noisy host timing.

## Gate R6 — Qualification ready
- applicable Perfect Qualification matrix passes;
- cross-crate conversions/integration pass;
- deterministic/canonical behaviors pass;
- release evidence retained.

## Gate R7A — Registry-package ready while private
- README/rustdoc/examples reflect actual implementation;
- changelog/release notes are current;
- version/feature/MSRV metadata is correct;
- repository/homepage/documentation/readme/keywords/categories metadata is complete;
- `publish = false` remains enabled during private retention;
- crates.io package contents are inspected;
- packaged crate builds in all release-blocking feature configurations;
- packaged crate builds offline from a populated Cargo cache;
- private Perfect dependencies carry both an exact Git revision and a registry-compatible version requirement;
- the generated package manifest is checked for future registry compatibility;
- license/publication/security-channel fields may remain explicitly deferred until open-release authorization.

## Gate R7B — Open publication authorized
- the owner has explicitly authorized opening/publication;
- project license is selected and represented correctly in package/repository metadata;
- required crates.io names are available/claimed;
- public-facing vulnerability reporting is configured and verified;
- `publish = false` is removed only for the exact qualified release candidate;
- every non-development Perfect dependency has already been published bottom-up through the production dependency DAG;
- crates.io upload succeeds for the exact qualified revision;
- docs.rs output is verified;
- Git tag/release is created from the exact qualified revision;
- downstream release manifests are updated to consume released registry versions.

See [crates.io Readiness and Publication Policy](CRATES-IO-READINESS.md).

## Stable 1.0 gate

A private 1.0 candidate requires all applicable engineering/qualification gates
plus R7A and a deliberate API/semantic stability review.

A public 1.0 release additionally requires R7B.
