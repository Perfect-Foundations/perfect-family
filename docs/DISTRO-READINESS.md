# Linux Distribution and Packaging Readiness

Perfect Foundations crates are intended to be straightforward to package in Linux distributions and other source-first build environments.

## Build requirements

The preferred default is:
- Cargo + Rust toolchain only;
- no network access during build;
- no downloaded test vectors or generated source at build time;
- no vendored prebuilt native binaries;
- no mandatory C/C++/Fortran toolchain;
- no mandatory Python/Node/JVM build step;
- deterministic build scripts with narrowly documented inputs.

If a project cannot meet that baseline, the exception must be documented in the project blueprint.

## Cargo packaging

Crates.io/package readiness is maintained **while the crate is still private**;
actual registry publication is a separate final gate.

Every implemented crate should verify:

- `publish = false` remains set during private retention;
- `cargo package --list` contains only intended files;
- `cargo package` succeeds from a clean checkout;
- the produced crate builds from the packaged tarball;
- the produced crate builds offline from a populated Cargo source cache;
- required generated tables/data are included or reproducibly generated without the network;
- licenses/notices required by dependencies or source datasets are included;
- metadata includes repository, homepage where appropriate, documentation,
  description, categories, keywords, readme, and rust-version;
- the project license may remain intentionally undecided until open-release
  authorization, but that deferral must be explicit rather than guessed;
- private Perfect production dependencies include an exact Git revision plus a
  registry-compatible version requirement;
- the generated package manifest is inspected to ensure future registry
  consumers will not require the private Git source.

See [crates.io Readiness and Publication Policy](CRATES-IO-READINESS.md).

## Offline build

A qualification job should build from an already-populated Cargo source cache with network access disabled.

The test should detect:
- hidden HTTP requests;
- git submodule assumptions;
- remote code/data generation;
- build-time package-manager calls;
- undeclared system-library discovery.

## Reproducible source inputs

Authoritative generated constants/tables/reference vectors should have:
- checked-in source inputs or an immutable source reference;
- a documented generator;
- generator version;
- deterministic output;
- a verification hash or reproducible comparison.

## System dependencies

Optional native/system dependencies must be:
- isolated behind explicit features;
- documented by package name/function, not only by one distro-specific package;
- replaceable by the Pure-Rust core where that is part of the crate mission.

## Linux architecture expectations

Where relevant, qualification should consider:
- x86_64
- aarch64
- riscv64 where ecosystem/tooling permits
- 32-bit targets when integer width or pointer width could affect semantics
- little- vs big-endian behavior where serialization or bit-level code is involved

A crate need not support every architecture; it must state the truth.

## Distribution-friendly project behavior

Prefer:
- stable release tarballs/tags;
- no vendored build artifacts;
- predictable feature sets;
- stable generated files;
- no auto-updaters;
- no telemetry;
- no runtime dependency on writable source directories;
- tests that can run without internet access;
- examples/benchmarks that are not required for normal packaging.

## Distribution integration evidence

A mature project should eventually maintain a packaging note containing:
- runtime/build/test dependencies;
- default and optional features;
- system library requirements;
- generated-data provenance;
- test commands suitable for distro CI;
- cross-compilation notes;
- known architecture limitations.
