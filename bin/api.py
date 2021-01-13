# api.py
#
# This program runs in Python 3.8
#

import time, os
import json, csv
import requests
import urllib.request
import platform



# "https://web.metro.taipei/apis/metrostationapi/menuline"
def getRouteAPI() -> None:
    path = "./API/routeAPI.json";
    # if platform.system() == "Windows": path = "./API/routeAPI.json";
    # elif platform.system() == "Linux": path = "./API/routeAPI.json";
    # else: path = "";

    if os.path.exists(path):
        if (time.time() - os.stat(path).st_mtime < 2600000):
            return path;

    url = 'https://web.metro.taipei/apis/metrostationapi/menuline'
    respone = requests.post(url, data = {"LineID":"0","Lang":'tw'})
    jsondata = respone.json()

    with open(path, 'w', encoding = 'utf8') as jsonfile:
        json.dump(jsondata, jsonfile, ensure_ascii = False);

    return path;



# "https://data.taipei/api/getDatasetInfo/downloadResource?id=513e97fe-6a98-4a0d-b7dc-11122c8638d4&rid=c32998fa-c9b2-4324-9016-e19fbe0815f1"
def getTravelTimeAPI() -> None:
    path = "./API/travelTimeAPI.csv";
    # if platform.system() == "Windows": path = "../API/travelTimeAPI.csv";
    # elif platform.system() == "Linux": path = "./API/travelTimeAPI.csv";
    # else: path = "";

    if os.path.exists(path):
        if (time.time() - os.stat(path).st_mtime < 2600000):
            return path;

    url = "https://data.taipei/api/getDatasetInfo/downloadResource?id=513e97fe-6a98-4a0d-b7dc-11122c8638d4&rid=c32998fa-c9b2-4324-9016-e19fbe0815f1"
    urllib.request.urlretrieve(url, path);

    return path;



# "https://data.taipei/api/getDatasetInfo/downloadResource?id=782c2b71-8f5a-4575-9bf2-e86999be2863&rid=14fd1af0-dc2b-4174-87d4-fcb9de783496"
def getTransferTimeAPI() -> None:
    path = "./API/transferTimeAPI.csv"
    # if platform.system() == "Windows": path = "../API/transferTimeAPI.csv";
    # elif platform.system() == "Linux": path = "./API/transferTimeAPI.csv";
    # else: path = "";

    if os.path.exists(path):
        if (time.time() - os.stat(path).st_mtime < 2600000):
            return path;

    url = "https://data.taipei/api/getDatasetInfo/downloadResource?id=782c2b71-8f5a-4575-9bf2-e86999be2863&rid=14fd1af0-dc2b-4174-87d4-fcb9de783496"
    urllib.request.urlretrieve(url, path);

    return path;



# "https://data.taipei/api/getDatasetInfo/downloadResource?id=4acb4911-0360-4063-808d-fcee629508b3&rid=893c2f2a-dcfd-407b-b871-394a14105532"
def getPriceAPI() -> None:
    path = "./API/priceAPI.csv";
    # if platform.system() == "Windows": path = "../API/priceAPI.csv";
    # elif platform.system() == "Linux": path = "./API/priceAPI.csv";
    # else: path = "";

    if os.path.exists(path):
        if (time.time() - os.stat(path).st_mtime < 2600000):
            return path;

    url = "https://data.taipei/api/getDatasetInfo/downloadResource?id=4acb4911-0360-4063-808d-fcee629508b3&rid=893c2f2a-dcfd-407b-b871-394a14105532"
    urllib.request.urlretrieve(url, path);

    return path;

def getAllAPI() -> None:
    getRouteAPI()
    getTravelTimeAPI()
    getTransferTimeAPI()
    getPriceAPI()

def DEBUG(path):
    print("***** %s *****" %path);
    print(os.stat(path));
    print("******************************\n")

if __name__ == '__main__':
    DEBUG(getRouteAPI());
    DEBUG(getTravelTimeAPI());
    DEBUG(getTransferTimeAPI());
    DEBUG(getPriceAPI());
