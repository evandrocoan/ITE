#!/usr/bin/env bash


build=$1

if [[ -z "$build" ]]
then
    printf "Error: The first parameter variable is empty.\n"
    printf "You need to pass the build folder.\n"
    exit 1
fi

sublime_text_root="/cygdrive/f/SublimeText"
sublime_text_builds="/cygdrive/d/User/Programs/SublimeText"

if ! [ -d "$sublime_text_root" ]
then
    printf "Error: The sublime_text_root: $sublime_text_root folder does not exists.\n"
    printf "You need to edit this script fixing its path.\n"
    exit 1
fi

if ! [ -d "$sublime_text_builds" ]
then
    printf "Error: The sublime_text_builds: $sublime_text_builds folder does not exists.\n"
    printf "You need to edit this script fixing its path.\n"
    exit 1
fi


printf "$(date)\nRemoving folders...\n"

cd $sublime_text_root
rm -r "Packages"
rm "changelog.txt"
rm "msvcr100.dll"
rm "plugin_host.exe"
rm "python33.dll"
rm "sublime.py"
rm "sublime_text.exe"
rm "crash_reporter.exe"
rm "python3.3.zip"
rm "subl.exe"
rm "sublime_plugin.py"
rm "update_installer.exe"


printf "Copying new files...\n"
cd $sublime_text_builds

cp -r "$build/Packages" $sublime_text_root/
cp "$build/changelog.txt" $sublime_text_root/
cp "$build/msvcr100.dll" $sublime_text_root/
cp "$build/plugin_host.exe" $sublime_text_root/
cp "$build/python33.dll" $sublime_text_root/
cp "$build/sublime.py" $sublime_text_root/
cp "$build/sublime_text.exe" $sublime_text_root/
cp "$build/crash_reporter.exe" $sublime_text_root/
cp "$build/python3.3.zip" $sublime_text_root/
cp "$build/subl.exe" $sublime_text_root/
cp "$build/sublime_plugin.py" $sublime_text_root/
cp "$build/update_installer.exe" $sublime_text_root/


