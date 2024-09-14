import requests
import json

url = "https://sportapi7.p.rapidapi.com/api/v1/sport/football/2024-03-25/0/categories"

headers = {
    "x-rapidapi-key": "6671df0abcmshd2fdd7437cff733p17cf53jsn9678db55def6",
    "x-rapidapi-host": "sportapi7.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
data = response.json()

# Guardar el resultado en un archivo JSON
with open('categories.json', 'w') as archivo_json:
    json.dump(data, archivo_json, indent=4)

print("Datos de las categorías guardados en categories.json")
