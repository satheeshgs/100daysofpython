import requests
from dotenv import load_dotenv
import os

load_dotenv()

APP_ID = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")
NUTRITIONIX_BASE_ENDPOINT = os.getenv("NUTRITIONIX_HOST")
NLP_ENDPOINT = os.getenv("NLP_ENDPOINT")
GENDER = os.getenv("GENDER")
WEIGHT_KG = os.getenv("WEIGHT_KG")
HEIGHT_CM = os.getenv("HEIGHT_CM")
AGE = os.getenv("AGE")

host_domain = NUTRITIONIX_BASE_ENDPOINT + NLP_ENDPOINT

headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-api-key': API_KEY
}

query = input("Enter the exercises that you did: \n")

parameters = {
    'query': query,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}

response = requests.post(url=host_domain, json=parameters, headers=headers)
response.raise_for_status()
print(response.text)
