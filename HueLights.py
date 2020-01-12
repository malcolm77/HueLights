import requests
import json
import sys

bridgeIP = "192.168.1.126"
userName = "qxb5PJleolvND8RAvqokpuj1eM7o4N--9bdavDAs"

# this is what the url should look like, see newuser.txt for how to create a user
# url = "http://192.168.1.126/api/qxb5PJleolvND8RAvqokpuj1eM7o4N--9bdavDAs/lights/5/state" 

def mybedroom(state):
    lightNo = "4"
    url = "http://" + bridgeIP + "/api/" + userName + "/lights/" + lightNo + "/state"
    if state == "on":
        payload = {'on':True}
    elif state == "off":
        payload = {'on':False}
    r = requests.put(url, json=payload)
    print (r.text)

def loungeroom(state):
    lightNo = "5"
    url = "http://" + bridgeIP + "/api/" + userName + "/lights/" + lightNo + "/state"
    if state == "on":
        payload = {'on':True}
    elif state == "off":
        payload = {'on':False}
    r = requests.put(url, json=payload)
    #if json string returned does not contain "success" then
    #  print (r.text)

def dinngingroom(state):
    lightNo = "6"
    url = "http://" + bridgeIP + "/api/" + userName + "/lights/" + lightNo + "/state"
    if state == "on":
        payload = {'on':True}
    elif state == "off":
        payload = {'on':False}
    r = requests.put(url, json=payload)
    #if json string returned does not contain "success" then
    print (r.text)


# loungeroom("on")
dinngingroom("on")
# mybedroom("on")

