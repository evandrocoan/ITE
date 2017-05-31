


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
        old_selections = []

        for selection in view.sel():
            old_selections.append( selection.end() )

        selection_index = 0
        completion_offset = 0
        window.run_command( "commit_completion" )

        for selection in view.sel():
            completion_end_point   = selection.end()
            duplicated_word_region = sublime.Region( completion_end_point, view.word( completion_end_point ).end() )
            duplicated_word        = view.substr( duplicated_word_region )
            part_completed_region  = sublime.Region( old_selections[ selection_index ] + completion_offset, completion_end_point )

            # print( "selection:           " + str( selection ) )
            # print( "inserted_word:       " + view.substr( sublime.Region( view.word( completion_end_point ).begin(), completion_end_point ) ) )
            # print( "full_completed_word: " + view.substr( view.word( completion_end_point ) ) )
            # print( "duplicated_word:     " + duplicated_word )
            # print( "part_completed_word: " + view.substr( part_completed_region ) )

            # inserted_word:       OverwriteCommitCompletionCommand
            # full_completed_word: OverwriteCommitCompletionCommandCommand
            # duplicated_word:     Command
            # part_completed_word: ompletionCommand
            if duplicated_word.isalnum() \
                    and duplicated_word in view.substr( part_completed_region ):

                # print( "Erasing duplication: " + duplicated_word )
                view.erase( edit, duplicated_word_region )

                # When the completion is inserted we need to save the completion_offset to be able
                # correct the outdated selection points after the auto completion for the remaining
                # selections
                completion_offset += part_completed_region.size() - duplicated_word_region.size()

            selection_index += 1


""" OverwriteCommitCompletionCommand

OverwriteCommitCompletionCommand
OverwriteCommitCompletionCommand

"""
