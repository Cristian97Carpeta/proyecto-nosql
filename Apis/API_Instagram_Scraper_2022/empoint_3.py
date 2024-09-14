import requests
import json

url = "https://instagram-scraper-2022.p.rapidapi.com/ig/web_profile_info/"

querystring = {"user": "sanembahcekapili"}

headers = {
    "x-rapidapi-key": "6671df0abcmshd2fdd7437cff733p17cf53jsn9678db55def6",
    "x-rapidapi-host": "instagram-scraper-2022.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

# Guardar el resultado en un archivo JSON
with open('web_profile_info.json', 'w') as archivo_json:
    json.dump(data, archivo_json, indent=4)

print("Datos del perfil web guardados en web_profile_info.json")
