
import sublime
import sublime_plugin


class CopyScopeToClipboardCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        syntax_name = self.view.scope_name(self.view.sel()[0].begin())
        print(syntax_name)
        sublime.set_clipboard(syntax_name)



class GetScopeAlwaysTextCommand( sublime_plugin.TextCommand ):
    """
    Use `view.window().run_command( "get_scope_always_text" )` on the Sublime Text Console, to get
    the current scople name. The package `ScopeAlways` and its command should be actiaved by
    `Toggle ScopeAlways` in order to this to work.
    """

    def run( self, edit ):

        # status = self.view.get_status( "scope_always" )
        status = sublime.active_window().active_view().get_status( "scope_always" )
        print( status )


