
import sublime
import sublime_plugin


class ForceRewriteSublimeSettingsCommand( sublime_plugin.TextCommand ):

    def run( self, edit ):

        sublime.save_settings( 'Preferences.sublime-settings' )



