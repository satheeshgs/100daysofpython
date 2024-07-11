import requests
import os
from dotenv import load_dotenv

load_dotenv()
latitude = os.getenv('LATITUDE')
longitude = os.getenv('LONGITUDE')
api_key = os.getenv('API_KEY')

parameters = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()

print(response.json())