# Perfect Foundations Benchmarking Standard

Benchmarking is the default decision instrument for optimization across Perfect
Foundations.

The purpose is to replace intuition, folklore, and premature tuning with retained
evidence. When two implementations, algorithms, representations, dependency
choices, feature layouts, or configuration thresholds compete, the decision
should be driven by correctness first and measurement second.

## 1. Core rule

No material optimization should be accepted merely because it is expected to be
faster, smaller, or cheaper.

For a meaningful optimization claim:

1. preserve or explicitly strengthen the approved semantic/correctness contract;
2. define the metric(s) that matter;
3. establish a retained baseline;
4. measure the candidate under comparable conditions;
5. compare relevant alternatives where useful;
6. retain the exact revisions/configurations/toolchain/target;
7. verify the result is reproducible enough to support the decision.

If the metric is too noisy to enforce as a hard CI gate, retain the evidence and
use statistically responsible review instead of pretending the noise is signal.

## 2. What should be benchmarked

Benchmarking is not limited to wall-clock speed.

Projects should measure the dimensions material to their contract, including as
applicable:

- latency;
- throughput;
- tail latency/distribution shape;
- scaling with input size, precision, dimensions, sparsity, or workload shape;
- peak resident memory;
- steady-state memory;
- allocations and bytes allocated;
- stack usage;
- code/text/rodata/data size;
- final linked binary delta;
- compile time;
- incremental build impact;
- dependency graph size/weight;
- initialization/startup cost;
- cycle/instruction counts;
- branch/cache behavior where material;
- I/O volume;
- temporary storage;
- energy/power where measurement is credible;
- embedded flash/RAM footprint;
- deterministic-resource bounds where promised.

Correctness/accuracy metrics are measured alongside performance whenever the
implementation can trade one for the other.

## 3. Baseline hierarchy

A benchmark should compare against one or more of:

1. the currently qualified Perfect implementation;
2. the previous release/candidate;
3. the simplest correct/reference implementation;
4. the strongest relevant Rust competitor;
5. the strongest relevant external implementation;
6. a theoretical/algorithmic bound when useful;
7. hardware/vendor acceleration when that is a relevant deployment option.

The baseline set should be strong enough to answer whether the new implementation
is actually better, not merely better than an intentionally weak comparison.

## 4. Fair-comparison rule

Comparisons must keep material semantics equivalent.

Do not compare:

- different precision and call it a speed win;
- approximate output against exact/certified output without labeling the difference;
- different error behavior;
- different supported domains;
- warm-cache against cold-cache without recording it;
- debug against release;
- vectorized/native-tuned code against a portable build without identifying the distinction;
- one-time setup against steady-state cost without separating them.

Any unavoidable semantic difference must be stated next to the benchmark result.

## 5. Corpus and workload design

Benchmark corpora should include more than happy-path examples.

As applicable include:

- common realistic inputs;
- tiny inputs;
- threshold/boundary inputs;
- very large inputs;
- pathological/adversarial inputs;
- sparse/dense cases;
- structured/random cases;
- inputs around algorithm-dispatch thresholds;
- embedded/constrained profiles;
- repeated steady-state workloads;
- startup/one-shot workloads.

Retained corpora should be deterministic where possible. Random corpus generation
must record seeds and generator revisions.

## 6. Algorithm dispatch and thresholds

If multiple algorithms are available, dispatch thresholds must be measured rather
than guessed.

For each threshold:

- benchmark both algorithms around the crossover region;
- measure on relevant targets/configurations;
- retain enough samples to avoid selecting a threshold from noise;
- consider code-size and memory cost in addition to throughput;
- document whether the threshold is global, target-specific, feature-specific, or dynamic.

Thresholds are implementation parameters and may evolve when evidence changes,
provided the public semantic contract is preserved.

## 7. Embedded and constrained targets

Host benchmarks do not establish embedded performance.

For supported constrained targets, measure what can be measured credibly:

- flash/code size;
- static data;
- stack;
- heap/allocation usage;
- cycle counts where available;
- execution time on representative hardware/emulator when meaningful;
- feature-cost deltas.

If execution benchmarking is not practical for a target, do not invent a claim;
retain compile/size/resource evidence and state the limitation.

## 8. Binary and compile-size optimization

Binary footprint is a first-class metric.

Where material, benchmark:

- minimal-feature library;
- default-feature library;
- representative linked executable;
- optional feature deltas;
- dependency-induced size deltas;
- table/data-section sizes;
- panic/unwind configuration effects where relevant.

Compile-time and build-graph cost should also be measured when a dependency or
code-generation strategy materially changes them.

## 9. Statistical discipline

For noisy timing metrics:

- use repeated samples;
- retain raw or sufficiently summarized results;
- record median/mean and dispersion as appropriate;
- isolate warmup where relevant;
- avoid declaring wins within measurement noise;
- investigate outliers rather than automatically deleting them;
- prefer stable microbenchmarks for algorithm comparisons and representative
  end-to-end benchmarks for user-visible impact.

A single CI wall-clock observation is not a performance result.

## 10. Benchmark environment record

Retained benchmark evidence should record enough to reproduce the run, including
as applicable:

- exact Perfect revision;
- exact competitor revision/version;
- Rust/toolchain version;
- compiler flags/profile;
- feature set;
- target triple;
- CPU/architecture;
- OS/kernel;
- memory;
- relevant hardware acceleration;
- benchmark harness revision;
- corpus revision;
- command line;
- sample/repetition count;
- environment variables that affect behavior.

## 11. Optimization workflow

The preferred loop is:

1. establish correctness;
2. measure the current baseline;
3. identify the actual bottleneck/resource cost;
4. form a specific hypothesis;
5. make the smallest complete change;
6. rerun correctness/verification;
7. rerun benchmarks;
8. compare all material metrics;
9. keep the change only when the evidence justifies it;
10. retain the result and update thresholds/baselines if qualified.

This applies to algorithm changes, dependency choices, allocations, data layout,
feature decomposition, metadata representation, table generation, caching,
vectorization, parallelism, unsafe/FFI acceleration, and compile/package choices.

## 12. No benchmark-driven semantic erosion

Benchmarking optimizes implementations, not truth.

A faster implementation that violates exactness, rounding, determinism,
canonicality, security, resource limits, or error semantics is a regression unless
the contract itself is deliberately changed through the normal requirement/ADR
process.

Performance shortcuts must never silently redefine the public contract.

## 13. Multi-objective decisions

The winner is not always the implementation with the lowest latency.

Projects should consider Pareto tradeoffs among:

- correctness/assurance;
- latency;
- throughput;
- memory;
- allocation;
- binary size;
- stack;
- dependency weight;
- portability;
- embedded suitability;
- security;
- maintainability.

If no single implementation dominates, expose profiles/features/algorithm
selection where doing so keeps the API coherent and the smallest user from paying
for capabilities it does not need.

## 14. Competitor optimization loop

Competitor/reference benchmarks should not be a one-time release exercise.

At major milestones and before stable release:

1. recheck leading alternatives;
2. update competitor versions;
3. rerun relevant benchmark suites;
4. inspect areas where Perfect is worse;
5. determine whether the gap is a stronger-contract tradeoff or an improvement opportunity;
6. implement and retest high-value feasible improvements;
7. retain evidence for accepted tradeoffs.

The goal is continual competitive improvement without weakening correctness.

## 15. Regression gates

Stable deterministic metrics may become CI gates.

Examples:

- binary size must not exceed an approved threshold;
- allocations must remain zero on a designated path;
- memory/stack must remain below a target ceiling;
- deterministic operation count must remain bounded;
- microbenchmark regression must remain inside an approved stable threshold.

Noisy host timing should usually be retained and reviewed rather than used as a
brittle hard gate unless the project has demonstrated a stable methodology.

Threshold changes require evidence and should not be loosened merely to make CI
green.

## 16. Evidence retention

Each project should retain benchmark evidence in a machine-readable form where
practical and document:

- what changed;
- why it was tested;
- before/after results;
- correctness/semantic equivalence;
- competitor/reference results;
- decision;
- remaining regressions/tradeoffs.

Benchmarks are engineering evidence, not decoration.

## 17. Relationship to qualification and release

Benchmarking begins during implementation and continues through hardening.

Before private release-candidate/default-grade status, applicable R5 evidence must
show:

- representative baseline coverage;
- competitor/reference comparison;
- resource behavior;
- no unexplained material regressions;
- known material disadvantages corrected, justified, or explicitly deferred.

Benchmarking therefore removes guesswork from optimization while still keeping
correctness, explicit semantics, and reproducible evidence above raw speed.
