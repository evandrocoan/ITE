
import sublime
import sublime_plugin


class ForceRewriteSublimeSettingsCommand( sublime_plugin.TextCommand ):

    def run( self, edit ):

        sublime.save_settings( 'Preferences.sublime-settings' )



class ForceReloadSublimeColorScheme( sublime_plugin.TextCommand ):

    def run( self, edit ):

        views   = None
        windows = sublime.windows()

        for window in windows:

            print( "\nWindow id: " + str( window.id() ) )
            views = window.views()

            for view in views:

                print( "\"" + "%-32s" % str( view.name() ) + "\": " + self.view.window().active_view().settings().get("color_scheme") )
                view.settings().erase("color_scheme")



