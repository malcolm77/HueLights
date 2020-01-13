# Turn 'My Bedroom Light' on or off
def mybedroom(state):
    lightNo = "4"
    url = "http://" + bridgeIP + "/api/" + userName + "/lights/" + lightNo + "/state"
    if state == "on":
        payload = {'on':True}
    elif state == "off":
        payload = {'on':False}
    r = requests.put(url, json=payload)
    # print (r.text)

def loungeroom(state):
    lightNo = "5"
    url = "http://" + bridgeIP + "/api/" + userName + "/lights/" + lightNo + "/state"
    if state == "on":
        payload = {'on':True}
    elif state == "off":
        payload = {'on':False}
    r = requests.put(url, json=payload)
    # print (r.text)

def dinngingroom(state):
    lightNo = "6"
    url = "http://" + bridgeIP + "/api/" + userName + "/lights/" + lightNo + "/state"
    if state == "on":
        payload = {'on':True}
    elif state == "off":
        payload = {'on':False}
    r = requests.put(url, json=payload)
    # print (r.text)