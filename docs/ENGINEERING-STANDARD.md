# Engineering Standard

This document records the family-wide engineering direction. Individual crates may strengthen these rules when their domain requires it.

The governing optimization objective is defined in the [Perfect Foundations Excellence Doctrine](EXCELLENCE-DOCTRINE.md): correctness and explicit semantics are hard constraints; every other material dimension should be improved as far as evidence, domain requirements, and honest tradeoffs permit.

## Correctness

- Define behavior before optimizing it.
- Prefer explicit result types over silent fallback behavior.
- Make precision loss, rounding, overflow, underflow, saturation, truncation, and approximation visible in the API where material.
- Avoid panic-driven normal control flow.
- Treat edge cases, invalid states, NaN/infinity semantics, zero/sign behavior, and domain errors as first-class design work.

## Determinism and reproducibility

Where meaningful:
- same defined inputs and configuration should produce the same defined outputs;
- seeded stochastic operations should be reproducible;
- unordered execution must not silently change promised numerical results;
- canonical encodings must be byte-stable.

## Resource behavior

- Prefer bounded or caller-controlled resource use in low-level crates.
- Avoid hidden global state.
- Avoid unnecessary allocation.
- Support `no_std` where the domain and implementation reasonably permit it.
- Keep optional heavy functionality behind features.

## Rust policy

- Rust-first and Pure Rust by default.
- Unsafe code, when unavoidable, must be isolated, documented, justified, and tested.
- Production code should avoid `unwrap`, `expect`, `panic!`, `todo!`, and equivalent uncontrolled failure paths.
- MSRV is declared by each crate and changed intentionally.

## Verification

Use the strongest practical combination of:
- unit and property tests;
- independent reference generators;
- known-answer vectors;
- differential testing;
- fuzzing;
- mutation testing;
- sanitizers/Miri where applicable;
- cross-platform and cross-target CI;
- reproducibility checks;
- benchmark regression checks;
- external/reference implementation comparison.

## Performance and resource excellence

Optimization follows correctness, but it is not optional once the contract is
established. Projects should actively seek algorithmic, representation, and
implementation improvements in latency, throughput, scaling, memory, allocation,
stack, code/data size, dependency weight, startup cost, and target suitability.

Performance/resource work should:

- preserve the contract;
- compare against the strongest relevant alternatives;
- include reproducible benchmarks and retained versions/configurations;
- distinguish algorithmic improvements from machine-specific tuning;
- measure binary/code/data/stack/allocation behavior where material;
- keep specialized acceleration optional when a portable core is expected;
- prefer a measured Pareto-efficient default rather than an inherited historical default;
- record known material regressions/tradeoffs rather than hiding them.

Custom algorithms are encouraged when they materially improve the approved
contract and are backed by independent verification. See
[EXCELLENCE-DOCTRINE.md](EXCELLENCE-DOCTRINE.md).

## Documentation

Every public crate must document:
- scope and non-goals;
- correctness contract;
- supported representations;
- resource model;
- feature flags;
- MSRV;
- platform/target support;
- FFI/runtime requirements, if any;
- security or safety considerations where relevant.


## Ecosystem and distribution-grade adoption target

Perfect Foundations projects are intended to mature into infrastructure that can credibly be chosen as a default dependency by Rust applications and packaged by Linux distributions.

That target requires more than algorithmic correctness. Mature crates must also address:

- source/API and semantic stability;
- offline, source-first, reproducible packaging;
- no hidden network access in builds;
- minimal and auditable dependencies;
- documented MSRV and target support;
- additive feature discipline;
- crates.io/docs.rs quality;
- cross-compilation;
- supply-chain and build-script review;
- predictable maintenance and release processes.

The family does **not** claim present endorsement by the Rust project or any Linux distribution. “Default-grade” is an internal readiness bar that must be earned with evidence. See [ADOPTION-STANDARD.md](ADOPTION-STANDARD.md), [DISTRO-READINESS.md](DISTRO-READINESS.md), and [RELEASE-QUALITY-GATES.md](RELEASE-QUALITY-GATES.md).


## Architecture decisions and traceability

Every planned/active crate maintains durable design records.

Material architectural choices must be recorded as Architecture Decision Records under `docs/decisions/` according to [ADR-STANDARD.md](ADR-STANDARD.md).

Projects must also maintain:
- `docs/requirements/README.md` for stable requirement identities and records;
- `docs/TRACEABILITY.md` for the Requirement → ADR/design → Implementation → Verification evidence → Qualification/release-gate chain.

Architecture work is not complete merely because a design conversation occurred. Decisions that materially define representation, semantics, public API, dependencies, MSRV, target policy, `no_std`, unsafe/FFI boundaries, canonical formats, source authority, or compatibility must survive as repository records.

Requirements must not silently drift to match implementation after the fact. Changes are recorded and traced.

Canonical vocabulary for terms such as exact, correctly rounded, rigorous enclosure, deterministic, reproducible, canonical, verified, qualified, and default-grade is defined in [GLOSSARY.md](GLOSSARY.md).
