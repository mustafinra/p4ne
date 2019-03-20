from flask import Flask, jsonify, render_template

import sys
import requests
import json
import os
import time
import pprint

url = 'https://sandboxapic.cisco.com/api/v1/ticket'
payload = {"username":"devnetuser", "password":"Cisco123!"}
header = {"content-type": "application/json"}

r1 = requests.post(url, data=json.dumps(payload), headers=header, verify=False)
ticket = r1.json()['response']['serviceTicket']
print(ticket)
time.sleep(1)

header["X-Auth-Token"] = ticket
controller = "devnetapi.cisco.com/sandbox/apic_em"
url2 = "https://"+controller+"/api/v1/host"
r2 = requests.get(url2, headers=header, verify=False)
pprint.pprint(json.dumps(r2.json()))
time.sleep(1)

url3 = 'https://sandboxapic.cisco.com/api/v1/network-device'
r3 = requests.get(url3, headers=header, verify=False)
pprint.pprint(json.dumps(r3.json()))
time.sleep(1)

url4= 'https://sandboxapic.cisco.com/api/v1/topology/physical-topology'
r4 = requests.get(url4, headers=header, verify=False)
pprint.pprint((r4.json()))
time.sleep(1)

app = Flask(__name__)

@app.route('/index')
def index1():
    return 'Заходи на http://127.0.0.1:5000/api/topology'

@app.route('/api/topology')
def topology():
    global r4
    return jsonify(r4.json()['response'])

@app.route("/")
def index():
    return render_template("topology.html")

app.run(debug=True)





