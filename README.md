# Perfect Foundations Family

This repository is the **authoritative architecture, catalog, roadmap, and policy record** for the Perfect Foundations family.

Perfect Foundations is a collection of focused, independently versioned foundational Rust crates. It is intentionally **not** a monorepo, not a single umbrella runtime, and not a requirement that every crate depend on every earlier crate.

## Canonical count

- **40 new planned crates** are reserved under `Perfect-Foundations`.
- **Perfectπ / `perfect-pi`** is the existing first family member.
- **Total family members: 41.**
- Organization-support repositories such as `.github`, `perfect-family`, and `perfect-qualification` are not counted as family crates.

## Canonical project list

### Core numeric and mathematical foundations
1. Perfect Numeric — `perfect-numeric`
2. Perfect Arithmetic — `perfect-arithmetic`
3. Perfect Rational — `perfect-rational`
4. Perfect Float — `perfect-float`
5. Perfect Decimal — `perfect-decimal`
6. Perfect Math — `perfect-math` — includes trigonometry
7. Perfect Complex — `perfect-complex`
8. Perfect Interval — `perfect-interval` — interval, ball, and complex-ball arithmetic
9. Perfect Algebra — `perfect-algebra`
10. Perfect Number Theory — `perfect-number-theory`
11. Perfect Polynomial — `perfect-polynomial`
12. Perfect Special Functions — `perfect-special-functions`
13. Perfect Calculus — `perfect-calculus`
14. Perfect Differential Equations — `perfect-differential-equations`
15. Perfect Geometry — `perfect-geometry`

### Probability, information, optimization, signal, and engineering
16. Perfect Probability — `perfect-probability`
17. Perfect Statistics — `perfect-statistics`
18. Perfect Information Theory — `perfect-information-theory`
19. Perfect Error Correction — `perfect-error-correction`
20. Perfect Optimization — `perfect-optimization`
21. Perfect Signal — `perfect-signal`
22. Perfect Mechanics — `perfect-mechanics`
23. Perfect Estimation — `perfect-estimation`
24. Perfect Control — `perfect-control`

### Quantum foundations
25. Perfect Quantum Information — `perfect-quantum-information`
26. Perfect Quantum Circuits — `perfect-quantum-circuits`
27. Perfect Quantum Simulation — `perfect-quantum-simulation`
28. Perfect Quantum Compilation — `perfect-quantum-compilation`
29. Perfect Quantum Error Correction — `perfect-quantum-error-correction`

### Scientific and domain foundations
30. Perfect Finance — `perfect-finance`
31. Perfect Meteorology — `perfect-meteorology`
32. Perfect Navigation — `perfect-navigation`
33. Perfect GNSS — `perfect-gnss`
34. Perfect Biosignal — `perfect-biosignal`
35. Perfect Units — `perfect-units`
36. Perfect Uncertainty — `perfect-uncertainty`

### Representation, evidence, and authoritative data
37. Perfect Wire — `perfect-wire`
38. Perfect Evidence — `perfect-evidence`
39. Perfect CODATA — `perfect-codata`
40. Perfect Constants — `perfect-constants`

### Existing family member
41. Perfectπ — `perfect-pi`

## Current repository state

The 40 new crate repositories are reserved privately while their architecture is developed. This protects the names and preserves the design record without presenting empty public repositories as finished software.

Perfectπ remains under `DrTomLLC/perfect-pi` until it is complete and in service. It is **not to be moved during active completion work**.

## Authoritative supporting documents

- [Machine-readable family catalog](catalog.toml)
- [Architecture](docs/ARCHITECTURE.md)
- [Provisional dependency map](docs/DEPENDENCY-MAP.md)
- [Build order and phases](docs/BUILD-ORDER.md)
- [Engineering standard](docs/ENGINEERING-STANDARD.md)
- [Reuse and dependency policy](docs/REUSE-POLICY.md)
- [FFI and foreign-runtime policy](docs/FFI-POLICY.md)
- [Scope boundaries and explicitly deferred areas](docs/SCOPE-BOUNDARIES.md)
- [Repository lifecycle](docs/REPOSITORY-LIFECYCLE.md)
- [Initial decisions record](docs/DECISIONS.md)

## Core rules

1. **Build order is not dependency order.**
2. A crate depends on another Perfect crate only when that dependency is materially required.
3. Specialist crates own their truth; aggregators consume specialists instead of duplicating them.
4. Exact representations remain exact until an explicitly requested operation requires rounding or approximation.
5. Lossy operations must be explicit and documented.
6. Determinism and reproducibility are contracts, not assumptions.
7. Mandatory foreign-language/runtime dependencies are avoided unless explicitly justified.
8. Mature external Rust crates are reused when they already solve a problem well.
9. Perfectπ remains independent and unchanged while it is being completed.
10. The family must not become a giant umbrella crate that forces unrelated functionality onto users.
