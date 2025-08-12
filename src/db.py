import sqlite3

def get_connection():
    conn = sqlite3.connect("youtube-videos.db")

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
            )
    ''')
    
    return conn, cursor