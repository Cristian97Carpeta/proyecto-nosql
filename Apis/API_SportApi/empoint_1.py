import requests
import json

url = "https://sportapi7.p.rapidapi.com/api/v1/sport/football/scheduled-events/2022-02-11"

headers = {
    "x-rapidapi-key": "6671df0abcmshd2fdd7437cff733p17cf53jsn9678db55def6",
    "x-rapidapi-host": "sportapi7.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
data = response.json()

# Guardar el resultado en un archivo JSON
with open('scheduled_events.json', 'w') as archivo_json:
    json.dump(data, archivo_json, indent=4)

print("Datos de los eventos programados guardados en scheduled_events.json")
