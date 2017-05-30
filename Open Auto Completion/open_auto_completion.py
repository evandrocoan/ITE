


import sublime
import sublime_plugin


class OpenAutoCompletionCommand(sublime_plugin.TextCommand):
    """
        How to autocomplete inside a word?
        https://forum.sublimetext.com/t/how-to-autocomplete-inside-a-word/28646
    """

    def run(self, edit, **kargs):
        # print( "kargs: ", str( kargs ) )

        view = self.view
        view.run_command("insert", {"characters": kargs["keystroke"]})

        window = view.window()
        # window.run_command("auto_complete")


