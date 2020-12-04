# get-light-names.py
#
# Example of how to get the list of lights from the bridge
# then iteriate through the list and display the name of each list as well as its number

import json 
import requests

print ("-----------------------------------------------------------------------------")

bridgeIP = "192.168.1.151"
userName = "qxb5PJleolvND8RAvqokpuj1eM7o4N--9bdavDAs"

response = requests.get("http://" + bridgeIP + "/api/" + userName + "/")
devices = json.loads(response.text)

# you can create a "sub-collection" of just certain items like this
# groups = devices["groups"]
# configs = devices["config"]
# but you don't need to

# get the name and ip address of the hub
print ( "Your hub is called " + devices["config"]["name"] + " and is on IP Address " + devices["config"]["ipaddress"] )

print ("You have the following lights configure on your hub:")
lights = devices["lights"]
for light in lights:
    print (lights[light]['name'] + " (" + light + ")" )
    # print datastore["office"]["parking"]["style"]

print ("-----------------------------------------------------")

# get the name of group number 5
# print ( devices["groups"]["5"]["name"] )

print ("You have the following groups configure on your hub:")
for group in devices["groups"]:
    print ( "    " + devices["groups"][group]["name"] )

# example of how to get sub nob elements from another program
# for device in devices:
    # print ( devices[device] )
    # print datastore["office"]["parking"]["style"]
    
print ("-----------------------------------------------------")

print ("You have the following sensors configure on your hub:")
sensors = devices["sensors"]
for sensor in sensors:
    print (sensors[sensor]['name'] + " (" + sensor + ")" )
    # print datastore["office"]["parking"]["style"]

print ("-----------")
print ("sensor info")
print (sensors["59"]["state"]["temperature"])