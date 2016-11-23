


import sublime
import sublime_plugin


def plugin_loaded():

    views   = None
    windows = sublime.windows()

    for window in windows:

        views = window.views()

        for view in views:

            print( "( plugin_loaded ) Callling on_activated, view id {0}".format( view.id() ) )
            view.run_command( "move", {"by": "lines", "forward": False} )
            view.run_command( "move", {"by": "lines", "forward": True} )


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

    def on_load( self, view ):
    # def on_load_async( self, view ):
    # def on_activated( self, view ):
    # def on_activated_async( self, view ):

        # print( "( OnLoadedViewCommand ) Callling on_activated, view id {0}".format( view.id() ) )
        # { "keys": ["up"], "command": "move", "args": {"by": "lines", "forward": false} },
        # { "keys": ["down"], "command": "move", "args": {"by": "lines", "forward": true} },
        view.run_command( "move", {"by": "lines", "forward": False} )
        view.run_command( "move", {"by": "lines", "forward": True} )



