from pysnmp.hlapi import *

ipaddr = "10.31.70.107"

result = getCmd(SnmpEngine(),
	CommunityData('public', mpModel=0),
	UdpTransportTarget((ipaddr, 161)),
	ContextData(),
	ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))


print("-=====================SNMP Data=====================-")
for x in result:
    for t in x[3]:
        print(t)

print("-=====================And Ports=====================-")
result2 = nextCmd(SnmpEngine(),
	CommunityData('public', mpModel=0),
	UdpTransportTarget((ipaddr, 161)),
	ContextData(),
	ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),
    lexicographicMode=False)

for a in result2:
	for b in a[3]:
		print(b)

