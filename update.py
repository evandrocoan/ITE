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

    # https://github.com/sublimehq/Packages
    # "https://backstroke.us/",

    # unittest.main()


#
# Repositories which are a fork from outside the Github, which need manually checking.
#
# https://github.com/sublimehq/Packages
# https://github.com/evandrocoan/SublimeAMXX_Editor
# https://github.com/evandrocoan/SublimePreferencesEditor


#
# My forks upstreams
#

def create_backstroke_pulls():

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
