# Package ownership and upstream review

The paths below are the explicit classification for this checkout. `.gitmodules` defines the
submodule paths and declared upstreams. A repository under `evandrocoan` is generally Evandro's
project even when it started as a fork, has an upstream, or contains only a small change from him.
The review category describes how closely an upstream update needs to be checked; it does not
change ownership or authorize merging a proposed update without inspecting it.

## Evandro-maintained packages

Review upstream updates to these packages in depth. They contain local code changes, substantial
adaptations, or no sufficiently verified upstream relationship for lighter review.

- `Packages/AllAutocomplete`
- `Packages/AmxxChannel`
- `Packages/AmxxEditor`
- `Packages/AmxxPawn`
- `Packages/AutoFileName`
- `Packages/AutoRefresh`
- `Packages/BufferScroll`
- `Packages/BuildView`
- `Packages/CaseConversion`
- `Packages/channelmanager`
- `Packages/ClearCursorsCarets`
- `Packages/ClipboardScopeCopy`
- `Packages/debugtools`
- `Packages/Default`
- `Packages/DefaultSyntax`
- `Packages/ExtendedTabSwitcher`
- `Packages/FixedToggleFindPanel`
- `Packages/FixProjectSwitchRestartBug`
- `Packages/FixSelectionAfterIndent`
- `Packages/ForceRewriteSublimeSettings`
- `Packages/HighlightWords`
- `Packages/HighlightWordsOnSelection`
- `Packages/KeepPastedTextSelected`
- `Packages/Language - English and Portuguese`
- `Packages/LSP`
- `Packages/MarkdownToBBCode`
- `Packages/MaxPane`
- `Packages/Notepad++ Color Scheme`
- `Packages/Octave`
- `Packages/OpenAutoCompletion`
- `Packages/OverrideCommitCompletion`
- `Packages/OverrideEditSettingsDefaultContents`
- `Packages/OverrideUnpackedPackages`
- `Packages/PackagesManager`
- `Packages/plantumlconnection`
- `Packages/PlantUmlDiagrams`
- `Packages/pushdownparser`
- `Packages/QuickSettings`
- `Packages/RememberCommandPaletteInput`
- `Packages/RemoveNonAsciiChars`
- `Packages/RichPlainText`
- `Packages/SelectAllSpellingErrors`
- `Packages/SkipCloseForClonedViews`
- `Packages/SQLKeywordUppercase`
- `Packages/StudioChannel`
- `Packages/TestPlier`
- `Packages/ToggleSettingsInBatch`
- `Packages/UnitTesting`
- `Packages/User`
- `Packages/ViewSettingsFreely`
- `Packages/WordingStatus`
- `Packages/WrapPlus`

The non-package submodules `.versioning` and `githubpullrequests` are also Evandro-maintained.

## Light upstream forks under `evandrocoan`

- `Packages/BBCode`
- `Packages/PushdownParserSyntax`

Their current differences from their upstreams do not modify upstream code files. An upstream
sync can receive focused review when the proposed changes do not overlap local customizations.
Check the actual diff, conflicts, and package integration for every update. Use in-depth review
if the update touches locally maintained code or changes package behavior materially.

## Other forks and maintenance

Treat packages whose canonical repository is under `evandroforks` as light upstream forks by
default. `Packages/sublime_lib` belongs here: its `evandrocoan` URL in `.gitmodules` currently
redirects to `evandroforks`.

When adding a package or changing its repository ownership, compare its current upstream with
local changes and update this classification. A declared upstream or a GitHub fork label alone
does not establish the review category.
