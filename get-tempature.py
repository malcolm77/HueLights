
import json 
import requests

print ("-----------------------------------------------------------------------------")

bridgeIP = "192.168.1.151"
userName = "qxb5PJleolvND8RAvqokpuj1eM7o4N--9bdavDAs"

response = requests.get("http://" + bridgeIP + "/api/" + userName + "/")
devices = json.loads(response.text)

print ("You have the following sensors configure on your hub:")
sensors = devices["sensors"]
for sensor in sensors:
    print (sensors[sensor]['name'] + " (" + sensor + ")" )
    # print datastore["office"]["parking"]["style"]

print ("-----------")
print ("sensor info")
print (sensors["59"])

print ("-----------")
print ("temperature info")
print (sensors["59"]["state"]["temperature"]/100)
