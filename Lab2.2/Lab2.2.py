from flask import Flask, jsonify
import sys
import os
import re

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'Заходи на /configs'

@app.route('/configs')
def configs():
    path = "C:/Users/ra.mustafin/Seafile/p4ne_training/config_files"
    files = os.listdir(path)
    return jsonify(files)

@app.route('/configs/<hostname_conf>')
def show_ip_from_config(hostname_conf):
    global iphostg
    return jsonify(iphostg[hostname_conf])


if __name__ == '__main__':
    pathg = "C:/Users/ra.mustafin/Seafile/p4ne_training/config_files"
    filesg = os.listdir(pathg)
    iplistg = list()
    iphostg = dict()
    intlist = list()
    hostlist = list()
    ipreg = "^ ip address ([0-9]{1,3}\.?){4} ([0-9]{1,3}\.?){4}"

    for confileg in filesg:
        fullpathg = pathg + "/" + str(confileg)
        # print(fullpath)
        with open(fullpathg) as cfg:
            iplistg = list()
            for clineg in cfg:
                if bool(re.match(ipreg, clineg)):
                    clineg.strip()
                    iplistg.append(clineg)
            iphostg[confileg]=iplistg

    print(iphostg)
    app.run(debug=True)