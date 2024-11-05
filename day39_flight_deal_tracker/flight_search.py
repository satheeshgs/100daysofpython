from dotenv import load_dotenv
import os, requests
load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):

        self._api_key = os.getenv('API_KEY_AMADEUS')
        self._api_secret = os.getenv('API_SECRET_AMADEUS')
        self.token_url = os.getenv('AMADEUS_TOKEN_URL')
        self._token = self._get_new_token()


    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }

        response = requests.post(url=self.token_url, headers=header, data=body)
        response.raise_for_status()

        return response.json()['access_token']


    def get_destination_code(self, city_name):
        
        city_search_endpoint = os.getenv('IATA_ENDPOINT')
        headers = {"Authorization": f"Bearer {self._token}"}

        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }

        response = requests.get(url=city_search_endpoint, params=query, headers=headers)
        try:
            code = response.json()['data'][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"
        return code
