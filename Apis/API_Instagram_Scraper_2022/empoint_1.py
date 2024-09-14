import requests
import json


#EMPOINT 1

#url = "https://instagram-scraper-2022.p.rapidapi.com/ig/reels_posts/"

querystring = {"id_user": "25025320"}

headers = {
    "x-rapidapi-key": "6671df0abcmshd2fdd7437cff733p17cf53jsn9678db55def6",
    "x-rapidapi-host": "instagram-scraper-2022.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

# Guardar el resultado en un archivo JSON
with open('reels_posts.json', 'w') as archivo_json:
    json.dump(data, archivo_json, indent=4)

print("Datos de los reels guardados en reels_posts.json")
