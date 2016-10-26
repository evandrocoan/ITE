

# $1 is the first shell argument and $2 is the second shell argument passed by AmxxPawn.sublime-build
# Usually they should be the plugin's file full path and the plugin's file name without extension.
#
# Example: $1="F:/SteamCMD/steamapps/common/Half-Life/czero/addons/my_plugin.sma" and $2="my_plugin"
# "C:\Program Files (x86)\PostgreSQL\9.6\bin\psql.exe" --host "localhost" --port 5432 --username "postgres" -d "aula20"
#
PGPASSWORD=admin;psql --host "localhost" --port 5432 --username "postgres" -d "aula23" < $1

