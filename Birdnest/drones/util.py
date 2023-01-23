import requests
import xmltodict
import json
import sqlite3
import django_tables2 as tables

from . import models


def addToDatabase(pilotDict):
    con = sqlite3.connect('db.sqlite3')
    
    cursor = con.cursor()
    cursor.execute("CREATE TABLE DronesTable(name, lastName, number, email)")
    cursor.executemany("INSERT INTO PilotTable VALUES(:name, :lName, :number, :email)", [pilotDict])
    con.commit()
    con.close()


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
            return serialNumber

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

                pilotData = (
                    {"name": pilotName, "lName": pilotLastName, "number": phoneNumber, "email": email}
                )

                addToDatabase(pilotData)
                return addToDatabase
            else:
                return None

class PilotsTable(tables.Table):
    class Meta:
        model = models.PilotTable
        template_name = "django_tables2/bootstrap.html"

