'
'  Make Notepad++ the Default TXT Editor
'  http://docs.notepad-plus-plus.org/index.php?title=Replacing_Notepad
'
'  Replacing Notepad with Notepad++ using Image File Execution Options
'  https://www.cult-of-tech.net/2011/10/replacing-notepad-with-notepad-using-image-file-execution-options/
'
' This program is free software; you can redistribute it and/or modify it
' under the terms of the GNU General Public License as published by the
' Free Software Foundation; either version 3 of the License, or ( at
' your option ) any later version.
'
' This program is distributed in the hope that it will be useful, but
' WITHOUT ANY WARRANTY; without even the implied warranty of
' MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
' General Public License for more details.
'
' You should have received a copy of the GNU General Public License
' along with this program.  If not, see <http://www.gnu.org/licenses/>.
'
' DISCLAIMER
' THIS COMES WITH NO WARRANTY, IMPLIED OR OTHERWISE. USE AT YOUR OWN RISK
' IF YOU ARE NOT COMFORTABLE EDITING THE REGISTRY THEN DO NOT USE THIS SCRIPT
'
' NOTES:
' This affects all users.
' This will prevent ANY executable named notepad.exe from running located anywhere on this computer!!
'
' Save this text to your notepad++ folder as a text file named npp.vbs (some AV don't like vbs, get a different AV :-P )
'
' USAGE
' 1)
' Navigate to registry key HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Image File Execution Options\
'
' 2)
' Add new subkey called notepad.exe
' This step is what tells windows to use the notepad++ exe, to undo simply delete this key
'
' 3)
' Create new Sting Value called Debugger
'
' 4)
' Modify value and enter wscript.exe "path to npp.vbs" e.g. wscript.exe "C:\Program Files\Notepad++\npp.vbs" "notepad++.exe"
'

Option Explicit

Dim sCmd
Dim index
Dim oShell

' The first command line will the the program name to run
sCmd = """" & LeftB(WScript.ScriptFullName, LenB(WScript.ScriptFullName) - LenB(WScript.ScriptName)) & WScript.Arguments(0) & """ -n """

' The `Image File Execution Options`, sends each command line's path as a separate command line
' argument to the VBScript. Hence here we gather them all together as one again.
'
' The command line argument `index 1` is the original program's path, which we do not need here,
' therefore we start taking the arguments we need which start at the `index 2`.
'
For index = 2 To WScript.Arguments.Count - 1
   sCmd = sCmd & WScript.Arguments(index) & " "
Next

' Wscript.Echo "WScript.Arguments(0): " & WScript.Arguments(0)
sCmd = Trim(sCmd) & """"

' Wscript.Echo "sCmd: " & sCmd
Set oShell = CreateObject("WScript.Shell")

' Is there a way to start a program minimized with VBScript using WScript.Shell?
' https://stackoverflow.com/questions/13792429/is-there-a-way-to-start-a-program-minimized-with-vbscript-using-wscript-shell
oShell.Run sCmd, 3, True

' How can I maximize, restore, or minimize a window with a vb script?
' https://stackoverflow.com/questions/3824284/how-can-i-maximize-restore-or-minimize-a-window-with-a-vb-script
oShell.SendKeys "% x"
WScript.Quit




