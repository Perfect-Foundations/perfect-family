# Historical Proven-Reuse Gate

Perfect Foundations is younger than two owner projects that already contain substantial independently reviewed engineering work:

- **Lifetime Medical Evidence System (LMES)** — assurance, authority, evidence, traceability, verification-scope, negative-path, and failure-state discipline.
- **Perfectπ / `Perfect-Foundations/perfect-pi`** — numerical semantics, certification, resource control, reproducibility, independent-oracle, fuzz/mutation, and measurement discipline.

The family MUST systematically evaluate that proven work before rediscovering the same defects.

This gate is a **reuse/assurance control**, not a dependency mandate and not a progress award.

## Protected source boundaries

### Perfectπ

Perfectπ remains read-only from Perfect Foundations work. The family may consume it when π is genuinely required and may generalize techniques with provenance, but MUST NOT modify/fork it or make it an unrelated utility dependency.

Current reviewed source points are recorded in the [Proven Reuse Register](PROVEN-REUSE-REGISTER.md).

### LMES

LMES remains an independent medical system. Perfect Foundations may generalize cross-domain engineering lessons but MUST NOT import medical truth, PHI/PII policy, clinical semantics, or LMES authority decisions into generic crates.

The LMES GitHub repository is a secondary mirror; its cited revision is reference provenance, not proof of current authoritative GitLab state.

## Required dispositions

For each applicable reuse item, the destination records exactly one disposition:

- **REUSE_DEPENDENCY** — the source project is the correct runtime owner and an intentional dependency is justified.
- **ADAPT_WITH_PROVENANCE** — reusable implementation/contract machinery is generalized into the correct Perfect owner with exact source provenance.
- **REUSE_METHOD_ONLY** — verification, assurance, fuzzing, benchmarking, certification, or process methodology is reused without copying runtime implementation.
- **EVALUATED_REJECTED** — evaluated and rejected with a durable technical reason.
- **DEFERRED_WITH_IMPACT** — deferred, with the affected milestone/release capability and recheck trigger recorded.
- **NOT_APPLICABLE** — explicitly not relevant to the destination contract, with a short reason when non-obvious.

Silence is not a disposition.

## Required review record

A material reuse decision MUST retain enough information to reconstruct the decision:

1. source project and exact revision;
2. source artifact/algorithm/contract or defect class;
3. destination crate and requirement/ADR affected;
4. chosen disposition;
5. transfer/ownership boundary;
6. implementation reference when adapted;
7. independent verification/reference plan;
8. licensing/provenance review where code/data is adapted;
9. unresolved limitations or deferred impact;
10. next mandatory recheck gate.

Source verification never automatically transfers to the destination.

## Lifecycle checkpoints

### M1 — Minimal Correct Core

Before M1 closes, the crate MUST review its row in the [Proven Reuse Applicability Matrix](PROVEN-REUSE-MATRIX.md), the live [Proven Reuse Register](PROVEN-REUSE-REGISTER.md), and relevant source revisions.

The M1 review answers:

- Which predecessor contracts/techniques apply to this core?
- Which are runtime dependencies versus adapted methods?
- Which known defect classes require preventive tests now?
- Which items are rejected/deferred, and why?

### M3 — Performance / algorithm architecture

Before M3 closes, re-review Perfectπ-derived algorithm/resource/measurement lessons and any LMES-derived evidence/derivation semantics affected by optimization.

An optimization MUST NOT erase provenance, weaken semantics, narrow fuzz reach, silently change resource limits, or replace an independent oracle with a copied implementation.

### M5 — Hardening

Before M5 closes, applicable historical defect classes MUST be represented by adversarial/property/fuzz/mutation/regression evidence or be durably marked NOT_APPLICABLE with technical rationale.

Deep-path reachability matters: a fuzz target that cannot reach the risky algorithm is not evidence for that algorithm.

### M6 — Qualification / prerelease

Before M6 closes, Perfect Qualification MUST verify that:

- all earlier reuse dispositions are present and revision-bound;
- adapted work has destination-specific verification;
- copied/adapted machinery is not used as its own independent oracle;
- unresolved DEFERRED_WITH_IMPACT items are explicitly release-compatible or blocking;
- no required check is treated as passing when unavailable, skipped, indeterminate, permission-blocked, or runner-provisioning-failed.

## Catch-up rule for projects already beyond a checkpoint

This standard does not retroactively falsify previously retained evidence.

A project already past one or more checkpoints MUST complete a catch-up review before its **next unresolved milestone, requalification, release-candidate refresh, or public-release claim**.

No prior qualification report is silently rewritten. New claims use the new standard.

## Historical defect classes to prevent

### LMES-derived assurance failures

The reusable classes include:

- stale or contradictory authority/status text;
- semantic routing or parser scope that can falsely pass prohibited content;
- verification claims broader than the exact checked scope;
- required-test isolation and fixture-discovery gaps;
- dependency-direction drift;
- suppression/exception controls that can hide required security checks;
- source/coverage/reference drift;
- synthetic fixtures or mirrors being mistaken for independent authority;
- unavailable/indeterminate checks being promoted to success.

### Perfectπ-derived numerical/verification failures

The reusable classes include:

- precision-dependent certification cliffs that representative small tests miss;
- fuzz selectors or configurations that are syntactically present but unreachable;
- fuzz campaigns that never reach the deep arithmetic path they claim to test;
- production/reference implementations losing algorithmic independence;
- optimization accepted on timing without attached correctness/certification evidence;
- resource/precision limits being checked after mutation instead of before;
- benchmark/size measurements being generalized beyond the measured target/configuration.

These classes are prompts for destination-specific review, not claims that every crate contains the same defect.

## Status consequence

Creating a reuse document or disposition does **not** award lifecycle percentage.

However, when this gate applies to a milestone, that milestone MUST NOT be newly closed without the required review evidence.
