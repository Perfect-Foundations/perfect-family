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

## Gate R5 — Performance ready
- representative benchmarks recorded;
- no known catastrophic regressions;
- resource behavior documented;
- comparisons to relevant reference implementations available.

## Gate R6 — Qualification ready
- applicable Perfect Qualification matrix passes;
- cross-crate conversions/integration pass;
- deterministic/canonical behaviors pass;
- release evidence retained.

## Gate R7 — Publication ready
- README/rustdoc/examples reflect actual implementation;
- changelog/release notes complete;
- version/feature/MSRV metadata correct;
- crates.io package inspected;
- Git tag/release created from exact qualified revision.

## Stable 1.0 gate

1.0 requires all applicable gates plus a deliberate API/semantic stability review.
