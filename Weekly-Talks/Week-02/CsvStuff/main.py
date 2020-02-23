"""
This file opens a folder of csv data files and counts how many lines of data are in each.
Its helpful in the fact that lots of research requires processing folders full of data, and 
this shows you at least how to scan a specific folder and "look" at each file. Future work
is obviously to calculate some aggregate values or specific stats for each file. 
"""
import os
from os import walk

mypath = "./Data/baseballdatabank/core"

# get all the csv files from the above directory
files = []
for (dirpath, dirnames, filenames) in walk(mypath):
    files.extend(filenames)

lineCount = 0
for f in files:
    # we need to append the path to each file so we know where to open from
    fp = open(os.path.join(mypath,f),"r")

    # read each line into a list
    data = fp.readlines()

    # add the files line count to a total
    lineCount += len(data)-1 # -1 for the headers in a csv

# print out totals
print(f"There are {lineCount} lines of data in {len(files)} files.")
