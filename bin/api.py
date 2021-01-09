# api.py
#
# This file runs in Python 3
#

import os
import time
import json
import requests



# "https://web.metro.taipei/apis/metrostationapi/menuline"
def getRouteAPI() -> None:
    API_path = './apidoc/MRTRouteAPI.json';
    API_path = '../apidoc/MRTRouteAPI.json';    # For Windows

    if os.path.exists(API_path) and time.time() - os.stat(API_path).st_mtime < 2600000: return

    url = 'https://web.metro.taipei/apis/metrostationapi/menuline'
    respone = requests.post(url, data = {"LineID":"0","Lang":lang})
    jsondata = respone.json()

    with open(API_path, 'w', encoding = 'utf8') as jsonfile:
        json.dump(jsondata, jsonfile, ensure_ascii = False)



# "https://data.taipei/api/getDatasetInfo/downloadResource?id=513e97fe-6a98-4a0d-b7dc-11122c8638d4&rid=c32998fa-c9b2-4324-9016-e19fbe0815f1"
def getTravalTimeAPI() -> None:
    pass;



# "https://data.taipei/api/getDatasetInfo/downloadResource?id=782c2b71-8f5a-4575-9bf2-e86999be2863&rid=14fd1af0-dc2b-4174-87d4-fcb9de783496"
def getInterchangeTimeAPI() -> None:
    pass;


# "https://data.taipei/api/getDatasetInfo/downloadResource?id=4acb4911-0360-4063-808d-fcee629508b3&rid=893c2f2a-dcfd-407b-b871-394a14105532"
def getPriceAPI() -> None:
    pass;



if __name__ == '__main__':
    getRouteAPI();
    getTravalTimeAPI();
    getInterchangeTimeAPI();
    getPriceAPI();
