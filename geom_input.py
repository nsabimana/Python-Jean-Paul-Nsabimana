__author__ = 'jean'

import sys

print(sys.argv)
## called as $ python3 input_cl2.py -v 1 --somearg "five"

import argparse

parser = argparse.ArgumentParser(description='demonstration.')
parser.add_argument('-v', type=int, dest = 'theint',
                   help='an integer')
parser.add_argument('--somearg', dest = 'thestring', type=str,
                   help='a string')
parser.add_argument('-u', dest='uncalled', type=float, default=42.0,
                   help='an optional arg')

args = parser.parse_args()
print("\n", args, args.thestring, args.theint)


something = input("enter something:")
while something != "stop":
    print(something)
    something = input("enter something, 'stop' to stop:")

anumber = None

while anumber != -1:
    try:
        anumber = int(input("enter an integer, -1 to stop:"))
    except (TypeError, ValueError) as err:
        print(err.args[0])
    else:
        print("success", anumber)

something = input("enter something:")
while something != "stop":
    print(something)
    something = input("enter something, 'stop' to stop:")

anumber = None

while anumber != -1:
    try:
        anumber = int(input("enter an integer, -1 to stop:"))
    except (TypeError, ValueError) as err:
        print(err.args[0])
    else:
        print("success", anumber)


myfile = open("filename.csv",'r') # 'r' is for read

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

with open("filename.csv",'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        print(row)