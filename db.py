import sqlite3

def init_db():
    conn = sqlite3.connect("reminders.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS reminders 
                 (id INTEGER PRIMARY KEY, number TEXT, intent TEXT, time TEXT)''')
    conn.commit()
    conn.close()

def add_reminder(number, intent, time):
    conn = sqlite3.connect("reminders.db")
    c = conn.cursor()
    c.execute("INSERT INTO reminders (number, intent, time) VALUES (?, ?, ?)", (number, intent, time))
    conn.commit()
    conn.close()

def get_due_reminders(current_time):
    conn = sqlite3.connect("reminders.db")
    c = conn.cursor()
    c.execute("SELECT * FROM reminders WHERE time=?", (current_time,))
    reminders = c.fetchall()
    conn.close()
    return reminders
