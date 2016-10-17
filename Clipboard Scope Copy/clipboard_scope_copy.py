import sublime
import sublime_plugin


class CopyScopeToClipboardCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    syntax_name = self.view.scope_name(self.view.sel()[0].begin())
    print(syntax_name)
    self.view.set_status("Scope",syntax_name)
    sublime.set_clipboard(syntax_name)



