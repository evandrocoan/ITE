#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import shlex
import json
import subprocess
import shutil

from debug_tools.estimated_time_left import sequence_timer
from debug_tools.estimated_time_left import progress_info

"""
Iterates through all repositories from a user and enable the issue tracker.
"""

from debug_tools import getLogger
log = getLogger( __name__ )

current_directory = os.path.dirname( os.path.realpath(__file__) )
# current_directory = os.path.join( current_directory, '..', 'Packages' )
log( 1, 'directory walk %s', current_directory )

# The maximum count of repositories to to process when calling this batch script.
maximum_process_limit = 1000

# GitHub token with full repository access
# https://github.com/settings/tokens
token = "8217398127859182039802175098213389019766"
user_name = "username"


def run_command(absolute_path, command_name):
    command = shlex.split( command_name )
    log( 1, 'command: %s', command )

    command_line_interface = subprocess.Popen( command, stdout=subprocess.PIPE, cwd=absolute_path )
    output = command_line_interface.communicate()[0]

    # log( 1, "%s", output )
    # log( 1, "\n%s", output.decode('utf-8') )
    return output


def main():
    page_index = 1

    while process_repositories_page( page_index ):
        page_index += 1


def process_repositories_page(page_index):
    global maximum_process_limit

    # https://stackoverflow.com/questions/27331849/github-api-v3-doesnt-show-all-user-repositories
    items_per_page = 100

    # https://stackoverflow.com/questions/8713596/how-to-retrieve-the-list-of-all-github-repositories-of-a-person
    repositories_text = run_command( current_directory,
            "curl -H '%s' https://api.github.com/users/%s/repos?per_page=%s&page=%s" % ( token, user_name, items_per_page, page_index ) )

    repositories_json = json.loads( repositories_text.decode('utf-8') )

    for repository_data, pi in sequence_timer( repositories_json, info_frequency=0 ):
        progress = progress_info( pi )
        log( 1, '' )
        log( 1, '' )
        log( 1, '' )
        log( 1, '' )
        log( 1, "{:s} Processing {:3d} of {:d} repositories... {:s}".format( progress, pi.index + 1, pi.count, repository_data['full_name'] ) )

        if maximum_process_limit <= 0: return
        maximum_process_limit -= 1

        full_command = \
        r"""
            curl
                -H "Authorization: Token {token}"
                -H "Content-Type: application/json"
                -H "Accept: application/json"
                -X PATCH
                --data '{data}'
                https://api.github.com/repos/{full_name}
        """.format(
                token=token,
                data=json.dumps(
                    {
                        "name": repository_data['name'],
                        "has_issues": True
                    }
                ),
                full_name=repository_data['full_name']
            )
        log( 1, 'full_command: %s' % full_command )

        result = run_command( current_directory, full_command )
        log( 1, 'result: %s' % result.decode('utf-8') )

    return len( repositories_json ) == items_per_page


if __name__ == "__main__":
    main()

