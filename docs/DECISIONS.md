# Initial Decisions Record

This file preserves the major decisions established before implementation of the new family.

## D-001 — Family identity
The collection is named **Perfect Foundations**. Individual projects use descriptive names of the form **Perfect X** and package/repository names of the form `perfect-x`.

## D-002 — Perfectπ
Perfectπ is the first existing family member. It remains under `DrTomLLC/perfect-pi` until complete and in service. No early transfer.

## D-003 — Independent repositories
Family crates use independent repositories rather than a giant monorepo.

## D-004 — No umbrella runtime
There is no mandatory `perfect` crate that pulls the family together. Applications choose only needed crates.

## D-005 — Specialist ownership
Specialist crates own domain truth. Aggregators consume specialists rather than reimplementing them.

Examples:
- Perfect CODATA remains CODATA-specific.
- Perfect Constants is the unified constants layer.
- Perfect Math includes trigonometry rather than creating Perfect Trig.

## D-006 — Pure-Rust direction
Core functionality should be Pure Rust where practical. FFI may exist as optional interoperability/reference/acceleration.

## D-007 — Reuse
Proven code, algorithms, designs, tests, and verification methods may be reused across projects when appropriate. Dependencies are not created merely because code originated elsewhere.

## D-008 — Existing strong Rust ecosystems
Do not create Perfect crates simply to replace strong Rust-native networking, cryptography, FFT, linear algebra, time, serialization, ML/tensor, or domain libraries without a demonstrated missing contract.

## D-009 — Private reservation
The 40 new crate names are reserved privately during initial planning so architectural work is preserved without presenting empty repositories as completed public projects.

## D-010 — Cross-family qualification
`perfect-qualification` verifies compatibility, determinism, targets, MSRV, feature matrices, and integration across crate boundaries without owning production algorithms.
