#!/usr/bin/env bash


target_zip_file="$1"
build="$2"

if [ -z $target_zip_file ]; then
    target_zip_file="PackageControlBuilt.zip"

    # sync_only="Uncomment this to sync only, instead of doing a full replacement."
    # target_zip_file="NothingBuilt.zip"
    # target_zip_file="PackageControlBuilt.zip"
    target_zip_file="PackagesManagerBuild.zip"
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
    printf "$(date)\nRemoving directories from %s\n" "$(get_file_path "$build/Data/")"
    rm -rf "$build/Data/"
fi

printf "Unzipping files from %s\n" "$(get_file_path "$clean_testing/$target_zip_file")"
unzip -q -n "./$clean_testing/$target_zip_file" -d "$build/Data/"

if [[ "$target_zip_file" != "NothingBuilt.zip" ]]
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

    printf "%s\n" "$(get_file_path "$build/Data/Packages/PackagesManager")"
    mkdir -p "$build/Data/Packages/PackagesManager"
    rsync -r --exclude /.git "$full_data/Packages/PackagesManager/" \
            "$build/Data/Packages/PackagesManager/"

    printf "%s\n" "$(get_file_path "$build/Data/Packages/UnitTesting")"
    mkdir -p "$build/Data/Packages/UnitTesting"
    rsync -r --exclude /.git "$full_data/Packages/UnitTesting/" \
            "$build/Data/Packages/UnitTesting/"

    printf "%s\n" "$(get_file_path "$build/Data/Packages/coverage")"
    mkdir -p "$build/Data/Packages/coverage"
    rsync -r --exclude /.git "$full_data/Packages/coverage/" \
            "$build/Data/Packages/coverage/"

    printf "%s\n" "$(get_file_path "$build/Data/Packages/ConcurrentLogHandler")"
    mkdir -p "$build/Data/Packages/ConcurrentLogHandler"
    rsync -r --exclude /.git "$full_data/Packages/ConcurrentLogHandler/" \
            "$build/Data/Packages/ConcurrentLogHandler/"

    printf "%s\n" "$(get_file_path "$build/Data/Packages/PortalockerFiles")"
    mkdir -p "$build/Data/Packages/PortalockerFiles"
    rsync -r --exclude /.git "$full_data/Packages/PortalockerFiles/" \
            "$build/Data/Packages/PortalockerFiles/"

    printf "%s\n" "$(get_file_path "$build/Data/Packages/python-pywin32")"
    mkdir -p "$build/Data/Packages/python-pywin32"
    rsync -r --exclude /.git "$full_data/Packages/python-pywin32/" \
            "$build/Data/Packages/python-pywin32/"

fi

printf "Done syncing!\n"
