


import sublime
import sublime_plugin


class OverwriteCommitCompletionCommand(sublime_plugin.TextCommand):
    """
        Complete whole word
        https://forum.sublimetext.com/t/complete-whole-word/26375

        It is possible to pass an array to a command without **kargs?
        https://forum.sublimetext.com/t/it-is-possible-to-pass-an-array-to-a-command-without-kargs/28969
    """

    def run(self, edit):
        view = self.view
        window = view.window()
        old_selections = []

        for selection in view.sel():
            old_selections.append( selection.end() )

        window.run_command( "commit_completion" )
        window.run_command( "overwrite_commit_completion_assistant", { "old_selections" : old_selections } )

class OverwriteCommitCompletionAssistantCommand( sublime_plugin.TextCommand ):
    """
        Save the edit when running a Sublime Text 3 plugin
        https://stackoverflow.com/questions/20466014/save-the-edit-when-running-a-sublime-text-3-plugin
    """

    def run( self, edit, old_selections ):
        """
            Since Sublime Text build ~3134, we need to wait until Sublime Text insert the completion.
        """
        view              = self.view
        selection_index   = 0
        completion_offset = 0

        for selection in view.sel():
            completion_end_point   = selection.end()
            duplicated_word_region = sublime.Region( completion_end_point, view.word( completion_end_point ).end() )
            duplicated_word        = view.substr( duplicated_word_region )
            part_completed_region  = sublime.Region( old_selections[ selection_index ] + completion_offset, completion_end_point )

            # print( "selection:           " + str( selection ) )
            # print( "selection_word:      " + str( view.substr( selection ) ) )
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

tooMuchLeft
tooMuchLeft
tooMuchLeft

"""
