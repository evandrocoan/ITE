
import os
import sublime
import sublime_plugin



isNotSyncedSideBarEnabled = True

class SyncedSideBarRevealInSideBarCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        self.view.window().run_command ("reveal_in_side_bar")

    def is_visible(self):

        # print( 'isNotSyncedSideBarEnabled: ' + str( isNotSyncedSideBarEnabled ) )
        return isNotSyncedSideBarEnabled



def plugin_loaded():

    global isNotSyncedSideBarEnabled

    userSettings    = sublime.load_settings('Preferences.sublime-settings')
    packageSettings = sublime.load_settings('SyncedSideBar.sublime-settings')

    def updateIsSyncedSideBarEnabled():

        # print('    updateIsSyncedSideBarEnabled!!!!')
        updateGlobalData( packageSettings, is_package_enabled( userSettings, "SyncedSideBar" ) )

    def updateGlobalData( packageSettings, isEnabled ):

        global isNotSyncedSideBarEnabled

        if isEnabled:

            isEnabled = packageSettings.get( "reveal-on-activate" )
            isNotSyncedSideBarEnabled = not isEnabled

        else:

            isNotSyncedSideBarEnabled = True

        # print( 'isNotSyncedSideBarEnabled: ' + str( isNotSyncedSideBarEnabled ) )


    def read_pref_async():

        # print('READ_PREF_ASYNC!!!!')
        updateIsSyncedSideBarEnabled()

    def read_user_preferences():

        # print('READ_package_PREFERENCES!!!!')
        userSettings = sublime.load_settings('Preferences.sublime-settings')
        updateIsSyncedSideBarEnabled()

    def read_package_preferences():

        # print('READ_package_PREFERENCES!!!!')
        packageSettings = sublime.load_settings('SyncedSideBar.sublime-settings')
        updateIsSyncedSideBarEnabled()

    # read initial setting, after all packages being loaded
    sublime.set_timeout_async( read_pref_async, 10000 )

    # listen for changes
    packageSettings.add_on_change( "Preferences", read_user_preferences )
    packageSettings.add_on_change( "SyncedSideBar", read_package_preferences )

    # print( packageSettings.get( "reveal-on-activate" ) )
    # print( userSettings.get( "ignored_packages" ) )



def is_package_enabled( userSettings, package_name ):

    # print( "is_package_enabled = " + sublime.packages_path()
    #         + "/All Autocomplete/ is dir? " \
    #         + str( os.path.isdir( sublime.packages_path() + "/" + package_name ) ) )

    # print( "is_package_enabled = " + sublime.installed_packages_path()
    #         + "/All Autocomplete.sublime-package is file? " \
    #         + str( os.path.isfile( sublime.installed_packages_path() + "/" + package_name + ".sublime-package" ) ) )

    ignoredPackages = userSettings.get('ignored_packages')

    if ignoredPackages is not None:

        return ( os.path.isdir( sublime.packages_path() + "/" + package_name ) \
                or os.path.isfile( sublime.installed_packages_path() + "/" + package_name + ".sublime-package" ) ) \
                and not package_name in ignoredPackages

    return os.path.isdir( sublime.packages_path() + "/" + package_name ) \
            or os.path.isfile( sublime.installed_packages_path() + "/" + package_name + ".sublime-package" )




