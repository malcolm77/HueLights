import json

lights = {}

def GetJSON():
    # read JSON data file file
    with open('hue-all-devices-data-example.json') as json_file:
        data = json.load(json_file)
        # seperate out just the light information
        global lights
        lights = data['lights']

def IsValidLight(lightNo):
    if lightNo in lights:
        return True
    else:
        return False

def ListLights():
    # print the number of lights
    print ( 'Number of lights: ' + str(len(lights)) )
    # print each light name and number
    for light in lights:
        print(lights[light]['name'] + ' is light number : ' + light)

def ListLightStates():
    # print the number of lights
    print ( 'Number of lights: ' + str(len(lights)) )
    # print each light name and number
    for light in lights:
        if lights[light]['state']['on']:
            print("The " + lights[light]['name'] + " is  :  on")
        else:
            print("The " + lights[light]['name'] + " is  :  off")

def CheckLightStatus():
    for light in lights:
        if lights[light]['state']['reachable']:
            print("The " + lights[light]['name'] + " is  :  connected")
        else:
            print("The " + lights[light]['name'] + " is  :  not reachable")

# --------------- MAIN --------------

GetJSON()

CheckLightStatus()

# check if light number is in list of lights
#if IsValidLight('5'):
#    print ( 'yes' )

