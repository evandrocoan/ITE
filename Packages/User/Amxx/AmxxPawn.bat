

@echo off

:: AMXX Plugin Compiler Script
::
::  This program is free software; you can redistribute it and/or modify it
::  under the terms of the GNU General Public License as published by the
::  Free Software Foundation; either version 2 of the License, or ( at
::  your option ) any later version.
::
::  This program is distributed in the hope that it will be useful, but
::  WITHOUT ANY WARRANTY; without even the implied warranty of
::  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
::  See the GNU General Public License for more details.
::
::  You should have received a copy of the GNU General Public License
::  along with this program.  If not, see <http://www.gnu.org/licenses/>.
::


:: Get the current date to the variable CURRENT_DATE
for /f %%i in ('date /T') do set CURRENT_DATE=%%i

:: The format of %TIME% is HH:MM:SS,CS for example 23:59:59,99
echo.
echo Compiling %2... Current time is: %TIME% - %CURRENT_DATE%
echo.

:: Put here the paths to the folders where do you want to install the plugin.
:: You must to provide at least one folder.
set folders_list[0]=F:\SteamCMD\steamapps\common\Half-Life\czero\addons\amxmodx\plugins

:: Where is your compiler?
::
:: Example:
:: F:\SteamCMD\steamapps\common\Half-Life\czero\addons\amxmodx\scripting\amxxpc.exe
::
set AMXX_COMPILER_PATH=F:\SteamCMD\steamapps\common\Half-Life\czero\addons\amxmodx\scripting\amxxpc.exe





::
:: Setup the time calculation script
::
:: Time calculation downloaded from:
:: http://stackoverflow.com/questions/9922498/calculate-time-difference-in-windows-batch-file
::
:: AMX Mod X compiling batch downloaded from:
:: https://github.com/alliedmodders/amxmodx/pull/212/commits

:: Here begins the command you want to measure
for /F "tokens=1-4 delims=:.," %%a in ("%time%") do (
   set /A "start=(((%%a*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100"
)


::
:: Setup the batch variables
::
:: $1 is the first shell argument and $2 is the second shell argument passed by AmxxPawn.sublime-build
:: Usually they should be the plugin's file full path and the plugin's file name without extension.
::
:: Example: $1=F:\SteamCMD\steamapps\common\Half-Life\czero\addons\my_plugin.sma
set PLUGIN_SOURCE_CODE_FILE_PATH=%1

:: Removing double quotes from variables in batch file creates problems with CMD environment
:: https://stackoverflow.com/questions/1964192/removing-double-quotes-from-variables-in-batch-file-creates-problems-with-cmd-en
set PLUGIN_SOURCE_CODE_FILE_PATH=%PLUGIN_SOURCE_CODE_FILE_PATH:"=%

:: $4 is the path of the folder where the plugin source code is.
:: Example F:\SteamCMD\steamapps\common\Half-Life\czero\addons\
set SOURCE_CODE_INCLUDE_FOLDER=%4\include
set SOURCE_CODE_INCLUDE_FOLDER=%SOURCE_CODE_INCLUDE_FOLDER:"=%

:: Example: $2="my_plugin"
set PLUGIN_BASE_FILE_NAME=%2
set PLUGIN_BASE_FILE_NAME=%PLUGIN_BASE_FILE_NAME:"=%
set PLUGIN_BINARY_FILE_PATH=%folders_list[0]%\%PLUGIN_BASE_FILE_NAME%.amxx

IF "%PLUGIN_BASE_FILE_NAME%"=="" echo You must to save the plugin before to compile it. & goto end


::
:: Copy the include files to the compiler include files, if they exist.
::
setlocal enabledelayedexpansion enableextensions

:: See: http://stackoverflow.com/questions/659647/how-to-get-folder-path-from-file-path-with-cmd
:: set AMXX_COMPILER_PATH=C:\Somewhere\Somewhere\SomeFile.txt
call :path_from_file_name AMXX_COMPILER_FOLDER !AMXX_COMPILER_PATH!

:: Build the compiler include folder path
set COMPILER_INCLUDE_FOLDER_PATH=%AMXX_COMPILER_FOLDER%include

:: Check for cyclic copies and skip copying the include folder.
:: echo $COMPILER_INCLUDE_FOLDER_PATH: %COMPILER_INCLUDE_FOLDER_PATH%
:: echo $SOURCE_CODE_INCLUDE_FOLDER:   %SOURCE_CODE_INCLUDE_FOLDER%
for %%A in ("%COMPILER_INCLUDE_FOLDER_PATH%") do for %%B in ("%SOURCE_CODE_INCLUDE_FOLDER%") do if "%%~fA"=="%%~fB" echo Skipping copy include files... & goto compile_the_plugin

:: Copy the include folder
:: https://stackoverflow.com/questions/3018289/xcopy-file-rename-suppress-does-xxx-specify-a-file-name-message
IF EXIST "%SOURCE_CODE_INCLUDE_FOLDER%" call echo d | xcopy /S /Y "%SOURCE_CODE_INCLUDE_FOLDER%" "%COMPILER_INCLUDE_FOLDER_PATH%" > nul

:: Closes the `enabledelayedexpansion` scope
endlocal


::
:: Compile the AMXX plugin
:compile_the_plugin

:: Delete the old binary in case some crazy problem on the compiler, or in the system while copy it.
:: So, this way there is not way you are going to use the wrong version of the plugin without knowing it.
IF EXIST "%PLUGIN_BINARY_FILE_PATH%" del "%PLUGIN_BINARY_FILE_PATH%"

:: To call the compiler to compile the plugin to the output folder $PLUGIN_BINARY_FILE_PATH
"%AMXX_COMPILER_PATH%" -i"%SOURCE_CODE_INCLUDE_FOLDER%/" -o"%PLUGIN_BINARY_FILE_PATH%" "%PLUGIN_SOURCE_CODE_FILE_PATH%"

:: If there was a compilation error, there is nothing more to be done.
IF NOT EXIST "%PLUGIN_BINARY_FILE_PATH%" echo There was an compilation error. Exiting... & goto end


::
:: Copy the compiled plugin to the game folder(s)
::
echo.
echo 1 File(s) copied, to the folder %folders_list[0]%

:: Initial array index to loop into.
set "currentIndex=1"

:: Loop throw all games to install the new files.
:SymLoop
if defined folders_list[%currentIndex%] (

    :: Some how the AMXX compiler could not compiling/copied some times, so let us know when it does not.
    setlocal EnableDelayedExpansion

    :: Try to delete the file only if it exists
    IF EXIST "!folders_list[%currentIndex%]!\%PLUGIN_BASE_FILE_NAME%.amxx" del "!folders_list[%currentIndex%]!\%PLUGIN_BASE_FILE_NAME%.amxx"

    :: To do the actual copying/installing.
    for /f "delims=" %%a in ( 'xcopy /S /Y "%PLUGIN_BINARY_FILE_PATH%"^
            "!folders_list[%currentIndex%]!"^|find /v "%PLUGIN_BASE_FILE_NAME%"' ) do echo %%a, to the folder !folders_list[%currentIndex%]!

    :: Update the next 'for/array' index to copy/install.
    set /a "currentIndex+=1"

    goto :SymLoop
)


::
:: Subroutines/Function calls
::
goto :end

:: Copy the include files to the compiler include files, if they exist.
setlocal enabledelayedexpansion enableextensions

:: This one must to be on the `enabledelayedexpansion` range
:path_from_file_name <resultVar> <pathVar>
(
    set "%~1=%~dp2"
    exit /b
)

:: Closes the `enabledelayedexpansion` scope
endlocal


::
:: The end of the compilation
::
:end

:: Calculating the duration is easy
for /F "tokens=1-4 delims=:.," %%a in ("%time%") do (
   set /A "end=(((%%a*60)+1%%b %% 100)*60+1%%c %% 100)*100+1%%d %% 100"
)

:: Get elapsed time
set /A elapsed=end-start

:: Show elapsed time:
set /A hh=elapsed/(60*60*100), rest=elapsed%%(60*60*100), mm=rest/(60*100), rest%%=60*100, ss=rest/100, cc=rest%%100
if %mm% lss 10 set mm=0%mm%
if %ss% lss 10 set ss=0%ss%
if %cc% lss 10 set cc=0%cc%

:: Outputting
echo.
echo Took %hh%:%mm%:%ss%,%cc% seconds to run this script.

:: Pause the script for result reading, when it is run without any command line parameters
echo.
if "%PLUGIN_SOURCE_CODE_FILE_PATH%"=="" pause



