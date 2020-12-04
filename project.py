import os, csv, json
import os.path
from os import path
import pandas as pd
import urllib.request
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup

API_path = 'MRT_tw_API' # default

def A_Star(departure, destination):
    closeSet = set()
    openSet = {departure}



def evaluateTime(path):
    url = 'https://data.taipei/api/getDatasetInfo/downloadResource?id=513e97fe-6a98-4a0d-b7dc-11122c8638d4&rid=c32998fa-c9b2-4324-9016-e19fbe0815f1'
    urllib.request.urlretrieve(url, 'MRT_Time_API.csv')

    with open('MRT_Time_API.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)

        for row in csv_reader:
            # print(row)
            pass



def findPaths(departure, destination):
    if departure['LineID'] == destination['LineID']:
        print([departure['StationLabel'][:-2]+str(i).zfill(2) for i in range(int(departure['StationLabel'][-2:]), int(destination['StationLabel'][-2:])+1)])
        return [departure['StationLabel'][:-2]+str(i).zfill(2) for i in range(int(departure['StationLabel'][-2:]), int(destination['StationLabel'][-2:])+1)]



def getStation(line):
    with open(API_path, 'r', encoding = 'utf8') as jsonfile:
        data = json.load(jsonfile)[int(line)-1]['LineStations']

        for i, _ in enumerate(data):
            print('-%2s\t%s\t%s' %(str(i+1), _['StationLabel'], _['StationName']))
        print('\n-Q 返回上一頁 Return previous page')

        while True:
            station = input('\n請輸入捷運站編號：')
            if (station == 'Q'): return getRoute()
            if 0 < int(station) < len(data)+1:
                return data[int(station)-1]

            print('{:^30}'.format('*** 輸入錯誤，請重新輸入 ***'))
            print('*** Input error, please input again ***')



def getRoute():
    with open(API_path, 'r', encoding = 'utf8') as jsonfile:
        data = json.load(jsonfile)

        lines = {}
        for _ in data:
            line = _['LineName'].split(' ')
            lines.update({line[0]: _['LineID']})
            print('- %s\t%s' %(line[0], line[1]))

        while True:
            line = input('\n請輸入捷運路線代號：')
            if line in lines: return getStation(lines[line])

            print('{:^30}'.format('*** 輸入錯誤，請重新輸入 ***'))
            print('*** Input error, please input again ***')



def getPrice(departure, destination):
    url = 'https://data.taipei/api/getDatasetInfo/downloadResource?id=4acb4911-0360-4063-808d-fcee629508b3&rid=893c2f2a-dcfd-407b-b871-394a14105532'
    urllib.request.urlretrieve(url, 'MRT_Price_API.csv')

    with open('MRT_Price_API.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)

        for row in csv_reader:
            if (row[0] == departure and row[1] == destination): return row



def getAPI(lang) -> None:
    global API_path
    API_path = 'MRT_%s_API.json'%lang
    if path.exists(API_path): return

    url = 'https://web.metro.taipei/apis/metrostationapi/menuline'
    respone = requests.post(url, data = {"LineID":"0","Lang":lang})
    jsondata = respone.json()

    with open(API_path, 'w', encoding = 'utf8') as jsonfile:
        json.dump(jsondata, jsonfile, ensure_ascii = False)



if __name__ == '__main__':
    print('\n{:^25}'.format('--- 請選擇語言 ---'))
    print('--- Please select language ---')

    while True:
        lang = int(input('1.中文 | 2.English\n'))
        if 0 < lang < 3: break

        print('\n{:^30}'.format('*** 輸入錯誤，請重新輸入 ***'))
        print('*** Input error, please input again ***')

    getAPI('tw' if lang == 1 else 'en')

    print('\n{:^50}'.format('--- 請選擇出發地捷運路線 ---'))
    print('--- Please select the MRT route from the place of departure ---')
    departure = getRoute()

    print('\n---{:^50}---'.format('--- 請選擇目的地捷運路線 ---'))
    print('--- Please select the MRT route from the place of departure ---')
    destination = getRoute()

    print(departure)
    print(destination)

    path = findPaths(departure, destination)
    # print(path)
    # print(evaluateTime(path))


    price = getPrice(departure['StationName'], destination['StationName'])
    print('[%s] -> [%s]'%(departure['StationName'], destination['StationName']))
    print('全票票價：%s\t敬老、愛心票價：%s'%(price[2], price[3]))
