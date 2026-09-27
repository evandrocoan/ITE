# ITE project instructions

This directory is the Sublime Text `Data` tree and the parent Git repository for the ITE
package set. `README.md` covers user setup and operation; this file records agent-facing
constraints that span packages.

## Repository boundaries

- Use `.gitmodules` to identify submodule paths. Inspect the parent repository and the owning
  submodule before changing a package. Make code changes in the owning submodule; the parent
  repository records its commit through a gitlink.
- Preserve unrelated dirty submodules and runtime files. A commit in a submodule does not update
  the parent's gitlink by itself.
- Treat `Installed Packages/`, `Log/`, `Cache/`, and `Crash Reports/` as runtime locations. Inspect
  them when diagnosing failures, but do not treat their contents as the source for package fixes.

## Repository ownership

- Use `PACKAGE_OWNERSHIP.md` for the explicit list of Evandro-maintained packages and the
  `evandrocoan` packages that can receive upstream updates with focused review. Account ownership
  alone does not determine review effort; an upstream entry alone does not grant lighter review.
- Treat packages under `evandroforks` as light upstream forks by default. Follow the canonical
  repository destination when a URL in `.gitmodules` redirects to another account.
- For a light upstream fork, inspect the proposed update and its overlap with local customizations
  before accepting it. Review changes to locally maintained code or integration behavior in depth.

## Upstream updates and conflict resolution

- Apply the same review to every upstream update in this parent repository and its submodules,
  regardless of ownership, fork classification, or whether Git reports a conflict. Treat the local
  checkout as a maintained rewrite built from upstream code. Preserve its customizations and
  design; a clean automatic merge is not evidence that an upstream change fits the local code.

### Identify changes since the previous update

- In the owning repository, identify the verified upstream revision or snapshot used as the
  source for the previous update before claiming which upstream changes are newly published.
  Inspect the previous merge's upstream parent and history when available; that parent identifies
  a source tip, not which changes were accepted locally. In a single-head merge in progress,
  `HEAD` is the local pre-merge tip and `MERGE_HEAD` is the incoming tip; neither identifies the
  previous upstream source by itself. The merge base supports a three-way comparison but does
  not prove which upstream snapshot was used in the previous update.
- Compare that verified prior upstream source with the incoming upstream state to find candidate
  newly published changes. Use a commit range only after verifying that the prior upstream commit
  is an ancestor of the incoming tip; otherwise compare verified snapshots. Compare the local
  rewrite with the common ancestor separately where that ancestry exists. Account individually
  for changes previously applied, adapted, skipped, or partially applied so they are not called
  new. Copied or selective updates and rewritten history may leave no reliable single prior
  snapshot. If the source or per-change provenance cannot be verified, explain the uncertainty
  and consult the user before calling a change new or deciding to apply or skip it.
- For every affected file and behavior, identify what upstream actually changed, why it changed,
  and its effect before deciding whether it applies locally. Use upstream history, tests, and code
  context as evidence; label inferred or unknown rationale. Do not mistake existing upstream code
  for a new correction. Verify Git's rename matches against each file's platform and role before
  relying on them; similar content can pair unrelated files.

### Adapt changes to the local rewrite

- When an upstream change applies, adapt its intended behavior to the local implementation with
  the smallest equivalent change, rather than replacing the local rewrite. Review the resulting
  behavior even in files Git merged automatically; do not silently discard an upstream change.
- If the upstream reason cannot be established, the equivalent local change is unclear or cannot
  be applied, or the change conflicts with the local design, explain the observed upstream change,
  the available rationale, and the trade-offs to the user. Consult the user before applying,
  skipping, or replacing that part of the local implementation.

### Preserve merge direction in history

- For an upstream merge in this repository or any submodule, create a temporary local branch at
  the incoming upstream tip without tracking the remote branch. Merge the local branch into that
  temporary branch with an explicit merge commit: its first parent must be upstream and its second
  parent the local branch. Resolve conflicts there while preserving the local rewrite and
  reviewing upstream behavior as above.
- Return to the local branch and merge the temporary branch with another explicit merge commit:
  its first parent must be the previous local tip and its second parent the temporary merge. Check
  the first merge's first-parent diff for the project's changes applied to upstream, and the
  second merge's first-parent diff for upstream changes applied to the local branch. Verify both
  parent orders and check each merge's first-parent diff with `git diff --check`; inspect
  conflict-resolved files for mixed line endings. Remove the temporary branch only after both
  merges and their results are verified. Do not mutate the upstream remote or push unless
  separately requested.

## Python runtime

- Python 3.3 compatibility is no longer required. Target Python 3.8 or newer for new code
  maintained by this project. Do not add compatibility branches solely for Python 3.3.
- Check a package's `.python-version` and the Sublime Text build before using Python features or
  Sublime APIs. Keep the runtime declaration aligned with code changes; the system Python used
  for local checks may differ from Sublime's embedded interpreter.
- During upstream merges, retain the upstream `.python-version` unless actual runtime behavior
  proves it incompatible. Sublime may run a declared Python version through a compatible plugin
  host even when there is no executable with that exact version in its name. Verify which host
  loads the package in the intended editor before changing the declaration or adapting code for
  a different runtime.
- Respect a vendored dependency's own compatibility contract when editing its source.
- Before updating a dependency managed by `Packages/PackagesManager`, verify its supported Python
  versions and installation layout against the loader and its consumers. Coordinate any layout
  change with the loader or installer, then check affected imports after a fresh Sublime startup.

## Source and deployed packages

- Confirm which `Data` tree a running Sublime Text instance uses. The versioned source and a
  separate portable test installation may contain different copies of the same plugin.
- `Utilities/ConsoleCapture/` is the collector source. Its `README.md` describes how to build
  and install the archive under `Installed Packages/`. Editing or committing the source alone
  does not update an installed archive.
- When a fix depends on startup or plugin loading, verify it in the intended Sublime Text
  instance. The console collector records Python plugin output only after the collector loads.
- During a merge, plugin errors from intermediate checkouts do not establish the final result.
  Once the final tree is in place, record the current console log position, explicitly reload the
  affected package, exercise a representative command, and inspect only the subsequent output.
  A successful command-line exit or a silent log does not by itself prove that the command ran.
- In PowerShell, keep JSON quotes intact when passing arguments to `subl --command` as one native
  argument. Verify the received argument if a command produces no observable result.
