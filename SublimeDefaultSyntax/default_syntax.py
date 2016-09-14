


import sublime
import sublime_plugin


class DefaultSyntaxCommand(sublime_plugin.EventListener):

	def on_new(self, view):

		view.set_syntax_file("Packages/C++/C++.tmLanguage")



class ForceRewriteSublimeSettingsCommand(sublime_plugin.TextCommand):

    def run(self, edit):

        sublime.save_settings('Preferences.sublime-settings')



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

    userSettings           = sublime.active_window().active_view().settings()
    packageControlSettings = sublime.load_settings('Package Control.sublime-settings')

    def updateIsSyncedSideBarEnabled():

        #print('    updateIsSyncedSideBarEnabled!!!!')
        global isNotSyncedSideBarEnabled

        ignoredPackages   = userSettings.get( "ignored_packages" )
        installedPackages = packageControlSettings.get( "installed_packages" )

        isIgnored         = any( "SyncedSideBar" in package for package in ignoredPackages )
        isInstalled       = any( "SyncedSideBar" in package for package in installedPackages )

        #print( 'isIgnored: ' + str( isIgnored ) )
        #print( 'isInstalled: ' + str( isInstalled ) )

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
        updateIsSyncedSideBarEnabled()


    def read_pref_preferences():

        #print('READ_PREF_PREFERENCES!!!!')
        updateIsSyncedSideBarEnabled()


    # read initial setting, after all packages being loaded
    sublime.set_timeout_async( read_pref_async, 10000 )

    # listen for changes
    userSettings.add_on_change( "Preferences", read_pref_preferences )
    packageControlSettings.add_on_change( "Package Control", read_pref_package )

    #print( userSettings.get( "ignored_packages" ) )
    #print( packageControlSettings.get( "installed_packages" ) )




