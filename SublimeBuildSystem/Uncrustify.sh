

UNCRUSTIFY_SETTINGS_FILE="D:/User/Dropbox/Applications/SoftwareVersioning/MyUncrustifyConfigs/amxmodx_semicolon.cfg"

# Convert the windows path to linux path
FILE_TO_APPLY=$(echo $1 | sed -e 's@\\@\/@g')

# Declare an array variable. You can access them using echo "${arr[0]}", "${arr[1]}"
declare -a terminal_list=( "uncrustify" "uncrustify.exe" )

# Now loop through the above array
for current_terminal in "${terminal_list[@]}"
do
    if command -v $current_terminal >/dev/null 2>&1;
    then
        $current_terminal -c $UNCRUSTIFY_SETTINGS_FILE --no-backup $FILE_TO_APPLY
    fi
done


