

import sublime
import sublime_plugin

class DefaultSyntaxCommand(sublime_plugin.EventListener):
	def on_new(self, view):
		view.set_syntax_file("Packages/C++/C++.tmLanguage")



