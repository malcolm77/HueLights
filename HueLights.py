# HueLights.py
# 
# Main code file for controlling Hue Lights

import requests
import json
import sys

# GLOBAL variables
devices = {}
light = {}
bridgeIP = "192.168.1.126"
userName = "qxb5PJleolvND8RAvqokpuj1eM7o4N--9bdavDAs"

# this is what the url should look like, see Hue-Notes.txt for how to create a user
# url = "http://192.168.1.126/api/qxb5PJleolvND8RAvqokpuj1eM7o4N--9bdavDAs/lights/5/state" 

# get the device data from the Hub
def GetJSON():
    response = requests.get("http://" + bridgeIP + "/api/" + userName + "/")
    # get all devices
    global devices
    devices = json.loads(response.text)
    # seperate out just the lights
    global lights
    lights = devices["lights"]
    

# specify lightNo to switch and state to switch it to
def LightSwitch(lightNo,state):
    if lightNo != None and state != None:   # check to make sure both lightNo nor state have a value
        if lightNo in lights:               # check the given light number is in the list of lights
            url = "http://" + bridgeIP + "/api/" + userName + "/lights/" + lightNo + "/state"
            if state == "on":
                payload = {'on':True}
            elif state == "off":
                payload = {'on':False}
            requests.put(url, json=payload)

# Display a list of the lights and thier numbers
def ListLights():
    # print the number of lights
    print ( 'Number of lights: ' + str(len(lights)) )
    # print each light name and number
    for light in lights:
        print(lights[light]['name'] + ' is light number : ' + light)

# Returns reachable state of light number
def CheckLightStatus(light):
    if lights[light]['state']['reachable']:
        return True
    else:
        return False

# Returns light full name, given light number
def GetLightName(light):
    return lights[light]['name']

# ------------------------- MAIN --------------------------------

if __name__ == "__main__":
    GetJSON()
    LightSwitch("5","off")

    # loungeroom("on")
    # dinngingroom("on")
    # mybedroom("on")


