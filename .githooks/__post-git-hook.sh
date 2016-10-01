#!/usr/bin/env bash

#
# Run the version update script.
#



GIT_DIR_="$(git rev-parse --git-dir)"
githooksConfig=$(cat $GIT_DIR_/../.githooks/githooksConfig.txt)

# $filePathToUpdate example: scripting/galileo.sma
filePathToUpdate=$GIT_DIR_/../$(echo $githooksConfig | cut -d',' -f 2)

# $fileNameToUpdate example: galileo.sma
# Remove the '/app/blabla/' from the $filePathToUpdate argument name - https://regex101.com/r/rR0oM2/1
fileNameToUpdate=$(echo $filePathToUpdate | sed -r "s/((.+\/)+)//")

# $updateFlagFilePath example: isToUpdateTheGalileoFile.txt
sulfixName="FlagFile.txt"
updateFlagFilePath="$GIT_DIR_/$fileNameToUpdate$sulfixName"

currentBranch=$(git rev-parse --symbolic-full-name --abbrev-ref HEAD)
updateVersionProgram=$GIT_DIR_/../.githooks/updateVersion.sh


cleanUpdateFlagFile()
{
    if [ -f $updateFlagFilePath ]
    then
        echo "Removing old post-commit or checkout configuration file '$updateFlagFilePath'..."
        rm $updateFlagFilePath
    fi
}


# Updates and changes the files if the flag file exits, if and only if we are on the 'develop'
# branch.
# '-C HEAD' do not prompt for a commit message, use the HEAD as commit message.
# '--no-verify' do not call the pre-commit hook to avoid infinity loop.
if [ -f $updateFlagFilePath ]
then
    if [[ $currentBranch == "develop" ]]
    then
        if sh $updateVersionProgram build
        then
            echo "Successfully ran '$updateVersionProgram'."
        else
            echo "Could not run the update program '$updateVersionProgram' properly!"
            cleanUpdateFlagFile
            exit 1
        fi
        echo "Amending commits..."
        git commit --amend -C HEAD --no-verify
    else
        echo "It is not time to amend, as we are not on the 'develop' branch."
    fi
else
    echo "It is not time to amend, as the file '$updateFlagFilePath' does not exist."
fi


# To clean any old missed file
cleanUpdateFlagFile


# Exits the program using a successful exit status code.
exit 0





