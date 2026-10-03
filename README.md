# Perfect Foundations Family

This repository is the authoritative architecture and roadmap for the **Perfect Foundations** family.

The family consists of focused, independently versioned foundational Rust crates. It is intentionally **not** a monorepo and not a single umbrella runtime crate.

## Status

- **Perfectπ / `perfect-pi`** — existing public project; remains under `DrTomLLC` until complete and in service.
- **40 new family crate repositories** — names reserved under `Perfect-Foundations`; kept private during planning/early implementation and made public deliberately as they mature.
- **`perfect-qualification`** — cross-family compatibility and qualification repository.

## Planned family

### Numeric and mathematical foundations

1. **Perfect Numeric** — `perfect-numeric`
2. **Perfect Arithmetic** — `perfect-arithmetic`
3. **Perfect Rational** — `perfect-rational`
4. **Perfect Float** — `perfect-float`
5. **Perfect Decimal** — `perfect-decimal`
6. **Perfect Math** — `perfect-math` — includes trigonometry
7. **Perfect Complex** — `perfect-complex`
8. **Perfect Interval** — `perfect-interval` — interval, ball, and complex-ball arithmetic
9. **Perfect Algebra** — `perfect-algebra`
10. **Perfect Number Theory** — `perfect-number-theory`
11. **Perfect Polynomial** — `perfect-polynomial`
12. **Perfect Special Functions** — `perfect-special-functions`
13. **Perfect Calculus** — `perfect-calculus`
14. **Perfect Differential Equations** — `perfect-differential-equations`
15. **Perfect Geometry** — `perfect-geometry`

### Probability, information, optimization, and engineering

16. **Perfect Probability** — `perfect-probability`
17. **Perfect Statistics** — `perfect-statistics`
18. **Perfect Information Theory** — `perfect-information-theory`
19. **Perfect Error Correction** — `perfect-error-correction`
20. **Perfect Optimization** — `perfect-optimization`
21. **Perfect Signal** — `perfect-signal`
22. **Perfect Mechanics** — `perfect-mechanics`
23. **Perfect Estimation** — `perfect-estimation`
24. **Perfect Control** — `perfect-control`

### Quantum foundations

25. **Perfect Quantum Information** — `perfect-quantum-information`
26. **Perfect Quantum Circuits** — `perfect-quantum-circuits`
27. **Perfect Quantum Simulation** — `perfect-quantum-simulation`
28. **Perfect Quantum Compilation** — `perfect-quantum-compilation`
29. **Perfect Quantum Error Correction** — `perfect-quantum-error-correction`

### Scientific and domain foundations

30. **Perfect Finance** — `perfect-finance`
31. **Perfect Meteorology** — `perfect-meteorology`
32. **Perfect Navigation** — `perfect-navigation`
33. **Perfect GNSS** — `perfect-gnss`
34. **Perfect Biosignal** — `perfect-biosignal`
35. **Perfect Units** — `perfect-units`
36. **Perfect Uncertainty** — `perfect-uncertainty`

### Representation, evidence, and authoritative data

37. **Perfect Wire** — `perfect-wire`
38. **Perfect Evidence** — `perfect-evidence`
39. **Perfect CODATA** — `perfect-codata`
40. **Perfect Constants** — `perfect-constants`

### Existing family member

41. **Perfectπ** — `perfect-pi`

## Architecture rules

1. A crate depends on another Perfect crate only when the dependency is materially required.
2. Build order is not a mandate for a linear dependency chain.
3. Specialist crates own their truth. Aggregators reference specialists rather than duplicating them.
4. Exact representations remain exact until an explicitly requested operation requires rounding or approximation.
5. Lossy operations are named and documented.
6. Determinism and reproducibility are explicit contracts, not assumptions.
7. Foreign-language dependencies must never silently become mandatory foundations.
8. Mature external Rust crates are reused when they already solve a problem well; the family is not a rewrite-for-ownership exercise.
9. Perfectπ remains independent and unchanged while it is being completed. Transfer into the organization happens only after it is complete and in service.
