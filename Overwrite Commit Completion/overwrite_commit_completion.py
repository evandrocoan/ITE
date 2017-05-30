


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
        window.run_command( "commit_completion" )

        for sel in view.sel():
            completion_end_point   = sel.b
            sublime_completed_word = view.word( completion_end_point )
            duplicated_word_region = sublime.Region( completion_end_point, sublime_completed_word.end() )

            # print( "completion_end_point:   " + str( completion_end_point ) )
            # print( "sublime_completed_word: " + view.substr( sublime_completed_word ) )
            # print( "duplicated_word_region: " + view.substr( duplicated_word_region ) )

            if view.substr( duplicated_word_region ).isalnum():
                # print( "Erasing duplicated word: " + view.substr( duplicated_word_region ) )
                view.erase( edit, duplicated_word_region )

""" OverwriteCommitCompletionCommand

OverwriteCommitCompletionCommand
OverwriteCommitCompletionCommand

"""
