# get-light-names.py
#
# Example of how to get the list of lights from the bridge
# then iteriate through the list and display the name of each list as well as its number

import json 
import requests

bridgeIP = "192.168.1.126"
userName = "qxb5PJleolvND8RAvqokpuj1eM7o4N--9bdavDAs"

response = requests.get("http://" + bridgeIP + "/api/" + userName + "/lights/")
lights = json.loads(response.text)

for light in lights:
    print (lights[light]['name'] + " (" + light + ")" )
    # print datastore["office"]["parking"]["style"]