
"""
This is designed to clear the mouse selections before close any opened panel when hitting the
`escape` key. Be sure there is not any key conflicts with this package `Default.sublime-keymap` file.

http://stackoverflow.com/questions/37904510/sublime-text-pressing-esc-from-multiple-selections-put-cursor-at-last-select
http://stackoverflow.com/questions/14963775/multiple-cursors-in-sublime-text-2-windows
https://www.sublimetext.com/docs/3/multiple_selection_with_the_keyboard.html
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


