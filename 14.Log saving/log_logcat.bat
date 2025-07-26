@echo off
:: Get current date and time in a safe format
for /f "tokens=1-4 delims=/ " %%a in ('date /t') do (
    set mydate=%%d-%%b-%%c
)
for /f "tokens=1-2 delims=: " %%a in ('time /t') do (
    set mytime=%%a-%%b
)

:: Remove AM/PM if present
set mytime=%mytime: =%

:: Create timestamp
set timestamp=%mydate%_%mytime%
set timestamp=%timestamp::=-%

:: Set filename
set filename=Logcat_%timestamp%.txt

:: Save logcat output
adb logcat -d > "%filename%"

echo Logcat saved as %filename%
pause
