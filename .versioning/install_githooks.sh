#!/usr/bin/env bash


# Whether we are dealing with a git-submodule or not, this get the correct git file path for the
# project root folder if run on it directory, or for the sub-module folder if run on its directory.
GIT_DIR_="$(git rev-parse --git-dir)"
gitHooksPath="$GIT_DIR_/hooks"



if [ -d $gitHooksPath ]
then
    printf "Installing the githooks...\n\n"

    # Reliable way for a bash script to get the full path to itself?
    # http://stackoverflow.com/questions/4774054/reliable-way-for-a-bash-script-to-get-the-full-path-to-itself
    pushd `dirname $0` > /dev/null
    SCRIPT_FOLDER_PATH=`pwd`
    popd > /dev/null

    # Remove the '/app/blabla/' from the $SCRIPT_FOLDER_PATH variable.
    # https://regex101.com/r/rR0oM2/1
    AUTO_VERSIONING_ROOT_FOLDER_NAME=$(echo $SCRIPT_FOLDER_PATH | sed -r "s/((.+\/)+)//")

    # Get the submodule (if any) or the main's repository root directory
    PROJECT_ROOT_DIRECTORY=$(git rev-parse --show-toplevel)

    # Given:
    # D:/User/Dropbox/Applications/SoftwareVersioning/SublimeText/Data/Packages/.git/modules/amxmodx (GIT_DIR_)
    # D:/User/Dropbox/Applications/SoftwareVersioning/SublimeText/Data/Packages/amxmodx (PROJECT_ROOT_DIRECTORY)
    #
    # Returns:
    # ../../../amxmodx
    # pathToSubmodule=$(python -c "import os.path; print os.path.relpath('$PROJECT_ROOT_DIRECTORY', '$GIT_DIR_')")

    # Get the `AUTO_VERSIONING_ROOT_FOLDER_PATH`, i.e., the folder to the auto-versioning scripts.
    AUTO_VERSIONING_ROOT_FOLDER_PATH="$AUTO_VERSIONING_ROOT_FOLDER_NAME"

    # Write specify the githooks' root folder
    echo "$AUTO_VERSIONING_ROOT_FOLDER_PATH/scripts" > $gitHooksPath/gitHooksRoot.txt

    cp -v "$SCRIPT_FOLDER_PATH/scripts/post-checkout" $gitHooksPath
    cp -v "$SCRIPT_FOLDER_PATH/scripts/post-commit" $gitHooksPath
    cp -v "$SCRIPT_FOLDER_PATH/scripts/prepare-commit-msg" $gitHooksPath

    printf "\nThe githooks are successfully installed!\n"
else
    printf "Error! Could not to install the githooks.\n"
    printf "The folder \`$gitHooksPath\` folder is missing.\n\n"
fi




