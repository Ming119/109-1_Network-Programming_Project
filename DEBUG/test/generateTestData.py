# generateTestData.py
#
# This program runs in Python 3.8
#
import json


print("===== Generating Test Data =====");
fileID = 0;
with open('./API/routeAPI.json', 'r') as f:
    routeData = json.load(f);
    for line1 in range(1, len(routeData)+1):
        for line2 in range(1, len(routeData)+1):
            for station1 in range(1, len(routeData[line1-1]['LineStations'])+1):
                for station2 in range(1, len(routeData[line2-1]['LineStations'])+1):
                    with open('./DEBUG/input/%d.txt' %fileID, 'w') as testfile:
                        testfile.write("%d\n%d\n%d\n%d\n" %(line1, station1, line2, station2));

                    fileID += 1;

print("===== Finish! Generated %d files===== " %fileID);
