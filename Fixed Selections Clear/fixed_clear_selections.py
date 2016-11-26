import sublime
import sublime_plugin


class FixedClearSelectionsCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        # print( 'Calling FixedClearSelections...' )
        self.view.sel().clear()


