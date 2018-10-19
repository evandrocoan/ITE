#!/usr/bin/env bash


# Unpack the default Sublime Text files non available on versioning system.
build=$1
sublime_text_builds="/cygdrive/d/User/Programs/SublimeText"

if [[ -z "$build" ]]
then
    printf "Error: The first parameter variable is empty.\n"
    printf "You need to pass the build folder.\n"
    exit 1
fi


sublime_text_git_versioning="$sublime_text_builds/GitVersioning"
sublime_text_currrent_build="$sublime_text_builds/$build"

if ! [ -d "$sublime_text_currrent_build" ]
then
    printf "Error: The sublime_text_builds: $sublime_text_currrent_build folder does not exists.\n"
    printf "You need to edit this script fixing its path.\n"
    exit 1
fi

if ! [ -d "$sublime_text_git_versioning" ]
then
    printf "Error: The sublime_text_git_versioning: $sublime_text_git_versioning folder does not exists.\n"
    printf "You need to edit this script fixing its path.\n"
    exit 1
fi


# How do I make rsync delete files that have been deleted from the source folder?
# https://askubuntu.com/questions/476041/how-do-i-make-rsync-delete-files-that-have-been-deleted-from-the-source-folder
#
# Prevent rsync from deleting destination files that match a given pattern
# https://stackoverflow.com/questions/19024532/prevent-rsync-from-deleting-destination-files-that-match-a-given-pattern
#
# How to exclude multiple directories with rsync?
# https://askubuntu.com/questions/320458/how-to-exclude-multiple-directories-with-rsync
printf "$(date)\nCoping files from build $build...\n"
rsync -r --delete "$sublime_text_currrent_build/" $sublime_text_git_versioning/ \
--exclude .git --exclude __pycache__ --exclude *.pyc --no-p --chmod=ugo=rwX \
--exclude "Packages/ActionScript.sublime-package" \
--exclude "Packages/AppleScript.sublime-package" \
--exclude "Packages/ASP.sublime-package" \
--exclude "Packages/Batch File.sublime-package" \
--exclude "Packages/C#.sublime-package" \
--exclude "Packages/C++.sublime-package" \
--exclude "Packages/Clojure.sublime-package" \
--exclude "Packages/Color Scheme - Default.sublime-package" \
--exclude "Packages/Color Scheme - Legacy.sublime-package" \
--exclude "Packages/CSS.sublime-package" \
--exclude "Packages/D.sublime-package" \
--exclude "Packages/Diff.sublime-package" \
--exclude "Packages/Erlang.sublime-package" \
--exclude "Packages/Go.sublime-package" \
--exclude "Packages/Graphviz.sublime-package" \
--exclude "Packages/Groovy.sublime-package" \
--exclude "Packages/Haskell.sublime-package" \
--exclude "Packages/HTML.sublime-package" \
--exclude "Packages/Java.sublime-package" \
--exclude "Packages/JavaScript.sublime-package" \
--exclude "Packages/Language - English.sublime-package" \
--exclude "Packages/LaTeX.sublime-package" \
--exclude "Packages/Lisp.sublime-package" \
--exclude "Packages/Lua.sublime-package" \
--exclude "Packages/Makefile.sublime-package" \
--exclude "Packages/Markdown.sublime-package" \
--exclude "Packages/Matlab.sublime-package" \
--exclude "Packages/Objective-C.sublime-package" \
--exclude "Packages/OCaml.sublime-package" \
--exclude "Packages/Pascal.sublime-package" \
--exclude "Packages/Perl.sublime-package" \
--exclude "Packages/PHP.sublime-package" \
--exclude "Packages/Python.sublime-package" \
--exclude "Packages/R.sublime-package" \
--exclude "Packages/Rails.sublime-package" \
--exclude "Packages/Regular Expressions.sublime-package" \
--exclude "Packages/RestructuredText.sublime-package" \
--exclude "Packages/Ruby.sublime-package" \
--exclude "Packages/Rust.sublime-package" \
--exclude "Packages/Scala.sublime-package" \
--exclude "Packages/ShellScript.sublime-package" \
--exclude "Packages/SQL.sublime-package" \
--exclude "Packages/TCL.sublime-package" \
--exclude "Packages/Text.sublime-package" \
--exclude "Packages/Textile.sublime-package" \
--exclude "Packages/Theme - Default.sublime-package" \
--exclude "Packages/Vintage.sublime-package" \
--exclude "Packages/XML.sublime-package" \
--exclude "Packages/YAML.sublime-package"

printf "Unpacking new files on $sublime_text_git_versioning...\n"
cd $sublime_text_git_versioning

# How to loop through a directory recursively to delete files with certain extensions
# https://stackoverflow.com/questions/4638874/how-to-loop-through-a-directory-recursively-to-delete-files-with-certain-extensi
shopt -s globstar

# Unzip All Files In A Directory
# https://stackoverflow.com/questions/2374772/unzip-all-files-in-a-directory
for zip_file_name in Packages/*.{zip,sublime\-package}; do
    directory_name=`echo $zip_file_name | sed 's/\.\(zip\|sublime\-package\)$//'`
    printf "Unpacking zip file \`$sublime_text_git_versioning/$zip_file_name\`...\n"

    if [ -f "$sublime_text_git_versioning/$zip_file_name" ]; then
        mkdir -p "$sublime_text_git_versioning/$directory_name"
        unzip -o -q "$sublime_text_git_versioning/$zip_file_name" -d "$directory_name"

        # Some files have the executable flag and were not being deleted because of it.
        chmod -x "$sublime_text_git_versioning/$zip_file_name"
        rm -f "$sublime_text_git_versioning/$zip_file_name"
    fi
done

git add -A
git commit -m "Added build $build"

