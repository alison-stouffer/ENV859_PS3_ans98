#-------------------------------------------------------------
# ProblemSet3_Part1.py
#
# Description: Problem Set 3 (Part 1)
#
# Author: Alison Stouffer (alison.stouffer@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

#%% Task 1: Python Syntax & Code Manipulation

mountain  = "Denali"
nickname  = "Mt. McKinley"
elevation = "20322"

print (mountain + ", formerly\nknown as " "\"" + nickname + "\"" + "\nis " + elevation + "\' above sea level.")

#%% Task 2: Lists & Iteration

data_folder = "W:\859_data\\tri_state"
data_list   = ["roads.shp", "road_types.dbf", "naip_imagery.tif"]
user_item   = "streams.shp"

data_list.append(user_item)

for item in data_list:
    print(data_folder + "\\" + item)

#%% Task 3: Lists & Iteration

user_numbers = []

for x in range(1, 4):
    user_numbers.append(int(input("Enter an integer: ")))

user_numbers.sort()

print(user_numbers[2])

#%% Task 3: Challenge

user_numbers = []

for x in range(1, 4):
    user_numbers.append(int(input("Enter an integer: ")))

user_numbers.sort(reverse=True)

print(user_numbers)  