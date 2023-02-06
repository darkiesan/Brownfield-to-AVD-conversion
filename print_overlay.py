#!/usr/bin/env python
import json

def interfaceVlanExists(interfaceVlanDict, vlanId):
    Exists = False
    for interface in interfaceVlanDict:
        if vlanId == interface["vlanId"]:
            Exists = True
    return Exists

#
# Set needed variables
#

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
# Print AVD output for l2vlans
#

print ("%s") % ( "tenants:" )
print ("  %s") % ( "ASSA:" )
print ("    %s") % ( "mac_vrf_vni_base: 10000" )
print ("    %s") % ( "l2vlans:" )

for vlan in vlanList:
    myVlanId = vlan["vlanId"]
    myVlanName = vlan["vlanName"]
    if not interfaceVlanExists(interfaceVlanList, myVlanId):
        print("      %s:") % ( myVlanId )
        print("        name: %s") % ( myVlanName )
        print("        tags:")
        print("        - fabricwide")

#
# Print AVD output for VRFs and SVIs
#

print ("    %s") % ( "vrfs:" )
counter = 1
for vrf in vrfList:
    myVrfName = vrf
    print("      %s:") % ( myVrfName )
    print("        vrf_vni: %s") % ( counter )
    print("        svis:")

    for vlan in interfaceVlanList:
        if myVrfName == vlan["vrfName"]:
            print("          %s:") % ( vlan["vlanId"] )
            print("            name: %s") % ( vlan["description"])
            print("            enabled: true")
            print("            mtu: 9000")
            print("            arp_aging_timeout: 900")
            print("            tags:")
            print("            - fabricwide")
            if vlan["virtualIp"] != "None":
                print("            ip_virtual_router_address: %s") % ( vlan["virtualIp"])
            print("            nodes:")
            for node in vlan["nodeList"]:
                print ("              %s:") % ( node["deviceName"] )
                print ("                ip_address: %s") % ( node["ipAddress"])
    counter = counter + 1