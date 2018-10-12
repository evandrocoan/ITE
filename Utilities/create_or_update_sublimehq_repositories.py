#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import shlex
import json
import subprocess
import shutil

"""
Iterates through all subdirectories of the current directory where this script file is on, but do not
recurse into them.

1. https://stackoverflow.com/questions/23937436/add-subdirectory-of-remote-repo-with-git-subtree
1. https://stackoverflow.com/questions/20102594/git-subtree-push-squash-does-not-squash
1. https://stackoverflow.com/questions/9614255/git-subtree-push-squash-needs-a-long-time-and-it-is-getting-longer-over-time
1. https://stackoverflow.com/questions/16134975/reduce-increasing-time-to-push-a-subtree
1. https://stackoverflow.com/questions/10081681/git-subtree-push-changes-back-to-subtree-project
1. https://stackoverflow.com/questions/26928299/why-does-git-subtree-push-always-list-hundreds-of-commits
1. https://github.com/git/git/blob/master/contrib/subtree/git-subtree.txt
1. https://github.com/git/git/blob/master/contrib/subtree/git-subtree.sh
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
user_name = "your_user_name"


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
        repository_name = "SublimePackage%s" % submodule_name
        submodule_remote = "https://github.com/%s/%s.git" % ( user_name, repository_name )

        # https://developer.github.com/v3/repos/#create
        # repository_type = "https://api.github.com/user/repos"
        repository_type = "https://api.github.com/orgs/%s/repos" % user_name

        global maximum_process_limit
        maximum_process_limit -= 1

        result = run_command( current_directory, "curl -H '%s' https://api.github.com/repos/%s/%s" % ( token, user_name, repository_name ) )
        result_json = json.loads( result.decode('utf-8') )

        if 'message' not in result_json:
            log( 1, "Running git subtree push only: %s", repository_name )
            run_command( current_directory, 'git subtree push --prefix=%s %s master' % ( submodule_name, submodule_remote ) )

        elif 'message' in result_json and result_json['message'] == 'Not Found':
            log( 1, "equals: %s", repository_name )

            if TYPE == ProcessType.CREATE_README:
                destine_readme = os.path.realpath( os.path.join( submodule_path, 'README.md' ) )

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

                # Too slow to run these commands separately
                # run_command( current_directory, 'git subtree push --prefix=%s %s master' % ( submodule_name, submodule_remote ) )
                # run_command( current_directory, 'git subtree split --rejoin --prefix=%s' % ( submodule_name ) )

                run_command( current_directory, 'git subtree split --rejoin --prefix=%s -b split-branch' % ( submodule_name ) )
                run_command( current_directory, 'git push %s split-branch:master' % ( submodule_remote ) )
                run_command( current_directory, 'git branch -d split-branch' )

        else:
            log( 1, '' )
            log( 1, '' )
            log( 1, '' )
            log( 1, "\n%s", result.decode('utf-8') )
            raise RuntimeError( "ERROR PROCESSING %s" % submodule_name )

    else:
        log( 1, "Not equals: %s", submodule_name )


def main():

    for submodule_name in default_packages:
        submodule_path = os.path.join(current_directory, submodule_name)

        if os.path.isdir(submodule_path):
            log(1, '')
            log(1, '')
            log(1, '')
            log(1, '')
            log(1, 'submodule_name: %s', submodule_name)

            if maximum_process_limit <= 0:
                return

            process_submodule(current_directory, submodule_path, submodule_name)

    if TYPE == ProcessType.CREATE_README:
        run_command( current_directory, 'git commit -m "Created README.md and LICENSE"' )


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

