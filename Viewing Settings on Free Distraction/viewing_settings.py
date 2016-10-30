

import sublime
import sublime_plugin


class SampleListener(sublime_plugin.EventListener):
    """
    It requires the packaga `DistractionFreeWindow` installed and configured to hide the SideBar and
    the Mini Map.
    
    The dirt trick here is to put the current window on the `distraction_free_window` mode on the
    `on_window_command` pre command hook, then the new setting windows will inherited it.
    
    Later on the `on_post_window_command` post command hook, we set the current window back from
    the `distraction_free_window` mode.
    
    How to hook the new show settings event?
    https://forum.sublimetext.com/t/how-to-hook-the-new-show-settings-event/23793/2
    http://docs.sublimetext.info/en/latest/extensibility/commands.html

    Add option to disable the minimap and/or lines numbers (if actived) when opening the new Settings 
    https://github.com/evandrocoan/SublimeTextStudio/issues/12
    """
    
    def on_window_command(self, window, command, args):
        
        if command == "edit_settings":
            
            print ("About to execute " + command)
            window.run_command("distraction_free_window")


    def on_post_window_command(self, window, command, args):
        
        #print ("Finished executing " + command)
        
        if command == "edit_settings":
            
            #print ("EXECUTING...")
            window.run_command("distraction_free_window")



