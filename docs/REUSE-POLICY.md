# Reuse and Dependency Policy

Perfect Foundations aggressively reuses proven work without creating fake dependencies.

## Reuse hierarchy

1. **Exact reusable implementation already exists in a Perfect project:** depend on it when the runtime dependency is appropriate.
2. **A useful implementation is too specialized to justify a dependency:** copy/adapt/generalize it into the correct crate with provenance preserved.
3. **Only the engineering method is reusable:** reuse the design, tests, CI strategy, reference-generation method, or verification approach.
4. **A mature external Rust crate already solves the problem well:** use it rather than rewriting solely for ownership.
5. **Multiple projects converge on the same stable generalized primitive:** consider extracting a dedicated Perfect crate only when that shared primitive has a clear independent contract.

## Perfectπ-specific rule

Perfectπ remains strictly π-focused.

Other family projects may:
- call Perfectπ when they actually need π;
- reuse or adapt Perfectπ algorithms, internal techniques, test strategies, CI ideas, or verification methods when appropriate.

They must not make Perfectπ a dependency merely to access unrelated implementation machinery.

## Anti-monolith rule

There will be no giant `perfect` umbrella runtime crate that enables all family members by default.

Applications should depend only on the crates they need.
