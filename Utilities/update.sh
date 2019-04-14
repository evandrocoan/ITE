#!/usr/bin/env bash


build=$1
printf '%s\n' "$(date)"

if [[ -z "${build}" ]]
then
    printf 'Error: The first parameter variable is empty.\n'
    printf 'You need to pass the build directory.\n'
    exit 1
fi

sublime_text_root=(
"/cygdrive/f/SublimeText"
"/cygdrive/f/SublimeText/MSYS2"
"/cygdrive/f/SublimeText/StableVersion"
"/cygdrive/f/SublimeText/Vanilla"
"/cygdrive/f/SublimeText/CleanTesting/3176"
)
sublime_text_builds="/cygdrive/d/User/Programs/SublimeText"
sublime_text_build="${sublime_text_builds}/${build}"

if ! [ -d "${sublime_text_build}" ]
then
    printf 'Error: The sublime_text_build: %s directory does not exists.\n' "${sublime_text_build}"
    printf 'You need to edit this script fixing its path.\n'
    exit 1
fi

for sublime_destine_path in "${sublime_text_root[@]}"
do
    if [ ! -d "${sublime_destine_path}" ]
    then
        printf 'Error: The sublime_destine_path: %s directory does not exists.\n' "${sublime_destine_path}"
        printf 'You need to edit this script fixing its path.\n'
        exit 1
    fi
done

# https://stackoverflow.com/questions/1951506/add-a-new-element-to-an-array-without-specifying-the-index-in-bash
declare -a filenames

for filename in "${sublime_text_build}"/*
do
    if [[ ! -d ${filename} ]]
    then
        # filenames+=($(basename "${filename}"))
        filenames=("${filenames[@]}" $(basename "${filename}"))
    fi
done

for sublime_destine_path in "${sublime_text_root[@]}"
do
    printf '\nRemoving Packages directory...\n'
    rm -r "${sublime_destine_path}/Packages"

    # https://stackoverflow.com/questions/15691942/bash-print-array-elements-on-separate-lines
    printf 'Removing files...\n'

    for filename in "${filenames[@]}"
    do
        full_path="${sublime_destine_path}/${filename}"
        rm -v "${full_path}"
    done

    printf '\nCopying Packages directory...\n'
    cp -r "${sublime_text_build}/Packages" "${sublime_destine_path}/"

    printf 'Copying files...\n'
    for filename in "${filenames[@]}"
    do
        source_full_path="${sublime_text_build}/${filename}"
        destine_full_path="${sublime_destine_path}/${filename}"

        cp -v "${source_full_path}" "${destine_full_path}"
    done
done

