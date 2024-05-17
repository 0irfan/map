from flask import jsonify
import sqlite3
import os

# Use __file__ to get the absolute path of the current script file
DATABASE_PATH = os.path.join(os.path.dirname(__file__), 'podio.db')

def init_database():
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS podio_items
                 (id INTEGER PRIMARY KEY,
                  external_id TEXT,
                   latitude REAL,
                  longitude REAL,
                  title TEXT,
                  url TEXT)''')
    conn.commit()
    conn.close()

def add_item(external_id, latitude, longitude, title, url):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO podio_items (external_id, latitude, longitude, title, url) VALUES (?, ?, ?, ?, ?)",
              (external_id, latitude, longitude, title, url))
    conn.commit()
    conn.close()

def get_items():
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("SELECT id, latitude, longitude, title FROM podio_items")
    items = c.fetchall()
    conn.close()
    
    # Convert the items to a list of dictionaries
    items_dict = []
    for item in items:
        items_dict.append({
            "external_id": item[0],
            "latitude": item[1],
            "longitude": item[2],
            "title": item[3],
            
        })
    
    return items_dict

# Call init_database() to create the table if it doesn't exist
