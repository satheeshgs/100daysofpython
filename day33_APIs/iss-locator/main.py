import smtplib
import time

import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
latitude = os.getenv('LATITUDE')
longitude = os.getenv('LONGITUDE')
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

parameters = {
    'lat': latitude,
    'lng': longitude,
    'formatted': 0
}

def is_iss_overhead():
    #ISS location now
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    iss_data = response.json()
    iss_latitude = float(iss_data['iss_position']['latitude'])
    iss_longitude = float(iss_data['iss_position']['longitude'])
    #check relative positions within +-5 degrees of ISS
    if (abs(iss_latitude - float(latitude)) <= 5) and (abs(iss_longitude - float(longitude)) <= 5):
        return True

def is_night():
    #sunset times
    #response = requests.get(url=f'https://api.sunrise-sunset.org/json?lat={latitude}&lng={longitude}')
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters, )
    response.raise_for_status()
    sun_data = response.json()
    sunrise = int(sun_data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(sun_data['results']['sunset'].split("T")[1].split(":")[0])
    print(f'sunrise at {sunrise} and sunset at {sunset}')

    time_now = datetime.now().hour

    if time_now >= sunset and time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        #send email to myself via smtplib
        connection = smtplib.SMTP(host="", port=)
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs='satheesh.gowtham@gmail.com',
            msg="Subject: Look up \n\nThe ISS is above your sky"
        )