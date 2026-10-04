# crates.io Name Availability Audit

**Audit date:** 2026-10-03
**Method:** exact crates.io API lookup for each planned Perfect Foundations crate name.

This is a point-in-time risk record. crates.io name availability can change at
any time and must be rechecked immediately before any public publication.

## Summary

| Result | Count |
|---|---:|
| Planned crate names checked | 40 |
| Available at audit time | 39 |
| Already taken | 1 |

## Current conflict

### `perfect-decimal` — TAKEN

The crates.io name `perfect-decimal` is already owned by an unrelated project:

- current version: `0.0.2`;
- description: “Limited range decimals which serialize as IEE754 floats with no loss of precision.”;
- repository: `https://github.com/deepcomet/perfect-decimal`;
- owners reported by crates.io: `mintthemoon`, `github:deepcomet:devs`;
- created/last updated: 2024-08-13.

No Perfect Foundations rename, alternate package name, owner-contact attempt, or
placeholder publication is authorized by this audit. The repository remains
`Perfect-Foundations/perfect-decimal` until a deliberate naming decision is
made.

## Available at audit time

- `perfect-numeric`
- `perfect-arithmetic`
- `perfect-rational`
- `perfect-float`
- `perfect-algebra`
- `perfect-number-theory`
- `perfect-math`
- `perfect-complex`
- `perfect-interval`
- `perfect-polynomial`
- `perfect-special-functions`
- `perfect-calculus`
- `perfect-differential-equations`
- `perfect-geometry`
- `perfect-probability`
- `perfect-statistics`
- `perfect-information-theory`
- `perfect-error-correction`
- `perfect-optimization`
- `perfect-signal`
- `perfect-units`
- `perfect-uncertainty`
- `perfect-mechanics`
- `perfect-estimation`
- `perfect-control`
- `perfect-quantum-information`
- `perfect-quantum-circuits`
- `perfect-quantum-simulation`
- `perfect-quantum-compilation`
- `perfect-quantum-error-correction`
- `perfect-finance`
- `perfect-meteorology`
- `perfect-navigation`
- `perfect-gnss`
- `perfect-biosignal`
- `perfect-wire`
- `perfect-evidence`
- `perfect-codata`
- `perfect-constants`

## Policy

Name availability is monitored while the family remains private, but unfinished
placeholder publication is not the default reservation mechanism.

Immediately before open-release publication:

1. recheck the exact name;
2. resolve any naming conflict deliberately;
3. publish only from the qualified bottom-up dependency sequence;
4. verify the resulting crates.io owner/package metadata.

See [crates.io Readiness and Publication Policy](CRATES-IO-READINESS.md).
