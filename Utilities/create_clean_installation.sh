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

sync_directory_path () {
    package_name="$1"
    printf "%s\n" "$(get_file_path "$build/Data/Packages/$package_name")"
    mkdir -p "$build/Data/Packages/$package_name"
    rsync -r --exclude .git --exclude __pycache__ --exclude *.pyc --no-p --chmod=ugo=rwX \
            "$full_data/Packages/$package_name/" \
            "$build/Data/Packages/$package_name/"
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

    sync_directory_path "StudioChannel"
    # sync_directory_path "AmxxChannel"
    sync_directory_path "channelmanager"
    sync_directory_path "debugtools"
    sync_directory_path "PackagesManager"
    sync_directory_path "UnitTesting"
    sync_directory_path "coverage"
    sync_directory_path "concurrentloghandler"
    sync_directory_path "portalockerfiles"
    sync_directory_path "python-pywin32"

fi

printf "Done syncing!\n"
