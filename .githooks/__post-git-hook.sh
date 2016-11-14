#!/usr/bin/env bash

#
# Run the version update script.
#



# This script is run straight from the project's git root folder, as the current working directory.
printf "Running the __post-git-hook.sh script...\n"


# Reliable way for a bash script to get the full path to itself?
# http://stackoverflow.com/questions/4774054/reliable-way-for-a-bash-script-to-get-the-full-path-to-itself
pushd `dirname $0` > /dev/null
SCRIPTPATH=`pwd`
popd > /dev/null

# Remove the '/app/blabla/' from the $SCRIPTPATH variable.
# https://regex101.com/r/rR0oM2/1
AUTO_VERSIONING_ROOT_FOLDER_NAME=$(echo $SCRIPTPATH | sed -r "s/((.+\/)+)//")

# Read the configurations file.
GIT_DIR_="$(git rev-parse --git-dir)"
githooksConfig=$(cat $GIT_DIR_/../$AUTO_VERSIONING_ROOT_FOLDER_NAME/githooksConfig.txt)

# $filePathToUpdate example: scripting/galileo.sma
filePathToUpdate=$GIT_DIR_/../$(echo $githooksConfig | cut -d',' -f 2)

# $targetBranch example: develop, use . to operate all branches
targetBranch=$(echo $githooksConfig | cut -d',' -f 3)

# Remove the '/app/blabla/' from the $filePathToUpdate argument name. Example: galileo.sma
# https://regex101.com/r/rR0oM2/1
fileNameToUpdate=$(echo $filePathToUpdate | sed -r "s/((.+\/)+)//")

# $updateFlagFilePath example: isToUpdateTheGalileoFile.txt
sulfixName="FlagFile.txt"
updateFlagFilePath="$GIT_DIR_/$fileNameToUpdate$sulfixName"

currentBranch=$(git rev-parse --symbolic-full-name --abbrev-ref HEAD)
updateVersionProgram=$GIT_DIR_/../$AUTO_VERSIONING_ROOT_FOLDER_NAME/updateVersion.sh


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
        printf "Amending commits...\n"
        git commit --amend -C HEAD --no-verify
    else
        printf "It is not time to amend, as we are not on the '$targetBranch' branch.\n"
    fi
else
    printf "It is not time to amend, as the file '$updateFlagFilePath' does not exist.\n"
fi


# To clean any old missed file
cleanUpdateFlagFile


# Exits the program using a successful exit status code.
exit 0





