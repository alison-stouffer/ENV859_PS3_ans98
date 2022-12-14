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

    mmsi  = lineData[0]
    fleet = lineData[4]

    vesselDict[mmsi] = fleet

#%% Task 4.4

vesselID = '258799000'

for the_key, the_value in vesselDict.items():
    
    if the_key == vesselID:
       print(f"Vessel #{vesselID} flies the flag of {the_value}")
       
#%% Task 5

#Read contents of data file:
fileObj = open(file='loitering_events_20180723.csv', mode='r')
lineList = fileObj.readlines()
fileObj.close()

#Create header index:
headerLineString = lineList[0]
headerItems = headerLineString.split(sep=',')

#Create empty dictionary for targeted vessels that meet criteria:
targetDict = {}

#Read each line of data:
for lineString in lineList:

    if lineString[0] == 't':
        continue
    
    #Split the string into a list of data items:
    lineData = lineString.split(sep=',')

    #Extract items in list into variables:
    mmsi       = lineData[0]
    start_lat  = float(lineData[1])
    end_lat    = float(lineData[3])
    start_long = float(lineData[2])

    #Add vessel information to dictionary, if criteria is met:
    if start_lat < 0 and end_lat > 0 and 165 < start_long < 170:
        targetDict[mmsi] = (start_lat, end_lat, start_long)
 
#Create an empty key list:
matching_keys = []

#Extract intersecting keys in latitude and longitude dictionaries:
for the_key in targetDict:
    if the_key in vesselDict:
        matching_keys.append(the_key)
     
#Display message if criteria are not met:
if len(matching_keys) == 0:
    print("No vessels meet criteria")

#Display message if criteria are met:
for the_key, the_value in vesselDict.items():
    if the_key in matching_keys:
        print(f"Vessel #{the_key} flies the flag of {the_value}")
