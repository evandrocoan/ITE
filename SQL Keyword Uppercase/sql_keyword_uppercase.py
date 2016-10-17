"""
Automatically set all SQL keywords to upper case after the space keystroke.
Originally created by `kingkeith` on `https://forum.sublimetext.com/t/automatically-set-sql-keywords-to-upper-case/23760`.

Change log:

1.1 - Added multiple scopes support for the SQL's `support` scope on the `sublime.keymap` file.
1.0 - Initial release by `kingkeith`.
"""

import sublime
import sublime_plugin


class UpperCasePreviousItemAndInsertSpaceCommand( sublime_plugin.TextCommand ):
    """
    Called each time the space is pressed to process the preceding keyword.
    Set the space key bind to:

    { "keys": [" "], "command": "upper_case_previous_item_and_insert_space",
        "context":
        [
            { "key": "selector", "operator": "equal", "operand": "source.sql", "match_all": true },
            { "key": "selection_empty", "operator": "equal", "operand": true, "match_all": true },
            { "key": "scope_before_cursor", "operator": "equal", "operand": ["keyword", "support"], "match_all": true },
        ]
    },

    This class extends the `sublime_plugin.TextCommand` class.
    """

    def run( self, edit ):

        # can't use `view.sel()[:]` because it gives an error `TypeError: an integer is required`
        selections   = [ cursor for cursor in self.view.sel() ]
        to_uppercase = []

        for sel in selections:

            if sel.end() > 0:
                if self.view.substr( sel.end() - 1 ) == '(':
                    offset = 2
                else:
                    offset = 1

                #prev_item = self.view.extract_scope( sel.end() - offset )
                scope = self.view.scope_name( sel.end() - offset )
                begin = sel.end() - offset

                while self.view.scope_name( begin ) == scope and begin > 0:
                    begin -= 1

                prev_item = sublime.Region( begin, sel.end() )
                to_uppercase.append( prev_item )

        self.view.sel().clear()
        self.view.sel().add_all( to_uppercase )
        self.view.run_command( 'upper_case' )

        self.view.sel().clear()
        self.view.sel().add_all( selections )
        self.view.run_command( 'insert', { 'characters': ' ' } )


class ScopeBeforeCursorEventListener( sublime_plugin.EventListener ):
    """
    Event listener used on the key binding `scope_before_cursor` available on the class's
    `UpperCasePreviousItemAndInsertSpaceCommand` documentation.
    """

    def on_query_context( self, view, key, operator, operand, match_all ):

        if key != 'scope_before_cursor':
            return None

        if operator not in ( sublime.OP_EQUAL, sublime.OP_NOT_EQUAL ):
            return None

        match = False

        for sel in view.sel():
            #print( max( 0, sel.end() - 1 ) )

            if view.substr( sel.end() - 1 ) == '(':
                offset = 2
            else:
                offset = 1

            for op in operand:
                match = view.match_selector( max( 0, sel.end() - offset ), op )
                #print( 'On 1º match: ', match )
                
                if match:
                    break

            if operator == sublime.OP_NOT_EQUAL:
                match = not match

            if match != match_all:
                break

        #print( 'match: ', match )
        return match



