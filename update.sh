#!/bin/bash

##
## Usage:
##   make <target>
##
## Targets:
##   all              generate all assets
##
##   forks            check all forks not supported by `backstroke` against their upstream
##   backstroke       check all backstroke registered repositories updates with their upstream
##   update           perform a git pull from the remote repositories
##

main()
{
    create_backstroke_pulls
    return 0
}

#
# Repositories which are a fork from outside the Github, which need manually checking.
#
# https://github.com/sublimehq/Packages
# https://github.com/evandrocoan/SublimeAMXX_Editor
# https://github.com/evandrocoan/SublimePreferencesEditor

#
# My repositories, which are not fork. So no need to update with the upstream.
#
# https://github.com/evandrocoan/.versioning
# https://github.com/evandrocoan/SublimeActiveViewJumpBack
# https://github.com/evandrocoan/SublimeAmxxPawn
# https://github.com/evandrocoan/ClearCursorsCarets
# https://github.com/evandrocoan/SublimeClipboardScopeCopy
# https://github.com/evandrocoan/SublimeDefaultSyntax
# https://github.com/evandrocoan/SublimeFixProjectSwitchRestartBug
# https://github.com/evandrocoan/SublimeFixSelectionAfterIndent
# https://github.com/evandrocoan/SublimeFixedSelectionsClear
# https://github.com/evandrocoan/SublimeForceRewriteSublimeSettings
# https://github.com/evandrocoan/SublimeNotepadPlusPlusTheme
# https://github.com/evandrocoan/SublimeOctave
# https://github.com/evandrocoan/SublimeOpenAutoCompletion
# https://github.com/evandrocoan/SublimeUnpackedPackagesOverride
# https://github.com/evandrocoan/SublimeOverwriteCommitCompletion
# https://github.com/evandrocoan/SublimeRichPlainText
# https://github.com/evandrocoan/SublimeSQLKeywordUppercase
# https://github.com/evandrocoan/SublimeSelectAllSpellingErrors
# https://github.com/evandrocoan/SublimeTextStudioChannel
# https://github.com/evandrocoan/SublimeUncrustify
# https://github.com/evandrocoan/SublimeMultilingualDictionary

#
# My forks upstreams
#

create_backstroke_pulls()
{
    # Declare an array variable.
    # You can access them using echo "${arr[0]}", "${arr[1]}"
    declare -a backstroke_request_list=(
    "https://backstroke.us/"  # https://github.com/sublimehq/Packages
    "https://backstroke.us/"  # https://github.com/aziz/SublimeANSI
    "https://backstroke.us/"  # https://github.com/DavidGerva/AddFolderToProject-SublimePlugin
    "https://backstroke.us/"  # https://github.com/wadetb/Sublime-Text-Advanced-CSV
    "https://backstroke.us/"  # https://github.com/skuroda/Sublime-AdvancedNewFile/
    "https://backstroke.us/"  # https://github.com/randy3k/AlignTab
    "https://backstroke.us/"  # https://github.com/alienhard/SublimeAllAutocomplete
    "https://backstroke.us/"  # https://github.com/BoundInCode/AutoFileName
    "https://backstroke.us/"  # https://github.com/chipotle/BBCode
    "https://backstroke.us/"  # https://github.com/aponxi/sublime-better-coffeescript
    "https://backstroke.us/"  # https://github.com/titoBouzout/BufferScroll
    "https://backstroke.us/"  # https://github.com/wbond/ChannelRepositoryTools
    "https://backstroke.us/"  # https://github.com/Monnoroch/ColorHighlighter
    "https://backstroke.us/"  # https://github.com/facelessuser/ColorHelper
    "https://backstroke.us/"  # https://github.com/DougTy/sublime-compare-side-by-side
    "https://backstroke.us/"  # https://github.com/theskyliner/CopyFilepathWithLineNumbers
    "https://backstroke.us/"  # https://github.com/crash5/CopyWithLineNumbersReloaded
    "https://backstroke.us/"  # https://github.com/spadgos/sublime-jsdocs
    "https://backstroke.us/"  # https://github.com/facelessuser/ExportHtml
    "https://backstroke.us/"  # https://github.com/rajeshvaya/Sublime-Extended-Tab-Switcher
    "https://backstroke.us/"  # https://github.com/colinta/SublimeFileDiffs
    "https://backstroke.us/"  # https://github.com/math2001/FileManager
    "https://backstroke.us/"  # https://github.com/facelessuser/FuzzyFileNav
    "https://backstroke.us/"  # https://github.com/sagold/FuzzyFilePath
    "https://backstroke.us/"  # https://github.com/condemil/Gist
    "https://backstroke.us/"  # https://github.com/noahcoad/google-spell-check
    "https://backstroke.us/"  # https://github.com/shagabutdinov/sublime-goto-last-edit-enhanced
    "https://backstroke.us/"  # https://github.com/bblanchon/SublimeText-HighlightBuildErrors
    "https://backstroke.us/"  # https://github.com/xdrop/Hungry-Backspace
    "https://backstroke.us/"  # https://github.com/Epskampie/sublime_indent_and_braces
    "https://backstroke.us/"  # https://github.com/vontio/sublime-invert-selection
    "https://backstroke.us/"  # https://github.com/SublimeText/LaTeXTools
    "https://backstroke.us/"  # https://github.com/vishr/local-history
    "https://backstroke.us/"  # https://github.com/Kristinita/1Sasha1MarkdownNoBBCode
    "https://backstroke.us/"  # https://github.com/SublimeText/Origami
    "https://backstroke.us/"  # https://github.com/wbond/package_control
    "https://backstroke.us/"  # https://github.com/SublimeText/PackageDev
    "https://backstroke.us/"  # https://github.com/MaokaiLin/PowerCursors
    "https://backstroke.us/"  # https://github.com/reywood/sublime-project-specific-syntax
    "https://backstroke.us/"  # https://github.com/jgbishop/sxs-settings
    "https://backstroke.us/"  # https://github.com/SideBarEnhancements-org/SideBarEnhancements
    "https://backstroke.us/"  # https://github.com/SublimeCodeIntel/SublimeCodeIntel
    "https://backstroke.us/"  # https://github.com/wuub/SublimeREPL
    "https://backstroke.us/"  # https://github.com/evandrocoan/SyncedSideBar
    "https://backstroke.us/"  # https://github.com/randy3k/SyntaxManager
    "https://backstroke.us/"  # https://github.com/duydao/Text-Pastry
    "https://backstroke.us/"  # https://github.com/titoBouzout/Toolbar
    "https://backstroke.us/"  # https://github.com/jonlabelle/Trimmer
    "https://backstroke.us/"  # https://github.com/ehuss/Sublime-Wrap-Plus
    "https://backstroke.us/"  # https://github.com/Microsoft/TypeScript-Sublime-Plugin
    "https://backstroke.us/"  # https://github.com/dzhibas/SublimePrettyJson
    "https://backstroke.us/"  # https://github.com/SublimeText/VBScript
    "https://backstroke.us/"  # https://github.com/robertcollier4/REG
    "https://backstroke.us/"  # https://github.com/skozlovf/Sublime-GenericConfig
    )

    # Now loop through the above array
    for current_url in "${backstroke_request_list[@]}"
    do
        echo $current_url
        # curl -X POST $current_url
    done

    return 0
}








# Forward declarations in bash?
# https://stackoverflow.com/questions/13588457/forward-declarations-in-bash
main "$@"
exit $?

