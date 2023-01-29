import requests
import xmltodict
import json
import sqlite3
import django_tables2 as tables

from . import models

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
            return serialNumber #, closestDistance

def getPilotInfo():
            serialNumber = droneInfo()
            # Store pilots' details
            pilotUrl = f"http://assignments.reaktor.com/birdnest/pilots/{serialNumber}"
            
            getPilotJSON = requests.get(pilotUrl)
            treatPilotJSON = getPilotJSON.content
            content = json.loads(treatPilotJSON)       

            pilotData = ()  

            if getPilotJSON.ok: # if response = 404 then return none
                
                pilotName = content['firstName']
                pilotLastName = content['lastName']
                phoneNumber = content['phoneNumber']
                email = content['email']

                models.PilotTable.objects.all()
                pilot = models.PilotTable(first_name = pilotName, last_name = pilotLastName, phone_number = phoneNumber, email = email, closest_distance = 0, ndz_time = 0)
                pilot.save()
            else:
                return None

# Models for table
class PilotsTable(tables.Table):
    class Meta:
        model = models.PilotTable
        template_name = "django_tables2/bootstrap.html"

