import requests
import json
import main

def abfrage():

    url = (
     f"https://portal-chemnitz.opendata.arcgis.com/datasets/4c331993dab54b49bbc9debfc5928ec3_0/explore?location=50.822923%2C12.887629%2C12.21&showTable=true")
    response = requests.get(url)
    data = response.json()

    json_filename = "chemnitz_schulen.json"
    with open(json_filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)

    print(f"Schuldaten wurden geschrieben nach: {json_filename}")