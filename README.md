# 臺北市捷運系統最佳路線

### 組員姓名
108590049 符芷琪 \
108590050 李浩銘

## 摘要說明
This program is going to find out the best path from the departure station A to the destination station B for the Taipei MRT system using the Dijkstra's Algorithm. \
The algorithm is dependent on the travel time from station A to station B by the undirected weighted graph

## 動機背景
市面上有很多除了官方出的APP都是可以搜尋臺北捷運的搭乘路線，例如臺北捷運通等APP，\
但是很多的APP都有些BUG,它們的演算法並不能計算出實際的最佳(所需時間最短)路線，\
因為有轉乘線站，有些線路到達目的地的站數和距離都各不相同,那些APP只考慮到是否能到達目的地，\
並沒有找出最快到達的路線。


## 相關研究/實作
[政府資料開放平台](https://data.gov.tw/datasets/search?qs=&order=pubdate&type=dataset)

[臺北大眾捷運股份有限公司](https://web.metro.taipei/pages/tw/ticketroutetimequery)

[Github - Dijkstra-shortest-path by wntun](https://github.com/wntun/Dijkstra-shortest-path)

[Academic Journal of Engineering and Technology Science (ISSN 2616-5767) \
By Francis Academic Press, UK \
Subway Distribution Path Optimization Issues Based on Dijkstra Algorithm](https://francis-press.com/uploads/papers/pVs76FClOYAeJn0o7wjuXH7cAM6FgzOqDu8p8FDa.pdf)


## 功能說明
- [x] Select the Departure Station A
- [x] Select the Destination Station B
- [x] Provide the *best path* from Station A to Station B
- [x] Provide the *price* from Station A to Station B
- [x] Provide the *travel time* from Station A to Station B
- [x] Provide a *User Interface*
- [ ] Provide the route of *Out-of-Station Transfer*

## 程式執行部署環境與步驟
This program runs in Python3

### Flask
For using the Web Application, you need to install **Flask**:
> $ pip3 install flask

### run with make
If you have install *'make'* on your system:
> $ make

or
> $ make run_web

for the Web Application.

### run without make
If you do not have *'make'* on your system:
> $ python3 ./bin/main.py

or
> $ python3 ./bin/app.py

for the Web Application.



## 優點/貢獻/好處
1. print out the entire route
2. Travel time can be accurate to second
3. Cross-platform
4. Visualization

## 執行畫面截圖
*注意:請先下載整份檔案\
step1.\
![image](https://github.com/Ming119/Network-Programming-Project/blob/main/document/1.JPG) \
step2.\
![image](https://github.com/Ming119/Network-Programming-Project/blob/main/document/2.JPG) \
step3.\
![image](https://github.com/Ming119/Network-Programming-Project/blob/main/document/3.JPG) \
step4.\
![image](https://github.com/Ming119/Network-Programming-Project/blob/main/document/4.JPG)

## 網頁操作畫面截圖
step1.\
![image](https://github.com/Ming119/Network-Programming-Project/blob/main/document/pic3.gif)\
step2.\
![image](https://github.com/Ming119/Network-Programming-Project/blob/main/document/pic4.gif)\
step3.\
![image](https://github.com/Ming119/Network-Programming-Project/blob/main/document/pic5.gif)

## 例子：(來源:臺北捷運通.APP)
![image](https://github.com/Ming119/Network-Programming-Project/blob/main/document/pic1.gif) \
![image](https://github.com/Ming119/Network-Programming-Project/blob/main/document/pic2.gif)

## LICENSES
[GNU General Public License v3.0](https://github.com/Ming119/109-1_Network-Programming_Project/blob/main/LICENSE) \
[Open Government Data License, version 1.0](https://data.gov.tw/license)

