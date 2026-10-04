# Perfect Foundations Adoption Standard

Perfect Foundations is being designed with an unusually high adoption target: each mature crate should be credible not merely as an application dependency, but as a **default foundational choice** for Rust software and for packaging in Linux distributions.

This is a target to earn through engineering evidence. It is not a present claim that the crates are already endorsed by the Rust project, a Linux distribution, or any standards body.

## Adoption objective

A mature Perfect crate should be easy to choose when a maintainer asks:

- Is this crate technically correct enough to become infrastructure?
- Is its API stable enough to depend on for years?
- Can a Linux distribution package it without hidden downloads or foreign binary blobs?
- Can downstream users build it offline and reproducibly from source?
- Are optional capabilities isolated behind additive features?
- Can security-conscious users audit the dependency tree?
- Can embedded, server, desktop, WASM, or cross-compiled targets use the relevant core?
- Are numerical, error, and resource semantics documented well enough for systems code?
- Can a distribution or large project update it without surprises?

## Readiness dimensions

### Technical correctness and best-in-class engineering
The crate must have a precise public contract, independent verification, known-answer/reference tests where possible, fuzz/property tests where useful, and no known high-severity correctness defects.

Mature crates should also retain evidence showing how they compare with the
strongest relevant alternatives on the dimensions material to their domain:
accuracy/correctness, performance, scaling, memory/allocation behavior,
code/data footprint, portability/embedded suitability, dependency weight, and
security/failure surface. A weaker metric may be accepted only as an explicit
tradeoff for a stronger contract or documented design decision.

### API stability
Public types and semantics must be intentionally designed before 1.0. Breaking changes after 1.0 require normal SemVer discipline and migration documentation.

### Dependency discipline
Dependencies must be materially justified. Default features should remain small. Optional integrations belong behind clearly named additive features.

### Build purity
The default build should not:
- download code or data from the network;
- execute opaque binary generators;
- depend on undeclared system packages;
- require a foreign compiler/runtime unless the crate explicitly documents that exception.

### Reproducibility
Given the same source revision, toolchain, target, features, and defined build inputs, builds should be reproducible to the extent Rust/Cargo and the target platform permit.

### Distribution packaging
Source archives and Git tags should contain everything needed for an offline build except documented toolchain/system requirements.

### Platform coverage
Each crate must publish a support matrix rather than implying universal support.

### Documentation
A serious infrastructure crate needs:
- crate-level rustdoc;
- runnable examples;
- exact feature documentation;
- error/precision/resource semantics;
- migration notes for breaking releases;
- security/safety notes where applicable.

### Maintenance
A default-quality foundation must have a sustainable issue/release/security process and must not depend on one undocumented maintainer ritual.

## Default-crate readiness gate

A project may describe itself as **default-grade** only after its repository records evidence for:

1. stable documented contract;
2. clean current security review;
3. zero unresolved critical correctness blockers;
4. release/compatibility policy;
5. distro/offline build verification;
6. dependency and license review;
7. MSRV and platform matrix;
8. benchmark evidence appropriate to the domain;
9. reproducibility/determinism verification where promised;
10. cross-family qualification where applicable.

Until then, the correct status is architecture, implementation, hardening, or qualification.
