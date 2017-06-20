# Sublime Text Studio

An incredible set of settings/packages/shortcuts for Sublime Text 3. Currently it is optimized
to program on:

1. Java
1. C/C++
1. Octave/Matlab
1. Pawn
1. SQL
1. Markdown
1. BBCode
1. Shell Script
1. Windows Batch
1. LaTeX
1. CSS
1. Javascript


Its current version is: v1.0.1-481


#### Descriptions

See its main post at the AlliedModders' Forum: [Versioned Sublime Text Settings](https://forums.alliedmods.net/showthread.php?p=2454292#post2454292)




___
## Installation


### For Linux/Max OS

Requirements for `Linux` systems are:

1. An Unix shell terminal/command line available
1. Install `git` (https://git-scm.com/)
1. Install `rsync` (http://rsync.samba.org/)
1. Install `Sublime Text` (https://www.sublimetext.com/)

```
sudo apt-get update
sudo apt-get install git
sudo apt-get install rsync
sudo apt-get install sublime-text
printf "Success\!\n"
```


#### Steps

1. Open `Sublime Text`, and to go the menu: `Preferences -> Browse Packages...`.
It should open your `Sublie Text` **Packages** folder.
![](http://i.imgur.com/UIevtzm.gif)
1. Then open `a shell command line` on this folder.
1. Now close `Sublime Text` and run these commands:
```
# This is the folder where all your `Sublime Text` settings/data is on
sublime_text_folder=sublime-text-3

# Backup your settings and files, assuming the current folder is `Packages`
cd ../..
mv ./$sublime_text_folder/ ./'$sublime_text_folder'_backup/
mkdir ./$sublime_text_folder
cd ./$sublime_text_folder

# Download the required files
git clone https://github.com/evandrocoan/Packages
git clone --recursive https://github.com/evandrocoan/SublimeTextStudio

# Configure the environment
mkdir -p ./Packages
shopt -s dotglob

# To install the files
mv ./SublimeTextStudio/Packages/* ./Packages
rsync -a ./SublimeTextStudio/ ./
rm -r -f ./SublimeTextStudio

# Success
printf "Success\!\n"
```

After finish running all these commands, open `Sublime Text` and wait until the `Packages Control`
install all the packages:

* It should some minutes until install all new packages, after that restart your `Sublime Text`.
* You can open the Console on View -> Console (Ctrl+`) to view the download progress.



### Windows

Requirements for `Linux` systems are:

1. Install an Unix shell terminal
1. Install `rsync` from http://rsync.samba.org/
1. Install `Sublime Text` from https://www.sublimetext.com/

#### Steps




2) Close your `Sublime Text` and delete/rename the folder below, if it exists:
```

```
 * The folder `sublime-text-3/` above contain all your current settings


3) While keeping your `Sublime Text` closed, clone this repository using this command:
```
git clone --recursive https://github.com/evandrocoan/SublimeTextStudio.git ~/.config/sublime-text-3/Packages
```

 * The packages will be automatically installed on the first `Sublime Text` run after the repository clone.
 * If you are a Windows/Mac user, just figure out where are your settings folders:
```
~/.config/sublime-text-3/ --> "C:\Users\YOUR_USER_NAME\AppData\Roaming\Sublime Text 3\"
~/.config/sublime-text-3/ --> "~/Library/Application Support/Sublime Text 3"
```


4) Open your `Sublime Text` and wait several minutes until it install all new packages and restart your `Sublime Text`.


5) You can open the Console on View -> Console (Ctrl+`) to view the download progress.
 * It is not clear enough? See the video tutorial [How to the Install Sublime Studio](https://vid.me/ODYj).



___
## Notes

If you are using the portable version (Linux/Windows/Mac), delete/rename the folder `Data/`, if it exists: (the folder `Data/` below contain all your current settings)
```
rename $SUBLIME_ROOT_FOLDER/Data/ $SUBLIME_ROOT_FOLDER/Data_Old/
```
And clone it with: (remenber to replace the `\` with `/`, example, `D:\Sublime\Data` to `D:/Sublime/Data`)
```
git clone --recursive https://github.com/evandrocoan/SublimeTextStudio.git "SUBLIME_ROOT_FOLDER/Data/Packages"
```



___
## Debugging

Use on the console: (View -> Show Console)
```
sublime.log_input(True); sublime.log_commands(True); sublime.log_result_regex(True)
```
To disable it do:
```
sublime.log_input(False); sublime.log_commands(False); sublime.log_result_regex(False)
```



___
## Licence

All files in this repository are released under GNU General Public License v3.0, unless stated otherwise.
See:

1. The [LICENSE](LICENSE.TXT) file.
1. And the website [https://www.gnu.org/licenses/gpl-3.0.en.html](https://www.gnu.org/licenses/gpl-3.0.en.html).

For more information.





