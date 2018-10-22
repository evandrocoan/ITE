#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

####################### Licensing #######################################################
#
# PackagesManager, Re-enabler Utility
# Copyright (C) 2018 Evandro Coan <https://github.com/evandrocoan>
#
#  Redistributions of source code must retain the above
#  copyright notice, this list of conditions and the
#  following disclaimer.
#
#  Redistributions in binary form must reproduce the above
#  copyright notice, this list of conditions and the following
#  disclaimer in the documentation and/or other materials
#  provided with the distribution.
#
#  Neither the name Evandro Coan nor the names of any
#  contributors may be used to endorse or promote products
#  derived from this software without specific prior written
#  permission.
#
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the
#  Free Software Foundation; either version 3 of the License, or ( at
#  your option ) any later version.
#
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################################
#

'''
Reenable PackagesManager, if it was disabled during its own update and get lost.

This has no effect if the user disabled PackagesManager by himself because this program only takes
effect when PackagesManager is disabled and is inserted on the PackagesManager `in_process_packages`
setting. And the setting `in_process_packages` is only set by PackagesManager, when its starts
updating some package.

See the issue:
1. https://github.com/wbond/package_control/issues/1164
   Create a dummy package that can re-enable Package Control if ST was restarted during a Package Control update
'''

import sublime

import os
import random
import time
import threading

SUBLIME_SETTING_NAME = "Preferences"
PACKAGESMANAGER_NAME = "PackagesManager"

PACKAGE_ROOT_DIRECTORY = os.path.dirname( os.path.realpath( __file__ ) )


def main_directory():
    return get_main_directory( PACKAGE_ROOT_DIRECTORY )


def get_main_directory(current_directory):
    possible_main_directory = os.path.normpath( os.path.dirname( os.path.dirname( current_directory ) ) )

    if sublime:
        sublime_text_packages = os.path.normpath( os.path.dirname( sublime.packages_path() ) )

        if possible_main_directory == sublime_text_packages:
            return possible_main_directory

        else:
            return sublime_text_packages

    return possible_main_directory


def sublime_setting_path():
    return os.path.join( main_directory(), "Packages", "User", "%s.sublime-settings" % SUBLIME_SETTING_NAME )


def packagesmanager_setting_path():
    return os.path.join( main_directory(), "Packages", "User", "%s.sublime-settings" % PACKAGESMANAGER_NAME )


def sublime_setting_file():
    return '%s.sublime-settings' % SUBLIME_SETTING_NAME


def packagesmanager_setting_file():
    return '%s.sublime-settings' % PACKAGESMANAGER_NAME


def plugin_loaded():
    threading.Thread( target=_delayed_in_progress_removal, args=(PACKAGESMANAGER_NAME,) ).start()


def _delayed_in_progress_removal(package_name):
    sleep_delay = 60 + random.randint( 0, 60 )
    time.sleep( sleep_delay )

    packages_setting = sublime.load_settings( packagesmanager_setting_file() )
    in_process_count = packages_setting.get( 'in_process_packages_count', 0 )
    in_process_packages = packages_setting.get( 'in_process_packages', [] )

    # print("in_process_count:", in_process_count, ", in_process_packages:", in_process_packages)
    if package_name in in_process_packages:
        sublime_settings = sublime.load_settings( sublime_setting_file() )
        ignored_packages = sublime_settings.get( 'ignored_packages', [] )

        if package_name in ignored_packages:
            print( "PackagesManager: The package `%s` should not be in your User `ignored_packages` "
                  "package settings, after %d seconds." % ( package_name, sleep_delay ) )

            if in_process_count > 3:
                ignored_packages.remove( package_name )

                sublime_settings.set( 'ignored_packages', ignored_packages )
                packages_setting.erase( 'in_process_packages_count' )

                sublime.save_settings( sublime_setting_file() )
                sublime.save_settings( packagesmanager_setting_file() )

            else:
                packages_setting.set( 'in_process_packages_count', in_process_count + 1 )
                sublime.save_settings( packagesmanager_setting_file() )

        else:
            print("PackagesManager: Finishing the package `%s` changes after randomly %s seconds delay." % ( package_name, sleep_delay ) )
            in_process_packages.remove( package_name )

            packages_setting.erase( 'in_process_packages_count' )
            packages_setting.set( 'in_process_packages', in_process_packages )
            sublime.save_settings( packagesmanager_setting_file() )
