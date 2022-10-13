#-------------------------------------------------------------
# ProblemSet3_Part2.py
#
# Description: Problem Set 3 (Part 2)
#
# Author: Alison Stouffer (alison.stouffer@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

#%% Task 4.1

fileObj = open(file='transshipment_vessels_20180723.csv', mode='r')
lineList = fileObj.readlines()
fileObj.close()

headerLineString = lineList[0]

print(headerLineString)

#%% Task 4.2

headerItems = headerLineString.split(sep=',')

mmsi_idx  = headerItems.index('mmsi')
name_idx  = headerItems.index('shipname')
fleet_idx = headerItems.index('fleet_name')

print(mmsi_idx,name_idx,fleet_idx)

#%% Task 4.3

vesselDict = {}

for lineString in lineList:

    if lineString[0] == 'm':
        continue
    
    lineData = lineString.split(sep=',')

    mmsi = lineData[0]
    fleet = lineData[4]

    vesselDict[mmsi] = fleet

#%% Task 4.4

vesselID = '258799000'

for the_key, the_value in vesselDict.items():
    
    if the_key == vesselID:
       print(f"Vessel #{vesselID} flies the flag of {the_value}")