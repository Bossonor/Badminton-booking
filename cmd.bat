@echo off
set n=12
:name
if %n%==0 exit
start python gui.py %n%
TIMEOUT /T 10
set /a n-=1
goto name