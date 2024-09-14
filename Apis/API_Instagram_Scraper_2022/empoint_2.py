#EMPOINT 2

import requests
import json

url = "https://instagram-scraper-2022.p.rapidapi.com/ig/info/"

querystring = {"id_user": "48318169414"}

headers = {
    "x-rapidapi-key": "6671df0abcmshd2fdd7437cff733p17cf53jsn9678db55def6",
    "x-rapidapi-host": "instagram-scraper-2022.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

# Guardar el resultado en un archivo JSON
with open('user_info.json', 'w') as archivo_json:
    json.dump(data, archivo_json, indent=4)

print("Datos del usuario guardados en user_info.json")
