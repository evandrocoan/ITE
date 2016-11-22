


import sublime
import sublime_plugin


class OnLoadedViewCommand( sublime_plugin.EventListener ):
    """
        This partially fix the issues:

        Restore session, does not set the last scroll position after a project change, or sublime restart #1379
        https://github.com/SublimeTextIssues/Core/issues/1379

        Scroll sync doesn't work (ST3 3084)
        https://github.com/titoBouzout/BufferScroll/issues/23

        To accomplish it, it move the caret up and down, this way it forces the scroll view to be switched.
        This causes the undesired behavior when switching views after the file being loaded or the
        project being restored.

        To fix this problems, just on to perform those operations when the file is loaded for the first time.
        This is a problem when Sublime Text just starts because this package is not loaded yet. This way
        we need to perform this action at the first time the file is chose/switched to.
    """

    # def on_load( self, view ):
    # def on_load_async( self, view ):
    def on_activated( self, view ):
    # def on_activated_async( self, view ):

        # print( "( OnLoadedViewCommand ) Callling on_activated" )
        # { "keys": ["up"], "command": "move", "args": {"by": "lines", "forward": false} },
        # { "keys": ["down"], "command": "move", "args": {"by": "lines", "forward": true} },
        view.run_command( "move", {"by": "lines", "forward": False} )
        view.run_command( "move", {"by": "lines", "forward": True} )



