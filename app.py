from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from nlp import extract_intent_and_time
from db import init_db, add_reminder
from scheduler import start_scheduler

app = Flask(__name__)
init_db()
start_scheduler()

@app.route("/bot", methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '')
    sender = request.values.get('From', '').replace("whatsapp:", "")

    intent, time = extract_intent_and_time(incoming_msg)

    resp = MessagingResponse()
    msg = resp.message()

    if intent and time:
        add_reminder(sender, intent, time)
        msg.body(f"Got it! Reminder set for *{intent}* at *{time}*.")
    else:
        msg.body("Sorry, I didn't understand. Try: *Remind me to drink water at 17:30*")

    return str(resp)
