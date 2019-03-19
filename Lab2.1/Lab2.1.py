import socket
import os
import requests
import json
import pprint
import time

print('Первые три карты')
cards = ('47148700', '42790100', '42763801')

for cardx in cards:
    time.sleep(2)
    geturl = 'https://lookup.binlist.net/'+cardx
    r = requests.get(geturl, headers={'Accept-Version': "3"})
    print(geturl)
    print(r.status_code)
    #cardinfo = pprint.pprint(r.json())
    cardinfo1 = r.json()
    print(cardx, cardinfo1['bank']['name'])

print('А теперь из файлов')
filespath = 'C:/Users/ra.mustafin/AppData/Local/Programs/Python/Python37/Scripts/'
#file1 = json.load(filespath+'card1.json')

finallist=list()
with open(filespath+'card1.json') as file1:
    data1 = json.loads(file1.read())
    for i in data1:
        d = dict(i)
        for ccn in d.values():
            time.sleep(2)
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
              if 'name' in cardinfo_ccn['bank']:
                print(ccn['CardNumber'], cardinfo_ccn['bank']['name'])
                finallist.append(str(cardinfo_ccn['bank']['name']))

with open(filespath+'card2.json') as file1:
    data1 = json.loads(file1.read())
    for i in data1:
        d = dict(i)
        for ccn in d.values():
            time.sleep(2)
            #print(ccn['CardNumber'])
            #print(type(ccn))
            ccn_str = str(ccn['CardNumber'])[0:8]
            #print(ccn_str)
            geturl = 'https://lookup.binlist.net/' + ccn_str
            print(geturl)
            r = requests.get(geturl, headers={'Accept-Version': "3"})
            #print(r.status_code)
            if r.status_code == 200:
              cardinfo_ccn = r.json()
              if 'name' in cardinfo_ccn['bank']:
                print(ccn['CardNumber'], cardinfo_ccn['bank']['name'])
                finallist.append(str(cardinfo_ccn['bank']['name']))


with open(filespath+'card3.json') as file1:
    data1 = json.loads(file1.read())
    for i in data1:
        d = dict(i)
        for ccn in d.values():
            time.sleep(2)
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
              if 'name' in cardinfo_ccn['bank']:
                print(ccn['CardNumber'], cardinfo_ccn['bank']['name'])
                finallist.append(str(cardinfo_ccn['bank']['name']))


print("И собственно вывод уникальных имен банков")
finallist = sorted(set(finallist))
for eachline in finallist:
    print(eachline)
