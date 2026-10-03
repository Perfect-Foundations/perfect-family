# Perfect Foundations Glossary & Terminology Standard

This document defines the canonical meaning of high-value terms used across Perfect Foundations.

The goal is not linguistic formality. The goal is to prevent two crates from using the same word to mean different engineering guarantees.

When a crate needs a stricter domain-specific definition, it may strengthen a term, but it must not silently weaken or contradict the family definition.

## Guarantee vocabulary

### Exact

A result is **exact** when it represents the mathematical result without approximation or information loss within the stated mathematical domain.

Examples:
- arbitrary-precision integer addition;
- rational arithmetic;
- finite decimal addition when the exact finite-decimal result is representable by the type.

“Exact” must not be used merely because a computation is deterministic.

### Representationally exact

A conversion is **representationally exact** when the destination representation denotes exactly the same value as the source.

Example: an integer converted to a binary float only when that integer is exactly representable at the destination precision.

### Lossless

A transformation is **lossless** when all information that the contract promises to preserve can be recovered or retained.

Lossless is broader than numeric exactness. A wire encoding can be lossless even when it is not itself a numerical operation.

### Correctly rounded

A finite result is **correctly rounded** when it is the result obtained by applying the stated rounding mode exactly once to the exact mathematical result.

Claims of correct rounding require evidence appropriate to the supported domain.

### Faithfully rounded

A result is **faithfully rounded** when it is one of the two adjacent representable values surrounding the exact mathematical result.

Faithful rounding is weaker than correct rounding and must be labeled as such.

### Bounded-error

A result has a **bounded error** when the implementation states and verifies a numeric upper bound on its error under the documented assumptions.

“High accuracy” without a bound is not equivalent.

### Rigorous enclosure

A value is **rigorously enclosed** when a returned interval/ball/set is guaranteed to contain the mathematical result under the documented model.

A statistically likely range is not a rigorous enclosure.

### Certified / verified result

A result is **certified** or **verified** only when evidence establishes the stated mathematical/semantic property, such as a root enclosure, proof witness, certificate, or independently checked condition.

Do not use “verified” merely to mean “unit tests passed.”

## Precision and error vocabulary

### Precision

**Precision** describes the resolution/capacity of a representation or computation, such as bits, digits, or an explicit working precision.

Precision is not the same as accuracy.

### Accuracy

**Accuracy** describes closeness to the intended true/reference value under the stated metric.

A high-precision result can still be inaccurate.

### Tolerance

A **tolerance** is a caller- or algorithm-defined threshold used for convergence, equivalence, stopping, or acceptance.

Tolerances must identify what quantity they apply to and whether they are absolute, relative, mixed, or domain-specific.

### Approximation

An **approximation** is a result that intentionally does not preserve exact mathematical identity.

Approximation must be explicit when it can materially affect correctness.

### Numerical loss

**Numerical loss** includes rounding, truncation, saturation, overflow handling, underflow handling, quantization, or other representation changes that alter value/information.

Material loss should be visible through API semantics.

## Interval, uncertainty, and probability

### Interval / enclosure

An **interval** represents a set of possible mathematical values and, when used rigorously, guarantees containment.

### Measurement uncertainty

**Measurement uncertainty** characterizes uncertainty associated with a measured/derived quantity under a stated measurement model.

It is not automatically a hard bound and is not interchangeable with interval enclosure.

### Probability distribution

A **probability distribution** describes probability mass/density under a stochastic model.

It is not automatically an uncertainty budget or enclosure.

### Confidence / coverage

Confidence or coverage terminology must state the statistical/metrological model and level. It must not be presented as certainty.

## Determinism and reproducibility

### Deterministic

An operation is **deterministic** when the same defined inputs and configuration produce the same defined output under the documented contract.

If hardware/backend-dependent variation is allowed, that limitation must be stated.

### Reproducible

A result/process is **reproducible** when another permitted environment can regenerate the stated result/evidence from the recorded inputs, configuration, versions, and procedure.

Reproducibility may be byte-for-byte or semantic/numerical; the promised level must be stated.

### Order-invariant

An operation is **order-invariant** when permitted reordering of inputs/evaluation does not change the promised result.

Deterministic does not automatically imply order-invariant.

### Seeded reproducibility

A stochastic algorithm has **seeded reproducibility** only when the RNG, seed/state, algorithm version, and relevant configuration are sufficient to reproduce the promised output sequence/result.

## Representation and identity

### Canonical

A representation is **canonical** when each logical value/identity covered by the contract has exactly one permitted canonical representation.

Canonicality must define treatment of details such as:
- map ordering;
- integer encodings;
- decimal scale;
- rational normalization;
- floating NaNs and signed zero;
- unknown fields;
- schema versions.

### Semantic identity

**Semantic identity** means two values/artifacts are considered the same under the domain contract.

Semantic identity can differ from byte identity.

### Byte identity

**Byte identity** means exact equality of the serialized byte sequence.

### Stable identifier

A **stable identifier** is designed to retain identity across allowed renames, display changes, or source-edition changes according to its documented scope.

## Evidence and provenance

### Evidence

**Evidence** is retained information that supports verification of a claim, result, source, transformation, or release assertion.

Evidence does not itself guarantee truth.

### Provenance

**Provenance** records origin and derivation: where something came from, what transformed it, with what inputs/configuration/tool/version, and how outputs relate to sources.

### Authority

An **authority** is the designated authoritative source for a class of facts/data.

Examples may include CODATA/BIPM for specified scientific data or an owning Perfect specialist crate for family semantics.

### Source of truth

A **source of truth** is the record designated authoritative within a defined system.

Examples:
- `project-status.toml` is the status source of truth;
- specialist crates own specialist truth;
- the Perfect Family catalog owns family membership records.

### Specialist owns truth

A specialist crate is authoritative for its bounded domain. Aggregators and consumers delegate rather than duplicate that truth.

Example: Perfect Constants delegates π to Perfectπ and CODATA physical constants to Perfect CODATA.

### Aggregator

An **aggregator** provides a unified interface over specialist sources without redefining or silently flattening specialist semantics.

## Verification vocabulary

### Verification

**Verification** asks whether an implementation/result satisfies its stated technical contract.

### Validation

**Validation** asks whether the chosen model/contract is appropriate for the intended use.

The terms may overlap in domain standards, but Perfect documentation should distinguish them when material.

### Qualification

**Qualification** is the recorded evidence process demonstrating that a crate or supported crate combination passes the applicable Perfect release/integration gates.

Qualification is stronger and broader than a passing unit-test suite.

### Oracle / independent reference

An **oracle** or **independent reference** is a sufficiently independent source used to check behavior/results.

It can be:
- a mature external implementation;
- a standard dataset;
- a high-precision calculation;
- an analytic result;
- a separately implemented checker.

The independence and limitations must be documented.

### Golden / known-answer vector

A **golden vector** is a retained input/output or evidence vector whose expected result is fixed and reviewable.

### Differential testing

**Differential testing** compares independent implementations/paths over shared inputs to detect disagreement.

### Property testing

**Property testing** verifies general invariants/relations across generated inputs, not just fixed examples.

### Mutation testing

**Mutation testing** deliberately changes implementation logic to measure whether the test suite detects meaningful faults.

### Invariant

An **invariant** is a property that must remain true for a representation, state transition, or algorithm under the documented preconditions.

## API and compatibility vocabulary

### Public API

The **public API** is the supported Rust-facing contract downstream users may rely upon.

It includes more than function names when public types, traits, feature flags, and documented behavior matter.

### Semantic contract

The **semantic contract** defines what an API/result means, including rounding, error classification, canonicalization, defaults, convergence rules, and other behavior that can remain source-compatible while changing results.

### Source compatibility

**Source compatibility** means existing downstream source continues to compile under the supported compatibility promise.

### Semantic compatibility

**Semantic compatibility** means existing supported operations continue to mean and behave as promised.

A change can preserve source compatibility while breaking semantic compatibility.

### Breaking change

A **breaking change** violates the documented compatibility promise. After 1.0, this includes semantic breaks as well as Rust API breaks.

### Experimental

An **experimental** API/feature is intentionally not yet covered by the same stability promise as stable functionality and must be labeled.

## Architecture vocabulary

### Core

The **core** is the smallest capability set required to fulfill the crate's primary mission.

Core does not mean “everything enabled by default.”

### Optional feature

An **optional feature** is an additive capability that can be excluded without silently weakening the correctness of the remaining contract.

### Backend

A **backend** is an implementation strategy or execution engine behind a higher-level contract.

Examples: portable scalar, SIMD, GPU, arbitrary-precision, stabilizer, tensor-network.

Backends may differ in performance/capability but may not silently violate the selected semantic contract.

### Adapter

An **adapter** integrates an external format, ecosystem, provider, device, protocol, or implementation without making that external concern the owning core abstraction.

### Provider

A **provider** supplies a capability through a defined interface, commonly for crypto, RNG, storage, or external-data access.

### DAG

The family dependency architecture is a **directed acyclic graph**. Build/development order is not automatically Cargo dependency order.

### Dependency

A **dependency** is required because the crate materially uses the upstream contract/implementation.

Conceptual relation, build order, or shared methodology alone is not a dependency.

## Rust/platform vocabulary

### MSRV

**MSRV** is the Minimum Supported Rust Version that the project intentionally tests and supports.

The family does not set a fake placeholder MSRV; each crate must decide and qualify one before release.

### `no_std`

A crate claiming **`no_std` support** must compile and satisfy its documented contract without `std` for the stated feature/target configuration.

“Could probably be made no_std” is not support.

### Pure Rust

**Pure Rust core** means the core does not require foreign-language compiled/runtime components.

Optional FFI acceleration/integration does not invalidate the phrase only when it is genuinely optional and isolated.

### FFI

**FFI** is a foreign-function/interface boundary to non-Rust ABI/runtime code.

FFI must be optional/isolated where the family policy requires and must have explicit safety/failure/lifecycle contracts.

### Unsafe Rust

**Unsafe Rust** is code using Rust's `unsafe` capabilities. It is not automatically wrong, but every unsafe invariant must be documented and independently reviewed/qualified.

## Lifecycle and status vocabulary

### Reserved

Repository/name exists; implementation has not begun.

### Architecture

Scope, semantics, representation, API direction, dependencies, errors, targets, verification, and decisions are being closed.

### Implementation

Production capability is being built against the approved architecture.

### Hardening

The implementation exists and focus shifts toward pathological cases, fuzzing, mutation, performance, portability, and robustness.

### Qualification

Applicable family/domain release evidence is being executed and retained.

### Prerelease

The crate is release-shaped and undergoing final API/semantic/release review.

### Stable

A stable release satisfying the project's applicable gates exists.

### Maintenance

Stable functionality is being supported, corrected, optimized, and evolved under the compatibility policy.

### Gate

A **gate** is an objective completion condition required to advance progress/readiness.

### Blocker

A **blocker** is a known condition preventing the current milestone/gate from completing.

An unresolved design question is not automatically a blocker.

### Health

**Health** describes whether the current milestone appears on-track, at-risk, blocked, paused, or stable.

### Default-grade

**Default-grade** is the Perfect Foundations internal readiness standard for infrastructure that could credibly be a natural default dependency in its domain.

It is not a claim of endorsement by the Rust project, crates.io, a Linux distribution, or a standards body.

## Documentation rule

If a project page, ADR, requirement, API, or release note uses one of these terms with a materially different meaning, it must:

1. state the project-specific definition;
2. explain why the stronger/different definition is necessary;
3. avoid implying the family-wide guarantee when it is not met.
