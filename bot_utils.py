# bot_utils.py
import nltk
from nltk.tokenize import word_tokenize
from datetime import datetime

nltk.download("punkt")

def detect_intent(text):
    tokens = word_tokenize(text.lower())
    if "remind" in tokens or "reminder" in tokens:
        return "set_reminder"
    elif "hi" in tokens or "hello" in tokens:
        return "greeting"
    else:
        return "unknown"

def generate_reply(text):
    intent = detect_intent(text)
    if intent == "set_reminder":
        return "Okay, please tell me what and when to remind you!"
    elif intent == "greeting":
        return "Hey! I'm your personal WhatsApp reminder bot 🕰️"
    else:
        return "Sorry, I didn't get that. Can you rephrase?"
