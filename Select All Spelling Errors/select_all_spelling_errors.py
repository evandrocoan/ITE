

#
# Select All Spelling Errors Command
#
# Select all mispelled words in Sublime Text at once
# http://superuser.com/questions/1052497/select-all-mispelled-words-in-sublime-text-at-once
#
# cProfile for Python does not recognize Function name
# http://stackoverflow.com/questions/8900899/cprofile-for-python-does-not-recognize-function-name
#

import sublime
import sublime_plugin

import cProfile


class SelectAllSpellingErrorsCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        cProfile.runctx( 'findRegions(self, edit)', globals(), locals() )

def findRegions(self, edit):

    regionsList = []

    while True:

        self.view.run_command('next_misspelling')

        if self.view.sel()[0] not in regionsList:

            regionsList.append( self.view.sel()[0] )

        else:

            break

    self.view.sel().clear()
    self.view.sel().add_all( regionsList )



