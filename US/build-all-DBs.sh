#!/bin/bash

cd ..

./init-DB-files.sh

./build-trunkDB.py -l US/usdc1nsd101-vlan-file.txt
./build-trunkDB.py -l US/usdc1nsd102-vlan-file.txt
./build-trunkDB.py -l US/usdc1nsd103-vlan-file.txt
./build-trunkDB.py -l US/usdc1nsd104-vlan-file.txt
./build-trunkDB.py -l US/usdc1nsd105-vlan-file.txt
./build-trunkDB.py -l US/usdc1nsd106-vlan-file.txt
./build-trunkDB.py -l US/usdc1nse101-vlan-file.txt
./build-trunkDB.py -l US/usdc1nse102-vlan-file.txt

./build-trunkDB.py -l US/usdc2nsd101-vlan-file.txt
./build-trunkDB.py -l US/usdc2nsd102-vlan-file.txt
./build-trunkDB.py -l US/usdc2nsd103-vlan-file.txt
./build-trunkDB.py -l US/usdc2nsd104-vlan-file.txt
./build-trunkDB.py -l US/usdc2nsd105-vlan-file.txt
./build-trunkDB.py -l US/usdc2nsd106-vlan-file.txt
./build-trunkDB.py -l US/usdc2nse101-vlan-file.txt
./build-trunkDB.py -l US/usdc2nse102-vlan-file.txt

./build_overlay.py -n USDC1NSD101 -r US/usdc1nsd101-vrf-file.txt -l US/usdc1nsd101-vlan-file.txt -s US/usdc1nsd101-vlan-interface-file.txt
./build_overlay.py -n USDC1NSD102 -r US/usdc1nsd102-vrf-file.txt -l US/usdc1nsd102-vlan-file.txt -s US/usdc1nsd102-vlan-interface-file.txt
./build_overlay.py -n USDC1NSD103 -r US/usdc1nsd103-vrf-file.txt -l US/usdc1nsd103-vlan-file.txt -s US/usdc1nsd103-vlan-interface-file.txt
./build_overlay.py -n USDC1NSD104 -r US/usdc1nsd104-vrf-file.txt -l US/usdc1nsd104-vlan-file.txt -s US/usdc1nsd104-vlan-interface-file.txt
./build_overlay.py -n USDC1NSD105 -r US/usdc1nsd105-vrf-file.txt -l US/usdc1nsd105-vlan-file.txt -s US/usdc1nsd105-vlan-interface-file.txt
./build_overlay.py -n USDC1NSD106 -r US/usdc1nsd106-vrf-file.txt -l US/usdc1nsd106-vlan-file.txt -s US/usdc1nsd106-vlan-interface-file.txt
./build_overlay.py -n USDC1NSE101 -r US/usdc1nse101-vrf-file.txt -l US/usdc1nse101-vlan-file.txt -s US/usdc1nse101-vlan-interface-file.txt
./build_overlay.py -n USDC1NSE102 -r US/usdc1nse102-vrf-file.txt -l US/usdc1nse102-vlan-file.txt -s US/usdc1nse102-vlan-interface-file.txt

./build_overlay.py -n USDC2NSD101 -r US/usdc2nsd101-vrf-file.txt -l US/usdc2nsd101-vlan-file.txt -s US/usdc2nsd101-vlan-interface-file.txt
./build_overlay.py -n USDC2NSD102 -r US/usdc2nsd102-vrf-file.txt -l US/usdc2nsd102-vlan-file.txt -s US/usdc2nsd102-vlan-interface-file.txt
./build_overlay.py -n USDC2NSD103 -r US/usdc2nsd103-vrf-file.txt -l US/usdc2nsd103-vlan-file.txt -s US/usdc2nsd103-vlan-interface-file.txt
./build_overlay.py -n USDC2NSD104 -r US/usdc2nsd104-vrf-file.txt -l US/usdc2nsd104-vlan-file.txt -s US/usdc2nsd104-vlan-interface-file.txt
./build_overlay.py -n USDC2NSD105 -r US/usdc2nsd105-vrf-file.txt -l US/usdc2nsd105-vlan-file.txt -s US/usdc2nsd105-vlan-interface-file.txt
./build_overlay.py -n USDC2NSD106 -r US/usdc2nsd106-vrf-file.txt -l US/usdc2nsd106-vlan-file.txt -s US/usdc2nsd106-vlan-interface-file.txt
./build_overlay.py -n USDC2NSE101 -r US/usdc2nse101-vrf-file.txt -l US/usdc2nse101-vlan-file.txt -s US/usdc2nse101-vlan-interface-file.txt
./build_overlay.py -n USDC2NSE102 -r US/usdc2nse102-vrf-file.txt -l US/usdc2nse102-vlan-file.txt -s US/usdc2nse102-vlan-interface-file.txt

./build_interfaces.py -n1 USDC1NSD101 -n2 USDC1NSD102 -i1 US/usdc1nsd101-interface-file.txt -i2 US/usdc1nsd102-interface-file.txt
./build_interfaces.py -n1 USDC1NSD103 -n2 USDC1NSD104 -i1 US/usdc1nsd103-interface-file.txt -i2 US/usdc1nsd104-interface-file.txt
./build_interfaces.py -n1 USDC1NSD105 -n2 USDC1NSD106 -i1 US/usdc1nsd105-interface-file.txt -i2 US/usdc1nsd106-interface-file.txt
./build_interfaces.py -n1 USDC1NSE101 -n2 USDC1NSE102 -i1 US/usdc1nse101-interface-file.txt -i2 US/usdc1nse102-interface-file.txt

./build_interfaces.py -n1 USDC2NSD101 -n2 USDC2NSD102 -i1 US/usdc2nsd101-interface-file.txt -i2 US/usdc2nsd102-interface-file.txt
./build_interfaces.py -n1 USDC2NSD103 -n2 USDC2NSD104 -i1 US/usdc2nsd103-interface-file.txt -i2 US/usdc2nsd104-interface-file.txt
./build_interfaces.py -n1 USDC2NSD105 -n2 USDC2NSD106 -i1 US/usdc2nsd105-interface-file.txt -i2 US/usdc2nsd106-interface-file.txt
./build_interfaces.py -n1 USDC2NSE101 -n2 USDC2NSE102 -i1 US/usdc2nse101-interface-file.txt -i2 US/usdc2nse102-interface-file.txt
