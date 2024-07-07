import requests

response = requests.get(url='http://api.open-notify.org/iss-now.json')
data = response.json()
print(data)


response = requests.get(url='https://api.sunrise-sunset.org/json')
