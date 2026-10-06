# Perfect Foundations Claim Assurance Standard

Perfect Foundations uses evidence-scoped claims. A statement is not made stronger by confidence, repetition, polished prose, CI color, or agreement among agents.

This standard generalizes proven epistemic-assurance ideas from the owner's Lifetime Medical Evidence System into a domain-neutral engineering contract for Perfect Foundations. It does **not** import medical semantics into the family.

## Source provenance

Reference material used to derive this standard:

- Lifetime Medical Evidence System GitHub mirror commit `95a6cb30cae8cf4a35ff33878e2f9348d1471db5`;
- mirror artifact `docs/requirements/LMES-EAIS-001.md`, blob `0360b5ddf361648878be16a27ab9855e1ce27516`;
- mirror artifact `docs/verification/LMES-VVP-001.md`, blob `44301611148e788444fac8acccc29b114fde243d`.

The LMES repository itself states that GitLab is its authoritative SCM and GitHub is a secondary mirror. Perfect Foundations therefore treats the cited GitHub revision as a reusable reference snapshot, not as proof of LMES's current authoritative state.

## Claim-assurance classes

For material engineering claims, distinguish the support class when it affects interpretation:

- **VERIFIED_REPOSITORY_STATE** — directly observed from the current repository/tool state for the named revision/scope.
- **VERIFIED_PRIMARY_SOURCE** — checked against a current authoritative external primary source.
- **SUPPORTED_BY_PROJECT_AUTHORITY** — supported by an accepted requirement, ADR, policy, or other controlling project artifact.
- **DERIVED_DETERMINISTIC** — calculated by a specified deterministic process with reproducible inputs/configuration.
- **DERIVED_STATISTICAL** — produced by a statistical or empirical process whose method, sample, uncertainty, and assumptions are retained.
- **AI_DERIVED** — produced or interpreted by an AI system and not independently promoted to another class.
- **USER_PROVIDED** — supplied by the user but not independently verified in the current workflow.
- **ASSUMPTION** — deliberately assumed and explicitly scoped.
- **HYPOTHESIS** — plausible but unverified proposition under investigation.
- **CONFLICTING** — material sources or authorities disagree.
- **UNKNOWN** — evidence is insufficient.
- **UNVERIFIABLE_CURRENTLY** — verification is required but unavailable with the present tools/sources.

These are support semantics, not a linear confidence score. A claim may have multiple orthogonal attributes; for example, a deterministic derivation can still depend on user-provided inputs.

## Non-negotiable rules

1. **Evidence before confidence.** Confidence is not verification.
2. **AI is not its own source.** Model memory, repeated generations, or model consensus are not independent evidence.
3. **No fabricated completion.** Missing identifiers, values, dates, tests, results, hashes, revisions, artifacts, or support states remain missing.
4. **Verification scope is exact.** A passing unit test does not prove the crate; a successful build does not prove correctness; a digest match does not prove factual truth; one target does not prove another.
5. **Tool-result honesty.** A command, test, CI job, file, commit, package, target, benchmark, or qualification result is claimed only when actually observed.
6. **Unknown stays unknown.** Failed/unavailable verification becomes UNKNOWN, CONFLICTING, or UNVERIFIABLE_CURRENTLY as appropriate, never an inferred success.
7. **Primary-source freshness.** Changeable standards, dependencies, advisories, APIs, toolchains, and external facts are version/date-bound when material.
8. **Recommendations are not decisions.** Drafts, experiments, proposed ADRs, agent suggestions, and preferred options do not become accepted authority without the controlling process.
9. **Derived output stays derived.** Generated tables, benchmark summaries, charts, transformations, and analyses retain source/derivation identity; repetition does not convert them into source authority.
10. **Conflicts are preserved.** Material disagreement is not silently resolved by convenience, recency, or majority vote without an approved rule.
11. **Negative evidence is disciplined.** Absence of observed failure is not proof of correctness, completeness, safety, security, or performance.
12. **Verification failure is visible.** Skipped, timed-out, permission-blocked, runner-provisioning-failed, unsupported, or indeterminate required checks are not passing.
13. **Claims survive handoff.** Summaries and status reports preserve the support state and enough source/revision context to reconstruct material claims.
14. **No synthetic corroboration.** Mirrors, copied reports, caches, duplicated fixtures, or derivative summaries are not independent corroborating sources unless independence is established.
15. **Quantitative claims preserve method.** Inputs, units, transformations, rounding, configuration, toolchain/target, and algorithm/version are retained when material.

## Verification versus validation

- **Verification** asks whether an implementation/artifact satisfies its specified contract.
- **Validation** asks whether that contract/result is fit for the intended real use.

Passing verification does not automatically establish validation. Perfect Qualification may contain both, but must label them distinctly.

## Engineering use

For a material requirement, ADR, benchmark conclusion, qualification result, or release claim, reviewers should be able to answer:

1. What exactly is being claimed?
2. What support class applies?
3. Which source/evidence supports it?
4. What exact revision/version/configuration was checked?
5. What does the evidence **not** prove?
6. What uncertainty/conflict remains?
7. How can the claim be reproduced or challenged?

If those answers cannot be recovered, the claim is not ready to be treated as verified project authority.

## Perfect Evidence relationship

Perfect Evidence is the intended runtime owner for reusable cross-domain provenance/verification metadata where a stable runtime contract is proven.

This family standard does not force every crate to depend on Perfect Evidence. Build/test/release processes may retain claim-assurance metadata outside production runtime code. A runtime dependency is added only when the crate's public capability materially needs it.

## Perfect Qualification relationship

Qualification evidence must identify:

- exact subject revision;
- requirement/gate being evaluated;
- method/profile;
- environment/toolchain/target/features;
- inputs/corpus/fixtures;
- status: passed, failed, inconclusive, error/not-run;
- evidence artifact identity where retained;
- scope/limitations;
- independent oracle/reference identity where applicable.

A green CI dashboard alone is not a qualification result.

## Status/progress consequence

Claim classification never awards progress by itself. Progress is earned only by the existing gate model and evidence satisfying those gates.
