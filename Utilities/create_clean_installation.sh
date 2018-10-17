#!/usr/bin/env bash


target_zip_file="$1"
build="$2"

if [ -z $target_zip_file ]; then
    target_zip_file="IteBasicStudioTest.zip"
fi

if [ -z $build ]; then
    build="3176"
fi

# sync_only="Uncomment this to sync only, instead of doing a full replacement."
# target_zip_file="IteMinimal.zip"

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
    printf "$(date)\nRemoving directories from %s\n" "$(get_file_path "$build/Data/")"
    rm -rf "$build/Data/"
fi

printf "Unzipping files from %s\n" "$(get_file_path "$clean_testing/$target_zip_file")"
unzip -q -n "./$clean_testing/$target_zip_file" -d "$build/Data/"

if [[ "$target_zip_file" != "IteMinimal.zip" ]]
then
    printf "\n"
    printf "Syncing folders...\n"

    printf "%s\n" "$(get_file_path "$build/Data/Packages/StudioChannel")"
    mkdir -p "$build/Data/Packages/StudioChannel"
    rsync -r --exclude /.git "$full_data/Packages/StudioChannel/" \
            "$build/Data/Packages/StudioChannel/"

    # printf "%s\n" "$(get_file_path "$build/Data/Packages/AmxxChannel")"
    # mkdir -p "$build/Data/Packages/AmxxChannel"
    # rsync -r --exclude /.git "$full_data/Packages/AmxxChannel/" \
    #         "$build/Data/Packages/AmxxChannel/"

    printf "%s\n" "$(get_file_path "$build/Data/Packages/ChannelManager")"
    mkdir -p "$build/Data/Packages/ChannelManager"
    rsync -r --exclude /.git "$full_data/Packages/ChannelManager/" \
            "$build/Data/Packages/ChannelManager/"

    printf "%s\n" "$(get_file_path "$build/Data/Packages/DebugTools")"
    mkdir -p "$build/Data/Packages/DebugTools"
    rsync -r --exclude /.git "$full_data/Packages/DebugTools/" \
            "$build/Data/Packages/DebugTools/"

    # printf "%s\n" "$(get_file_path "$build/Data/Packages/PackagesManager")"
    # mkdir -p "$build/Data/Packages/PackagesManager"
    # rsync -r --exclude /.git "$full_data/Packages/PackagesManager/" \
    #         "$build/Data/Packages/PackagesManager/"

    printf "%s\n" "$(get_file_path "$build/Data/Packages/UnitTesting")"
    mkdir -p "$build/Data/Packages/UnitTesting"
    rsync -r --exclude /.git "$full_data/Packages/UnitTesting/" \
            "$build/Data/Packages/UnitTesting/"

fi

printf "Done syncing!\n"
