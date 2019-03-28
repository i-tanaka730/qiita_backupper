@echo off

rem Qiita account name
set ACCOUNT=i-tanaka730

rem Output format (all / md / html)
set FORMAT=md

python qiita_backupper.py %ACCOUNT% %FORMAT%
pause
