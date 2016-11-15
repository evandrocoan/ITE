# Git Hooks

This folder contains the git hooks used the by this project. 
To install them, just copy the files "post-checkout", "post-commit"
and "prepare-commit-msg" to "$THIS_REPOSITORY_DIR/.git/hooks/", 
or run the installer `install_githooks.sh`.


Open the file "githooksConfig.txt" to configure the files to be
used and updated when the program "./updateVersion.sh" to run.


Program usage: 
```
./updateVersion.sh [major | minor | patch | build]
```
Example:

1. `./updateVersion` to show help.
1. `./updateVersion build` to increment the build number.


### Installing

To install this automated versioning script, you need to:

1. Fork this repository on yours git repository main's root folder.
1. Run the script `updateVersion.sh` and read the instructions.

For automated versioning when committing:

1. Run the `git hooks` installer script `install_githooks.sh`.
1. Re-run the installer `install_githooks.sh` every time you rename the folder where repository
is forked into.



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




