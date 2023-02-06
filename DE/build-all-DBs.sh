cd ..

./init-DB-files.sh

./build-trunkDB.py -l DE/dedusnsd101-vlan-file.txt
./build-trunkDB.py -l DE/dedusnsd102-vlan-file.txt
./build-trunkDB.py -l DE/dedusnsd103-vlan-file.txt
./build-trunkDB.py -l DE/dedusnsd104-vlan-file.txt
./build-trunkDB.py -l DE/dedusnsd105-vlan-file.txt
./build-trunkDB.py -l DE/dedusnsd106-vlan-file.txt
./build-trunkDB.py -l DE/dedusnsd107-vlan-file.txt
./build-trunkDB.py -l DE/dedusnsd108-vlan-file.txt
./build-trunkDB.py -l DE/dedusnse101-vlan-file.txt
./build-trunkDB.py -l DE/dedusnse102-vlan-file.txt

./build_overlay.py -n DEDUSNSD101 -r DE/dedusnsd101-vrf-file.txt -l DE/dedusnsd101-vlan-file.txt -s DE/dedusnsd101-vlan-interface-file.txt
./build_overlay.py -n DEDUSNSD102 -r DE/dedusnsd102-vrf-file.txt -l DE/dedusnsd102-vlan-file.txt -s DE/dedusnsd102-vlan-interface-file.txt
./build_overlay.py -n DEDUSNSD103 -r DE/dedusnsd103-vrf-file.txt -l DE/dedusnsd103-vlan-file.txt -s DE/dedusnsd103-vlan-interface-file.txt
./build_overlay.py -n DEDUSNSD104 -r DE/dedusnsd104-vrf-file.txt -l DE/dedusnsd104-vlan-file.txt -s DE/dedusnsd104-vlan-interface-file.txt
./build_overlay.py -n DEDUSNSD105 -r DE/dedusnsd105-vrf-file.txt -l DE/dedusnsd105-vlan-file.txt -s DE/dedusnsd105-vlan-interface-file.txt
./build_overlay.py -n DEDUSNSD106 -r DE/dedusnsd106-vrf-file.txt -l DE/dedusnsd106-vlan-file.txt -s DE/dedusnsd106-vlan-interface-file.txt
./build_overlay.py -n DEDUSNSD107 -r DE/dedusnsd107-vrf-file.txt -l DE/dedusnsd107-vlan-file.txt -s DE/dedusnsd107-vlan-interface-file.txt
./build_overlay.py -n DEDUSNSD108 -r DE/dedusnsd108-vrf-file.txt -l DE/dedusnsd108-vlan-file.txt -s DE/dedusnsd108-vlan-interface-file.txt
./build_overlay.py -n DEDUSNSE101 -r DE/dedusnse101-vrf-file.txt -l DE/dedusnse101-vlan-file.txt -s DE/dedusnse101-vlan-interface-file.txt
./build_overlay.py -n DEDUSNSE102 -r DE/dedusnse102-vrf-file.txt -l DE/dedusnse102-vlan-file.txt -s DE/dedusnse102-vlan-interface-file.txt

./build_interfaces.py -n1 DEDUSNSD101 -n2 DEDUSNSD102 -i1 DE/dedusnsd101-interface-file.txt -i2 DE/dedusnsd102-interface-file.txt
./build_interfaces.py -n1 DEDUSNSD103 -n2 DEDUSNSD104 -i1 DE/dedusnsd103-interface-file.txt -i2 DE/dedusnsd104-interface-file.txt
./build_interfaces.py -n1 DEDUSNSD105 -n2 DEDUSNSD106 -i1 DE/dedusnsd105-interface-file.txt -i2 DE/dedusnsd106-interface-file.txt
./build_interfaces.py -n1 DEDUSNSD107 -n2 DEDUSNSD108 -i1 DE/dedusnsd107-interface-file.txt -i2 DE/dedusnsd108-interface-file.txt
./build_interfaces.py -n1 DEDUSNSE101 -n2 DEDUSNSE102 -i1 DE/dedusnse101-interface-file.txt -i2 DE/dedusnse102-interface-file.txt

./print_overlay.py > DE/DEDUS_TENANTS.yml
./print-pair.py > DE/DEDUS_SERVERS.yml

./init-DB-files.sh

./build-trunkDB.py -l DE/demeensd101-vlan-file.txt
./build-trunkDB.py -l DE/demeensd102-vlan-file.txt
./build-trunkDB.py -l DE/demeensd103-vlan-file.txt
./build-trunkDB.py -l DE/demeensd104-vlan-file.txt
./build-trunkDB.py -l DE/demeensd105-vlan-file.txt
./build-trunkDB.py -l DE/demeensd106-vlan-file.txt
./build-trunkDB.py -l DE/demeensd107-vlan-file.txt
./build-trunkDB.py -l DE/demeensd108-vlan-file.txt
./build-trunkDB.py -l DE/demeensd109-vlan-file.txt
./build-trunkDB.py -l DE/demeensd110-vlan-file.txt
./build-trunkDB.py -l DE/demeensd111-vlan-file.txt
./build-trunkDB.py -l DE/demeensd112-vlan-file.txt
./build-trunkDB.py -l DE/demeense101-vlan-file.txt
./build-trunkDB.py -l DE/demeense102-vlan-file.txt

./build_overlay.py -n DEMEENSD101 -r DE/demeensd101-vrf-file.txt -l DE/demeensd101-vlan-file.txt -s DE/demeensd101-vlan-interface-file.txt
./build_overlay.py -n DEMEENSD102 -r DE/demeensd102-vrf-file.txt -l DE/demeensd102-vlan-file.txt -s DE/demeensd102-vlan-interface-file.txt
./build_overlay.py -n DEMEENSD103 -r DE/demeensd103-vrf-file.txt -l DE/demeensd103-vlan-file.txt -s DE/demeensd103-vlan-interface-file.txt
./build_overlay.py -n DEMEENSD104 -r DE/demeensd104-vrf-file.txt -l DE/demeensd104-vlan-file.txt -s DE/demeensd104-vlan-interface-file.txt
./build_overlay.py -n DEMEENSD105 -r DE/demeensd105-vrf-file.txt -l DE/demeensd105-vlan-file.txt -s DE/demeensd105-vlan-interface-file.txt
./build_overlay.py -n DEMEENSD106 -r DE/demeensd106-vrf-file.txt -l DE/demeensd106-vlan-file.txt -s DE/demeensd106-vlan-interface-file.txt
./build_overlay.py -n DEMEENSD106 -r DE/demeensd107-vrf-file.txt -l DE/demeensd107-vlan-file.txt -s DE/demeensd107-vlan-interface-file.txt
./build_overlay.py -n DEMEENSD106 -r DE/demeensd108-vrf-file.txt -l DE/demeensd108-vlan-file.txt -s DE/demeensd108-vlan-interface-file.txt
./build_overlay.py -n DEMEENSD106 -r DE/demeensd109-vrf-file.txt -l DE/demeensd109-vlan-file.txt -s DE/demeensd109-vlan-interface-file.txt
./build_overlay.py -n DEMEENSD106 -r DE/demeensd110-vrf-file.txt -l DE/demeensd110-vlan-file.txt -s DE/demeensd110-vlan-interface-file.txt
./build_overlay.py -n DEMEENSD106 -r DE/demeensd111-vrf-file.txt -l DE/demeensd111-vlan-file.txt -s DE/demeensd111-vlan-interface-file.txt
./build_overlay.py -n DEMEENSD106 -r DE/demeensd112-vrf-file.txt -l DE/demeensd112-vlan-file.txt -s DE/demeensd112-vlan-interface-file.txt
./build_overlay.py -n DEMEENSE101 -r DE/demeense101-vrf-file.txt -l DE/demeense101-vlan-file.txt -s DE/demeense101-vlan-interface-file.txt
./build_overlay.py -n DEMEENSE102 -r DE/demeense102-vrf-file.txt -l DE/demeense102-vlan-file.txt -s DE/demeense102-vlan-interface-file.txt

./build_interfaces.py -n1 DEMEENSD101 -n2 DEMEENSD102 -i1 DE/demeensd101-interface-file.txt -i2 DE/demeensd102-interface-file.txt
./build_interfaces.py -n1 DEMEENSD103 -n2 DEMEENSD104 -i1 DE/demeensd103-interface-file.txt -i2 DE/demeensd104-interface-file.txt
./build_interfaces.py -n1 DEMEENSD105 -n2 DEMEENSD106 -i1 DE/demeensd105-interface-file.txt -i2 DE/demeensd106-interface-file.txt
./build_interfaces.py -n1 DEMEENSD107 -n2 DEMEENSD108 -i1 DE/demeensd107-interface-file.txt -i2 DE/demeensd108-interface-file.txt
./build_interfaces.py -n1 DEMEENSD109 -n2 DEMEENSD110 -i1 DE/demeensd109-interface-file.txt -i2 DE/demeensd110-interface-file.txt
./build_interfaces.py -n1 DEMEENSD111 -n2 DEMEENSD112 -i1 DE/demeensd111-interface-file.txt -i2 DE/demeensd112-interface-file.txt
./build_interfaces.py -n1 DEMEENSE101 -n2 DEMEENSE102 -i1 DE/demeense101-interface-file.txt -i2 DE/demeense102-interface-file.txt

./print_overlay.py > DE/DEMEE_TENANTS.yml
./print-pair.py > DE/DEMEE_SERVERS.yml
