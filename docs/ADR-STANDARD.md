# Perfect Foundations Architecture Decision Record Standard

Perfect Foundations uses Architecture Decision Records (ADRs) so major design choices remain understandable years after the discussion that produced them.

A chat, issue, pull request, commit message, or code comment may contain useful discussion, but none of them replaces an accepted ADR for decisions that materially define a crate's long-term contract.

## ADR location

Each planned/active crate maintains:

`docs/decisions/`

The directory contains:
- `README.md` — decision index and rules;
- numbered ADR files.

Canonical filename:

`ADR-NNNN-short-kebab-title.md`

Examples:
- `ADR-0001-core-representation.md`
- `ADR-0002-error-taxonomy.md`
- `ADR-0003-msrv-policy.md`

ADR numbers are never reused.

## Status values

Use one of:

- **Proposed** — under review; not authoritative.
- **Accepted** — current architectural decision.
- **Superseded** — replaced by one or more later ADRs.
- **Rejected** — considered and explicitly not chosen.
- **Deprecated** — accepted historically but intentionally being retired.

Do not silently rewrite an Accepted ADR to make history look cleaner. If the decision changes, create a new ADR and supersede the old one.

## Decisions that normally require an ADR

Create an ADR for decisions that materially affect:

- canonical internal/public representation;
- public API shape or central traits;
- error taxonomy;
- rounding/precision/approximation semantics;
- canonical encoding or persisted identity;
- source authority / data edition policy;
- dependency selection for foundational behavior;
- algorithm-family selection when it defines guarantees;
- deterministic/reproducibility behavior;
- threading/parallel semantics;
- workspace/scratch/allocation model;
- `no_std` policy;
- MSRV policy;
- supported target policy;
- unsafe-code boundary;
- FFI/native-runtime boundary;
- cryptographic provider boundary;
- feature architecture;
- interoperability contract;
- compatibility/versioning policy;
- release/qualification exception.

Tiny refactors, local implementation details, and reversible non-contractual choices do not need ADRs.

## Required ADR fields

Every ADR includes:

- ID;
- title;
- status;
- date;
- owners/reviewers;
- related requirements;
- related issues/PRs when available;
- supersedes / superseded-by when applicable.

And these sections:

### Context

What problem/constraint caused the decision to be needed?

### Decision

What is being decided? State it precisely.

### Rationale

Why is this the preferred choice?

### Alternatives considered

What serious alternatives were evaluated and why were they not selected?

### Consequences

Record both benefits and costs.

### Compatibility impact

Does this affect public API, semantics, persisted data, wire compatibility, MSRV, targets, features, or migration?

### Verification / evidence

How will the decision be tested or independently supported?

### Traceability

Which requirements/gates depend on this decision?

## ADR acceptance rule

An ADR becomes Accepted only when:

1. the decision is specific enough to implement/test;
2. relevant requirements are identified;
3. compatibility impact is understood;
4. verification approach is identified;
5. conflicts with family policy are resolved or explicitly approved;
6. the crate's decision index is updated.

## Superseding a decision

A replacement ADR must:
- identify the ADR it supersedes;
- explain why the old decision is no longer sufficient;
- describe migration/compatibility impact;
- update affected requirements and traceability.

The old ADR remains in the repository as historical evidence.

## Cross-family decisions

A crate-local ADR must not unilaterally redefine a family-wide contract.

If a decision changes:
- glossary meaning;
- dependency-layer rules;
- qualification model;
- status scoring;
- FFI policy;
- canonical family ownership;
- specialist/aggregator authority;

the family record in `perfect-family` must also be updated.

## Decision quality rule

The purpose of an ADR is not to justify a foregone conclusion.

Alternatives should be represented fairly, evidence should be cited where available, and unresolved uncertainty should be recorded instead of disguised as confidence.
