# 臺北市捷運系統最佳路線

### 組員姓名
108590049 符芷琪 \
108590050 李浩銘

## 摘要說明
This program is going to find out the best path from the departure station A to the destination station B for the Taipei MRT system using the Dijkstra's Algorithm. \
The algorithm is dependent on the travel time from station A to station B by the weighted graph.

該程序將使用Dijkstra算法為台北捷運系統找到從出發站A到目的地站B的最佳路徑。 \
該算法取決於加權圖從站點A到站點B的旅行時間。


## 動機背景
市面上有很多除了官方出的APP都是可以搜尋臺北捷運的搭乘路線，例如臺北捷運通等APP，\
但是很多的APP都有些BUG,它們的演算法並不能計算出實際的最佳(所需時間最短)路線，\
因為有轉乘線站，有些線路到達目的地的站數和距離都各不相同,那些APP只考慮到是否能到達目的地，\
並沒有找出最快到達的路線。


## 相關研究/實作
臺北大眾捷運股份有限公司:\
https://web.metro.taipei/pages/tw/ticketroutetimequery \
非開源

Github - wntun: (韓國) \
https://github.com/wntun/Dijkstra-shortest-path \
使用 Adjacency Matrix + Dijkstra

Academic Journal of Engineering and Technology Science (ISSN 2616-5767) \
By Francis Academic Press, UK \
Subway Distribution Path Optimization Issues Based on Dijkstra Algorithm \
https://francis-press.com/uploads/papers/pVs76FClOYAeJn0o7wjuXH7cAM6FgzOqDu8p8FDa.pdf


## 功能說明
輸入所出發的臺北捷運站名和需到達的臺北捷運站名，\
輸出搭乘臺北捷運的最佳(所需時間最短)的捷運路線和所有票價供用戶參考。

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

and
> $ python3 ./bin/app.py

for the Web Application.



If you have install *'make'* on your system
> $ make

or
> $ make run_web

for the Web Application.



## 優點/貢獻/好處
> 可以把整條捷運路線印出來 \
> 搭乘時間可準確到單位秒 \
> 跨平台 \
> 可視化

## 執行畫面截圖
*注意:請先下載整份檔案\
step1.\
![image](https://github.com/Ming119/Network-Programming-Project/blob/main/document/1.JPG)\
step2.\
![image](https://github.com/Ming119/Network-Programming-Project/blob/main/document/2.JPG)\
step3.\
![image](https://github.com/Ming119/Network-Programming-Project/blob/main/document/3.JPG)\
step4.\
![image](https://github.com/Ming119/Network-Programming-Project/blob/main/document/4.JPG)\

## 例子：(來源:臺北捷運通.APP)
![image](https://github.com/Ming119/Network-Programming-Project/blob/main/document/pic1.gif)\
![image](https://github.com/Ming119/Network-Programming-Project/blob/main/document/pic2.gif)\
