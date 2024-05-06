import requests
import json
import main

def abfrage():
    print("reading data from URL..")
    url = "https://services6.arcgis.com/jiszdsDupTUO3fSM/arcgis/rest/services/Schulen_OpenData/FeatureServer/0/query?f=json&cacheHint=true&maxRecordCountFactor=4&resultOffset=0&resultRecordCount=8000&where=1%3D1&orderByFields=OBJECTID&outFields=*&outSR=102100&spatialRel=esriSpatialRelIntersects"
    response = requests.get(url)
    myResponse = response.json()
    data = myResponse["features"]

    json_filename = "chemnitz_schulen.json"
    with open(json_filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)
    print("reading data is done...")

    # print(f"Schuldaten wurden geschrieben nach: {json_filename}")