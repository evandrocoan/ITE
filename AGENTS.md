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

## Python runtime

- Python 3.3 compatibility is no longer required. Target Python 3.8 or newer for new code
  maintained by this project. Do not add compatibility branches solely for Python 3.3.
- Check a package's `.python-version` and the Sublime Text build before using Python features or
  Sublime APIs. Keep the runtime declaration aligned with code changes; the system Python used
  for local checks may differ from Sublime's embedded interpreter.
- Respect a vendored dependency's own compatibility contract when editing its source.

## Source and deployed packages

- Confirm which `Data` tree a running Sublime Text instance uses. The versioned source and a
  separate portable test installation may contain different copies of the same plugin.
- `Utilities/ConsoleCapture/` is the collector source. Its `README.md` describes how to build
  and install the archive under `Installed Packages/`. Editing or committing the source alone
  does not update an installed archive.
- When a fix depends on startup or plugin loading, verify it in the intended Sublime Text
  instance. The console collector records Python plugin output only after the collector loads.
