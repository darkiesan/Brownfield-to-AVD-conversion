#!/usr/bin/env python

switchList = [
                # { 
                #   "switchName": "USDC1NSD103",
                #   "interfaceName": [ 'Ethernet1', 'Ethernet3', 'Ethernet9', 'Ethernet10', 'Ethernet11', 'Ethernet12', 'Ethernet13', 'Ethernet14', 'Ethernet15', 'Ethernet16', 'Ethernet18', 'Ethernet20', 'Ethernet23', 'Ethernet24', 'Ethernet27', 'Ethernet33', 'Ethernet34', 'Ethernet35', 'Ethernet36', 'Ethernet37', 'Ethernet38', 'Ethernet39', 'Ethernet44', 'Ethernet47', 'Ethernet48', 'Ethernet53/1', 'Ethernet54/1', 'Ethernet55/1', 'Ethernet56/1' ]
                # },
                # {
                #   "switchName": "USDC1NSD104",
                #   "interfaceName": [ 'Ethernet9', 'Ethernet10', 'Ethernet11', 'Ethernet12', 'Ethernet13', 'Ethernet14', 'Ethernet15', 'Ethernet16', 'Ethernet18', 'Ethernet20', 'Ethernet24', 'Ethernet28', 'Ethernet33', 'Ethernet35', 'Ethernet37', 'Ethernet39', 'Ethernet47', 'Ethernet48', 'Ethernet53/1', 'Ethernet54/1', 'Ethernet55/1', 'Ethernet56/1' ]
                # }
                # {
                # "switchName": "USDC1NSD105",
                # "interfaceName": [ 'Ethernet9', 'Ethernet13', 'Ethernet14', 'Ethernet15', 'Ethernet16', 'Ethernet17', 'Ethernet18', 'Ethernet19', 'Ethernet20', 'Ethernet22', 'Ethernet23', 'Ethernet24', 'Ethernet25', 'Ethernet26', 'Ethernet27', 'Ethernet28', 'Ethernet29', 'Ethernet30', 'Ethernet31', 'Ethernet32', 'Ethernet33', 'Ethernet34', 'Ethernet35', 'Ethernet36', 'Ethernet37', 'Ethernet38', 'Ethernet39', 'Ethernet40', 'Ethernet41', 'Ethernet42', 'Ethernet43', 'Ethernet44', 'Ethernet45', 'Ethernet46', 'Ethernet47', 'Ethernet48', 'Ethernet53/1', 'Ethernet54/1', 'Ethernet55/1', 'Ethernet56/1' ]
                # },
                # {
                # "switchName": "USDC1NSD106",
                # "interfaceName": [ 'Ethernet9', 'Ethernet13', 'Ethernet14', 'Ethernet15', 'Ethernet16', 'Ethernet17', 'Ethernet18', 'Ethernet19', 'Ethernet20', 'Ethernet22', 'Ethernet23', 'Ethernet24', 'Ethernet25', 'Ethernet26', 'Ethernet27', 'Ethernet28', 'Ethernet29', 'Ethernet30', 'Ethernet31', 'Ethernet32', 'Ethernet33', 'Ethernet34', 'Ethernet35', 'Ethernet36', 'Ethernet37', 'Ethernet38', 'Ethernet39', 'Ethernet40', 'Ethernet41', 'Ethernet42', 'Ethernet43', 'Ethernet44', 'Ethernet45', 'Ethernet46', 'Ethernet47', 'Ethernet48', 'Ethernet53/1', 'Ethernet54/1', 'Ethernet55/1', 'Ethernet56/1' ]
                # }
                {
                  "switchName": "USDC1NSE101",
                  "interfaceName": [ 'Ethernet5', 'Ethernet6', 'Ethernet7', 'Ethernet8', 'Ethernet15', 'Ethernet16', 'Ethernet17', 'Ethernet18', 'Ethernet19', 'Ethernet20', 'Ethernet54/1' ]
                },
                {
                  "switchName": "USDC1NSE102",
                  "interfaceName": [ 'Ethernet5', 'Ethernet6', 'Ethernet7', 'Ethernet8', 'Ethernet15', 'Ethernet16', 'Ethernet17', 'Ethernet18', 'Ethernet19', 'Ethernet20', 'Ethernet24', 'Ethernet26', 'Ethernet28', 'Ethernet37', 'Ethernet54/1' ]
                }

                # "USDC2NSD101": [],
                # "USDC2NSD102": [],
                # "USDC2NSD103": [],
                # "USDC2NSD104": [],
                # "USDC2NSD105": [],
                # "USDC2NSE106": [],
                # "USDC2NSE102": [],
                ]

for switch in switchList:
    switchName = switch["switchName"]
    for interfaceName in switch["interfaceName"]:
        print ("  %s_%s_Unused_ports:") % ( switchName, interfaceName )
        print ("    adapters:")
        print ("      - mode: trunk")
        print ("        enabled: false")
        print ("        switches:")
        print ("        - %s") % ( switchName )
        print ("        switch_ports:")
        print ("        - %s") % ( interfaceName )
        print ("        description: UNUSED")
        print ("        server_ports:")
        print ("        - ETH0")