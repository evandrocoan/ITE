Git Hooks
=============================

This folder contains the git hooks used the by this project. 
To install them, just copy the files "post-checkout", "post-commit"
and "prepare-commit-msg" to "$THIS_REPOSITORY_DIR/.git/hooks/".


Open the file ".githooks/githooksConfig.txt" to configure the files to be
used and updated when the program "./.githooks/updateVersion.sh" to run.


Program usage: 
```
./.githooks/updateVersion [major | minor | patch | build]
```
Example: ./.githooks/updateVersion build


Note: The program "./.githooks/updateVersion.sh" must to be run from
the main repository folder "$THIS_REPOSITORY_DIR". See its documentation
reading its file ".githooks/updateVersion.sh".



##### Learn more about git hooks on the following links:

1. https://git-scm.com/docs/githooks
2. https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks




