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

current_directory = os.path.dirname( os.path.realpath(__file__) )
# current_directory = os.path.join( current_directory, '..', 'Packages' )

log( 1, 'directory walk %s', current_directory )
maximum_process_limit = 1000


def run_command(absolute_path, command_name):
    log( 1, "Running", command_name, absolute_path )
    command = shlex.split( command_name )

    command_line_interface = subprocess.Popen( command, stdout=subprocess.PIPE, cwd=absolute_path )
    output = command_line_interface.communicate()[0]

    # log( 1, "%s", output.decode('utf-8') )
    log( 1, "%s", output )

    if command_line_interface.returncode != 0:
        raise RuntimeError( "A process exited with error!" )
    return output


def process_submodule(absolute_path):
    output = run_command( absolute_path, "git log -1 --pretty=%B" )

    # https://stackoverflow.com/questions/17683458/how-do-i-commit-case-sensitive-only-filename-changes-in-git
    # run_command( absolute_path, 'git config core.ignorecase false' )
    return

    if output == b'Normalized the README.md with case-sensitive name\n\n':
        log( 1, "equals" )
        global maximum_process_limit
        maximum_process_limit -= 1

        # run_command( absolute_path, 'git reset --soft HEAD^ --' )
        # run_command( absolute_path, 'git commit --amend --no-edit' )
        # run_command( absolute_path, 'git push --force-with-lease --tags origin master' )
        run_command( absolute_path, "git commit --amend -m '%s'" %
            "Normalized the README.md with case-sensitive name\n\n" )

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

