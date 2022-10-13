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

#Create empty latitude and longitude dictionaries:
latDict  = {}
longDict = {}

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

    #Add start and end latitudes to dictionary, if criteria is met:
    if start_lat < 0 and end_lat > 0:
        latDict[mmsi] = (start_lat, end_lat)
    #Add start longitude to dictionary, if criteria is met:
    if 165 < start_long < 170:
        longDict[mmsi] = (start_long)
 
#Create an empty key list:
matching_keys = []


#use the value of the transmission_mmsi for the current line to query the vesselsDict created above to print the vessel’s mmsi and its fleet.

#Extract intersecting keys in latitude and longitude dictionaries:
for the_key in longDict:
    if the_key in latDict:
        matching_keys.append(the_key)




#BONUS: If no vessels meet your criteria, print a message that states “No vessels met criteria”
     
# Report whether no keys were found.
if len(matching_keys) == 0:
    print(f"Sara was not located on {user_date}")

#Reveal locations for each key in matching_keys.
for matching_key in matching_keys:
    obs_lat, obs_lon = location_dict[matching_key]
    print(f"Record {matching_key} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {user_date}")
    




