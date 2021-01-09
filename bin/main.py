# main.py
#
# This program runs in Python 3.8
#

import csv, json
import route, api
import platform



def getStation(lineField, lines):
    print("\n\n\n---** 請輸入捷運路線代號 **---");

    for i, station in enumerate(lines[lineField]):
        print('-%2s\t%s\t%s' %((i+1), station.label, station.sName));
    print('\n-Q 返回上一頁 Return previous page');

    while True:
        stationCode = input('\n---** 請輸入捷運站編號：');
        if (stationCode == 'Q' or stationCode == 'q'): return getRoute(lines);

        if 0 < int(stationCode) < len(lines[lineField])+1:
            return lines[lineField][int(stationCode)-1];

        print('---{:^30}---'.format('--- ** 輸入錯誤!!! 請重新輸入!!! ** ---'));
        print('---** Input error!!! please input again!!! **---');



def getRoute(lines):
    if platform.system() == "Windows": path = "../API/routeAPI.json";
    elif platform.system() == "Linux": path = "./API/routeAPI.json";
    else: path = "";

    with open(path, 'r', encoding = 'utf8') as f:
        routeData = json.load(f);

        for line in routeData:
            print('- %s\t%s' %(line['LineID'], line['LineName']));
        print('\n-Q 退出 Exit');

        while True:
            lineCode = input('\n---** 請輸入捷運路線代號：');
            if (lineCode == 'Q' or lineCode == 'q'): exit();
            for line in routeData:
                if lineCode == line['LineID']: return getStation(line['LineField'], lines);
            else:
                print('---{:^30}---'.format('---** 輸入錯誤!!! 請重新輸入!!! **---'));
                print('---** Input error!!! please input again!!! **---');



def getPrice(start, end):
    if platform.system() == "Windows": path = "../API/priceAPI.csv";
    elif platform.system() == "Linux": path = "./API/priceAPI.csv";
    else: path = "";

    with open(path, 'r', encoding='BIG5') as f:
        priceData = csv.reader(f)

        for row in priceData:
            r1 = row[0][:-1] if '站' in row[0] else row[0];
            r2 = row[1][:-1] if '站' in row[1] else row[1];
            if (r1 == start.sName and r2 == end.sName): return row;



# main function
if __name__ == '__main__':
    print(" ***** 初始化 Initializing ****** ");
    api.getAllAPI();
    stations = route.arrangeData();
    graph = route.constructRoute(stations);
    print(" ***** 初始化完成 Finished ***** ");



    print('\n---{:^50}---'.format('---** 請選擇出發地捷運路線 **---'))
    print('---** Please select the MRT route from the place of departure **---')
    start = getRoute(stations);
    print('\n出發地：%s - %s' %(start.label, start.sName));


    print('\n\n\n---{:^50}---'.format('---** 請選擇目的地捷運路線 **---'))
    print('---** Please select the MRT route from the place of departure **---')
    end = getRoute(stations);
    print('\n目的地：%s - %s' %(end.label, end.sName));

    path, time = route.dijsktra(graph, start, end);

    price = getPrice(start, end);

    for i, p in enumerate(path):
        print("[%s - %s]" %(p[0], p[1]), end = '');
        if i != len(path)-1: print(" -> ", end = '');
        else: print();

    print('全票票價：$ %s\t \n*敬老、愛心票價：$ %s' %(price[2], price[3]))
