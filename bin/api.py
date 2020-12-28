# api.py
#
# This file runs in Python 3
#

import os
import time
import json
import requests

def getAPI(lang) -> None:
    global API_path
    API_path = './apidoc/MRT_%s_API.json'%lang
    if os.path.exists(API_path) and time.time() - os.stat(API_path).st_mtime < 2600000:
        return

    url = 'https://web.metro.taipei/apis/metrostationapi/menuline'
    respone = requests.post(url, data = {"LineID":"0","Lang":lang})
    jsondata = respone.json()

    with open(API_path, 'w', encoding = 'utf8') as jsonfile:
        json.dump(jsondata, jsonfile, ensure_ascii = False)


if __name__ == '__main__':
    getAPI('tw');
    getAPI('en');
