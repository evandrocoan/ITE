

import sublime
import sublime_plugin
import os


class MyJumpBackCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        # print( 'Calling MyJumpBackCommand...' )
        view = sublime.active_window().active_view()
        view.run_command("jump_back")



class MyJumpForwardCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        # print( 'Calling MyJumpBackCommand...' )
        view = sublime.active_window().active_view()
        view.run_command("jump_forward")



