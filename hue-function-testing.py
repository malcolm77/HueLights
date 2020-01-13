import json

lights = {}

# get the Hue information from a JSON file instead from the Hub
def GetJSON():
    # read JSON data file file
    with open('hue-all-devices-data-example.json') as json_file:
        data = json.load(json_file)
        # seperate out just the light information
        global lights
        lights = data['lights']

# is given light in the list of lights
def IsValidLight(lightNo):
    if lightNo in lights:
        return True
    else:
        return False

# list all the lights connected to the hub
def ListLights():
    # print the number of lights
    print ( 'Number of lights: ' + str(len(lights)) )
    # print each light name and number
    for light in lights:
        print(lights[light]['name'] + ' is light number : ' + light)

# Get the on/off status of each light
def ListLightStates():
    # print the number of lights
    print ( 'Number of lights: ' + str(len(lights)) )
    # print each light name and number
    for light in lights:
        if lights[light]['state']['on']:
            print("The " + lights[light]['name'] + " is  :  on")
        else:
            print("The " + lights[light]['name'] + " is  :  off")

# get the reachable status of each light
def ListLightStatus():
    for light in lights:
        if lights[light]['state']['reachable']:
            print("The " + lights[light]['name'] + " is  :  connected")
        else:
            print("The " + lights[light]['name'] + " is  :  not reachable")

def CheckLightStatus(light):
    if lights[light]['state']['reachable']:
        return True
    else:
        return False

def GetLightName(light):
    return lights[light]['name']

# --------------- MAIN --------------

GetJSON()

for light in lights:
    if CheckLightStatus(light):
        print ("Light " + light + " is online")
    else:
        print ("Light " + GetLightName(light) + " is offline")


# check if light number is in list of lights
#if IsValidLight('5'):
#    print ( 'yes' )

