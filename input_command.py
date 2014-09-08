__author__ = 'jean'

import sys



myfile = open("input_geom.csv",'r') # 'r' is for read

print("first pass\n")
for line in myfile:
    print(line)

print("second pass\n")
for line in myfile:
    print(line)

myfile.seek(0) # need to reset position in file

print("works this time?\n")
for line in myfile:
    print(line.rstrip())

myfile.close()

print("\nnow with csv:")

import csv

with open("input_geom.csv",'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        print(row)