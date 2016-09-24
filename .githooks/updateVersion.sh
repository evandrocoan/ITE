#!/usr/bin/env bash


#
# This file must be ran from the main repository folder. It updates the software version number
# indicated at "filePathToUpdate" and "versionFilePath". The versions at these two files must to be
# synchronized for a correct version update. 
#
# You can also update the version manually, but you must to update both files: "./.githooks/VERSION.txt"
# and "./scripting/galileo.sma" using the same version number.
#
# Program usage: updateVersion [major | minor | patch | build]
# Example: ./updateVersion build
#
#
# Change log:
# 
# v1.1.2
# Added error message when the 'sed' operation fails.
# 
# v1.1.1
# Placed this file within the repository sub-folder "./.githooks".
#
# v1.1
#  Implemented build incrementing number.
#  Created variables to hold the used files names.
#  Added file search and replace to update the version numbers.
#
# v1.0
#  Downloaded from: https://github.com/cloudfoundry/cli/blob/master/bin/bump-version
#
#



GIT_DIR_="$(git rev-parse --git-dir)"
githooksConfig=$(cat $GIT_DIR_/../.githooks/githooksConfig.txt)

# $versionFilePath example: .githooks/GALILEO_SMA_VERSION.txt
versionFilePath=$GIT_DIR_/../$(echo $githooksConfig | cut -d',' -f 1)

# $filePathToUpdate example: scripting/galileo.sma
filePathToUpdate=$GIT_DIR_/../$(echo $githooksConfig | cut -d',' -f 2)

currentVersion=$(cat $versionFilePath)
originalVersion=$currentVersion

component=$1


# 'cut' Print selected parts of lines from each FILE to standard output
# 
# '-d' use another delimiter instead of TAB for field delimiter.
# '-f' select only these fields.
#
major=$(echo $currentVersion | cut -d'.' -f 1)
minor=$(echo $currentVersion | cut -d'.' -f 2)
patch=$(echo $currentVersion | cut -d'.' -f 3 | cut -d'-' -f 1)
build=$(echo $currentVersion | cut -d'-' -f 2)


if [ -z "${major}" ] || [ -z "${minor}" ] || [ -z "${patch}" ] || [ -z "${build}" ]
then
    echo "VAR <$major>.<$minor>.<$patch>-<$build> is bad set or set to the empty string"
    exit 1
fi


case "$component" in
    major )
        major=$(expr $major + 1)
        minor=0
        patch=0
        ;;
        
    minor )
        minor=$(expr $minor + 1)
        patch=0
        ;;
        
    patch )
        patch=$(expr $patch + 1)
        ;;
        
    build )
        build=$(expr $build + 1)
        ;;
        
    * )
        echo "Error - argument must be 'major', 'minor', 'patch' or 'build'"
        echo "Usage: updateVersion [major | minor | patch | build]"
        exit 1
        ;;
esac


currentVersion=$major.$minor.$patch-$build


# To prints a error message when it does not find the version number on the file.
#
# 'F' affects how PATTERN is interpreted (fixed string instead of a regex).
# 'q' shhhhh... minimal printing.
#
if ! grep -Fq "v$originalVersion" "$filePathToUpdate"
then
    echo "Error! Could not find v$originalVersion and update the file '$filePathToUpdate'."
    echo "The current version number on this file must be v$originalVersion!"
    echo "Or fix the file '$versionFilePath' to the correct value."
    exit 1
fi


if sed -i -- "s/v$originalVersion/v$currentVersion/g" $filePathToUpdate
then
    echo "Replacing the version v$originalVersion -> v$currentVersion in '$filePathToUpdate'"
    
    # Replace the file with the $versionFilePath with the $currentVersion.
    echo $currentVersion > $versionFilePath
else
    echo "ERROR! Could not replace the version v$originalVersion -> v$currentVersion in '$filePathToUpdate'"
    exit 1
fi


# To add the recent updated files to the commit
echo "Staging '$versionFilePath' and '$filePathToUpdate'..."
git add $versionFilePath
git add $filePathToUpdate


# Exits the program using a successful exit status code.
exit 0


