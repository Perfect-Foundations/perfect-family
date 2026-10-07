# Proven-Reuse Applicability Matrix

This matrix is the family-wide baseline assessment of where predecessor work from LMES and Perfectπ should be examined. It is not a dependency graph, implementation claim, or qualification result.

Each crate still records its own exact disposition under the [Historical Proven-Reuse Gate](HISTORICAL-REUSE-GATE.md).

Source revisions remain pinned in the [Proven Reuse Register](PROVEN-REUSE-REGISTER.md). A newer source revision is not silently substituted.

## Applicability legend

- **Direct** — source semantics/implementation ownership may directly affect the public or internal contract.
- **Method** — reuse assurance/verification/benchmarking/certification methodology, not a runtime dependency.
- **Specialist** — direct dependency only for the specialist capability actually required.
- **N/A runtime** — no runtime dependency is expected; method-level lessons can still apply.

## Baseline assessment — all 40 planned crates

| Crate | LMES-derived applicability | Perfectπ-derived applicability | Mandatory next review |
|---|---|---|---|
| `perfect-numeric` | Method: exact claim scope, unknown/error separation, traceability | **Direct/Method:** rounding vocabulary, exact-vs-lossy conversion, finite-domain vectors, reproducibility | Catch-up before any new requalification/release claim |
| `perfect-arithmetic` | Method: resource/failure negative paths, evidence scope | **Direct/Method:** bigint backend candidate, caller ceilings, quotient/root certification, deep fuzz/mutation | **M6 catch-up now** |
| `perfect-rational` | Method: exact scope, failure-state and traceability discipline | Method: exact-arithmetic certification, independent reference, pathological/deep testing | **M5 catch-up now** |
| `perfect-float` | Method: exact scope and explicit unknown/unverified state | **Direct/Method:** rounding/precision/conversion semantics, certified bounds, deep fuzzing | Before M5 |
| `perfect-decimal` | **Direct/Method:** exact reported decimal/source-vs-derived discipline, loss classification | **Direct/Method:** explicit rounding, finite conversion vectors, resource/certification methods | **M1 now** |
| `perfect-number-theory` | Method: exact verification scope, negative/error cases | **Direct/Method:** arbitrary-precision/resource/certification/fuzz lessons | **M1 now** |
| `perfect-algebra` | Method: authority/traceability and exact verification scope | Method: exact arithmetic, independent oracle and mutation strategy | **M1 now** |
| `perfect-math` | Method: scoped claims and unavailable != pass | **Specialist/Direct:** π authority/generated-data provenance, certified bounds, independent algorithms | **M1 now** |
| `perfect-complex` | Method: semantic/verification scope | Method; Specialist only if later π-dependent functions require it | **M1 now** |
| `perfect-interval` | Method: guarantee scope must not exceed evidence | **Direct/Method:** directed rounding/certified-bound methodology | **M1 now** |
| `perfect-polynomial` | Method: traceability and negative-path discipline | Method: exact arithmetic, independent references, resource/benchmark discipline | **M1 now** |
| `perfect-special-functions` | Method: scoped quantitative claims and derivation provenance | **Specialist/Method:** π-derived constants where required; generated-data reproducibility and independent references | **M1 now** |
| `perfect-calculus` | Method: verification vs validation; estimate != certificate | Method: independent numerical references, bounded-resource/benchmark discipline | **M1 now** |
| `perfect-differential-equations` | Method: validation distinction, derivation/configuration provenance | Method: reproducibility, deep/pathological verification, benchmark scope | **M1 now** |
| `perfect-geometry` | Method: exact scope, authority and failure semantics | Method: exact/reference split, reproducibility, risk-targeted mutation | **M1 now** |
| `perfect-probability` | **Direct/Method:** statistical derivation must not become factual/clinical confidence; method identity retained | Method: rounding/numerical verification and reproducibility | **M1 now** |
| `perfect-statistics` | **Direct:** DERIVED_STATISTICAL semantics, method/sample/assumption provenance, conflicts/unknown | Method: reproducibility and evidence-scoped numerical testing | **M1 now** |
| `perfect-information-theory` | Method: derivation/claim scope and assumptions | Method: numerical/reference independence and reproducibility | **M1 now** |
| `perfect-error-correction` | Method: failure/unknown/outside-radius semantics and negative evidence | Method: exhaustive finite domains, mutation/fuzz, cross-target reproducibility | **M1 now** |
| `perfect-optimization` | Method: assumption/derived-result/validation separation | Method: benchmark equivalence, reproducibility, independent reference | **M1 now** |
| `perfect-signal` | **Direct/Method:** transformation lineage, source-vs-derived separation, quality/gap provenance | Method: deterministic processing, resource and fuzz/benchmark discipline | **M1 now** |
| `perfect-units` | **Direct:** source unit vs normalized value separation, exact conversion provenance | **Direct/Method:** exact/lossy conversion and rounding semantics | **M1 now** |
| `perfect-uncertainty` | **Direct:** measurement uncertainty must remain distinct from certainty/confidence/verification | Method: explicit numeric/rounding semantics and reference evidence | **M1 now** |
| `perfect-mechanics` | Method: validation vs verification, transformation provenance | Method: numerical reproducibility and benchmark/resource scope | **M1 now** |
| `perfect-estimation` | **Direct/Method:** derived-estimate provenance, assumptions, diagnostics != truth | Method: deterministic/reproducible numerical qualification | **M1 now** |
| `perfect-control` | Method: successful simulation != validated stability; exact evidence scope | Method: deterministic/reference/benchmark discipline | **M1 now** |
| `perfect-quantum-information` | Method: derived/probabilistic result provenance and exact claim scope | Method; Specialist only for genuine π-angle/constants needs | **M1 now** |
| `perfect-quantum-circuits` | Method: semantic identity vs derived representation/provenance | Method; Specialist for genuine π-angle representation only | **M1 now** |
| `perfect-quantum-simulation` | Method: deterministic vs stochastic evidence scope, unknown/inconclusive states | Method: independent backend/reference and reproducibility discipline | **M1 now** |
| `perfect-quantum-compilation` | **Direct/Method:** transformation lineage, inconclusive equivalence remains inconclusive | Method; Specialist only for genuine π-angle/synthesis inputs | **M1 now** |
| `perfect-quantum-error-correction` | Method: exact failure/outside-guarantee states, evidence scope | Method: exhaustive domains, independent decoder/reference and fuzz/mutation | **M1 now** |
| `perfect-finance` | **Direct/Method:** source/derived separation, exact decimal provenance, versioned authority | Method: explicit rounding and reproducibility; N/A runtime π | **M1 now** |
| `perfect-meteorology` | **Direct/Method:** versioned source/model provenance, units/uncertainty separation | Method; Specialist only where a genuine π constant is required | **M1 now** |
| `perfect-navigation` | **Direct/Method:** versioned model/source authority, derivation provenance | Method; Specialist where angle/geodesy formulas genuinely require π | **M1 now** |
| `perfect-gnss` | **Direct/Method:** observation/source/derived correction provenance, explicit integrity-claim scope | Method: deterministic/reproducible numeric verification | **M1 now** |
| `perfect-biosignal` | **Direct:** waveform provenance, quality/gaps/transform lineage, LMES-style downstream evidence boundary | Method: deterministic signal processing and qualification discipline; N/A runtime π | **M1 now** |
| `perfect-wire` | **Direct:** canonical-byte/integrity boundaries, source-vs-derived identity, versioned schema authority | **Direct/Method:** cross-host byte reproducibility, exhaustive finite vectors, generated-data checks | **M1 now** |
| `perfect-evidence` | **Direct:** claim-support classes, immutable provenance, scoped verification, unknown/conflict semantics | Method: generated-data provenance, reproducibility, independent qualification patterns | **M1 now** |
| `perfect-codata` | **Direct:** authoritative source/version pinning, source-vs-derived separation, evidence identity | Method: exact numeric/reproducible-generation discipline; N/A runtime π unless a source explicitly requires it | Before M0→M1 |
| `perfect-constants` | **Direct:** authoritative source/version/provenance and derived-view separation | **Specialist/Direct:** Perfectπ owns π; deterministic generated constants and exact target-bit verification | Before M0→M1 |

## Perfect Qualification support repository

`perfect-qualification` is not a family crate, but it MUST enforce the gate at M6 and use the LMES/Perfectπ defect classes when selecting adversarial qualification evidence.

## Interpretation rules

1. **Direct does not automatically mean dependency.** The correct disposition may still be ADAPT_WITH_PROVENANCE or REUSE_METHOD_ONLY.
2. **Method does not mean optional.** If a historical defect class is applicable, the destination must address it or explicitly reject it with technical rationale.
3. **Specialist means ownership is preserved.** Perfectπ remains the π authority; other crates must not duplicate a π engine.
4. This matrix does not import LMES medical semantics into generic crates.
5. This matrix does not award progress or mark any requirement Implemented/Verified/Qualified.
6. Each crate's live `project-status.toml` remains authoritative for lifecycle state.
