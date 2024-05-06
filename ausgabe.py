import json

def liste():

    with open("Schulen.geojson", "r") as file:
        data = json.load(file)
        zeilen = file.readline()
        i = 0

        myList = data["features"]

        print(myList)


        for i in myList:
            # print(i["attributes"]["BEZEICHNUNG"])
            # print(i["attributes"]["ID"])
            print(i["properties"]["BEZEICHNUNG"])
            print("=========================================")
