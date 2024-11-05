from pprint import pprint
import os
import requests
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth

load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):

        self.endpoint = os.getenv('SHEETY_ENDPOINT')
        self._user = os.getenv('SHEETY_USERNAME')
        self._password = os.getenv('SHEETY_PASSWORD')
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self.token = os.getenv('SHEETY_TOKEN')
        self.headers = {
            'Authorization': f'Basic {self.token}'
        }
        self.destination_data = {}



    def get_destination_data(self):

        response = requests.get(url=self.endpoint, headers=self.headers)
        # response = requests.get(url=self.endpoint, auth=self._authorization)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data



    def update_destination_codes(self):

        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f'{self.endpoint}/{city["id"]}',
                headers=self.headers,
                json=new_data
            )
            # can use auth=self._authorization instead of headers=self.headers
            print(response.text)
