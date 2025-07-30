import nltk
import json
import datetime
import re
from apscheduler.schedulers.background import BackgroundScheduler

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

reminders = []

# Simplistic NLP parser using regex and NLTK
def extract_reminder(text):
    time_patterns = [
        r'at (\d{1,2} ?(?:am|pm|AM|PM))',
        r'(\d{1,2}:\d{2} ?(?:am|pm|AM|PM))',
        r'at (\d{1,2})'
    ]
    date = datetime.datetime.now().strftime("%Y-%m-%d")  # default: today

    task = text
    time_str = None
    for pattern in time_patterns:
        match = re.search(pattern, text)
        if match:
            time_str = match.group(1)
            task = text.replace(match.group(0), '')  # remove time part
            break

    if not time_str:
        return None, None

    try:
        full_time = datetime.datetime.strptime(time_str.strip(), "%I %p").time()
    except:
        try:
            full_time = datetime.datetime.strptime(time_str.strip(), "%I:%M %p").time()
        except:
            return None, None

    return task.strip(), full_time


def add_reminder(text, sender):
    task, time = extract_reminder(text)
    if task and time:
        reminder_time = datetime.datetime.combine(datetime.date.today(), time)
        reminders.append({"task": task, "time": reminder_time, "sender": sender})
        return f"Got it! I’ll remind you to **{task}** at **{time.strftime('%I:%M %p')}**"
    return "Sorry, I couldn’t understand the time. Try saying something like ‘Remind me to study at 4 PM’."


# Send reminders (dummy print for now, integrate Twilio later)
def check_reminders():
    now = datetime.datetime.now()
    for r in reminders[:]:
        if now >= r["time"]:
            print(f"Reminder for {r['sender']}: {r['task']}")
            # Here you’d call send_whatsapp_message()
            reminders.remove(r)

scheduler = BackgroundScheduler()
scheduler.add_job(check_reminders, 'interval', seconds=60)
scheduler.start()
