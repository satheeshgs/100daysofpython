from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv('ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')
from_number = os.getenv('FROM_NUM')
to_number = os.getenv('TO_NUM')

client = Client(account_sid, auth_token)

text_message = 'Hi, Testing Twillio message'

message = client.messages.create(
  from_=from_number,
  body=text_message,
  to=to_number
)

print(message.status)