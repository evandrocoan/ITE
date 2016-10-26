# Sublime Text Studio

An incredible set of settings/packages/shortcuts for Sublime Text 3. Currently it is optimized
to program on:

1. Java
2. Octave/Matlab
3. C/C++
4. Pawn
5. SQL


Its current version is: v1.0.1-67



___
## Descriptions

See its main post at the AlliedModders' Forum: [Versioned Sublime Text Settings](https://forums.alliedmods.net/showthread.php?p=2454292#post2454292)



___
## Installation

1) Install `Sublime Text` from [https://www.sublimetext.com/3](https://www.sublimetext.com/3)

2) Close your Sublime Text and delete/rename the folder below, if it exists: (the folder `sublime-text-3/` below contain all your current settings)
```
mv -v ~/.config/sublime-text-3/ ~/.config/sublime-text-3_Old/
```

3) While keeping your Sublime Text closed, clone this repository using this command: (Linux Only)
```
git clone --recursive https://github.com/evandrocoan/SublimeTextStudio.git ~/.config/sublime-text-3/Packages
```

 * The packages will be automatically installed on the first `Sublime Text` run after the repository clone.

 * If you are a Windows/Mac user, just figure out where are your settings folders: (the folder `Sublime Text 3\` below contain all your current settings)
```
~/.config/sublime-text-3/ --> "C:\Users\YOUR_USER_NAME\AppData\Roaming\Sublime Text 3\"
~/.config/sublime-text-3/ --> "~/Library/Application Support/Sublime Text 3"
```

4) Open your Sublime Text and wait several minutes until it install all new packages and restart your Sublime Text.

5) You can open the Console on View -> Console (Ctrl+`) to view the download progress.



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





