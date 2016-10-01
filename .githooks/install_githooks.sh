#!/usr/bin/env bash

githooksPath="../.git/hooks/"

cp -v post-checkout $githooksPath
cp -v post-commit $githooksPath
cp -v prepare-commit-msg $githooksPath

