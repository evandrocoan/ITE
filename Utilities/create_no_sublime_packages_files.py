#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os

"""
Creates a `.no-sublime-package` into all subdirectories of the current directory where this script
file is on.
"""

current_directory = os.path.dirname(os.path.realpath(__file__))
print('\ndirectory walk', current_directory)

def create_no_sublime_package():

    for directory_name in os.listdir(current_directory):
        full_path = os.path.join(current_directory, directory_name)

        if os.path.isdir(full_path):
            print('directory_name', directory_name)
            full_path = os.path.join(full_path, '.no-sublime-package')

            if not os.path.exists(full_path):
                open(full_path, 'a').close()



if __name__ == "__main__":
    create_no_sublime_package()
