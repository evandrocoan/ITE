#!/usr/bin/env bash

#
# Run the version update script.
#



# This script is run straight from the project's git root folder, as the current working directory.
# printf "Running the __post-git-hook.sh script...\n"


# Reliable way for a bash script to get the full path to itself?
# http://stackoverflow.com/questions/4774054/reliable-way-for-a-bash-script-to-get-the-full-path-to-itself
pushd `dirname $0` > /dev/null
SCRIPT_FOLDER_PATH=`pwd`
popd > /dev/null

# Get the project's `.git` folder. It will return the absolute path to the `.git` folder, unless
# the current working directory is already the project's git root path or the `.git` folder itself.
GIT_DIR_="$(git rev-parse --git-dir)"

# Get the submodule (if any) or the main's repository root directory
PROJECT_ROOT_DIRECTORY=$(git rev-parse --show-toplevel)


# Read the configurations file.
githooksConfig=$(cat $SCRIPT_FOLDER_PATH/githooksConfig.txt)

# $filePathToUpdate example: $PROJECT_ROOT_DIRECTORY/scripting/galileo.sma
filePathToUpdate=$PROJECT_ROOT_DIRECTORY/$(echo $githooksConfig | cut -d',' -f 2)

# $targetBranch example: develop, use . to operate all branches
targetBranch=$(echo $githooksConfig | cut -d',' -f 3)

# Remove the '/app/blabla/' from the $filePathToUpdate argument name. Example: galileo.sma
# https://regex101.com/r/rR0oM2/1
fileNameToUpdate=$(echo $filePathToUpdate | sed -r "s/((.+\/)+)//")

# $updateFlagFilePath example: Galileo.txtFlagFile.txt
sulfixName="FlagFile.txt"
updateFlagFilePath="$GIT_DIR_/$fileNameToUpdate$sulfixName"

# The the current active branch name.
currentBranch=$(git rev-parse --symbolic-full-name --abbrev-ref HEAD)

# Creates the path to the `updateVersion.sh` script.
updateVersionProgram=$SCRIPT_FOLDER_PATH/updateVersion.sh


cleanUpdateFlagFile()
{
    if [ -f $updateFlagFilePath ]
    then
        printf "Removing old post-commit or checkout configuration file '$updateFlagFilePath'...\n"
        rm $updateFlagFilePath
    fi
}


# Updates and changes the files if the flag file exits, if and only if we are on the '$targetBranch'
# branch.
if [ -f $updateFlagFilePath ]
then
    if [[ $currentBranch == $targetBranch || $targetBranch == "." ]]
    then
        if sh $updateVersionProgram build
        then
            printf "Successfully ran '$updateVersionProgram'.\n"
        else
            printf "Could not run the update program '$updateVersionProgram' properly!\n"
            cleanUpdateFlagFile
            exit 1
        fi

        # '-C HEAD' do not prompt for a commit message, use the HEAD as commit message.
        # '--no-verify' do not call the pre-commit hook to avoid infinity loop.
        # printf "Amending commits...\n"
        git commit --amend -C HEAD --no-verify
    else
        printf "It is not time to amend, as we are not on the '$targetBranch' branch.\n"
    fi
else
    # printf "It is not time to amend, as the file '$updateFlagFilePath' does not exist.\n"
    :
fi


# To clean any old missed file
cleanUpdateFlagFile


# Exits the program using a successful exit status code.
exit 0





