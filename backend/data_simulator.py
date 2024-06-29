import time
import random
import sqlite3

DB_NAME = "battery_data.db"
SIMULATION_DURATION = 120  # Duration in seconds

def generate_battery_data():
    battery_data = {
        "temperature": round(random.uniform(20.0, 40.0), 2),
        "voltage": round(random.uniform(3.0, 4.2), 2),
        "current": round(random.uniform(0.0, 5.0), 2),
        "timestamp": time.time()
    }
    return battery_data

def store_battery_data(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS BatteryData (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        temperature REAL,
        voltage REAL,
        current REAL,
        timestamp REAL
    )
    """)
    
    cursor.execute("""
    INSERT INTO BatteryData (temperature, voltage, current, timestamp) 
    VALUES (?, ?, ?, ?)
    """, (data['temperature'], data['voltage'], data['current'], data['timestamp']))
    
    conn.commit()
    conn.close()
    print("Data stored in the database:", data)

def main():
    start_time = time.time()
    while True:
        battery_data = generate_battery_data()
        store_battery_data(battery_data)
        time.sleep(1)  # Adjust the interval as needed
        
        elapsed_time = time.time() - start_time
        if elapsed_time > SIMULATION_DURATION:
            print("Simulation completed after 120 seconds.")
            break

if __name__ == "__main__":
    main()
