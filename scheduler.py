import threading
import time
from datetime import datetime
from db import get_due_reminders
from twilio.rest import Client

# Set these with your Twilio credentials
TWILIO_SID = "YOUR_SID"
TWILIO_AUTH = "YOUR_AUTH"
FROM_NUMBER = "whatsapp:+14155238886"

client = Client(TWILIO_SID, TWILIO_AUTH)

def send_reminder(number, text):
    client.messages.create(
        body=f"⏰ Reminder: {text}",
        from_=FROM_NUMBER,
        to=f"whatsapp:{number}"
    )

def background_task():
    while True:
        now = datetime.now().strftime('%H:%M')
        reminders = get_due_reminders(now)
        for r in reminders:
            send_reminder(r[1], r[2])
        time.sleep(60)

def start_scheduler():
    thread = threading.Thread(target=background_task)
    thread.daemon = True
    thread.start()
