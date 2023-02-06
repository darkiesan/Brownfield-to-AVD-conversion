#!/usr/bin/env python

Switches = ['CNIDCNSD101', 'CNIDCNSD102']

for switch in Switches:
    i = 1
    while (i < 49):
        print("  %s_Ethernet%s:") % ( switch, i)
        print("""    adapters:
    - mode: trunk
      enabled: false
      description: UNUSED
      server_ports:
      - ETH0
      switch_ports:""")
        print("      - Ethernet%s") % ( i )
        print("      switches:")
        print("      - %s") % ( switch )
        print("""      spanning_tree_portfast: edge
      spanning_tree_bpduguard: true
      vlans: '1540'""")
        i = i+1
