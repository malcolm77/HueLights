import json 
import requests

response = requests.get("http://192.168.1.126/api/qxb5PJleolvND8RAvqokpuj1eM7o4N--9bdavDAs/lights/")
lights = json.loads(response.text)

# print( lights['4']['name'] )

for light in lights:
    print (lights[light]['name'] + " (" + light + ")" )
    # print datastore["office"]["parking"]["style"]