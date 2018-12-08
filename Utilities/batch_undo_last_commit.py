#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import shlex
import subprocess

"""
Iterates through all subdirectories of the current directory where this script file is on, but do not
recurse into them. Then, replace the last commit message, if matches the defined pattern.
"""

from debug_tools import getLogger
log = getLogger( __name__ )

# current_directory = os.path.dirname( os.path.realpath(__file__) )
current_directory = os.path.join( os.path.dirname( os.path.dirname( os.path.realpath(__file__) ) ), "Packages" )
log( 1, 'directory walk %s', current_directory )

maximum_process_limit = 1000


def run_command(absolute_path, command_name):
    command = shlex.split( command_name )
    command_line_interface = subprocess.Popen( command, stdout=subprocess.PIPE, cwd=absolute_path )
    output = command_line_interface.communicate()[0]

    log( 1, "%s", output )
    # log( 1, "%s", output.decode('utf-8') )

    return output


def process_submodule(absolute_path):
    checkout_result = run_command( absolute_path, "git checkout master" )
    last_commit_message = run_command( absolute_path, "git log -1 --pretty=%B" )

    if last_commit_message == b'Created a .no-sublime-package for all packages, in attempt to fix\n\nevandrocoan/ITE 108 - Expand Region keybind is not working on stable version.\n\n':
        log( 1, "equals" )

        # https://stackoverflow.com/questions/19176359/how-to-get-the-last-commit-id-of-a-remote-repo-using-curl-like-command
        last_commit_id = run_command( absolute_path, "git rev-parse HEAD" )

        global maximum_process_limit
        maximum_process_limit -= 1

        run_command( absolute_path, 'git revert %s' % last_commit_id.decode("utf-8") )

    else:
        log( 1, "Not equals" )


def main():

    for directory_name in os.listdir( current_directory ):
        full_path = os.path.join( current_directory, directory_name )

        if os.path.isdir( full_path ):
            global maximum_process_limit
            log( 1, 'directory_name: %s', directory_name )

            if maximum_process_limit < 0:
                return

            process_submodule( full_path )


if __name__ == "__main__":
    main()
    # pass
    # process_submodule( "F:\\SublimeText\\Data\\Packages\\ConcurrentLogHandler" )
