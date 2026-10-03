# Supply-Chain and Build Security

Perfect Foundations aims to be suitable for infrastructure use, so dependency and build-system behavior are part of the product.

## Dependency principles

- Prefer fewer dependencies.
- Prefer Rust-native dependencies when capability and quality are comparable.
- Pinning is not a substitute for review.
- Optional capability should not become an unconditional dependency.
- Avoid abandoned or opaque dependencies for foundational behavior.

## Build scripts

`build.rs` is allowed only when justified.

Build scripts should not:
- access the network;
- inspect unrelated host state;
- execute downloaded binaries;
- silently alter numerical semantics based on undeclared environment state.

Generated files should be reproducible.

## Unsafe Rust

Unsafe code is not categorically forbidden, but every unsafe block/module should have:
- a stated invariant;
- a reason safe Rust is insufficient or materially worse;
- tests exercising boundary conditions;
- Miri/sanitizer coverage where applicable.

Crates that do not need unsafe should prefer `#![forbid(unsafe_code)]` or equivalent policy.

## Security advisories

Repositories should support private vulnerability reporting before wide public adoption.

Security-sensitive fixes should receive:
- severity assessment;
- affected-version analysis;
- regression tests;
- coordinated release notes/advisory when warranted.

## Cryptography boundary

Perfect Foundations does not equate “written in Rust” with “secure cryptography.”

Crates needing hashes/signatures/randomness should use mature reviewed implementations through narrow interfaces unless a dedicated, independently reviewed cryptographic project is explicitly established.

## Provenance of authoritative data

Constants, tables, standards-derived profiles, and reference vectors should record:
- source authority;
- source version/edition;
- retrieval/import method;
- transformation/generation script;
- verification method;
- retained hash where appropriate.
