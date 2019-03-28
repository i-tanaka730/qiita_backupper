# -*- coding: utf-8 -*-

import json
import os
import sys
import requests
import re
import urllib.request
import urllib.parse

# フォーマットチェック
def check_format():
    if FORMAT not in ['all', 'md', 'html']:
        print('Error : Please check the output format.')
        sys.exit(1)

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

    if FORMAT in ['all', 'md']:
        save_markdown(title, body)

    if FORMAT in ['all', 'html']:
        save_html(title, body)

    print ('[OK!] ' + title)

# ファイル名に使用できない文字を除外
def exclude_unavailable_filename(name):
    return re.sub(r'[\\|/|:|?|.|"|<|>|\|]', '', name)

# markdown形式で保存
def save_markdown(title, body):
    filename = '{0}.md'.format(title)
    filepath = os.path.join(BUCKUP_DIR, filename)

    with open(filepath, 'wb') as file:
        file.write(body)

# html形式で保存
def save_html(title, body):
    filename = '{0}.html'.format(title)
    filepath = os.path.join(BUCKUP_DIR, filename)

    request = urllib.request.Request(HTML_CONVERT_URL)
    request.add_header('Content-Type', 'text/plain')
    f = urllib.request.urlopen(request, body)

    with open(filepath,'bw') as file:
        file.write(f.read())


ACCOUNT = sys.argv[1]
FORMAT = sys.argv[2]
# バックアップするQiitaアカウントのURL
QIITA_ACCOUNT_URL = 'https://qiita.com/api/v2/users/' + ACCOUNT + '/items'
# バックアップ件数
QIITA_PARAMS = {
    'page'     : 1,
    'per_page' : 100,
}
# バックアップ先のフォルダのパス
BUCKUP_DIR = os.path.abspath(os.path.dirname(__file__)) + '/backup'
# markdownをhtmlに変換するGitHubApiのURL
HTML_CONVERT_URL = 'https://api.github.com/markdown/raw'

check_format()
response = requests.get(QIITA_ACCOUNT_URL, params=QIITA_PARAMS)
check_response(response)
make_backup_dir()
items = response.json()
for item in items:
    save(item)
