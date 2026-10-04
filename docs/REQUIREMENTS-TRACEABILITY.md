# Perfect Foundations Requirements & Traceability Standard

Perfect Foundations projects are intended to become long-lived infrastructure. Requirements therefore need durable identities and a visible chain from intent to evidence.

The family traceability goal is:

`Requirement → ADR/design → Implementation → Test/reference evidence → Qualification/release gate`

Traceability should be strong enough to answer:

- Why does this behavior exist?
- Where was the design choice made?
- What code implements it?
- What proves it works?
- Which release/qualification gate depends on it?
- What breaks if it changes?

## Project structure

Each planned/active crate maintains:

- `docs/requirements/README.md` — requirement index and requirement records;
- `docs/TRACEABILITY.md` — project traceability matrix;
- `docs/decisions/` — ADRs referenced by requirements.

The structure may later be machine-generated, but the identifiers and relationships must remain stable.

## Requirement identifiers

Canonical pattern:

`REQ-<CATEGORY>-NNNN`

Recommended categories:

- `CORE` — fundamental functional behavior
- `SEM` — semantic/numerical guarantees
- `ERR` — errors/failure behavior
- `PERF` — performance/resource requirements
- `ALG` — algorithm selection, complexity, dispatch, certification, or independent-reference requirements
- `META` — typed metadata, provenance linkage, algorithm/configuration identity, or schema/version requirements
- `PORT` — target/platform/no_std/MSRV requirements
- `PKG` — Cargo/distro/offline packaging
- `SEC` — security/supply-chain/unsafe/FFI
- `INT` — interoperability/integration
- `DATA` — authoritative datasets/provenance/versioning
- `DET` — determinism/reproducibility/canonicality
- `VER` — verification/qualification evidence
- `DOC` — documentation/public-contract requirements

Projects may add a domain category when it materially improves clarity.

Numbers are never reused after publication.

## Requirement statuses

- **Proposed**
- **Approved**
- **Implemented**
- **Verified**
- **Qualified**
- **Deferred**
- **Superseded**
- **Rejected**

Status advancement must reflect evidence, not intention.

## Requirement strength

Use RFC-style normative words consistently:

- **MUST** — mandatory for the applicable scope.
- **MUST NOT** — prohibited.
- **SHOULD** — expected unless a documented reason justifies deviation.
- **SHOULD NOT** — discouraged unless justified.
- **MAY** — optional/permitted.

## Required requirement fields

Each requirement record should identify:

- Requirement ID
- Status
- Requirement statement
- Rationale
- Applicability / configuration
- Source / authority
- Related ADRs
- Verification method
- Qualification/release gate
- Implementation references when known
- Evidence references when known

## Good requirement properties

A useful requirement is:

- specific;
- testable or otherwise verifiable;
- scoped;
- unambiguous;
- necessary;
- traceable to a purpose/source;
- free of premature implementation detail unless the implementation itself is required.

Bad:

> The crate should be fast.

Better:

> REQ-PERF-0007 — For the qualified x86_64 baseline, the scalar parsing path MUST process the retained benchmark corpus without a regression greater than the project's approved threshold relative to the qualified release baseline.

The exact threshold can be approved later; the requirement structure makes the decision visible.

## Architecture requirements

Before M0 Architecture can close, requirements should exist for the material decisions relevant to that crate, including as applicable:

- semantic/numerical contract;
- representation invariants;
- error behavior;
- deterministic behavior;
- resource/allocation limits;
- target/MSRV/no_std policy;
- dependency/FFI/unsafe boundaries;
- interoperability;
- verification/reference strategy;
- distro/offline packaging;
- security/supply-chain requirements.

## Traceability matrix

`docs/TRACEABILITY.md` should contain at least:

| Requirement | Status | ADR / design | Implementation | Verification evidence | Qualification / release gate |
|---|---|---|---|---|---|

Empty columns are acceptable before implementation; missing requirement identity is not.

## Evidence rules

A requirement may move to:

### Implemented

when the implementation exists and is linked.

### Verified

when the specified verification evidence passes for the applicable configuration.

### Qualified

when all applicable project/family qualification and release-gate evidence is satisfied.

Implementation alone is never qualification.

## Change control

If a requirement changes materially:

1. record why;
2. update or supersede the requirement;
3. update affected ADRs;
4. update implementation/tests/evidence;
5. reassess compatibility and release impact.

Requirements must not silently drift to match whatever the current code happens to do.

## External standards and authority

When a requirement derives from an external standard, dataset, regulation, or specification, record:

- authority/source;
- edition/version/profile;
- relevant section/identifier;
- whether the project is claiming conformance or merely using the source as design/reference guidance.

Do not claim standard conformance without the corresponding conformance requirements and evidence.

## Relationship to live status

Status percentages may be informed by completed requirement/gate evidence, but requirement count itself is not a progress metric.

Creating 100 weak requirements must never increase project progress.

Progress comes from completing the defined engineering gates in the family Status System.
