import requests
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

#Create a user in pixela
pixela_endpoint = os.getenv('PIXELA_ENDPOINT')
token = os.getenv('TOKEN')
username = os.getenv('USERNAME')

user_creation_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_creation_params)
# print(response.text)

#Create a graph
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_headers = {
    "X-USER-TOKEN": token
}

graph_params = {
    "id": "graph1",
    "name": "Coding graph",
    "unit": "minutes",
    "type": "int",
    "color": "ajisai"
}

# response = requests.post(url=graph_endpoint,json=graph_params, headers=graph_headers)
# print(response.text)

#post a pixel on a graph
graph_id = "graph1"
pixel_post_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}"

now = datetime.datetime.now()
date_now = now.strftime("%Y%m%d")
print(date_now)

pixel_params = {
    "date": date_now,
    "quantity": "20",
}

response = requests.post(url=pixel_post_endpoint, json=pixel_params, headers=graph_headers)
print(response.text)


#update request
update_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{date_now}"
update_params = {
    "quantity": "20"
}

# response = requests.put(url=update_endpoint, json=update_params, headers=graph_headers)
# print(response.text)

#delete request
# delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{date_now}"

# response = requests.delete(url=delete_endpoint, headers=graph_headers)
# print(response.text)