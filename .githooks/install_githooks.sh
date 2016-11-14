#!/usr/bin/env bash

githooksPath="../.git/hooks/"

if [ -d $githooksPath ]
then
    printf "Installing the githooks...\n\n"

    # Get the `AUTO_VERSIONING_ROOT_FOLDER_NAME`, i.e., the current folder name.
    AUTO_VERSIONING_ROOT_FOLDER_NAME=$(echo "${PWD##*/}")

    # Write specify the githooks' root folder
    echo "$AUTO_VERSIONING_ROOT_FOLDER_NAME" > $githooksPath/gitHooksRoot.txt

    cp -v post-checkout $githooksPath
    cp -v post-commit $githooksPath
    cp -v prepare-commit-msg $githooksPath

    printf "\nThe githooks are successfully installed!\n"
else
    printf "Error! Could not to install the githooks.\n"
    printf "The folder \`$githooksPath\` is missing. Are you using this as a sub-module?\n\n"
    printf "If so, then to install the files manually coping and pasting the following files:\n"
    printf "\`post-checkout\`\n"
    printf "\`post-commit\`\n"
    printf "\`prepare-commit-msg\`\n\n"
    printf "To the folder: ./git/modules/\$THIS_MODULE_NAME\n\n"
fi




