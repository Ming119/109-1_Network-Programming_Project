# route.py
#
# This file runs in Python 3
#

import json

# Extended Doubly Linked List
class Station:
    def __init__(self, id, name, label):
        self.StationId = id;
        self.StationName = name;
        self.StationLabel = label;
        self.prevStation = None;
        self.nextStation = None;
        self.interchange = None;    # For Branch Line or Interchage Station

    # For Testing
    def toStr(self):
        print("*** %s - %s ***" %(self.StationLabel, self.StationName), end = "");
        if self.interchange is not None:
            print(" Link to %s - %s" %(self.interchange.StationLabel, self.interchange.StationName));
        else: print()

class Line:
    def __init__(self, id, name, color):
        self.LineId = id;
        self.LineName = name;
        self.LineColor = color;
        self.head = None;
        self.tail = None;

    def insert(self, data):
        new_node = Station(data['SID'], data['StationName'], data['StationLabel']);     #StationId, StationName

        # First Node
        if self.head is None: self.head = self.tail = new_node;

        # Others
        else:
            # Branch Line
            if data['StationLabel'][-1].isalpha():
                new_node.interchange = self.tail;
                self.tail.interchange = new_node;

            # Same Line
            else:
                new_node.prevStation = self.tail;
                self.tail.nextStation = new_node;
                self.tail = new_node;

            # Interchange Station
            _StationLabel = data['StationLabelForRoadmap'].split(' ');
            if len(_StationLabel) == 2:
                _FindStation = _StationLabel[0] if _StationLabel[1] == data['StationLabel'] else _StationLabel[1];
                _FindLine = _FindStation[0:2] if _FindStation[1].isalpha() else _FindStation[0];

                for line in existing_line:
                    if line.LineColor != _FindLine: continue;

                    inter_node = line.head;
                    while inter_node.nextStation is not None:
                        if inter_node.StationLabel == _FindStation:
                            new_node.interchange = inter_node;
                            inter_node.interchange = new_node;
                            break;
                        inter_node = inter_node.nextStation;

    # For Testing
    def toStr(self):
        print("*** %s - %s ***" %(self.LineId, self.LineName));





# Construct Route from JSON
# Input a JSON format data
# Return a list with class "Line"
existing_line = [];
def constructRoute(data):
    for line in data:
        new_line = Line(line['LineID'], line['LineName'], line['LineField']);
        for station in line['LineStations']:
            new_line.insert(station);

        existing_line.append(new_line);
    return existing_line



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



# Find all possible paths form START to END
# Input two pointer of class "Station"
# Return a list with all possible paths
def findPaths(start, end):
    _StartLine = start.StationLabel[0:2] if start.StationLabel[1].isalpha() else start.StationLabel[0];
    _EndLine = end.StationLabel[0:2] if end.StationLabel[1].isalpha() else end.StationLabel[0];
    _StartStation = int(start.StationLabel[len(_StartLine):]);
    _EndStation = int(end.StationLabel[len(_EndLine):]);

    # At the same line
    paths = [];
    if _StartLine == _EndLine:
        path = [];
        ptr = start;
        while True:
            if ptr is None: break;
            path.append(ptr);
            if ptr.StationLabel == end.StationLabel: break

            ptr = ptr.nextStation if _StartStation < _EndStation else ptr.prevStation;

        paths.append(path);
        return paths;

    # At different line
    pass;



if __name__ == '__main__':``
    file = "./apidoc/MRT_tw_API.json";  # File path for Linux
    # file = "../apidoc/MRT_tw_API.json"; # File path for Windows
    with open(file, 'r') as f:
        data = json.load(f);
        constructRoute(data);

    for line in existing_line:
        line.toStr();

        sptr = line.head;
        while sptr.nextStation is not None:
            sptr.toStr();
            sptr = sptr.nextStation;

        print();

    # start = getStation(label = 'G12');
    start = getStation(label = 'BL10');
    end = getStation(label = 'BL14');

    # p = findPaths(start, end);
    p = findPaths(end, start);
    print(p)
    for i in p:
        for j in i:
            print(j.StationLabel)
