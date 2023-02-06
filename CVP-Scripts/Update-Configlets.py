#!/usr/bin/env python2

import argparse
import cvp

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
    help="If debug is set, nothing will actually be sent to CVP and proposed configs are written to terminal",
    default=False,
)
ap.add_argument(
    "-t",
    "--trace",
    dest="trace",
    action="store_true",
    help="If trace is set, alongside actual changes to CVP configlets, there will be trace messages to terminal",
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

Switches = [ 'USDC1NSC101', 'USDC1NSC102', 'USDC1NSE101', 'USDC1NSE102', 'USDC1NSD101', 'USDC1NSD102', 'USDC1NSD103', 'USDC1NSD104', 'USDC1NSD105', 'USDC1NSD106', 'USDC2NSC101', 'USDC2NSC102', 'USDC2NSE101', 'USDC2NSE102', 'USDC2NSD101', 'USDC2NSD102', 'USDC2NSD103', 'USDC2NSD104', 'USDC2NSD105', 'USDC2NSD106' ]

#
# Connect to CVP
#

server = cvp.Cvp( host )
server.authenticate( user , password )

#
# Open config file and write to configlet 
#

for switch in Switches:
    fileName = '../../ASSA/US-lab/intended/configs/' + switch + ".cfg"
    configFile = open(fileName, 'r')
    configuration = configFile.read()
    configFile.close()
#    print "%s" % ( configuration )

    configletName = switch + " Config"
    configlet = server.getConfiglet(configletName)
#    print "%s" % ( configlet.config )

    configlet.config = configuration
    server.updateConfiglet( configlet )
    