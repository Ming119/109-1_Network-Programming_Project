# 題目
臺北市捷運系統最佳路線

# 組員姓名
108590049 符芷琪 \
108590050 李浩銘

## 摘要說明
This program is going to find out the best path from the departure station A to the destination station B for the Taipei MRT system.\
The algorithm is dependent on the travel time from A to B.\
該程序將為台北捷運系統找到從出發站A到目的地站B的最佳路徑，該算法取決於從A到B的時間。


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

## 專題優點、好處
1.可以把整條捷運路線印出來\
2.搭乘時間可準確到單位秒\
3.
