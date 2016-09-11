

import sublime
import sublime_plugin

class DefaultSyntaxCommand(sublime_plugin.EventListener):
	def on_new(self, view):
		view.set_syntax_file("Packages/C++/C++.tmLanguage")


class ForceReloadSublimeSettingsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sublime.save_settings('Preferences.sublime-settings')

