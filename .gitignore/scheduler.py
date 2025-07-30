import os
from twilio.rest import Client

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH = os.getenv("TWILIO_AUTH")
FROM_NUMBER = os.getenv("FROM_NUMBER")

client = Client(TWILIO_SID, TWILIO_AUTH)
