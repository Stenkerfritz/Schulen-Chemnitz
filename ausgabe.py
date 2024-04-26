import json

def liste():


        with open("Schulen.geojson", "r") as file:
            data = json.load(file)
            zahl = data["features"]
            zeilen = zahl.readline()
            zeilen = int(len(zeilen))
            print(zeilen)


    # Access and process the retrieved JSON data
            date = data["features"][0]["properties"]["ART"]

        horoscope_data = data["features"][0]["properties"]["BEZEICHNUNG"]

    # Print the retrieved data
        print(f"Horoscope for date {date}: {horoscope_data}")
