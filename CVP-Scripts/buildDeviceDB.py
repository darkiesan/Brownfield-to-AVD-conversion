#!/usr/bin/env python2

import argparse
import cvp
import json

#
# Define supporting function
#

# def getCommonConfig(server, switchName):
    
#     return config

#
# Define command line options for argparse
#

usage = 'usage: %prog [options]'

ap = argparse.ArgumentParser()
ap.add_argument(
    "-c",
    "--cvphostname",
    dest="cvphostname",
    action="store",
    required=True,
    help="CVP host name FQDN or IP",
)

ap.add_argument(
    "-u",
    "--cvpusername",
    dest="cvpusername",
    action="store",
    required=True,
    help="CVP username",
)

ap.add_argument(
    "-p",
    "--cvppassword",
    dest="cvppassword",
    action="store",
    required=True,
    help="CVP password",
)

ap.add_argument(
    "-d",
    "--debug",
    dest="debug",
    action="store_true",
    help="If debug is set, nothing will actually be sent to CVP and only debug is sent to terminal",
    default=False,
)
ap.add_argument(
    "-t",
    "--trace",
    dest="trace",
    action="store_true",
    help="If trace is set, there will be trace messages to terminal",
    default=False,
)

opts = ap.parse_args()

#
# Assign command line options to variables and assign static variables.
#

host = opts.cvphostname
user = opts.cvpusername
password = opts.cvppassword
debug = opts.debug
trace = opts.trace

#
# Define constants
#

# Switches = [ 'USDC1NSC101', 'USDC1NSC102', 'USDC1NSE101', 'USDC1NSE102', 'USDC1NSD101', 'USDC1NSD102', 'USDC1NSD103', 'USDC1NSD104', 'USDC1NSD105', 'USDC1NSD106', 'USDC2NSC101', 'USDC2NSC102', 'USDC2NSE101', 'USDC2NSE102', 'USDC2NSD101', 'USDC2NSD102', 'USDC2NSD103', 'USDC2NSD104', 'USDC2NSD105', 'USDC2NSD106' ]
Switches = [ 'DEDUSNSC101', 'DEDUSNSC102', 'DEDUSNSE101', 'DEDUSNSE102', 'DEDUSNSD101', 'DEDUSNSD102', 'DEDUSNSD103', 'DEDUSNSD104', 'DEDUSNSD105', 'DEDUSNSD106', 'DEDUSNSD107', 'DEDUSNSD108', 'DEMEENSC101', 'DEMEENSC102', 'DEMEENSE101', 'DEMEENSE102', 'DEMEENSD101', 'DEMEENSD102', 'DEMEENSD103', 'DEMEENSD104', 'DEMEENSD105', 'DEMEENSD106', 'DEMEENSD107', 'DEMEENSD108', 'DEMEENSD109', 'DEMEENSD110', 'DEMEENSD111', 'DEMEENSD112' ]

#
# Connect to CVP
#

server = cvp.Cvp( host )
server.authenticate( user , password )

#
# Dump config for each switch to a file in the local directory configs
#

deviceList = server.getDevices()
deviceDB = []
dbFile = open("deviceDB.txt", "w")

for device in deviceList:
    if "NST" not in device.fqdn:
        if trace:
            print("FQDN: %s") % (device.fqdn)
            print("IP: %s") % (device.ipAddress)
            print("MAC: %s") % (device.macAddress)
            print("\n")

        deviceNameList = device.fqdn.split(".")
        deviceName = deviceNameList[0]
        deviceMacAddress = device.macAddress

        deviceEntry = { "deviceName": deviceName, "deviceMacAddress": deviceMacAddress }
        deviceDB.append( deviceEntry )

dbFile.write(json.dumps(deviceDB, sort_keys=True, indent=4))
dbFile.close()