import requests
import xmltodict
import json
import time

# Get NDZ Drone Info
def droneInfo():

    # Getting xml data and turn to json 
    infoUrl = "http://assignments.reaktor.com/birdnest/drones"
    treatInfoXml = requests.get(infoUrl)

    infoDataJson = xmltodict.parse(treatInfoXml.text)
    
    drones = infoDataJson['report']['capture']['drone']
    ndzDrones = {}
    
    # Storing individual Drone info
    for drone in drones:
        if float(drone['positionY']) <= 250000 and float(drone['positionX']) <= 250000:
            serialNumber = drone['serialNumber'] 
            
            # Store pilots' details
            pilotUrl = f"http://assignments.reaktor.com/birdnest/pilots/{serialNumber}"
            
            getPilotJSON = requests.get(pilotUrl)
            treatPilotJSON = getPilotJSON.content
            content = json.loads(treatPilotJSON)         

            if getPilotJSON.ok: # if response = 404 then return none
                pilotName = content['firstName']
                pilotLastName = content['lastName']
                phoneNumber = content['phoneNumber']
                email = content['email']
                ndzDrones = {pilotName, pilotLastName, phoneNumber, email}
            else:
                return None
            
    print(ndzDrones)

droneInfo()

