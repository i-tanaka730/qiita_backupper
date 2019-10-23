# qiita_backupper

## Overview

It is a tool to back up the article of the specified account.

## Requirement

- Python3.X
- Requests (Python libraries)
```sh
pip install requests
```

## Usage(Windows)

#### 1. Git clone
```sh
git clone https://github.com/i-tanaka730/qiita_backupper
```

#### 2. Edit backup.bat
Please edit ACCOUNT and FORMAT.
```sh
@echo off

rem Qiita account name
set ACCOUNT=i-tanaka730

rem Output format (all / md / html)
set FORMAT=md

python qiita_backupper.py %ACCOUNT% %FORMAT%
pause
```

#### 3. Run backup.bat
```sh
backup.bat
[OK!] AAAAA
[OK!] BBBBB
[OK!] CCCCC
```

## Usage(macOS, Linux)

#### 1. Git clone
```sh
git clone https://github.com/i-tanaka730/qiita_backupper
```

#### 2. Run bachup.sh
```sh
$ ./backup.sh $ACCOUNT_NAME $FORMAT
[OK!] AAAAA
[OK!] BBBBB
[OK!] CCCCC
```

|Arguments|Details|
|:---:|:---|
|$USER_NAME|Your account neme of Qiita|
|$FORMAT|all / md / html|

## License
[MIT](https://github.com/i-tanaka730/qiita_backupper/blob/master/LICENSE)

## Author
[Ikuya Tanaka](https://github.com/i-tanaka730)
