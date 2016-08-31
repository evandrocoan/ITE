

# Where is your compiler?
# Example: "F:/SteamCMD/steamapps/common/Half-Life/czero/addons/amxmodx/scripting/amxxpc.exe"
AMXX_COMPILER_PATH="amxxpc.exe"

# Where put the '.amxx' compiled file?
# Example: "/SteamCMD/steamapps/common/Half-Life/czero/addons/amxmodx/plugins"
AMXX_OUTPUT_PLUGIN_FOLDER="F:/SteamCMD/steamapps/common/Half-Life/czero/addons/amxmodx/plugins"

# $1 is the first shell argument and $2 is the second shell argument passed by AmxxPawn.sublime-build
# Usually they should be the plugin's file full path and the plugin's file name without extension.
# Example: $1="F:/SteamCMD/steamapps/common/Half-Life/czero/addons/my_plugin.sma" and $2="my_plugin"
$AMXX_COMPILER_PATH -o$AMXX_OUTPUT_PLUGIN_FOLDER/$2.amxx $1

