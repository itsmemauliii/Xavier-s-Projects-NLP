# scheduler.py
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
FROM_NUMBER = os.getenv("FROM_NUMBER")
TO_NUMBER = os.getenv("TO_NUMBER")

client = Client(TWILIO_SID, TWILIO_AUTH)

def send_reminder(msg):
    message = client.messages.create(
        from_=FROM_NUMBER,
        body=msg,
        to=TO_NUMBER
    )
    print("Sent:", message.sid)
