# My Sublime Text 3 Settings

This are my sublime settings/packages used to program on:

1. Java
2. Octave/Matlab
3. C/C++
4. Pawn



___
## Installation

1) Open the Sublime Text.

2) Install package manager [https://packagecontrol.io/installation](https://packagecontrol.io/installation):
```
import urllib.request,os,hashlib;

h   = '2915d1851351e5ee549c20394736b442' + '8bc59f460fa1548d1514676163dafc88';
pf  = 'Package Control.sublime-package';
ipp = sublime.installed_packages_path();

urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) );
by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read();

dh hashlib.sha256(by).hexdigest();
print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```

3) Close your Sublime Text and delete the folder below:
```
~/.config/sublime-text-3/Packages/User
```

4) While keeping your Sublime Text closed, clone this repository using this command:
```
git clone --recursive https://github.com/evandrocoan/MySublimeSettings.git ~/.config/sublime-text-3/Packages/User
```

5) Open your Sublime Text and wait several minutes until it install all new packages.


___
## Notes

If you are using the portable version, delete the folder:
```
$SUBLIME_ROOT_FOLDER/Data/Packages/User
```
And clone it with:
```
git clone --recursive https://github.com/evandrocoan/MySublimeSettings.git $SUBLIME_ROOT_FOLDER/Data/Packages/User
```

1. You can open the Console on View -> Console (Ctrl+`).
1. If you are a Windows user, just figure out where are your settings folders.
1. The packages will be automatically installed on the first run after the repository clone.











