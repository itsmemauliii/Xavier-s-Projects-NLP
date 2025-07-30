from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import nltk
from nltk.chat.util import Chat, reflections
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

pairs = [
    [r"hi|hello", ["Hey there!", "Hello!"]],
    [r"what is your name?", ["I'm your reminder bot"]],
    [r"set reminder (.*)", ["Reminder set for %1"]],
    [r"bye", ["Bye! Take care."]],
]

chatbot = Chat(pairs, reflections)

@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    reply = chatbot.respond(incoming_msg)
    if reply:
        resp.message(reply)
    else:
        resp.message("Sorry, I didn’t get that. Try saying 'set reminder 5pm call mom'.")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
