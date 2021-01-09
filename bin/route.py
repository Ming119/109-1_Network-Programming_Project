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
# Weighted Graph
class Graph:
    def __init__(self):
        self.edges = collections.defaultdict(list);
        self.weights = {};

    def insertEdge(self, fromNode, toNode, weight):
        self.edges[fromNode].append(toNode);
        self.edges[toNode].append(fromNode);
        self.weights[(fromNode, toNode)] = weight;
        self.weights[(toNode, fromNode)] = weight;

    # For Testing
    def toStr(self):
        for e in self.graph:
            print(e);


# Function: dijsktra()
# Find the Shortest Path by Dijsktra Algorithm
def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)};
    current_node = initial;
    visited = set();

    while current_node != end:
        visited.add(current_node);
        destinations = graph.edges[current_node];
        weight_to_current_node = shortest_paths[current_node][1];

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node;
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight);
            else:
                current_shortest_weight = shortest_paths[next_node][1];
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight);

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited};
        if not next_destinations:
            return "Route Not Possible";
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1]);

    # Work back through destinations in shortest path
    path = [];
    while current_node is not None:
        path.append(current_node);
        next_node = shortest_paths[current_node][0];
        current_node = next_node;
    # Reverse path
    path = path[::-1];
    return path;



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
    route = arrangeData();
    graph = Graph();

    with open("./API/MRT_Time_API.csv", 'r', encoding='BIG5') as f:
        timeData = list(csv.reader(f));

        for field, stations in field.items():
            for i in range(len(stations)-1):
                travelTime = 0;
                fromNode = statons[i];
                toNode = stations[i+1];

                for index, row in enumerate(timeData):

                    if (row[1][2:-1] == fromNode.sName) and (row[2][2:-1] == toNode.sName) or \
                        (row[2][2:-1] == fromNode.sName) and (row[1][2:-1] == toNode.sName):

                        travelTime += (int(row[3]) + int(row[5]));
                        if travelTime: timeData.pop(index);
                        break;

                if travelTime: graph.insertEdge(fromNode, toNode, travelTime);

                if fromNode.interchange: toNode = fromNode.interchange;
                if fromNode == "台北車站": 

                for index, row in enumerate(timeData):

                    if (row[1][2:-1] == fromNode.sName) and (row[2][2:-1] == toNode.sName) or \
                        (row[2][2:-1] == fromNode.sName) and (row[1][2:-1] == toNode.sName):

                        travelTime += (int(row[3]) + int(row[5]));
                        if travelTime: timeData.pop(index);
                        break;






                #     # '台北車站' Needs special treatment
                #     if (station.sName == '台北車站'):
                #         if (row[1][2:] == '台北車站') and (row[2][2:-1] == toNode.sName) or \
                #             (row[2][2:] == '台北車站') and (row[1][2:-1] == toNode.sName):
                #
                #             travelTime += (int(row[3]) + int(row[5]));
                #             if travelTime: timeData.pop(index);
                #             break;
                #
                #     elif (toNode.sName == '台北車站'):
                #         if (row[1][2:] == '台北車站') and (row[2][2:-1] == formNode.sName) or \
                #             (row[2][2:] == '台北車站') and (row[1][2:-1] == formNode.sName):
                #
                #             travelTime += (int(row[3]) + int(row[5]));
                #             if travelTime: timeData.pop(index);
                #             break;
                #
                #     elif (row[1][2:-1] == formNode.sName) and (row[2][2:-1] == toNode.sName) or \
                #         (row[1][2:-1] == toNode.sName) and (row[2][2:-1] == formNode.sName):
                #         travelTime += (int(row[3]) + int(row[5]));
                #
                #         if travelTime: timeData.pop(index);
                #         break;
                # if travelTime: graph.insertEdge(formNode, toNode, travelTime);

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
