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

Verification claims follow the [Claim Assurance Standard](CLAIM-ASSURANCE-STANDARD.md). Verification and validation are distinct: conformance to a specified contract does not by itself establish fitness for every downstream use.

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

Required checks that are skipped, unavailable, timed out, permission-blocked, runner-provisioning-failed, unsupported, or indeterminate are not passing. Self-generated fixtures and self-round-trips are useful but are not independent evidence unless independence is separately established.

## Test environment fidelity and zero-cost-first execution

Before buying CI minutes, runners, hardware, hosted VMs, or test services, use
already-authorized free/local infrastructure when it can satisfy the actual
requirement: native local operating systems, hardware-accelerated VMs, isolated
containers, available physical machines, and independent emulation/reference
testing. Never create costs, change billing limits, or publish private source
merely to bypass a CI allowance without explicit authorization. Budget CI
runs, suppress duplicate event triggers, and reuse exact-source evidence.

**Execution method is part of verification evidence**, not an interchangeable
implementation detail. Record the machine and hardware ISA, guest/container
architecture, actual operating-system kernel and ABI, virtualization or emulator
model/version, Rust toolchain, dependency/source SHAs, feature/target matrix,
command, log, resource limits, and exit status. Distinguish:

- **Native ISA execution:** tests run on physical CPU hardware of the required
  instruction-set architecture, either directly or through hardware-assisted
  virtualization on a same-ISA host. A VM can establish guest OS-specific
  behavior when its guest kernel/ABI matches the requirement, but it does not
  automatically establish bare-metal timing, peripheral, driver, GPU, or other
  hardware-specific behavior.
- **Container execution:** tests use the host/VM kernel and native ISA; a
  container does not provide a new OS kernel or a different hardware ISA.
  Windows/Linux containers and WSL must be identified by their actual kernel
  and runtime semantics, not marketed as bare-metal equivalents.
- **Foreign-ISA emulation:** QEMU user-mode or full-system emulation may execute
  real target-ISA binaries and reveal functional/ABI defects. This is useful
  *emulated execution*, not native CPU or native hardware qualification.
  Identify user-mode versus system-mode, emulated OS/kernel limits, and
  separately validate hardware-sensitive behavior when required.
- **Cross-compilation:** produces a target artifact but does not execute that
  target. Compilation success must not stand in for an execution requirement.
- **Other OS virtualization:** use license-compliant, authorized environments
  capable of running the required kernel and APIs; compatibility shims are not
  assumed equivalent to the actual operating system. In particular, a macOS
  VM is not a substitute for permitted Apple-hosted macOS execution unless
  applicable platform and licensing constraints are met.

A missing native target remains **BLOCKED/NOT-RUN** until matching evidence
exists. Run useful alternative/emulated checks independently without upgrading
the unavailable gate. A genuine native ARM64 CPU or hardware-accelerated VM on
authorized ARM64 hardware can satisfy a native-ISA requirement if the specified
OS/ABI and configuration are actually exercised; x86-hosted QEMU cannot.
Use exact source and independent oracles to compare results across environments.

Self-hosted CI executing repository code on a user's machine must be
least-privilege and isolated: prefer single-use/ephemeral runners, pinned
reviewed commits, restricted labels and triggers, minimal token permissions,
resource limits, and no host worktree/credential/container-engine socket
mounts. Never attach general untrusted pull-request code to a privileged
long-lived local runner.

## Performance and resource excellence

Optimization follows correctness, but it is not optional once the contract is
established. Projects should actively seek algorithmic, representation, and
implementation improvements in latency, throughput, scaling, memory, allocation,
stack, code/data size, dependency weight, startup cost, and target suitability.

Performance/resource work should follow the
[Benchmarking Standard](BENCHMARKING-STANDARD.md). Benchmarking is the default
decision instrument for optimization; material choices should be measured rather
than guessed.

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
