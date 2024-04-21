#with open("weather_data.csv") as data:
#    weather_data = data.readlines()

#print(weather_data)

"""
import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    headers = next(data) #skipping headers
    temperatures = []
    for row in data:
        temperatures.append(int(row[1]))
    
    print(temperatures)

import pandas as pd
data = pd.read_csv("weather_data.csv")
data_dict = data.to_dict()

#max value of temperatures
max_temp = data["temp"].max()
mean_temp = data["temp"].mean()

max_day = data[data.temp == data.temp.max()]

print(max_day.day)
"""


