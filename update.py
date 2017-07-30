# -*- coding: UTF-8 -*-
#
# This first line allow to use UTF-8 encoding on this file.
#
#

#
# Licensing
#
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the
#  Free Software Foundation; either version 3 of the License, or ( at
#  your option ) any later version.
#
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import sys
import unittest

sys.path.insert(0,'Packages/PythonDebugTools')
from debug_tools import log

log( 1, "Debugging" )
log( 1, "..." )
log( 1, "..." )

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
def main():
    log( 1, "Entering on main(0)" )
    create_backstroke_pulls()
    # unittest.main()


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

def create_backstroke_pulls():

    # Declare an array variable
    backstroke_request_list = \
    [
    "https://backstroke.us/",  # https://github.com/sublimehq/Packages
    "https://backstroke.us/",  # https://github.com/aziz/SublimeANSI
    "https://backstroke.us/",  # https://github.com/DavidGerva/AddFolderToProject-SublimePlugin
    "https://backstroke.us/",  # https://github.com/wadetb/Sublime-Text-Advanced-CSV
    "https://backstroke.us/",  # https://github.com/skuroda/Sublime-AdvancedNewFile/
    "https://backstroke.us/",  # https://github.com/randy3k/AlignTab
    "https://backstroke.us/",  # https://github.com/alienhard/SublimeAllAutocomplete
    "https://backstroke.us/",  # https://github.com/BoundInCode/AutoFileName
    "https://backstroke.us/",  # https://github.com/chipotle/BBCode
    "https://backstroke.us/",  # https://github.com/aponxi/sublime-better-coffeescript
    "https://backstroke.us/",  # https://github.com/titoBouzout/BufferScroll
    "https://backstroke.us/",  # https://github.com/wbond/ChannelRepositoryTools
    "https://backstroke.us/",  # https://github.com/Monnoroch/ColorHighlighter
    "https://backstroke.us/",  # https://github.com/facelessuser/ColorHelper
    "https://backstroke.us/",  # https://github.com/DougTy/sublime-compare-side-by-side
    "https://backstroke.us/",  # https://github.com/theskyliner/CopyFilepathWithLineNumbers
    "https://backstroke.us/",  # https://github.com/crash5/CopyWithLineNumbersReloaded
    "https://backstroke.us/",  # https://github.com/spadgos/sublime-jsdocs
    "https://backstroke.us/",  # https://github.com/facelessuser/ExportHtml
    "https://backstroke.us/",  # https://github.com/rajeshvaya/Sublime-Extended-Tab-Switcher
    "https://backstroke.us/",  # https://github.com/colinta/SublimeFileDiffs
    "https://backstroke.us/",  # https://github.com/math2001/FileManager
    "https://backstroke.us/",  # https://github.com/facelessuser/FuzzyFileNav
    "https://backstroke.us/",  # https://github.com/sagold/FuzzyFilePath
    "https://backstroke.us/",  # https://github.com/condemil/Gist
    "https://backstroke.us/",  # https://github.com/noahcoad/google-spell-check
    "https://backstroke.us/",  # https://github.com/shagabutdinov/sublime-goto-last-edit-enhanced
    "https://backstroke.us/",  # https://github.com/bblanchon/SublimeText-HighlightBuildErrors
    "https://backstroke.us/",  # https://github.com/xdrop/Hungry-Backspace
    "https://backstroke.us/",  # https://github.com/Epskampie/sublime_indent_and_braces
    "https://backstroke.us/",  # https://github.com/vontio/sublime-invert-selection
    "https://backstroke.us/",  # https://github.com/SublimeText/LaTeXTools
    "https://backstroke.us/",  # https://github.com/vishr/local-history
    "https://backstroke.us/",  # https://github.com/Kristinita/1Sasha1MarkdownNoBBCode
    "https://backstroke.us/",  # https://github.com/SublimeText/Origami
    "https://backstroke.us/",  # https://github.com/wbond/package_control
    "https://backstroke.us/",  # https://github.com/SublimeText/PackageDev
    "https://backstroke.us/",  # https://github.com/MaokaiLin/PowerCursors
    "https://backstroke.us/",  # https://github.com/reywood/sublime-project-specific-syntax
    "https://backstroke.us/",  # https://github.com/jgbishop/sxs-settings
    "https://backstroke.us/",  # https://github.com/SideBarEnhancements-org/SideBarEnhancements
    "https://backstroke.us/",  # https://github.com/SublimeCodeIntel/SublimeCodeIntel
    "https://backstroke.us/",  # https://github.com/wuub/SublimeREPL
    "https://backstroke.us/",  # https://github.com/evandrocoan/SyncedSideBar
    "https://backstroke.us/",  # https://github.com/randy3k/SyntaxManager
    "https://backstroke.us/",  # https://github.com/duydao/Text-Pastry
    "https://backstroke.us/",  # https://github.com/titoBouzout/Toolbar
    "https://backstroke.us/",  # https://github.com/jonlabelle/Trimmer
    "https://backstroke.us/",  # https://github.com/ehuss/Sublime-Wrap-Plus
    "https://backstroke.us/",  # https://github.com/Microsoft/TypeScript-Sublime-Plugin
    "https://backstroke.us/",  # https://github.com/dzhibas/SublimePrettyJson
    "https://backstroke.us/",  # https://github.com/SublimeText/VBScript
    "https://backstroke.us/",  # https://github.com/robertcollier4/REG
    "https://backstroke.us/"  # https://github.com/skozlovf/Sublime-GenericConfig
    ]

    # Now loop through the above array
    for current_url in backstroke_request_list:
        print( str( current_url ) )
        # curl -X POST current_url



# Here's our "unit".
def IsOdd(n):
    return n % 2 == 1

class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.failUnless(IsOdd(1))


if __name__ == "__main__":
    main()
