import requests
import xmltodict
import json
import time

# Get NDZ Drone Info
def droneInfo():

    # Getting xml data and turn to json 
    infoUrl = "http://assignments.reaktor.com/birdnest/drones"
    treatedXml = requests.get(infoUrl)

    jsonData = xmltodict.parse(treatedXml.text)
    
    drones = jsonData["report"]["capture"]['drone']
    ndzDrones = {}
    n = 1
    
    # Storing individual Drone info
    for drone in drones:
        if float(drone["positionY"]) <= 250000 and float(drone["positionX"]) <= 250000:
            ndzDrones[f"Drone {n}"] = drone
            n += 1 
    print(ndzDrones)

droneInfo()

