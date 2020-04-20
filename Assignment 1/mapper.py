#!/usr/bin/env python3

inputFile = "".join(open("data.txt", "r").read().split("."))
currBiagram = ""

for index in range(0,1000,2):
    currBiagram = inputFile[index]+inputFile[index+1]
    print("%s\t%d" % (currBiagram,1))
















