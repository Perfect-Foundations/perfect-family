# Provisional Dependency Map

This document centralizes the **anticipated relationships** recorded in the initial crate charters.

It is not a lockfile and not a mandate. Dependencies are added only after crate-level architecture work proves that they are materially justified.

## Numeric kernel

- Perfect Numeric: foundational numerical semantics.
- Perfect Arithmetic: may use Perfect Numeric.
- Perfect Rational: naturally builds on Perfect Arithmetic; may use Perfect Numeric.
- Perfect Float: naturally builds on Perfect Numeric + Arithmetic + Rational.
- Perfect Decimal: naturally builds on Perfect Numeric + Arithmetic + Rational.

## Algebra and core mathematics

- Perfect Algebra: likely uses Arithmetic and Rational.
- Perfect Number Theory: likely uses Arithmetic + Algebra; Rational where useful.
- Perfect Math: uses Numeric and supported numeric backends; may consume PerfectPi when pi is genuinely required.
- Perfect Complex: likely uses Float + Math; other numeric backends only where sound.
- Perfect Interval: likely uses Numeric + supported numeric backends + Math; Complex for complex balls.
- Perfect Polynomial: likely uses Algebra + Arithmetic + Rational; Float/Complex/Interval for approximate/certified paths.
- Perfect Special Functions: likely uses Math + Float + Complex + Interval + Polynomial.
- Perfect Calculus: likely uses Math + Float + Interval + Polynomial.
- Perfect Differential Equations: likely uses Calculus + Math + Float + Interval; Optimization where useful.
- Perfect Geometry: likely uses Numeric + Rational/Float + Math + Interval.

## Probability, information, optimization, and signals

- Perfect Probability: likely uses Math + Special Functions + numerical representations.
- Perfect Statistics: likely uses Probability + Math + Special Functions.
- Perfect Information Theory: likely uses Probability + Math; Statistics where inference is required.
- Perfect Error Correction: likely uses Algebra + Polynomial + Number Theory + Probability + Information Theory.
- Perfect Optimization: likely uses Calculus + Math + Interval; Statistics where objective models require it.
- Perfect Signal: likely uses Math + Complex + Numeric; Statistics for analytical operations.

## Engineering

- Perfect Units: likely uses Rational + Decimal + Numeric; Math for genuinely nonlinear conversions.
- Perfect Uncertainty: likely uses Probability + Statistics + Units + Math + Calculus where sensitivity derivatives are required.
- Perfect Mechanics: likely uses Geometry + Math + Differential Equations + Units.
- Perfect Estimation: likely uses Probability + Statistics + Optimization + Geometry + Mechanics + Units.
- Perfect Control: likely uses Mechanics + Estimation + Optimization + Calculus + Differential Equations + Units.

## Quantum branch

- Perfect Quantum Information: likely uses Complex + Math + Probability + Information Theory; Interval where rigorous bounds help.
- Perfect Quantum Circuits: likely uses Quantum Information; numeric/math support for parameters as required.
- Perfect Quantum Simulation: likely uses Quantum Information + Circuits + Complex + Probability.
- Perfect Quantum Compilation: likely uses Quantum Information + Circuits + Optimization; Algebra/Number Theory where synthesis requires them.
- Perfect Quantum Error Correction: likely uses Quantum Information + Circuits + Simulation + Probability; classical Error Correction concepts when reusable.

## Domain foundations

- Perfect Finance: likely uses Decimal + Math + Probability + Statistics + Optimization + Calculus + Differential Equations + Units.
- Perfect Meteorology: likely uses Math + Units + Uncertainty + Statistics + Signal + Geometry.
- Perfect Navigation: likely uses Geometry + Mechanics + Estimation + Math + Units.
- Perfect GNSS: likely uses Navigation + Estimation + Signal + Math + Statistics + Units.
- Perfect Biosignal: likely uses Signal + Statistics + Units + Uncertainty + Evidence.

## Representation, evidence, and authoritative data

- Perfect Wire: feature-gated integration with relevant numeric/units/uncertainty types only when useful.
- Perfect Evidence: likely uses Wire and selected numeric/units/uncertainty representations.
- Perfect CODATA: likely uses Decimal + Units + Uncertainty + Evidence + Wire as appropriate.
- Perfect Constants: likely consumes PerfectPi + Perfect CODATA + Math/Decimal/Units/Uncertainty/Evidence as required.

## Anti-coupling rules

- Build order is not dependency order.
- No crate imports a predecessor merely because it was built first.
- Optional integration should be feature-gated when it prevents unnecessary dependency weight.
- Circular dependencies are not acceptable.
- PerfectPi remains strictly pi-focused.
- Perfect Constants is an aggregator, not an alternate implementation of PerfectPi or Perfect CODATA.
- perfect-qualification is never a production dependency.
