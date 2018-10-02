@echo off
set /P ACCOUNT="Please enter the Qiita account to be back up: "
python qiita_backupper.py %ACCOUNT%
pause
