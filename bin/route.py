# route.py
#
# This file runs in Python 3
#

import json, csv
import collections
import heapq

# Class: Node
class Node:
    def __init__(self, lid, sid, lName, sName, field, label):
        self.lid = lid
        self.sid = sid;
        self.lName = lName
        self.sName = sName;
        self.field = field;
        self.label = label;
        self.interchange = None;

    # For Testing
    def toStr(self):
        print("*****\nlid: %s - field: %s - lName: %s\nsid: %s - label: %s - sName: %s\ninterchange: %s\n*****" %(self.lid, self.field, self.lName, self.sid, self.label, self.sName, self.interchange), end = "");



# Class: Graph
# Weighted DAG
class Graph:
    def __init__(self):
        self.graph = collections.defaultdict(list);

    def insertEdge(self, node, neighbour, cost):
        # {node:[(cost,neighbour), ...]}
        self.graph[node].append((cost, neighbour));

    # Find the Shortest Path
    def shortestPath(self, _from, _dest):
        # create a priority queue and hash set to store visited nodes
        queue = [(0, _from, [])];    # Priority Queue
        visited = set();
        heapq.heapify(queue);

        # BFS Traversal
        while queue:
            (cost, node, path) = heapq.heappop(queue);

            # visit the node if the node is non-visited
            if node not in visited:
                visited.add(node);
                path = path + [node];

                # Hit the dest
                if node == _dest: return (cost, path);

                # visit neighbours
                for c, neighbour in graph[node]:
                    if neightbour not in visited:
                        heapq.heappush(queue, (cost+c, neighbour, path));

        # Path Not Found
        return int("inf");

    # For Testing
    def toStr(self):
        for e in self.graph:
            print(e);


# Function: arrangeData()
def arrangeData():
    all_stations = {};

    with open('./API/MRT_tw_API.json', 'r') as f:
        routeData = json.load(f);

        for line in routeData:
            lid = line['LineID'];
            field = line['LineField'];
            lName = line['LineName'];

            if (field not in all_stations): all_stations.update({field: []});

            stations = line['LineStations'];
            for station in stations:
                sid = station['SID'];
                label = station['StationLabel'];
                sName = station['StationName'];

                node = Node(lid, sid, lName, sName, field, label);
                all_stations[field].append(node);

                # Interchange Station
                interchange = station['StationLabelForRoadmap'].split(' ');
                if (len(interchange) > 1):
                    interLabel = interchange[0] if interchange[1] == label else interchange[1];
                    interField = interLabel[0] if interLabel[1].isdigit() else interLabel[0:1];
                    if (interField in all_stations):
                        for inter in all_stations[interField]:
                            if inter.label == interLabel:
                                inter.interchange = node;
                                node.interchange = inter;
                                break;

    return all_stations;


# Function: constructRoute()
def constructRoute():
    stations = arrangeData();
    graph = Graph();

    travelTime = 0;
    with open("./API/MRT_Time_API.csv", 'r', encoding='BIG5') as f:
        timeData = list(csv.reader(f));

        for key, val in stations.items():
            for index, row in enumerate(timeData):

                # '台北車站' Needs special treatment
                if (formNode.sName == '台北車站'):
                    if (row[1][2:] == '台北車站') and (row[2][2:-1] == neighbour.sName) or \
                        (row[2][2:] == '台北車站') and (row[1][2:-1] == neighbour.sName):

                        travelTime += (int(row[3]) + int(row[5]));
                        if travelTime: timeData.pop(index);
                        break;

                elif (neighbour.sName == '台北車站'):
                    if (row[1][2:] == '台北車站') and (row[2][2:-1] == formNode.sName) or \
                        (row[2][2:] == '台北車站') and (row[1][2:-1] == formNode.sName):

                        travelTime += (int(row[3]) + int(row[5]));
                        if travelTime: timeData.pop(index);
                        break;

                elif (row[1][2:-1] == formNode.sName) and (row[2][2:-1] == neighbour.sName) or \
                    (row[1][2:-1] == neighbour.sName) and (row[2][2:-1] == formNode.sName):
                    travelTime += (int(row[3]) + int(row[5]));

                    if travelTime: timeData.pop(index);
                    break;
            if travelTime: graph.insertEdge(formNode, neighbour, travelTime);

    return graph;



# Get station by ID or LABEL
# Input a LABEL is better than a ID
# Return a pointer of the class "Station"
def getStation(id = '', label = ''):
    for line in existing_line:
        if label:
            _FindLine = label[0:2] if label[1].isalpha() else label[0];
            if line.LineColor != _FindLine: continue;

        ptr = line.head;
        while ptr.nextStation is not None:
            if label and ptr.StationLabel == label: return ptr
            if id and ptr.StationId == id: return ptr

            ptr = ptr.nextStation;

    print(" Error: getStation(), cannot find any matchabe station ")
    return None;

if __name__ == '__main__':
    stations = arrangeData();

    graph = constructRoute();


    # for line in existing_line:
    #     line.toStr();
    #
    #     sptr = line.head;
    #     while sptr is not None:
    #         sptr.toStr();
    #         sptr = sptr.nextStation;
    #
    #     print();
    #
    # start = getStation(label = 'G12');
    # # start = getStation(label = 'BL10');
    # end = getStation(label = 'BL14');
    #
    # # print(p)
    # # for i in p:
    # #     for j in i:
    # #         print(j.toStr());
