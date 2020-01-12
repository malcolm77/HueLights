# get-light-names.py
#
# Example of how to get the list of lights from the bridge
# then iteriate through the list and display the name of each list as well as its number

import json 
import requests

bridgeIP = "192.168.1.126"
userName = "qxb5PJleolvND8RAvqokpuj1eM7o4N--9bdavDAs"

response = requests.get("http://" + bridgeIP + "/api/" + userName + "/")
devices = json.loads(response.text)

print ( devices["groups"] )

# for device in devices:
    #print ( devices[device] )
    # print datastore["office"]["parking"]["style"]
    