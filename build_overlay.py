#!/usr/bin/env python
import json,argparse

def vrfExists(vrfDict, vrfName):
    Exists = False
    for vrf in vrfDict:
        if vrfName == vrf:
            Exists = True
    return Exists

def vlanExists(vlanDict, vlanId):
    Exists = False
    for vlan in vlanDict:
        if vlanId == vlan["vlanId"]:
            Exists = True
    return Exists

def interfaceVlanExists(interfaceVlanDict, vlanId):
    Exists = False
    for interface in interfaceVlanDict:
        if vlanId == interface["vlanId"]:
            Exists = True
    return Exists

def deviceNameExists(interfaceVlanDict, deviceName, vlanId):
    Exists = False
    for interface in interfaceVlanDict:
        if vlanId == interface["vlanId"]:
            for node in interface["nodeList"]:
                if deviceName == node["deviceName"]:
                    Exists = True
    return Exists

def getNodeList(interfaceVlanDict, vlanId):
    for interface in interfaceVlanDict:
        if vlanId == interface["vlanId"]:
            nodeList = interface["nodeList"]
    return nodeList

def updateInterfaceVlanList(nodeList, interfaceVlanList, vlanId):
    for interface in interfaceVlanList:
        if vlanId == interface["vlanId"]:
            interface["nodeList"] = nodeList
    return interfaceVlanList
#
# Define command line options for argparse
#

usage = 'usage: %prog [options]'

# Define command line options for argparse
ap = argparse.ArgumentParser()
ap.add_argument(
    "-n",
    "-device-name",
    dest="deviceName",
    action="store",
    required=True,
    help="Name of the switch having the config being parsed.",
)

ap.add_argument(
    "-r",
    "-vrf-filename",
    dest="vrfFileName",
    action="store",
    required=True,
    help="Name of the file containing VRF info.",
)

ap.add_argument(
    "-l",
    "-vlan-filename",
    dest="vlanFileName",
    action="store",
    required=True,
    help="Name of the file containing VLAN info.",
)

ap.add_argument(
    "-s",
    "-svi-filename",
    dest="sviFileName",
    action="store",
    required=True,
    help="Name of the file containing SVI info.",
)

opts = ap.parse_args()

deviceName = opts.deviceName
vrfFileName = opts.vrfFileName
vlanFileName = opts.vlanFileName
sviFileName = opts.sviFileName

vrfDBFileName = "vrfDB.txt"
vlanDBFileName = "vlanDB.txt"
sviDBFileName = "interfaceVlanDB.txt"

#
# Open all persistent DBs
#

vrfFile = open(vrfDBFileName, "r")
vlanFile = open(vlanDBFileName, "r")
interfaceVlanFile = open(sviDBFileName, "r")

vrfList = json.loads(vrfFile.read())
vlanList = json.loads(vlanFile.read())
interfaceVlanList = json.loads(interfaceVlanFile.read())

vrfFile.close()

vlanFile.close()
interfaceVlanFile.close()

#
# Collect all vrf names and put them in a list
#

inputFile = open(vrfFileName, "r")
file_contents = inputFile.read().splitlines()

for element in file_contents:
    if "vrf" in element:
        elementList = element.split(" ")
        vrfName = elementList[2]
        if not vrfExists(vrfList, vrfName):
            vrfList.append(vrfName)        

inputFile.close()

#
# Collect all VLAN interfaces
#

inputFile = open(sviFileName, "r")

line = "START"
counter = 1
while line != "":
    vlanId = ""
    description = ""
    vrfName = ""
    ipAddress = ""
    virtualIp = "None"
    interfaceVlanDict = {}
    line = inputFile.readline().rstrip("\n")

    while not "!" in line and line != "":
        if "interface" in line:
            vlanId = line.split("Vlan")[1]
        if "description" in line:
            description = line.split("description ")[1]
        if "vrf" in line:
            vrfName = line.split("vrf ")[1]
        if "ip address" in line:
            ipAddress = line.split("ip address ")[1]
        if "virtual-router" in line:
            virtualIp = line.split(" ")[6]
        line = inputFile.readline().rstrip("\n")
    
    if vlanId != "":
        if not interfaceVlanExists(interfaceVlanList, vlanId):
            nodeList = []
            nodeDict = {    "deviceName": deviceName,
                            "ipAddress": ipAddress  }
            nodeList.append(nodeDict)
            interfaceVlanDict = { "vlanId": vlanId, "description": description, "vrfName": vrfName, "virtualIp": virtualIp, "nodeList": nodeList }
            interfaceVlanList.append(interfaceVlanDict)
        elif interfaceVlanExists(interfaceVlanList, vlanId):
            nodeDict = {    "deviceName": deviceName,
                            "ipAddress": ipAddress  }    
            nodeList = getNodeList(interfaceVlanList, vlanId)
            nodeList.append(nodeDict)
            interfaceVlanList = updateInterfaceVlanList(nodeList, interfaceVlanList, vlanId)

inputFile.close()

#
# Collect all VLANs
#

inputFile = open(vlanFileName, "r")

line = "START"
while line != "":
    line = inputFile.readline().strip("\n")
    if "vlan" in line:
        vlanId = line.split(" ")[1]
        line = inputFile.readline()
        vlanName = line.split("name")[1]
        vlanDict = {"vlanId": vlanId, "vlanName": vlanName }
        if not vlanExists(vlanList, vlanId):
            vlanList.append(vlanDict)

inputFile.close()

#
# Save all persistent DBs
#

vrfDB = json.dumps(vrfList, sort_keys=True, indent=4)
vlanDB = json.dumps(vlanList, sort_keys=True, indent=4)
interfaceVlanDB = json.dumps(interfaceVlanList, sort_keys=True, indent=4)

vrfFile = open(vrfDBFileName, "w")
vlanFile = open(vlanDBFileName, "w")
interfaceVlanFile = open(sviDBFileName, "w")

vrfFile.write(vrfDB)
vlanFile.write(vlanDB)
interfaceVlanFile.write(interfaceVlanDB)

vrfFile.close()
vlanFile.close()
interfaceVlanFile.close()
