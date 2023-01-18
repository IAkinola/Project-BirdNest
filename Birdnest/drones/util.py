import requests
import xmltodict
import json
import sqlite3
import time

from models import PilotTable

def addToDatabase(fName, lName, pNumber, email, cDistance):
    conn = sqlite3.connect('db.sqlite3')
    
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO PilotTable VALUES(fName, lName, pNumber, email, cDistance)''')
    conn.commit()
    conn.close()


# Get NDZ Drone Info
def droneInfo():

    # Getting xml data and turn to json 
    infoUrl = "http://assignments.reaktor.com/birdnest/drones"
    treatInfoXml = requests.get(infoUrl)

    infoDataJson = xmltodict.parse(treatInfoXml.text)
    
    drones = infoDataJson['report']['capture']['drone']
    
    # Storing individual Drone info
    for drone in drones:
        positionY = float(drone['positionY'])
        positionX = float(drone['positionX'])

        if positionY > positionX:
            closestDistance = 500000 - positionX
        else:
            closestDistance = 500000 - positionY
        
        
        if positionY <= 350000 and positionX <= 350000:
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

                addToDatabase(pilotName, pilotLastName, phoneNumber, email, closestDistance)
            else:
                return None


