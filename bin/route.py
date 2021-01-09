# route.py
#
# This program runs in Python 3.8
#

import json, csv
import collections
import heapq



# Class: Node
# Initial input: Line ID        (lid),
#                Station ID     (sid),
#                Line Name      (lName),
#                Station Name   (sName),
#                Line Field     (field),
#                Station Label  (label)
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
        print("*****\nlid: %s - field: %s - lName: %s\nsid: %s - label: %s - sName: %s\ninterchange: %s\n*****\n" %(self.lid, self.field, self.lName, self.sid, self.label, self.sName, self.interchange));



# Class: Graph
# Weighted Graph
# Initial input: None
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
        for key, val in self.weights.items():
            print("*****\nFrom %s to %s\nTime: %ds\n*****\n" %(key[0], key[1], val));
        for key, val in self.edges.items():
            print(key, val);



# Function: dijsktra()
# Find the Shortest Path by the Dijsktra Algorithm
# Input: a weighted graph (Graph), an initial node (Node), a destination node (Node)
# Return: the shortest path of from the initial node to the destination node
def dijsktra(graph, start, destination):
    initial = (start.label, start.sName);
    end = (destination.label, destination.sName);

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
# Read the data from the API files and arrange the data
# Input: None
# Return: the arranged Data in the following format:
#         {LineField: [*Node, ...], ...}
def arrangeData():
    all_stations = {};

    with open('./API/routeAPI.json', 'r') as f:
        routeData = json.load(f);

        for line in routeData:
            lid = line['LineID'];
            field = line['LineField'];
            lName = line['LineName'];

            if ((lid, field, lName) not in all_stations): all_stations.update({(lid, field, lName): []});

            stations = line['LineStations'];
            for station in stations:
                sid = station['SID'];
                label = station['StationLabel'];
                sName = station['StationName'];

                node = Node(lid, sid, lName, sName, field, label);
                all_stations[(lid, field, lName)].append(node);

                # Interchange Station
                interchange = station['StationLabelForRoadmap'].split(' ');
                if (len(interchange) > 1):
                    interLabel = interchange[0] if interchange[1] == label else interchange[1];
                    interField = interLabel[0] if interLabel[1].isdigit() else interLabel[0:1];
                    if (interField in all_stations):
                        for inter in all_stations[interField]:
                            if inter.label == interLabel:
                                node.interchange = inter;
                                inter.interchange = node;
                                break;

    return all_stations;



# Function: constructRoute()
# Construct a Weighted Graph from the data
# Input: None
# Return: a weighted graph
def constructRoute():
    route = arrangeData();
    graph = Graph();

    for field, stations in route.items():
        for i in range(len(stations)-1):
            fromNode = stations[i];
            toNode = stations[i+1];

            with open("./API/travelTimeAPI.csv", 'r', encoding='BIG5') as f:
                timeData = list(csv.reader(f));

                for row in timeData:
                    if (fromNode.sName in row[1]) and (toNode.sName in row[2]) or \
                        (fromNode.sName in row[2]) and (toNode.sName in row[1]):

                        travelTime = (int(row[3]) + int(row[5]));
                        # if travelTime: graph.insertEdge(fromNode.label, toNode.label, travelTime);
                        if travelTime: graph.insertEdge((fromNode.label, fromNode.sName), (toNode.label, toNode.sName), travelTime);
                        # if travelTime: graph.insertEdge(fromNode, toNode, travelTime);
                        break;

            # Interchange
            if fromNode.interchange:
                with open("./API/interchangeTimeAPI.csv", 'r', encoding='BIG5') as f:
                    timeData = list(csv.reader(f));

                    for row in timeData:
                        if (fromNode.sName in row[1]):
                            travelTime = int(row[2])*60;
                            # graph.insertEdge(fromNode.label, fromNode.interchange.label, travelTime);
                            graph.insertEdge((fromNode.label, fromNode.sName), (fromNode.interchange.label, fromNode.interchange.sName), travelTime);
                            # graph.insertEdge(fromNode, fromNode.interchange, travelTime);
                            break;
                        # else: graph.insertEdge(fromNode.label, fromNode.interchange.label, 0);
                        else: graph.insertEdge((fromNode.label, fromNode.sName), (fromNode.interchange.label, fromNode.interchange.sName), 0);
                        # else: graph.insertEdge(fromNode, fromNode.interchange, 0);

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



# DEBUG
if __name__ == '__main__':
    stations = arrangeData();
    for key, val in stations.items():
        print(key);
        for v in val:
            v.toStr();

    graph = constructRoute();
    graph.toStr();
