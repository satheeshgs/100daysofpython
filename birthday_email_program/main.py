##################### Hard Starting Project ######################
import datetime
import smtplib
import os
import pandas as pd
import random
from dotenv import load_dotenv

load_dotenv()

my_email = os.getenv('EMAIL')
my_password = os.getenv('PASSWORD')

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 
now = datetime.datetime.now()
today_day = now.day
today_month = now.month
today_tuple = (today_month, today_day)

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
data_file = pd.read_csv('birthdays.csv')
birthdays_dict = {
    (data_row.month, data_row.day): data_row for (index, data_row) in data_file.iterrows()
}

#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
if today_tuple in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person = birthdays_dict[today_tuple]
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )