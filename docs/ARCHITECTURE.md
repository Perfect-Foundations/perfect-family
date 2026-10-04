# Architecture

## Purpose

Perfect Foundations is a **directed family of independent crates**, not a linear stack and not a monolith.

The architectural objective is simple: the smallest system should pay only for the capabilities it actually uses.

## Layers

### Numerical substrate
`perfect-numeric` defines numerical semantics. `perfect-arithmetic`, `perfect-rational`, `perfect-float`, and `perfect-decimal` build exact and explicit representations on top of those semantics as appropriate.

### Mathematical substrate
`perfect-algebra`, `perfect-number-theory`, `perfect-math`, `perfect-complex`, `perfect-interval`, `perfect-polynomial`, `perfect-special-functions`, `perfect-calculus`, `perfect-differential-equations`, and `perfect-geometry` provide reusable mathematics.

### Probability and engineering substrate
`perfect-probability`, `perfect-statistics`, `perfect-information-theory`, `perfect-error-correction`, `perfect-optimization`, `perfect-signal`, `perfect-mechanics`, `perfect-estimation`, and `perfect-control` supply cross-domain scientific and engineering foundations.

### Quantum branch
Quantum Information supplies the mathematical model; Circuits represent executable programs; Simulation executes them; Compilation transforms them; Quantum Error Correction builds fault-tolerant/error-correction infrastructure.

### Domain foundations
Finance, Meteorology, Navigation, GNSS, Biosignal, Units, and Uncertainty consume only the lower foundations they actually need.

### Representation and evidence
`perfect-wire` provides canonical deterministic representation. `perfect-evidence` provides provenance/derivation/verification primitives. `perfect-codata` represents CODATA-specific authoritative data. `perfect-constants` aggregates authoritative constants without duplicating specialist implementations.

## Algorithms and metadata

Algorithms are owned by the specialist crate whose domain contract they implement
unless proven cross-crate reuse justifies extraction. Custom algorithms are
expected when they materially improve correctness, determinism, performance,
resource use, portability, embedded suitability, dependency weight, security, or
verification. A generic algorithm dumping ground is prohibited.

Metadata follows the same ownership rule. Domain-specific metadata stays with the
domain owner. Cross-domain provenance/derivation/canonical representation should
prefer intentional owners such as Perfect Evidence and Perfect Wire. A new shared
metadata primitive/crate is justified only after a stable independent contract
and real reuse are demonstrated.

See [Perfect Foundations Excellence Doctrine](EXCELLENCE-DOCTRINE.md).

## Perfectπ

Perfectπ is a specialist crate. Where another family crate genuinely needs π, it may consume Perfectπ.

Perfectπ is **not** a dumping ground for unrelated shared utilities. If a generally useful implementation technique from Perfectπ is needed elsewhere, it may be copied, adapted, or generalized into the appropriate independent crate.

## Dependency rules

- No dependency exists merely because one project was built earlier.
- Feature-gate optional integration where doing so prevents unnecessary dependency weight.
- Avoid circular dependencies.
- Prefer stable low-level semantic contracts over convenience coupling.
- Aggregator crates must not become alternate implementations of specialist domains.
- Cross-family integration belongs in `perfect-qualification`, not in hidden coupling.

## Target shape

The family is expected to form a DAG, with multiple sibling branches and optional integration edges rather than a single chain.
