import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

ENDPOINT = "get-linkedin-profile"
API = "fresh-linkedin-profile-data.p.rapidapi.com"

URL_API = f"https://{API}/{ENDPOINT}"

url = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-linkedin-profile"

querystring = {"linkedin_url":"https://www.linkedin.com/in/cjfollini/","include_skills":"false"}

headers = {
	"x-rapidapi-key": os.getenv("API_KEY"),
	"x-rapidapi-host": API
}

def call_api(linkedin_url, include_sills):
	params = {"linkedin_url":linkedin_url,"include_skills": include_sills}
	response = requests.get(URL_API, headers=headers, params=params)

	r = json.dumps(response.json(),indent=4)
	with open("flpdprc", "w")
	print(response.json())---------------------------------------
call_api("https://www.linkedin.com/in/cjfollini/","false")

