


import sublime
import sublime_plugin


def plugin_loaded():

    # print( "( fix_project_switch_restart_bug.py )" )

    views   = None
    windows = sublime.windows()

    for window in windows:

        views = window.views()

        for view in views:

            # print( "( fix_project_switch_restart_bug.py ) View id {0}, buffer id {1}".format( view.id(), view.buffer_id() ) )
            restore_view( view )



def restore_view( view ):
    """
        view.set_viewport_position( , False )
    """

    # for selection in view.sel(): print( "( fix_project_switch_restart_bug.py ) Iterating view.sel()[i].begin() {0}".format( selection ) )

    # print( "( fix_project_switch_restart_bug.py ) Setting show_at_center to view id {0}".format( view.id() ) )
    view.show_at_center( view.sel()[0].begin() )



lastOnLoadViewCallTime = 0

def are_we_on_the_project_switch_process():
    """
        Call `plugin_loaded()` only one time, after the project switch process is finished.

        Restrictions:
        1. We cannot call `plugin_loaded()` if this function is called only one time.
        2. If this function is called consequently 2 times with less than 0.1 seconds, then we
           must to return True.
           Basically, on each call
    """

    # set task to call plugin_loaded() after 2 seconds, if this task currently does not exists.

    return False



class OnLoadedViewCommand( sublime_plugin.EventListener ):
    """
        This partially fix the issues:

        Restore session, does not set the last scroll position after a project change, or sublime restart #1379
        https://github.com/SublimeTextIssues/Core/issues/1379

        Scroll sync doesn't work (ST3 3084)
        https://github.com/titoBouzout/BufferScroll/issues/23

        Finish the package: Fix Project Switch-Restart Bug
        https://github.com/evandrocoan/SublimeTextStudio/issues/26
    """

    # def on_load( self, view ):
    def on_load_async( self, view ):
    # def on_activated( self, view ):
    # def on_activated_async( self, view ):

        # { "keys": ["up"], "command": "move", "args": {"by": "lines", "forward": false} },
        # { "keys": ["down"], "command": "move", "args": {"by": "lines", "forward": true} },
        # view.run_command( "move", {"by": "lines", "forward": False} )
        # view.run_command( "move", {"by": "lines", "forward": True} )
        #
        # print( "( fix_project_switch_restart_bug.py ) Calling restore_view, view id {0}".format( view.id() ) )

        # Need to fix to the bug on the Sublime Text core, where all cloned views are called with the same
        # view object. If we do not fix this here, it would set all the cloned views to the same
        # position. So to overcome this, we call all the views to center with `plugin_loaded()`.
        #
        # #1253 Event handlers for cloned views get called with the wrong view object
        # https://github.com/SublimeTextIssues/Core/issues/1253
        #
        # The `on_load_async()` is called for each view on for the project change, however
        # due the bug https://github.com/SublimeTextIssues/Core/issues/1253, the cloned
        # views are called with the wrong `view`, then we need to call `plugin_loaded()` to catch
        # all the correct views (including the cloned ones) to apply the scroll fix for the bug
        # https://github.com/SublimeTextIssues/Core/issues/1379.
        #
        if not are_we_on_the_project_switch_process():

            restore_view( view )





