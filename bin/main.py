import os
import os.path
from os import path
import time
import pandas as pd
import urllib.request
import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup

import route

#
# def getStation(line):
#     with open(API_path, 'r', encoding = 'utf8') as jsonfile:
#         data = json.load(jsonfile)[int(line)-1]['LineStations']
#
#         for i, _ in enumerate(data):
#             print('-%2s\t%s\t%s' %(str(i+1), _['StationLabel'], _['StationName']))
#         print('\n-Q 返回上一頁 Return previous page')
#
#         while True:
#             station = input('\n請輸入捷運站編號：')
#             if (station == 'Q'): return getRoute()
#             if 0 < int(station) < len(data)+1:
#                 return data[int(station)-1]
#
#             print('{:^30}'.format('*** 輸入錯誤，請重新輸入 ***'))
#             print('*** Input error, please input again ***')
#
#
#
# def getRoute():
#     with open(API_path, 'r', encoding = 'utf8') as jsonfile:
#         data = json.load(jsonfile)
#
#         lines = {}
#         for _ in data:
#             line = _['LineName'].split(' ')
#             lines.update({line[0]: _['LineID']})
#             print('- %s\t%s' %(line[0], line[1]))
#
#         while True:
#             line = input('\n請輸入捷運路線代號：')
#             if line in lines: return getStation(lines[line])
#
#             print('{:^30}'.format('*** 輸入錯誤，請重新輸入 ***'))
#             print('*** Input error, please input again ***')
#



# def printout():
    #     print('\n{:^50}'.format('--- 請選擇出發地捷運路線 ---'))
    #     print('--- Please select the MRT route from the place of departure ---')
    #     departure = getRoute()
    #
    #     print('\n---{:^50}---'.format('--- 請選擇目的地捷運路線 ---'))
    #     print('--- Please select the MRT route from the place of departure ---')
    #     destination = getRoute()
    #
    #     print(departure)
    #     print(destination)
    #
    #     path = findPaths(departure, destination)
    #     # print(path)
    #     # print(evaluateTime(path))
    #
    #
    #     price = getPrice(departure['StationName'], destination['StationName'])
    #     print('[%s] -> [%s]'%(departure['StationName'], destination['StationName']))
    #     print('全票票價：%s\t敬老、愛心票價：%s'%(price[2], price[3]))



if __name__ == '__main__':
    graph = route.constructRoute();



    path = route.dijsktra(graph, start, end);
