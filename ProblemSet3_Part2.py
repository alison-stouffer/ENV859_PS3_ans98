#-------------------------------------------------------------
# ProblemSet3_Part2.py
#
# Description: Problem Set 3 (Part 2)
#
# Author: Alison Stouffer (alison.stouffer@duke.edu)
# Date:   Fall 2022
#--------------------------------------------------------------

#%% Task 4.1

#Reading in the data.
fileObj = open(file='transshipment_vessels_20180723.csv', mode='r')
lineList = fileObj.readlines()
fileObj.close()

#Save the contents of the first line in the list of lines to the variable "headerLineString"
headerLineString = █

#Print the contents of the headerLine
#print(headerLineString)