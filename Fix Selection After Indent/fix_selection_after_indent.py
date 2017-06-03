

import sublime
import sublime_plugin


class IndentSelectWholeFirstLineEventListener(sublime_plugin.EventListener):
    """
        Sublime Text 3: Keep entire lines selected when indenting with tab
        https://stackoverflow.com/questions/24688117/sublime-text-3-keep-entire-lines-selected-when-indenting-with-tab/

        How to keep the first line indentation selected when indenting?
        https://forum.sublimetext.com/t/how-to-keep-the-first-line-indentation-selected-when-indenting/28741

        Keep the first line indentation selected when indenting text
        https://github.com/SublimeTextIssues/Core/issues/1746
    """

    def on_post_text_command(self, view, command_name, args):

        if command_name == 'indent':

            if all(not sel.empty() for sel in view.sel()):

                if all(view.line(sel.begin()) != view.line(sel.end()) for sel in view.sel()):
                    new_selections = []

                    for sel in view.sel():
                        new_selections.append(sel.cover(view.line(sel.begin())))

                    view.sel().clear()
                    view.sel().add_all(new_selections)



