
"""
See/read the README.MD file.
"""


import sublime
import sublime_plugin


class SingleSelectionLastCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        # print( 'Calling Selection Last...' )
        last = self.view.sel()[-1]
        self.view.sel().clear()
        self.view.sel().add(last)
        self.view.show(last)



class SingleSelectionFirstCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        # print( 'Calling Selection First...' )
        first = self.view.sel()[0]
        self.view.sel().clear()
        self.view.sel().add(first)
        self.view.show(first)




