from ipaddress import IPv4Network
from ipaddress import IPv4Address
import ipaddress
import random

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        n = (ipaddress.IPv4Address(random.randint(184549376, 3741319168)), str(random.randint(8, 24)))
        IPv4Network.__init__(self,n, strict=False)
    def key_value(self):
        return(self.netmask, self.network_address)

def sorting(x):
    return x.key_value()

counter=0
netw_list=[]

#r.is_global == False

for counter in range(1,10):
  r = IPv4RandomNetwork()
  while r.is_global == False:
    r = IPv4RandomNetwork()
  else:
    #print(r)
    netw_list.append(r)

print("Not Sorted")
for ns in range (0,9):
  print(netw_list[ns])
print("Sorted")
for n in sorted(netw_list, key=sorting):

    print(n)


