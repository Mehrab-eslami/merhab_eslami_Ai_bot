import sqlite3

conn = sqlite3.connect("database.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    sender TEXT,
    message TEXT
)''')
conn.commit()

def save_message(user_id, sender, message):
    cursor.execute("INSERT INTO messages (user_id, sender, message) VALUES (?, ?, ?)", (user_id, sender, message))
    conn.commit()

def get_all_messages():
    cursor.execute("SELECT * FROM messages ORDER BY id DESC")
    return cursor.fetchall()