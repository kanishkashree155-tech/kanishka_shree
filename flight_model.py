import sqlite3
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE_DIR, "database")
os.makedirs(DB_DIR, exist_ok=True)
DB_PATH = os.path.join(DB_DIR, "flight.db")
import sqlite3
def create_table():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS flight ( id INTEGER PRIMARY KEY AUTOINCREMENT, flight_number TEXT, departure_city TEXT, arrival_city TEXT, prediction REAL)""")
    conn.commit()
    cursor.execute("PRAGMA table_info(flight)")
    print(cursor.fetchall())
    conn.close()
def save_flight(flight_number, departure_city, arrival_city, prediction):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO flight (flight_number, departure_city, arrival_city, prediction)
        VALUES (?, ?, ?, ?)
    """, (flight_number, departure_city, arrival_city, prediction))
    conn.commit()
    conn.close()
def predict_delay(departure_city, arrival_city):
    if departure_city == arrival_city:
        return "No Delay"
    else:
        return "Delay possible"
def get_all_flights():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flight")
    data = cursor.fetchall()
    conn.close()
    return data
