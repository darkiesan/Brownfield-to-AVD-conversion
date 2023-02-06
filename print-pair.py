#!/usr/bin/env python

import json

def mlagExists(mlagList, mlagId):
    Exists = False
    for mlagInterface in mlagList:
        if mlagId == mlagInterface["mlagId"]:
            Exists = True
    return Exists

def getMlagMembers(interfaceList, mlagId):
    mlagMemberList = []
    for interface in interfaceList:
        if "channelGroup" in interface:
            if mlagId == interface["channelGroup"]:
                mlagMemberList.append(interface["interfaceName"])
    return mlagMemberList

def findMlagInterface(mlagInterfaceList, mlagId, deviceName):
    counter = 0
    found = False
    for mlagInterface in mlagInterfaceList:
        if mlagInterface["mlagId"] == mlagId and deviceName in mlagInterface["deviceList"]:
            found = True
        if not found:
            counter = counter + 1
    return counter

def isMyNeighbor(deviceName, mlagInterfaceList):
    Exists = False
    for mlagInterface in mlagInterfaceList:
        if deviceName in mlagInterface["deviceList"]:
            Exists = True
    return Exists

def getNeighbor(switchPair, myName):
    deviceName1 = switchPair.split("-")[0]
    deviceName2 = switchPair.split("-")[1]
    if deviceName1 == myName:
        return deviceName2
    else:
        return deviceName1

pairDBFileName = "pairDB.txt"
pairDBFile = open(pairDBFileName, "r")
pairDB = json.loads(pairDBFile.read())
pairDBFile.close()

mlagInterfaces = []
portChannels = []
ethernetInterfaces = []

for pairs in pairDB:
    for switches in pairs["switches"]:
        deviceName = switches["switchName"]
        neighborName = getNeighbor(pairs["switchpair"], deviceName)
        for interface in switches["interfaceList"]:
            if "mlag" in interface:
                if not mlagExists(mlagInterfaces, interface["mlag"]):
                    deviceList = []
                    deviceList.append(deviceName)
                    mlagMemberList = getMlagMembers(switches["interfaceList"], interface["mlag"])
                    if interface["switchportMode"] == "trunk":
                        mlagInterface = {
                                            "mlagId": interface["mlag"],
                                            "interfaceName": interface["interfaceName"],
                                            "deviceList": deviceList,
                                            "description": interface["description"],
                                            "spanningTree": interface["spanningTree"],
                                            "switchportMode": interface["switchportMode"],
                                            "mlagMemberList": mlagMemberList,
                                            "vlanList": interface["vlanList"]
                                            }
                    else:
                        mlagInterface = {
                                            "mlagId": interface["mlag"],
                                            "interfaceName": interface["interfaceName"],
                                            "deviceList": deviceList,
                                            "description": interface["description"],
                                            "spanningTree": interface["spanningTree"],
                                            "switchportMode": interface["switchportMode"],
                                            "mlagMemberList": mlagMemberList,
                                            "vlanList": interface["accessVlan"]
                                            }

                    mlagInterfaces.append(mlagInterface)

                elif mlagExists(mlagInterfaces, interface["mlag"]) and isMyNeighbor(neighborName, mlagInterfaces):
                    mlagInterfaceIdx = findMlagInterface(mlagInterfaces, interface["mlag"], neighborName)
                    if deviceName not in mlagInterfaces[mlagInterfaceIdx]["deviceList"]:
                        mlagInterfaces[mlagInterfaceIdx]["deviceList"].append(deviceName)
                        mlagMemberList = getMlagMembers(switches["interfaceList"], interface["mlag"])
                        mlagInterfaces[mlagInterfaceIdx]["mlagMemberList"].extend(mlagMemberList)

                elif mlagExists(mlagInterfaces, interface["mlag"]) and not isMyNeighbor(neighborName, mlagInterfaces):
                    deviceList = []
                    deviceList.append(deviceName)
                    mlagMemberList = getMlagMembers(switches["interfaceList"], interface["mlag"])
                    if interface["switchportMode"] == "trunk":
                        mlagInterface = {
                                            "mlagId": interface["mlag"],
                                            "interfaceName": interface["interfaceName"],
                                            "deviceList": deviceList,
                                            "description": interface["description"],
                                            "spanningTree": interface["spanningTree"],
                                            "switchportMode": interface["switchportMode"],
                                            "mlagMemberList": mlagMemberList,
                                            "vlanList": interface["vlanList"]
                                            }
                    else:
                        mlagInterface = {
                                            "mlagId": interface["mlag"],
                                            "interfaceName": interface["interfaceName"],
                                            "deviceList": deviceList,
                                            "description": interface["description"],
                                            "spanningTree": interface["spanningTree"],
                                            "switchportMode": interface["switchportMode"],
                                            "mlagMemberList": mlagMemberList,
                                            "vlanList": interface["accessVlan"]
                                            }

                    mlagInterfaces.append(mlagInterface)

            if not "mlag" in interface and "Port-Channel" in interface["interfaceName"] and not "2000" in interface["interfaceName"]:
                LagMemberList =  getMlagMembers(switches["interfaceList"], interface["interfaceName"].split("Port-Channel")[1])
                if interface["switchportMode"] == "trunk":
                    LagInterface = {
                                        "interfaceName": interface["interfaceName"],
                                        "description": interface["description"],
                                        "spanningTree": interface["spanningTree"],
                                        "switchportMode": interface["switchportMode"],
                                        "LagMemberList": LagMemberList,
                                        "vlanList": interface["vlanList"],
                                        "deviceName": deviceName                             
                                    }
                else:
                    LagInterface = {
                                        "interfaceName": interface["interfaceName"],
                                        "description": interface["description"],
                                        "spanningTree": interface["spanningTree"],
                                        "switchportMode": interface["switchportMode"],
                                        "LagMemberList": LagMemberList,
                                        "vlanList": interface["accessVlan"],
                                        "deviceName": deviceName                             
                                    }

                portChannels.append(LagInterface)

            if "Ethernet" in interface["interfaceName"] and not "channelGroup" in interface:
                if interface["switchportMode"] == "trunk":
                    ethernetInterface = {
                                        "interfaceName": interface["interfaceName"],
                                        "description": interface["description"],
                                        "spanningTree": interface["spanningTree"],
                                        "switchportMode": interface["switchportMode"],
                                        "vlanList": interface["vlanList"],
                                        "deviceName": deviceName                             
                                        }
                if interface["switchportMode"] == "access":
                    ethernetInterface = {
                                        "interfaceName": interface["interfaceName"],
                                        "description": interface["description"],
                                        "spanningTree": interface["spanningTree"],
                                        "switchportMode": interface["switchportMode"],
                                        "vlanList": interface["accessVlan"],
                                        "deviceName": deviceName                             
                                        }
                ethernetInterfaces.append(ethernetInterface)

mlagInterfacesFile = open("mlagInterfacesDB.txt","w")
mlagInterfacesFile.write(json.dumps(mlagInterfaces, sort_keys=True, indent=4))
mlagInterfacesFile.close()

print("servers:")

for interface in mlagInterfaces:
    if not len(interface["mlagMemberList"]) == 0:
        description = interface["description"] + "-" + "_".join(interface["deviceList"]) + "-" + interface["interfaceName"]
        description.replace(" ","-")

        print("  %s:") % ( description )
        print("    adapters:")
        print("    - mode: %s") % ( interface["switchportMode"])
        print("      port_channel:")
        print("        description: %s") % ( interface["description"] )
        print("        mode: active")
        print("        state: present")
        print("      server_ports:")
        for member in interface["mlagMemberList"]:
            print("      - %s") % ( member )
        print("      switch_ports:")
        for member in interface["mlagMemberList"]:
            print("      - %s") % ( member )
        print("      switches:")
        for device in interface["deviceList"]:
            if len(interface["mlagMemberList"]) > 2:
                print("      - %s") % ( device )
                print("      - %s") % ( device )
            else:
                print("      - %s") % ( device )
        if interface["spanningTree"]:
            print("      spanning_tree_portfast: edge")
            print("      spanning_tree_bpduguard: true")
        if interface["switchportMode"] == "trunk":
            if not len(interface["vlanList"]) == 0:
                print("      vlans: '%s'") % ( ",".join(interface["vlanList"]).replace(" ","") )
        else:
            print("      vlans: '%s'") % ( interface["vlanList"] )

for interface in portChannels:
    description = interface["description"] + "-" + interface["deviceName"] + "-" + interface["interfaceName"]
    description.replace(" ","-")
    
    print("  %s:") % ( description )
    print("    adapters:")
    print("    - mode: %s") % ( interface["switchportMode"])
    print("      port_channel:")
    print("        description: %s") % ( interface["description"] )
    print("        mode: active")
    print("        state: present")
    print("      server_ports:")
    for member in interface["LagMemberList"]:
        print("      - %s") % ( member )
    print("      switch_ports:")
    for member in interface["LagMemberList"]:
        print("      - %s") % ( member )
    print("      switches:")
    print("      - %s") % ( interface["deviceName"] )
    print("      - %s") % ( interface["deviceName"] )
    if interface["spanningTree"]:
        print("      spanning_tree_portfast: edge")
        print("      spanning_tree_bpduguard: true")
    if interface["switchportMode"] == "trunk":
        if not len(interface["vlanList"]) == 0:
            print("      vlans: '%s'") % ( ",".join(interface["vlanList"]).replace(" ","") )
    else:
            print("      vlans: '%s'") % ( interface["vlanList"] )

for interface in ethernetInterfaces:
    if interface["description"] == "### UNUSED ###":
        description = "UNUSED"
    else:
        description = interface["description"].replace(" ","-")

    print("  %s:") % ( description + "-" + interface["deviceName"] + "-" + interface["interfaceName"] )
    print("    adapters:")
    print("    - mode: %s") % ( interface["switchportMode"])
    print("      description: %s") % ( description )
    print("      server_ports:")   
    print("      - ETH0")
    print("      switch_ports:")
    print("      - %s") % ( interface["interfaceName"] )
    print("      switches:")
    print("      - %s") % ( interface["deviceName"] )
    if interface["spanningTree"]:
        print("      spanning_tree_portfast: edge")
        print("      spanning_tree_bpduguard: true")
    if interface["switchportMode"] == "trunk":
        if not len(interface["vlanList"]) == 0:
            print("      vlans: '%s'") % ( ",".join(interface["vlanList"]).replace(" ","") )
    if interface["switchportMode"] == "access":
        print("      vlans: '%s'") % ( interface["vlanList"] )