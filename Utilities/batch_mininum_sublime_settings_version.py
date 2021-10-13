#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import os
import shlex
import subprocess

"""
Iterates through all subdirectories of the current directory where this script file is on, but do not
recurse into them.

Creates a `settings.json` inside each directory with a specific Sublime Text version.
This is used when updating a major Sublime Text version for ChannelManager settings.json feature
control. See its README.md documentation for details.
"""

from debug_tools import getLogger
from debug_tools.third_part import load_data_file
from debug_tools.third_part import write_data_file

log = getLogger( __name__ )

# current_directory = os.path.dirname( os.path.realpath(__file__) )
current_directory = os.path.join( os.path.dirname( os.path.dirname( os.path.realpath(__file__) ) ), "Packages" )
log( 1, 'directory walk %s', current_directory )

minimum_sublime_text_version = "3999"

maximum_process_limit = 1000


def run_command(command_name, absolute_path):
    command = shlex.split( command_name )
    command_line_interface = subprocess.Popen( command, stdout=subprocess.PIPE, cwd=absolute_path )
    output = command_line_interface.communicate()[0]

    log( 1, "%s <%s> %s", command_name, absolute_path, output )
    # log( 1, "%s", output.decode('utf-8') )

    return output.decode('utf-8', errors='ignore'), command_line_interface


def process_submodule(absolute_path):
    checkout_result, _ = run_command( "git checkout master", absolute_path )

    version_settings_file = {}
    repository_settings_path = os.path.join( absolute_path, 'settings.json' )

    if os.path.exists( repository_settings_path ):
        try:
            version_settings_file = load_data_file( repository_settings_path )

        except Exception:
            log(1, "ERROR\n" * 8)
            log.exception( "Could not process: %s", repository_settings_path )

    if 'tags' not in version_settings_file:
        version_settings_file['tags'] = []

    if minimum_sublime_text_version not in version_settings_file['tags']:
        version_settings_file['tags'].append( minimum_sublime_text_version )
        write_data_file(repository_settings_path, version_settings_file)
    else:
        log(1, "Is already updated with %s<%s>", minimum_sublime_text_version, absolute_path)

    output, _ = run_command( "git tag -l %s" % ( minimum_sublime_text_version ), absolute_path )
    if output.strip() == minimum_sublime_text_version:
        log(1, "WARNING\n" * 8)
        log(1, "Git tag %s already exists for %s", minimum_sublime_text_version, absolute_path )

    else:
        output, proc = run_command( "git tag %s" % ( minimum_sublime_text_version ), absolute_path )

        if proc.returncode != 0:
            log(1, "WARNING\n" * 8)
            log(1, "Could not create git tag for %s<%s>", minimum_sublime_text_version, absolute_path)
        else:
            log( 1, 'Created git tag `%s`:\n%s', minimum_sublime_text_version, output )

        output, proc = run_command( "git push origin %s" % ( minimum_sublime_text_version ), absolute_path )
        if proc.returncode != 0:
            log(1, "WARNING\n" * 8)
            log(1, "Could not push the git tag to the remote for %s<%s>", minimum_sublime_text_version, absolute_path)
        else:
            log( 1, 'Pushed git tag for `%s`:\n%s', minimum_sublime_text_version, output )

    global maximum_process_limit
    maximum_process_limit -= 1


def main():

    for directory_name in os.listdir( current_directory ):
        full_path = os.path.join( current_directory, directory_name )

        if os.path.isdir( full_path ):
            global maximum_process_limit
            log( 1, 'directory_name: %s', directory_name )

            if directory_name == '.git':
                log(1, 'skipping git dir %s', full_path)
                continue

            if not os.path.exists(os.path.join( full_path, '.git' )):
                log(1, "Skipping, %s is not a git repository", full_path)
                continue

            if maximum_process_limit < 0:
                return

            process_submodule( full_path )


if __name__ == "__main__":
    main()
    # pass
    # process_submodule( "F:\\SublimeText\\Data\\Packages\\concurrentloghandler" )
