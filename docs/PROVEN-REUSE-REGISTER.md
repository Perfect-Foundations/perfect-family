# Proven Reuse Register

This register records high-value reusable work that may be adapted/generalized into Perfect Foundations while preserving source provenance and ownership boundaries.

It is not a dependency list and it does not imply that every listed technique has already been implemented or qualified in the destination crate. Mandatory review mechanics are defined by the [Historical Proven-Reuse Gate](HISTORICAL-REUSE-GATE.md); crate applicability is recorded in the [Proven Reuse Applicability Matrix](PROVEN-REUSE-MATRIX.md).

## Reuse rules

- Prefer direct dependency only when the source project is the correct runtime owner.
- Otherwise adapt/generalize the reusable machinery into the correct Perfect crate.
- Preserve exact source revision, relevant files/algorithms/contracts, and adaptation history.
- Re-verify in the destination contract. Source verification does not automatically transfer.
- User ownership/permission permits reuse but does not remove the engineering need for provenance, licensing clarity for eventual publication, independent validation, or semantic review.
- A copied algorithm is not an independent oracle for itself.

## DrTomLLC/perfect-pi — read-only technical authority

Repository: `DrTomLLC/perfect-pi`

Protected rule: Perfectπ is read-only from Perfect Foundations.

Current inspected authorities:

- main: `d95e1f7864bd12bf58f38951680126aedbf63412`;
- open specialized-runtime PR #13 exact head: `bdf7baacc180ac8a245d67b5b81fc7861d40339b`.

### Reusable/generalizable assets

| Proven work | Intended Perfect owner/use | Transfer rule |
|---|---|---|
| Six explicit rounding modes; exact-vs-lossy conversion naming; precision-preservation boundaries | Perfect Numeric; consumers such as Float/Decimal/Math | Generalize semantics/types only when not already owned; preserve π-specific proof context separately |
| Dependency-free bounded/no_std/no-allocation core layering | Family engineering pattern; Numeric/Math/Constants | Reuse architecture/feature-isolation technique, not π dependency |
| Caller-owned output buffers and caller-selected precision/resource ceilings | Arithmetic, Number Theory, Float, parsers/generators | Generalize resource API pattern where variable work is attacker/caller controlled |
| Certified Chudnovsky bounds and exact output certification | Perfectπ itself for π; certification methodology for other numerical crates | Do not copy π algorithm into other crates; reuse bound/certification methodology |
| Specialized arbitrary-precision engine: decimal limbs, schoolbook/Karatsuba/NTT tiers, reciprocal-Newton division/sqrt, exact quotient/root certification | Perfect Arithmetic evaluation/adaptation candidate | Benchmark and independently qualify against existing Arithmetic backend before backend replacement; preserve source provenance |
| Algorithmically independent production/reference split (Chudnovsky vs Machin/Gauss-Legendre/reference implementations) | Qualification and numerical specialists | Production algorithm and oracle must remain materially independent |
| Exact finite-domain conversion-vector generation | Numeric/Float/Decimal/Wire | Reuse vector-generation methodology and exhaustive-domain testing where finite |
| Cross-host byte reproducibility, feature matrices, constrained-target probes | Qualification and family CI patterns | Generalize evidence methodology; target claims remain target-specific |
| Mutation/fuzz/coverage hardening with deep seeded arithmetic lanes | Arithmetic/Number Theory/Float/Math/Qualification | Reuse risk-targeted test design; thresholds remain destination-specific |
| Code/text/rodata/data/stack/linked-size measurement discipline | Benchmarking/Qualification | Reuse measurement methods; never convert object instruction counts into WCET claims |
| Generated-prefix deterministic regeneration and byte checking | Evidence/Constants/Math/Special Functions | Generalize generated-data provenance and reproducibility, not π content |

### Explicit non-transfer

- Perfectπ remains the only Perfect-family π specialist.
- Perfect Foundations must not fork or modify Perfectπ under this project.
- No crate should depend on Perfectπ solely to access unrelated bigint, CI, or verification machinery.

## Lifetime Medical Evidence System — assurance/reference source

Repository mirror: `Lifetime-Medical-Evidence-System/lifetime-medical-evidence-system`

Inspected GitHub mirror revision: `95a6cb30cae8cf4a35ff33878e2f9348d1471db5`.

The repository declares GitLab authoritative and GitHub a secondary/non-authoritative mirror. Therefore these GitHub materials are reusable reference snapshots, not assertions about the current authoritative LMES baseline.

Key inspected artifacts:

- `docs/requirements/LMES-EAIS-001.md` blob `0360b5ddf361648878be16a27ab9855e1ce27516`;
- `docs/verification/LMES-VVP-001.md` blob `44301611148e788444fac8acccc29b114fde243d`;
- `AGENTS.md` blob `eb5baa73f408f23dd7c31d463820d9079657f3bb`;
- `crates/lmes-identity/src/lib.rs` blob `29d01f9f621b273b934f32cb10a5bf7cdc24f12b`;
- `crates/lmes-verification/src/lib.rs` blob `05cd636ed64a8e501a6cf3172f740bb0ef341746`.

### Reusable/generalizable assets

| Proven work | Intended Perfect owner/use | Transfer rule |
|---|---|---|
| Claim-assurance states and anti-hallucination invariants | Family Claim Assurance Standard; Perfect Evidence metadata; Qualification reporting | Generalize cross-domain semantics; remove medical-only policy |
| Verification vs validation distinction | Perfect Qualification and release gates | Preserve as separate evidence concepts |
| Exact verification-scope discipline | AGENTS, Qualification, Evidence | Tool/test result proves only its defined scope |
| Requirement→implementation→verification→evidence traceability | Family requirements standard; Qualification | Strengthen existing model rather than duplicate |
| Negative-path/fault/resource/recovery verification | Qualification and risk-specific crate verification | Apply proportionally to crate risk/contract |
| Typed opaque identity domains with strict canonical parsing | Evidence/Wire/API design reference | Generalize only if/when an identity primitive has proven cross-domain need; do not copy LMES domain markers |
| Immutable source vs derived output separation | Evidence; generated-data users | Generalize source/derivation identity and non-authority of derived artifacts |
| Version/revision-bound external claims and deterministic derivation metadata | Evidence, Constants/CODATA, Qualification | Reuse metadata discipline |
| Drift control: accepted semantics cannot silently change to match implementation | Family ADR/requirements/API stability | Strengthen existing anti-drift process |
| Synthetic fixtures separated from authority | Qualification | Fixtures are test aids, not proof/source authority |
| Required-check unavailable/indeterminate != pass | Qualification/status/CI | Preserve explicit not-run/error/inconclusive states |
| Supply-chain executable-input review | Family supply-chain standard | Apply to build scripts, proc macros, Actions, generators, containers |

## Historical defect corpus

The register also preserves defect classes already exposed by deep review so the family can prevent recurrence rather than rediscover them.

### Perfectπ review lessons

- precision-dependent certification failures can exist far beyond representative small-digit tests;
- fuzz inputs/selectors must be proven to reach the intended deep arithmetic path;
- caller/resource limit branches must be reachable and tested;
- production and reference algorithms must remain materially independent;
- performance evidence is accepted only with attached correctness/certification gates.

### LMES review lessons

- stale/contradictory authority text and parser/routing edge cases can create false-PASS assurance;
- required-test isolation and fixture discovery are themselves verification concerns;
- dependency direction, suppression controls, coverage scope, and reference integrity can drift unless explicitly checked;
- mirrors, generated fixtures, or repeated AI assertions are not independent authority;
- unavailable/indeterminate checks remain non-passing.

## Reuse review triggers

M1/M3/M5/M6 reviews are mandatory where applicable under the [Historical Proven-Reuse Gate](HISTORICAL-REUSE-GATE.md). The allowed dispositions are:

- REUSE_DEPENDENCY;
- ADAPT_WITH_PROVENANCE;
- REUSE_METHOD_ONLY;
- EVALUATED_REJECTED;
- DEFERRED_WITH_IMPACT;
- NOT_APPLICABLE.

The register does not force scope expansion or dependency addition, and its existence does not award progress.
