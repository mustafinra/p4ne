import glob
import os
import re
os.system('cls')

path = "C:/Users/ra.mustafin/Seafile/p4ne_training/config_files"
files = os.listdir(path)
#print(files)
iplist = list()
intlist = list()
hostlist = list()
ipreg = r^"ip address ([0-9]{1,3}\.?){4} ([0-9]{1,3}\.?){4}"

for confile in files:
    fullpath = path+"/"+str(confile)
    #print(fullpath)
    with open(fullpath) as cf:
        for cline in cf:
            if cline.find('ip address') != -1:
                if cline.find('dhcp') == -1:
                    if cline.find('match') == -1:
                        if cline.find('no') == -1:
                          cline.strip()
                          megalist.append(cline)

megalist = sorted(set(megalist))

for eachline in megalist:
    print(eachline)

