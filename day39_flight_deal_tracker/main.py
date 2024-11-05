#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
import os
import requests
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
import time


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

if sheet_data[0]["iataCode"] == "":

    print(f"Token: {flight_search._token}")
    for row in sheet_data:
        if row["iataCode"] == "":
            row["iataCode"] = flight_search.get_destination_code(row["city"])
            time.sleep(2)
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()


