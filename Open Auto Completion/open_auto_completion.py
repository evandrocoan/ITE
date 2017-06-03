


import sublime
import sublime_plugin


class OpenAutoCompletionCommand(sublime_plugin.TextCommand):
    """
        How to autocomplete inside a word?
        https://forum.sublimetext.com/t/how-to-autocomplete-inside-a-word/28646

        Run command on space
        https://forum.sublimetext.com/t/run-command-on-space/28198

        Is it possible to detect if panels are visible AND have focus?
        https://forum.sublimetext.com/t/solved-is-it-possible-to-detect-if-panels-are-visible-and-have-focus/18507
    """

    def run(self, edit, **kargs):
        # print( "kargs: ", str( kargs ) )

        view = self.view
        view.run_command("insert", {"characters": kargs["keystroke"]})

        if not view.settings().get('is_widget'):
            window = view.window()
            window.run_command("auto_complete", {'disable_auto_insert': True, 'next_completion_if_showing': False})


