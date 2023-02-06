#!/usr/bin/env python

import json

vrfFile = open("VRFDB.txt", "r")
vrfDict = json.loads(vrfFile.read())
vrfFile.close()

for vrf in vrfDict:
    print("        %s:") % ( vrf["name"])
    print("          vrf_vni: %s") % ( vrf["vrfVni"] )
    print("          tags:")
    print("          - fabricwide")
    print("          redistribute_static: true")

vlanFile = open("VLANDB.txt", "r")
vlanDict = json.loads(vlanFile.read())
vlanFile.close()

print("        %s") % ( "svis:")

for key, value in vlanDict["SE1"].items():
    if "interface_ip" in value:
        print("          %s:") % ( key )
        print("            name: %s") % ( value["name"] )
        print("            enabled: true")
        print("            arp_aging_timeout: 900")
        print("            mtu: 9000")
        print("            ip_address_virtual: %s/%s") % ( value["interface_ip"], value["interface_subnet"] )
        if "ip_helper" in value:
            print("            ip_helpers:")
            for ipHelper in value["ip_helper"]:
                print("              %s:") % ipHelper
        print("            tags:")
        print("            - fabricwide")
        print("            vrf: %s") % ( value["vrf"] )

print("============================================================================================")
for key, value in vlanDict["SE1"].items():
    if not "interface_ip" in value:
        print("      %s:") % ( key )
        print("        name: %s") % ( value["name"])
        print("        tags:")
        print("        - fabricwide")
