#!/usr/bin/env python

import json,argparse

def vlanExists(vlanDict, vlanId):
    Exists = False
    for vlan in vlanDict:
        if vlanId in vlan["vlanId"]:
            Exists = True
    return Exists

def trunkNameExists(trunkList, trunkName):
    Exists = False
    for vlan in trunkList:
        if vlan["trunkName"] == trunkName:
            Exists = True
    return Exists

def getVlanList(trunkList, trunkName):
    vlanList = []
    for vlan in trunkList:
        if vlan["trunkName"] == trunkName:
            vlanList = vlan["vlanId"]
    return vlanList

#
# Define command line options for argparse
#

usage = 'usage: %prog [options]'

# Define command line options for argparse
ap = argparse.ArgumentParser()

ap.add_argument(
    "-l",
    "-vlan-filename",
    dest="vlanFileName",
    action="store",
    required=True,
    help="Name of the file containing VLAN info.",
)
opts = ap.parse_args()

vlanFileName = opts.vlanFileName
trunkDBFileName = "trunkDB.txt"

#
# Open persistent DBs
#

trunkDBFile = open(trunkDBFileName, "r")
trunkList = json.loads(trunkDBFile.read())
trunkDBFile.close()

#
# Collect all info
#

inputFile = open(vlanFileName, "r")

line = inputFile.readline().rstrip("\n")
line = "START"

while line != "":
    vlanId = ""
    trunkName = ""
    trunkGroupList = []

    line = inputFile.readline().rstrip("\n")
    while not "!" in line and line != "":
        if "vlan" in line:
            vlanId = line.split("vlan")[1]
        if "trunk" in line:
            trunkName = line.split("group ")[1]
            trunkGroupList.append(trunkName)
        line = inputFile.readline().rstrip("\n")

    for trunkGroupName in trunkGroupList:
        if trunkGroupName != "":
            if not vlanExists(trunkList, vlanId) and not trunkNameExists(trunkList, trunkGroupName):
                vlanList = []
                vlanList.append(vlanId)
                trunkDict = {
                                "vlanId": vlanList,
                                "trunkName": trunkGroupName
                            }
                trunkList.append(trunkDict)
            elif trunkNameExists(trunkList, trunkGroupName) and not vlanExists(trunkList, vlanId):
                vlanList = getVlanList(trunkList, trunkGroupName)
                vlanList.append(vlanId)
                trunkDict = {
                                "vlanId": vlanList,
                                "trunkName": trunkGroupName
                            }
                trunkList.append(trunkDict)
            elif vlanExists(trunkList, vlanId) and trunkNameExists(trunkList, trunkGroupName):
                vlanList = getVlanList(trunkList, trunkGroupName)
                if not vlanId in vlanList:
                    vlanList.append(vlanId)
                    trunkDict = {
                                "vlanId": vlanList,
                                "trunkName": trunkGroupName
                                }
                    trunkList.append(trunkDict)
                    
inputFile.close()

#
# Save all persistent DBs
#

trunkDB = json.dumps(trunkList, sort_keys=True, indent=4)

trunkDBFile = open(trunkDBFileName, "w")
trunkDBFile.write(trunkDB)
trunkDBFile.close()
