#!/usr/bin/env bash

githooksPath="../.git/hooks/"

printf "Installing the githooks...\n"
cp -v post-checkout $githooksPath
cp -v post-commit $githooksPath
cp -v prepare-commit-msg $githooksPath

printf "The githooks are successfully installed!\n"
