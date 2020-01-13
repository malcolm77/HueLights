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

def GetLights():
    # print the number of lights
    print ( 'Number of lights: ' + str(len(lights)) )
    # print each light name and number
    for light in lights:
        print(lights[light]['name'] + ' is light number : ' + light)

# --------------- MAIN --------------

GetJSON()

GetLights()

# check if light number is in list of lights
if IsValidLight('5'):
    print ( 'yes' )
