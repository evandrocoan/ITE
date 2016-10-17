
import sublime
import sublime_plugin


isNotSyncedSideBarEnabled = True

class SyncedSideBarRevealInSideBarCommand(sublime_plugin.TextCommand):

    global isNotSyncedSideBarEnabled

    def run(self, edit):

        self.view.window().run_command ("reveal_in_side_bar")


    def is_visible(self):

        #print( 'isNotSyncedSideBarEnabled: ' + str( isNotSyncedSideBarEnabled ) )
        return isNotSyncedSideBarEnabled



def plugin_loaded():

    global isNotSyncedSideBarEnabled

    userSettings           = sublime.load_settings('SyncedSideBar.sublime-settings')
    packageControlSettings = sublime.load_settings('Package Control.sublime-settings')

    def updateIsSyncedSideBarEnabled():

        #print('    updateIsSyncedSideBarEnabled!!!!')

        isIgnored = False
        isIgnored = False
        
        ignoredPackages   = userSettings.get( "ignored_packages" )
        installedPackages = packageControlSettings.get( "installed_packages" )

        if( ignoredPackages != None ):

            isIgnored = any( "SyncedSideBar" in package for package in ignoredPackages )

        if( installedPackages != None ):

            isInstalled = any( "SyncedSideBar" in package for package in installedPackages )

        updateGlobalData( isIgnored, isInstalled )

        #print( 'isIgnored: ' + str( isIgnored ) )
        #print( 'isInstalled: ' + str( isInstalled ) )


    def updateGlobalData( isIgnored, isInstalled ):

        global isNotSyncedSideBarEnabled

        if isIgnored:

            isNotSyncedSideBarEnabled = True

        else:

            if isInstalled:

                isEnabled = userSettings.get( "reveal-on-activate" )
                isNotSyncedSideBarEnabled = not isEnabled

            else:

                isNotSyncedSideBarEnabled = True

        #print( 'isNotSyncedSideBarEnabled: ' + str( isNotSyncedSideBarEnabled ) )


    def read_pref_async():

        #print('READ_PREF_ASYNC!!!!')
        updateIsSyncedSideBarEnabled()


    def read_pref_package():

        #print('READ_PREF_PACKAGE!!!!')
        packageControlSettings = sublime.load_settings('Package Control.sublime-settings')
        updateIsSyncedSideBarEnabled()


    def read_pref_preferences():

        #print('READ_PREF_PREFERENCES!!!!')
        userSettings = sublime.load_settings('SyncedSideBar.sublime-settings')
        updateIsSyncedSideBarEnabled()


    # read initial setting, after all packages being loaded
    sublime.set_timeout_async( read_pref_async, 10000 )

    # listen for changes
    userSettings.add_on_change( "SyncedSideBar", read_pref_preferences )
    packageControlSettings.add_on_change( "Package Control", read_pref_package )

    #print( userSettings.get( "ignored_packages" ) )
    #print( packageControlSettings.get( "installed_packages" ) )



