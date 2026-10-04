# Perfect Foundations Excellence Doctrine

Perfect Foundations is not intended to be merely adequate infrastructure.

The engineering objective is to produce foundations that are **best-in-class for
their defined contracts and supported configurations**, and to keep improving
them when evidence shows that a better design, algorithm, representation,
metadata model, verification method, dependency structure, or implementation is
possible.

This is an engineering objective that must be earned with reproducible evidence.
It is not permission to make unsupported absolute claims such as “fastest,”
“smallest,” “error-free,” or “most secure” without a defined comparison,
configuration, benchmark, and retained result.

## 1. Hard constraints and optimization targets

Correctness and explicit semantics are hard constraints.

An optimization that changes a documented result, rounding rule, failure
classification, determinism guarantee, canonical representation, or safety
boundary is not an optimization unless that contract change is separately
approved.

Subject to those hard constraints, every crate should actively optimize the
dimensions that matter to its domain:

- mathematical/numerical correctness and attainable accuracy;
- latency and throughput;
- algorithmic complexity and scaling;
- peak memory and steady-state memory;
- allocation count and allocation size;
- stack usage;
- executable/text/rodata/writable-data size;
- dependency count and transitive dependency weight;
- compile time and build complexity where material;
- startup/initialization cost;
- deterministic and reproducible behavior;
- portability and cross-target consistency;
- `no_std`, no-allocation, and embedded suitability where practical;
- energy/cycle cost where the target and evidence justify measuring it;
- security, unsafe-code exposure, FFI/native-runtime exposure, and attack surface;
- panic/failure-path discipline;
- API clarity and misuse resistance;
- package/distribution/offline-build quality;
- maintainability without sacrificing the stronger requirements above.

No single metric is automatically dominant. Where goals conflict, the project
must expose the tradeoff explicitly and choose or provide profiles that preserve
the domain contract.

## 2. Best available work first

Before significant implementation or optimization, inspect:

1. existing Perfect-family implementations;
2. Perfectπ where technically relevant and read-only;
3. mature Rust crates;
4. authoritative/reference implementations in other ecosystems;
5. standards, papers, proofs, and published algorithms relevant to the domain;
6. retained benchmark/resource evidence from serious alternatives.

Reuse proven work when it already satisfies the contract.

Do not rewrite for branding or ownership.

Conversely, existing work is not protected from replacement. If evidence shows a
custom Perfect implementation can materially improve the required contract,
performance, resource behavior, portability, determinism, dependency footprint,
or assurance level, building that implementation is encouraged.

## 3. Custom algorithm rule

A Perfect crate may and should implement a custom algorithm when the evidence
shows that doing so is materially better for its contract.

Examples of valid reasons include:

- stronger correctness or certified bounds;
- correctly rounded or exact results where competitors approximate;
- deterministic/reproducible behavior;
- lower asymptotic or practical runtime;
- lower memory or allocation cost;
- smaller code/data footprint;
- better `no_std` / embedded behavior;
- reduced dependency or FFI exposure;
- stronger pathological-input behavior;
- better controllable resource limits;
- a missing algorithm or capability;
- a design that enables materially stronger verification.

Custom algorithms require provenance, an explicit semantic contract, independent
verification, pathological/adversarial testing, and representative comparison
with the best relevant alternatives.

When practical, retain an algorithmically independent reference implementation
for tests/qualification even after a faster production implementation replaces
it. Perfectπ's production Chudnovsky path plus independent Machin/reference
verification is the model: the production algorithm and the oracle should not
silently collapse into the same implementation.

## 4. Algorithm ownership and extraction

Domain algorithms belong in their owning specialist crate by default.

Do not create a generic algorithm dumping ground.

When multiple crates independently need the same stable generalized machinery:

1. prove the reuse is real;
2. identify the narrow independent contract;
3. choose the correct existing owner if one exists;
4. otherwise consider a new sharply scoped Perfect crate;
5. preserve provenance and cross-crate qualification.

Shared implementation is extracted because ownership/reuse is proven, not
because the word “algorithm” is generic.

## 5. Metadata improvement rule

Metadata is part of correctness when downstream interpretation, provenance,
reproducibility, auditability, or safe use depends on it.

A Perfect crate should define custom typed metadata when doing so materially
improves the result or prevents ambiguity. Examples include:

- algorithm identity/version;
- parameter/threshold/configuration identity;
- precision and rounding policy;
- units, scale, coordinate/reference frame, or representation;
- source/dataset/model version;
- uncertainty/covariance links;
- transformation/derivation history;
- deterministic seed or stochastic configuration;
- solver/tolerance policy;
- target/backend/profile identity where results or resource evidence depend on it;
- qualification/evidence identifiers;
- schema/serialization version.

Metadata should be minimal for the contract, deterministic where canonicality is
promised, and should not force heavy runtime costs onto users that do not need it.

Domain-specific metadata remains with the domain owner. Cross-domain metadata
primitives should be generalized only after proven reuse, normally toward
Perfect Evidence, Perfect Wire, or another intentional owner. A new shared
metadata crate is justified only when a stable independent runtime contract is
demonstrated.

## 6. Competitor/reference baseline

Each material capability should identify the strongest relevant comparison set,
which may include:

- leading Rust crates;
- standard-library functionality;
- widely used C/C++/Fortran/Go/Python/Java implementations;
- specialist numerical libraries;
- authoritative research/reference implementations;
- hardware/vendor implementations where relevant.

Comparisons must be fair:

- same operation/semantic contract;
- comparable precision and error guarantees;
- comparable input domain;
- comparable target/hardware/toolchain;
- release builds and documented features;
- retained benchmark corpus and harness;
- versions/revisions recorded.

A faster result with weaker semantics is not automatically superior.
A smaller binary that omits required behavior is not automatically superior.

## 7. Pareto and profile rule

Some objectives conflict.

A crate may legitimately provide separate profiles/features/algorithms such as:

- smallest/no-allocation embedded path;
- portable default path;
- high-throughput path;
- high-precision/certified path;
- optional hardware acceleration.

Those profiles must share explicit semantics where claimed and must not hide
meaningful behavioral changes behind a performance feature.

The preferred default should sit on the project's measured Pareto frontier for
the intended general-use contract, not merely inherit historical defaults from a
dependency.

## 8. Measurement requirements

Performance/resource work should measure the dimensions material to the crate,
including where applicable:

- latency distributions;
- throughput;
- scaling with input size/precision;
- peak/steady memory;
- allocations;
- stack;
- code/text/rodata/data size;
- linked binary delta;
- compile-time impact;
- dependency graph delta;
- cycle/instruction counts;
- startup cost;
- target-specific behavior.

Measurements must distinguish host benchmarking from embedded/target claims.
CI-host wall-clock timing alone is not sufficient evidence for tight performance
claims.

Regression gates should use metrics stable enough to enforce responsibly.
Noisy metrics may remain retained evidence without becoming hard CI thresholds.

## 9. Security and failure discipline

Optimization must reduce or at least not silently expand attack/failure surface.

Projects should prefer:

- safe Rust;
- typed, explicit failure;
- validation before expensive work;
- resource ceilings for attacker-controlled inputs where appropriate;
- no hidden network or runtime code acquisition;
- no unnecessary build scripts/native code;
- minimal unsafe/FFI boundaries when unavoidable;
- fuzzing/sanitizers/Miri/property/mutation testing appropriate to the risk.

Constant-time or side-channel-resistant behavior is never implied by being
“secure”; such claims require a dedicated contract and evidence.

## 10. Embedded and smallest-target rule

The smallest supported target must not pay for capabilities it does not use.

Where practical:

- keep the core `no_std`;
- avoid allocation in bounded/common paths;
- isolate large tables and heavy algorithms behind features;
- permit caller-owned storage/workspace;
- avoid hidden initialization/global state;
- measure code/data/stack footprints on representative constrained targets;
- make expensive precision/capability opt-in.

Desktop/server convenience may be layered on top without contaminating the
smallest core.

## 11. Improvement review

At architecture, hardening, qualification, and release-candidate review, each
crate must ask:

- What is currently the best relevant alternative?
- Where are we objectively worse?
- Is the difference required by a stronger semantic contract, an accepted
  tradeoff, or an implementation opportunity?
- Can a better algorithm/representation/metadata model remove that gap?
- Can dependencies, allocations, code size, or build complexity be reduced?
- Can verification become more independent or exhaustive?
- Can the embedded/portable path become stronger?
- Are there known high-value feasible improvements not yet implemented?

A known material improvement must be one of:

1. implemented and evidenced;
2. rejected with a documented technical reason;
3. explicitly deferred with scope, rationale, and release impact.

It must not simply disappear from the record.

## 12. Claim discipline

“Best,” “fastest,” “smallest,” “most accurate,” “correctly rounded,” “secure,”
“verified,” “qualified,” and similar claims are scoped engineering claims.

A comparative claim must identify enough of the following to reproduce it:

- exact Perfect revision;
- competitor/version;
- operation and semantics;
- corpus/input distribution;
- features/configuration;
- toolchain;
- target/hardware;
- metric and methodology.

The family may set the goal of surpassing competitors broadly. Public claims are
made only where the evidence supports them.

## 13. Release consequence

A release candidate is not blocked merely because theoretical improvement is
always possible.

It **is** blocked by a known material defect or a known feasible improvement that
is required to meet an approved contract/gate and has neither been completed nor
explicitly deferred by the appropriate decision process.

The objective is continual engineering improvement without turning “perfect” into
an unverifiable slogan.
