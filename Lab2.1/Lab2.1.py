import socket
import os
import requests
import json
import pprint

print('Первые три карты')
cards = ('47148700', '42790100', '42763801')

for cardx in cards:
    geturl = 'https://lookup.binlist.net/'+cardx
    r = requests.get(geturl, headers={'Accept-Version': "3"})
    #print(r.status_code)
    #cardinfo = pprint.pprint(r.json())
    cardinfo1 = r.json()
    print(cardx, cardinfo1['bank']['name'])

print('А теперь из файлов')
filespath = 'C:/Users/ra.mustafin/AppData/Local/Programs/Python/Python37/Scripts/'
#file1 = json.load(filespath+'card1.json')

with open(filespath+'card1.json') as file1:
    data1 = json.loads(file1.read())
    for i in data1:
        d = dict(i)
        for ccn in d.values():
            #print(ccn['CardNumber'])
            #print(type(ccn))
            ccn_str = str(ccn['CardNumber'])[0:8]
            #print(ccn_str)
            geturl = 'https://lookup.binlist.net/' + ccn_str
            #print(geturl)
            r = requests.get(geturl, headers={'Accept-Version': "3"})
            #print(r.status_code)
            if r.status_code == 200:
              cardinfo_ccn = r.json()
              print(ccn['CardNumber'], cardinfo_ccn['bank']['name'])

