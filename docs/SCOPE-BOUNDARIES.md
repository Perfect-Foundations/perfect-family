# Scope Boundaries

The family is intentionally broad, but it is not a plan to rewrite every software category in Rust.

## Explicitly not planned as general Perfect crates at this stage

### Networking
No general Perfect TCP/IP, DNS, HTTP, TLS, or QUIC stack is planned. Rust already has strong native networking foundations.

### Cryptography
No general Perfect Cryptography crate is planned. Cryptography requires specialized security review, constant-time and side-channel discipline, and mature implementations already exist. Perfect arithmetic may expose useful primitives, but that does not imply a home-grown cryptographic suite.

### Robotics and drones
No giant Perfect Robotics or Perfect Drone framework is planned. The reusable foundations are Geometry, Mechanics, Estimation, Optimization, Control, Signal, Navigation, GNSS, Units, Probability, and Statistics.

### Biomedical platform
No giant Perfect Biomedical crate is planned. Biosignal handles physiological waveform foundations; standards such as DICOM/FHIR/HL7/terminology should use strong existing Rust implementations unless a concrete deficiency justifies new work.

### Deep-space platform
No Perfect SPICE/astrodynamics clone is currently planned. Navigation, Estimation, Mechanics, Differential Equations, Units, Signal, and Error Correction provide reusable foundations while existing Rust-native astrodynamics/SPICE work can be consumed.

### Linear algebra / FFT / tensor / ML
These are not committed Perfect crates because strong Rust-native implementations already exist. Revisit only if a missing correctness/determinism contract emerges that cannot be layered cleanly on existing work.

### General serialization
Perfect Wire is specifically for canonical deterministic representation where exact bytes matter. It is not a replacement for every serialization framework.

### Time
No Perfect Time crate is currently planned. Use mature high-fidelity Rust time libraries unless future family requirements expose a missing contract.

## Rule for adding a new Perfect project

A new family member should exist only when at least one of the following is true:
- a foundational capability is genuinely missing or fragmented;
- serious Rust users still depend on foreign-language runtimes for the core capability;
- multiple family/application projects need the same primitive with a stable independent contract;
- an existing ecosystem implementation cannot meet required determinism, exactness, safety, resource, or verification guarantees.

Brand expansion alone is never sufficient.
