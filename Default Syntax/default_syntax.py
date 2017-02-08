


import sublime
import sublime_plugin


class DefaultSyntaxCommand( sublime_plugin.EventListener ):

    def on_new( self, view ):

        settings = sublime.load_settings("Preferences.sublime-settings")
        view.set_syntax_file( settings.get('new_file_syntax') )




