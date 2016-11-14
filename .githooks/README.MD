# Git Hooks

This folder contains the git hooks used the by this project. 
To install them, just copy the files "post-checkout", "post-commit"
and "prepare-commit-msg" to "$THIS_REPOSITORY_DIR/.git/hooks/", 
or run the installer `install_githooks.sh`.


Open the file ".githooks/githooksConfig.txt" to configure the files to be
used and updated when the program "./.githooks/updateVersion.sh" to run.


Program usage: 
```
./.githooks/updateVersion [major | minor | patch | build]
```
Example:

1. `./.githooks/updateVersion` to show help.
1. `./.githooks/updateVersion build` to increment the build number.


Note: The program "./.githooks/updateVersion.sh" must to be run from
the main repository folder "$THIS_REPOSITORY_DIR". See its documentation
reading its file ".githooks/updateVersion.sh".



#### Semantic Versioning 2.0.0

Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
1. MINOR version when you add functionality in a backwards-compatible manner, and
1. PATCH version when you make backwards-compatible bug fixes.

Additional labels for pre-release and build metadata are available as extensions to the
MAJOR.MINOR.PATCH format.

http://semver.org/



##### Learn more about git hooks on the following links:

1. https://git-scm.com/docs/githooks
2. https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks




