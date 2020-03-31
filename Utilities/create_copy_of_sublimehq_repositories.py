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
Iterates through all subdirectories of the current directory where this script file is on, but do not
recurse into them.
"""

from debug_tools import getLogger
log = getLogger( __name__ )

current_directory = os.path.dirname( os.path.realpath(__file__) )
log( 1, 'directory walk %s', current_directory )


# If `TYPE` is equals to ProcessType.CREATE_README, it will not git for subtree operations but will
# create `README.md` and `LICENSE` on all repositories. Notice, an existing `README.md` will be
# overridden.
TYPE = 1

# The maximum count of repositories to to process when calling this batch script.
maximum_process_limit = 1000

# GitHub token with full repository access
token = "Authorization: token 1231231241231231251231231232131231223123"
user_name = "evandroforks"


class ProcessType(object):
    CREATE_README = 0


def run_command(absolute_path, command_name):
    command = shlex.split( command_name )
    log( 1, 'command: %s', command )

    command_line_interface = subprocess.Popen( command, stdout=subprocess.PIPE, cwd=absolute_path )
    output = command_line_interface.communicate()[0]

    # log( 1, "%s", output )
    log( 1, "\n%s", output.decode('utf-8') )
    return output


def process_submodule(current_directory, submodule_path, submodule_name):

    if os.path.isdir(submodule_path):
        repository_name = "SublimePackage%s" % submodule_name.replace( ' ', '' )
        submodule_remote = "https://github.com/%s/%s.git" % ( user_name, repository_name )

        # https://developer.github.com/v3/repos/#create
        # repository_type = "https://api.github.com/user/repos"
        repository_type = "https://api.github.com/orgs/%s/repos" % user_name

        global maximum_process_limit
        maximum_process_limit -= 1

        result = run_command( current_directory, "curl -H '%s' https://api.github.com/repos/%s/%s" % ( token, user_name, repository_name ) )
        result_json = json.loads( result.decode('utf-8') )

        if 'message' in result_json and result_json['message'] == 'Not Found':
            log( 1, "equals: %s", repository_name )

            if TYPE == ProcessType.CREATE_README:
                destine_readme = os.path.realpath( os.path.join( submodule_path, 'README.md' ) )
                destine_gitignore = os.path.realpath( os.path.join( submodule_path, '.gitignore' ) )

                source_license = os.path.realpath( os.path.join( current_directory, 'LICENSE' ) )
                destine_license = os.path.realpath( os.path.join(submodule_path, 'LICENSE') )

                if not os.path.exists(destine_license):
                    shutil.copyfile( source_license, destine_license )

                with open( destine_readme, "w" ) as text_file:
                    text_file.write(
                        "# Sublime Text `%s` Package\n"
                        "\n"
                        "This repository is a mirror from Sublimehq/Packages for distributing its updates with Package Control/PackagesManager.\n"
                        "See:\n"
                        "1. https://github.com/sublimehq/Packages\n"
                        "1. https://github.com/evandroforks/Packages\n"
                        "1. https://github.com/evandrocoan/StudioChannel\n"
                        "\n"
                        "## License\n"
                        "See the `LICENSE` file under this repository.\n" % ( submodule_name )
                    )

                with open( destine_gitignore, "w" ) as text_file:
                    text_file.write(
                        "/.git**\n"
                        "!/.gitignore\n"
                        "!/.gitattributes\n"
                        "!/.gitmodules\n"
                    )

            else:

                full_command = \
                r"""
                    curl -i -H '%s'
                        -d '{
                            "name": "%s",
                            "description": "A mirror from Sublimehq/Packages for distributing its updates with Package Control/PackagesManager",
                            "homepage": "https://github.com/evandroforks/Packages",
                            "private": false
                            }'
                        %s
                """ % ( token, repository_name, repository_type )

                log( 1, 'submodule_path: %s' % full_command )
                run_command( submodule_path, full_command )

                run_command( submodule_path, 'git init' )
                run_command( submodule_path, 'git add --all' )
                run_command( submodule_path, 'git commit -m "Added initial files for Sublime Text build 3176"' )
                run_command( submodule_path, 'git remote add origin %s' % ( submodule_remote ) )
                run_command( submodule_path, 'git push origin master' )

                data_directory = os.path.realpath( os.path.join(current_directory, '..') )
                run_command( data_directory, 'git submodule add -- %s "Packages/%s"' % ( submodule_remote, submodule_name ) )

        else:
            log( 1, "\n%s", result.decode('utf-8') )

    else:
        log( 1, "Not equals: %s", submodule_name )


def main():

    for submodule_name, pi in sequence_timer( default_packages, info_frequency=0 ):
        submodule_path = os.path.join(current_directory, submodule_name)

        if os.path.isdir(submodule_path):
            progress = progress_info( pi )
            log(1, '')
            log(1, '')
            log(1, '')
            log(1, '')
            log( 1, "{:s} Processing {:3d} of {:d} repositories... {:s}".format( progress, pi.index, pi.count, submodule_name ) )

            if maximum_process_limit <= 0:
                return

            process_submodule(current_directory, submodule_path, submodule_name)


default_packages = \
[
    "ActionScript",
    "AppleScript",
    "ASP",
    "Batch File",
    "C#",
    "C++",
    "Clojure",
    "CSS",
    "D",
    "Diff",
    "Erlang",
    "Git Formats",
    "Go",
    "Graphviz",
    "Groovy",
    "Haskell",
    "HTML",
    "Java",
    "JavaScript",
    "JSON",
    "LaTeX",
    "Lisp",
    "Lua",
    "Makefile",
    "Markdown",
    "Matlab",
    "Objective-C",
    "OCaml",
    "Pascal",
    "Perl",
    "PHP",
    "Python",
    "R",
    "Rails",
    "Regular Expressions",
    "RestructuredText",
    "Ruby",
    "Rust",
    "Scala",
    "ShellScript",
    "SQL",
    "TCL",
    "Text",
    "Textile",
    "XML",
    "YAML",
]


if __name__ == "__main__":
    main()

