# -*- coding: utf-8 -*-

import json
import os
import sys
import requests
import re

# レスポンスチェック
def check_response(response):
    try:
        response.raise_for_status()
    except Exception as exc:
        print('Error : {}'.format(exc))
        sys.exit(1)

# バックアップフォルダ作成
def make_backup_dir():
    if not os.path.isdir(BUCKUP_DIR):
        os.mkdir(BUCKUP_DIR)

# 保存
def save(item):
    title = exclude_unavailable_filename(item["title"])
    body  = item['body'].encode('utf-8')
    filename = '{0}.md'.format(title)
    fullpath = os.path.join(BUCKUP_DIR, filename)

    with open(fullpath, 'wb') as f:
        f.write(body)

    print ('[OK!] ' + filename)

# ファイル名に使用できない文字を除外
def exclude_unavailable_filename(name):
    return re.sub(r'[\\|/|:|?|.|"|<|>|\|]', '', name)

# バックアップするQiitaアカウントのURL
URL = 'https://qiita.com/api/v2/users/' + sys.argv[1] + '/items'
# バックアップ先のフォルダのパス
BUCKUP_DIR = os.path.abspath(os.path.dirname(__file__)) + '/backup'

response = requests.get(URL)
check_response(response)
make_backup_dir()
items = response.json()
for item in items:
    save(item)
