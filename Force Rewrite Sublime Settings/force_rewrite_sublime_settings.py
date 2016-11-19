
import sublime
import sublime_plugin


class ForceRewriteSublimeSettingsCommand( sublime_plugin.TextCommand ):

    def run( self, edit ):

        sublime.save_settings( 'Preferences.sublime-settings' )



class ForceReloadSublimeColorScheme( sublime_plugin.TextCommand ):

    def run( self, edit ):

        print( "\n" + self.view.window().active_view().settings().get("color_scheme") )
        self.view.window().active_view().settings().erase("color_scheme")



