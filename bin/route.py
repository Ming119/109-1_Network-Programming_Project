# route.py
#
# This program runs in Python 3.8
#

import json, csv
import collections
import heapq
import platform



# Class: Node
# Initial parameters: Line ID        (lid)
#                     Station ID     (sid)
#                     Line Name      (lName)
#                     Station Name   (sName)
#                     Line Field     (field)
#                     Station Label  (label)
#
# Contain variable(s): lid          <string>
#                      sid          <string>
#                      lName        <string>
#                      sName        <string>
#                      field        <string>
#                      label        <string>
#                      transfer  <Node object>
#
# Contain function(s): toStr() -> <None>
#
class Node:
    def __init__(self, lid, sid, lName, sName, field, label):
        self.lid = lid
        self.sid = sid;
        self.lName = lName
        self.sName = sName;
        self.field = field;
        self.label = label;
        self.transfer = None;

    # For Testing
    def toStr(self):
        print("*****\n%s\nlid: %s - field: %s - lName: %s\nsid: %s - label: %s - sName: %s\ntransfer: %s\n*****\n" %(self, self.lid, self.field, self.lName, self.sid, self.label, self.sName, self.transfer));



# Class: Graph (Weighted Graph)
# Initial parameters: None
#
# Contain variable(s): edges    <collections.defaultdict object>
#                      weights  <dict>
#
# Contain function(s): insertEdge() -> <None>
#                      toStr()      -> <None>
#
class Graph:
    def __init__(self):
        self.edges = collections.defaultdict(list);
        self.weights = {};

    # Function insertEdge()
    # Insert edge between fromNode and toNode with the weight
    #
    # Parameters: fromNode  <tuple>
    #             toNode    <tuple>
    #             weight    <int>
    def insertEdge(self, fromNode, toNode, weight):
        if (toNode not in self.edges[fromNode]): self.edges[fromNode].append(toNode);   # {fromNode: [$(neighbours)...]}
        if (fromNode not in self.edges[toNode]): self.edges[toNode].append(fromNode);   # {toNode: [$(neighbours)...]}
        self.weights[(fromNode, toNode)] = weight;  # {(fromNode, toNode): weight}
        self.weights[(toNode, fromNode)] = weight;  # {(toNode, fromNode): weight}

    # For Testing
    def toStr(self):
        print();
        for key, val in self.edges.items():
            print("**********\nFrom %s\n%s\n**********\n" %(key, val));

        print();
        for key, val in self.weights.items():
            print("**********\nFrom %s to %s\nTime: %ds\n**********\n" %(key[0], key[1], val));




# Function: dijsktra()
# Find the shortest path and needed time by the Dijsktra's Algorithm
#
# Parameters: graph         <Graph object>
#             start         <Node object>
#             destination   <Node object>
#
# Return: the shortest path and needed time from the initial node to the destination node
#           path   -> <list>
#           weight -> <int>
#
def dijsktra(graph, start, destination):
    initial = (start.label, start.sName);
    end = (destination.label, destination.sName);

    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)};
    current_node = initial;
    visited = set();
    weight = 0;

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

    return path, weight;



# Function: arrangeData()
# Read the data from the API files and arrange the data
#
# Parameters: None
#
# Return: the arranged Data in the following format:
#         {LineField: [*Node, ...], ...}
#         all_stations -> <dict>
#
def arrangeData():
    all_stations = {};

    if platform.system() == "Windows": path = "./API/routeAPI.json";
    elif platform.system() == "Linux": path = "./API/routeAPI.json";
    else: path = "";

    with open(path, 'r', encoding = 'utf-8') as f:
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

                # Handling Orange Line O12 -> O50 Branch
                if (label == 'O50'):
                    for inter in all_stations[field]:
                        if (inter.label == 'O12'):
                            node.transfer = inter;
                            inter.transfer = node;
                            break;

                # Handling Subline
                if (label[-1].isalpha()):
                    for inter in all_stations[field]:
                        if (inter.label == label[:-1]):
                            node.transfer = inter;
                            inter.transfer = node;
                            break;

                all_stations[field].append(node);

                # Interchange Station
                transfer = station['StationLabelForRoadmap'].split(' ');
                if (len(transfer) > 1):
                    interLabel = transfer[0] if transfer[1] == label else transfer[1];
                    interField = interLabel[0] if interLabel[1].isdigit() else interLabel[0:2];

                    if (interField in all_stations):
                        for inter in all_stations[interField]:
                            if (inter.label == interLabel):
                                node.transfer = inter;
                                inter.transfer = node;
                                break;

    return all_stations;



# Function: constructRoute()
# Construct a Weighted Graph from the data
#
# Parameters: route <dict>
#
# Return: a weighted graph
#         graph -> <Graph object>
#
def constructRoute(route):
    # Interchange
    def transfer(fromNode):
        if fromNode.transfer:

            if platform.system() == "Windows": path = "./API/transferTimeAPI.csv";
            elif platform.system() == "Linux": path = "./API/transferTimeAPI.csv";
            else: path = "";

            with open(path, 'r', encoding='BIG5') as f:
                timeData = list(csv.reader(f));

                for row in timeData:
                    if (fromNode.sName in row[1]):
                        travelTime = int(row[2])*60;
                        graph.insertEdge((fromNode.label, fromNode.sName), (fromNode.transfer.label, fromNode.transfer.sName), travelTime);
                        break;
                    else: graph.insertEdge((fromNode.label, fromNode.sName), (fromNode.transfer.label, fromNode.transfer.sName), 10);



    graph = Graph();

    for field, stations in route.items():
        for i in range(len(stations)-1):
            fromNode = stations[i];
            toNode = stations[i+2] if stations[i+1].label[-1].isalpha() else stations[i+1];

            if platform.system() == "Windows": path = "./API/travelTimeAPI.csv";
            elif platform.system() == "Linux": path = "./API/travelTimeAPI.csv";
            else: path = "";

            with open(path, 'r', encoding='BIG5') as f:
                timeData = list(csv.reader(f));

                for row in timeData:
                    if (fromNode.sName in row[1]) and (toNode.sName in row[2]) or \
                        (fromNode.sName in row[2]) and (toNode.sName in row[1]):

                        travelTime = (int(row[3]) + int(row[5]));
                        if travelTime: graph.insertEdge((fromNode.label, fromNode.sName), (toNode.label, toNode.sName), travelTime);
                        break;

            transfer(fromNode);

        fromNode = stations[-1];
        transfer(fromNode);

    return graph;



# DEBUG
if __name__ == '__main__':
    stations = arrangeData();
    for key, val in stations.items():
        print(key);
        for v in val:
            v.toStr();

    graph = constructRoute(stations);
    graph.toStr();
