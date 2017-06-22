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
## Installation for Linux/Max OS

Requirements for `Linux` systems are:

1. A shell terminal/command line available
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

1. Open `Sublime Text`
1. Go to the menu: `Preferences -> Browse Packages...`. It should open your `Sublie Text` **Packages** folder:
![](http://i.imgur.com/VA4zC7F.gif)
1. Then open `a shell command line` on this folder.
1. Now close `Sublime Text` and run these commands:
```
# This is the folder where all your `Sublime Text` settings/data is on.
#
# * If you are running the portable version of `Sublime Text`, replace `sublime-text-3` by `Data`
# * If you are a Mac OS User, replace `sublime-text-3` by `Sublime Text 3`
#
sublime_text_folder="sublime-text-3"

# Backup your settings and files, assuming the current folder is `Packages`
cd ../..
mv ./$sublime_text_folder/ ./"$sublime_text_folder"_backup_$(date '+%Y%m%d%H%M%S')/
mkdir ./$sublime_text_folder
cd ./$sublime_text_folder

# Download the required files
git clone https://github.com/evandrocoan/Packages
git clone --recursive -j8 https://github.com/evandrocoan/SublimeTextStudio

# Configure the environment
mkdir -p ./Packages
shopt -s dotglob
git submodule foreach git checkout master

# To install the files
mv ./SublimeTextStudio/Packages/* ./Packages
rsync -a ./SublimeTextStudio/ ./
rm -r -f ./SublimeTextStudio

# Success
printf "Success\\!\n"
```

After finish running all these commands, open `Sublime Text` and wait until the `Packages Control`
install all the packages:

* It should take some minutes until install all new packages, after that restart your `Sublime Text`.
* You can open the Console on `View -> Console (Ctrl+`) to view the download progress.
* This is a sample output of the full process on the command line: [Linux Command line output](https://gist.github.com/evandrocoan/60a1303ef5c0a6cb40c064ff27563020)




___
## Installation for Windows

Requirements for `Windows` systems are:

1. An command line available
1. Install `git` (https://git-scm.com/)
1. Install `Sublime Text` (https://www.sublimetext.com/)



#### Steps

1. Open `Sublime Text`
1. Go to the menu: `Preferences -> Browse Packages...`. It should open your `Sublie Text` **Packages** folder:
![](http://i.imgur.com/iYwE4IO.gif)
1. Then open `a command line` on this folder.
1. Run the command line `cmd /open`
1. Now close the Windows Explorer opened on the Packages folder.
1. And also close `Sublime Text` and run these commands bellow:
```
:: This is the folder where all your `Sublime Text` settings/data is on.
:: * If you are running the portable version of `Sublime Text`, replace `Sublime Text 3` by `Data`
::
set sublime_text_folder=Sublime Text 3

:: Backup your settings and files, assuming the current folder is `Packages`
cd ..\..
set "pp=%%"
for /f "delims=" %pp:~-1%a in ('wmic OS Get localdatetime  ^| find "."') do set dt=%pp:~-1%a
rename "%sublime_text_folder%" "%sublime_text_folder% Backup %dt:~8,2%-%dt:~10,2%-%dt:~12,2%"
mkdir "%sublime_text_folder%"
cd .\%sublime_text_folder%

:: Download the required files
git clone https://github.com/evandrocoan/Packages
git clone --recursive -j8 https://github.com/evandrocoan/SublimeTextStudio

:: Configure the environment
mkdir Packages
git submodule foreach git checkout master

:: To install the files
robocopy /move /e .\SublimeTextStudio\Packages\ .\Packages\ /NFL /NDL /nc /ns
robocopy /move /e .\SublimeTextStudio\ .\ /NFL /NDL /NJH /NJS /nc /ns /np

:: Success
echo "Success\\!\n"
```

After finish running all these commands, open `Sublime Text` and wait until the `Packages Control`
install all the packages:

* It should take some minutes until install all new packages, after that restart your `Sublime Text`.
* You can open the Console on `View -> Console (Ctrl+') to view the download progress.
* You can also see this *old video* tutorial [How to the Install Sublime Studio](https://vid.me/ODYj).
* This is a sample output of the full process on the command line: [Windows Command line output](https://gist.github.com/evandrocoan/a2e69c01e1f2721e6772b73fff88ff3c)




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





