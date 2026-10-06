# Reuse and Dependency Policy

Perfect Foundations aggressively reuses proven work without creating fake dependencies.

## Reuse hierarchy

1. **Exact reusable implementation already exists in a Perfect project:** depend on it when the runtime dependency is appropriate.
2. **A useful implementation is too specialized to justify a dependency:** copy/adapt/generalize it into the correct crate with provenance preserved.
3. **Only the engineering method is reusable:** reuse the design, tests, CI strategy, reference-generation method, or verification approach.
4. **A mature external Rust crate already solves the problem well:** use it rather than rewriting solely for ownership.
5. **A custom Perfect implementation can materially improve the required contract:** build it when evidence supports stronger correctness, determinism, performance, resource use, portability, embedded suitability, dependency reduction, security, or verification. Preserve provenance and independent comparison.
6. **Multiple projects converge on the same stable generalized primitive:** consider extracting a dedicated Perfect crate only when that shared primitive has a clear independent contract and proven reuse.

## Perfectπ-specific rule

Perfectπ remains strictly π-focused.

Other family projects may:
- call Perfectπ when they actually need π;
- reuse or adapt Perfectπ algorithms, internal techniques, test strategies, CI ideas, or verification methods when appropriate.

They must not make Perfectπ a dependency merely to access unrelated implementation machinery.

## Anti-monolith rule

There will be no giant `perfect` umbrella runtime crate that enables all family members by default.

Applications should depend only on the crates they need.


## Provenance requirement

Every material adaptation/generalization records enough provenance to answer:

- source repository/project;
- exact source revision and relevant artifact/file/algorithm when known;
- what was copied, adapted, generalized, or only used as methodology;
- destination owner and why that crate owns the generalized machinery;
- semantic differences introduced by adaptation;
- independent verification/oracle used after adaptation;
- licensing/publication disposition when source and destination licensing differ.

Common ownership or explicit permission to reuse does not remove this engineering record. Provenance is required for auditability, future maintenance, and independent qualification.

The family-wide high-value source register is [Proven Reuse Register](PROVEN-REUSE-REGISTER.md).

## Verification-transfer rule

Evidence does not transfer automatically with code.

A source implementation may be deeply verified and still require destination-specific verification because:

- the public contract changed;
- types/representations changed;
- compiler/target/features changed;
- algorithms were generalized;
- dependencies/resources differ;
- integration introduces new failure paths.

Retain the source evidence as provenance and baseline context, then independently qualify the adapted destination contract.
