import pandas as pd
data = pd.read_csv("2018_Central_Park_squirrel_data.csv")
#print(data.columns)

data_new = data.groupby("Primary Fur Color").size()
data_new.to_csv("squirrel_data_grouped.csv")