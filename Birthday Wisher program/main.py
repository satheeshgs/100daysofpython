import datetime as dt
import random
import smtplib
import pandas as pd
import os
from dotenv import load_dotenv

now = dt.datetime.now()
day_of_week = now.weekday()

load_dotenv()

my_email = os.getenv('EMAIL')
my_password = os.getenv('PASSWORD')

def random_quote():
    with open(file="quotes.txt") as file:
        df = pd.read_table(file, delimiter="\t", header=None)
        random_number = random.randint(0, len(df)-1)
        return df[0][random_number]


weeks_days = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"

}

quote_of_the_day = random_quote()
print(day_of_week)

if day_of_week == 5:
    print("yes")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="satheesh.gowtham@gmail.com",
            msg=f"Subject:Quote of the Week \n\n{quote_of_the_day}"
        )


