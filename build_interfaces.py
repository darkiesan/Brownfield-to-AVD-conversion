#!/usr/bin/env python

import json,argparse

def resolveTrunk(trunkName, trunkDict):
    vlanId = 0
    vlanList = []
    for trunkGroup in trunkDict:
        if trunkName == trunkGroup["trunkName"]:
            vlanList = trunkGroup["vlanId"]
    return vlanList

def parseFile(inputFile, trunkDict):
    interfaceList = []
    line = "START"

    interfaceName = ""
    description = "### UNUSED ###"
    switchportMode = ""
    spanningTree = False
    vlanList = []
    mlag = ""
    channelGroup = ""

    while line != "":
        interfaceName = ""
        description = "### UNUSED ###"
        switchportMode = ""
        spanningTree = False
        vlanList = []
        mlag = ""
        channelGroup = ""

        line = inputFile.readline().rstrip("\n")
        while not "!" in line and line != "":
            if "interface" in line:
                interfaceName = line.split("interface ")[1]
            if "description" in line:
                description = line.split("description ")[1]
            if "mode" in line:
                switchportMode = "trunk"
            if "access vlan" in line:
                switchportMode = "access"
                accessVlan = line.split("vlan ")[1]
            if "trunk group" in line:
                myVlanList = resolveTrunk(line.split("group ")[1], trunkDict)
                vlanList = vlanList + myVlanList
            if "mlag" in line:
                mlag = line.split("mlag ")[1]
            if "channel-group" in line:
                channelGroup = line.split(" ")[4]
            if "spanning-tree" in line:
                spanningTree = True
            line = inputFile.readline().rstrip("\n")

        if "Port-Channel" in interfaceName:
            if mlag != "" and switchportMode == "trunk":
                interfaceDict = {
                                    "interfaceName": interfaceName,
                                    "description": description,
                                    "switchportMode": switchportMode,
                                    "vlanList": vlanList,
                                    "mlag": mlag,
                                    "spanningTree": spanningTree
                                }
            if mlag != "" and switchportMode == "access":
                interfaceDict = {
                                    "interfaceName": interfaceName,
                                    "description": description,
                                    "switchportMode": switchportMode,
                                    "accessVlan": accessVlan,
                                    "spanningTree": spanningTree,
                                    "mlag": mlag
                                }
            if mlag == "" and switchportMode == "trunk":
                interfaceDict = {
                                    "interfaceName": interfaceName,
                                    "description": description,
                                    "switchportMode": switchportMode,
                                    "vlanList": vlanList,
                                    "spanningTree": spanningTree
                                }
            if mlag == "" and switchportMode == "access":
                interfaceDict = {
                                    "interfaceName": interfaceName,
                                    "description": description,
                                    "switchportMode": switchportMode,
                                    "accessVlan": accessVlan,
                                    "spanningTree": spanningTree
                                }
            interfaceList.append(interfaceDict)
        
        if "Ethernet" in interfaceName:
            if channelGroup != "":
                interfaceDict = {
                                    "interfaceName": interfaceName,
                                    "description": description,
                                    "channelGroup": channelGroup
                                }
            if channelGroup == "" and switchportMode == "access":
                interfaceDict = {
                                    "interfaceName": interfaceName,
                                    "description": description,
                                    "switchportMode": switchportMode,
                                    "accessVlan": accessVlan,
                                    "spanningTree": spanningTree
                                }
            if channelGroup == "" and switchportMode == "trunk":
                interfaceDict = {
                                    "interfaceName": interfaceName,
                                    "description": description,
                                    "switchportMode": switchportMode,
                                    "vlanList": vlanList,
                                    "spanningTree": spanningTree
                                }
            interfaceList.append(interfaceDict)

    return interfaceList

def switchExists(interfaceDict, switchName):
    Exists = False
    for switch in interfaceDict:
        if switch["switchName"] == switchName:
            Exists = True
    return Exists

#
# Define command line options for argparse
#

usage = 'usage: %prog [options]'

# Define command line options for argparse
ap = argparse.ArgumentParser()
ap.add_argument(
    "-n1",
    "-device-name-1",
    dest="deviceName1",
    action="store",
    required=True,
    help="Name of the first switch having the config being parsed.",
)

ap.add_argument(
    "-n2",
    "-device-name-2",
    dest="deviceName2",
    action="store",
    required=True,
    help="Name of the second switch having the config being parsed.",
)

ap.add_argument(
    "-i1",
    "-interface-filename-1",
    dest="interfaceFileName1",
    action="store",
    required=True,
    help="Name of the first file containing interface info.",
)

ap.add_argument(
    "-i2",
    "-interface-filename-2",
    dest="interfaceFileName2",
    action="store",
    required=True,
    help="Name of the second file containing interface info.",
)

opts = ap.parse_args()

deviceName1 = opts.deviceName1
deviceName2 = opts.deviceName2
interfaceFileName1 = opts.interfaceFileName1
interfaceFileName2 = opts.interfaceFileName2

trunkDBFileName = "trunkDB.txt"
interfaceDBFileName = "interfaceDB.txt"
pairDBFileName = "pairDB.txt"

trunkDBFile = open(trunkDBFileName, "r")
trunkList = json.loads(trunkDBFile.read())
trunkDBFile.close()

interfaceDBFile = open(interfaceDBFileName, "r")
interfaceDB = json.loads(interfaceDBFile.read())
interfaceDBFile.close()

pairDBFile = open(pairDBFileName, "r")
pairDB = json.loads(pairDBFile.read())
pairDBFile.close()

newPairList = []
addedPair = False

if not switchExists(interfaceDB, deviceName1):
    inputFile = open(interfaceFileName1, "r")
    interfaceList = parseFile(inputFile, trunkList)
    interfaceDict = {
                        "switchName": deviceName1,
                        "interfaceList": interfaceList
                    }
    interfaceDB.append(interfaceDict)
    newPairList.append(interfaceDict)
    inputFile.close()

if not switchExists(interfaceDB, deviceName2):
    inputFile = open(interfaceFileName2, "r")
    interfaceList = parseFile(inputFile, trunkList)
    interfaceDict = {
                        "switchName": deviceName2,
                        "interfaceList": interfaceList
                    }
    interfaceDB.append(interfaceDict)
    newPairList.append(interfaceDict)
    inputFile.close()
    addedPair = True

if addedPair:
    newPairDict = {
                    "switchpair": deviceName1 + "-" + deviceName2,
                    "switches": newPairList
                    }
    pairDB.append(newPairDict)

interfaceDBFile = open(interfaceDBFileName, "w")
interfaceDBFile.write(json.dumps(interfaceDB, sort_keys=True, indent=4))
interfaceDBFile.close()

pairDBFile = open(pairDBFileName, "w")
pairDBFile.write(json.dumps(pairDB, sort_keys=True, indent=4))
pairDBFile.close()