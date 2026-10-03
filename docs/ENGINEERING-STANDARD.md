# Engineering Standard

This document records the initial family-wide engineering direction. Individual crates may strengthen these rules when their domain requires it.

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

## Performance

Optimization follows correctness. Performance work should:
- preserve the contract;
- include reproducible benchmarks;
- distinguish algorithmic improvements from machine-specific tuning;
- keep specialized acceleration optional when a portable core is expected.

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
