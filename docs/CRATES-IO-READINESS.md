# crates.io Readiness and Publication Policy

Perfect Foundations separates **registry readiness** from **public publication**.

Every Rust crate should become crates.io-ready while it is still private. Actual
publication, repository opening, license selection, public security-channel
verification, tagging, and docs.rs/crates.io release are intentionally deferred
until explicit open-release authorization.

This keeps publication as a controlled deployment step rather than a late
engineering project.

## 1. Private crates.io-ready state

As soon as a repository has a real Cargo package, its manifest and package
pipeline must be maintained as though it could be published, except for the
deliberately deferred open-release fields.

Required while private:

- `publish = false`;
- package name and private version;
- edition and explicit `rust-version`;
- accurate description;
- repository URL;
- homepage URL where appropriate;
- future docs.rs documentation URL;
- README path;
- crates.io-valid keywords and categories;
- complete feature declarations;
- materially justified dependency metadata;
- no hidden build-network requirements;
- `cargo package --list` inspection;
- `cargo package` from a clean checkout;
- build/test of the produced package;
- offline build of the produced package from a populated Cargo cache;
- rustdoc with warnings denied;
- retained package/qualification evidence.

The project license may remain undecided while the repository is retained
privately when the owner has explicitly deferred that decision. In that state,
the manifest should not invent a license. `project-status.toml` records the
license as TBD and the final open-release license gate remains pending.

## 2. Perfect-to-Perfect dependencies while private

Private development must not require crates.io publication.

When a Perfect crate consumes another unpublished Perfect crate, use an exact
Git revision **and** a registry-compatible version requirement:

```toml
perfect-numeric = {
    version = "=0.1.0",
    git = "https://github.com/Perfect-Foundations/perfect-numeric.git",
    rev = "<exact-qualified-sha>",
    default-features = false,
}
```

Rules:

- `rev` pins the exact private source used for engineering/qualification;
- `version` defines the registry contract Cargo will use when packaging for
  crates.io;
- the dependency must follow the family DAG;
- downstream qualification records the exact upstream SHA;
- moving the SHA requires revalidation appropriate to the dependency change;
- unpublished Perfect dependencies do not force early registry publication.

Before any public downstream publication, every non-development Perfect
dependency must already exist on crates.io at a compatible released version.

## 3. Package contract checks

Every implemented crate CI should eventually enforce:

1. clean manifest metadata other than explicitly deferred license/publication;
2. `publish = false` during private retention;
3. `cargo package --list`;
4. `cargo package`;
5. generated package manifest inspection;
6. package build with default/all relevant features;
7. package build with minimum/no-default features where supported;
8. offline package build;
9. rustdoc release-quality checks;
10. no VCS/build artifacts in the package;
11. no unresolved path-only or Git-only production dependency in the packaged
    registry manifest;
12. exact dependency provenance retained for the private candidate.

A crate with a private Perfect Git dependency must prove that the generated
package manifest carries the intended registry version dependency and does not
require the private Git URL for a future crates.io consumer.

## 4. Name readiness

Desired crates.io names should be checked periodically while development is
private. Name availability is a risk to track, not a reason to publish
unfinished placeholder crates by default.

Any deliberate name-reservation publication requires explicit owner approval.

## 5. Final open-release sequence

Public release happens only after the family is privately complete/qualified and
the owner authorizes opening it.

Order:

1. retain exact private 1.0-candidate revisions;
2. finish the family dependency DAG and qualification evidence;
3. select/finalize project licenses;
4. verify/claim required crates.io names;
5. enable and verify public security-reporting paths;
6. prepare repositories/packages for public visibility;
7. publish crates **bottom-up by production dependency DAG**;
8. after each publication, verify crates.io metadata and docs.rs;
9. update downstream release manifests to consume the released registry version;
10. publish the next dependent crate;
11. create exact Git tags/releases from qualified revisions;
12. run final public family qualification.

Implementation order is not publication order. Publication order is determined
by production dependencies.

## 6. Bottom-up publication rule

For a dependency chain such as:

`perfect-rational -> perfect-arithmetic -> perfect-numeric`

public registry order is:

1. `perfect-numeric`;
2. verify crates.io + docs.rs;
3. `perfect-arithmetic`;
4. verify crates.io + docs.rs;
5. `perfect-rational`.

The same rule applies recursively across the complete family DAG.

Perfect Qualification is infrastructure and is never a production dependency,
so it does not force a crates.io publication dependency.

## 7. Open-release gates that remain intentionally deferred

Until explicit authorization to go open, these may remain pending without
blocking private implementation, hardening, qualification, or private 1.0
candidate status:

- project license selection;
- removal of `publish = false`;
- public repository visibility;
- crates.io publication;
- docs.rs publication;
- public-facing vulnerability-reporting verification;
- public tags/releases.

They must all be resolved before the applicable public release is claimed.

## 8. Evidence rule

“crates.io-ready” means package mechanics and metadata are verified while
private. It does **not** mean published.

“published” means the exact qualified revision has passed the open-release gate
and the resulting crates.io/docs.rs artifacts have been verified.
