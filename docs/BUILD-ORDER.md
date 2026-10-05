# Build Order

This is the **recommended implementation sequence**, not a mandatory dependency chain.

## Phase 0 — family infrastructure
- perfect-family
- perfect-qualification
- organization standards
- Perfectπ remains under DrTomLLC until complete and in service

## Phase 1 — numeric kernel
1. perfect-numeric
2. perfect-arithmetic
3. perfect-rational
4. perfect-float
5. perfect-decimal

## Phase 2 — core mathematics
6. perfect-number-theory
7. perfect-algebra
8. perfect-math
9. perfect-complex
10. perfect-interval
11. perfect-polynomial
12. perfect-special-functions
13. perfect-calculus
14. perfect-differential-equations
15. perfect-geometry

## Phase 3 — probability, information, optimization, and signals
16. perfect-probability
17. perfect-statistics
18. perfect-information-theory
19. perfect-error-correction
20. perfect-optimization
21. perfect-signal

## Phase 4 — engineering foundations
22. perfect-units
23. perfect-uncertainty
24. perfect-mechanics
25. perfect-estimation
26. perfect-control

## Phase 5 — quantum branch
27. perfect-quantum-information
28. perfect-quantum-circuits
29. perfect-quantum-simulation
30. perfect-quantum-compilation
31. perfect-quantum-error-correction

## Phase 6 — applied foundational domains
32. perfect-finance
33. perfect-meteorology
34. perfect-navigation
35. perfect-gnss
36. perfect-biosignal

## Phase 7 — representation, evidence, and authoritative data
37. perfect-wire
38. perfect-evidence
39. perfect-codata
40. perfect-constants

## Existing specialist
41. Perfectπ / perfect-pi

Perfectπ is developed independently and may be consumed wherever π is genuinely required.

## Important

The sequence may change after architecture audits. A project may begin earlier when doing so uncovers requirements needed by a lower layer. Any such change must preserve the family dependency rules.

The 2026-10-05 Algebra/Number Theory M0 architecture audit changed Phase 2 so `perfect-number-theory` precedes `perfect-algebra`. Number Theory owns validated prime-modulus/primality and general modular arithmetic; Algebra consumes those capabilities and owns finite-field structure. This is an implementation-sequence correction driven by the actual production DAG, not a claim that either M1 implementation is complete.

## Public crates.io publication order

Implementation order is **not** the registry publication order.

All Perfect crates remain privately consumable through exact Git revisions while
the family is being built and qualified. crates.io publication is deferred until
explicit open-release authorization.

When publication begins, crates are published **bottom-up by the actual
production dependency DAG**:

1. publish an already-qualified crate whose production Perfect dependencies are
   all already present on crates.io;
2. verify the crates.io artifact and docs.rs output;
3. update/requalify the next dependent release manifest against the released
   registry dependency;
4. continue upward until the intended family release set is published.

For the initial numeric chain, if the approved dependency map remains:

`perfect-rational -> perfect-arithmetic -> perfect-numeric`

then registry publication is:

`perfect-numeric -> perfect-arithmetic -> perfect-rational`.

See [crates.io Readiness and Publication Policy](CRATES-IO-READINESS.md).
