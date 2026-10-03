# FFI and Foreign-Runtime Policy

One motivation for Perfect Foundations is to reduce situations where serious Rust software must cross into C, C++, Fortran, Python, JVM, or vendor-specific runtimes for foundational behavior.

## Default

The default/core implementation of a Perfect crate should be Pure Rust where practical.

## Allowed foreign integration

FFI or foreign runtimes may be supported when they are:
- optional;
- isolated behind clearly named features/modules;
- useful for interoperability, comparison, migration, acceleration, or qualification;
- not required to understand or use the crate's core semantics.

## Mandatory FFI

A mandatory foreign dependency requires an explicit architecture decision documenting:
- why a Pure-Rust implementation is not currently practical;
- the ABI/runtime requirements;
- supported platforms;
- failure and deployment implications;
- the plan, if any, for removing the dependency.

## Reference implementations

C/C++/Fortran/Python implementations may be used as:
- test oracles;
- benchmark comparisons;
- qualification references;
- import/export interoperability targets.

That does not make them production dependencies.

## Vendor acceleration

CUDA, ROCm, hardware QPU SDKs, BLAS implementations, and similar systems should normally be optional accelerators/adapters rather than mandatory foundations.
