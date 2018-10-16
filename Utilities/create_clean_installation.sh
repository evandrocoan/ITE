
# sync_only="Uncomment this"
target_zip_file="$1"
build="$2"

if [ -z $target_zip_file ]; then
    target_zip_file="IteBasicStudioTest.zip"
fi

if [ -z $build ]; then
    build="3176"
fi

full_data="./../"
clean_testing="./../../CleanTesting"
build="./$clean_testing/$build"

get_file_path () {
   printf "%s" "$(cd $(dirname "$1") && pwd -P)/$(basename "$1")"
}

get_directory_path () {
   printf "%s" "$(cd $(dirname "$1") && pwd -P)/"
}

if [ -z $sync_only ]; then
    printf "$(date)\nRemoving folders from %s\n" "$(get_directory_path "$build/Data/")"
    rm -rf "$build/Data/"
fi

printf "Unzipping files from %s\n" "$(get_file_path "$clean_testing/$target_zip_file")"
unzip -q "./$clean_testing/$target_zip_file" -d "$build/Data/"

if [[ "$target_zip_file" != "IteMinimal.zip" ]]
then
    printf "Syncing folders...\n"

    # mkdir -p "$build/Data/Packages/StudioChannel"
    # rsync -r --exclude /.git "$full_data/lPackages/StudioChannel/" \
    #         "$build/Data/Packages/StudioChannel/"

    # mkdir -p "$build/Data/Packages/AmxxChannel"
    # rsync -r --exclude /.git "$full_data/lPackages/AmxxChannel/" \
    #         "$build/Data/Packages/AmxxChannel/"

    # mkdir -p "$build/Data/Packages/ChannelManager"
    # rsync -r --exclude /.git "$full_data/lPackages/ChannelManager/" \
    #         "$build/Data/Packages/ChannelManager/"

    # mkdir -p "$build/Data/Packages/DebugTools"
    # rsync -r --exclude /.git "$full_data/lPackages/DebugTools/" \
    #         "$build/Data/Packages/DebugTools/"

    mkdir -p "$build/Data/Packages/PackagesManager"
    rsync -r --exclude /.git "$full_data/Packages/PackagesManager/" \
            "$build/Data/Packages/PackagesManager/"

fi

printf "Done syncing!\n"
