import requests
import xmltodict
import json
import time

# Get Drone Info
def droneInfo():

    # Getting xml data and turn to json 
    infoUrl = "http://assignments.reaktor.com/birdnest/drones"
    treatedXml = requests.get(infoUrl)

    jsonData = xmltodict.parse(treatedXml.text)
    
    results = jsonData["report"]["capture"]
    print(results)

droneInfo()
