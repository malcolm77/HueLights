# get-light-names.py
#
# Example of how to get the list of lights from the bridge
# then iteriate through the list and display the name of each list as well as its number

import json 
import requests

print ("-----------------------------------------------------------------------------")

bridgeIP = "192.168.1.126"
userName = "qxb5PJleolvND8RAvqokpuj1eM7o4N--9bdavDAs"

response = requests.get("http://" + bridgeIP + "/api/" + userName + "/")
devices = json.loads(response.text)

# you can create a "sub-collection" of just certain items like this
# groups = devices["groups"]
# configs = devices["config"]
# but you don't need to

# get the name and ip address of the hub
print ( "Your hub is called " + devices["config"]["name"] + " and is on IP Address " + devices["config"]["ipaddress"] )

# get the name of group number 5
# print ( devices["groups"]["5"]["name"] )

print ("You have the following groups configure on your hub:")
for group in devices["groups"]:
    print ( "    " + devices["groups"][group]["name"] )

# example of how to get sub nob elements from another program
# for device in devices:
    #print ( devices[device] )
    # print datastore["office"]["parking"]["style"]
    