@echo off
set /P ACCOUNT="バックアップ対象のQiitaアカウント名を入力してください: "
python qiita_backupper.py %ACCOUNT%
pause
