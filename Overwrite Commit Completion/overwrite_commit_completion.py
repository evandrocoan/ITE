


import sublime
import sublime_plugin


class OverwriteCommitCompletionCommand(sublime_plugin.TextCommand):
    """
        Complete whole word
        https://forum.sublimetext.com/t/complete-whole-word/26375
    """

    def run(self, edit):
        view = self.view
        window = view.window()
        window.run_command("commit_completion")

        for sel in view.sel():
            point = sel.b
            word = view.word(point)
            reg = sublime.Region(point, word.end())

            if view.substr(reg).isalnum():
                view.erase(edit, reg)


