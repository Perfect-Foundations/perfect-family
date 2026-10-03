# Perfect Foundations Presentation Standard

This document defines the initial visual and information architecture for Perfect Foundations repository landing pages.

The goal is **clarity + technical depth + visual coherence**. A README should be enjoyable to read without turning into a marketing page or implying features that do not exist.

## 1. Required landing-page structure

Planned crate repositories should normally include:

1. centered project title;
2. one-sentence technical tagline;
3. restrained status/language/family/license badges;
4. **Vision**;
5. explicit current-status disclaimer;
6. authoritative **Live project status** dashboard;
7. **At a glance** table;
8. **Why this exists**;
9. **Goals**;
10. **Planned capability map**;
11. **Where this becomes useful**;
12. **Place in the Perfect family** using native GitHub Markdown/table presentation;
13. provisional upstream/downstream relationships;
14. **Design questions to settle**;
15. **Explicit non-goals**;
16. **Quality bar**;
17. visual **Roadmap**;
18. **Design dossier** with Blueprint, ADRs, requirements, traceability, and family-standard links;
19. family navigation links.

Public/mature repositories may replace planning language with real implementation, compatibility, examples, API, benchmarks, release, and evidence sections as they become true.

## 2. Truthfulness rule

A beautiful README must never make the repository look more implemented than it is.

Use explicit lifecycle language:

- Reserved
- Architecture planning
- Implementation
- Hardening
- Qualification
- Prerelease
- Stable
- Maintenance

Planned capability sections must say they are planned.

Badges must represent current facts, not desired future states.

## 3. Visual language

### Color direction

The family uses a restrained technical palette in static badges:

- cyan/teal for family identity and primary information;
- slate/graphite for status/architecture;
- Rust orange/brown for language;
- muted gray for undecided metadata such as license/MSRV.

Do not turn READMEs into a rainbow of decorative badges.

### Layout

Prefer:

- centered hero only at the top;
- normal left-aligned technical content below;
- short paragraphs;
- tables for dense metadata;
- bullets for scannability;
- native GitHub Markdown tables/flows for architecture and lifecycle relationships;
- horizontal rules only for major visual breaks.

Avoid:

- giant ASCII art;
- dozens of badges;
- animated GIFs;
- meaningless “enterprise-grade / blazing-fast / revolutionary” claims;
- large decorative images that push engineering information below the fold.

## 4. Technical depth standard

Every project page should answer:

- What exact foundational problem is being solved?
- Why is a separate crate justified?
- What is in scope?
- What is deliberately out of scope?
- What existing Rust/non-Rust work should be reused or compared?
- What lower Perfect layers may be needed?
- Who benefits from the crate?
- What design questions remain unresolved?
- What evidence will be required before release?
- What would make the implementation fail its stated mission?

## 5. Maturity evolution

### Reserved / architecture

Focus on purpose, intended capabilities, boundaries, design questions, and quality targets.

### Implementation

Add:

- current supported feature table;
- examples;
- API/design notes;
- current limitations;
- build/test instructions.

### Hardening / qualification

Add:

- benchmark results;
- reference comparisons;
- fuzz/mutation results;
- target matrix;
- MSRV;
- feature matrix;
- known limitations;
- qualification evidence links.

### Stable

Lead with what exists rather than what is planned.

Include:

- installation;
- minimal example;
- supported contract/version;
- docs.rs/crates.io links;
- compatibility;
- changelog/release policy;
- evidence/benchmark summaries.

## 6. Family navigation

### Design-record navigation

Every planned/active crate README should make the durable design records easy to reach:

- Project Blueprint;
- live `project-status.toml`;
- Architecture Decision Records;
- Requirements index;
- Traceability matrix.

The README remains the front door; these records hold the implementation-starting detail and architectural history.



Every project README should make it easy to reach:

- `perfect-family`;
- `perfect-qualification`;
- the Perfect Family GitHub Project.

Specialist relationships should also be linked once public, but links must not falsely imply a dependency.

## 7. Accessibility and maintainability

- Meaningful text must not exist only inside images.
- Do not depend on Mermaid/rich-display rendering for required information; use native Markdown so core content renders reliably.
- Avoid relying on color alone.
- Keep badge alt text meaningful.
- Use standard GitHub Markdown/HTML that renders reliably.
- Favor structures that can be updated mechanically across the family when standards change.

## 8. The standard itself may evolve

This is the initial family presentation system.

Changes should improve readability, factual precision, or maintenance—not merely add decoration.


## 9. Live status presentation

Every planned or active Perfect crate must maintain an authoritative root-level `project-status.toml`.

The README dashboard should surface, at minimum:

- lifecycle and health;
- current milestone and next gate;
- overall weighted progress;
- architecture, implementation, verification, distro, qualification, and release progress;
- default-grade readiness;
- blocker counts;
- current design-question count;
- CI health;
- MSRV, license, release state, and last qualified revision when available;
- expandable current gate accounting and project-specific design questions.

Progress bars must use native Markdown/text and must not depend on Mermaid or another rich-display renderer.

The detailed status-scoring contract is owned by [STATUS-SYSTEM.md](STATUS-SYSTEM.md).
