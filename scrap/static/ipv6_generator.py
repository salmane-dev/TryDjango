#!/usr/bin/env python3
"""
Generate a random IPv6 address for a specified subnet
"""

from random import seed, getrandbits
from ipaddress import IPv6Network, IPv6Address

# subnet = '2001:db8:100::/64'
# for add in range(1,10):
#   seed()
#   network = IPv6Network(subnet)
#   address = IPv6Address(network.network_address + getrandbits(network.max_prefixlen - network.prefixlen))
#   print(address)



def GenIPv6(subnet,number_ips):
  ipv6_list=[]
  for add in range(0,number_ips):
    seed()
    network = IPv6Network(subnet)
    address = str(IPv6Address(network.network_address + getrandbits(network.max_prefixlen - network.prefixlen)) ) + "/64"
    ipv6_list.append(str(address))
  return ipv6_list


ipv6_list = GenIPv6("2001:bc8:32d7:186::/64",500)
print(len(ipv6_list))
outfile = open("outttttttttt.txt", "w")

for element in ipv6_list:
    outfile.write(element + "  ")
    #outfile.write("/sbin/ifconfig eth0 inet6 add  " + element  + ";\n")
outfile.close()

