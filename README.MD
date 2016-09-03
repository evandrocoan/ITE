# Sublime Text Studio

These are my sublime settings/packages used to program on:

1. Java
2. Octave/Matlab
3. C/C++
4. Pawn



___
## Installation

1) Open the Sublime Text, after install it from [https://www.sublimetext.com/download](https://www.sublimetext.com/3)

2) Install package manager [https://packagecontrol.io/installation](https://packagecontrol.io/installation):
`
import urllib.request,os,hashlib; h = '2915d1851351e5ee549c20394736b442' + '8bc59f460fa1548d1514676163dafc88'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
`

3) Close your Sublime Text and rename the folder below: (the folder `Packages/User` below contain all your current settings)
```
mv -v ~/.config/sublime-text-3/Packages ~/.config/sublime-text-3/Packages_Old
```

4) While keeping your Sublime Text closed, clone this repository using this command:
```
git clone --recursive https://github.com/evandrocoan/SublimeTextStudio.git ~/.config/sublime-text-3/Packages
```

5) Open your Sublime Text and wait several minutes until it install all new packages and restart your Sublime Text.



___
## Notes

If you are using the portable version (Linux/Windows/Mac), delete the folder:
```
$SUBLIME_ROOT_FOLDER/Data/Packages/User
```
And clone it with:
```
git clone --recursive https://github.com/evandrocoan/SublimeTextStudio.git $SUBLIME_ROOT_FOLDER/Data/Packages
```

1. You can open the Console on View -> Console (Ctrl+`).
1. The packages will be automatically installed on the first run after the repository clone.
1. If you are a Windows user, just figure out where are your settings folders.

```
~/.config/sublime-text-3/Packages --> "C:\Users\YOUR_USER_NAME\AppData\Roaming\Sublime Text 3\Packages"
```



___
## Debugging

Use on the console:
```
sublime.log_commands(True)
sublime.log_input(True)
```



___
## Licence
All files in this repository are released under GNU General Public License v3.0, unless stated otherwise.
See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.en.html) file for more information.



___
## TODO
Remove all settings from the user files, and added them to the default settings well documented.


1. Go to: `Preferences -> Pacakge Settings -> Gist -> Settings - Default`
  Copy its contents and go to: `Preferences -> Pacakge Settings -> Gist -> Settings - User`
  Then read the instructions on `// Your GitHub API token`






